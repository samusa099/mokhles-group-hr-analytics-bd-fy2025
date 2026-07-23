# Excel and Power Query Guide

## Option A: Use the existing Excel portfolio

Open the consolidated master workbook or any specialised workbook from:

```text
data/excel/
```

This is the fastest route for reviewing the existing dashboards and tables.

## Option B: Import a single CSV

1. Open Excel.
2. Select **Data → Get Data → From File → From Text/CSV**.
3. Select an original or BI-ready CSV.
4. Choose **Transform Data**.
5. Set data types and clean values.
6. Select **Close & Load**.

## Option C: Use the Excel Data Model

Load the dimension and fact tables as connections and add them to the Data
Model. Create relationships using the relationship map.

## Folder import warning

The **From Folder** feature is designed to combine files that share the same
schema. The HR portfolio contains different tables with different structures,
so do not combine the entire CSV folder into one table.

Use From Folder only when combining repeated monthly files of the same table.

## Recommended Power Pivot measures

```DAX
Active Headcount :=
CALCULATE(
    DISTINCTCOUNT(Employees[employee_id]),
    Employees[employment_status] = "Active at FY2025 year-end"
)
```

```DAX
Training Hours :=
SUM(Training[hours])
```

## Official references

- Import and combine folder files:
  https://support.microsoft.com/en-us/excel/import-data-from-a-folder-with-multiple-files-power-query
- Text/CSV connector:
  https://learn.microsoft.com/en-us/power-query/connectors/text-csv
