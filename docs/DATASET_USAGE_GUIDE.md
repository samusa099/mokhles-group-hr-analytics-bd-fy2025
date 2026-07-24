# 📘 Dataset Usage Guide

> **Mokhles Group HR Analytics Demo 2025** is a fully synthetic HR and People Analytics dataset created for learning, portfolio development, dashboard prototyping and analytical practice in a Bangladesh business context.

<p align="center">
  <strong>Why to use it · How to use it · Where to use it · What to calculate</strong>
</p>

---

## 🎯 Why use this dataset?

This project helps learners and practitioners move beyond one flat spreadsheet and practise a complete HR analytics workflow:

- 🧹 **Data cleaning** — missing values, data types, naming standards and duplicate checks
- 🧱 **Data modeling** — dimensions, fact tables, keys, grain and relationships
- 🧮 **HR KPI calculation** — headcount, turnover, hiring, leave, training, compensation, performance and safety
- 📊 **Dashboard building** — operational, management and board-level reporting
- 🐍 **Python analysis** — pandas, profiling, visualisation and reproducible automation
- 🗄️ **SQL practice** — joins, aggregations, CTEs, window functions and reusable views
- 🤖 **Machine-learning practice** — workforce-risk classification, forecasting and segmentation
- 💼 **Portfolio development** — GitHub, Kaggle, interview case studies and presentation-ready outputs

Because all records are synthetic, users can experiment without exposing real employee, applicant, payroll, medical or organisational information.

---

## 👥 Who can use it?

| User | Practical value |
|---|---|
| 🎓 Students | Learn HR metrics, Excel, SQL, Python and BI with realistic business tables |
| 👩‍💼 HR professionals | Practise People Analytics and management reporting |
| 📊 Data analysts | Build star schemas, KPI models and dashboards |
| 🐍 Python learners | Perform EDA, cleaning, profiling and automation |
| 🧑‍🏫 Trainers | Create structured exercises for Excel, Power BI, SQL and analytics classes |
| 💼 Job seekers | Build portfolio projects and interview case studies |
| 🔬 Researchers | Demonstrate analytical methods with non-confidential synthetic data |

---

## 🌍 Where can it be used?

### 📊 Business intelligence

- Power BI executive dashboards
- Excel Power Query and Power Pivot models
- Looker Studio reports
- Tableau relationship models
- Qlik Sense applications
- Metabase dashboards

### 🧪 Data and analytics practice

- Exploratory data analysis
- SQL data marts
- Data-quality assessment
- Data dictionary and metadata exercises
- KPI validation
- Workforce forecasting
- Employee segmentation
- Turnover-risk modelling

### 💼 Career and portfolio use

- GitHub portfolio repository
- Kaggle dataset and notebook
- HR analytics case study
- Data analyst interview presentation
- Power BI portfolio dashboard
- Academic assignment or capstone demonstration
- Internal training workshop using synthetic information

### 🏢 HR functional analysis

- Workforce structure and headcount
- Recruitment funnel and hiring efficiency
- Employee separation and retention
- Leave and absence patterns
- Diversity and representation
- Learning and development
- Compensation and total rewards
- Performance and promotion readiness
- Workplace health and safety
- Quarterly board reporting

---

## 🗂️ Choose the correct data layer

| Need | Recommended location | Why |
|---|---|---|
| Understand original HR records | `data/csv/` | Authoritative source tables with operational-style fields |
| Build a relational BI model | `data/bi_ready_csv/` | Normalised dimensions and fact tables |
| Start quickly with one employee table | `data/analysis_ready/employee_360_fy2025.csv` | One row per employee with consolidated analytical fields |
| Compare departments | `data/analysis_ready/department_360_summary_fy2025.csv` | One row per department with summary KPIs |
| Review data quality | `data/data_quality/` | Table profile, field profile and validation rules |
| Use Excel dashboards | `data/excel/` | Master workbook and specialised reports |
| Use the numbered Kaggle package | `packages/kaggle/structured_workspace/` | Download-friendly folders separated by purpose |
| Understand every field | Data Dictionary and metadata resources | Definitions, types and analytical meaning |
| Build Power BI | `docs/platforms/power_bi_assets/` and `bi_assets/` | Relationship map, DAX, Power Query and theme |

