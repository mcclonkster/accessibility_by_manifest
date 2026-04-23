from __future__ import annotations

from accessibility_by_manifest.inputs.docx import build_manifest_from_docx
from accessibility_by_manifest.inputs.docx.config import DocxManifestConfig
from accessibility_by_manifest.inputs.docx.paths import DocxOutputPaths, DocxRun, output_paths
from accessibility_by_manifest.outputs.docx_manifest import write_docx_manifest_outputs
from accessibility_by_manifest.pipeline import ManifestPipeline, ManifestPipelineResult


DocxManifestResult = ManifestPipelineResult[DocxRun, DocxOutputPaths, dict]


def run_docx(config: DocxManifestConfig, run: DocxRun) -> DocxManifestResult:
    return docx_manifest_pipeline().run(config, run)


def docx_manifest_pipeline() -> ManifestPipeline[DocxManifestConfig, DocxRun, DocxOutputPaths, dict]:
    return ManifestPipeline(
        output_paths_for_run=output_paths,
        build_manifest=build_manifest_from_docx,
        write_outputs=write_docx_outputs,
        success_message=lambda _: "DOCX manifest extracted.",
    )


def write_docx_outputs(context, manifest: dict) -> None:
    write_docx_manifest_outputs(context.output_paths, manifest, context.config.overwrite)
