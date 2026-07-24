# Metabase Guide

## Simple CSV workflow

Upload one CSV at a time from `02_CLEAN_DATA/analysis_ready/` or
`02_CLEAN_DATA/bi_ready_csv/`.

Recommended starting files:

- employee_360_fy2025.csv
- department_360_summary_fy2025.csv
- 02_fact_monthly_hr_kpi_fy2025.csv

Metabase CSV uploads create an underlying table and a model. Appending or
replacing data requires matching columns, order and types. Metabase attempts to
infer column types, so use the included data-quality and column-profile files
to verify dates and numeric fields.

For a maintained production workflow, load the tables into a supported
database and connect Metabase to that database rather than repeatedly uploading
CSV files.

Official references:

- https://www.metabase.com/docs/latest/exploration-and-organization/uploads
- https://www.metabase.com/docs/latest/databases/uploads
- https://www.metabase.com/docs/latest/data-modeling/start