> 💡 **Fastest starting point:** use `employee_360_fy2025.csv` for employee analysis and `department_360_summary_fy2025.csv` for executive comparison.

---

## 🧭 Which table answers which question?

| Business question | Recommended table |
|---|---|
| How many employees are active? | Employee Master / Employee 360 |
| Which departments are growing? | Monthly HR KPI / Department Annual Summary |
| How many employees were hired? | Monthly HR KPI / Recruitment Master |
| What is the average time-to-fill? | Recruitment Master |
| Why are employees leaving? | Employee Separations |
| Which department has the highest turnover? | Employee Separations + Employee/Department dimension |
| What leave types are most common? | Leave Transactions |
| Is representation balanced? | Diversity and Inclusion Master |
| How much training was delivered? | Training and Development Master |
| Did assessment scores improve? | Training and Development Master |
| Are salaries aligned with bands? | Compensation and Benefits Master |
| Who may be promotion-ready? | Performance Evaluation Master |
| What safety incidents occurred? | Health and Safety Master |
| What should leadership review? | Quarterly Board KPI / Department 360 Summary |

---

## 🚀 Recommended analysis workflow

### 1️⃣ Define the business question

Examples:

- Which department has the highest employee turnover?
- Which recruitment source produces faster hires?
- Is compensation aligned with salary bands?
- Does training participation relate to performance?
- Which departments require management attention?

### 2️⃣ Confirm the grain

- **Employee grain:** one row per employee
- **Transaction grain:** one row per leave, training, recruitment or safety event
- **Monthly grain:** one row per month or department-month
- **Department grain:** one row per department
- **Quarterly grain:** one row per quarter or board KPI

> ⚠️ Never join tables before confirming their grain. An incorrect one-to-many join can inflate totals and produce misleading KPIs.

### 3️⃣ Read the Data Dictionary

Before calculating a KPI:

- confirm the field definition;
- identify whether the field is a count, amount, percentage or score;
- confirm whether blank values are valid;
- identify the primary or relationship key;
- confirm the reporting period and unit.

### 4️⃣ Validate data quality

```bash
python scripts/validate_repository.py
python scripts/profile_data.py
```

Review:

```text
data/data_quality/table_quality_summary.csv
data/data_quality/column_profile.csv
data/data_quality/validation_rules.csv
```

### 5️⃣ Build analytical layers

```bash
python scripts/build_bi_ready_layer.py
python scripts/build_analysis_ready.py
```

### 6️⃣ Calculate and cross-check KPIs

For important KPIs, compare at least two implementations when practical—for example Python versus Excel, SQL or Power BI.

### 7️⃣ Build a decision-focused report

A useful report should answer:

1. **What happened?**
2. **Where did it happen?**
3. **Why might it have happened?**
4. **What should management review next?**

---

# 🧮 HR KPI Calculation Library

## 👥 Workforce calculations

### Beginning headcount

```text
Beginning Headcount = Ending Headcount - Hires + Separations
```

Portfolio example:

```text
456 - 96 + 60 = 420 employees
```

### Average headcount

```text
Average Headcount = (Beginning Headcount + Ending Headcount) / 2
```

```text
(420 + 456) / 2 = 438 employees
```

### Headcount growth rate

```text
Headcount Growth % = (Ending Headcount - Beginning Headcount) / Beginning Headcount × 100
```

```text
(456 - 420) / 420 × 100 = 8.57%
```

### Hiring rate

```text
Hiring Rate % = Hires / Average Headcount × 100
```

