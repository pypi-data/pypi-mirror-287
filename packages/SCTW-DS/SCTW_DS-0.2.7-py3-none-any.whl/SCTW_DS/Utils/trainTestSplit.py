from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple

import pandas as pd

from .DataPoint import DataPoint
from .progress_bar import ProgressBar


def process_chunk(df_chunk: pd.DataFrame, cols: pd.Index) -> List[DataPoint]:
    data_points = []
    for _, row in df_chunk.iterrows():
        inputs = [row[cols[j]] for j in range(len(cols) - 1)]
        output = row[cols[-1]]
        expected_outputs = [0.0] * (int(row[cols[-1]].max()) + 1)
        expected_outputs[int(output)] = 1.0
        data_points.append(DataPoint(inputs, expected_outputs))
    return data_points


def trainTestSplit(
    df: pd.DataFrame, ratio: float = 0.8, num_threads: int = 4
) -> Tuple[List[DataPoint], List[DataPoint]]:
    data_points = []
    cols = df.columns
    p = ProgressBar(total=len(df), program_name="PAIN")

    chunk_size = len(df) // num_threads
    chunks = [df.iloc[i : i + chunk_size] for i in range(0, len(df), chunk_size)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_chunk = {
            executor.submit(process_chunk, chunk, cols): chunk for chunk in chunks
        }

        for future in as_completed(future_to_chunk):
            data_points.extend(future.result())
            p.increment(len(future.result()))

    train_data = data_points[: int(ratio * len(data_points))]
    test_data = data_points[int(ratio * len(data_points)) :]

    return train_data, test_data
