from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DocxRun:
    docx_path: Path
    output_dir: Path


@dataclass(frozen=True)
class DocxOutputPaths:
    manifest_json: Path
    normalized_manifest_json: Path
    log_file: Path


def is_real_docx(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() == ".docx" and not path.name.startswith("~$")


def discover_docx_files(input_path: Path, recursive: bool) -> list[Path]:
    if input_path.is_file():
        return [input_path] if is_real_docx(input_path) else []
    pattern = "**/*.docx" if recursive else "*.docx"
    return sorted(path for path in input_path.glob(pattern) if is_real_docx(path))


def safe_name(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._-")
    return cleaned or "document"


def plan_runs(docx_files: list[Path], input_path: Path, output_root: Path | None) -> list[DocxRun]:
    runs: list[DocxRun] = []
    used_dirs: set[Path] = set()
    batch_mode = input_path.is_dir()

    for docx_path in docx_files:
        if output_root is None:
            output_dir = docx_path.parent / f"{docx_path.stem}_docx_manifest_output"
        elif batch_mode:
            output_dir = output_root / f"{safe_name(docx_path.stem)}_docx_manifest_output"
        else:
            output_dir = output_root

        suffix = 2
        original = output_dir
        while output_dir in used_dirs:
            output_dir = original.parent / f"{original.name}_{suffix}"
            suffix += 1

        used_dirs.add(output_dir)
        runs.append(DocxRun(docx_path=docx_path, output_dir=output_dir))
    return runs


def output_paths(run: DocxRun) -> DocxOutputPaths:
    stem = run.docx_path.stem
    return DocxOutputPaths(
        manifest_json=run.output_dir / f"{stem}_docx_manifest.json",
        normalized_manifest_json=run.output_dir / f"{stem}_docx_normalized_ir.json",
        log_file=run.output_dir / f"{stem}.log",
    )
