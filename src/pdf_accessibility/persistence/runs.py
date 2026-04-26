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
    inputs_dir: Path
    outputs_dir: Path
    metrics_dir: Path
    page_images_dir: Path
    checkpoints_dir: Path
    artifacts_dir: Path
    logs_dir: Path


def create_run(source_pdf: Path, output_dir: Path) -> RunContext:
    source_pdf = source_pdf.resolve()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_id = f"{source_pdf.stem}_{timestamp}"
    run_dir = output_dir.resolve() / run_id
    inputs_dir = run_dir / "inputs"
    outputs_dir = run_dir / "outputs"
    metrics_dir = run_dir / "metrics"
    page_images_dir = run_dir / "page_images"
    checkpoints_dir = run_dir / "checkpoints"
    artifacts_dir = run_dir / "artifacts"
    logs_dir = run_dir / "logs"
    for path in (inputs_dir, outputs_dir, metrics_dir, page_images_dir, checkpoints_dir, artifacts_dir, logs_dir):
        path.mkdir(parents=True, exist_ok=True)
    input_pdf = run_dir / "input.pdf"
    if source_pdf != input_pdf:
        shutil.copyfile(source_pdf, input_pdf)
    return RunContext(
        run_id=run_id,
        source_pdf=source_pdf,
        run_dir=run_dir,
        input_pdf=input_pdf,
        inputs_dir=inputs_dir,
        outputs_dir=outputs_dir,
        metrics_dir=metrics_dir,
        page_images_dir=page_images_dir,
        checkpoints_dir=checkpoints_dir,
        artifacts_dir=artifacts_dir,
        logs_dir=logs_dir,
    )


def initial_document_state(context: RunContext) -> DocumentState:
    return DocumentState(
        document_id=document_id_for_path(context.input_pdf),
        source_path=context.input_pdf,
        run_dir=context.run_dir,
    )
