# Tableau Guide

Use the files in `02_CLEAN_DATA/bi_ready_csv/`.

Recommended method:

1. Connect each CSV as a logical table.
2. Use relationships instead of flattening all tables into one large join.
3. Use shared dimensions such as employee, department, location and date.
4. Preserve each fact table's native grain.
5. Follow `03_POWER_BI/semantic_model/relationship_map.csv`.

Tableau relationships keep logical tables separate and preserve their level of
detail until analysis requires them.

Official references:

- https://help.tableau.com/current/pro/desktop/en-us/datasource_datamodel.htm
- https://help.tableau.com/current/pro/desktop/en-us/relate_tables.htm
