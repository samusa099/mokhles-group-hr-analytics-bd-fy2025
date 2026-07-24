# Complete File Information

Every published project file is documented below.

## `00_START_HERE/FOLDER_MAP.md`

Visual map of the professional structured analytics workspace.

## `00_START_HERE/README_START_HERE.md`

Primary navigation guide for choosing the correct data and platform workflow.

## `00_START_HERE/platform_readiness_matrix.csv`

Cross-platform readiness matrix for Power BI, Excel, Looker Studio, Tableau, Qlik Sense and Metabase.

## `01_SOURCE_DATA/csv_original/01_Employee_Master_FY2025.csv`

Year-end synthetic employee master records for workforce composition, headcount, tenure, organisational structure and salary analysis.

## `01_SOURCE_DATA/csv_original/02_Monthly_HR_KPI_FY2025.csv`

Monthly FY2025 HR indicators covering headcount movement, turnover, absence, overtime, training, payroll, vacancies and engagement.

## `01_SOURCE_DATA/csv_original/03_Department_Annual_Summary_FY2025.csv`

Annual department-level HR summary covering headcount, hiring, exits, turnover, absence, training and average performance.

## `01_SOURCE_DATA/csv_original/04_Quarterly_Board_KPI_FY2025.csv`

Quarterly strategic HR indicators prepared for executive and board-level workforce review.

## `01_SOURCE_DATA/csv_original/05_Recruitment_Master_FY2025.csv`

Recruitment requisitions and candidate-funnel records covering applications, interviews, offers, hires, time-to-fill and recruitment cost.

## `01_SOURCE_DATA/csv_original/06_Employee_Separations_FY2025.csv`

Employee turnover records covering exit dates, exit types, reasons, tenure at exit and regrettable separation status.

## `01_SOURCE_DATA/csv_original/07_Leave_Transactions_FY2025.csv`

Employee leave and absence transactions covering leave categories, dates, duration, reasons and approval status.

## `01_SOURCE_DATA/csv_original/08_Diversity_Inclusion_Master_FY2025.csv`

Workforce diversity records covering gender, age, disability status, education, job level, location and Bangladesh division of origin.

## `01_SOURCE_DATA/csv_original/09_Training_Development_Master_FY2025.csv`

Employee-level training participation records covering programmes, hours, completion, assessments, feedback and learning cost.

## `01_SOURCE_DATA/csv_original/10_Compensation_Benefits_Master_FY2025.csv`

Employee compensation and total-reward records covering salary, allowances, bonus, provident fund, gratuity, insurance and compa-ratio.

## `01_SOURCE_DATA/csv_original/11_Performance_Evaluation_Master_FY2025.csv`

Employee performance records covering goal completion, competency, ratings, potential, readiness and development priorities.

## `01_SOURCE_DATA/csv_original/12_Health_Safety_Master_FY2025.csv`

Health and safety records covering incidents, lost-time injuries, days lost, root causes, corrective actions and closure status.

## `01_SOURCE_DATA/csv_original/13_Data_Dictionary_FY2025.csv`

Field-level definitions, data types and source lineage for the consolidated Mokhles Group HR analytics dataset.

## `01_SOURCE_DATA/excel_master/Mokhles_Group_HR_Analytics_Master_Dataset_FY2025.xlsx`

Consolidated master Excel workbook with an executive dashboard, 12 analytical data sheets and a data dictionary.

## `01_SOURCE_DATA/excel_reports/01_Mokhles_Group_Headcount_Analytics_Report_FY2025.xlsx`

Excel headcount dashboard and employee snapshot for workforce structure, tenure and location analysis.

## `01_SOURCE_DATA/excel_reports/02_Mokhles_Group_Monthly_HR_Analytics_Report_FY2025.xlsx`

Excel monthly HR dashboard covering workforce movement, absence, payroll, training, vacancies and engagement.

## `01_SOURCE_DATA/excel_reports/03_Mokhles_Group_Annual_HR_Analytics_Report_FY2025.xlsx`

Excel annual HR dashboard covering executive KPIs, department outcomes and strategic HR initiatives.

## `01_SOURCE_DATA/excel_reports/04_Mokhles_Group_Board_HR_Analytics_Report_FY2025.xlsx`

Excel board-level HR report covering quarterly KPIs, workforce risks and governance actions.

