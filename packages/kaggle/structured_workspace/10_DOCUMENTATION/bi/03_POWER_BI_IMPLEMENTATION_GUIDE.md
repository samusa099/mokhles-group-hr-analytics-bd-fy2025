# Power BI Implementation Guide

## 1. Import the BI-ready files

1. Open Power BI Desktop.
2. Select **Home → Get data → Text/CSV**.
3. Import the required files from `data/bi_ready_csv/`.
4. Select **Transform Data** rather than loading immediately.
5. Confirm data types in Power Query.
6. Select **Close & Apply**.

For the complete portfolio, import the dimensions and all required facts. For a
smaller dashboard, import only the tables required by the selected report page.

## 2. Recommended data types

- IDs and keys: Text
- Dates: Date
- Headcount, hires, exits and days: Whole number
- Salary and cost fields: Decimal or fixed decimal
- Rates: Decimal number formatted as percentage
- Ratings and scores: Decimal number

## 3. Build relationships

Open **Model view** and create the relationships listed in:

```text
bi_assets/semantic_model/relationship_map.csv
```

Recommended defaults:

- Cardinality: one-to-many
- Filter direction: single
- Active relationship: yes for the primary date
- Date dimension: mark `00_dim_date` as the date table

## 4. Import the project theme

1. Open the **View** ribbon.
2. Select **Themes → Browse for themes**.
3. Choose:

```text
bi_assets/power_bi/Mokhles_Group_HR_Analytics_Theme.json
```

## 5. Starter DAX measures

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
Total Hires =
SUM('02_fact_monthly_hr_kpi_fy2025'[hires])
```

```DAX
Average Time to Fill =
AVERAGE('05_fact_recruitment_fy2025'[time_to_fill_days])
```

```DAX
Training Hours =
SUM('09_fact_training_development_fy2025'[hours])
```

```DAX
Training Completion Rate =
DIVIDE(
    CALCULATE(
        COUNTROWS('09_fact_training_development_fy2025'),
        '09_fact_training_development_fy2025'[completion_status] = "Completed"
    ),
    COUNTROWS('09_fact_training_development_fy2025')
)
```

```DAX
Average Performance Score =
AVERAGE('11_fact_performance_evaluation_fy2025'[overall_score])
```

```DAX
Female Representation =
DIVIDE(
    CALCULATE(
        DISTINCTCOUNT('01_dim_employee_fy2025'[employee_id]),
        '01_dim_employee_fy2025'[gender] = "Female",
        '01_dim_employee_fy2025'[employment_status] = "Active at FY2025 year-end"
    ),
    [Active Headcount]
)
```

```DAX
Monthly Gross Payroll =
SUM('10_fact_compensation_benefits_fy2025'[monthly_gross])
```

## 6. Recommended report pages

Use `10_DASHBOARD_BLUEPRINT.md` for the six-page layout.

## 7. Publish and refresh

Publish the `.pbix` to the appropriate Power BI workspace. Refresh options
depend on where the source files are stored. For maintainable refreshes, store
the source in OneDrive, SharePoint, Fabric, or another supported governed
location rather than relying on an unmanaged local path.

## Official references

- Connect to data:
  https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-connect-to-data
- Text/CSV connector:
  https://learn.microsoft.com/en-us/power-query/connectors/text-csv
- Create and manage relationships:
  https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships
