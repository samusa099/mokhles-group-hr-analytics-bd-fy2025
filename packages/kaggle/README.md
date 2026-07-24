# 📦 Kaggle Distribution Package

This directory keeps the Kaggle-oriented files separate from the GitHub engineering source so the repository root remains clean and easy to navigate.

## Folder layout

```text
packages/kaggle/
├── structured_workspace/
│   ├── 00_START_HERE/
│   ├── 01_SOURCE_DATA/
│   ├── 02_CLEAN_DATA/
│   ├── 03_POWER_BI/
│   ├── 04_EXCEL_ANALYTICS/
│   ├── 05_LOOKER_STUDIO/
│   ├── 06_TABLEAU/
│   ├── 07_QLIK/
│   ├── 08_METABASE/
│   ├── 09_NOTEBOOKS/
│   ├── 10_DOCUMENTATION/
│   ├── 11_KAGGLE_METADATA/
│   └── 12_SCRIPTS/
└── publish/
    ├── dataset-metadata.json
    └── dataset-cover-image.png
```

## 🧭 Which folder should I open?

| Goal | Folder |
|---|---|
| Understand the package | `structured_workspace/00_START_HERE/` |
| Use original CSV or Excel data | `structured_workspace/01_SOURCE_DATA/` |
| Use BI-ready or analysis-ready data | `structured_workspace/02_CLEAN_DATA/` |
| Build a Power BI project | `structured_workspace/03_POWER_BI/` |
| Practise Excel analytics | `structured_workspace/04_EXCEL_ANALYTICS/` |
| Use another BI platform | `structured_workspace/05_LOOKER_STUDIO/` to `08_METABASE/` |
| Open the notebook | `structured_workspace/09_NOTEBOOKS/` |
| Read documentation | `structured_workspace/10_DOCUMENTATION/` |
| Review Kaggle metadata | `structured_workspace/11_KAGGLE_METADATA/` |
| Run preparation scripts | `structured_workspace/12_SCRIPTS/` |

## ✅ Packaging principle

- GitHub development files remain in the standard repository folders.
- Kaggle distribution files remain inside `packages/kaggle/`.
- Duplicate flat files are not stored in the repository root.
- Raw data, clean data, project assets, notebooks, documentation and scripts remain separated by purpose.

> All project records are synthetic and must not be presented as real employee or organisational information.
