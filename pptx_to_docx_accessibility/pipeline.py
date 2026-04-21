from __future__ import annotations

from dataclasses import dataclass

from .config import WorkflowConfig
from .docx_writer import write_companion_docx, write_slides_docx
from .errors import WorkflowError
from .extraction import extract_manifest
from .markdown_writer import write_slides_markdown
from .models import Manifest
from .paths import DeckRun, OutputPaths, output_paths
from .rendering import render_slide_images
from .reports import write_manifest_files, write_reports


@dataclass(frozen=True)
class DeckResult:
    deck: DeckRun
    output_paths: OutputPaths
    ok: bool
    message: str
    manifest: Manifest | None = None


def run_deck(config: WorkflowConfig, deck: DeckRun) -> DeckResult:
    paths = output_paths(deck)
    if config.dry_run:
        return dry_run_deck(config, deck, paths)

    try:
        deck.output_dir.mkdir(parents=True, exist_ok=True)
        render_result = render_slide_images(deck.pptx_path, paths.slide_image_dir, config)
        manifest = extract_manifest(deck.pptx_path, paths.companion_docx, render_result)
        write_manifest_files(manifest, paths, config.overwrite)
        write_companion_docx(manifest, paths, config.overwrite)
        write_slides_docx(manifest, paths, config.overwrite)
        write_slides_markdown(manifest, paths, config.overwrite)
        write_reports(manifest, paths, config.overwrite)
        message = "Completed with warnings. Manual review is required." if manifest.summary()["slides_with_warnings"] else "Completed."
        return DeckResult(deck=deck, output_paths=paths, ok=True, message=message, manifest=manifest)
    except WorkflowError as exc:
        return DeckResult(deck=deck, output_paths=paths, ok=False, message=str(exc))
    except Exception as exc:
        return DeckResult(deck=deck, output_paths=paths, ok=False, message=f"Unexpected failure: {exc}")


def dry_run_deck(config: WorkflowConfig, deck: DeckRun, paths: OutputPaths) -> DeckResult:
    try:
        render_result = render_slide_images(deck.pptx_path, paths.slide_image_dir, config)
        manifest = extract_manifest(deck.pptx_path, paths.companion_docx, render_result)
        return DeckResult(
            deck=deck,
            output_paths=paths,
            ok=True,
            message="Dry run completed. No files were written.",
            manifest=manifest,
        )
    except WorkflowError as exc:
        return DeckResult(deck=deck, output_paths=paths, ok=False, message=str(exc))
    except Exception as exc:
        return DeckResult(deck=deck, output_paths=paths, ok=False, message=f"Unexpected failure: {exc}")
