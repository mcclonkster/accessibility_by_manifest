from __future__ import annotations

from pathlib import Path

import fitz


def get_page_count(pdf_path: Path) -> int:
    with fitz.open(pdf_path) as pdf:
        return pdf.page_count

