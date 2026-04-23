from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel


class WorkflowConfig(BaseModel):
    output_dir: Path
    render_pages: bool = False
    run_validator: bool = True
    allow_scaffold_writeback: bool = True

