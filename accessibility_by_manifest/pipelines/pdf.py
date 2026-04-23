from __future__ import annotations

from accessibility_by_manifest.inputs.pdf import build_manifest_from_pdf
from accessibility_by_manifest.inputs.pdf.config import PdfManifestConfig
from accessibility_by_manifest.inputs.pdf.paths import PdfOutputPaths, PdfRun, output_paths
from accessibility_by_manifest.outputs.adobe_reference import write_adobe_reference_comparison_if_available
from accessibility_by_manifest.outputs.manifest import write_pdf_manifest_bundle
from accessibility_by_manifest.outputs.pdf_docx import write_pdf_docx_output
from accessibility_by_manifest.pipeline import ManifestPipeline, ManifestPipelineResult


PdfManifestResult = ManifestPipelineResult[PdfRun, PdfOutputPaths, dict]


def run_pdf(config: PdfManifestConfig, run: PdfRun) -> PdfManifestResult:
    return pdf_manifest_pipeline().run(config, run)


def pdf_manifest_pipeline() -> ManifestPipeline[PdfManifestConfig, PdfRun, PdfOutputPaths, dict]:
    return ManifestPipeline(
        output_paths_for_run=output_paths,
        build_manifest=build_manifest_from_pdf,
        write_outputs=write_pdf_outputs,
        success_message=lambda _: "Manifest extracted and draft DOCX projected.",
    )


def write_pdf_outputs(context, manifest: dict) -> None:
    write_pdf_manifest_bundle(context.output_paths, manifest, context.config.overwrite)
    write_pdf_docx_output(manifest, context.output_paths, context.config.overwrite)
    write_adobe_reference_comparison_if_available(manifest, context.run, context.output_paths, context.config.overwrite)
