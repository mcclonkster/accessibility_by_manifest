from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PptxManifestConfig:
    input_path: Path
    output_root: Path | None = None
    recursive: bool = True
    overwrite: bool = False
    dry_run: bool = False
    include_slide_images: bool = True
    require_slide_images: bool = False
    render_dpi: int = 160
    libreoffice_path: Path = Path("/Applications/LibreOffice.app/Contents/MacOS/soffice")
    pdftoppm_path: Path = Path("/opt/homebrew/bin/pdftoppm")

    @property
    def should_render_images(self) -> bool:
        return self.include_slide_images
