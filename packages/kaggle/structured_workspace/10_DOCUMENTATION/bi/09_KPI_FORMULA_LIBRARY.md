# Cross-Platform KPI Formula Library

The canonical business definitions are stored in:

```text
bi_assets/semantic_model/kpi_catalog.csv
```

## Core KPI definitions

### Active Headcount

Distinct employees where:

```text
employment_status = Active at FY2025 year-end
```

### Hires

```text
SUM(hires)
```

### Exits

```text
DISTINCTCOUNT(employee_id)
```

using the employee-separations fact.

### Turnover Rate

```text
exits / average_headcount
```

Use the supplied monthly or departmental turnover rate when reproducing the
published reports.

### Average Time to Fill

```text
AVERAGE(time_to_fill_days)
```

Exclude blank values for open requisitions.

### Training Completion Rate

```text
completed training records / all training records
```

### Assessment Improvement

```text
post_assessment_score - pre_assessment_score
```

### Female Representation

```text
distinct active female employees / distinct active employees
```

### Average Performance Score

```text
AVERAGE(overall_score)
```

### Monthly Gross Payroll

```text
SUM(monthly_gross)
```

### Lost-Time Injuries

Count safety records where:

```text
lost_time_injury = Yes
```

## Formatting standards

- Headcount: whole number
- Currency: BDT with thousand separators
- Rates: percentage with one or two decimals
- Scores: one or two decimals
- Days and hours: whole number unless averages are used
