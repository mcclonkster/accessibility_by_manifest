from __future__ import annotations

from accessibility_by_manifest.inputs.docx.config import DocxManifestConfig
from accessibility_by_manifest.inputs.docx.paths import DocxOutputPaths, DocxRun
from accessibility_by_manifest.manifest.docx_builder import build_docx_manifest
from accessibility_by_manifest.pipeline import ManifestPipelineContext


def build_manifest_from_docx(context: ManifestPipelineContext[DocxManifestConfig, DocxRun, DocxOutputPaths]) -> dict:
    return build_docx_manifest(
        context.run.docx_path,
        context.output_paths,
        include_rebuild_payloads=context.config.include_rebuild_payloads,
    )
