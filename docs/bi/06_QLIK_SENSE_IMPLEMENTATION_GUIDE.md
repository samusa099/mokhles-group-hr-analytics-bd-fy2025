# Qlik Sense Implementation Guide

1. Run `python scripts/build_bi_ready_layer.py`.
2. Create or open a Qlik Sense app.
3. Open **Data Manager → Add data**.
4. Upload the required BI-ready CSV files.
5. Review profiling, field types and proposed associations.
6. Load the data.

Compare automatic associations with `bi_assets/semantic_model/relationship_map.csv`.

## Key fields

- `employee_id`
- `department`
- `location`
- `date`
- `month`

Rename fields in the load script when two fields share a name but have different business meanings.

## Starter master measures

```text
Count({<employment_status={'Active at FY2025 year-end'}>} DISTINCT employee_id)
```

```text
Sum(hours)
```

```text
Avg(overall_score)
```

Official reference: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/data-management.htm
