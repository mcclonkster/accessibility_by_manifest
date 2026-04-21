from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PdfRun:
    pdf_path: Path
    output_dir: Path


@dataclass(frozen=True)
class PdfOutputPaths:
    manifest_json: Path
    extractor_manifest_dir: Path
    normalized_manifest_json: Path
    review_queue_json: Path
    projected_docx: Path
    preview_image_dir: Path

    def extractor_manifest_json(self, extractor_name: str) -> Path:
        stem = self.manifest_json.stem.removesuffix("_manifest")
        extractor_slug = safe_name(extractor_name.replace(".", "_")).lower()
        return self.extractor_manifest_dir / f"{stem}_{extractor_slug}_manifest.json"


def is_real_pdf(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() == ".pdf" and not path.name.startswith("~$")


def discover_pdf_files(input_path: Path, recursive: bool) -> list[Path]:
    if input_path.is_file():
        return [input_path] if is_real_pdf(input_path) else []
    pattern = "**/*.pdf" if recursive else "*.pdf"
    return sorted(path for path in input_path.glob(pattern) if is_real_pdf(path))


def safe_name(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._-")
    return cleaned or "document"


def plan_runs(pdf_files: list[Path], input_path: Path, output_root: Path | None) -> list[PdfRun]:
    runs: list[PdfRun] = []
    used_dirs: set[Path] = set()
    batch_mode = input_path.is_dir()

    for pdf_path in pdf_files:
        if output_root is None:
            output_dir = pdf_path.parent / f"{pdf_path.stem}_manifest_output"
        elif batch_mode:
            output_dir = output_root / f"{safe_name(pdf_path.stem)}_manifest_output"
        else:
            output_dir = output_root

        suffix = 2
        original = output_dir
        while output_dir in used_dirs:
            output_dir = original.parent / f"{original.name}_{suffix}"
            suffix += 1

        used_dirs.add(output_dir)
        runs.append(PdfRun(pdf_path=pdf_path, output_dir=output_dir))
    return runs


def output_paths(run: PdfRun) -> PdfOutputPaths:
    stem = run.pdf_path.stem
    return PdfOutputPaths(
        manifest_json=run.output_dir / f"{stem}_manifest.json",
        extractor_manifest_dir=run.output_dir / f"{stem}_extractor_manifests",
        normalized_manifest_json=run.output_dir / f"{stem}_normalized_manifest.json",
        review_queue_json=run.output_dir / f"{stem}_review_queue.json",
        projected_docx=run.output_dir / f"{stem}_draft.docx",
        preview_image_dir=run.output_dir / f"{stem}_page_images",
    )
