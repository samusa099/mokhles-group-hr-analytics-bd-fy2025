# Tableau Implementation Guide

## 1. Connect to the data

1. Open Tableau Desktop or Tableau Public.
2. Under **Connect**, choose **Text File**.
3. Select a file from `data/bi_ready_csv/`.
4. Add additional CSV connections as required.
5. Use the Data Source page to review field types.

## 2. Use relationships before joins

Place logical tables on the relationship canvas and connect matching fields.

Recommended relationship fields:

- `employee_id`
- `department`
- `location`
- `date`
- `month`

Relationships preserve the level of detail of the separate tables. Use a
physical join only when a fixed row-level combination is intentionally needed.

## 3. Starter calculated fields

### Active Headcount

```text
COUNTD(
    IF [employment_status] = "Active at FY2025 year-end"
    THEN [employee_id]
    END
)
```

### FY2025 Exits

```text
COUNTD([employee_id])
```

### Training Improvement

```text
AVG([post_assessment_score] - [pre_assessment_score])
```

### Female Representation

```text
COUNTD(IF [gender] = "Female" THEN [employee_id] END)
/
COUNTD([employee_id])
```

## 4. Recommended dashboard actions

- Department filter
- Location filter
- Date range filter
- Highlight action for job level
- Drill-through from KPI to employee or transaction detail
- Tooltip pages for KPI definitions

## Official references

- Connect to text files:
  https://help.tableau.com/current/pro/desktop/en-us/examples_text.htm
- Relate data:
  https://help.tableau.com/current/pro/desktop/en-us/relate_tables.htm
- Relationships versus joins:
  https://help.tableau.com/current/pro/desktop/en-us/datasource_relationships_learnmorepage.htm
