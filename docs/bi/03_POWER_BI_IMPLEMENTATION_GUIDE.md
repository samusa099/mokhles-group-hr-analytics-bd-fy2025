# Power BI Implementation Guide

## 1. Generate and import

```bash
python scripts/build_bi_ready_layer.py
```

In Power BI Desktop choose **Home → Get data → Text/CSV**, select the required files from `data/bi_ready_csv/`, then choose **Transform Data**.

## 2. Confirm data types

- IDs and keys: Text
- Dates: Date
- Headcount, hires, exits and days: Whole number
- Salary and cost: Decimal/fixed decimal
- Rates: Decimal formatted as percentage
- Ratings and scores: Decimal

## 3. Build relationships

Use `bi_assets/semantic_model/relationship_map.csv`. Recommended defaults are one-to-many cardinality, single-direction filtering and one active primary-date relationship per fact.

## 4. Import the theme

Choose **View → Themes → Browse for themes**, then select:

```text
bi_assets/power_bi/Mokhles_Group_HR_Analytics_Theme.json
```

## 5. Starter DAX

```DAX
Active Headcount =
CALCULATE(
    DISTINCTCOUNT('01_dim_employee_fy2025'[employee_id]),
    '01_dim_employee_fy2025'[employment_status] = "Active at FY2025 year-end"
)
```

```DAX
FY2025 Exits =
DISTINCTCOUNT('06_fact_employee_separations_fy2025'[employee_id])
```

```DAX
Total Hires =
SUM('02_fact_monthly_hr_kpi_fy2025'[hires])
```

```DAX
Average Time to Fill =
AVERAGE('05_fact_recruitment_fy2025'[time_to_fill_days])
```

```DAX
Training Hours =
SUM('09_fact_training_development_fy2025'[hours])
```

```DAX
Average Performance Score =
AVERAGE('11_fact_performance_evaluation_fy2025'[overall_score])
```

## 6. Dashboard design

Use `10_DASHBOARD_BLUEPRINT.md` for the six-page report layout.

## 7. Publish and refresh

Publish to an appropriate workspace. For maintainable refresh, store source files in OneDrive, SharePoint, Fabric or another supported governed location rather than an unmanaged local path.

Official references:

- https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-connect-to-data
- https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships
