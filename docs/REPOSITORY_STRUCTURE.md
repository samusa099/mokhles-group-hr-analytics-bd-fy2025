# Repository Structure

```text
mokhles-group-hr-analytics-bd-fy2025/
├── .github/                 GitHub Actions and contribution templates
├── assets/                  Cover and dashboard preview images
├── data/
│   ├── csv/                 13 analysis-ready CSV tables
│   └── excel/
│       ├── master/          Consolidated Excel master workbook
│       └── reports/         12 specialised Excel dashboards
├── docs/                    Dataset, field and publishing documentation
├── examples/                Reusable Python example
├── metadata/                Project, GitHub and Kaggle metadata
├── notebooks/               Exploratory Jupyter Notebook
├── scripts/                 Repository validation utilities
├── src/                     Reusable Python data-loading package
├── README.md
├── CITATION.cff
├── LICENSE
├── LICENSE-CODE
└── pyproject.toml
```

The repository is the maintainable source version. The Kaggle distribution
is published separately so platform-specific metadata can remain at the
required package root.
