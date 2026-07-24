"""Validate repository data, metadata, notebooks and document security."""

from __future__ import annotations

import csv
import json
import sys
import zipfile
from decimal import Decimal, InvalidOperation
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
ROOT_RESOLVED = ROOT.resolve()
METADATA_PATH = ROOT / "metadata" / "kaggle-dataset-metadata.json"

MAX_TEXT_BYTES = 25 * 1024 * 1024
MAX_XLSX_BYTES = 50 * 1024 * 1024
MAX_XLSX_UNCOMPRESSED_BYTES = 250 * 1024 * 1024
MAX_ZIP_ENTRIES = 10_000
MAX_CSV_ROWS = 2_000_000
MAX_CSV_FIELD_BYTES = 1_000_000

FORBIDDEN_XLSX_PARTS = (
    "xl/vbaproject.bin",
    "xl/activex/",
    "xl/embeddings/",
)
FORBIDDEN_NOTEBOOK_CALLS = {
    "shell command": "os.system(",
    "subprocess execution": "subprocess.",
    "dynamic eval": "eval(",
    "dynamic exec": "exec(",
    "unsafe pickle loading": "pickle.load(",
    "unsafe joblib loading": "joblib.load(",
}

csv.field_size_limit(MAX_CSV_FIELD_BYTES)


