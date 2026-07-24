# Complete CSV Column Descriptions

This document mirrors the CSV schemas published in dataset-metadata.json.

## `00_START_HERE/platform_readiness_matrix.csv`

Cross-platform readiness matrix for Power BI, Excel, Looker Studio, Tableau, Qlik Sense and Metabase.

| Column | Type | Description |
|---|---|---|
| `platform` | `string` | Analytics or BI platform. |
| `recommended_source` | `string` | Recommended project source folder. |
| `primary_method` | `string` | Preferred connection or import method. |
| `best_for` | `string` | Primary analytical use case. |
| `important_note` | `string` | Platform-specific implementation note. |

## `01_SOURCE_DATA/csv_original/01_Employee_Master_FY2025.csv`

Year-end synthetic employee master records for workforce composition, headcount, tenure, organisational structure and salary analysis.

| Column | Type | Description |
|---|---|---|
| `Employee ID` | `id` | Unique synthetic employee identifier used consistently across the master datasets. |
| `Employee Name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. |
| `Gender` | `string` | Synthetic gender category used for workforce representation analysis. |
| `Age` | `integer` | Employee age as of the reporting snapshot. |
| `Age Band` | `string` | Grouped employee age range used for demographic analysis. |
| `Division of Origin` | `string` | Synthetic administrative division of Bangladesh associated with the employee. |
| `Disability Status` | `string` | Synthetic self-declared disability indicator used only for inclusion analysis. |
| `Education` | `string` | Highest synthetic education level recorded for the employee. |
| `Department` | `string` | Organisational department assigned to the employee or record. |
| `Cost Center` | `numeric` | Synthetic finance and workforce cost-centre code. |
| `Job Title` | `string` | Employee position title within Mokhles Group. |
| `Job Level` | `string` | Organisational grade or hierarchy level. |
| `Employment Type` | `string` | Employment arrangement such as permanent, contract, probation or intern. |
| `Location` | `string` | Mokhles Group operating site or office in Bangladesh. |
| `Join Date` | `datetime` | Employee's synthetic employment start date. |
| `Tenure (Years)` | `numeric` | Length of service in years at the reporting date. |
| `Manager` | `string` | Fictional line manager associated with the employee. |
| `Monthly Gross` | `numeric` | Monthly gross compensation in Bangladeshi Taka. |

## `01_SOURCE_DATA/csv_original/02_Monthly_HR_KPI_FY2025.csv`

Monthly FY2025 HR indicators covering headcount movement, turnover, absence, overtime, training, payroll, vacancies and engagement.

| Column | Type | Description |
|---|---|---|
| `Month` | `datetime` | Reporting month within FY2025. |
| `Opening Headcount` | `integer` | Employees active on the first day of the reporting period. |
| `Hires` | `integer` | Number of employees hired during the reporting period. |
| `Exits` | `integer` | Number of employee separations during the reporting period. |
| `Closing Headcount` | `integer` | Employees active on the last day of the reporting period. |
| `Average Headcount` | `numeric` | Average of opening and closing headcount. |
| `Turnover Rate` | `numeric` | Employee exits divided by average headcount. |
| `Approved Absence Days` | `integer` | Synthetic approved absence days field used in the Monthly HR KPI dataset. |
| `Absence Rate` | `numeric` | Approved absence days divided by estimated available workdays. |
| `Overtime Hours` | `integer` | Synthetic overtime hours field used in the Monthly HR KPI dataset. |
| `Training Hours` | `integer` | Synthetic training hours field used in the Monthly HR KPI dataset. |
| `Payroll Cost (BDT)` | `numeric` | Total monthly gross payroll cost in Bangladeshi Taka. |
| `Open Vacancies` | `integer` | Synthetic open vacancies field used in the Monthly HR KPI dataset. |
| `Average Time to Fill (Days)` | `numeric` | Synthetic average time to fill (days) field used in the Monthly HR KPI dataset. |
| `Engagement Pulse (1-5)` | `numeric` | Synthetic engagement pulse (1-5) field used in the Monthly HR KPI dataset. |

## `01_SOURCE_DATA/csv_original/03_Department_Annual_Summary_FY2025.csv`

Annual department-level HR summary covering headcount, hiring, exits, turnover, absence, training and average performance.

| Column | Type | Description |
|---|---|---|
| `Department` | `string` | Organisational department assigned to the employee or record. |
| `Opening Headcount` | `integer` | Employees active on the first day of the reporting period. |
| `Hires` | `integer` | Number of employees hired during the reporting period. |
| `Exits` | `integer` | Number of employee separations during the reporting period. |
| `Closing Headcount` | `integer` | Employees active on the last day of the reporting period. |
| `Average Headcount` | `numeric` | Average of opening and closing headcount. |
| `Turnover Rate` | `numeric` | Employee exits divided by average headcount. |
| `Approved Absence Days` | `integer` | Synthetic approved absence days field used in the Department Annual dataset. |
| `Training Hours` | `integer` | Synthetic training hours field used in the Department Annual dataset. |
| `Average Performance Score` | `numeric` | Synthetic average performance score field used in the Department Annual dataset. |

## `01_SOURCE_DATA/csv_original/04_Quarterly_Board_KPI_FY2025.csv`

Quarterly strategic HR indicators prepared for executive and board-level workforce review.

| Column | Type | Description |
|---|---|---|
| `Quarter` | `string` | Synthetic quarter field used in the Quarterly Board KPI dataset. |
| `Closing Headcount` | `integer` | Employees active on the last day of the reporting period. |
| `Hires` | `integer` | Number of employees hired during the reporting period. |
| `Exits` | `integer` | Number of employee separations during the reporting period. |
| `Turnover Rate` | `numeric` | Employee exits divided by average headcount. |
| `Payroll Cost (BDT)` | `numeric` | Total monthly gross payroll cost in Bangladeshi Taka. |
| `Absence Rate` | `numeric` | Approved absence days divided by estimated available workdays. |
| `Training Hours` | `integer` | Synthetic training hours field used in the Quarterly Board KPI dataset. |
| `Female Representation` | `numeric` | Synthetic female representation field used in the Quarterly Board KPI dataset. |
| `Engagement Pulse` | `numeric` | Synthetic engagement pulse field used in the Quarterly Board KPI dataset. |
| `Open Vacancies` | `integer` | Synthetic open vacancies field used in the Quarterly Board KPI dataset. |

## `01_SOURCE_DATA/csv_original/05_Recruitment_Master_FY2025.csv`

Recruitment requisitions and candidate-funnel records covering applications, interviews, offers, hires, time-to-fill and recruitment cost.

| Column | Type | Description |
|---|---|---|
| `Requisition ID` | `id` | Unique synthetic recruitment requisition identifier. |
| `Department` | `string` | Organisational department assigned to the employee or record. |
| `Location` | `string` | Mokhles Group operating site or office in Bangladesh. |
| `Job Title` | `string` | Employee position title within Mokhles Group. |
| `Job Level` | `string` | Organisational grade or hierarchy level. |
| `Hiring Manager` | `string` | Synthetic hiring manager field used in the Recruitment Master dataset. |
| `Posted Date` | `datetime` | Synthetic posted date field used in the Recruitment Master dataset. |
| `Target Close Date` | `datetime` | Planned date for closing the corrective action. |
| `Actual Close Date` | `datetime` | Synthetic actual close date field used in the Recruitment Master dataset. |
| `Status` | `string` | Current workflow status of the record. |
| `Planned Vacancies` | `integer` | Synthetic planned vacancies field used in the Recruitment Master dataset. |
| `Applications` | `integer` | Number of applications received for the requisition. |
| `Shortlisted` | `integer` | Number of candidates selected for initial consideration. |
| `Interviewed` | `integer` | Number of candidates interviewed. |
| `Offers` | `integer` | Number of employment offers issued. |
| `Hires` | `integer` | Number of employees hired during the reporting period. |
| `Primary Source` | `string` | Synthetic primary source field used in the Recruitment Master dataset. |
| `Time to Fill (Days)` | `integer` | Calendar days from requisition posting to closure. |
| `Recruitment Cost (BDT)` | `numeric` | Synthetic recruitment expenditure in Bangladeshi Taka. |
| `Candidate Experience Score` | `numeric` | Synthetic candidate feedback score on a 1–5 scale. |

## `01_SOURCE_DATA/csv_original/06_Employee_Separations_FY2025.csv`

Employee turnover records covering exit dates, exit types, reasons, tenure at exit and regrettable separation status.

| Column | Type | Description |
|---|---|---|
| `Employee ID` | `id` | Unique synthetic employee identifier used consistently across the master datasets. |
| `Employee Name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. |
| `Gender` | `string` | Synthetic gender category used for workforce representation analysis. |
| `Department` | `string` | Organisational department assigned to the employee or record. |
| `Job Title` | `string` | Employee position title within Mokhles Group. |
| `Job Level` | `string` | Organisational grade or hierarchy level. |
| `Location` | `string` | Mokhles Group operating site or office in Bangladesh. |
| `Join Date` | `datetime` | Employee's synthetic employment start date. |
| `Exit Date` | `datetime` | Employee separation date. |
| `Tenure at Exit (Years)` | `numeric` | Synthetic tenure at exit (years) field used in the Employee Separations dataset. |
| `Exit Type` | `string` | Voluntary or involuntary separation classification. |
| `Exit Reason` | `string` | Primary synthetic reason for employee separation. |
| `Regrettable Exit` | `string` | Indicator for a strategically undesirable employee departure. |
| `Manager` | `string` | Fictional line manager associated with the employee. |

## `01_SOURCE_DATA/csv_original/07_Leave_Transactions_FY2025.csv`

Employee leave and absence transactions covering leave categories, dates, duration, reasons and approval status.

