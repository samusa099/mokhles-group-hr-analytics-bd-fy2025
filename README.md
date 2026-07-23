<p align="center">
  <img src="assets/mokhles-hr-analytics-cover.png" alt="Mokhles Group HR Analytics Demo 2025" width="100%">
</p>

<h1 align="center">Mokhles Group HR Analytics Demo 2025</h1>

<p align="center">
  A realistic synthetic HR analytics portfolio designed around a Bangladesh business environment.
</p>

<p align="center">
  <img alt="Data Type" src="https://img.shields.io/badge/data-synthetic%20%7C%20tabular-625BEB">
  <img alt="Country" src="https://img.shields.io/badge/context-Bangladesh-1E8E5A">
  <img alt="Period" src="https://img.shields.io/badge/coverage-FY2025-F36B21">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.11%2B-3776AB">
  <img alt="License" src="https://img.shields.io/badge/data%20license-CC%20BY%204.0-lightgrey">
</p>

## Release v2.1.0

Release **v2.1.0** adds a maintainable, cross-platform Business Intelligence layer for Power BI, Looker Studio, Tableau, Qlik Sense, Excel Power Query/Power Pivot and Metabase.

- **GitHub:** https://github.com/samusa099/mokhles-group-hr-analytics-bd-fy2025
- **Kaggle:** https://www.kaggle.com/datasets/samusahr/mokhles-group-hr-analytics-portfolio-bd-fy2025

## Overview

This repository contains a complete HR analytics portfolio for **Mokhles Group**, a fictional Bangladesh-based organisation. The records are fully synthetic, while the structure, terminology, employee profiles, compensation values and HR transactions were designed to resemble realistic organisational data.

The project combines 13 analysis-ready CSV tables, a consolidated Excel master workbook, 12 specialised Excel reports, a Jupyter Notebook, field-level metadata, automated validation and documented BI implementation paths.

> **Privacy and ethics:** No real employee, applicant, salary, performance, health or confidential organisational data is included.

## Project highlights

| Area | Volume |
|---|---:|
| Employees represented during FY2025 | 516 |
| Year-end headcount | 456 |
| Hires | 96 |
| Employee separations | 60 |
| Leave transactions | 1,043 |
| Training participation records | 1,011 |
| Recruitment requisitions | 110 |
| Performance evaluation records | 456 |
| Health and safety records | 120 |
| Native field descriptions | 186 |

## Business Intelligence compatibility

Supported implementation guides:

- Power BI Desktop
- Looker Studio
- Tableau
- Qlik Sense
- Excel Power Query and Power Pivot
- Metabase

Start here:

```text
docs/bi/00_BI_START_HERE.md
```

Generate the complete 15-table BI-ready layer locally:

```bash
python scripts/build_bi_ready_layer.py
```

The generator creates lowercase `snake_case` dimensions and facts inside `data/bi_ready_csv/`, plus an original-to-BI field mapping. The repository also includes a semantic relationship map, KPI catalogue, dashboard blueprint and Power BI JSON theme.

## Python → BI-ready layer → Power BI workflow

### What the Python layer does

The command reads the authoritative HR tables from `data/csv/` and produces a reusable analytical layer in `data/bi_ready_csv/`.

It performs the following work:

1. Reads the original HR CSV tables.
2. Converts column names to lowercase `snake_case` for cross-platform compatibility.
3. Creates reusable date, department and location dimensions.
4. Builds a unified employee dimension covering active and separated employees.
5. Produces normalized HR fact tables for KPI, recruitment, separation, leave, training, compensation, performance and safety analysis.
6. Writes the original-to-BI field mapping to `bi_assets/semantic_model/field_name_mapping.csv`.

### Windows PowerShell commands

Run these commands from the repository root:

```powershell
py -m pip install -r requirements.txt
py scripts\build_bi_ready_layer.py
Get-ChildItem .\data\bi_ready_csv\*.csv | Select-Object Name, Length
```

Confirm that 15 BI-ready CSV files were created:

```powershell
py -c "from pathlib import Path; files=list(Path('data/bi_ready_csv').glob('*.csv')); print('BI-ready CSV files:', len(files)); [print(f.name) for f in files]"
```

Expected result:

```text
BI-ready CSV files: 15
```

