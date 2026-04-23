from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel


def model_to_jsonable(value: BaseModel) -> dict[str, Any]:
    return value.model_dump(mode="json")


def write_json(path: Path, value: BaseModel | dict[str, Any] | list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(value, BaseModel):
        data: Any = model_to_jsonable(value)
    else:
        data = value
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def append_jsonl(path: Path, rows: list[BaseModel | dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for row in rows:
            data: Any = model_to_jsonable(row) if isinstance(row, BaseModel) else row
            handle.write(json.dumps(data, ensure_ascii=False) + "\n")

