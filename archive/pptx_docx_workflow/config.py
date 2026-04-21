from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class WorkflowOptions:
    input_path: Path
    output_root: Path | None = None
    preview_dir: Path | None = None
    recursive: bool = True
    include_slide_images: bool = True
    script1_only: bool = False
    require_slide_images: bool = False
    overwrite: bool = False
    dry_run: bool = False

    @property
    def auto_render_slide_images(self) -> bool:
        return self.include_slide_images and self.preview_dir is None
