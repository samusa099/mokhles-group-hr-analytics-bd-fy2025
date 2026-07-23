# Power BI Implementation Guide

## Recommended source

Use `02_CLEAN_DATA/bi_ready_csv/`. The model is already separated into
dimensions and facts.

## Setup

1. Create the `ProjectRoot` text parameter.
2. Paste the `.m` queries from `03_POWER_BI/power_query_m/`.
3. Apply data types in Power Query.
4. Use `03_POWER_BI/semantic_model/relationship_map.csv`.
5. Mark `00_dim_date[date]` as the date table.
6. Import the JSON theme from `03_POWER_BI/theme/`.
7. Add measures from `03_POWER_BI/dax/`.
8. Follow the dashboard blueprint.

## Important folder rule

Power Query's Folder connector can see files in the chosen folder and its
subfolders. Combine Files should only be used when the files share the same
schema. This project therefore keeps unlike tables in separate logical folders
and provides one query per analytical table.

Official references:

- https://learn.microsoft.com/en-us/power-query/connectors/folder
- https://learn.microsoft.com/en-us/power-query/combine-files-overview
- https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships
