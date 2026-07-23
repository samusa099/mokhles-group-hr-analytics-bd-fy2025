<p align="center">
  <img src="assets/mokhles-hr-analytics-cover.png" alt="Mokhles Group HR Analytics Demo 2025" width="100%">
</p>

<h1 align="center">Mokhles Group HR Analytics Demo 2025</h1>

<p align="center">
  <strong>A portfolio-grade, fully synthetic HR analytics ecosystem built for Bangladesh.</strong><br>
  From raw workforce records to board-ready insights across Power BI, Excel, Looker Studio, Tableau, Qlik Sense, Metabase, Python and SQL.
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

---

## ✨ Executive overview

**Mokhles Group HR Analytics Demo 2025** is a complete, portfolio-ready HR and People Analytics project for a fictional Bangladesh-based organisation.

The data is fully synthetic, but the workforce structure, employee profiles, locations, BDT compensation values, recruitment activity, leave, training, performance and safety records are designed to resemble realistic organisational operations.

> **Built to demonstrate an end-to-end analytics workflow:** source data → cleaning → modelling → quality control → KPI design → executive reporting.

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

## 🎯 Project objectives

The project demonstrates how fragmented operational HR records can be transformed into a structured, analysis-ready and cross-platform analytics solution.

The workflow covers:

1. Organising raw HR source data
2. Cleaning and validating employee records
3. Developing HR KPIs and business measures
4. Creating dimension and fact tables
5. Building Employee 360 and Department 360 datasets
6. Designing Excel and Power BI dashboards
7. Performing exploratory analysis with Python and Jupyter Notebook
8. Preparing data for multiple BI platforms
9. Documenting files, columns, relationships and validation rules
10. Presenting management and board-level workforce insights

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

- Workforce structure and headcount
- Monthly and annual HR KPIs
- Recruitment funnel and time-to-fill
- Turnover and retention
- Leave and absence
- Diversity and inclusion
- Training and development
- Compensation and total reward
- Performance and promotion readiness
- Workplace health and safety
- Employee 360 and Department 360 analysis
- Executive and board reporting

---

## 🇧🇩 Bangladesh HR context

The portfolio includes:

- Synthetic Bangladeshi employee names
- Business locations in Dhaka, Gazipur, Narayanganj, Chattogram and Rajshahi
- Salaries, payroll and employment costs in Bangladeshi Taka
- Common local job titles and organisational departments
- Bangladesh-relevant leave and employment categories
- Realistic recruitment and hiring patterns
- Department-level workforce structures
- Performance and promotion-readiness categories
- Training and development records
- Workplace health and safety records

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
| **BI-ready data** | Normalised dimensions and facts | `data/bi_ready_csv/` |
| **Analysis-ready data** | Consolidated Employee 360 and Department 360 tables | `data/analysis_ready/` |
| **Data quality** | Table and column profiling | `data/data_quality/` |
| **BI assets** | Theme, relationships, KPIs, DAX and Power Query | `bi_assets/`, `docs/platforms/` |
| **Automation** | Validation and data-preparation scripts | `scripts/` |

---

## 🗂️ Repository structure

```text
mokhles-group-hr-analytics-bd-fy2025/
├── .github/
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
├── src/mokhles_hr_analytics/
├── wiki/
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── LICENSE-CODE
├── README.md
└── requirements.txt
```

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

### Power BI

- 15 Power Query M scripts
- DAX starter-measure library
- JSON theme
- Relationship map
- Field-name mapping
- KPI catalogue
- Dashboard blueprint
- Reusable `ProjectRoot` parameter

### Excel

- Power Query workflow
- Power Pivot model guidance
- PivotTable and PivotChart blueprint
- Cleaning checklist
- Data-quality summary
- Column profile
- Excel analytics starter workbook

### Looker Studio

- 17 upload-ready CSV files
- Data-source map
- Calculated fields
- Employee 360 and Department 360 datasets
- Dashboard page recommendations

### Tableau, Qlik Sense and Metabase

- Tableau relationship modelling guide
- Qlik Sense load script
- Metabase upload and modelling guide
- Shared semantic-model documentation

---

## 🚀 Quick start

```bash
git clone https://github.com/samusa099/mokhles-group-hr-analytics-bd-fy2025.git
cd mokhles-group-hr-analytics-bd-fy2025
python -m venv .venv
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py -m pip install -e .
```

### macOS or Linux

```bash
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

---

## 🗄️ SQL practice opportunities

The CSV tables can be loaded into SQLite, MySQL, PostgreSQL or another relational database to answer questions such as:

- Which departments have the highest employee turnover?
- What is the average salary by designation?
- Which recruitment sources generate the most successful hires?
- Which employees have the highest leave utilisation?
- What is the average performance score by department?
- Which training programmes have the highest completion rates?
- What are the monthly hiring and separation trends?
- Which departments have the highest payroll cost?
- How does employee tenure relate to performance?
- Which locations report the most workplace incidents?

---

## 💡 Recommended uses

- HR analytics portfolio projects
- Kaggle datasets and notebooks
- Power BI dashboard development
- Excel dashboard, Power Query and Power Pivot practice
- Python and SQL analysis
- Looker Studio, Tableau, Qlik Sense and Metabase projects
- Workforce planning exercises
- Recruitment-funnel analysis
- Turnover and retention analysis
- Compensation and payroll analysis
- Performance and promotion-readiness analysis
- Training and development analysis
- Diversity and inclusion analysis
- Workplace-safety analysis
- Data-cleaning and data-modelling practice
- HR interview presentations
- Academic assignments and professional learning

---

## 🧠 Skills demonstrated

- HR and People Analytics
- Workforce planning
- HR KPI development
- Data cleaning and transformation
- Data validation and quality profiling
- Dimensional modelling and star-schema design
- Dashboard design and data visualisation
- Excel Power Query and Power Pivot
- Power BI and DAX
- Python and Pandas
- SQL analysis
- Cross-platform BI implementation
- Technical documentation
- Executive HR reporting

---

## 👥 Target audience

This project is suitable for:

- HR professionals and HR students
- People Analytics practitioners
- Data and business intelligence analysts
- Power BI and Excel learners
- Python and SQL learners
- University students
- Job seekers and portfolio builders
- Trainers and instructors

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
- Compensation-band modelling
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

All employee names, employee IDs, applicant information, salaries, payroll values, performance results, leave records, recruitment outcomes, training records, compensation values and health-and-safety incidents are fictional.

No real employee, applicant, salary, medical, performance or confidential organisational information was collected or used. The dataset must not be presented as real organisational or employee information.