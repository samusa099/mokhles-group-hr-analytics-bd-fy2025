# BI Analytics Start Here

This folder explains how to use the Mokhles Group HR Analytics portfolio in
common business-intelligence and reporting platforms.

## Supported workflows

| Platform | Recommended source | Modeling approach | Best use |
|---|---|---|---|
| Power BI Desktop | `data/bi_ready_csv/` or Excel master workbook | Star/snowflake model with relationships | Full HR dashboard portfolio |
| Looker Studio | `data/bi_ready_csv/` | Separate data sources, blends, or Google Sheets/BigQuery | Shareable web dashboards |
| Tableau | `data/bi_ready_csv/` | Logical relationships | Interactive visual analytics |
| Qlik Sense | `data/bi_ready_csv/` | Data Manager associations | Associative exploration |
| Excel Power Query | Original CSVs, BI-ready CSVs, or Excel reports | Queries and Data Model | Familiar Excel-based analysis |
| Metabase | BI-ready CSV upload or database load | Models and saved questions | Lightweight browser BI |

## Which files should I use?

### Original analytical files

```text
data/csv/
```

Use these files when you want the original business-friendly column names.

### Cross-platform BI files

```text
data/bi_ready_csv/
```

Use these files when the platform prefers simple field names. They use:

- UTF-8 encoding
- Lowercase `snake_case` headers
- No spaces or punctuation in field names
- Separate employee, date, department and location dimensions
- Fact-table naming for transactional and KPI datasets

## Recommended learning order

1. Read `01_CROSS_PLATFORM_COMPATIBILITY.md`
2. Read `02_DATA_MODEL_AND_RELATIONSHIPS.md`
3. Open the guide for your selected BI platform
4. Review `09_KPI_FORMULA_LIBRARY.md`
5. Use `10_DASHBOARD_BLUEPRINT.md` to build the report pages

## Supporting assets

```text
bi_assets/
├── power_bi/
│   └── Mokhles_Group_HR_Analytics_Theme.json
└── semantic_model/
    ├── relationship_map.csv
    ├── field_name_mapping.csv
    ├── kpi_catalog.csv
    └── dashboard_blueprint.csv
```

## Project links

- GitHub: https://github.com/samusa099/mokhles-group-hr-analytics-bd-fy2025
- Kaggle: https://www.kaggle.com/datasets/samusahr/mokhles-group-hr-analytics-portfolio-bd-fy2025
