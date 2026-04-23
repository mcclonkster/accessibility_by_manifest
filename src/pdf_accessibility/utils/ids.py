from __future__ import annotations

import hashlib
from pathlib import Path


def stable_id(*parts: object) -> str:
    raw = "|".join(str(part) for part in parts)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


def document_id_for_path(path: Path) -> str:
    return f"doc-{stable_id(path.name, path.stat().st_size if path.exists() else 0)}"


def event_id(node_name: str, *parts: object) -> str:
    return f"evt-{node_name}-{stable_id(*parts)}"