## `01_SOURCE_DATA/excel_reports/05_Mokhles_Group_Recruitment_Analytics_Report_FY2025.xlsx`

Excel recruitment dashboard covering candidate funnels, time-to-fill, hiring sources and recruitment cost.

## `01_SOURCE_DATA/excel_reports/06_Mokhles_Group_Turnover_Retention_Analytics_Report_FY2025.xlsx`

Excel turnover and retention dashboard covering exit reasons, regrettable exits and department retention.

## `01_SOURCE_DATA/excel_reports/07_Mokhles_Group_Absence_Leave_Analytics_Report_FY2025.xlsx`

Excel leave and absence dashboard covering leave type, duration, frequency and department patterns.

## `01_SOURCE_DATA/excel_reports/08_Mokhles_Group_Diversity_Inclusion_Analytics_Report_FY2025.xlsx`

Excel diversity and inclusion dashboard covering gender, age, disability, education and geographic representation.

## `01_SOURCE_DATA/excel_reports/09_Mokhles_Group_Learning_Development_Analytics_Report_FY2025.xlsx`

Excel learning and development dashboard covering participation, completion, assessments, hours and cost.

## `01_SOURCE_DATA/excel_reports/10_Mokhles_Group_Compensation_Benefits_Analytics_Report_FY2025.xlsx`

Excel compensation dashboard covering salary, benefits, total reward, compa-ratio and pay-equity indicators.

## `01_SOURCE_DATA/excel_reports/11_Mokhles_Group_Performance_Analytics_Report_FY2025.xlsx`

Excel performance dashboard covering ratings, potential, promotion readiness and development needs.

## `01_SOURCE_DATA/excel_reports/12_Mokhles_Group_Health_Safety_Analytics_Report_FY2025.xlsx`

Excel health and safety dashboard covering incidents, lost time, root causes and corrective-action closure.

## `02_CLEAN_DATA/analysis_ready/department_360_summary_fy2025.csv`

Consolidated one-row-per-department summary for executive and Looker Studio analysis.

## `02_CLEAN_DATA/analysis_ready/employee_360_fy2025.csv`

Consolidated one-row-per-employee analytical table combining workforce, diversity, compensation, performance, leave, training and separation attributes.

## `02_CLEAN_DATA/bi_ready_csv/00_dim_date.csv`

Reusable calendar dimension covering every date found across the HR portfolio.

## `02_CLEAN_DATA/bi_ready_csv/00_dim_department.csv`

Department lookup dimension with normalized keys and cost-center mapping.

## `02_CLEAN_DATA/bi_ready_csv/00_dim_location.csv`

Work-location lookup dimension with normalized relationship keys.

## `02_CLEAN_DATA/bi_ready_csv/01_dim_employee_fy2025.csv`

Unified employee dimension containing 456 year-end employees and 60 FY2025 separations.

## `02_CLEAN_DATA/bi_ready_csv/02_fact_monthly_hr_kpi_fy2025.csv`

BI-ready normalized version of 02_Monthly_HR_KPI_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

## `02_CLEAN_DATA/bi_ready_csv/03_fact_department_annual_summary_fy2025.csv`

BI-ready normalized version of 03_Department_Annual_Summary_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

## `02_CLEAN_DATA/bi_ready_csv/04_fact_quarterly_board_kpi_fy2025.csv`

BI-ready normalized version of 04_Quarterly_Board_KPI_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

## `02_CLEAN_DATA/bi_ready_csv/05_fact_recruitment_fy2025.csv`

BI-ready normalized version of 05_Recruitment_Master_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

## `02_CLEAN_DATA/bi_ready_csv/06_fact_employee_separations_fy2025.csv`

BI-ready normalized version of 06_Employee_Separations_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

## `02_CLEAN_DATA/bi_ready_csv/07_fact_leave_transactions_fy2025.csv`

BI-ready normalized version of 07_Leave_Transactions_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

## `02_CLEAN_DATA/bi_ready_csv/08_dim_diversity_inclusion_fy2025.csv`

BI-ready normalized version of 08_Diversity_Inclusion_Master_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

## `02_CLEAN_DATA/bi_ready_csv/09_fact_training_development_fy2025.csv`

BI-ready normalized version of 09_Training_Development_Master_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

