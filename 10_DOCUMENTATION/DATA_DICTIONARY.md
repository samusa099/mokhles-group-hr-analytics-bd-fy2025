# Data Dictionary

This document provides field-level definitions and source lineage for the consolidated HR datasets.

**Documented fields:** 180

## Compensation Master

| Field | Definition | Data type |
|---|---|---|
| `Employee ID` | Unique synthetic employee identifier used consistently across the master datasets. | Text |
| `Employee Name` | Fictional Bangladesh-based employee name generated for portfolio use. | Text |
| `Gender` | Synthetic gender category used for workforce representation analysis. | Text |
| `Department` | Organisational department assigned to the employee or record. | Text |
| `Location` | Mokhles Group operating site or office in Bangladesh. | Text |
| `Job Title` | Employee position title within Mokhles Group. | Text |
| `Job Level` | Organisational grade or hierarchy level. | Text |
| `Employment Type` | Employment arrangement such as permanent, contract, probation or intern. | Text |
| `Basic Salary` | Basic monthly salary in Bangladeshi Taka. | Currency (BDT) |
| `House Rent` | Monthly house-rent allowance in Bangladeshi Taka. | Number |
| `Medical Allowance` | Monthly medical allowance in Bangladeshi Taka. | Currency (BDT) |
| `Conveyance` | Monthly conveyance allowance in Bangladeshi Taka. | Number |
| `Other Allowance` | Additional monthly allowance in Bangladeshi Taka. | Currency (BDT) |
| `Monthly Gross` | Monthly gross compensation in Bangladeshi Taka. | Currency (BDT) |
| `Annual Bonus` | Synthetic annual bonus field used in the Compensation Master dataset. | Currency (BDT) |
| `Monthly Employer PF` | Synthetic monthly employer pf field used in the Compensation Master dataset. | Currency (BDT) |
| `Annual Gratuity Provision` | Synthetic annual gratuity provision field used in the Compensation Master dataset. | Currency (BDT) |
| `Annual Insurance Value` | Synthetic annual insurance value field used in the Compensation Master dataset. | Currency (BDT) |
| `Annual Total Reward` | Annualised salary and synthetic employer-funded benefits. | Currency (BDT) |
| `Compa-Ratio` | Employee monthly gross divided by the synthetic job-level midpoint. | Percentage / Ratio |

## Department Annual

| Field | Definition | Data type |
|---|---|---|
| `Department` | Organisational department assigned to the employee or record. | Text |
| `Opening Headcount` | Employees active on the first day of the reporting period. | Number |
| `Hires` | Number of employees hired during the reporting period. | Number |
| `Exits` | Number of employee separations during the reporting period. | Number |
| `Closing Headcount` | Employees active on the last day of the reporting period. | Number |
| `Average Headcount` | Average of opening and closing headcount. | Number |
| `Turnover Rate` | Employee exits divided by average headcount. | Percentage / Ratio |
| `Approved Absence Days` | Synthetic approved absence days field used in the Department Annual dataset. | Number |
| `Training Hours` | Synthetic training hours field used in the Department Annual dataset. | Number |
| `Average Performance Score` | Synthetic average performance score field used in the Department Annual dataset. | Number |

## Diversity Master

| Field | Definition | Data type |
|---|---|---|
| `Employee ID` | Unique synthetic employee identifier used consistently across the master datasets. | Text |
| `Employee Name` | Fictional Bangladesh-based employee name generated for portfolio use. | Text |
| `Gender` | Synthetic gender category used for workforce representation analysis. | Text |
| `Age` | Employee age as of the reporting snapshot. | Number |
| `Age Band` | Grouped employee age range used for demographic analysis. | Text |
| `Division of Origin` | Synthetic administrative division of Bangladesh associated with the employee. | Text |
| `Disability Status` | Synthetic self-declared disability indicator used only for inclusion analysis. | Text |
| `Education` | Highest synthetic education level recorded for the employee. | Text |
| `Department` | Organisational department assigned to the employee or record. | Text |
| `Job Title` | Employee position title within Mokhles Group. | Text |
| `Job Level` | Organisational grade or hierarchy level. | Text |
| `Employment Type` | Employment arrangement such as permanent, contract, probation or intern. | Text |
| `Location` | Mokhles Group operating site or office in Bangladesh. | Text |

