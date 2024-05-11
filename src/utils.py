from pathlib import Path

RAW_DATA_DIR = Path("..", "data", "parquet")
PROCESSED_DATA_DIR = Path("..", "data", "processed")

PROCESSED_DATA_DIR.joinpath('training').mkdir(exist_ok = True)
PROCESSED_DATA_DIR.joinpath('test').mkdir(exist_ok = True)