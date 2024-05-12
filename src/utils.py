from pathlib import Path

import polars as pl
from sklearn.metrics import root_mean_squared_error, r2_score, mean_absolute_error

RAW_DATA_DIR = Path("..", "data", "parquet")
PROCESSED_DATA_DIR = Path("..", "data", "processed")

PROCESSED_DATA_DIR.joinpath('training').mkdir(exist_ok = True)
PROCESSED_DATA_DIR.joinpath('test').mkdir(exist_ok = True)

VALIDATION_CUTOFF = pl.date(2018, 11, 30)

def print_metrics(y_true: pl.Series, y_pred: pl.Series, label = ""):
    if len(label) > 0:
        print(label)

    rmse = root_mean_squared_error(y_true, y_pred)
    print(f"RMSE: {rmse:.4f}")

    mae = mean_absolute_error(y_true, y_pred)
    print(f"MAE: {mae:.4f}")

    r2 = r2_score(y_true, y_pred)
    print(f"R2: {r2:.3%}")

    max_error = (y_true - y_pred).abs().max()
    print(f"Max error: {max_error:.4f}")

    print()