class ValidationError(RuntimeError):
    """Raised when repository validation fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT_RESOLVED).as_posix()
    except ValueError:
        return path.as_posix()


def resolve_repository_path(relative_path: Path) -> Path:
    require(not relative_path.is_absolute(), f"Absolute path is not allowed: {relative_path}")
    candidate = (ROOT / relative_path).resolve()
    require(
        candidate == ROOT_RESOLVED or ROOT_RESOLVED in candidate.parents,
        f"Path escapes repository root: {relative_path}",
    )
    return candidate


def require_file(path: Path, maximum_bytes: int, label: str) -> None:
    require(path.is_file(), f"Missing {label}: {display_path(path)}")
    require(
        path.stat().st_size <= maximum_bytes,
        f"{label} exceeds the safe size limit: {display_path(path)}",
    )


def validate_json(path: Path) -> object:
    require_file(path, MAX_TEXT_BYTES, "JSON file")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except UnicodeDecodeError as exc:
        raise ValidationError(f"JSON is not UTF-8: {display_path(path)}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Invalid JSON in {display_path(path)}: {exc}") from exc


def looks_like_spreadsheet_formula(value: str) -> bool:
    candidate = (value or "").lstrip("\ufeff\t\r\n ")
    if not candidate:
        return False
    if candidate[0] in {"=", "@"}:
        return True
    if candidate[0] not in {"+", "-"} or candidate in {"+", "-"}:
        return False
    try:
        Decimal(candidate.replace(",", ""))
        return False
    except InvalidOperation:
        return True


def validate_csv_resource(resource: dict[str, object]) -> tuple[int, int]:
    relative_text = str(resource.get("path", "")).strip()
    require(relative_text, "Metadata resource has a blank path.")
    relative_path = Path(relative_text)
    require(relative_path.suffix.lower() == ".csv", f"Expected CSV resource: {relative_path}")

    path = resolve_repository_path(relative_path)
    require_file(path, MAX_TEXT_BYTES, "CSV resource")

    schema = resource.get("schema")
    require(isinstance(schema, dict), f"Missing schema for {relative_path}")
    fields = schema.get("fields")
    require(isinstance(fields, list) and fields, f"Missing fields for {relative_path}")

    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.reader(handle)
            try:
                headers = next(reader)
            except StopIteration as exc:
                raise ValidationError(f"Empty CSV: {relative_path}") from exc

            require(headers, f"CSV has no headers: {relative_path}")
            require(len(headers) == len(set(headers)), f"Duplicate CSV headers: {relative_path}")
            require(
                not any(looks_like_spreadsheet_formula(header) for header in headers),
                f"Spreadsheet-formula-like CSV header: {relative_path}",
            )

            rows = 0
            for row_number, row in enumerate(reader, start=2):
                require(
                    len(row) == len(headers),
                    f"CSV column-count mismatch at {relative_path}:{row_number}",
                )
                for column, value in zip(headers, row):
                    require(
                        not looks_like_spreadsheet_formula(value),
                        f"Potential spreadsheet formula injection at "
                        f"{relative_path}:{row_number}/{column}",
                    )
                rows += 1
                require(rows <= MAX_CSV_ROWS, f"CSV row limit exceeded: {relative_path}")
    except UnicodeDecodeError as exc:
        raise ValidationError(f"CSV is not UTF-8: {relative_path}") from exc
    except csv.Error as exc:
        raise ValidationError(f"Invalid CSV in {relative_path}: {exc}") from exc

    schema_names = [
        str(field.get("name", ""))
        for field in fields
        if isinstance(field, dict)
    ]
    require(len(schema_names) == len(fields), f"Invalid field metadata: {relative_path}")
    require(headers == schema_names, f"Schema/header mismatch: {relative_path}")

    for field in fields:
        require(isinstance(field, dict), f"Invalid field metadata: {relative_path}")
        require(str(field.get("name", "")).strip(), f"Blank field name: {relative_path}")
        require(
            str(field.get("description", "")).strip(),
            f"Blank field description: {relative_path}/{field.get('name')}",
        )
        require(str(field.get("type", "")).strip(), f"Blank field type: {relative_path}")

    require(rows > 0, f"CSV has no data rows: {relative_path}")
    return rows, len(headers)


def validate_excel(path: Path) -> None:
    resolved = path.resolve()
    require(
        resolved == ROOT_RESOLVED or ROOT_RESOLVED in resolved.parents,
        f"Excel path escapes repository root: {display_path(path)}",
    )
    require_file(resolved, MAX_XLSX_BYTES, "Excel workbook")
    require(zipfile.is_zipfile(resolved), f"Invalid XLSX container: {display_path(resolved)}")

    try:
        with zipfile.ZipFile(resolved) as workbook:
            entries = workbook.infolist()
            require(
                len(entries) <= MAX_ZIP_ENTRIES,
                f"XLSX entry limit exceeded: {display_path(resolved)}",
            )

            total_uncompressed = 0
            for entry in entries:
                archive_path = PurePosixPath(entry.filename)
                require(
                    not archive_path.is_absolute() and ".." not in archive_path.parts,
                    f"Unsafe XLSX member path: {display_path(resolved)}/{entry.filename}",
                )
                total_uncompressed += entry.file_size
                require(
                    total_uncompressed <= MAX_XLSX_UNCOMPRESSED_BYTES,
                    f"XLSX expands beyond the safe limit: {display_path(resolved)}",
                )
                lowered = entry.filename.lower()
                require(
                    not any(
                        lowered == forbidden or lowered.startswith(forbidden)
                        for forbidden in FORBIDDEN_XLSX_PARTS
                    ),
                    f"Active XLSX content is not allowed: {display_path(resolved)}",
                )

            require(workbook.testzip() is None, f"Corrupt XLSX: {display_path(resolved)}")
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        raise ValidationError(f"Unsafe or invalid XLSX: {display_path(resolved)}") from exc


def validate_notebook(path: Path) -> None:
    notebook = validate_json(path)
    require(isinstance(notebook, dict), "Notebook root must be a JSON object.")
    require(notebook.get("nbformat") == 4, "Notebook must use nbformat 4.")
    cells = notebook.get("cells")
    require(isinstance(cells, list), "Notebook cells are missing.")

    for index, cell in enumerate(cells, start=1):
        require(isinstance(cell, dict), f"Notebook cell {index} must be an object.")
        if cell.get("cell_type") != "code":
            continue

        require(
            cell.get("execution_count") is None,
            f"Notebook code cell {index} must have cleared execution state.",
        )
        outputs = cell.get("outputs", [])
        require(
            isinstance(outputs, list) and not outputs,
            f"Notebook code cell {index} must not contain committed outputs.",
        )

        source = cell.get("source", [])
        code = "".join(str(part) for part in source) if isinstance(source, list) else str(source)
        lowered = code.lower()

        for line in lowered.splitlines():
            stripped = line.lstrip()
            require(
                not stripped.startswith("!"),
                f"Notebook code cell {index} contains a shell escape.",
            )
            require(
                not stripped.startswith(("%%bash", "%%powershell")),
                f"Notebook code cell {index} contains a shell cell magic.",
            )

        for label, pattern in FORBIDDEN_NOTEBOOK_CALLS.items():
            require(
                pattern not in lowered,
                f"Notebook code cell {index} contains forbidden {label}.",
            )


def main() -> int:
    metadata = validate_json(METADATA_PATH)
    validate_json(ROOT / "metadata" / "kaggle-kernel-metadata.json")
    validate_json(ROOT / "metadata" / "project-metadata.json")
    validate_notebook(ROOT / "notebooks" / "Mokhles_HR_Analytics_EDA.ipynb")

    require(isinstance(metadata, dict), "Dataset metadata root must be an object.")
    resources = metadata.get("resources")
    require(isinstance(resources, list) and resources, "No metadata resources found.")

    resource_paths: list[str] = []
    for resource in resources:
        require(isinstance(resource, dict), "Metadata resources must be objects.")
        resource_paths.append(str(resource.get("path", "")).strip())
    require(all(resource_paths), "Metadata resource paths must not be blank.")
    require(
        len(resource_paths) == len(set(resource_paths)),
        "Duplicate resource paths in metadata.",
    )

    csv_rows = 0
    csv_columns = 0
    csv_count = 0

    for resource in resources:
        assert isinstance(resource, dict)
        resource_path = Path(str(resource.get("path", "")))
        full_path = resolve_repository_path(resource_path)
        require(full_path.exists(), f"Missing metadata resource: {resource_path}")

        if resource_path.suffix.lower() == ".csv":
            rows, columns = validate_csv_resource(resource)
            csv_rows += rows
            csv_columns += columns
            csv_count += 1

    for workbook in (ROOT / "data" / "excel").rglob("*.xlsx"):
        validate_excel(workbook)

    require(csv_count == 13, f"Expected 13 CSV tables, found {csv_count}.")

    print("Repository security and integrity validation passed.")
    print(f"CSV tables: {csv_count}")
    print(f"Combined CSV data rows: {csv_rows:,}")
    print(f"Documented CSV columns: {csv_columns}")
    print("Notebook JSON and code policy: valid")
    print("Excel workbooks: bounded, passive and valid ZIP containers")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
