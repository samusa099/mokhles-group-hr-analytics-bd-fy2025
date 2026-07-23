# Looker Studio Implementation Guide

## Prepare the files

```bash
python scripts/build_bi_ready_layer.py
```

The generated CSVs use UTF-8 and lowercase `snake_case` headers without spaces or punctuation.

## Upload a source

1. Open Looker Studio.
2. Select **Create → Data source**.
3. Choose **CSV file upload**.
4. Create a dataset and upload one BI-ready CSV.
5. Select **Connect** and review field types.

Start with `02_fact_monthly_hr_kpi_fy2025.csv` for an executive trend page.

## Focused sources

- Workforce: `01_dim_employee_fy2025.csv`
- Recruitment: `05_fact_recruitment_fy2025.csv`
- Retention: `06_fact_employee_separations_fy2025.csv`
- Leave: `07_fact_leave_transactions_fy2025.csv`
- Learning: `09_fact_training_development_fy2025.csv`
- Compensation: `10_fact_compensation_benefits_fy2025.csv`
- Performance: `11_fact_performance_evaluation_fy2025.csv`
- Safety: `12_fact_health_safety_fy2025.csv`

## Calculated-field examples

```text
Assessment Improvement
post_assessment_score - pre_assessment_score
```

```text
Annual Gross Equivalent
monthly_gross * 12
```

Use blends only when a report genuinely requires multiple sources. For a scalable reusable model, load the CSVs into Google Sheets or BigQuery.

Do not re-upload the same file into an existing CSV dataset unless appending duplicate rows is intentional.

Official reference: https://docs.cloud.google.com/looker/docs/studio/upload-csv-files-to-looker-studio
