# Cross-Platform BI Compatibility

## Compatibility principle

The original CSV files remain the authoritative analytical tables. The
`data/bi_ready_csv/` directory provides normalized copies and dimensions that
are easier to import into desktop, cloud and browser-based BI tools.

No proprietary report file is required. Users can reproduce the model in the
platform of their choice.

## Compatibility matrix

| Capability | Power BI | Looker Studio | Tableau | Qlik Sense | Excel Power Query | Metabase |
|---|---:|---:|---:|---:|---:|---:|
| Import CSV | Yes | Yes | Yes | Yes | Yes | Yes |
| Import Excel | Yes | Via supported connector/workaround | Yes | Yes | Yes | Database route preferred |
| Multi-table model | Strong | Limited through blends; stronger through Sheets/BigQuery | Strong | Strong | Strong with Data Model | Stronger after database load |
| Reusable calculated metrics | DAX measures | Calculated fields | Calculated fields | Master measures | Measures / formulas | Models, metrics and SQL |
| Scheduled refresh | Service/gateway dependent | Connector dependent | Platform dependent | Platform dependent | Source-dependent | Database and deployment dependent |
| Best package | BI-ready CSV + dimensions | BI-ready CSV or Google Sheets | BI-ready CSV | BI-ready CSV | Original or BI-ready data | BI-ready CSV or database |

## Important platform notes

- Looker Studio CSV upload expects clean tabular files and restrictive field
  names. The BI-ready files use valid lowercase `snake_case` headers.
- Power BI, Tableau and Qlik can maintain relationships between multiple
  tables; avoid flattening all tables into one file unless a tool or use case
  requires it.
- Metabase CSV upload is suitable for demonstrations and ad hoc analysis.
  Frequent refresh and production use are better handled by loading the data
  into a supported database first.
- Excel Power Query can import individual files or combine repeated files with
  the same schema from a folder. Do not combine unrelated HR tables merely
  because they are stored together.

## Official references

- Power Query Text/CSV connector:
  https://learn.microsoft.com/en-us/power-query/connectors/text-csv
- Power BI relationships:
  https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships
- Looker Studio CSV upload:
  https://docs.cloud.google.com/looker/docs/studio/upload-csv-files-to-looker-studio
- Tableau text files:
  https://help.tableau.com/current/pro/desktop/en-us/examples_text.htm
- Tableau relationships:
  https://help.tableau.com/current/pro/desktop/en-us/datasource_relationships_learnmorepage.htm
- Qlik Data Manager:
  https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/data-management.htm
- Metabase uploads:
  https://www.metabase.com/docs/latest/exploration-and-organization/uploads
- Excel Power Query from folder:
  https://support.microsoft.com/en-us/excel/import-data-from-a-folder-with-multiple-files-power-query
