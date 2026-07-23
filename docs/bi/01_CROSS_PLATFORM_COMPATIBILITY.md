# Cross-Platform BI Compatibility

The original files in `data/csv/` remain authoritative. The generated `data/bi_ready_csv/` layer uses UTF-8 encoding, lowercase `snake_case` headers, dimension/fact naming and reusable keys for broad BI-tool compatibility.

## Compatibility matrix

| Capability | Power BI | Looker Studio | Tableau | Qlik Sense | Excel Power Query | Metabase |
|---|---:|---:|---:|---:|---:|---:|
| Import CSV | Yes | Yes | Yes | Yes | Yes | Yes |
| Multi-table model | Strong | Limited through blends | Strong | Strong | Strong with Data Model | Stronger after database load |
| Reusable metrics | DAX | Calculated fields | Calculated fields | Master measures | Measures/formulas | Models, metrics and SQL |
| Recommended package | BI-ready CSVs | BI-ready CSVs/Sheets/BigQuery | BI-ready CSVs | BI-ready CSVs | Original or BI-ready data | BI-ready CSVs/database |

## Key guidance

- Do not flatten every HR table into one file unless a specific use case requires it.
- Use dimensions to filter facts and preserve each table's natural level of detail.
- Looker Studio works best with focused data sources or a managed Google Sheets/BigQuery model.
- Metabase CSV upload is suitable for demonstrations; recurring production refreshes are better through a database.
- Excel From Folder should combine only repeated files with the same schema, not unrelated HR tables.

## Official references

- Power Query Text/CSV: https://learn.microsoft.com/en-us/power-query/connectors/text-csv
- Power BI relationships: https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships
- Looker Studio CSV upload: https://docs.cloud.google.com/looker/docs/studio/upload-csv-files-to-looker-studio
- Tableau text files: https://help.tableau.com/current/pro/desktop/en-us/examples_text.htm
- Qlik Data Manager: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/data-management.htm
- Metabase uploads: https://www.metabase.com/docs/latest/exploration-and-organization/uploads
