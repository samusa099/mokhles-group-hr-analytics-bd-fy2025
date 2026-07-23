# Excel Data Cleaning, Analysis and Analytics Guide

## Recommended workflow

1. Open `Mokhles_Group_Excel_Analytics_Starter.xlsx`.
2. Review the Table Inventory and Data Quality Summary sheets.
3. In Excel, select **Data → Get Data → From File → From Folder**.
4. Point Power Query to one specific data folder.
5. Select **Transform Data** before combining files.
6. Filter by Folder Path and Extension.
7. Combine only files that have the same schema.
8. Load cleaned tables to the Data Model.
9. Create relationships using the Relationship Map.
10. Build PivotTables and PivotCharts using the Pivot Blueprint.

## Folder choices

- Original data: `01_SOURCE_DATA/csv_original`
- Clean analytical data: `02_CLEAN_DATA/bi_ready_csv`
- Employee-level analysis: `02_CLEAN_DATA/analysis_ready/employee_360_fy2025.csv`
- Department-level analysis: `02_CLEAN_DATA/analysis_ready/department_360_summary_fy2025.csv`

Official references:

- https://learn.microsoft.com/en-us/power-query/connectors/folder
- https://learn.microsoft.com/en-us/power-query/combine-files-overview
