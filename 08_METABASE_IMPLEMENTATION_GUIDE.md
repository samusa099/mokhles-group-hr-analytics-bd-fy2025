# Metabase Implementation Guide

## Quick portfolio route: CSV upload

1. Open a collection where you have upload access.
2. Select **Add data → CSV**.
3. Upload a file from `data/bi_ready_csv/`.
4. Save the generated model.
5. Review field types and metadata.
6. Build questions and dashboards from the model.

## Recommended first uploads

- `02_fact_monthly_hr_kpi_fy2025.csv`
- `01_dim_employee_fy2025.csv`
- `05_fact_recruitment_fy2025.csv`
- `06_fact_employee_separations_fy2025.csv`

## Production-style route

For frequent updates or a reusable multi-table model:

1. Load the BI-ready CSV files into PostgreSQL, MySQL, ClickHouse, DuckDB or
   another supported analytical database.
2. Connect Metabase to the database.
3. Define table metadata, relationships and models.
4. Create metrics and dashboards from the database-backed model.

CSV upload is best for ad hoc and portfolio use. A database is more maintainable
for larger data volumes and recurring refreshes.

## Official references

- Uploading CSV data:
  https://www.metabase.com/docs/latest/exploration-and-organization/uploads
- Upload configuration and database recommendations:
  https://www.metabase.com/docs/latest/databases/uploads