| Column | Type | Description |
|---|---|---|
| `Leave ID` | `id` | Unique synthetic leave transaction identifier. |
| `Employee ID` | `id` | Unique synthetic employee identifier used consistently across the master datasets. |
| `Employee Name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. |
| `Department` | `string` | Organisational department assigned to the employee or record. |
| `Location` | `string` | Mokhles Group operating site or office in Bangladesh. |
| `Leave Type` | `string` | Category of employee leave. |
| `Start Date` | `datetime` | Start date of the leave or programme record. |
| `End Date` | `datetime` | End date of the leave period. |
| `Leave Days` | `integer` | Total leave duration recorded for the transaction. |
| `Reason Category` | `string` | Synthetic reason category field used in the Leave Master dataset. |
| `Approval Status` | `string` | Workflow status of the leave request. |
| `Approved By` | `string` | Synthetic approved by field used in the Leave Master dataset. |

## `01_SOURCE_DATA/csv_original/08_Diversity_Inclusion_Master_FY2025.csv`

Workforce diversity records covering gender, age, disability status, education, job level, location and Bangladesh division of origin.

| Column | Type | Description |
|---|---|---|
| `Employee ID` | `id` | Unique synthetic employee identifier used consistently across the master datasets. |
| `Employee Name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. |
| `Gender` | `string` | Synthetic gender category used for workforce representation analysis. |
| `Age` | `integer` | Employee age as of the reporting snapshot. |
| `Age Band` | `string` | Grouped employee age range used for demographic analysis. |
| `Division of Origin` | `string` | Synthetic administrative division of Bangladesh associated with the employee. |
| `Disability Status` | `string` | Synthetic self-declared disability indicator used only for inclusion analysis. |
| `Education` | `string` | Highest synthetic education level recorded for the employee. |
| `Department` | `string` | Organisational department assigned to the employee or record. |
| `Job Title` | `string` | Employee position title within Mokhles Group. |
| `Job Level` | `string` | Organisational grade or hierarchy level. |
| `Employment Type` | `string` | Employment arrangement such as permanent, contract, probation or intern. |
| `Location` | `string` | Mokhles Group operating site or office in Bangladesh. |

## `01_SOURCE_DATA/csv_original/09_Training_Development_Master_FY2025.csv`

Employee-level training participation records covering programmes, hours, completion, assessments, feedback and learning cost.

| Column | Type | Description |
|---|---|---|
| `Program ID` | `id` | Unique synthetic training programme identifier. |
| `Program Name` | `string` | Name of the learning programme. |
| `Category` | `string` | Synthetic category field used in the Training Master dataset. |
| `Training Date` | `datetime` | Date on which the training programme occurred. |
| `Employee ID` | `id` | Unique synthetic employee identifier used consistently across the master datasets. |
| `Employee Name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. |
| `Department` | `string` | Organisational department assigned to the employee or record. |
| `Job Level` | `string` | Organisational grade or hierarchy level. |
| `Mode` | `string` | Synthetic mode field used in the Training Master dataset. |
| `Provider` | `string` | Synthetic provider field used in the Training Master dataset. |
| `Venue` | `string` | Synthetic venue field used in the Training Master dataset. |
| `Hours` | `integer` | Synthetic hours field used in the Training Master dataset. |
| `Completion Status` | `string` | Whether the employee completed the training. |
| `Pre-Assessment Score` | `numeric` | Synthetic score before training. |
| `Post-Assessment Score` | `numeric` | Synthetic score after training. |
| `Feedback Rating` | `numeric` | Synthetic participant rating on a 1–5 scale. |
| `Cost (BDT)` | `numeric` | Synthetic cost (bdt) field used in the Training Master dataset. |
| `Mandatory` | `string` | Synthetic mandatory field used in the Training Master dataset. |

## `01_SOURCE_DATA/csv_original/10_Compensation_Benefits_Master_FY2025.csv`

Employee compensation and total-reward records covering salary, allowances, bonus, provident fund, gratuity, insurance and compa-ratio.

| Column | Type | Description |
|---|---|---|
| `Employee ID` | `id` | Unique synthetic employee identifier used consistently across the master datasets. |
| `Employee Name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. |
| `Gender` | `string` | Synthetic gender category used for workforce representation analysis. |
| `Department` | `string` | Organisational department assigned to the employee or record. |
| `Location` | `string` | Mokhles Group operating site or office in Bangladesh. |
| `Job Title` | `string` | Employee position title within Mokhles Group. |
| `Job Level` | `string` | Organisational grade or hierarchy level. |
| `Employment Type` | `string` | Employment arrangement such as permanent, contract, probation or intern. |
| `Basic Salary` | `numeric` | Basic monthly salary in Bangladeshi Taka. |
| `House Rent` | `integer` | Monthly house-rent allowance in Bangladeshi Taka. |
| `Medical Allowance` | `numeric` | Monthly medical allowance in Bangladeshi Taka. |
| `Conveyance` | `integer` | Monthly conveyance allowance in Bangladeshi Taka. |
| `Other Allowance` | `numeric` | Additional monthly allowance in Bangladeshi Taka. |
| `Monthly Gross` | `numeric` | Monthly gross compensation in Bangladeshi Taka. |
| `Annual Bonus` | `numeric` | Synthetic annual bonus field used in the Compensation Master dataset. |
| `Monthly Employer PF` | `numeric` | Synthetic monthly employer pf field used in the Compensation Master dataset. |
| `Annual Gratuity Provision` | `numeric` | Synthetic annual gratuity provision field used in the Compensation Master dataset. |
| `Annual Insurance Value` | `numeric` | Synthetic annual insurance value field used in the Compensation Master dataset. |
| `Annual Total Reward` | `numeric` | Annualised salary and synthetic employer-funded benefits. |
| `Compa-Ratio` | `numeric` | Employee monthly gross divided by the synthetic job-level midpoint. |

## `01_SOURCE_DATA/csv_original/11_Performance_Evaluation_Master_FY2025.csv`

Employee performance records covering goal completion, competency, ratings, potential, readiness and development priorities.

