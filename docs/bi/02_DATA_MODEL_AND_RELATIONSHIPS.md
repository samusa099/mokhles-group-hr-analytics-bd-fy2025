# BI Data Model and Relationships

## Recommended dimensions

- `00_dim_date.csv`
- `00_dim_department.csv`
- `00_dim_location.csv`
- `01_dim_employee_fy2025.csv`

## Recommended facts

- Monthly HR KPI
- Department annual summary
- Quarterly board KPI
- Recruitment
- Employee separations
- Leave transactions
- Training and development
- Compensation and benefits
- Performance evaluation
- Health and safety

Use `bi_assets/semantic_model/relationship_map.csv` as the implementation checklist.

## Primary keys

- `employee_id`
- `department`
- `location`
- `date`
- `month`

## Modeling rules

- Dimensions should contain unique key values.
- Fact-table keys may repeat.
- Use one-to-many relationships from dimensions to facts.
- Keep single-direction filtering as the default in Power BI.
- Mark `00_dim_date[date]` as the date table.
- Keep one active date relationship per fact; use inactive alternatives only when needed.
- In Tableau, prefer logical relationships before physical joins.
- In Qlik, review automatic field associations to prevent unintended synthetic keys.
- In Looker Studio, use focused data sources and limited blends.

## Validation checklist

- Related columns have matching data types.
- Dates are parsed as dates rather than text.
- Currency values use BDT formatting.
- Rates use percentage formatting.
- Employee counts use distinct count where required.
