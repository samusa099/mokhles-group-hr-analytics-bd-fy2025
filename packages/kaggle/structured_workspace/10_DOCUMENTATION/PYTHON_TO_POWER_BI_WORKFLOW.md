# Python → BI-Ready Layer → Power BI

This guide explains how to preserve the original HR data and generate a
cross-platform analytical layer for Power BI, Looker Studio, Tableau,
Qlik Sense, Excel Power Query and Metabase.

## Workflow

```text
data/csv/
   ↓
scripts/build_bi_ready_layer.py
   ↓
data/bi_ready_csv/
   ↓
BI relationships, measures and dashboards
```

## Windows PowerShell

Run from the project root:

```powershell
py --version
py -m pip install -r requirements.txt
py scripts\build_bi_ready_layer.py
Get-ChildItem .\data\bi_ready_csv\*.csv | Select-Object Name, Length
```

Confirm the expected file count:

```powershell
py -c "from pathlib import Path; files=list(Path('data/bi_ready_csv').glob('*.csv')); print('BI-ready CSV files:', len(files)); [print(f.name) for f in files]"
```

Expected:

```text
BI-ready CSV files: 15
```

## Generated layer

```text
data/bi_ready_csv/
├── 00_dim_date.csv
├── 00_dim_department.csv
├── 00_dim_location.csv
├── 01_dim_employee_fy2025.csv
├── 02_fact_monthly_hr_kpi_fy2025.csv
├── 03_fact_department_annual_summary_fy2025.csv
├── 04_fact_quarterly_board_kpi_fy2025.csv
├── 05_fact_recruitment_fy2025.csv
├── 06_fact_employee_separations_fy2025.csv
├── 07_fact_leave_transactions_fy2025.csv
├── 08_dim_diversity_inclusion_fy2025.csv
├── 09_fact_training_development_fy2025.csv
├── 10_fact_compensation_benefits_fy2025.csv
├── 11_fact_performance_evaluation_fy2025.csv
└── 12_fact_health_safety_fy2025.csv
```

## Power BI Desktop

1. Open Power BI Desktop.
2. Select **Home → Get data → Text/CSV**.
3. Import the required files from `data/bi_ready_csv/`.
4. Select **Transform Data**.
5. Verify date, number, percentage and BDT currency fields.
6. Open **Model view**.
7. Follow `bi_assets/semantic_model/relationship_map.csv`.
8. Mark `00_dim_date[date]` as the date table.
9. Import `bi_assets/power_bi/Mokhles_Group_HR_Analytics_Theme.json`.
10. Use `bi_assets/semantic_model/kpi_catalog.csv`.
11. Follow `docs/bi/10_DASHBOARD_BLUEPRINT.md`.

## Refresh

When original files in `data/csv/` change:

```powershell
py scripts\build_bi_ready_layer.py
```

Then in Power BI:

```text
Home → Refresh
```

## Project links

- GitHub: https://github.com/samusa099/mokhles-group-hr-analytics-bd-fy2025
- Kaggle: https://www.kaggle.com/datasets/samusahr/mokhles-group-hr-analytics-portfolio-bd-fy2025
