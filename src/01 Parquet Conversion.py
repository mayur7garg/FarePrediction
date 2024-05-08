from pathlib import Path
import polars as pl

# Convert all files to parquet to reduce file size for git

for raw_path in Path("..", "data", "raw").glob("**/*.csv"):
    df = pl.read_csv(raw_path)
    output_file_path = Path("..", "data", "parquet", raw_path.parent.name, f"{raw_path.stem}.parquet")
    output_file_path.parent.mkdir(exist_ok = True)

    df.write_parquet(output_file_path)
    print(df.shape, output_file_path)