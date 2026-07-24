# Qlik Sense Guide

Qlik Sense can load CSV and Excel files from a folder connection.

1. Create a folder connection to the project root.
2. Open the Data Load Editor.
3. Update the path in `Mokhles_HR_Load_Script.qvs`.
4. Load the BI-ready tables.
5. Review associations around employee_id, department, location and date.
6. Avoid unintended synthetic keys by renaming fields when two unrelated
   tables share the same column name.

Official references:

- https://help.qlik.com/en-US/sense/May2024/Subsystems/Hub/Content/Sense_Hub/DataSource/load-data-from-files.htm
- https://help.qlik.com/en-US/sense/May2025/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Directory.htm
