"""Quick-start example for the Mokhles Group HR Analytics dataset."""

from pathlib import Path
import sys

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "src"))

from mokhles_hr_analytics import load_csv_table  # noqa: E402


def main() -> None:
    employees = load_csv_table("01_Employee_Master_FY2025.csv")

    print("Rows:", len(employees))
    print("\nHeadcount by department:")
    print(employees["Department"].value_counts())

    print("\nAverage monthly gross by job level:")
    print(
        employees.groupby("Job Level")["Monthly Gross"]
        .mean()
        .sort_values(ascending=False)
        .round(2)
    )


if __name__ == "__main__":
    main()
