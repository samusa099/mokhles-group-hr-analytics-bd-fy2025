# Excel and Power Query Guide

## Existing Excel portfolio

Open the consolidated master workbook or a specialised report from `data/excel/` for the fastest review experience.

## Import a CSV

1. Select **Data → Get Data → From File → From Text/CSV**.
2. Choose an original or BI-ready CSV.
3. Select **Transform Data**.
4. Confirm data types and cleaning steps.
5. Select **Close & Load**.

## Build the BI-ready layer

```bash
python scripts/build_bi_ready_layer.py
```

Load dimensions and facts as connections and add them to the Excel Data Model. Use `relationship_map.csv` to create relationships.

## Folder-import warning

**From Folder** combines files with the same schema. Do not combine the entire HR CSV folder because the tables have different structures. Use it only for repeated monthly files of one table.

Official references:

- https://support.microsoft.com/en-us/excel/import-data-from-a-folder-with-multiple-files-power-query
- https://learn.microsoft.com/en-us/power-query/connectors/text-csv
