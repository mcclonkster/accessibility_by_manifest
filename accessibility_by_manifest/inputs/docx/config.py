from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DocxManifestConfig:
    input_path: Path
    output_root: Path | None = None
    recursive: bool = True
    overwrite: bool = False
    dry_run: bool = False
    include_rebuild_payloads: bool = False
