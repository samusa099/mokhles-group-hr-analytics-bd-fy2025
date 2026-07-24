"""Validate the structured analytics workspace."""

from __future__ import annotations

from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]


def validate():
    metadata_path = ROOT / "dataset-metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    errors = []

    for resource in metadata.get("resources", []):
        path = ROOT / resource["path"]
        if not path.is_file():
            errors.append(f"Missing resource: {resource['path']}")
            continue
        if not resource.get("description", "").strip():
            errors.append(f"Missing file description: {resource['path']}")

        if resource["path"].lower().endswith(".csv"):
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                headers = next(csv.reader(handle))
            fields = resource.get("schema", {}).get("fields", [])
            if headers != [field.get("name") for field in fields]:
                errors.append(f"CSV schema mismatch: {resource['path']}")
            for field in fields:
                if not field.get("description", "").strip():
                    errors.append(
                        f"Missing field description: {resource['path']}::{field.get('name')}"
                    )

    if len(metadata.get("keywords", [])) < 10:
        errors.append("Dataset tags are incomplete.")

    if errors:
        raise RuntimeError("\n".join(errors))

    print(
        f"Validation passed: {len(metadata.get('resources', []))} resources."
    )


if __name__ == "__main__":
    validate()
