# Tableau Implementation Guide

1. Run `python scripts/build_bi_ready_layer.py`.
2. In Tableau select **Connect → Text File**.
3. Select a file from `data/bi_ready_csv/`.
4. Add other logical tables as required.
5. Review field types on the Data Source page.

## Relationships

Use logical relationships on `employee_id`, `department`, `location`, `date` and `month` before using physical joins. Relationships preserve each table's level of detail and reduce accidental duplication.

## Calculated fields

```text
Active Headcount
COUNTD(IF [employment_status] = "Active at FY2025 year-end" THEN [employee_id] END)
```

```text
Training Improvement
AVG([post_assessment_score] - [pre_assessment_score])
```

```text
Female Representation
COUNTD(IF [gender] = "Female" THEN [employee_id] END) / COUNTD([employee_id])
```

Recommended interactions include department/location/date filters, job-level highlights, KPI tooltips and drill-through to transaction detail.

Official references:

- https://help.tableau.com/current/pro/desktop/en-us/examples_text.htm
- https://help.tableau.com/current/pro/desktop/en-us/datasource_relationships_learnmorepage.htm
