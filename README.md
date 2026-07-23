<p align="center">
  <img src="https://github.com/user-attachments/assets/4e0c66e6-6a13-40c7-bd96-049664b2df81" alt="Mokhles Group HR Analytics Portfolio — Bangladesh FY2025" width="75%">
</p>

<h1 align="center">Mokhles Group HR Analytics Demo 2025</h1>

<p align="center">
  <strong>A portfolio-grade, fully synthetic HR analytics ecosystem built for Bangladesh.</strong><br>
  From raw workforce records to board-ready insights across Power BI, Excel, Looker Studio, Tableau, Qlik Sense, Metabase and Python.
</p>

<p align="center">
  <a href="https://www.kaggle.com/datasets/samusahr/mokhles-group-hr-analytics-portfolio-bd-fy2025"><img alt="Kaggle Dataset" src="https://img.shields.io/badge/Kaggle-Live%20Dataset-20BEFF?logo=kaggle&logoColor=white"></a>
  <img alt="Data Type" src="https://img.shields.io/badge/Data-Synthetic%20%7C%20Tabular-625BEB">
  <img alt="Country" src="https://img.shields.io/badge/Context-Bangladesh-1E8E5A">
  <img alt="Period" src="https://img.shields.io/badge/Coverage-FY2025-F36B21">
  <img alt="Release" src="https://img.shields.io/badge/Release-v2.3.0-7C3AED">
</p>

<p align="center">
  <img alt="Power BI" src="https://img.shields.io/badge/Power%20BI-Ready-F2C811?logo=powerbi&logoColor=black">
  <img alt="Excel" src="https://img.shields.io/badge/Excel-Power%20Query%20%7C%20Power%20Pivot-217346?logo=microsoftexcel&logoColor=white">
  <img alt="Looker Studio" src="https://img.shields.io/badge/Looker%20Studio-Ready-4285F4?logo=looker&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/Data%20License-CC%20BY%204.0-lightgrey">
</p>

<p align="center">
  <a href="#-executive-overview">Executive Overview</a> ·
  <a href="#-portfolio-at-a-glance">Portfolio at a Glance</a> ·
  <a href="#-analytics-architecture">Architecture</a> ·
  <a href="#-platform-readiness">Platform Readiness</a> ·
  <a href="#-quick-start">Quick Start</a> ·
  <a href="#-data-ethics">Data Ethics</a>
</p>

---

## ✨ Executive overview

**Mokhles Group HR Analytics Demo 2025** is a complete, portfolio-ready HR and People Analytics project for a fictional Bangladesh-based organisation.

The data is fully synthetic, but the workforce structure, employee profiles, locations, BDT compensation values, recruitment activity, leave, training, performance and safety records are designed to resemble realistic organisational operations.

> **Built to demonstrate an end-to-end analytics workflow:** source data → cleaning → modeling → quality control → KPI design → executive reporting.

<table>
<tr>
<td width="25%" align="center"><strong>516</strong><br>Employees represented</td>
<td width="25%" align="center"><strong>15</strong><br>BI-ready tables</td>
<td width="25%" align="center"><strong>14</strong><br>Excel workbooks</td>
<td width="25%" align="center"><strong>803</strong><br>Documented fields</td>
</tr>
</table>

### What makes this project different

| Capability | What is included |
|---|---|
| **Business realism** | Bangladesh names, locations, BDT compensation, HR terminology and operational-style transactions |
| **Analytics depth** | Workforce, recruitment, retention, leave, learning, compensation, performance, diversity and safety |
| **BI engineering** | Dimensions, facts, relationship maps, KPI catalogue, DAX, Power Query M and dashboard blueprint |
| **Data quality** | Table profiling, column profiling, duplicate checks, key validation and remediation rules |
| **Portfolio usability** | Excel dashboards, Jupyter analysis, Kaggle metadata, documentation and reproducible scripts |
| **Ethical design** | No real employee or confidential organisational data |

---

## 📊 Portfolio at a glance

| Business area | Volume |
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
| Original analytical CSV tables | 13 |
| BI-ready CSV tables | 15 |
| Consolidated analysis-ready tables | 2 |
| Excel workbooks | 14 |
| Looker Studio-ready CSV files | 17 |
| Structured metadata resources | 138 |
| Documented CSV fields | 803 |

### Analytics coverage

<table>
<tr>
<td width="33%">