| Column | Type | Description |
|---|---|---|
| `Employee ID` | `id` | Unique synthetic employee identifier used consistently across the master datasets. |
| `Employee Name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. |
| `Department` | `string` | Organisational department assigned to the employee or record. |
| `Job Title` | `string` | Employee position title within Mokhles Group. |
| `Job Level` | `string` | Organisational grade or hierarchy level. |
| `Manager` | `string` | Fictional line manager associated with the employee. |
| `Goal Completion (%)` | `numeric` | Synthetic achievement against assigned goals. |
| `Competency Score (1-5)` | `numeric` | Synthetic competency rating on a 1–5 scale. |
| `Attendance Score (%)` | `numeric` | Synthetic attendance score (%) field used in the Performance Master dataset. |
| `Overall Score` | `numeric` | Weighted performance evaluation score. |
| `Performance Rating` | `integer` | Numeric performance rating from 1 to 5. |
| `Rating Label` | `string` | Text label corresponding to the performance rating. |
| `Potential` | `string` | Synthetic talent-potential classification. |
| `Promotion Readiness` | `string` | Indicative readiness category for talent-review practice. |
| `Calibration Status` | `string` | Synthetic calibration status field used in the Performance Master dataset. |
| `Primary Development Area` | `string` | Synthetic primary development area field used in the Performance Master dataset. |

## `01_SOURCE_DATA/csv_original/12_Health_Safety_Master_FY2025.csv`

Health and safety records covering incidents, lost-time injuries, days lost, root causes, corrective actions and closure status.

| Column | Type | Description |
|---|---|---|
| `Incident ID` | `id` | Unique synthetic health and safety record identifier. |
| `Incident Date` | `datetime` | Date of the health and safety record. |
| `Location` | `string` | Mokhles Group operating site or office in Bangladesh. |
| `Department` | `string` | Organisational department assigned to the employee or record. |
| `Incident Type` | `string` | Health and safety incident or observation category. |
| `Severity` | `string` | Synthetic severity classification. |
| `Lost Time Injury` | `string` | Indicates whether the incident resulted in lost workdays. |
| `Days Lost` | `integer` | Number of workdays lost following the incident. |
| `Root Cause` | `string` | Primary synthetic causal factor identified. |
| `Corrective Action` | `string` | Action assigned to reduce recurrence risk. |
| `Responsible Owner` | `string` | Synthetic responsible owner field used in the HSE Master dataset. |
| `Target Close Date` | `datetime` | Planned date for closing the corrective action. |
| `Status` | `string` | Current workflow status of the record. |

## `01_SOURCE_DATA/csv_original/13_Data_Dictionary_FY2025.csv`

Field-level definitions, data types and source lineage for the consolidated Mokhles Group HR analytics dataset.

| Column | Type | Description |
|---|---|---|
| `Master Sheet` | `string` | Name of the consolidated master worksheet containing the documented field. |
| `Field Name` | `string` | Exact column name used in the relevant master dataset. |
| `Definition` | `string` | Business meaning and intended interpretation of the field. |
| `Data Type` | `string` | Human-readable data classification used in the workbook documentation. |
| `Source Workbook` | `string` | Original Excel report from which the field was consolidated. |
| `Original Sheet` | `string` | Original worksheet containing the source field. |

## `02_CLEAN_DATA/analysis_ready/department_360_summary_fy2025.csv`

Consolidated one-row-per-department summary for executive and Looker Studio analysis.

| Column | Type | Description |
|---|---|---|
| `department` | `string` | Department name. |
| `opening_headcount` | `integer` | Opening FY2025 headcount. |
| `hires` | `integer` | FY2025 hires. |
| `exits` | `integer` | FY2025 exits. |
| `closing_headcount` | `integer` | Closing FY2025 headcount. |
| `average_headcount` | `number` | Average FY2025 headcount. |
| `turnover_rate` | `number` | Annual department turnover rate. |
| `approved_absence_days` | `number` | Approved absence days from the annual summary. |
| `training_hours` | `number` | Training hours from the annual department summary. |
| `average_performance_score` | `number` | Average department performance score. |
| `employees_represented` | `integer` | All active and separated employees represented. |
| `active_headcount` | `integer` | Employees active at FY2025 year-end. |
| `female_headcount` | `integer` | Active female employee count. |
| `female_representation_percent` | `number` | Female share of active department headcount. |
| `average_monthly_gross_bdt` | `number` | Average active-employee monthly gross pay in BDT. |
| `annual_total_reward_bdt` | `number` | Total active-employee annual reward value in BDT. |
| `promotion_ready_employees` | `integer` | Employees categorized as promotion ready. |
| `employee_360_training_hours` | `number` | Training hours aggregated from employee records. |
| `employee_360_training_cost_bdt` | `number` | Training cost aggregated from employee records. |
| `employee_360_approved_leave_days` | `number` | Approved leave days aggregated from employee records. |

## `02_CLEAN_DATA/analysis_ready/employee_360_fy2025.csv`

Consolidated one-row-per-employee analytical table combining workforce, diversity, compensation, performance, leave, training and separation attributes.

| Column | Type | Description |
|---|---|---|
| `employee_id` | `string` | Unique synthetic employee identifier. |
| `employee_name` | `string` | Synthetic employee name. |
| `employment_status` | `string` | FY2025 year-end employment status. |
| `gender` | `string` | Employee gender category. |
| `age` | `integer` | Employee age in years where available. |
| `age_band` | `string` | Grouped employee age range. |
| `division_of_origin` | `string` | Bangladesh division associated with employee origin. |
| `disability_status` | `string` | Recorded synthetic disability-status category. |
| `education` | `string` | Highest recorded education category. |
| `department` | `string` | Employee department. |
| `department_key` | `string` | Normalized department relationship key. |
| `cost_center` | `string` | Department cost-center code. |
| `job_title` | `string` | Employee job title. |
| `job_level` | `string` | Employee job level or grade. |
| `employment_type` | `string` | Employment contract category. |
| `location` | `string` | Employee work location. |
| `location_key` | `string` | Normalized location relationship key. |
| `join_date` | `date` | Employee joining date. |
| `exit_date` | `date` | Employee exit date where applicable. |
| `manager` | `string` | Recorded reporting manager. |
| `monthly_gross_bdt` | `number` | Monthly gross compensation in BDT. |
| `annual_total_reward_bdt` | `number` | Annual total reward value in BDT. |
| `compa_ratio` | `number` | Employee compensation position relative to reference pay. |
| `goal_completion_percent` | `number` | Annual goal-completion percentage. |
| `overall_performance_score` | `number` | Overall FY2025 performance score. |
| `performance_rating` | `string` | Performance rating label. |
| `potential` | `string` | Talent-potential category. |
| `promotion_readiness` | `string` | Promotion-readiness category. |
| `leave_transactions` | `integer` | Number of employee leave transactions. |
| `approved_leave_days` | `number` | Total approved leave days. |
| `training_programs` | `integer` | Number of employee training participation records. |
| `training_hours` | `number` | Total training hours. |
| `training_cost_bdt` | `number` | Total allocated training cost in BDT. |
| `average_training_feedback` | `number` | Average training feedback rating. |
| `average_pre_assessment` | `number` | Average pre-training assessment score. |
| `average_post_assessment` | `number` | Average post-training assessment score. |
| `assessment_improvement` | `number` | Difference between average post- and pre-assessment scores. |
| `exit_type` | `string` | Exit type where the employee separated. |
| `exit_reason` | `string` | Recorded separation reason. |
| `regrettable_exit` | `string` | Whether the exit was categorized as regrettable. |
| `tenure_at_exit_years` | `number` | Employee tenure in years at exit. |

## `02_CLEAN_DATA/bi_ready_csv/00_dim_date.csv`

Reusable calendar dimension covering every date found across the HR portfolio.

| Column | Type | Description |
|---|---|---|
| `date_key` | `integer` | Integer date key in YYYYMMDD format. |
| `date` | `date` | Calendar date in ISO YYYY-MM-DD format. |
| `year` | `integer` | Calendar year. |
| `quarter` | `string` | Calendar quarter label from Q1 to Q4. |
| `year_quarter` | `string` | Combined year and quarter label. |
| `month_number` | `integer` | Calendar month number from 1 to 12. |
| `month_name` | `string` | Full English month name. |
| `month_short` | `string` | Three-letter English month name. |
| `year_month` | `string` | Combined year and month in YYYY-MM format. |
| `month_start` | `date` | First date of the calendar month. |
| `week_of_year` | `integer` | Week number within the calendar year. |
| `day_of_month` | `integer` | Day number within the month. |
| `day_name` | `string` | English weekday name. |
| `is_weekend` | `string` | Yes when the date is Saturday or Sunday; otherwise No. |

## `02_CLEAN_DATA/bi_ready_csv/00_dim_department.csv`

Department lookup dimension with normalized keys and cost-center mapping.

| Column | Type | Description |
|---|---|---|
| `department_key` | `string` | Normalized department key suitable for relationships. |
| `department` | `string` | Human-readable department name. |
| `cost_center` | `string` | Department cost-center code. |

## `02_CLEAN_DATA/bi_ready_csv/00_dim_location.csv`

Work-location lookup dimension with normalized relationship keys.

| Column | Type | Description |
|---|---|---|
| `location_key` | `string` | Normalized location key suitable for relationships. |
| `location` | `string` | Human-readable work location. |

## `02_CLEAN_DATA/bi_ready_csv/01_dim_employee_fy2025.csv`

Unified employee dimension containing 456 year-end employees and 60 FY2025 separations.

| Column | Type | Description |
|---|---|---|
| `employee_id` | `string` | Unique synthetic employee identifier across active and separated employees. |
| `employee_name` | `string` | Synthetic employee full name. |
| `gender` | `string` | Synthetic employee gender category. |
| `age` | `integer` | Employee age when available. |
| `age_band` | `string` | Grouped employee age range when available. |
| `division_of_origin` | `string` | Bangladesh division of origin when available. |
| `disability_status` | `string` | Synthetic disability-status category when available. |
| `education` | `string` | Highest recorded educational qualification when available. |
| `department` | `string` | Employee organisational department. |
| `department_key` | `string` | Normalized department relationship key. |
| `cost_center` | `string` | Employee department cost-center code. |
| `job_title` | `string` | Employee job title. |
| `job_level` | `string` | Employee organisational job level. |
| `employment_type` | `string` | Employment arrangement when available. |
| `location` | `string` | Employee work location. |
| `location_key` | `string` | Normalized location relationship key. |
| `join_date` | `date` | Employee joining date. |
| `exit_date` | `date` | Employee separation date when applicable. |
| `employment_status` | `string` | FY2025 active or separated status. |
| `manager` | `string` | Recorded reporting manager. |
| `monthly_gross_bdt` | `number` | Monthly gross compensation in Bangladeshi taka when available. |

## `02_CLEAN_DATA/bi_ready_csv/02_fact_monthly_hr_kpi_fy2025.csv`

BI-ready normalized version of 02_Monthly_HR_KPI_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

| Column | Type | Description |
|---|---|---|
| `month` | `datetime` | Reporting month within FY2025. BI-ready field name uses lowercase snake_case. |
| `opening_headcount` | `integer` | Employees active on the first day of the reporting period. BI-ready field name uses lowercase snake_case. |
| `hires` | `integer` | Number of employees hired during the reporting period. BI-ready field name uses lowercase snake_case. |
| `exits` | `integer` | Number of employee separations during the reporting period. BI-ready field name uses lowercase snake_case. |
| `closing_headcount` | `integer` | Employees active on the last day of the reporting period. BI-ready field name uses lowercase snake_case. |
| `average_headcount` | `numeric` | Average of opening and closing headcount. BI-ready field name uses lowercase snake_case. |
| `turnover_rate` | `numeric` | Employee exits divided by average headcount. BI-ready field name uses lowercase snake_case. |
| `approved_absence_days` | `integer` | Synthetic approved absence days field used in the Monthly HR KPI dataset. BI-ready field name uses lowercase snake_case. |
| `absence_rate` | `numeric` | Approved absence days divided by estimated available workdays. BI-ready field name uses lowercase snake_case. |
| `overtime_hours` | `integer` | Synthetic overtime hours field used in the Monthly HR KPI dataset. BI-ready field name uses lowercase snake_case. |
| `training_hours` | `integer` | Synthetic training hours field used in the Monthly HR KPI dataset. BI-ready field name uses lowercase snake_case. |
| `payroll_cost_bdt` | `numeric` | Total monthly gross payroll cost in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `open_vacancies` | `integer` | Synthetic open vacancies field used in the Monthly HR KPI dataset. BI-ready field name uses lowercase snake_case. |
| `average_time_to_fill_days` | `numeric` | Synthetic average time to fill (days) field used in the Monthly HR KPI dataset. BI-ready field name uses lowercase snake_case. |
| `engagement_pulse_1_5` | `numeric` | Synthetic engagement pulse (1-5) field used in the Monthly HR KPI dataset. BI-ready field name uses lowercase snake_case. |

## `02_CLEAN_DATA/bi_ready_csv/03_fact_department_annual_summary_fy2025.csv`

BI-ready normalized version of 03_Department_Annual_Summary_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

| Column | Type | Description |
|---|---|---|
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `opening_headcount` | `integer` | Employees active on the first day of the reporting period. BI-ready field name uses lowercase snake_case. |
| `hires` | `integer` | Number of employees hired during the reporting period. BI-ready field name uses lowercase snake_case. |
| `exits` | `integer` | Number of employee separations during the reporting period. BI-ready field name uses lowercase snake_case. |
| `closing_headcount` | `integer` | Employees active on the last day of the reporting period. BI-ready field name uses lowercase snake_case. |
| `average_headcount` | `numeric` | Average of opening and closing headcount. BI-ready field name uses lowercase snake_case. |
| `turnover_rate` | `numeric` | Employee exits divided by average headcount. BI-ready field name uses lowercase snake_case. |
| `approved_absence_days` | `integer` | Synthetic approved absence days field used in the Department Annual dataset. BI-ready field name uses lowercase snake_case. |
| `training_hours` | `integer` | Synthetic training hours field used in the Department Annual dataset. BI-ready field name uses lowercase snake_case. |
| `average_performance_score` | `numeric` | Synthetic average performance score field used in the Department Annual dataset. BI-ready field name uses lowercase snake_case. |

## `02_CLEAN_DATA/bi_ready_csv/04_fact_quarterly_board_kpi_fy2025.csv`

BI-ready normalized version of 04_Quarterly_Board_KPI_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

| Column | Type | Description |
|---|---|---|
| `quarter` | `string` | Synthetic quarter field used in the Quarterly Board KPI dataset. BI-ready field name uses lowercase snake_case. |
| `closing_headcount` | `integer` | Employees active on the last day of the reporting period. BI-ready field name uses lowercase snake_case. |
| `hires` | `integer` | Number of employees hired during the reporting period. BI-ready field name uses lowercase snake_case. |
| `exits` | `integer` | Number of employee separations during the reporting period. BI-ready field name uses lowercase snake_case. |
| `turnover_rate` | `numeric` | Employee exits divided by average headcount. BI-ready field name uses lowercase snake_case. |
| `payroll_cost_bdt` | `numeric` | Total monthly gross payroll cost in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `absence_rate` | `numeric` | Approved absence days divided by estimated available workdays. BI-ready field name uses lowercase snake_case. |
| `training_hours` | `integer` | Synthetic training hours field used in the Quarterly Board KPI dataset. BI-ready field name uses lowercase snake_case. |
| `female_representation` | `numeric` | Synthetic female representation field used in the Quarterly Board KPI dataset. BI-ready field name uses lowercase snake_case. |
| `engagement_pulse` | `numeric` | Synthetic engagement pulse field used in the Quarterly Board KPI dataset. BI-ready field name uses lowercase snake_case. |
| `open_vacancies` | `integer` | Synthetic open vacancies field used in the Quarterly Board KPI dataset. BI-ready field name uses lowercase snake_case. |

## `02_CLEAN_DATA/bi_ready_csv/05_fact_recruitment_fy2025.csv`

BI-ready normalized version of 05_Recruitment_Master_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

| Column | Type | Description |
|---|---|---|
| `requisition_id` | `id` | Unique synthetic recruitment requisition identifier. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `location` | `string` | Mokhles Group operating site or office in Bangladesh. BI-ready field name uses lowercase snake_case. |
| `job_title` | `string` | Employee position title within Mokhles Group. BI-ready field name uses lowercase snake_case. |
| `job_level` | `string` | Organisational grade or hierarchy level. BI-ready field name uses lowercase snake_case. |
| `hiring_manager` | `string` | Synthetic hiring manager field used in the Recruitment Master dataset. BI-ready field name uses lowercase snake_case. |
| `posted_date` | `datetime` | Synthetic posted date field used in the Recruitment Master dataset. BI-ready field name uses lowercase snake_case. |
| `target_close_date` | `datetime` | Planned date for closing the corrective action. BI-ready field name uses lowercase snake_case. |
| `actual_close_date` | `datetime` | Synthetic actual close date field used in the Recruitment Master dataset. BI-ready field name uses lowercase snake_case. |
| `status` | `string` | Current workflow status of the record. BI-ready field name uses lowercase snake_case. |
| `planned_vacancies` | `integer` | Synthetic planned vacancies field used in the Recruitment Master dataset. BI-ready field name uses lowercase snake_case. |
| `applications` | `integer` | Number of applications received for the requisition. BI-ready field name uses lowercase snake_case. |
| `shortlisted` | `integer` | Number of candidates selected for initial consideration. BI-ready field name uses lowercase snake_case. |
| `interviewed` | `integer` | Number of candidates interviewed. BI-ready field name uses lowercase snake_case. |
| `offers` | `integer` | Number of employment offers issued. BI-ready field name uses lowercase snake_case. |
| `hires` | `integer` | Number of employees hired during the reporting period. BI-ready field name uses lowercase snake_case. |
| `primary_source` | `string` | Synthetic primary source field used in the Recruitment Master dataset. BI-ready field name uses lowercase snake_case. |
| `time_to_fill_days` | `integer` | Calendar days from requisition posting to closure. BI-ready field name uses lowercase snake_case. |
| `recruitment_cost_bdt` | `numeric` | Synthetic recruitment expenditure in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `candidate_experience_score` | `numeric` | Synthetic candidate feedback score on a 1–5 scale. BI-ready field name uses lowercase snake_case. |

## `02_CLEAN_DATA/bi_ready_csv/06_fact_employee_separations_fy2025.csv`

BI-ready normalized version of 06_Employee_Separations_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

| Column | Type | Description |
|---|---|---|
| `employee_id` | `id` | Unique synthetic employee identifier used consistently across the master datasets. BI-ready field name uses lowercase snake_case. |
| `employee_name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. BI-ready field name uses lowercase snake_case. |
| `gender` | `string` | Synthetic gender category used for workforce representation analysis. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `job_title` | `string` | Employee position title within Mokhles Group. BI-ready field name uses lowercase snake_case. |
| `job_level` | `string` | Organisational grade or hierarchy level. BI-ready field name uses lowercase snake_case. |
| `location` | `string` | Mokhles Group operating site or office in Bangladesh. BI-ready field name uses lowercase snake_case. |
| `join_date` | `datetime` | Employee's synthetic employment start date. BI-ready field name uses lowercase snake_case. |
| `exit_date` | `datetime` | Employee separation date. BI-ready field name uses lowercase snake_case. |
| `tenure_at_exit_years` | `numeric` | Synthetic tenure at exit (years) field used in the Employee Separations dataset. BI-ready field name uses lowercase snake_case. |
| `exit_type` | `string` | Voluntary or involuntary separation classification. BI-ready field name uses lowercase snake_case. |
| `exit_reason` | `string` | Primary synthetic reason for employee separation. BI-ready field name uses lowercase snake_case. |
| `regrettable_exit` | `string` | Indicator for a strategically undesirable employee departure. BI-ready field name uses lowercase snake_case. |
| `manager` | `string` | Fictional line manager associated with the employee. BI-ready field name uses lowercase snake_case. |

