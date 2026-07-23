"""Rebuild consolidated analysis-ready HR tables."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
BI = ROOT / "02_CLEAN_DATA" / "bi_ready_csv"
OUTPUT = ROOT / "02_CLEAN_DATA" / "analysis_ready"


def read_dicts(name: str):
    with (BI / name).open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def write_dicts(name: str, headers, rows):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    with (OUTPUT / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, extrasaction="ignore")
        writer.writeheader()
        writer.writerows({h: row.get(h, "") for h in headers} for row in rows)


def number(value):
    try:
        return float(str(value or "").replace(",", "").replace("%", ""))
    except ValueError:
        return 0.0


def average(values):
    values = [v for v in values if v is not None]
    return round(sum(values) / len(values), 2) if values else ""


def build():
    _, employees = read_dicts("01_dim_employee_fy2025.csv")
    _, diversity_rows = read_dicts("08_dim_diversity_inclusion_fy2025.csv")
    _, compensation_rows = read_dicts("10_fact_compensation_benefits_fy2025.csv")
    _, performance_rows = read_dicts("11_fact_performance_evaluation_fy2025.csv")
    _, leave_rows = read_dicts("07_fact_leave_transactions_fy2025.csv")
    _, training_rows = read_dicts("09_fact_training_development_fy2025.csv")
    _, separation_rows = read_dicts("06_fact_employee_separations_fy2025.csv")
    _, department_rows = read_dicts("03_fact_department_annual_summary_fy2025.csv")

    diversity = {r["employee_id"]: r for r in diversity_rows}
    compensation = {r["employee_id"]: r for r in compensation_rows}
    performance = {r["employee_id"]: r for r in performance_rows}
    separation = {r["employee_id"]: r for r in separation_rows}

    leave_agg = defaultdict(lambda: {"transactions": 0, "approved_days": 0.0})
    for row in leave_rows:
        item = leave_agg[row["employee_id"]]
        item["transactions"] += 1
        if row.get("approval_status", "").lower() == "approved":
            item["approved_days"] += number(row.get("leave_days"))

    training_agg = defaultdict(
        lambda: {"programs": 0, "hours": 0.0, "cost": 0.0, "feedback": [], "pre": [], "post": []}
    )
    for row in training_rows:
        item = training_agg[row["employee_id"]]
        item["programs"] += 1
        item["hours"] += number(row.get("hours"))
        item["cost"] += number(row.get("cost_bdt"))
        for source, target in [
            ("feedback_rating", "feedback"),
            ("pre_assessment_score", "pre"),
            ("post_assessment_score", "post"),
        ]:
            value = str(row.get(source, "")).strip()
            if value:
                item[target].append(number(value))

    headers = [
        "employee_id", "employee_name", "employment_status", "gender", "age", "age_band",
        "division_of_origin", "disability_status", "education", "department",
        "department_key", "cost_center", "job_title", "job_level", "employment_type",
        "location", "location_key", "join_date", "exit_date", "manager",
        "monthly_gross_bdt", "annual_total_reward_bdt", "compa_ratio",
        "goal_completion_percent", "overall_performance_score", "performance_rating",
        "potential", "promotion_readiness", "leave_transactions", "approved_leave_days",
        "training_programs", "training_hours", "training_cost_bdt",
        "average_training_feedback", "average_pre_assessment",
        "average_post_assessment", "assessment_improvement", "exit_type",
        "exit_reason", "regrettable_exit", "tenure_at_exit_years",
    ]

    rows = []
    for emp in employees:
        employee_id = emp["employee_id"]
        div = diversity.get(employee_id, {})
        comp = compensation.get(employee_id, {})
        perf = performance.get(employee_id, {})
        sep = separation.get(employee_id, {})
        leave = leave_agg[employee_id]
        training = training_agg[employee_id]
        pre = average(training["pre"])
        post = average(training["post"])
        improvement = round(post - pre, 2) if pre != "" and post != "" else ""

        rows.append({
            "employee_id": employee_id,
            "employee_name": emp.get("employee_name"),
            "employment_status": emp.get("employment_status"),
            "gender": div.get("gender") or emp.get("gender"),
            "age": div.get("age") or emp.get("age"),
            "age_band": div.get("age_band") or emp.get("age_band"),
            "division_of_origin": div.get("division_of_origin") or emp.get("division_of_origin"),
            "disability_status": div.get("disability_status") or emp.get("disability_status"),
            "education": div.get("education") or emp.get("education"),
            "department": emp.get("department"),
            "department_key": emp.get("department_key"),
            "cost_center": emp.get("cost_center"),
            "job_title": emp.get("job_title"),
            "job_level": emp.get("job_level"),
            "employment_type": comp.get("employment_type") or emp.get("employment_type"),
            "location": emp.get("location"),
            "location_key": emp.get("location_key"),
            "join_date": emp.get("join_date"),
            "exit_date": emp.get("exit_date"),
            "manager": emp.get("manager"),
            "monthly_gross_bdt": comp.get("monthly_gross") or emp.get("monthly_gross_bdt"),
            "annual_total_reward_bdt": comp.get("annual_total_reward"),
            "compa_ratio": comp.get("compa_ratio"),
            "goal_completion_percent": perf.get("goal_completion_percent"),
            "overall_performance_score": perf.get("overall_score"),
            "performance_rating": perf.get("rating_label") or perf.get("performance_rating"),
            "potential": perf.get("potential"),
            "promotion_readiness": perf.get("promotion_readiness"),
            "leave_transactions": leave["transactions"],
            "approved_leave_days": round(leave["approved_days"], 2),
            "training_programs": training["programs"],
            "training_hours": round(training["hours"], 2),
            "training_cost_bdt": round(training["cost"], 2),
            "average_training_feedback": average(training["feedback"]),
            "average_pre_assessment": pre,
            "average_post_assessment": post,
            "assessment_improvement": improvement,
            "exit_type": sep.get("exit_type", ""),
            "exit_reason": sep.get("exit_reason", ""),
            "regrettable_exit": sep.get("regrettable_exit", ""),
            "tenure_at_exit_years": sep.get("tenure_at_exit_years", ""),
        })

    write_dicts("employee_360_fy2025.csv", headers, rows)
    print(f"Created employee_360_fy2025.csv with {len(rows)} rows.")


if __name__ == "__main__":
    build()
