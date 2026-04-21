from __future__ import annotations

from accessibility_by_manifest.inputs.pptx import build_manifest_from_pptx
from accessibility_by_manifest.inputs.pptx.config import PptxManifestConfig
from accessibility_by_manifest.inputs.pptx.paths import DeckRun, OutputPaths, output_paths
from accessibility_by_manifest.errors import ManifestError
from accessibility_by_manifest.manifest.pptx import Manifest
from accessibility_by_manifest.outputs.review_bundle import write_review_bundle_from_manifest
from accessibility_by_manifest.pipeline import ManifestPipeline, ManifestPipelineResult


DeckResult = ManifestPipelineResult[DeckRun, OutputPaths, Manifest]


def run_deck(config: PptxManifestConfig, deck: DeckRun) -> DeckResult:
    return pptx_manifest_pipeline().run(config, deck)


def pptx_manifest_pipeline() -> ManifestPipeline[PptxManifestConfig, DeckRun, OutputPaths, Manifest]:
    return ManifestPipeline(
        output_paths_for_run=output_paths,
        build_manifest=build_manifest_from_pptx,
        write_outputs=write_review_bundle_from_manifest,
        success_message=pptx_success_message,
        error_message=pptx_error_message,
    )


def pptx_success_message(manifest: Manifest) -> str:
    if manifest.summary()["slides_with_warnings"]:
        return "Completed with warnings. Manual review is required."
    return "Completed."


def pptx_error_message(exc: Exception) -> str:
    if isinstance(exc, ManifestError):
        return str(exc)
    return f"Unexpected failure: {exc}"