## `02_CLEAN_DATA/bi_ready_csv/07_fact_leave_transactions_fy2025.csv`

BI-ready normalized version of 07_Leave_Transactions_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

| Column | Type | Description |
|---|---|---|
| `leave_id` | `id` | Unique synthetic leave transaction identifier. BI-ready field name uses lowercase snake_case. |
| `employee_id` | `id` | Unique synthetic employee identifier used consistently across the master datasets. BI-ready field name uses lowercase snake_case. |
| `employee_name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `location` | `string` | Mokhles Group operating site or office in Bangladesh. BI-ready field name uses lowercase snake_case. |
| `leave_type` | `string` | Category of employee leave. BI-ready field name uses lowercase snake_case. |
| `start_date` | `datetime` | Start date of the leave or programme record. BI-ready field name uses lowercase snake_case. |
| `end_date` | `datetime` | End date of the leave period. BI-ready field name uses lowercase snake_case. |
| `leave_days` | `integer` | Total leave duration recorded for the transaction. BI-ready field name uses lowercase snake_case. |
| `reason_category` | `string` | Synthetic reason category field used in the Leave Master dataset. BI-ready field name uses lowercase snake_case. |
| `approval_status` | `string` | Workflow status of the leave request. BI-ready field name uses lowercase snake_case. |
| `approved_by` | `string` | Synthetic approved by field used in the Leave Master dataset. BI-ready field name uses lowercase snake_case. |

## `02_CLEAN_DATA/bi_ready_csv/08_dim_diversity_inclusion_fy2025.csv`

BI-ready normalized version of 08_Diversity_Inclusion_Master_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

| Column | Type | Description |
|---|---|---|
| `employee_id` | `id` | Unique synthetic employee identifier used consistently across the master datasets. BI-ready field name uses lowercase snake_case. |
| `employee_name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. BI-ready field name uses lowercase snake_case. |
| `gender` | `string` | Synthetic gender category used for workforce representation analysis. BI-ready field name uses lowercase snake_case. |
| `age` | `integer` | Employee age as of the reporting snapshot. BI-ready field name uses lowercase snake_case. |
| `age_band` | `string` | Grouped employee age range used for demographic analysis. BI-ready field name uses lowercase snake_case. |
| `division_of_origin` | `string` | Synthetic administrative division of Bangladesh associated with the employee. BI-ready field name uses lowercase snake_case. |
| `disability_status` | `string` | Synthetic self-declared disability indicator used only for inclusion analysis. BI-ready field name uses lowercase snake_case. |
| `education` | `string` | Highest synthetic education level recorded for the employee. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `job_title` | `string` | Employee position title within Mokhles Group. BI-ready field name uses lowercase snake_case. |
| `job_level` | `string` | Organisational grade or hierarchy level. BI-ready field name uses lowercase snake_case. |
| `employment_type` | `string` | Employment arrangement such as permanent, contract, probation or intern. BI-ready field name uses lowercase snake_case. |
| `location` | `string` | Mokhles Group operating site or office in Bangladesh. BI-ready field name uses lowercase snake_case. |

## `02_CLEAN_DATA/bi_ready_csv/09_fact_training_development_fy2025.csv`

BI-ready normalized version of 09_Training_Development_Master_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

