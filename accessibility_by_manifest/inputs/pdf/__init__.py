"""PDF input adapter."""

from __future__ import annotations

from accessibility_by_manifest.inputs.pdf.config import PdfManifestConfig
from accessibility_by_manifest.inputs.pdf.extractors.pdfminer import PdfminerAdapter
from accessibility_by_manifest.inputs.pdf.extractors.pikepdf import PikepdfAdapter
from accessibility_by_manifest.inputs.pdf.extractors.pymupdf import PyMuPDFAdapter
from accessibility_by_manifest.inputs.pdf.extractors.pypdf import PypdfAdapter
from accessibility_by_manifest.inputs.pdf.paths import PdfOutputPaths, PdfRun
from accessibility_by_manifest.manifest.pdf_builder import ManifestBuilder
from accessibility_by_manifest.manifest.pdf_validate import validate_manifest
from accessibility_by_manifest.pipeline import ManifestPipelineContext


def build_manifest_from_pdf(context: ManifestPipelineContext[PdfManifestConfig, PdfRun, PdfOutputPaths]) -> dict:
    builder = ManifestBuilder(input_path=context.run.pdf_path, output_paths=context.output_paths, config=context.config)
    PyMuPDFAdapter().populate(builder)
    PypdfAdapter().populate(builder)
    PikepdfAdapter().populate(builder)
    PdfminerAdapter().populate(builder)
    manifest = builder.build()
    validate_manifest(manifest)
    return manifest
