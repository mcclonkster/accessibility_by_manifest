from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


def schema_path() -> Path:
    return Path(__file__).resolve().parents[2] / "reference" / "pdf_accessibility_manifest.json"


@lru_cache(maxsize=1)
def load_schema() -> dict[str, Any]:
    return json.loads(schema_path().read_text(encoding="utf-8"))


def validate_manifest(manifest: dict[str, Any]) -> None:
    Draft202012Validator(load_schema()).validate(manifest)
