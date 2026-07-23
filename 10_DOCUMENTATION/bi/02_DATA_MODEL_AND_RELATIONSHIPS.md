# BI Data Model and Relationships

## Recommended model

Use a dimensional model instead of joining every file into one large table.

### Core dimensions

- `00_dim_date.csv`
- `00_dim_department.csv`
- `00_dim_location.csv`
- `01_dim_employee_fy2025.csv`

### Primary facts

- `02_fact_monthly_hr_kpi_fy2025.csv`
- `03_fact_department_annual_summary_fy2025.csv`
- `04_fact_quarterly_board_kpi_fy2025.csv`
- `05_fact_recruitment_fy2025.csv`
- `06_fact_employee_separations_fy2025.csv`
- `07_fact_leave_transactions_fy2025.csv`
- `09_fact_training_development_fy2025.csv`
- `10_fact_compensation_benefits_fy2025.csv`
- `11_fact_performance_evaluation_fy2025.csv`
- `12_fact_health_safety_fy2025.csv`

### Optional employee extension

- `08_dim_diversity_inclusion_fy2025.csv`

## Key relationships

Use `bi_assets/semantic_model/relationship_map.csv` as the implementation
checklist.

The most important keys are:

- `employee_id`
- `department`
- `location`
- `date`
- `month`

## Power BI recommendations

- Use one-to-many relationships from dimensions to facts.
- Use single-direction filtering as the default.
- Mark `00_dim_date[date]` as the date table.
- Keep one active date relationship per fact table.
- Create inactive relationships for alternative dates such as posted date,
  target close date, end date or target close date when needed.
- Avoid unnecessary bidirectional relationships.

## Tableau recommendations

Use logical relationships before physical joins. Relationships preserve the
level of detail of each table and reduce accidental duplication.

## Qlik recommendations

Review automatic associations carefully. Qlik can associate fields with the
same names; the included relationship map helps verify intended links.

## Looker Studio recommendations

For a quick portfolio dashboard, build separate report pages from focused data
sources. Use blends only for limited combinations. For a larger reusable model,
load the BI-ready CSVs into Google Sheets or BigQuery and connect Looker Studio
to that managed source.

## Validation checklist

- Dimension keys contain unique values.
- Fact-table keys can repeat.
- Related columns use the same data type.
- Dates are parsed as dates, not text.
- Currency fields use BDT formatting.
- Rates are formatted as percentages.
- Employee counts use distinct count when necessary.