## `02_CLEAN_DATA/bi_ready_csv/10_fact_compensation_benefits_fy2025.csv`

BI-ready normalized version of 10_Compensation_Benefits_Master_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

## `02_CLEAN_DATA/bi_ready_csv/11_fact_performance_evaluation_fy2025.csv`

BI-ready normalized version of 11_Performance_Evaluation_Master_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

## `02_CLEAN_DATA/bi_ready_csv/12_fact_health_safety_fy2025.csv`

BI-ready normalized version of 12_Health_Safety_Master_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

## `02_CLEAN_DATA/data_quality/column_profile.csv`

Column-level profile covering inferred types, blanks, distinct values, ranges and examples.

## `02_CLEAN_DATA/data_quality/table_quality_summary.csv`

Table-level data-quality profile covering row counts, blanks, duplicate rows and key checks.

## `02_CLEAN_DATA/data_quality/validation_rules.csv`

Reusable data-quality validation rules for Excel, Power BI, Looker Studio and relational modeling.

## `03_POWER_BI/README_POWER_BI.md`

Power BI setup guide covering parameters, Power Query, relationships, theme, DAX and refresh.

## `03_POWER_BI/dax/Mokhles_Group_HR_Starter_Measures.dax`

Starter DAX measure library for workforce, recruitment, turnover, payroll, learning, performance and diversity.

## `03_POWER_BI/power_query_m/00_PROJECT_ROOT_PARAMETER.md`

Instructions for creating the reusable ProjectRoot text parameter in Power BI.

## `03_POWER_BI/power_query_m/00_dim_date.m`

Power Query M template for loading `00_dim_date.csv` through the ProjectRoot parameter.

## `03_POWER_BI/power_query_m/00_dim_department.m`

Power Query M template for loading `00_dim_department.csv` through the ProjectRoot parameter.

## `03_POWER_BI/power_query_m/00_dim_location.m`

Power Query M template for loading `00_dim_location.csv` through the ProjectRoot parameter.

## `03_POWER_BI/power_query_m/01_dim_employee_fy2025.m`

Power Query M template for loading `01_dim_employee_fy2025.csv` through the ProjectRoot parameter.

## `03_POWER_BI/power_query_m/02_fact_monthly_hr_kpi_fy2025.m`

Power Query M template for loading `02_fact_monthly_hr_kpi_fy2025.csv` through the ProjectRoot parameter.

## `03_POWER_BI/power_query_m/03_fact_department_annual_summary_fy2025.m`

Power Query M template for loading `03_fact_department_annual_summary_fy2025.csv` through the ProjectRoot parameter.

## `03_POWER_BI/power_query_m/04_fact_quarterly_board_kpi_fy2025.m`

Power Query M template for loading `04_fact_quarterly_board_kpi_fy2025.csv` through the ProjectRoot parameter.

## `03_POWER_BI/power_query_m/05_fact_recruitment_fy2025.m`

Power Query M template for loading `05_fact_recruitment_fy2025.csv` through the ProjectRoot parameter.

## `03_POWER_BI/power_query_m/06_fact_employee_separations_fy2025.m`

Power Query M template for loading `06_fact_employee_separations_fy2025.csv` through the ProjectRoot parameter.

## `03_POWER_BI/power_query_m/07_fact_leave_transactions_fy2025.m`

Power Query M template for loading `07_fact_leave_transactions_fy2025.csv` through the ProjectRoot parameter.

## `03_POWER_BI/power_query_m/08_dim_diversity_inclusion_fy2025.m`

Power Query M template for loading `08_dim_diversity_inclusion_fy2025.csv` through the ProjectRoot parameter.

## `03_POWER_BI/power_query_m/09_fact_training_development_fy2025.m`

Power Query M template for loading `09_fact_training_development_fy2025.csv` through the ProjectRoot parameter.

## `03_POWER_BI/power_query_m/10_fact_compensation_benefits_fy2025.m`

Power Query M template for loading `10_fact_compensation_benefits_fy2025.csv` through the ProjectRoot parameter.

## `03_POWER_BI/power_query_m/11_fact_performance_evaluation_fy2025.m`

Power Query M template for loading `11_fact_performance_evaluation_fy2025.csv` through the ProjectRoot parameter.

## `03_POWER_BI/power_query_m/12_fact_health_safety_fy2025.m`