| Column | Type | Description |
|---|---|---|
| `program_id` | `id` | Unique synthetic training programme identifier. BI-ready field name uses lowercase snake_case. |
| `program_name` | `string` | Name of the learning programme. BI-ready field name uses lowercase snake_case. |
| `category` | `string` | Synthetic category field used in the Training Master dataset. BI-ready field name uses lowercase snake_case. |
| `training_date` | `datetime` | Date on which the training programme occurred. BI-ready field name uses lowercase snake_case. |
| `employee_id` | `id` | Unique synthetic employee identifier used consistently across the master datasets. BI-ready field name uses lowercase snake_case. |
| `employee_name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `job_level` | `string` | Organisational grade or hierarchy level. BI-ready field name uses lowercase snake_case. |
| `mode` | `string` | Synthetic mode field used in the Training Master dataset. BI-ready field name uses lowercase snake_case. |
| `provider` | `string` | Synthetic provider field used in the Training Master dataset. BI-ready field name uses lowercase snake_case. |
| `venue` | `string` | Synthetic venue field used in the Training Master dataset. BI-ready field name uses lowercase snake_case. |
| `hours` | `integer` | Synthetic hours field used in the Training Master dataset. BI-ready field name uses lowercase snake_case. |
| `completion_status` | `string` | Whether the employee completed the training. BI-ready field name uses lowercase snake_case. |
| `pre_assessment_score` | `numeric` | Synthetic score before training. BI-ready field name uses lowercase snake_case. |
| `post_assessment_score` | `numeric` | Synthetic score after training. BI-ready field name uses lowercase snake_case. |
| `feedback_rating` | `numeric` | Synthetic participant rating on a 1–5 scale. BI-ready field name uses lowercase snake_case. |
| `cost_bdt` | `numeric` | Synthetic cost (bdt) field used in the Training Master dataset. BI-ready field name uses lowercase snake_case. |
| `mandatory` | `string` | Synthetic mandatory field used in the Training Master dataset. BI-ready field name uses lowercase snake_case. |

## `02_CLEAN_DATA/bi_ready_csv/10_fact_compensation_benefits_fy2025.csv`

BI-ready normalized version of 10_Compensation_Benefits_Master_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

| Column | Type | Description |
|---|---|---|
| `employee_id` | `id` | Unique synthetic employee identifier used consistently across the master datasets. BI-ready field name uses lowercase snake_case. |
| `employee_name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. BI-ready field name uses lowercase snake_case. |
| `gender` | `string` | Synthetic gender category used for workforce representation analysis. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `location` | `string` | Mokhles Group operating site or office in Bangladesh. BI-ready field name uses lowercase snake_case. |
| `job_title` | `string` | Employee position title within Mokhles Group. BI-ready field name uses lowercase snake_case. |
| `job_level` | `string` | Organisational grade or hierarchy level. BI-ready field name uses lowercase snake_case. |
| `employment_type` | `string` | Employment arrangement such as permanent, contract, probation or intern. BI-ready field name uses lowercase snake_case. |
| `basic_salary` | `numeric` | Basic monthly salary in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `house_rent` | `integer` | Monthly house-rent allowance in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `medical_allowance` | `numeric` | Monthly medical allowance in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `conveyance` | `integer` | Monthly conveyance allowance in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `other_allowance` | `numeric` | Additional monthly allowance in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `monthly_gross` | `numeric` | Monthly gross compensation in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `annual_bonus` | `numeric` | Synthetic annual bonus field used in the Compensation Master dataset. BI-ready field name uses lowercase snake_case. |
| `monthly_employer_pf` | `numeric` | Synthetic monthly employer pf field used in the Compensation Master dataset. BI-ready field name uses lowercase snake_case. |
| `annual_gratuity_provision` | `numeric` | Synthetic annual gratuity provision field used in the Compensation Master dataset. BI-ready field name uses lowercase snake_case. |
| `annual_insurance_value` | `numeric` | Synthetic annual insurance value field used in the Compensation Master dataset. BI-ready field name uses lowercase snake_case. |
| `annual_total_reward` | `numeric` | Annualised salary and synthetic employer-funded benefits. BI-ready field name uses lowercase snake_case. |
| `compa_ratio` | `numeric` | Employee monthly gross divided by the synthetic job-level midpoint. BI-ready field name uses lowercase snake_case. |

## `02_CLEAN_DATA/bi_ready_csv/11_fact_performance_evaluation_fy2025.csv`

BI-ready normalized version of 11_Performance_Evaluation_Master_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

| Column | Type | Description |
|---|---|---|
| `employee_id` | `id` | Unique synthetic employee identifier used consistently across the master datasets. BI-ready field name uses lowercase snake_case. |
| `employee_name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `job_title` | `string` | Employee position title within Mokhles Group. BI-ready field name uses lowercase snake_case. |
| `job_level` | `string` | Organisational grade or hierarchy level. BI-ready field name uses lowercase snake_case. |
| `manager` | `string` | Fictional line manager associated with the employee. BI-ready field name uses lowercase snake_case. |
| `goal_completion_percent` | `numeric` | Synthetic achievement against assigned goals. BI-ready field name uses lowercase snake_case. |
| `competency_score_1_5` | `numeric` | Synthetic competency rating on a 1–5 scale. BI-ready field name uses lowercase snake_case. |
| `attendance_score_percent` | `numeric` | Synthetic attendance score (%) field used in the Performance Master dataset. BI-ready field name uses lowercase snake_case. |
| `overall_score` | `numeric` | Weighted performance evaluation score. BI-ready field name uses lowercase snake_case. |
| `performance_rating` | `integer` | Numeric performance rating from 1 to 5. BI-ready field name uses lowercase snake_case. |
| `rating_label` | `string` | Text label corresponding to the performance rating. BI-ready field name uses lowercase snake_case. |
| `potential` | `string` | Synthetic talent-potential classification. BI-ready field name uses lowercase snake_case. |
| `promotion_readiness` | `string` | Indicative readiness category for talent-review practice. BI-ready field name uses lowercase snake_case. |
| `calibration_status` | `string` | Synthetic calibration status field used in the Performance Master dataset. BI-ready field name uses lowercase snake_case. |
| `primary_development_area` | `string` | Synthetic primary development area field used in the Performance Master dataset. BI-ready field name uses lowercase snake_case. |

## `02_CLEAN_DATA/bi_ready_csv/12_fact_health_safety_fy2025.csv`

BI-ready normalized version of 12_Health_Safety_Master_FY2025.csv. Uses UTF-8 encoding and lowercase snake_case headers for broad BI-tool compatibility.

| Column | Type | Description |
|---|---|---|
| `incident_id` | `id` | Unique synthetic health and safety record identifier. BI-ready field name uses lowercase snake_case. |
| `incident_date` | `datetime` | Date of the health and safety record. BI-ready field name uses lowercase snake_case. |
| `location` | `string` | Mokhles Group operating site or office in Bangladesh. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `incident_type` | `string` | Health and safety incident or observation category. BI-ready field name uses lowercase snake_case. |
| `severity` | `string` | Synthetic severity classification. BI-ready field name uses lowercase snake_case. |
| `lost_time_injury` | `string` | Indicates whether the incident resulted in lost workdays. BI-ready field name uses lowercase snake_case. |
| `days_lost` | `integer` | Number of workdays lost following the incident. BI-ready field name uses lowercase snake_case. |
| `root_cause` | `string` | Primary synthetic causal factor identified. BI-ready field name uses lowercase snake_case. |
| `corrective_action` | `string` | Action assigned to reduce recurrence risk. BI-ready field name uses lowercase snake_case. |
| `responsible_owner` | `string` | Synthetic responsible owner field used in the HSE Master dataset. BI-ready field name uses lowercase snake_case. |
| `target_close_date` | `datetime` | Planned date for closing the corrective action. BI-ready field name uses lowercase snake_case. |
| `status` | `string` | Current workflow status of the record. BI-ready field name uses lowercase snake_case. |

## `02_CLEAN_DATA/data_quality/column_profile.csv`

Column-level profile covering inferred types, blanks, distinct values, ranges and examples.

| Column | Type | Description |
|---|---|---|
| `layer` | `string` | Data layer containing the source table. |
| `file_name` | `string` | CSV filename. |
| `column_name` | `string` | Column name. |
| `inferred_type` | `string` | Inferred broad data type. |
| `nonblank_count` | `integer` | Number of nonblank values. |
| `blank_count` | `integer` | Number of blank values. |
| `distinct_count` | `integer` | Number of distinct nonblank values. |
| `minimum_value` | `string` | Minimum numeric or lexical value. |
| `maximum_value` | `string` | Maximum numeric or lexical value. |
| `sample_values` | `string` | Up to three representative values. |

## `02_CLEAN_DATA/data_quality/table_quality_summary.csv`

Table-level data-quality profile covering row counts, blanks, duplicate rows and key checks.

| Column | Type | Description |
|---|---|---|
| `layer` | `string` | Data layer containing the table. |
| `file_name` | `string` | CSV filename. |
| `row_count` | `integer` | Number of data rows. |
| `column_count` | `integer` | Number of columns. |
| `blank_cells` | `integer` | Count of blank cells. |
| `blank_rate_percent` | `number` | Blank cells as a percentage of all cells. |
| `duplicate_rows` | `integer` | Number of fully duplicated rows. |
| `primary_key_hint` | `string` | Recommended unique key or composite key. |
| `duplicate_key_values` | `integer` | Count of duplicated values for the key hint. |
| `utf8_readable` | `string` | Whether the file was read successfully as UTF-8. |
| `quality_status` | `string` | PASS or REVIEW quality status. |

## `02_CLEAN_DATA/data_quality/validation_rules.csv`

Reusable data-quality validation rules for Excel, Power BI, Looker Studio and relational modeling.

| Column | Type | Description |
|---|---|---|
| `rule_id` | `string` | Unique data-quality rule identifier. |
| `scope` | `string` | Tables or platform affected by the rule. |
| `field_or_table` | `string` | Target field or table. |
| `validation_rule` | `string` | Validation requirement. |
| `severity` | `string` | Criticality of a failed rule. |
| `recommended_action` | `string` | Recommended corrective action. |

## `03_POWER_BI/semantic_model/dashboard_blueprint.csv`

Machine-readable six-page dashboard design plan.

| Column | Type | Description |
|---|---|---|
| `page` | `string` | Recommended dashboard page name. |
| `purpose` | `string` | Business purpose of the dashboard page. |
| `recommended_visuals` | `string` | Suggested visual elements. |
| `primary_tables` | `string` | Primary BI-ready source tables. |

## `03_POWER_BI/semantic_model/field_name_mapping.csv`

Maps original business-friendly fields to BI-ready snake_case fields.

| Column | Type | Description |
|---|---|---|
| `source_file` | `string` | Original source CSV filename. |
| `bi_ready_file` | `string` | Corresponding normalized BI-ready CSV filename. |
| `original_field` | `string` | Original business-friendly field name. |
| `bi_ready_field` | `string` | Lowercase snake_case field used in the BI-ready layer. |

## `03_POWER_BI/semantic_model/kpi_catalog.csv`

Canonical HR KPI definitions and preferred source fields.

| Column | Type | Description |
|---|---|---|
| `kpi` | `string` | Human-readable HR KPI name. |
| `business_definition` | `string` | Business meaning of the KPI. |
| `preferred_table` | `string` | Recommended BI-ready source table. |
| `preferred_field` | `string` | Recommended source field. |
| `calculation` | `string` | Cross-platform calculation guidance. |

## `03_POWER_BI/semantic_model/relationship_map.csv`

Cross-platform relationship implementation checklist.

| Column | Type | Description |
|---|---|---|
| `from_table` | `string` | Dimension or source table on the one-side of the relationship. |
| `from_field` | `string` | Relationship key in the source table. |
| `to_table` | `string` | Fact or target table on the many-side of the relationship. |
| `to_field` | `string` | Matching relationship key in the target table. |
| `cardinality` | `string` | Recommended relationship cardinality. |
| `active_recommendation` | `string` | Whether the relationship should normally be active. |
| `notes` | `string` | Implementation notes for the BI model. |

## `04_EXCEL_ANALYTICS/templates/dashboard_blueprint.csv`

Excel analytics template copied from the shared semantic-model assets.

| Column | Type | Description |
|---|---|---|
| `page` | `string` | Recommended dashboard page name. |
| `purpose` | `string` | Business purpose of the dashboard page. |
| `recommended_visuals` | `string` | Suggested visual elements. |
| `primary_tables` | `string` | Primary BI-ready source tables. |

## `04_EXCEL_ANALYTICS/templates/field_name_mapping.csv`

Excel analytics template copied from the shared semantic-model assets.

| Column | Type | Description |
|---|---|---|
| `source_file` | `string` | Original source CSV filename. |
| `bi_ready_file` | `string` | Corresponding normalized BI-ready CSV filename. |
| `original_field` | `string` | Original business-friendly field name. |
| `bi_ready_field` | `string` | Lowercase snake_case field used in the BI-ready layer. |

## `04_EXCEL_ANALYTICS/templates/kpi_catalog.csv`

Excel analytics template copied from the shared semantic-model assets.

| Column | Type | Description |
|---|---|---|
| `kpi` | `string` | Human-readable HR KPI name. |
| `business_definition` | `string` | Business meaning of the KPI. |
| `preferred_table` | `string` | Recommended BI-ready source table. |
| `preferred_field` | `string` | Recommended source field. |
| `calculation` | `string` | Cross-platform calculation guidance. |

## `04_EXCEL_ANALYTICS/templates/relationship_map.csv`

Excel analytics template copied from the shared semantic-model assets.

| Column | Type | Description |
|---|---|---|
| `from_table` | `string` | Dimension or source table on the one-side of the relationship. |
| `from_field` | `string` | Relationship key in the source table. |
| `to_table` | `string` | Fact or target table on the many-side of the relationship. |
| `to_field` | `string` | Matching relationship key in the target table. |
| `cardinality` | `string` | Recommended relationship cardinality. |
| `active_recommendation` | `string` | Whether the relationship should normally be active. |
| `notes` | `string` | Implementation notes for the BI model. |

## `05_LOOKER_STUDIO/data_source_map.csv`

Mapping of recommended Looker Studio data sources, grains, keys, dates and dashboard uses.

| Column | Type | Description |
|---|---|---|
| `file_name` | `string` | Looker Studio-ready CSV filename. |
| `recommended_data_source_name` | `string` | Suggested Looker Studio data-source name. |
| `grain` | `string` | Level of detail represented by each row. |
| `primary_key_or_dimension` | `string` | Recommended key or primary dimension. |
| `primary_date_field` | `string` | Recommended date dimension where available. |
| `recommended_use` | `string` | Suggested dashboard or analysis use. |

## `05_LOOKER_STUDIO/upload_ready_csv/00_dim_date.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `date_key` | `integer` | Integer date key in YYYYMMDD format. |
| `date` | `date` | Calendar date in ISO YYYY-MM-DD format. |
| `year` | `integer` | Calendar year. |
| `quarter` | `string` | Calendar quarter label from Q1 to Q4. |
| `year_quarter` | `string` | Combined year and quarter label. |
| `month_number` | `integer` | Calendar month number from 1 to 12. |
| `month_name` | `string` | Full English month name. |
| `month_short` | `string` | Three-letter English month name. |
| `year_month` | `string` | Combined year and month in YYYY-MM format. |
| `month_start` | `date` | First date of the calendar month. |
| `week_of_year` | `integer` | Week number within the calendar year. |
| `day_of_month` | `integer` | Day number within the month. |
| `day_name` | `string` | English weekday name. |
| `is_weekend` | `string` | Yes when the date is Saturday or Sunday; otherwise No. |

