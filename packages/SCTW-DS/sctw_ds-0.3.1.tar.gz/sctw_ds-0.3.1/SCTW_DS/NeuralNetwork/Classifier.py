import os
import pickle
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import set_start_method, shared_memory
from typing import List

import numpy as np

from ..Utils.progress_bar import ProgressBar
from .Layer import Layer

# from numba import jit


global_layers: List[Layer] = []
global_weights = []
global_biases = []

set_start_method("fork")


def initialize_shared_memory(layers):
    global global_layers, global_weights, global_biases
    global_layers = layers
    global_weights = []
    global_biases = []

    for layer in layers:
        weight_shm = shared_memory.SharedMemory(create=True, size=layer.weights.nbytes)
        bias_shm = shared_memory.SharedMemory(create=True, size=layer.biases.nbytes)
        global_weights.append(weight_shm)
        global_biases.append(bias_shm)
        np.copyto(
            np.ndarray(
                layer.weights.shape, dtype=layer.weights.dtype, buffer=weight_shm.buf
            ),
            layer.weights,
        )
        np.copyto(
            np.ndarray(
                layer.biases.shape, dtype=layer.biases.dtype, buffer=bias_shm.buf
            ),
            layer.biases,
        )


def cleanup_shared_memory():
    global global_weights, global_biases, global_layers
    for shm in global_weights:
        shm.close()
        shm.unlink()
    for shm in global_biases:
        shm.close()
        shm.unlink()

    global_weights = []
    global_biases = []
    global_layers = []


# @jit(nopython=True, parallel=True)
def _update_batch(batch: np.ndarray):
    global global_layers, global_weights, global_biases

    nabla_w = [np.zeros(layer.weights.shape) for layer in global_layers]
    nabla_b = [np.zeros(layer.biases.shape) for layer in global_layers]

    for data_point in batch:
        # Forward pass
        activation = data_point[0]
        activations = [activation]
        zs = []

        for i, layer in enumerate(global_layers):
            weights = np.ndarray(
                layer.weights.shape,
                dtype=layer.weights.dtype,
                buffer=global_weights[i].buf,
            )
            biases = np.ndarray(
                layer.biases.shape,
                dtype=layer.biases.dtype,
                buffer=global_biases[i].buf,
            )

            z = np.dot(activation, weights) + biases
            zs.append(z)
            activation = layer._activationFunction(z)
            activations.append(activation)

        # Backward pass
        delta = (activations[-1] - np.array(data_point[1])) * global_layers[
            -1
        ]._activationFunctionDerivative(zs[-1])
        nabla_b[-1] += delta.astype(float)
        nabla_w[-1] += np.outer(activations[-2], delta).astype(float)

        for layer_idx in range(2, len(global_layers) + 1):
            z = zs[-layer_idx]
            sp = global_layers[-layer_idx]._activationFunctionDerivative(z)
            weights_next = np.ndarray(
                global_layers[-layer_idx + 1].weights.shape,
                dtype=global_layers[-layer_idx + 1].weights.dtype,
                buffer=global_weights[-layer_idx + 1].buf,
            )
            delta = np.dot(delta, weights_next.T) * sp
            nabla_b[-layer_idx] += delta
            nabla_w[-layer_idx] += np.outer(activations[-layer_idx - 1], delta)

    return nabla_w, nabla_b


class NeuralNetwork:
    def __init__(self, layers: List[Layer]) -> None:
        self.layers = layers
        self.velocity_w = [np.zeros_like(layer.weights) for layer in layers]
        self.velocity_b = [np.zeros_like(layer.biases) for layer in layers]

        initialize_shared_memory(layers)

    def calculateOutputs(self, inputs: np.ndarray) -> np.ndarray:
        for layer in self.layers:
            inputs = layer.calculateOutputs(inputs)
        return inputs

    def _classify(self, inputs: np.ndarray) -> np.intp:
        outputs = self.calculateOutputs(inputs)
        return np.argmax(outputs)

    def classify(self, inputs: np.ndarray) -> List[np.intp]:
        preds: List[np.intp] = []
        for point in inputs:
            pred = self._classify(point[0])
            preds.append(pred)
        return preds

    def _cost(self, data_point: np.ndarray) -> float:
        outputs = self.calculateOutputs(np.array(data_point[0]))
        output_layer = self.layers[-1]
        cost = 0.0
        for out_node in range(len(outputs)):
            cost += output_layer.nodeCost(outputs[out_node], data_point[1][out_node])
        return cost

    def cost(self, data_points: np.ndarray) -> float:
        total_cost = 0.0
        for data_point in data_points:
            total_cost += self._cost(data_point)
        return total_cost / len(data_points)

    def learn(
        self,
        training_data: np.ndarray,
        learning_rate: float,
        batch_size: int,
        momentum: float,
    ) -> float:
        batches = [
            training_data[k : k + batch_size]
            for k in range(0, len(training_data), batch_size)
        ]

        initialize_shared_memory(self.layers)
        with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
            future_to_batch = {
                executor.submit(_update_batch, batch): batch for batch in batches
            }

            nabla_w_total = [np.zeros_like(layer.weights) for layer in self.layers]
            nabla_b_total = [np.zeros_like(layer.biases) for layer in self.layers]

            for future in as_completed(future_to_batch):
                nabla_w, nabla_b = future.result()
                for i in range(len(self.layers)):
                    nabla_w_total[i] += nabla_w[i]
                    nabla_b_total[i] += nabla_b[i]

        global global_layers
        for i, layer in enumerate(self.layers):
            self.velocity_w[i] = (
                momentum * self.velocity_w[i]
                - (learning_rate / batch_size) * nabla_w_total[i]
            )
            self.velocity_b[i] = (
                momentum * self.velocity_b[i]
                - (learning_rate / batch_size) * nabla_b_total[i]
            )
            # Correctly update shared memory
            layer.weights += self.velocity_w[i]
            layer.biases += self.velocity_b[i]

        cleanup_shared_memory()

        return self.cost(training_data)

    def train(
        self,
        iterations: int,
        data_points: np.ndarray,
        learning_rate: float,
        batch_size: int,
        momentum: float = 0.9,
        decay: float = 1e-7,
    ) -> List[float]:
        costs: List[float] = []
        progress = ProgressBar(total=iterations, program_name="training.")
        for i in range(iterations):
            cost = self.learn(data_points, learning_rate, batch_size, momentum)
            progress.increment(cost=cost)
            costs.append(cost)

        global global_weights, global_layers, global_biases
        del global_layers
        del global_weights
        del global_biases

        return costs

    def save_model(self, file_path: str):
        with open(file_path, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def load_model(cls, file_path: str) -> "NeuralNetwork":
        with open(file_path, "rb") as file:
            return pickle.load(file)
