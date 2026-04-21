"""PPTX input adapter."""

from __future__ import annotations

from accessibility_by_manifest.inputs.pptx.config import PptxManifestConfig
from accessibility_by_manifest.inputs.pptx.extraction import extract_manifest
from accessibility_by_manifest.inputs.pptx.paths import DeckRun, OutputPaths
from accessibility_by_manifest.inputs.pptx.rendering import render_slide_images
from accessibility_by_manifest.manifest.pptx import Manifest
from accessibility_by_manifest.pipeline import ManifestPipelineContext


def build_manifest_from_pptx(context: ManifestPipelineContext[PptxManifestConfig, DeckRun, OutputPaths]) -> Manifest:
    render_result = render_slide_images(context.run.pptx_path, context.output_paths.slide_image_dir, context.config)
    return extract_manifest(context.run.pptx_path, context.output_paths.companion_docx, render_result)