## `05_LOOKER_STUDIO/upload_ready_csv/00_dim_department.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `department_key` | `string` | Normalized department key suitable for relationships. |
| `department` | `string` | Human-readable department name. |
| `cost_center` | `string` | Department cost-center code. |

## `05_LOOKER_STUDIO/upload_ready_csv/00_dim_location.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `location_key` | `string` | Normalized location key suitable for relationships. |
| `location` | `string` | Human-readable work location. |

## `05_LOOKER_STUDIO/upload_ready_csv/01_dim_employee_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `employee_id` | `string` | Unique synthetic employee identifier across active and separated employees. |
| `employee_name` | `string` | Synthetic employee full name. |
| `gender` | `string` | Synthetic employee gender category. |
| `age` | `integer` | Employee age when available. |
| `age_band` | `string` | Grouped employee age range when available. |
| `division_of_origin` | `string` | Bangladesh division of origin when available. |
| `disability_status` | `string` | Synthetic disability-status category when available. |
| `education` | `string` | Highest recorded educational qualification when available. |
| `department` | `string` | Employee organisational department. |
| `department_key` | `string` | Normalized department relationship key. |
| `cost_center` | `string` | Employee department cost-center code. |
| `job_title` | `string` | Employee job title. |
| `job_level` | `string` | Employee organisational job level. |
| `employment_type` | `string` | Employment arrangement when available. |
| `location` | `string` | Employee work location. |
| `location_key` | `string` | Normalized location relationship key. |
| `join_date` | `date` | Employee joining date. |
| `exit_date` | `date` | Employee separation date when applicable. |
| `employment_status` | `string` | FY2025 active or separated status. |
| `manager` | `string` | Recorded reporting manager. |
| `monthly_gross_bdt` | `number` | Monthly gross compensation in Bangladeshi taka when available. |

## `05_LOOKER_STUDIO/upload_ready_csv/02_fact_monthly_hr_kpi_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `month` | `datetime` | Reporting month within FY2025. BI-ready field name uses lowercase snake_case. |
| `opening_headcount` | `integer` | Employees active on the first day of the reporting period. BI-ready field name uses lowercase snake_case. |
| `hires` | `integer` | Number of employees hired during the reporting period. BI-ready field name uses lowercase snake_case. |
| `exits` | `integer` | Number of employee separations during the reporting period. BI-ready field name uses lowercase snake_case. |
| `closing_headcount` | `integer` | Employees active on the last day of the reporting period. BI-ready field name uses lowercase snake_case. |
| `average_headcount` | `numeric` | Average of opening and closing headcount. BI-ready field name uses lowercase snake_case. |
| `turnover_rate` | `numeric` | Employee exits divided by average headcount. BI-ready field name uses lowercase snake_case. |
| `approved_absence_days` | `integer` | Synthetic approved absence days field used in the Monthly HR KPI dataset. BI-ready field name uses lowercase snake_case. |
| `absence_rate` | `numeric` | Approved absence days divided by estimated available workdays. BI-ready field name uses lowercase snake_case. |
| `overtime_hours` | `integer` | Synthetic overtime hours field used in the Monthly HR KPI dataset. BI-ready field name uses lowercase snake_case. |
| `training_hours` | `integer` | Synthetic training hours field used in the Monthly HR KPI dataset. BI-ready field name uses lowercase snake_case. |
| `payroll_cost_bdt` | `numeric` | Total monthly gross payroll cost in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `open_vacancies` | `integer` | Synthetic open vacancies field used in the Monthly HR KPI dataset. BI-ready field name uses lowercase snake_case. |
| `average_time_to_fill_days` | `numeric` | Synthetic average time to fill (days) field used in the Monthly HR KPI dataset. BI-ready field name uses lowercase snake_case. |
| `engagement_pulse_1_5` | `numeric` | Synthetic engagement pulse (1-5) field used in the Monthly HR KPI dataset. BI-ready field name uses lowercase snake_case. |

## `05_LOOKER_STUDIO/upload_ready_csv/03_fact_department_annual_summary_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `opening_headcount` | `integer` | Employees active on the first day of the reporting period. BI-ready field name uses lowercase snake_case. |
| `hires` | `integer` | Number of employees hired during the reporting period. BI-ready field name uses lowercase snake_case. |
| `exits` | `integer` | Number of employee separations during the reporting period. BI-ready field name uses lowercase snake_case. |
| `closing_headcount` | `integer` | Employees active on the last day of the reporting period. BI-ready field name uses lowercase snake_case. |
| `average_headcount` | `numeric` | Average of opening and closing headcount. BI-ready field name uses lowercase snake_case. |
| `turnover_rate` | `numeric` | Employee exits divided by average headcount. BI-ready field name uses lowercase snake_case. |
| `approved_absence_days` | `integer` | Synthetic approved absence days field used in the Department Annual dataset. BI-ready field name uses lowercase snake_case. |
| `training_hours` | `integer` | Synthetic training hours field used in the Department Annual dataset. BI-ready field name uses lowercase snake_case. |
| `average_performance_score` | `numeric` | Synthetic average performance score field used in the Department Annual dataset. BI-ready field name uses lowercase snake_case. |

## `05_LOOKER_STUDIO/upload_ready_csv/04_fact_quarterly_board_kpi_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `quarter` | `string` | Synthetic quarter field used in the Quarterly Board KPI dataset. BI-ready field name uses lowercase snake_case. |
| `closing_headcount` | `integer` | Employees active on the last day of the reporting period. BI-ready field name uses lowercase snake_case. |
| `hires` | `integer` | Number of employees hired during the reporting period. BI-ready field name uses lowercase snake_case. |
| `exits` | `integer` | Number of employee separations during the reporting period. BI-ready field name uses lowercase snake_case. |
| `turnover_rate` | `numeric` | Employee exits divided by average headcount. BI-ready field name uses lowercase snake_case. |
| `payroll_cost_bdt` | `numeric` | Total monthly gross payroll cost in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `absence_rate` | `numeric` | Approved absence days divided by estimated available workdays. BI-ready field name uses lowercase snake_case. |
| `training_hours` | `integer` | Synthetic training hours field used in the Quarterly Board KPI dataset. BI-ready field name uses lowercase snake_case. |
| `female_representation` | `numeric` | Synthetic female representation field used in the Quarterly Board KPI dataset. BI-ready field name uses lowercase snake_case. |
| `engagement_pulse` | `numeric` | Synthetic engagement pulse field used in the Quarterly Board KPI dataset. BI-ready field name uses lowercase snake_case. |
| `open_vacancies` | `integer` | Synthetic open vacancies field used in the Quarterly Board KPI dataset. BI-ready field name uses lowercase snake_case. |

