hello_tabulate.py

import argparse
from tabulate import tabulate


def main():
    parser = argparse.ArgumentParser(
        description="Display a personalized study summary."
    )
    parser.add_argument("--name", required=True, help="Your name")
    args = parser.parse_args()

    study_tasks = [
        ["Python practice", "Completed"],
        ["GitHub assignment", "In progress"],
        ["Open-source learning", "Planned"],
    ]

    print(f"\nHello, {args.name}!")
    print("Here is your study summary:\n")

    print(
        tabulate(
            study_tasks,
            headers=["Activity", "Status"],
            tablefmt="grid"
        )
    )


if __name__ == "__main__":
    main()
