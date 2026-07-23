# BI Analytics — Start Here

This section explains how to use the Mokhles Group HR Analytics portfolio in major business-intelligence platforms.

## Supported platforms

| Platform | Recommended source | Best use |
|---|---|---|
| Power BI Desktop | Generated BI-ready CSVs or Excel master workbook | Full HR dashboard portfolio |
| Looker Studio | Generated BI-ready CSVs, Google Sheets or BigQuery | Shareable web dashboards |
| Tableau | Generated BI-ready CSVs | Interactive visual analytics |
| Qlik Sense | Generated BI-ready CSVs | Associative exploration |
| Excel Power Query | Original CSVs, BI-ready CSVs or Excel reports | Excel-based analysis |
| Metabase | BI-ready CSV upload or database load | Lightweight browser BI |

## Step 1 — Generate the BI layer

From the repository root run:

```bash
python scripts/build_bi_ready_layer.py
```

The script creates 15 dimensions/facts inside `data/bi_ready_csv/` without changing the authoritative files in `data/csv/`.

## Step 2 — Understand the model

Read `02_DATA_MODEL_AND_RELATIONSHIPS.md` and use:

- `bi_assets/semantic_model/relationship_map.csv`
- `bi_assets/semantic_model/kpi_catalog.csv`
- `bi_assets/semantic_model/dashboard_blueprint.csv`

## Step 3 — Follow your platform guide

- `03_POWER_BI_IMPLEMENTATION_GUIDE.md`
- `04_LOOKER_STUDIO_IMPLEMENTATION_GUIDE.md`
- `05_TABLEAU_IMPLEMENTATION_GUIDE.md`
- `06_QLIK_SENSE_IMPLEMENTATION_GUIDE.md`
- `07_EXCEL_POWER_QUERY_GUIDE.md`
- `08_METABASE_IMPLEMENTATION_GUIDE.md`

All records are synthetic and intended for education, analytics practice and portfolio demonstration.
