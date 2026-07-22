"""Data loading helpers for the Mokhles Group HR Analytics repository."""

from __future__ import annotations

from pathlib import Path
from typing import Final

import pandas as pd


REPOSITORY_ROOT: Final[Path] = Path(__file__).resolve().parents[2]
CSV_DIRECTORY: Final[Path] = REPOSITORY_ROOT / "data" / "csv"
MASTER_WORKBOOK: Final[Path] = (
    REPOSITORY_ROOT
    / "data"
    / "excel"
    / "master"
    / "Mokhles_Group_HR_Analytics_Master_Dataset_FY2025.xlsx"
)


def list_csv_tables() -> list[str]:
    """Return the available analysis-ready CSV filenames."""
    if not CSV_DIRECTORY.exists():
        raise FileNotFoundError(f"CSV directory not found: {CSV_DIRECTORY}")
    return sorted(path.name for path in CSV_DIRECTORY.glob("*.csv"))


def load_csv_table(filename: str, **read_csv_kwargs: object) -> pd.DataFrame:
    """Load one CSV table by filename.

    Parameters
    ----------
    filename:
        Filename located inside ``data/csv``.
    **read_csv_kwargs:
        Additional keyword arguments forwarded to ``pandas.read_csv``.

    Raises
    ------
    FileNotFoundError
        If the requested table does not exist.
    ValueError
        If a path outside ``data/csv`` is requested.
    """
    requested = (CSV_DIRECTORY / filename).resolve()
    if CSV_DIRECTORY.resolve() not in requested.parents:
        raise ValueError("The requested file must be inside data/csv.")
    if not requested.exists():
        available = ", ".join(list_csv_tables())
        raise FileNotFoundError(
            f"CSV table not found: {filename}. Available tables: {available}"
        )
    return pd.read_csv(requested, **read_csv_kwargs)


def load_master_sheet(
    sheet_name: str,
    *,
    header: int = 3,
    **read_excel_kwargs: object,
) -> pd.DataFrame:
    """Load a worksheet from the consolidated master workbook.

    The Excel workbooks use the fourth row as the table header, therefore the
    default Pandas header index is ``3``.
    """
    if not MASTER_WORKBOOK.exists():
        raise FileNotFoundError(f"Master workbook not found: {MASTER_WORKBOOK}")
    return pd.read_excel(
        MASTER_WORKBOOK,
        sheet_name=sheet_name,
        header=header,
        **read_excel_kwargs,
    )
