from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PdfManifestConfig:
    input_path: Path
    output_root: Path | None = None
    recursive: bool = True
    overwrite: bool = False
    dry_run: bool = False
    ai_parser: str = "none"
    ai_parser_output_mode: str = "artifacts"
    ocr_parser: str = "none"
    include_preview_images: bool = False
    page_separator_mode: str = "PAGE_BREAK"
    include_warning_appendix: bool = True
    include_page_traceback: bool = True
    prefer_outline_for_headings: bool = True
    include_rebuild_payloads: bool = False
    include_char_level_evidence: bool = False
