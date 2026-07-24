# Looker Studio Implementation Guide

## Why use the BI-ready files?

Looker Studio CSV upload requires clean tabular data and restrictive field
names. The files in `data/bi_ready_csv/` use UTF-8 encoding and lowercase
`snake_case` headers without spaces or punctuation.

## 1. Upload a CSV data source

1. Open Looker Studio.
2. Select **Create → Data source**.
3. Choose the **CSV file upload** connector.
4. Create a dataset.
5. Upload one BI-ready CSV file.
6. Select **Connect**.
7. Review field types and aggregations.

Start with:

```text
02_fact_monthly_hr_kpi_fy2025.csv
```

This table can produce a complete executive trend page without blending.

## 2. Recommended focused data sources

- Executive trend: `02_fact_monthly_hr_kpi_fy2025.csv`
- Workforce: `01_dim_employee_fy2025.csv`
- Recruitment: `05_fact_recruitment_fy2025.csv`
- Retention: `06_fact_employee_separations_fy2025.csv`
- Leave: `07_fact_leave_transactions_fy2025.csv`
- Learning: `09_fact_training_development_fy2025.csv`
- Compensation: `10_fact_compensation_benefits_fy2025.csv`
- Performance: `11_fact_performance_evaluation_fy2025.csv`
- Safety: `12_fact_health_safety_fy2025.csv`

## 3. Calculated-field examples

```text
Turnover Percentage
turnover_rate * 100
```

```text
Assessment Improvement
post_assessment_score - pre_assessment_score
```

```text
Annual Gross Equivalent
monthly_gross * 12
```

```text
Active Employee Flag
CASE
  WHEN employment_status = "Active at FY2025 year-end" THEN 1
  ELSE 0
END
```

## 4. Blending guidance

Use blends only when the report genuinely requires fields from multiple data
sources. Keep blend keys simple, such as:

- `employee_id`
- `department`
- `location`
- `month`

For a more scalable multi-table solution, load the CSV files into Google Sheets
or BigQuery and connect Looker Studio to the managed source.

## 5. Avoid duplicate uploads

Adding files to an existing Looker Studio CSV dataset appends the rows. Do not
re-upload the same file unless duplication is intended.

## 6. Recommended report pages

Use one focused source per page whenever possible:

1. Executive Overview
2. Workforce and Diversity
3. Recruitment
4. Retention and Leave
5. Learning and Performance
6. Compensation and Safety

## Official references

- CSV upload:
  https://docs.cloud.google.com/looker/docs/studio/upload-csv-files-to-looker-studio
- Connectors and data sources:
  https://docs.cloud.google.com/looker/docs/studio/connector