### macOS or Linux commands

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build_bi_ready_layer.py
ls -1 data/bi_ready_csv/*.csv
```

### Generated layer

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

### Recommended Power BI method: import generated CSV files

1. Run the Python layer command.
2. Open Power BI Desktop.
3. Select **Home → Get data → Text/CSV**.
4. Import the required files from `data/bi_ready_csv/`.
5. Select **Transform Data** and verify dates, numbers, percentages and BDT currency fields.
6. Open **Model view** and implement the relationships listed in:

```text
bi_assets/semantic_model/relationship_map.csv
```

7. Mark `00_dim_date[date]` as the date table.
8. Import the Power BI theme from:

```text
bi_assets/power_bi/Mokhles_Group_HR_Analytics_Theme.json
```

9. Build measures using `bi_assets/semantic_model/kpi_catalog.csv` and the formulas in `docs/bi/09_KPI_FORMULA_LIBRARY.md`.
10. Build report pages using `docs/bi/10_DASHBOARD_BLUEPRINT.md`.

### Optional method: run Python directly inside Power BI Desktop

Power BI Desktop can run a Python script and import the resulting Pandas DataFrames. Replace the path below with the local repository path:

```python
from pathlib import Path
import runpy
import pandas as pd

PROJECT_ROOT = Path(
    r"C:\Users\YourName\Downloads\mokhles-group-hr-analytics-bd-fy2025"
)

runpy.run_path(
    str(PROJECT_ROOT / "scripts" / "build_bi_ready_layer.py"),
    run_name="__main__",
)

BI_DATA = PROJECT_ROOT / "data" / "bi_ready_csv"

employees = pd.read_csv(BI_DATA / "01_dim_employee_fy2025.csv")
monthly_hr_kpi = pd.read_csv(BI_DATA / "02_fact_monthly_hr_kpi_fy2025.csv")
recruitment = pd.read_csv(BI_DATA / "05_fact_recruitment_fy2025.csv")
separations = pd.read_csv(BI_DATA / "06_fact_employee_separations_fy2025.csv")
training = pd.read_csv(BI_DATA / "09_fact_training_development_fy2025.csv")
performance = pd.read_csv(BI_DATA / "11_fact_performance_evaluation_fy2025.csv")
```

In Power BI Desktop:

1. Configure Python under **File → Options and settings → Options → Python scripting**.
2. Select **Home → Get data → Other → Python script**.
3. Paste the script.
4. Select the DataFrames to import.
5. Build relationships and measures in the Power BI model.

### Refresh workflow

When the original HR CSV files change, run:

```powershell
py scripts\build_bi_ready_layer.py
```

Then refresh Power BI Desktop:

```text
Home → Refresh
```

For local portfolio work, the generated-CSV method is the simplest and most transparent. For scheduled Power BI Service refresh, store source files in a supported governed location and configure the required gateway or cloud connection.

### Detailed documentation

- [BI Start Here](docs/bi/00_BI_START_HERE.md)
- [Data Model and Relationships](docs/bi/02_DATA_MODEL_AND_RELATIONSHIPS.md)
- [Power BI Implementation Guide](docs/bi/03_POWER_BI_IMPLEMENTATION_GUIDE.md)
- [KPI Formula Library](docs/bi/09_KPI_FORMULA_LIBRARY.md)
- [Dashboard Blueprint](docs/bi/10_DASHBOARD_BLUEPRINT.md)
- [Repository Wiki Source](wiki/Home.md)

Official Microsoft references:

- https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-python-scripts
- https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-python-in-query-editor
- https://learn.microsoft.com/en-us/power-query/connectors/text-csv
- https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships

## Analytics coverage

- Headcount and workforce structure
- Monthly and annual HR KPIs
- Recruitment funnel and time-to-fill
- Employee turnover and retention
- Leave and absence
- Diversity and inclusion
- Learning and development
- Compensation and total reward
- Performance and talent readiness
- Health, safety and corrective actions
- Executive and board-level HR reporting

## Repository structure

```text
mokhles-group-hr-analytics-bd-fy2025/
├── .github/                 Workflows and contribution templates
├── assets/                  Cover and dashboard previews
├── bi_assets/               BI theme and semantic-model assets
├── data/
│   ├── csv/                 13 authoritative analytical CSVs
│   ├── bi_ready_csv/        Generated cross-platform BI layer
│   └── excel/               Master workbook and 12 reports
├── docs/bi/                 Platform-specific BI guides
├── wiki/                    Maintained Wiki Markdown source
├── examples/                Python usage example
├── metadata/                Project, GitHub and Kaggle metadata
├── notebooks/               Exploratory Jupyter Notebook
├── scripts/                 Validation and BI generation utilities
└── src/                     Reusable Python data loader
```

## Quick start

```bash
git clone https://github.com/samusa099/mokhles-group-hr-analytics-bd-fy2025.git
cd mokhles-group-hr-analytics-bd-fy2025
python -m pip install -r requirements.txt
python -m pip install -e .
python scripts/validate_repository.py
python scripts/build_bi_ready_layer.py
```

Launch the notebook:

```bash
jupyter lab notebooks/Mokhles_HR_Analytics_EDA.ipynb
```

## Excel portfolio

The `data/excel/` directory includes one consolidated master workbook and 12 specialised reports covering headcount, monthly KPIs, annual reporting, board KPIs, recruitment, turnover, leave, diversity, learning, compensation, performance and health and safety.

## Data dictionary

The complete field-level dictionary is available at:

```text
data/csv/13_Data_Dictionary_FY2025.csv
```

## Validation and quality controls

The repository validates required files, CSV headers, schema alignment, field descriptions, JSON/notebook validity and Excel workbook integrity through a local script and GitHub Actions.

## Author

**Siam Ahmad Musa**  
Human Resources professional and people analytics practitioner from Bangladesh.

## Licences

- **Dataset and documentation:** CC BY 4.0
- **Python utilities and supporting code:** MIT Licence

## Disclaimer

Mokhles Group is a fictional company name. All records are synthetic and must not be presented as real organisational or employee information.
