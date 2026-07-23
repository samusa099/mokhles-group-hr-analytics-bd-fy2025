# Qlik Sense Implementation Guide

## 1. Add the data

1. Create or open a Qlik Sense app.
2. Open **Data Manager**.
3. Select **Add data**.
4. Upload the required BI-ready CSV files.
5. Keep data profiling enabled.
6. Review the table preview and field types.
7. Load the data.

## 2. Manage associations

Qlik may associate fields with matching names automatically. Review the
Associations view and compare the proposed links with:

```text
bi_assets/semantic_model/relationship_map.csv
```

Create custom associations where necessary.

## 3. Key association fields

- `employee_id`
- `department`
- `location`
- `date`
- `month`

Avoid unintended associations from generic field names. Rename fields in the
load script when two fields have the same name but different business meaning.

## 4. Starter master measures

```text
Active Headcount
Count({<employment_status={'Active at FY2025 year-end'}>} DISTINCT employee_id)
```

```text
FY2025 Exits
Count(DISTINCT employee_id)
```

```text
Training Hours
Sum(hours)
```

```text
Average Performance Score
Avg(overall_score)
```

## Official references

- Data Manager:
  https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/data-management.htm
- Managing associations:
  https://help.qlik.com/en-US/sense/May2024/Subsystems/Hub/Content/Sense_Hub/LoadData/associating-data.htm
