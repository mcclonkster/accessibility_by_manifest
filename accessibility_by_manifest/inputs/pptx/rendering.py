from __future__ import annotations

import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

from .config import PptxManifestConfig
from accessibility_by_manifest.errors import RenderError
from accessibility_by_manifest.manifest.pptx import WarningEntry


@dataclass(frozen=True)
class RenderResult:
    image_dir: Path | None
    images_by_slide: dict[int, Path]
    warnings: tuple[WarningEntry, ...] = ()


def render_slide_images(pptx_path: Path, image_dir: Path, config: PptxManifestConfig) -> RenderResult:
    if not config.include_slide_images:
        return RenderResult(image_dir=None, images_by_slide={})
    if config.dry_run:
        return RenderResult(image_dir=image_dir, images_by_slide={})

    try:
        return _render_slide_images(pptx_path, image_dir, config)
    except Exception as exc:
        warning = WarningEntry(
            code="SLIDE_IMAGE_RENDER_FAILED",
            message=f"Slide image rendering failed: {exc}",
            scope="deck",
            manual_review_required=True,
        )
        if config.require_slide_images:
            raise RenderError(warning.message) from exc
        return RenderResult(image_dir=None, images_by_slide={}, warnings=(warning,))


def _resolve_executable(configured: Path, command_name: str) -> Path:
    if configured.exists():
        return configured
    found = shutil.which(command_name)
    if found:
        return Path(found)
    raise RenderError(f"Required renderer executable not found: {configured} or {command_name} on PATH.")


def _render_slide_images(pptx_path: Path, image_dir: Path, config: PptxManifestConfig) -> RenderResult:
    soffice = _resolve_executable(config.libreoffice_path, "soffice")
    pdftoppm = _resolve_executable(config.pdftoppm_path, "pdftoppm")

    image_dir.mkdir(parents=True, exist_ok=True)
    for old_image in image_dir.glob("slide_*.png"):
        old_image.unlink()

    with tempfile.TemporaryDirectory(prefix="manifest_render_") as temp_root:
        temp_root_path = Path(temp_root)
        pdf_dir = temp_root_path / "pdf"
        profile_dir = temp_root_path / "lo_profile"
        pdf_dir.mkdir(parents=True, exist_ok=True)
        profile_dir.mkdir(parents=True, exist_ok=True)

        _run_command(
            [
                str(soffice),
                f"-env:UserInstallation={profile_dir.resolve().as_uri()}",
                "--headless",
                "--convert-to",
                "pdf",
                "--outdir",
                str(pdf_dir),
                str(pptx_path),
            ],
            "LibreOffice PPTX-to-PDF conversion failed",
        )

        pdf_candidates = sorted(pdf_dir.glob("*.pdf"))
        if not pdf_candidates:
            raise RenderError("LibreOffice did not produce a PDF.")
        pdf_path = pdf_candidates[0]

        image_prefix = temp_root_path / "slide"
        _run_command(
            [str(pdftoppm), "-r", str(config.render_dpi), "-png", str(pdf_path), str(image_prefix)],
            "PDF-to-PNG rasterization failed",
        )

        rendered_pages = sorted(temp_root_path.glob("slide-*.png"))
        if not rendered_pages:
            raise RenderError("pdftoppm did not produce slide images.")

        images_by_slide: dict[int, Path] = {}
        for index, page in enumerate(rendered_pages, start=1):
            target = image_dir / f"slide_{index:03d}.png"
            page.replace(target)
            images_by_slide[index] = target

    return RenderResult(image_dir=image_dir, images_by_slide=images_by_slide)


def _run_command(command: list[str], failure_prefix: str) -> None:
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or str(exc)).strip()
        raise RenderError(f"{failure_prefix}: {detail}") from exc