## Employee Master

| Field | Definition | Data type |
|---|---|---|
| `Employee ID` | Unique synthetic employee identifier used consistently across the master datasets. | Text |
| `Employee Name` | Fictional Bangladesh-based employee name generated for portfolio use. | Text |
| `Gender` | Synthetic gender category used for workforce representation analysis. | Text |
| `Age` | Employee age as of the reporting snapshot. | Number |
| `Age Band` | Grouped employee age range used for demographic analysis. | Text |
| `Division of Origin` | Synthetic administrative division of Bangladesh associated with the employee. | Text |
| `Disability Status` | Synthetic self-declared disability indicator used only for inclusion analysis. | Text |
| `Education` | Highest synthetic education level recorded for the employee. | Text |
| `Department` | Organisational department assigned to the employee or record. | Text |
| `Cost Center` | Synthetic finance and workforce cost-centre code. | Currency (BDT) |
| `Job Title` | Employee position title within Mokhles Group. | Text |
| `Job Level` | Organisational grade or hierarchy level. | Text |
| `Employment Type` | Employment arrangement such as permanent, contract, probation or intern. | Text |
| `Location` | Mokhles Group operating site or office in Bangladesh. | Text |
| `Join Date` | Employee's synthetic employment start date. | Date |
| `Tenure (Years)` | Length of service in years at the reporting date. | Number |
| `Manager` | Fictional line manager associated with the employee. | Text |
| `Monthly Gross` | Monthly gross compensation in Bangladeshi Taka. | Currency (BDT) |

## Employee Separations

| Field | Definition | Data type |
|---|---|---|
| `Employee ID` | Unique synthetic employee identifier used consistently across the master datasets. | Text |
| `Employee Name` | Fictional Bangladesh-based employee name generated for portfolio use. | Text |
| `Gender` | Synthetic gender category used for workforce representation analysis. | Text |
| `Department` | Organisational department assigned to the employee or record. | Text |
| `Job Title` | Employee position title within Mokhles Group. | Text |
| `Job Level` | Organisational grade or hierarchy level. | Text |
| `Location` | Mokhles Group operating site or office in Bangladesh. | Text |
| `Join Date` | Employee's synthetic employment start date. | Date |
| `Exit Date` | Employee separation date. | Date |
| `Tenure at Exit (Years)` | Synthetic tenure at exit (years) field used in the Employee Separations dataset. | Number |
| `Exit Type` | Voluntary or involuntary separation classification. | Text |
| `Exit Reason` | Primary synthetic reason for employee separation. | Text |
| `Regrettable Exit` | Indicator for a strategically undesirable employee departure. | Text |
| `Manager` | Fictional line manager associated with the employee. | Text |

## HSE Master

| Field | Definition | Data type |
|---|---|---|
| `Incident ID` | Unique synthetic health and safety record identifier. | Text |
| `Incident Date` | Date of the health and safety record. | Date |
| `Location` | Mokhles Group operating site or office in Bangladesh. | Text |
| `Department` | Organisational department assigned to the employee or record. | Text |
| `Incident Type` | Health and safety incident or observation category. | Text |
| `Severity` | Synthetic severity classification. | Text |
| `Lost Time Injury` | Indicates whether the incident resulted in lost workdays. | Text |
| `Days Lost` | Number of workdays lost following the incident. | Number |
| `Root Cause` | Primary synthetic causal factor identified. | Text |
| `Corrective Action` | Action assigned to reduce recurrence risk. | Text |
| `Responsible Owner` | Synthetic responsible owner field used in the HSE Master dataset. | Text |
| `Target Close Date` | Planned date for closing the corrective action. | Date |
| `Status` | Current workflow status of the record. | Text |

## Leave Master

