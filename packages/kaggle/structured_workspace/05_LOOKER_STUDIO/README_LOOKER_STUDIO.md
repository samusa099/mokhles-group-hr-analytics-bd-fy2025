# Looker Studio Guide

## Fastest dashboard path

Start with:

- `employee_360_fy2025.csv`
- `department_360_summary_fy2025.csv`
- `02_fact_monthly_hr_kpi_fy2025.csv`

## Upload rule

Create a separate Looker Studio CSV dataset for each file because the tables
have different schemas. Looker Studio can append multiple files to one dataset
only when the headers are identical. Appending does not create relational joins
and does not remove duplicate rows.

All files in `upload_ready_csv/`:

- use UTF-8
- are tabular
- have unique lowercase snake_case headers
- use CSV format suitable for file upload

## Suggested report pages

1. Executive Overview
2. Workforce and Diversity
3. Recruitment
4. Retention and Leave
5. Learning and Performance
6. Compensation and Safety

Official reference:

- https://cloud.google.com/looker/docs/studio/upload-csv-files-to-looker-studio
