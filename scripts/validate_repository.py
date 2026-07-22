"""Validate repository data, metadata and document integrity."""

from __future__ import annotations

import csv
import json
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
METADATA_PATH = ROOT / "metadata" / "kaggle-dataset-metadata.json"


class ValidationError(RuntimeError):
    """Raised when repository validation fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def validate_json(path: Path) -> object:
    require(path.exists(), f"Missing JSON file: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValidationError(
            f"Invalid JSON in {path.relative_to(ROOT)}: {exc}"
        ) from exc


def validate_csv_resource(resource: dict[str, object]) -> tuple[int, int]:
    relative_path = Path(str(resource["path"]))
    path = ROOT / relative_path
    require(path.exists(), f"Missing CSV resource: {relative_path}")

    schema = resource.get("schema")
    require(isinstance(schema, dict), f"Missing schema for {relative_path}")
    fields = schema.get("fields")
    require(isinstance(fields, list) and fields, f"Missing fields for {relative_path}")

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        try:
            headers = next(reader)
        except StopIteration as exc:
            raise ValidationError(f"Empty CSV: {relative_path}") from exc
        rows = sum(1 for _ in reader)

    require(len(headers) == len(set(headers)), f"Duplicate CSV headers: {relative_path}")
    schema_names = [str(field.get("name", "")) for field in fields]
    require(headers == schema_names, f"Schema/header mismatch: {relative_path}")

    for field in fields:
        require(str(field.get("name", "")).strip(), f"Blank field name: {relative_path}")
        require(
            str(field.get("description", "")).strip(),
            f"Blank field description: {relative_path}/{field.get('name')}",
        )
        require(str(field.get("type", "")).strip(), f"Blank field type: {relative_path}")

    require(rows > 0, f"CSV has no data rows: {relative_path}")
    return rows, len(headers)


def validate_excel(path: Path) -> None:
    require(path.exists(), f"Missing Excel workbook: {path.relative_to(ROOT)}")
    require(zipfile.is_zipfile(path), f"Invalid XLSX container: {path.relative_to(ROOT)}")
    with zipfile.ZipFile(path) as workbook:
        require(workbook.testzip() is None, f"Corrupt XLSX file: {path.relative_to(ROOT)}")


def main() -> int:
    metadata = validate_json(METADATA_PATH)
    validate_json(ROOT / "metadata" / "kaggle-kernel-metadata.json")
    validate_json(ROOT / "metadata" / "project-metadata.json")

    notebook = validate_json(ROOT / "notebooks" / "Mokhles_HR_Analytics_EDA.ipynb")
    require(isinstance(notebook, dict), "Notebook root must be a JSON object.")
    require(notebook.get("nbformat") == 4, "Notebook must use nbformat 4.")
    require(isinstance(notebook.get("cells"), list), "Notebook cells are missing.")

    resources = metadata.get("resources")
    require(isinstance(resources, list) and resources, "No metadata resources found.")

    resource_paths = [str(resource.get("path", "")) for resource in resources]
    require(
        len(resource_paths) == len(set(resource_paths)),
        "Duplicate resource paths in metadata.",
    )

    csv_rows = 0
    csv_columns = 0
    csv_count = 0

    for resource in resources:
        resource_path = Path(str(resource.get("path", "")))
        full_path = ROOT / resource_path
        require(full_path.exists(), f"Missing metadata resource: {resource_path}")

        if resource_path.suffix.lower() == ".csv":
            rows, columns = validate_csv_resource(resource)
            csv_rows += rows
            csv_columns += columns
            csv_count += 1

    for workbook in (ROOT / "data" / "excel").rglob("*.xlsx"):
        validate_excel(workbook)

    require(csv_count == 13, f"Expected 13 CSV tables, found {csv_count}.")

    print("Repository validation passed.")
    print(f"CSV tables: {csv_count}")
    print(f"Combined CSV data rows: {csv_rows:,}")
    print(f"Documented CSV columns: {csv_columns}")
    print("Notebook JSON: valid")
    print("Excel workbooks: valid ZIP containers")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
