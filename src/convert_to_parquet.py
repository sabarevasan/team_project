import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


def convertCSVToParquet(filepath, out="../data/processed/data.parquet"):
    df = pd.read_csv(filepath)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, out)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser("convert_to_parquet")

    parser.add_argument("csv", help="input csv file.", type=str)
    parser.add_argument("out", help="output path.", type=str)
    args = parser.parse_args()

    print(args.csv)
    print(args.out)
