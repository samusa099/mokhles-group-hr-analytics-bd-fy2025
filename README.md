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

## Overview

This repository contains a complete HR analytics portfolio for **Mokhles Group**, a fictional Bangladesh-based organisation. The records are fully synthetic, but the structure, terminology, employee profiles, locations, compensation values and HR transactions were designed to resemble realistic organisational data.

The project combines analysis-ready CSV tables, a consolidated Excel master workbook, 12 specialised Excel reports, a Jupyter Notebook, field-level metadata and automated repository validation.

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
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── assets/
├── data/
│   ├── csv/
│   └── excel/
│       ├── master/
│       └── reports/
├── docs/
├── examples/
├── metadata/
├── notebooks/
├── scripts/
├── src/mokhles_hr_analytics/
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── LICENSE-CODE
├── README.md
└── requirements.txt
```

## Analysis-ready CSV tables

| No. | Table |
|---:|---|
| 01 | Employee Master |
| 02 | Monthly HR KPI |
| 03 | Department Annual Summary |
| 04 | Quarterly Board KPI |
| 05 | Recruitment Master |
| 06 | Employee Separations |
| 07 | Leave Transactions |
| 08 | Diversity and Inclusion Master |
| 09 | Training and Development Master |
| 10 | Compensation and Benefits Master |
| 11 | Performance Evaluation Master |
| 12 | Health and Safety Master |
| 13 | Data Dictionary |

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/mokhles-group-hr-analytics-bd-fy2025.git
cd mokhles-group-hr-analytics-bd-fy2025
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py -m pip install -e .
```

**macOS or Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .
```

### 3. Run the repository validation

```bash
python scripts/validate_repository.py
```

### 4. Launch the notebook

```bash
jupyter lab notebooks/Mokhles_HR_Analytics_EDA.ipynb
```

## Python example

```python
from mokhles_hr_analytics import load_csv_table

employees = load_csv_table("01_Employee_Master_FY2025.csv")
print(employees.head())
print(employees["Department"].value_counts())
```

## Excel portfolio

The `data/excel/` directory includes:

- One consolidated master workbook
- Twelve specialised HR analytics reports
- Executive dashboards
- Filterable Excel tables
- KPI definitions
- Bangladesh-based BDT compensation values

## Kaggle dataset

The published dataset is available on Kaggle:

**Mokhles Group HR Analytics Portfolio BD FY2025**  
https://www.kaggle.com/datasets/samusahr/mokhles-group-hr-analytics-portfolio-bd-fy2025

Kaggle-specific metadata is stored in `metadata/`.

## Data dictionary

The complete field-level data dictionary is available at:

```text
data/csv/13_Data_Dictionary_FY2025.csv
```

Every analysis-ready CSV field also has a native description in:

```text
metadata/kaggle-dataset-metadata.json
```

## Validation and quality controls

The repository includes a validation script and GitHub Actions workflow that check:

- Required files and directories
- CSV header uniqueness
- CSV row and column counts
- Kaggle schema-to-CSV column alignment
- Non-empty field descriptions
- JSON and notebook validity
- Excel workbook ZIP integrity
- Duplicate resource paths

## Suggested research and portfolio extensions

- Employee-turnover prediction
- Recruitment-source optimisation
- Compensation-band modelling
- Workforce forecasting
- Talent segmentation
- Department risk scoring
- Power BI executive dashboard
- SQL-based HR data mart
- Diversity representation analysis

## Author

**Siam Ahmad Musa**  
Human Resources professional and people analytics practitioner from Bangladesh.

## Citation

Please cite this project using the metadata in `CITATION.cff`.

Suggested citation:

> Musa, Siam Ahmad. (2026). *Mokhles Group HR Analytics Demo 2025: A Realistic Synthetic HR Dataset from Bangladesh* (Version 1.0.0).

## Licences

- **Dataset and documentation:** CC BY 4.0 — see `LICENSE`
- **Python code and notebook utilities:** MIT — see `LICENSE-CODE`

## Disclaimer

Mokhles Group is used as a fictional company name. All records are synthetic and must not be presented as real organisational or employee information.
