from __future__ import annotations

import json
import tempfile
from dataclasses import dataclass
from pathlib import Path

from .config import PdfWorkflowConfig
from .extractors.pymupdf_adapter import PyMuPDFAdapter
from .manifest.builder import ManifestBuilder
from .manifest.validate import validate_manifest
from .paths import PdfOutputPaths, PdfRun, output_paths


@dataclass(frozen=True)
class PdfDeckResult:
    run: PdfRun
    output_paths: PdfOutputPaths
    ok: bool
    message: str
    manifest: dict | None = None


def run_pdf(config: PdfWorkflowConfig, run: PdfRun) -> PdfDeckResult:
    paths = output_paths(run)
    try:
        builder = ManifestBuilder(input_path=run.pdf_path, output_paths=paths, config=config)
        PyMuPDFAdapter().populate(builder)
        manifest = builder.build()
        validate_manifest(manifest)
        if not config.dry_run:
            run.output_dir.mkdir(parents=True, exist_ok=True)
            atomic_write_json(paths.manifest_json, manifest, config.overwrite)
        return PdfDeckResult(run=run, output_paths=paths, ok=True, message="Manifest extracted.", manifest=manifest)
    except Exception as exc:
        return PdfDeckResult(run=run, output_paths=paths, ok=False, message=str(exc))


def atomic_write_json(path: Path, data: dict, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Output already exists. Use --overwrite or choose another folder: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".json", dir=str(path.parent), prefix=f"{path.stem}_") as temp_file:
            temp_path = Path(temp_file.name)
        temp_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        temp_path.replace(path)
    except Exception:
        if temp_path and temp_path.exists():
            temp_path.unlink(missing_ok=True)
        raise
