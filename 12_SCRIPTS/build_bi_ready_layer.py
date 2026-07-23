"""Build cross-platform BI-ready CSV tables from the authoritative HR data."""

from __future__ import annotations

import csv
import re
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "csv"
OUTPUT = ROOT / "data" / "bi_ready_csv"
MAPPING = ROOT / "bi_assets" / "semantic_model" / "field_name_mapping.csv"

TABLES = {
    "02_Monthly_HR_KPI_FY2025.csv": "02_fact_monthly_hr_kpi_fy2025.csv",
    "03_Department_Annual_Summary_FY2025.csv": "03_fact_department_annual_summary_fy2025.csv",
    "04_Quarterly_Board_KPI_FY2025.csv": "04_fact_quarterly_board_kpi_fy2025.csv",
    "05_Recruitment_Master_FY2025.csv": "05_fact_recruitment_fy2025.csv",
    "06_Employee_Separations_FY2025.csv": "06_fact_employee_separations_fy2025.csv",
    "07_Leave_Transactions_FY2025.csv": "07_fact_leave_transactions_fy2025.csv",
    "08_Diversity_Inclusion_Master_FY2025.csv": "08_dim_diversity_inclusion_fy2025.csv",
    "09_Training_Development_Master_FY2025.csv": "09_fact_training_development_fy2025.csv",
    "10_Compensation_Benefits_Master_FY2025.csv": "10_fact_compensation_benefits_fy2025.csv",
    "11_Performance_Evaluation_Master_FY2025.csv": "11_fact_performance_evaluation_fy2025.csv",
    "12_Health_Safety_Master_FY2025.csv": "12_fact_health_safety_fy2025.csv",
}


def normalise(name: str) -> str:
    value = name.strip().lower().replace("%", " percent ").replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_") or "field"
    return f"field_{value}" if value[0].isdigit() else value


def read_table(filename: str) -> tuple[list[str], list[dict[str, str]]]:
    path = SOURCE / filename
    if not path.exists():
        raise FileNotFoundError(f"Required source table not found: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def write_table(path: Path, headers: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, extrasaction="ignore")
        writer.writeheader()
        writer.writerows({h: row.get(h, "") for h in headers} for row in rows)


def parse_date(value: str) -> date | None:
    try:
        return datetime.fromisoformat((value or "").strip()).date()
    except ValueError:
        return None


def build() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    mapping_rows: list[dict[str, str]] = []
    all_source: dict[str, tuple[list[str], list[dict[str, str]]]] = {}

    for path in SOURCE.glob("*.csv"):
        if path.name.startswith("13_"):
            continue
        all_source[path.name] = read_table(path.name)

    _, employees = read_table("01_Employee_Master_FY2025.csv")
    _, separations = read_table("06_Employee_Separations_FY2025.csv")

    department_to_cost = {row["Department"]: row["Cost Center"] for row in employees}
    departments = [
        {"department_key": normalise(dept), "department": dept, "cost_center": cost}
        for dept, cost in sorted(department_to_cost.items())
    ]
    write_table(
        OUTPUT / "00_dim_department.csv",
        ["department_key", "department", "cost_center"],
        departments,
    )

    locations = sorted(
        {
            row["Location"]
            for _, rows in all_source.values()
            for row in rows
            if row.get("Location")
        }
    )
    write_table(
        OUTPUT / "00_dim_location.csv",
        ["location_key", "location"],
        [{"location_key": normalise(location), "location": location} for location in locations],
    )

    unified: dict[str, dict[str, object]] = {}
    for row in employees:
        unified[row["Employee ID"]] = {
            "employee_id": row["Employee ID"],
            "employee_name": row["Employee Name"],
            "gender": row["Gender"],
            "age": row["Age"],
            "age_band": row["Age Band"],
            "division_of_origin": row["Division of Origin"],
            "disability_status": row["Disability Status"],
            "education": row["Education"],
            "department": row["Department"],
            "department_key": normalise(row["Department"]),
            "cost_center": row["Cost Center"],
            "job_title": row["Job Title"],
            "job_level": row["Job Level"],
            "employment_type": row["Employment Type"],
            "location": row["Location"],
            "location_key": normalise(row["Location"]),
            "join_date": row["Join Date"],
            "exit_date": "",
            "employment_status": "Active at FY2025 year-end",
            "manager": row["Manager"],
            "monthly_gross_bdt": row["Monthly Gross"],
        }

    for row in separations:
        unified[row["Employee ID"]] = {
            "employee_id": row["Employee ID"],
            "employee_name": row["Employee Name"],
            "gender": row["Gender"],
            "age": "",
            "age_band": "",
            "division_of_origin": "",
            "disability_status": "",
            "education": "",
            "department": row["Department"],
            "department_key": normalise(row["Department"]),
            "cost_center": department_to_cost.get(row["Department"], ""),
            "job_title": row["Job Title"],
            "job_level": row["Job Level"],
            "employment_type": "",
            "location": row["Location"],
            "location_key": normalise(row["Location"]),
            "join_date": row["Join Date"],
            "exit_date": row["Exit Date"],
            "employment_status": "Separated during FY2025",
            "manager": row["Manager"],
            "monthly_gross_bdt": "",
        }

    employee_fields = list(next(iter(unified.values())).keys())
    write_table(
        OUTPUT / "01_dim_employee_fy2025.csv",
        employee_fields,
        [unified[key] for key in sorted(unified)],
    )

    dates: list[date] = []
    for headers, rows in all_source.values():
        for header in headers:
            if "Date" in header or header == "Month":
                dates.extend(
                    parsed
                    for row in rows
                    if (parsed := parse_date(row.get(header, "")))
                )

    current, end = min(dates), max(dates)
    calendar: list[dict[str, object]] = []
    while current <= end:
        quarter = (current.month - 1) // 3 + 1
        calendar.append(
            {
                "date_key": int(current.strftime("%Y%m%d")),
                "date": current.isoformat(),
                "year": current.year,
                "quarter": f"Q{quarter}",
                "year_quarter": f"{current.year}-Q{quarter}",
                "month_number": current.month,
                "month_name": current.strftime("%B"),
                "month_short": current.strftime("%b"),
                "year_month": current.strftime("%Y-%m"),
                "month_start": current.replace(day=1).isoformat(),
                "week_of_year": int(current.strftime("%W")) + 1,
                "day_of_month": current.day,
                "day_name": current.strftime("%A"),
                "is_weekend": "Yes" if current.weekday() >= 5 else "No",
            }
        )
        current += timedelta(days=1)

    write_table(OUTPUT / "00_dim_date.csv", list(calendar[0].keys()), calendar)

    for source_name, output_name in TABLES.items():
        headers, rows = read_table(source_name)
        output_headers = [normalise(header) for header in headers]
        output_rows = [
            {normalise(header): row.get(header, "") for header in headers}
            for row in rows
        ]
        write_table(OUTPUT / output_name, output_headers, output_rows)
        mapping_rows.extend(
            {
                "source_file": source_name,
                "bi_ready_file": output_name,
                "original_field": original,
                "bi_ready_field": renamed,
            }
            for original, renamed in zip(headers, output_headers)
        )

    write_table(
        MAPPING,
        ["source_file", "bi_ready_file", "original_field", "bi_ready_field"],
        mapping_rows,
    )

    generated = sorted(OUTPUT.glob("*.csv"))
    if len(generated) != 15:
        raise RuntimeError(f"Expected 15 BI-ready CSV files, found {len(generated)}.")

    print(f"BI-ready layer created: {len(generated)} CSV files")
    print(f"Output directory: {OUTPUT}")


if __name__ == "__main__":
    build()
