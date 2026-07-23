# Metabase Implementation Guide

## Quick portfolio route

1. Run `python scripts/build_bi_ready_layer.py`.
2. Open a collection where CSV upload is enabled.
3. Select **Add data → CSV**.
4. Upload a file from `data/bi_ready_csv/`.
5. Save the generated model and review field metadata.
6. Build questions and dashboards.

Recommended first files:

- `02_fact_monthly_hr_kpi_fy2025.csv`
- `01_dim_employee_fy2025.csv`
- `05_fact_recruitment_fy2025.csv`
- `06_fact_employee_separations_fy2025.csv`

## Production-style route

For recurring refreshes, load the BI-ready CSVs into PostgreSQL, MySQL, ClickHouse, DuckDB or another supported database, connect Metabase to it, and define relationships/models there.

CSV upload is best for ad hoc and portfolio use; a database is more maintainable for recurring production analysis.

Official reference: https://www.metabase.com/docs/latest/exploration-and-organization/uploads