```text
96 / 438 × 100 = 21.92%
```

### Turnover rate

```text
Turnover Rate % = Separations / Average Headcount × 100
```

```text
60 / 438 × 100 = 13.70%
```

### Retention rate

A simplified annual form:

```text
Retention Rate % = 100 - Turnover Rate %
```

```text
100 - 13.70 = 86.30%
```

For rigorous cohort retention, track only employees present at the start of the period.

---

## 🎯 Recruitment calculations

### Average time-to-fill

```text
Average Time-to-Fill = Total Time-to-Fill Days / Filled Requisitions
```

### Offer acceptance rate

```text
Offer Acceptance % = Accepted Offers / Total Offers × 100
```

### Selection rate

```text
Selection Rate % = Hires / Applicants × 100
```

### Cost per hire

```text
Cost per Hire = Total Recruitment Cost / Number of Hires
```

### Recruitment source effectiveness

Compare each source by:

- applicants generated;
- shortlisted candidates;
- offers accepted;
- hires completed;
- average time-to-fill;
- cost per hire.

---

## 🗓️ Leave and absence calculations

### Leave utilisation

```text
Leave Utilisation % = Leave Days Used / Leave Days Available × 100
```

### Absence rate

```text
Absence Rate % = Absent Workdays / Available Workdays × 100
```

### Average leave duration

```text
Average Leave Duration = Approved Leave Days / Approved Leave Transactions
```

Useful breakdowns:

- leave type;
- department;
- location;
- month;
- approval status;
- employee level.

---

## 🎓 Learning and development calculations

### Training completion rate

```text
Training Completion % = Completed Participants / Enrolled Participants × 100
```

### Average training hours

```text
Average Training Hours = Total Training Hours / Participants
```

### Assessment improvement

```text
Score Improvement = Post-Assessment Score - Pre-Assessment Score
```

### Training ROI

```text
Training ROI % = (Estimated Benefit - Training Cost) / Training Cost × 100
```

Use ROI only when benefit estimates have a transparent and defensible methodology.

---

## 💰 Compensation calculations

### Compa-ratio

```text
Compa-Ratio = Employee Salary / Salary Range Midpoint
```

Typical interpretation:

| Compa-ratio | Possible interpretation |
|---:|---|
| Below 0.80 | Well below midpoint; review context and band placement |
| 0.80–0.99 | Below midpoint |
| 1.00 | At midpoint |
| 1.01–1.20 | Above midpoint |
| Above 1.20 | Review range position, tenure and role conditions |

### Benefits cost ratio

```text
Benefits Cost Ratio % = Benefits Cost / Gross Payroll × 100
```

### Total reward

```text
Total Reward = Base Pay + Allowances + Bonus + Employer Benefits
```

---

## ⭐ Performance calculations

### Average performance score

```text
Average Performance Score = Total Performance Score / Evaluated Employees
```

### High-performer rate

```text
High-Performer % = High-Performing Employees / Evaluated Employees × 100
```

### Promotion-readiness rate

```text
Promotion-Ready % = Promotion-Ready Employees / Evaluated Employees × 100
```

Performance scores should support—not replace—managerial review, behavioural evidence, role requirements and fairness checks.

---

## 🦺 Health and safety calculations

### Incident rate

```text
Incident Rate = Number of Incidents / Average Headcount × 100
```

### Lost-time incident rate

```text
Lost-Time Incident Rate = Lost-Time Incidents / Average Headcount × 100
```

### Corrective-action closure rate

```text
Closure Rate % = Closed Corrective Actions / Total Corrective Actions × 100
```

Analyse incident type, location, department, severity, root cause and closure status together.

---

# 🛠️ Tool-specific examples

## 🟩 Excel

Useful functions:

```excel
=COUNTIFS(StatusRange,"Active")
=AVERAGEIFS(TimeToFillRange,StatusRange,"Filled")
=SUMIFS(LeaveDaysRange,DepartmentRange,A2)
=COUNTIFS(PerformanceRange,">=4")/COUNT(PerformanceRange)
```

