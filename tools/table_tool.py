
import argparse
import pandas as pd
from rich.console import Console
from rich.table import Table


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file")
    args = parser.parse_args()

    df = pd.read_csv(args.csv_file)

    # Keep servers with at least 32 GB of memory
    filtered_df = df[df["memory_gb"] >= 32]

    console = Console()
    table = Table(title="High-Memory Servers")

    for column in filtered_df.columns:
        table.add_column(str(column))

    for _, row in filtered_df.iterrows():
        table.add_row(*[str(value) for value in row])

    console.print(table)

    output_file = "data/filtered_servers.csv"
    filtered_df.to_csv(output_file, index=False)
    print(f"Saved {output_file}")


if __name__ == "__main__":
    main()

