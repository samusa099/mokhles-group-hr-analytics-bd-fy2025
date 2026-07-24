"""Profile CSV tables and write data-quality outputs."""

from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "02_CLEAN_DATA" / "data_quality"


def profile():
    folders = [
        ("source_csv", ROOT / "01_SOURCE_DATA" / "csv_original"),
        ("bi_ready_csv", ROOT / "02_CLEAN_DATA" / "bi_ready_csv"),
        ("analysis_ready", ROOT / "02_CLEAN_DATA" / "analysis_ready"),
    ]

    summary = []
    for layer, folder in folders:
        for path in sorted(folder.glob("*.csv")):
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)
                headers = list(reader.fieldnames or [])
                rows = list(reader)

            blank_cells = sum(
                1 for row in rows for header in headers
                if not str(row.get(header, "")).strip()
            )
            total_cells = max(1, len(rows) * len(headers))
            duplicates = len(rows) - len(
                {tuple(row.get(header, "") for header in headers) for row in rows}
            )

            summary.append({
                "layer": layer,
                "file_name": path.name,
                "row_count": len(rows),
                "column_count": len(headers),
                "blank_cells": blank_cells,
                "blank_rate_percent": round(blank_cells / total_cells * 100, 2),
                "duplicate_rows": duplicates,
                "quality_status": "PASS" if duplicates == 0 else "REVIEW",
            })

    OUTPUT.mkdir(parents=True, exist_ok=True)
    headers = list(summary[0].keys())
    with (OUTPUT / "table_quality_basic.csv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(summary)

    print(f"Profiled {len(summary)} CSV tables.")


if __name__ == "__main__":
    profile()