**Workforce**
- Headcount and structure
- Monthly and annual HR KPIs
- Diversity and inclusion
- Employee 360 analysis
- Department 360 analysis

</td>
<td width="33%">

**Talent**
- Recruitment funnel
- Time-to-fill
- Turnover and retention
- Learning and development
- Performance and promotion readiness

</td>
<td width="33%">

**Operations**
- Leave and absence
- Compensation and total reward
- Health and safety
- Data-quality profiling
- Executive and board reporting

</td>
</tr>
</table>

---

## 🧱 Analytics architecture

```text
Authoritative HR source tables
            │
            ▼
    Python transformation layer
            │
            ▼
 BI-ready dimensions and fact tables
            │
            ├────────► Power BI semantic model
            ├────────► Excel Power Query / Power Pivot
            ├────────► Looker Studio data sources
            ├────────► Tableau relationships
            ├────────► Qlik associative model
            └────────► Metabase models
```

### Core data layers

| Layer | Purpose | Location |
|---|---|---|
| **Source data** | Authoritative CSV and Excel portfolio | `data/csv/`, `data/excel/` |
| **BI-ready data** | Normalized dimensions and facts | `data/bi_ready_csv/` |
| **Analysis-ready data** | Consolidated Employee 360 and Department 360 tables | `data/analysis_ready/` |
| **Data quality** | Table and column profiling | `data/data_quality/` |
| **BI assets** | Theme, relationships, KPIs, DAX and Power Query | `bi_assets/`, `docs/platforms/` |
| **Automation** | Validation and data-preparation scripts | `scripts/` |

---

## 🗂️ Repository structure

<details open>
<summary><strong>View project structure</strong></summary>

```text
mokhles-group-hr-analytics-bd-fy2025/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── assets/
├── bi_assets/
│   ├── power_bi/
│   └── semantic_model/
├── data/
│   ├── csv/
│   ├── bi_ready_csv/
│   ├── analysis_ready/
│   ├── data_quality/
│   └── excel/
│       ├── master/
│       └── reports/
├── docs/
│   ├── bi/
│   └── platforms/
│       ├── power_bi_assets/
│       ├── excel_analytics/
│       ├── looker_studio/
│       ├── tableau/
│       ├── qlik/
│       └── metabase/
├── examples/
├── metadata/
├── notebooks/
├── scripts/
├── src/
│   └── mokhles_hr_analytics/
├── wiki/
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── LICENSE-CODE
├── README.md
└── requirements.txt
```

</details>

---

## 🧾 Source tables

| No. | Table | Primary analytical purpose |
|---:|---|---|
| 01 | Employee Master | Workforce profile and structure |
| 02 | Monthly HR KPI | Monthly HR performance trends |
| 03 | Department Annual Summary | Department-level annual review |
| 04 | Quarterly Board KPI | Executive and board reporting |
| 05 | Recruitment Master | Hiring funnel, cost and time-to-fill |
| 06 | Employee Separations | Turnover, exit reasons and regrettable loss |
| 07 | Leave Transactions | Leave volume, type and approval analysis |
| 08 | Diversity and Inclusion Master | Representation and inclusion indicators |
| 09 | Training and Development Master | Learning hours, cost and assessment improvement |
| 10 | Compensation and Benefits Master | Pay, benefits, total reward and compa-ratio |
| 11 | Performance Evaluation Master | Ratings, potential and promotion readiness |
| 12 | Health and Safety Master | Incidents, severity and corrective action |
| 13 | Data Dictionary | Field definitions and metadata |

---

## 🔄 BI-ready analytical layer

Run the generator:

```powershell
py scripts\build_bi_ready_layer.py
```

Expected output:

```text
BI-ready layer created: 15 CSV files
```

<details>
<summary><strong>View generated BI tables</strong></summary>

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

</details>

### Consolidated analysis-ready datasets

| Dataset | Grain | Best use |
|---|---|---|
| `employee_360_fy2025.csv` | One row per employee | Workforce, diversity, compensation, performance, leave, training and separation analysis |
| `department_360_summary_fy2025.csv` | One row per department | Executive comparison and departmental KPI analysis |

---

## ✅ Data-quality layer

```text
data/data_quality/
├── table_quality_summary.csv
├── column_profile.csv
└── validation_rules.csv
```

Checks include:

- Row and column counts
- Blank-cell rates
- Duplicate rows
- Primary and composite key checks
- UTF-8 readability
- Type inference
- Distinct-value counts
- Minimum and maximum values
- Sample values
- Recommended remediation actions

