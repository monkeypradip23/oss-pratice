
import argparse
from tabulate import tabulate

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    args = parser.parse_args()

    activities = [
        ["Python learning", "Completed"],
        ["GitHub practice", "In progress"],
        ["Open source", "Planned"]
    ]

    print(f"\nHello, {args.name}!")
    print(tabulate(
        activities,
        headers=["Activity", "Status"],
        tablefmt="grid"
    ))

if __name__ == "__main__":
    main()