Recommended workflow:

1. Format each source as an Excel Table.
2. Use Power Query for cleaning and joins.
3. Load repeated calculations to the Data Model.
4. Build PivotTables and PivotCharts.
5. Add slicers for department, location, gender, month and job level.

---

## 🟨 Power BI / DAX

```DAX
Active Headcount =
CALCULATE(
    DISTINCTCOUNT('01_dim_employee_fy2025'[employee_id]),
    '01_dim_employee_fy2025'[employment_status] = "Active at FY2025 year-end"
)
```

```DAX
FY2025 Exits =
DISTINCTCOUNT('06_fact_employee_separations_fy2025'[employee_id])
```

```DAX
Turnover Rate =
DIVIDE([FY2025 Exits], [Average Headcount])
```

```DAX
Average Time to Fill =
AVERAGE('05_fact_recruitment_fy2025'[time_to_fill_days])
```

Use the relationship map and KPI assets under `bi_assets/` and `docs/platforms/power_bi_assets/`.

---

## 🐍 Python

```python
import pandas as pd

employees = pd.read_csv("data/analysis_ready/employee_360_fy2025.csv")

active_headcount = (
    employees["employment_status"]
    .eq("Active at FY2025 year-end")
    .sum()
)

headcount_by_department = (
    employees.groupby("department")["employee_id"]
    .nunique()
    .sort_values(ascending=False)
)

print("Active headcount:", active_headcount)
print(headcount_by_department)
```

Turnover by department:

```python
separations = pd.read_csv(
    "data/bi_ready_csv/06_fact_employee_separations_fy2025.csv"
)

department_exits = (
    separations.groupby("department")["employee_id"]
    .nunique()
    .sort_values(ascending=False)
)

print(department_exits)
```

---

## 🗄️ SQL

Headcount by department:

```sql
SELECT
    department,
    COUNT(DISTINCT employee_id) AS employee_count
FROM employee_360_fy2025
GROUP BY department
ORDER BY employee_count DESC;
```

Average time-to-fill by source:

```sql
SELECT
    recruitment_source,
    COUNT(*) AS requisitions,
    AVG(time_to_fill_days) AS avg_time_to_fill
FROM fact_recruitment_fy2025
WHERE status = 'Filled'
GROUP BY recruitment_source
ORDER BY avg_time_to_fill;
```

---

# 💼 Suggested projects

## 🌱 Beginner

- Excel headcount dashboard
- Department-wise employee profile
- Leave-type analysis
- Recruitment source summary
- Data-quality checklist

## 🚀 Intermediate

- Power BI executive HR dashboard
- Turnover and retention analysis
- Compensation and compa-ratio review
- Training effectiveness study
- SQL HR data mart

## 🧠 Advanced

- Workforce forecasting
- Turnover-risk classification
- Talent segmentation
- Department risk score
- Automated validation and refresh pipeline
- Scenario-based workforce planning

---

## ⚠️ Responsible-use limitations

- The dataset is synthetic and must not be represented as real company information.
- Findings demonstrate analytical methods; they do not prove real-world causation.
- Sensitive HR decisions should never rely on one metric or model alone.
- Protected or personal attributes must not be used for discriminatory decisions.
- Predictive outputs should be reviewed for bias, explainability and operational relevance.
- Medical, safety and performance fields require careful interpretation even in synthetic exercises.

---

## ✅ Recommended final deliverables

A complete portfolio project may include:

1. cleaned analytical dataset;
2. documented data model;
3. validated KPI calculations;
4. interactive dashboard;
5. written management insights;
6. limitations and ethical-use statement;
7. reproducible notebook, SQL script or Python workflow.

---

## 👤 Author

**Musa**  
Human Resources Professional and People Analytics Practitioner, Bangladesh.