Power Query M template for loading `12_fact_health_safety_fy2025.csv` through the ProjectRoot parameter.

## `03_POWER_BI/semantic_model/dashboard_blueprint.csv`

Machine-readable six-page dashboard design plan.

## `03_POWER_BI/semantic_model/field_name_mapping.csv`

Maps original business-friendly fields to BI-ready snake_case fields.

## `03_POWER_BI/semantic_model/kpi_catalog.csv`

Canonical HR KPI definitions and preferred source fields.

## `03_POWER_BI/semantic_model/relationship_map.csv`

Cross-platform relationship implementation checklist.

## `03_POWER_BI/theme/Mokhles_Group_HR_Analytics_Theme.json`

Reusable corporate theme for Power BI reports.

## `04_EXCEL_ANALYTICS/Employee_360_Power_Query.m`

Excel Power Query M template for importing the employee 360 table through a named ProjectRoot cell.

## `04_EXCEL_ANALYTICS/Mokhles_Group_Excel_Analytics_Starter_v2_3_0.xlsx`

Professional Excel starter workbook containing platform matrix, data-quality review, relationship map, KPI catalogue and PivotTable blueprint.

## `04_EXCEL_ANALYTICS/README_EXCEL_ANALYTICS.md`

Excel Power Query, Power Pivot, PivotTable and data-cleaning workflow guide.

## `04_EXCEL_ANALYTICS/templates/dashboard_blueprint.csv`

Excel analytics template copied from the shared semantic-model assets.

## `04_EXCEL_ANALYTICS/templates/field_name_mapping.csv`

Excel analytics template copied from the shared semantic-model assets.

## `04_EXCEL_ANALYTICS/templates/kpi_catalog.csv`

Excel analytics template copied from the shared semantic-model assets.

## `04_EXCEL_ANALYTICS/templates/relationship_map.csv`

Excel analytics template copied from the shared semantic-model assets.

## `05_LOOKER_STUDIO/README_LOOKER_STUDIO.md`

Looker Studio CSV upload, data-source and dashboard setup guide.

## `05_LOOKER_STUDIO/calculated_fields.md`

Starter Looker Studio calculated-field formulas for major HR KPIs.

## `05_LOOKER_STUDIO/data_source_map.csv`

Mapping of recommended Looker Studio data sources, grains, keys, dates and dashboard uses.

## `05_LOOKER_STUDIO/upload_ready_csv/00_dim_date.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/00_dim_department.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/00_dim_location.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/01_dim_employee_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/02_fact_monthly_hr_kpi_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/03_fact_department_annual_summary_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/04_fact_quarterly_board_kpi_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/05_fact_recruitment_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/06_fact_employee_separations_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/07_fact_leave_transactions_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/08_dim_diversity_inclusion_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/09_fact_training_development_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/10_fact_compensation_benefits_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/11_fact_performance_evaluation_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/12_fact_health_safety_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/department_360_summary_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `05_LOOKER_STUDIO/upload_ready_csv/employee_360_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

## `06_TABLEAU/README_TABLEAU.md`

Tableau relationship-based multi-table modeling guide.

## `06_TABLEAU/relationship_map.csv`

Relationship map copied for direct Tableau implementation.

## `07_QLIK/Mokhles_HR_Load_Script.qvs`

Qlik Sense load script for importing the BI-ready CSV tables.

## `07_QLIK/README_QLIK.md`

Qlik Sense folder connection and associative-model guidance.

## `08_METABASE/README_METABASE.md`

Metabase CSV upload, type review and maintained database workflow guide.

## `09_NOTEBOOKS/Mokhles_HR_Analytics_EDA.ipynb`

Exploratory Python notebook covering headcount, recruitment, turnover, compensation, learning, performance and safety.

## `10_DOCUMENTATION/13_Data_Dictionary_FY2025.csv`

Documented project data dictionary.

## `10_DOCUMENTATION/ABOUT_DATASET.md`

Publication-ready dataset overview, analytical coverage and synthetic-data statement.

## `10_DOCUMENTATION/COLUMN_DESCRIPTIONS_COMPLETE.md`

Complete human-readable backup of CSV field names, data types and descriptions.

## `10_DOCUMENTATION/CURRENT_OFFICIAL_REFERENCES.md`

