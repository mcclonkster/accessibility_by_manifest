from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DeckRun:
    pptx_path: Path
    output_dir: Path


@dataclass(frozen=True)
class Script1Paths:
    companion_docx: Path
    manifest_json: Path
    manifest_yaml: Path
    extract_report: Path
    review_notes: Path


@dataclass(frozen=True)
class Script2Paths:
    remediated_docx: Path
    remediation_report: Path


def is_real_pptx(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() == ".pptx" and not path.name.startswith("~$")


def discover_pptx_files(input_path: Path, recursive: bool = True) -> list[Path]:
    if input_path.is_file():
        return [input_path] if is_real_pptx(input_path) else []

    pattern = "**/*.pptx" if recursive else "*.pptx"
    return sorted(path for path in input_path.glob(pattern) if is_real_pptx(path))


def safe_name(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._-")
    return cleaned or "deck"


def plan_runs(pptx_files: list[Path], input_path: Path, output_root: Path | None) -> list[DeckRun]:
    runs: list[DeckRun] = []
    used_dirs: set[Path] = set()
    batch_mode = input_path.is_dir()

    for pptx_path in pptx_files:
        if output_root is None:
            output_dir = pptx_path.parent / f"{pptx_path.stem}_workflow_output"
        elif batch_mode:
            output_dir = output_root / f"{safe_name(pptx_path.stem)}_workflow_output"
        else:
            output_dir = output_root

        if output_dir in used_dirs:
            parent_hint = safe_name(pptx_path.parent.name)
            output_dir = output_dir.parent / f"{safe_name(pptx_path.stem)}_{parent_hint}_workflow_output"

        suffix = 2
        original_output_dir = output_dir
        while output_dir in used_dirs:
            output_dir = original_output_dir.parent / f"{original_output_dir.name}_{suffix}"
            suffix += 1

        used_dirs.add(output_dir)
        runs.append(DeckRun(pptx_path=pptx_path, output_dir=output_dir))

    return runs


def script1_paths(run: DeckRun) -> Script1Paths:
    stem = run.pptx_path.stem
    return Script1Paths(
        companion_docx=run.output_dir / f"{stem}_companion.docx",
        manifest_json=run.output_dir / f"{stem}_extract_manifest.json",
        manifest_yaml=run.output_dir / f"{stem}_extract_manifest.yaml",
        extract_report=run.output_dir / f"{stem}_extract_report.md",
        review_notes=run.output_dir / f"{stem}_review_notes.md",
    )


def script2_paths(run: DeckRun) -> Script2Paths:
    stem = run.pptx_path.stem
    return Script2Paths(
        remediated_docx=run.output_dir / f"{stem}_remediated.docx",
        remediation_report=run.output_dir / f"{stem}_remediation_report.md",
    )
