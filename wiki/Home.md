# Mokhles Group HR Analytics — Project Wiki

Welcome to the maintained Wiki source for **Mokhles Group HR Analytics Demo 2025**.

This page explains how Python transforms the authoritative HR data into a BI-ready layer and how that layer is used in Power BI Desktop.

> **Data notice:** Mokhles Group is fictional. All employee, recruitment, compensation, performance, leave, training and workplace-safety records are synthetic.

---

## Python → BI layer → Power BI

```text
data/csv/
   ↓
Python generator
   ↓
data/bi_ready_csv/
   ↓
Power BI semantic model
   ↓
HR dashboards and KPI reporting
```

The authoritative source tables remain in:

```text
data/csv/
```

The generated cross-platform BI layer is written to:

```text
data/bi_ready_csv/
```

---

## 1. Prepare Python

Open PowerShell in the repository root and install the required packages:

```powershell
py -m pip install -r requirements.txt
```

Confirm Python:

```powershell
py --version
```

---

## 2. Build the BI-ready layer

Run:

```powershell
py scripts\build_bi_ready_layer.py
```

The generator will:

1. Read the original HR CSV files.
2. Normalize field names to lowercase `snake_case`.
3. Build date, department and location dimensions.
4. Create a unified employee dimension.
5. Generate normalized fact tables for HR analysis.
6. Write the original-to-BI field mapping.

Verify the generated files:

```powershell
Get-ChildItem .\data\bi_ready_csv\*.csv | Select-Object Name, Length
```

Count the generated CSV files:

```powershell
py -c "from pathlib import Path; files=list(Path('data/bi_ready_csv').glob('*.csv')); print('BI-ready CSV files:', len(files)); [print(f.name) for f in files]"
```

Expected result:

```text
BI-ready CSV files: 15
```

---

## 3. Generated BI tables

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

---

## 4. Recommended Power BI workflow

### Import the generated CSV files

1. Open Power BI Desktop.
2. Select **Home → Get data → Text/CSV**.
3. Choose the required files from `data/bi_ready_csv/`.
4. Select **Transform Data**.
5. Confirm field types.
6. Select **Close & Apply**.

### Recommended data types

| Field type | Power BI type |
|---|---|
| Employee and relationship keys | Text |
| Dates | Date |
| Headcount, hires, exits, hours and days | Whole number |
| Compensation and costs | Decimal or fixed decimal |
| Rates | Decimal formatted as percentage |
| Scores and ratings | Decimal number |

---

## 5. Build the Power BI model

Open **Model view** and follow:

```text
bi_assets/semantic_model/relationship_map.csv
```

Recommended rules:

- Dimension-to-fact relationships
- One-to-many cardinality
- Single-direction filtering by default
- One active date relationship per fact table
- `00_dim_date[date]` marked as the date table

Important relationship fields:

```text
employee_id
department
location
date
month
```

---

## 6. Import the Power BI theme

In Power BI Desktop:

```text
View → Themes → Browse for themes
```

Select:

```text
bi_assets/power_bi/Mokhles_Group_HR_Analytics_Theme.json
```

---

## 7. Starter DAX measures

### Active Headcount

```DAX
Active Headcount =
CALCULATE(
    DISTINCTCOUNT('01_dim_employee_fy2025'[employee_id]),
    '01_dim_employee_fy2025'[employment_status] = "Active at FY2025 year-end"
)
```

### FY2025 Exits

```DAX
FY2025 Exits =
DISTINCTCOUNT('06_fact_employee_separations_fy2025'[employee_id])
```

### Total Hires

```DAX
Total Hires =
SUM('02_fact_monthly_hr_kpi_fy2025'[hires])
```

### Average Time to Fill

```DAX
Average Time to Fill =
AVERAGE('05_fact_recruitment_fy2025'[time_to_fill_days])
```

### Training Hours

```DAX
Training Hours =
SUM('09_fact_training_development_fy2025'[hours])
```

### Average Performance Score

```DAX
Average Performance Score =
AVERAGE('11_fact_performance_evaluation_fy2025'[overall_score])
```

### Monthly Gross Payroll

```DAX
Monthly Gross Payroll =
SUM('10_fact_compensation_benefits_fy2025'[monthly_gross])
```

---

## 8. Optional: use Python directly inside Power BI

Power BI Desktop can run Python and import Pandas DataFrames.

First configure Python:

```text
File → Options and settings → Options → Python scripting
```

Then select:

```text
Home → Get data → Other → Python script
```

Use this script after replacing the project path:

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

Power BI will display the generated DataFrames for import.

---

## 9. Refresh workflow

Whenever the original HR CSV files change:

```powershell
py scripts\build_bi_ready_layer.py
```

Then refresh Power BI Desktop:

```text
Home → Refresh
```

For a local portfolio, importing generated CSVs is the simplest workflow. For scheduled refresh in Power BI Service, place the source files in a supported governed location and configure the required cloud connection or gateway.

---

## 10. Dashboard construction order

Recommended report pages:

1. Executive Overview
2. Workforce and Diversity
3. Recruitment
4. Retention and Leave
5. Learning and Performance
6. Compensation and Safety

Use:

```text
bi_assets/semantic_model/dashboard_blueprint.csv
```

and:

```text
docs/bi/10_DASHBOARD_BLUEPRINT.md
```

---

## Detailed guides

- [BI Start Here](../docs/bi/00_BI_START_HERE.md)
- [Data Model and Relationships](../docs/bi/02_DATA_MODEL_AND_RELATIONSHIPS.md)
- [Power BI Implementation Guide](../docs/bi/03_POWER_BI_IMPLEMENTATION_GUIDE.md)
- [KPI Formula Library](../docs/bi/09_KPI_FORMULA_LIBRARY.md)
- [Dashboard Blueprint](../docs/bi/10_DASHBOARD_BLUEPRINT.md)

---

## Project links

- [GitHub Repository](https://github.com/samusa099/mokhles-group-hr-analytics-bd-fy2025)
- [Kaggle Dataset](https://www.kaggle.com/datasets/samusahr/mokhles-group-hr-analytics-portfolio-bd-fy2025)

---

## Author

**Siam Ahmad Musa**  
HR Professional and People Analytics Practitioner, Bangladesh
