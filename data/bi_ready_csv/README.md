# BI-Ready CSV Layer

This directory is the output location for cross-platform BI tables.

Generate or refresh the complete layer from the authoritative files in `data/csv/`:

```bash
python scripts/build_bi_ready_layer.py
```

## Design rules

- UTF-8 encoding
- Lowercase `snake_case` headers
- No spaces or punctuation in field names
- Dimension and fact naming convention
- Unified active-and-separated employee dimension
- Reusable date, department and location dimensions

The original business-friendly CSV files remain authoritative and are not modified.
