from __future__ import annotations

from accessibility_by_manifest.outputs.docx import write_docx_outputs
from accessibility_by_manifest.outputs.manifest import write_json_manifest, write_yaml_manifest
from accessibility_by_manifest.outputs.markdown import write_markdown_outputs
from accessibility_by_manifest.outputs.reports import write_review_outputs
from accessibility_by_manifest.pipeline import ManifestPipelineContext

from accessibility_by_manifest.inputs.pptx.config import PptxManifestConfig
from accessibility_by_manifest.inputs.pptx.paths import DeckRun, OutputPaths
from accessibility_by_manifest.manifest.pptx import Manifest


def write_review_bundle_from_manifest(
    context: ManifestPipelineContext[PptxManifestConfig, DeckRun, OutputPaths],
    manifest: Manifest,
) -> None:
    context.run.output_dir.mkdir(parents=True, exist_ok=True)
    data = manifest.to_dict()
    write_json_manifest(context.output_paths.manifest_json, data, context.config.overwrite)
    write_yaml_manifest(context.output_paths.manifest_yaml, data, context.config.overwrite)
    write_docx_outputs(manifest, context.output_paths, context.config.overwrite)
    write_markdown_outputs(manifest, context.output_paths, context.config.overwrite)
    write_review_outputs(manifest, context.output_paths, context.config.overwrite)