---

## 🧰 Platform readiness

<table>
<tr>
<td width="50%">

### 🟨 Power BI

- 15 Power Query M scripts
- DAX starter-measure library
- JSON theme
- Relationship map
- Field-name mapping
- KPI catalogue
- Dashboard blueprint
- Reusable `ProjectRoot` parameter

**Start here:** `docs/platforms/power_bi_assets/`

</td>
<td width="50%">

### 🟩 Excel

- Power Query workflow
- Power Pivot model guidance
- PivotTable and PivotChart blueprint
- Cleaning checklist
- Data-quality summary
- Column profile
- Excel analytics starter workbook

**Start here:** `docs/platforms/excel_analytics/`

</td>
</tr>
<tr>
<td width="50%">

### 🟦 Looker Studio

- 17 upload-ready CSV files
- Data-source map
- Calculated fields
- Employee 360 and Department 360 datasets
- Dashboard page recommendations

**Start here:** `docs/platforms/looker_studio/`

</td>
<td width="50%">

### 🟪 Tableau, Qlik and Metabase

- Tableau relationship modeling guide
- Qlik Sense load script
- Metabase upload and modeling guide
- Shared semantic-model documentation

**Start here:** `docs/platforms/`

</td>
</tr>
</table>

---

## 🚀 Quick start

### Clone and prepare

```bash
git clone https://github.com/samusa099/mokhles-group-hr-analytics-bd-fy2025.git
cd mokhles-group-hr-analytics-bd-fy2025
```

#### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py -m pip install -e .
```

#### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .
```

### Validate, build and explore

```bash
python scripts/validate_repository.py
python scripts/build_bi_ready_layer.py
python scripts/build_analysis_ready.py
python scripts/profile_data.py
jupyter lab notebooks/Mokhles_HR_Analytics_EDA.ipynb
```

### Python example

```python
from mokhles_hr_analytics import load_csv_table

employees = load_csv_table("01_Employee_Master_FY2025.csv")

print(employees.head())
print(employees["Department"].value_counts())
```

---

## 📦 Excel portfolio

The Excel portfolio includes:

- One consolidated master workbook
- Twelve specialised HR analytics reports
- Executive dashboards
- Filterable tables
- KPI definitions
- BDT compensation values
- A dedicated Excel analytics starter workbook

---

## 🌐 Kaggle dataset

**Mokhles Group HR Analytics Portfolio BD FY2025**

https://www.kaggle.com/datasets/samusahr/mokhles-group-hr-analytics-portfolio-bd-fy2025

The Kaggle release includes:

- Dataset and file descriptions
- CSV schemas and column descriptions
- Tags and source statement
- Cover image and licence metadata
- Individually previewable CSV and Excel assets
- Downloadable structured analytics workspace

---

## 🧪 Validation and governance

The repository validates:

- Required files and directories
- CSV header uniqueness
- Row and column counts
- Schema alignment
- File descriptions
- Column descriptions
- Tags and source statement
- JSON and notebook validity
- Excel workbook integrity
- Duplicate metadata paths
- BI-layer completeness
- Structured-workspace integrity

---

## 🔬 Portfolio extension ideas

- Employee-turnover prediction
- Recruitment-source optimisation
- Compensation-band modeling
- Workforce forecasting
- Talent segmentation
- Department risk scoring
- Executive Power BI dashboard
- SQL-based HR data mart
- Diversity representation analysis
- Training ROI analysis
- Absence-risk analysis
- Automated BI refresh pipeline

---

## 👤 Author

**Siam Ahmad Musa**  
Human Resources professional and People Analytics practitioner from Bangladesh.

---

## 📝 Citation

Please cite this project using `CITATION.cff`.

> Musa, S. A. (2026). *Mokhles Group HR Analytics Demo 2025: A Realistic Synthetic HR Dataset and Cross-Platform Analytics Portfolio from Bangladesh* (Version 2.3.0).

---

## ⚖️ Licences

- **Dataset and documentation:** CC BY 4.0 — see `LICENSE`
- **Python code and notebook utilities:** MIT — see `LICENSE-CODE`

---

## 🛡️ Data ethics

Mokhles Group is a fictional company name.

All employee, applicant, compensation, performance, leave, training and health-and-safety records are synthetic. They must not be presented as real organisational or employee information.