## `05_LOOKER_STUDIO/upload_ready_csv/05_fact_recruitment_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `requisition_id` | `id` | Unique synthetic recruitment requisition identifier. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `location` | `string` | Mokhles Group operating site or office in Bangladesh. BI-ready field name uses lowercase snake_case. |
| `job_title` | `string` | Employee position title within Mokhles Group. BI-ready field name uses lowercase snake_case. |
| `job_level` | `string` | Organisational grade or hierarchy level. BI-ready field name uses lowercase snake_case. |
| `hiring_manager` | `string` | Synthetic hiring manager field used in the Recruitment Master dataset. BI-ready field name uses lowercase snake_case. |
| `posted_date` | `datetime` | Synthetic posted date field used in the Recruitment Master dataset. BI-ready field name uses lowercase snake_case. |
| `target_close_date` | `datetime` | Planned date for closing the corrective action. BI-ready field name uses lowercase snake_case. |
| `actual_close_date` | `datetime` | Synthetic actual close date field used in the Recruitment Master dataset. BI-ready field name uses lowercase snake_case. |
| `status` | `string` | Current workflow status of the record. BI-ready field name uses lowercase snake_case. |
| `planned_vacancies` | `integer` | Synthetic planned vacancies field used in the Recruitment Master dataset. BI-ready field name uses lowercase snake_case. |
| `applications` | `integer` | Number of applications received for the requisition. BI-ready field name uses lowercase snake_case. |
| `shortlisted` | `integer` | Number of candidates selected for initial consideration. BI-ready field name uses lowercase snake_case. |
| `interviewed` | `integer` | Number of candidates interviewed. BI-ready field name uses lowercase snake_case. |
| `offers` | `integer` | Number of employment offers issued. BI-ready field name uses lowercase snake_case. |
| `hires` | `integer` | Number of employees hired during the reporting period. BI-ready field name uses lowercase snake_case. |
| `primary_source` | `string` | Synthetic primary source field used in the Recruitment Master dataset. BI-ready field name uses lowercase snake_case. |
| `time_to_fill_days` | `integer` | Calendar days from requisition posting to closure. BI-ready field name uses lowercase snake_case. |
| `recruitment_cost_bdt` | `numeric` | Synthetic recruitment expenditure in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `candidate_experience_score` | `numeric` | Synthetic candidate feedback score on a 1–5 scale. BI-ready field name uses lowercase snake_case. |

## `05_LOOKER_STUDIO/upload_ready_csv/06_fact_employee_separations_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `employee_id` | `id` | Unique synthetic employee identifier used consistently across the master datasets. BI-ready field name uses lowercase snake_case. |
| `employee_name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. BI-ready field name uses lowercase snake_case. |
| `gender` | `string` | Synthetic gender category used for workforce representation analysis. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `job_title` | `string` | Employee position title within Mokhles Group. BI-ready field name uses lowercase snake_case. |
| `job_level` | `string` | Organisational grade or hierarchy level. BI-ready field name uses lowercase snake_case. |
| `location` | `string` | Mokhles Group operating site or office in Bangladesh. BI-ready field name uses lowercase snake_case. |
| `join_date` | `datetime` | Employee's synthetic employment start date. BI-ready field name uses lowercase snake_case. |
| `exit_date` | `datetime` | Employee separation date. BI-ready field name uses lowercase snake_case. |
| `tenure_at_exit_years` | `numeric` | Synthetic tenure at exit (years) field used in the Employee Separations dataset. BI-ready field name uses lowercase snake_case. |
| `exit_type` | `string` | Voluntary or involuntary separation classification. BI-ready field name uses lowercase snake_case. |
| `exit_reason` | `string` | Primary synthetic reason for employee separation. BI-ready field name uses lowercase snake_case. |
| `regrettable_exit` | `string` | Indicator for a strategically undesirable employee departure. BI-ready field name uses lowercase snake_case. |
| `manager` | `string` | Fictional line manager associated with the employee. BI-ready field name uses lowercase snake_case. |

## `05_LOOKER_STUDIO/upload_ready_csv/07_fact_leave_transactions_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `leave_id` | `id` | Unique synthetic leave transaction identifier. BI-ready field name uses lowercase snake_case. |
| `employee_id` | `id` | Unique synthetic employee identifier used consistently across the master datasets. BI-ready field name uses lowercase snake_case. |
| `employee_name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `location` | `string` | Mokhles Group operating site or office in Bangladesh. BI-ready field name uses lowercase snake_case. |
| `leave_type` | `string` | Category of employee leave. BI-ready field name uses lowercase snake_case. |
| `start_date` | `datetime` | Start date of the leave or programme record. BI-ready field name uses lowercase snake_case. |
| `end_date` | `datetime` | End date of the leave period. BI-ready field name uses lowercase snake_case. |
| `leave_days` | `integer` | Total leave duration recorded for the transaction. BI-ready field name uses lowercase snake_case. |
| `reason_category` | `string` | Synthetic reason category field used in the Leave Master dataset. BI-ready field name uses lowercase snake_case. |
| `approval_status` | `string` | Workflow status of the leave request. BI-ready field name uses lowercase snake_case. |
| `approved_by` | `string` | Synthetic approved by field used in the Leave Master dataset. BI-ready field name uses lowercase snake_case. |

## `05_LOOKER_STUDIO/upload_ready_csv/08_dim_diversity_inclusion_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `employee_id` | `id` | Unique synthetic employee identifier used consistently across the master datasets. BI-ready field name uses lowercase snake_case. |
| `employee_name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. BI-ready field name uses lowercase snake_case. |
| `gender` | `string` | Synthetic gender category used for workforce representation analysis. BI-ready field name uses lowercase snake_case. |
| `age` | `integer` | Employee age as of the reporting snapshot. BI-ready field name uses lowercase snake_case. |
| `age_band` | `string` | Grouped employee age range used for demographic analysis. BI-ready field name uses lowercase snake_case. |
| `division_of_origin` | `string` | Synthetic administrative division of Bangladesh associated with the employee. BI-ready field name uses lowercase snake_case. |
| `disability_status` | `string` | Synthetic self-declared disability indicator used only for inclusion analysis. BI-ready field name uses lowercase snake_case. |
| `education` | `string` | Highest synthetic education level recorded for the employee. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `job_title` | `string` | Employee position title within Mokhles Group. BI-ready field name uses lowercase snake_case. |
| `job_level` | `string` | Organisational grade or hierarchy level. BI-ready field name uses lowercase snake_case. |
| `employment_type` | `string` | Employment arrangement such as permanent, contract, probation or intern. BI-ready field name uses lowercase snake_case. |
| `location` | `string` | Mokhles Group operating site or office in Bangladesh. BI-ready field name uses lowercase snake_case. |

## `05_LOOKER_STUDIO/upload_ready_csv/09_fact_training_development_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `program_id` | `id` | Unique synthetic training programme identifier. BI-ready field name uses lowercase snake_case. |
| `program_name` | `string` | Name of the learning programme. BI-ready field name uses lowercase snake_case. |
| `category` | `string` | Synthetic category field used in the Training Master dataset. BI-ready field name uses lowercase snake_case. |
| `training_date` | `datetime` | Date on which the training programme occurred. BI-ready field name uses lowercase snake_case. |
| `employee_id` | `id` | Unique synthetic employee identifier used consistently across the master datasets. BI-ready field name uses lowercase snake_case. |
| `employee_name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `job_level` | `string` | Organisational grade or hierarchy level. BI-ready field name uses lowercase snake_case. |
| `mode` | `string` | Synthetic mode field used in the Training Master dataset. BI-ready field name uses lowercase snake_case. |
| `provider` | `string` | Synthetic provider field used in the Training Master dataset. BI-ready field name uses lowercase snake_case. |
| `venue` | `string` | Synthetic venue field used in the Training Master dataset. BI-ready field name uses lowercase snake_case. |
| `hours` | `integer` | Synthetic hours field used in the Training Master dataset. BI-ready field name uses lowercase snake_case. |
| `completion_status` | `string` | Whether the employee completed the training. BI-ready field name uses lowercase snake_case. |
| `pre_assessment_score` | `numeric` | Synthetic score before training. BI-ready field name uses lowercase snake_case. |
| `post_assessment_score` | `numeric` | Synthetic score after training. BI-ready field name uses lowercase snake_case. |
| `feedback_rating` | `numeric` | Synthetic participant rating on a 1–5 scale. BI-ready field name uses lowercase snake_case. |
| `cost_bdt` | `numeric` | Synthetic cost (bdt) field used in the Training Master dataset. BI-ready field name uses lowercase snake_case. |
| `mandatory` | `string` | Synthetic mandatory field used in the Training Master dataset. BI-ready field name uses lowercase snake_case. |

## `05_LOOKER_STUDIO/upload_ready_csv/10_fact_compensation_benefits_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `employee_id` | `id` | Unique synthetic employee identifier used consistently across the master datasets. BI-ready field name uses lowercase snake_case. |
| `employee_name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. BI-ready field name uses lowercase snake_case. |
| `gender` | `string` | Synthetic gender category used for workforce representation analysis. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `location` | `string` | Mokhles Group operating site or office in Bangladesh. BI-ready field name uses lowercase snake_case. |
| `job_title` | `string` | Employee position title within Mokhles Group. BI-ready field name uses lowercase snake_case. |
| `job_level` | `string` | Organisational grade or hierarchy level. BI-ready field name uses lowercase snake_case. |
| `employment_type` | `string` | Employment arrangement such as permanent, contract, probation or intern. BI-ready field name uses lowercase snake_case. |
| `basic_salary` | `numeric` | Basic monthly salary in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `house_rent` | `integer` | Monthly house-rent allowance in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `medical_allowance` | `numeric` | Monthly medical allowance in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `conveyance` | `integer` | Monthly conveyance allowance in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `other_allowance` | `numeric` | Additional monthly allowance in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `monthly_gross` | `numeric` | Monthly gross compensation in Bangladeshi Taka. BI-ready field name uses lowercase snake_case. |
| `annual_bonus` | `numeric` | Synthetic annual bonus field used in the Compensation Master dataset. BI-ready field name uses lowercase snake_case. |
| `monthly_employer_pf` | `numeric` | Synthetic monthly employer pf field used in the Compensation Master dataset. BI-ready field name uses lowercase snake_case. |
| `annual_gratuity_provision` | `numeric` | Synthetic annual gratuity provision field used in the Compensation Master dataset. BI-ready field name uses lowercase snake_case. |
| `annual_insurance_value` | `numeric` | Synthetic annual insurance value field used in the Compensation Master dataset. BI-ready field name uses lowercase snake_case. |
| `annual_total_reward` | `numeric` | Annualised salary and synthetic employer-funded benefits. BI-ready field name uses lowercase snake_case. |
| `compa_ratio` | `numeric` | Employee monthly gross divided by the synthetic job-level midpoint. BI-ready field name uses lowercase snake_case. |

## `05_LOOKER_STUDIO/upload_ready_csv/11_fact_performance_evaluation_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `employee_id` | `id` | Unique synthetic employee identifier used consistently across the master datasets. BI-ready field name uses lowercase snake_case. |
| `employee_name` | `string` | Fictional Bangladesh-based employee name generated for portfolio use. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `job_title` | `string` | Employee position title within Mokhles Group. BI-ready field name uses lowercase snake_case. |
| `job_level` | `string` | Organisational grade or hierarchy level. BI-ready field name uses lowercase snake_case. |
| `manager` | `string` | Fictional line manager associated with the employee. BI-ready field name uses lowercase snake_case. |
| `goal_completion_percent` | `numeric` | Synthetic achievement against assigned goals. BI-ready field name uses lowercase snake_case. |
| `competency_score_1_5` | `numeric` | Synthetic competency rating on a 1–5 scale. BI-ready field name uses lowercase snake_case. |
| `attendance_score_percent` | `numeric` | Synthetic attendance score (%) field used in the Performance Master dataset. BI-ready field name uses lowercase snake_case. |
| `overall_score` | `numeric` | Weighted performance evaluation score. BI-ready field name uses lowercase snake_case. |
| `performance_rating` | `integer` | Numeric performance rating from 1 to 5. BI-ready field name uses lowercase snake_case. |
| `rating_label` | `string` | Text label corresponding to the performance rating. BI-ready field name uses lowercase snake_case. |
| `potential` | `string` | Synthetic talent-potential classification. BI-ready field name uses lowercase snake_case. |
| `promotion_readiness` | `string` | Indicative readiness category for talent-review practice. BI-ready field name uses lowercase snake_case. |
| `calibration_status` | `string` | Synthetic calibration status field used in the Performance Master dataset. BI-ready field name uses lowercase snake_case. |
| `primary_development_area` | `string` | Synthetic primary development area field used in the Performance Master dataset. BI-ready field name uses lowercase snake_case. |

