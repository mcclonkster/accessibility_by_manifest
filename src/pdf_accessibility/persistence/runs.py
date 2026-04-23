from __future__ import annotations

import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from pdf_accessibility.models.state import DocumentState
from pdf_accessibility.utils.ids import document_id_for_path


@dataclass(frozen=True)
class RunContext:
    run_id: str
    source_pdf: Path
    run_dir: Path
    input_pdf: Path
    page_images_dir: Path
    checkpoints_dir: Path
    artifacts_dir: Path


def create_run(source_pdf: Path, output_dir: Path) -> RunContext:
    source_pdf = source_pdf.resolve()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_id = f"{source_pdf.stem}_{timestamp}"
    run_dir = output_dir.resolve() / run_id
    page_images_dir = run_dir / "page_images"
    checkpoints_dir = run_dir / "checkpoints"
    artifacts_dir = run_dir / "artifacts"
    for path in (page_images_dir, checkpoints_dir, artifacts_dir):
        path.mkdir(parents=True, exist_ok=True)
    input_pdf = run_dir / "input.pdf"
    if source_pdf != input_pdf:
        shutil.copyfile(source_pdf, input_pdf)
    return RunContext(
        run_id=run_id,
        source_pdf=source_pdf,
        run_dir=run_dir,
        input_pdf=input_pdf,
        page_images_dir=page_images_dir,
        checkpoints_dir=checkpoints_dir,
        artifacts_dir=artifacts_dir,
    )


def initial_document_state(context: RunContext) -> DocumentState:
    return DocumentState(
        document_id=document_id_for_path(context.input_pdf),
        source_path=context.input_pdf,
        run_dir=context.run_dir,
    )

