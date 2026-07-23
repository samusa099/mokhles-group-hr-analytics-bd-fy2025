# Cross-Platform KPI Formula Library

Canonical definitions are also stored in `bi_assets/semantic_model/kpi_catalog.csv`.

## Active headcount

Distinct employees where `employment_status = Active at FY2025 year-end`.

## Hires

```text
SUM(hires)
```

## Exits

Distinct count of `employee_id` in the employee-separations fact.

## Turnover rate

```text
exits / average_headcount
```

## Average time to fill

Average `time_to_fill_days`, excluding blank values for open requisitions.

## Training completion rate

```text
completed training records / all training records
```

## Assessment improvement

```text
post_assessment_score - pre_assessment_score
```

## Female representation

```text
distinct active female employees / distinct active employees
```

## Average performance score

```text
AVERAGE(overall_score)
```

## Monthly gross payroll

```text
SUM(monthly_gross)
```

## Lost-time injuries

Count records where `lost_time_injury = Yes`.

Formatting: whole numbers for headcount, BDT for currency, percentages for rates, and one or two decimals for scores/averages.