## `05_LOOKER_STUDIO/upload_ready_csv/12_fact_health_safety_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `incident_id` | `id` | Unique synthetic health and safety record identifier. BI-ready field name uses lowercase snake_case. |
| `incident_date` | `datetime` | Date of the health and safety record. BI-ready field name uses lowercase snake_case. |
| `location` | `string` | Mokhles Group operating site or office in Bangladesh. BI-ready field name uses lowercase snake_case. |
| `department` | `string` | Organisational department assigned to the employee or record. BI-ready field name uses lowercase snake_case. |
| `incident_type` | `string` | Health and safety incident or observation category. BI-ready field name uses lowercase snake_case. |
| `severity` | `string` | Synthetic severity classification. BI-ready field name uses lowercase snake_case. |
| `lost_time_injury` | `string` | Indicates whether the incident resulted in lost workdays. BI-ready field name uses lowercase snake_case. |
| `days_lost` | `integer` | Number of workdays lost following the incident. BI-ready field name uses lowercase snake_case. |
| `root_cause` | `string` | Primary synthetic causal factor identified. BI-ready field name uses lowercase snake_case. |
| `corrective_action` | `string` | Action assigned to reduce recurrence risk. BI-ready field name uses lowercase snake_case. |
| `responsible_owner` | `string` | Synthetic responsible owner field used in the HSE Master dataset. BI-ready field name uses lowercase snake_case. |
| `target_close_date` | `datetime` | Planned date for closing the corrective action. BI-ready field name uses lowercase snake_case. |
| `status` | `string` | Current workflow status of the record. BI-ready field name uses lowercase snake_case. |

## `05_LOOKER_STUDIO/upload_ready_csv/department_360_summary_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `department` | `string` | Department name. |
| `opening_headcount` | `integer` | Opening FY2025 headcount. |
| `hires` | `integer` | FY2025 hires. |
| `exits` | `integer` | FY2025 exits. |
| `closing_headcount` | `integer` | Closing FY2025 headcount. |
| `average_headcount` | `number` | Average FY2025 headcount. |
| `turnover_rate` | `number` | Annual department turnover rate. |
| `approved_absence_days` | `number` | Approved absence days from the annual summary. |
| `training_hours` | `number` | Training hours from the annual department summary. |
| `average_performance_score` | `number` | Average department performance score. |
| `employees_represented` | `integer` | All active and separated employees represented. |
| `active_headcount` | `integer` | Employees active at FY2025 year-end. |
| `female_headcount` | `integer` | Active female employee count. |
| `female_representation_percent` | `number` | Female share of active department headcount. |
| `average_monthly_gross_bdt` | `number` | Average active-employee monthly gross pay in BDT. |
| `annual_total_reward_bdt` | `number` | Total active-employee annual reward value in BDT. |
| `promotion_ready_employees` | `integer` | Employees categorized as promotion ready. |
| `employee_360_training_hours` | `number` | Training hours aggregated from employee records. |
| `employee_360_training_cost_bdt` | `number` | Training cost aggregated from employee records. |
| `employee_360_approved_leave_days` | `number` | Approved leave days aggregated from employee records. |

## `05_LOOKER_STUDIO/upload_ready_csv/employee_360_fy2025.csv`

UTF-8, lowercase snake_case CSV copy prepared for a separate Looker Studio CSV data source.

| Column | Type | Description |
|---|---|---|
| `employee_id` | `string` | Unique synthetic employee identifier. |
| `employee_name` | `string` | Synthetic employee name. |
| `employment_status` | `string` | FY2025 year-end employment status. |
| `gender` | `string` | Employee gender category. |
| `age` | `integer` | Employee age in years where available. |
| `age_band` | `string` | Grouped employee age range. |
| `division_of_origin` | `string` | Bangladesh division associated with employee origin. |
| `disability_status` | `string` | Recorded synthetic disability-status category. |
| `education` | `string` | Highest recorded education category. |
| `department` | `string` | Employee department. |
| `department_key` | `string` | Normalized department relationship key. |
| `cost_center` | `string` | Department cost-center code. |
| `job_title` | `string` | Employee job title. |
| `job_level` | `string` | Employee job level or grade. |
| `employment_type` | `string` | Employment contract category. |
| `location` | `string` | Employee work location. |
| `location_key` | `string` | Normalized location relationship key. |
| `join_date` | `date` | Employee joining date. |
| `exit_date` | `date` | Employee exit date where applicable. |
| `manager` | `string` | Recorded reporting manager. |
| `monthly_gross_bdt` | `number` | Monthly gross compensation in BDT. |
| `annual_total_reward_bdt` | `number` | Annual total reward value in BDT. |
| `compa_ratio` | `number` | Employee compensation position relative to reference pay. |
| `goal_completion_percent` | `number` | Annual goal-completion percentage. |
| `overall_performance_score` | `number` | Overall FY2025 performance score. |
| `performance_rating` | `string` | Performance rating label. |
| `potential` | `string` | Talent-potential category. |
| `promotion_readiness` | `string` | Promotion-readiness category. |
| `leave_transactions` | `integer` | Number of employee leave transactions. |
| `approved_leave_days` | `number` | Total approved leave days. |
| `training_programs` | `integer` | Number of employee training participation records. |
| `training_hours` | `number` | Total training hours. |
| `training_cost_bdt` | `number` | Total allocated training cost in BDT. |
| `average_training_feedback` | `number` | Average training feedback rating. |
| `average_pre_assessment` | `number` | Average pre-training assessment score. |
| `average_post_assessment` | `number` | Average post-training assessment score. |
| `assessment_improvement` | `number` | Difference between average post- and pre-assessment scores. |
| `exit_type` | `string` | Exit type where the employee separated. |
| `exit_reason` | `string` | Recorded separation reason. |
| `regrettable_exit` | `string` | Whether the exit was categorized as regrettable. |
| `tenure_at_exit_years` | `number` | Employee tenure in years at exit. |

## `06_TABLEAU/relationship_map.csv`

Relationship map copied for direct Tableau implementation.

| Column | Type | Description |
|---|---|---|
| `from_table` | `string` | Dimension or source table on the one-side of the relationship. |
| `from_field` | `string` | Relationship key in the source table. |
| `to_table` | `string` | Fact or target table on the many-side of the relationship. |
| `to_field` | `string` | Matching relationship key in the target table. |
| `cardinality` | `string` | Recommended relationship cardinality. |
| `active_recommendation` | `string` | Whether the relationship should normally be active. |
| `notes` | `string` | Implementation notes for the BI model. |

## `10_DOCUMENTATION/13_Data_Dictionary_FY2025.csv`

Documented project data dictionary.

| Column | Type | Description |
|---|---|---|
| `Master Sheet` | `string` | Field `Master Sheet` in 13_Data_Dictionary_FY2025.csv. |
| `Field Name` | `string` | Field `Field Name` in 13_Data_Dictionary_FY2025.csv. |
| `Definition` | `string` | Field `Definition` in 13_Data_Dictionary_FY2025.csv. |
| `Data Type` | `string` | Field `Data Type` in 13_Data_Dictionary_FY2025.csv. |
| `Source Workbook` | `string` | Field `Source Workbook` in 13_Data_Dictionary_FY2025.csv. |
| `Original Sheet` | `string` | Field `Original Sheet` in 13_Data_Dictionary_FY2025.csv. |