Current official documentation references used to design the platform-specific project structure.

## `10_DOCUMENTATION/DATA_DICTIONARY.md`

Readable field-level data dictionary for the 13 analysis-ready CSV tables.

## `10_DOCUMENTATION/DATA_ETHICS.md`

Privacy, ethical-use and interpretation limitations for the synthetic records.

## `10_DOCUMENTATION/FILE_CATALOG.md`

File inventory with dimensions and workbook descriptions.

## `10_DOCUMENTATION/FILE_INFORMATION_COMPLETE.md`

Complete human-readable file catalogue for the structured analytics workspace.

## `10_DOCUMENTATION/KAGGLE_DATASET_DESCRIPTION.md`

Kaggle-facing description of project scope, analytics assets and synthetic-data ethics.

## `10_DOCUMENTATION/PYTHON_TO_POWER_BI_WORKFLOW.md`

Step-by-step Windows PowerShell and Power BI workflow for generating, validating, importing and refreshing the BI-ready layer.

## `10_DOCUMENTATION/USAGE_GUIDE.md`

Quick instructions for using the package in Kaggle, Python and Excel.

## `10_DOCUMENTATION/bi/00_BI_START_HERE.md`

Entry point for choosing a BI platform, source files and recommended learning order.

## `10_DOCUMENTATION/bi/01_CROSS_PLATFORM_COMPATIBILITY.md`

Compatibility matrix for Power BI, Looker Studio, Tableau, Qlik Sense, Excel Power Query and Metabase.

## `10_DOCUMENTATION/bi/02_DATA_MODEL_AND_RELATIONSHIPS.md`

Recommended dimensional model, keys and relationship guidance.

## `10_DOCUMENTATION/bi/03_POWER_BI_IMPLEMENTATION_GUIDE.md`

Power BI import, Power Query, relationships, theme and starter DAX guide.

## `10_DOCUMENTATION/bi/04_LOOKER_STUDIO_IMPLEMENTATION_GUIDE.md`

Looker Studio CSV upload, calculated fields, blending and report-page guidance.

## `10_DOCUMENTATION/bi/05_TABLEAU_IMPLEMENTATION_GUIDE.md`

Tableau CSV connection, logical relationships and calculated fields.

## `10_DOCUMENTATION/bi/06_QLIK_SENSE_IMPLEMENTATION_GUIDE.md`

Qlik Data Manager, associations and master-measure guidance.

## `10_DOCUMENTATION/bi/07_EXCEL_POWER_QUERY_GUIDE.md`

Excel Power Query, Data Model and Power Pivot implementation guide.

## `10_DOCUMENTATION/bi/08_METABASE_IMPLEMENTATION_GUIDE.md`

Metabase CSV upload and database-backed implementation guidance.

## `10_DOCUMENTATION/bi/09_KPI_FORMULA_LIBRARY.md`

Cross-platform definitions for the primary HR KPIs.

## `10_DOCUMENTATION/bi/10_DASHBOARD_BLUEPRINT.md`

Six-page HR dashboard architecture with recommended visuals and filters.

## `11_KAGGLE_METADATA/column-metadata-coverage.json`

Coverage report for file descriptions, CSV schemas, field descriptions, tags and cover image.

## `11_KAGGLE_METADATA/file-manifest.json`

Complete structured-workspace file manifest with sizes and SHA-256 checksums.

## `11_KAGGLE_METADATA/project-metadata.json`

Structured project metadata covering release, ownership, content and supported analytics platforms.

## `12_SCRIPTS/build_analysis_ready.py`

Python script for rebuilding the employee 360 analysis-ready table.

## `12_SCRIPTS/build_bi_ready_layer.py`

Python utility that regenerates the complete 15-table BI-ready layer from the authoritative HR CSV files.

## `12_SCRIPTS/profile_data.py`

Python script for generating basic table-level quality profiles.

## `12_SCRIPTS/validate_workspace.py`

Python validation script for files, metadata, CSV schemas and descriptions.

## `LICENSE`

Creative Commons Attribution 4.0 licence for the dataset and documentation.

## `README.md`

Package overview, folder map, dataset scale and synthetic-data notice.

## `dataset-cover-image.png`

Project asset included in the structured HR analytics workspace.

## `requirements.txt`

Python dependency list for reproducing the exploratory notebook.