| Field | Definition | Data type |
|---|---|---|
| `Leave ID` | Unique synthetic leave transaction identifier. | Text |
| `Employee ID` | Unique synthetic employee identifier used consistently across the master datasets. | Text |
| `Employee Name` | Fictional Bangladesh-based employee name generated for portfolio use. | Text |
| `Department` | Organisational department assigned to the employee or record. | Text |
| `Location` | Mokhles Group operating site or office in Bangladesh. | Text |
| `Leave Type` | Category of employee leave. | Text |
| `Start Date` | Start date of the leave or programme record. | Date |
| `End Date` | End date of the leave period. | Date |
| `Leave Days` | Total leave duration recorded for the transaction. | Number |
| `Reason Category` | Synthetic reason category field used in the Leave Master dataset. | Text |
| `Approval Status` | Workflow status of the leave request. | Text |
| `Approved By` | Synthetic approved by field used in the Leave Master dataset. | Text |

## Monthly HR KPI

| Field | Definition | Data type |
|---|---|---|
| `Month` | Reporting month within FY2025. | Date |
| `Opening Headcount` | Employees active on the first day of the reporting period. | Number |
| `Hires` | Number of employees hired during the reporting period. | Number |
| `Exits` | Number of employee separations during the reporting period. | Number |
| `Closing Headcount` | Employees active on the last day of the reporting period. | Number |
| `Average Headcount` | Average of opening and closing headcount. | Number |
| `Turnover Rate` | Employee exits divided by average headcount. | Percentage / Ratio |
| `Approved Absence Days` | Synthetic approved absence days field used in the Monthly HR KPI dataset. | Number |
| `Absence Rate` | Approved absence days divided by estimated available workdays. | Percentage / Ratio |
| `Overtime Hours` | Synthetic overtime hours field used in the Monthly HR KPI dataset. | Number |
| `Training Hours` | Synthetic training hours field used in the Monthly HR KPI dataset. | Number |
| `Payroll Cost (BDT)` | Total monthly gross payroll cost in Bangladeshi Taka. | Currency (BDT) |
| `Open Vacancies` | Synthetic open vacancies field used in the Monthly HR KPI dataset. | Number |
| `Average Time to Fill (Days)` | Synthetic average time to fill (days) field used in the Monthly HR KPI dataset. | Number |
| `Engagement Pulse (1-5)` | Synthetic engagement pulse (1-5) field used in the Monthly HR KPI dataset. | Number |

## Performance Master

| Field | Definition | Data type |
|---|---|---|
| `Employee ID` | Unique synthetic employee identifier used consistently across the master datasets. | Text |
| `Employee Name` | Fictional Bangladesh-based employee name generated for portfolio use. | Text |
| `Department` | Organisational department assigned to the employee or record. | Text |
| `Job Title` | Employee position title within Mokhles Group. | Text |
| `Job Level` | Organisational grade or hierarchy level. | Text |
| `Manager` | Fictional line manager associated with the employee. | Text |
| `Goal Completion (%)` | Synthetic achievement against assigned goals. | Percentage / Ratio |
| `Competency Score (1-5)` | Synthetic competency rating on a 1–5 scale. | Number |
| `Attendance Score (%)` | Synthetic attendance score (%) field used in the Performance Master dataset. | Percentage / Ratio |
| `Overall Score` | Weighted performance evaluation score. | Number |
| `Performance Rating` | Numeric performance rating from 1 to 5. | Number |
| `Rating Label` | Text label corresponding to the performance rating. | Text |
| `Potential` | Synthetic talent-potential classification. | Text |
| `Promotion Readiness` | Indicative readiness category for talent-review practice. | Text |
| `Calibration Status` | Synthetic calibration status field used in the Performance Master dataset. | Percentage / Ratio |
| `Primary Development Area` | Synthetic primary development area field used in the Performance Master dataset. | Text |

## Quarterly Board KPI

| Field | Definition | Data type |
|---|---|---|
| `Quarter` | Synthetic quarter field used in the Quarterly Board KPI dataset. | Text |
| `Closing Headcount` | Employees active on the last day of the reporting period. | Number |
| `Hires` | Number of employees hired during the reporting period. | Number |
| `Exits` | Number of employee separations during the reporting period. | Number |
| `Turnover Rate` | Employee exits divided by average headcount. | Percentage / Ratio |
| `Payroll Cost (BDT)` | Total monthly gross payroll cost in Bangladeshi Taka. | Currency (BDT) |
| `Absence Rate` | Approved absence days divided by estimated available workdays. | Percentage / Ratio |
| `Training Hours` | Synthetic training hours field used in the Quarterly Board KPI dataset. | Number |
| `Female Representation` | Synthetic female representation field used in the Quarterly Board KPI dataset. | Percentage / Ratio |
| `Engagement Pulse` | Synthetic engagement pulse field used in the Quarterly Board KPI dataset. | Number |
| `Open Vacancies` | Synthetic open vacancies field used in the Quarterly Board KPI dataset. | Number |

## Recruitment Master

| Field | Definition | Data type |
|---|---|---|
| `Requisition ID` | Unique synthetic recruitment requisition identifier. | Text |
| `Department` | Organisational department assigned to the employee or record. | Text |
| `Location` | Mokhles Group operating site or office in Bangladesh. | Text |
| `Job Title` | Employee position title within Mokhles Group. | Text |
| `Job Level` | Organisational grade or hierarchy level. | Text |
| `Hiring Manager` | Synthetic hiring manager field used in the Recruitment Master dataset. | Text |
| `Posted Date` | Synthetic posted date field used in the Recruitment Master dataset. | Date |
| `Target Close Date` | Planned date for closing the corrective action. | Date |
| `Actual Close Date` | Synthetic actual close date field used in the Recruitment Master dataset. | Date |
| `Status` | Current workflow status of the record. | Text |
| `Planned Vacancies` | Synthetic planned vacancies field used in the Recruitment Master dataset. | Number |
| `Applications` | Number of applications received for the requisition. | Number |
| `Shortlisted` | Number of candidates selected for initial consideration. | Number |
| `Interviewed` | Number of candidates interviewed. | Number |
| `Offers` | Number of employment offers issued. | Number |
| `Hires` | Number of employees hired during the reporting period. | Number |
| `Primary Source` | Synthetic primary source field used in the Recruitment Master dataset. | Text |
| `Time to Fill (Days)` | Calendar days from requisition posting to closure. | Number |
| `Recruitment Cost (BDT)` | Synthetic recruitment expenditure in Bangladeshi Taka. | Currency (BDT) |
| `Candidate Experience Score` | Synthetic candidate feedback score on a 1–5 scale. | Date |

## Training Master

| Field | Definition | Data type |
|---|---|---|
| `Program ID` | Unique synthetic training programme identifier. | Text |
| `Program Name` | Name of the learning programme. | Text |
| `Category` | Synthetic category field used in the Training Master dataset. | Text |
| `Training Date` | Date on which the training programme occurred. | Date |
| `Employee ID` | Unique synthetic employee identifier used consistently across the master datasets. | Text |
| `Employee Name` | Fictional Bangladesh-based employee name generated for portfolio use. | Text |
| `Department` | Organisational department assigned to the employee or record. | Text |
| `Job Level` | Organisational grade or hierarchy level. | Text |
| `Mode` | Synthetic mode field used in the Training Master dataset. | Text |
| `Provider` | Synthetic provider field used in the Training Master dataset. | Text |
| `Venue` | Synthetic venue field used in the Training Master dataset. | Text |
| `Hours` | Synthetic hours field used in the Training Master dataset. | Number |
| `Completion Status` | Whether the employee completed the training. | Text |
| `Pre-Assessment Score` | Synthetic score before training. | Number |
| `Post-Assessment Score` | Synthetic score after training. | Number |
| `Feedback Rating` | Synthetic participant rating on a 1–5 scale. | Number |
| `Cost (BDT)` | Synthetic cost (bdt) field used in the Training Master dataset. | Currency (BDT) |
| `Mandatory` | Synthetic mandatory field used in the Training Master dataset. | Text |
