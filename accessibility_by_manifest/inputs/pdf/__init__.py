"""PDF input adapter."""

from __future__ import annotations

from accessibility_by_manifest.inputs.pdf.config import PdfManifestConfig
from accessibility_by_manifest.inputs.pdf.extractors.ai_parsers.docling import DoclingAdapter
from accessibility_by_manifest.inputs.pdf.extractors.ai_parsers.doctr import DoctrOcrAdapter
from accessibility_by_manifest.inputs.pdf.extractors.pdfminer import PdfminerAdapter
from accessibility_by_manifest.inputs.pdf.extractors.pikepdf import PikepdfAdapter
from accessibility_by_manifest.inputs.pdf.extractors.pymupdf import PyMuPDFAdapter
from accessibility_by_manifest.inputs.pdf.extractors.pypdf import PypdfAdapter
from accessibility_by_manifest.inputs.pdf.paths import PdfOutputPaths, PdfRun
from accessibility_by_manifest.manifest.pdf_builder import ManifestBuilder
from accessibility_by_manifest.manifest.pdf_validate import validate_manifest
from accessibility_by_manifest.normalize.pdf import normalize_pdf_manifest
from accessibility_by_manifest.pipeline import ManifestPipelineContext
from accessibility_by_manifest.review.pdf import review_pdf_manifest
from accessibility_by_manifest.util.logging import get_logger


logger = get_logger("inputs.pdf")


def build_manifest_from_pdf(context: ManifestPipelineContext[PdfManifestConfig, PdfRun, PdfOutputPaths]) -> dict:
    logger.info("PDF manifest build started: %s", context.run.pdf_path)
    builder = ManifestBuilder(input_path=context.run.pdf_path, output_paths=context.output_paths, config=context.config)
    logger.info("Running PyMuPDF extractor")
    PyMuPDFAdapter().populate(builder)
    logger.info("Running pypdf extractor")
    PypdfAdapter().populate(builder)
    logger.info("Running pikepdf extractor")
    PikepdfAdapter().populate(builder)
    logger.info("Running pdfminer.six extractor")
    PdfminerAdapter().populate(builder)
    if context.config.ocr_parser == "doctr":
        logger.info("Running doctr OCR sidecar parser")
        DoctrOcrAdapter().populate(builder)
    elif context.config.ocr_parser != "none":
        raise ValueError(f"Unsupported PDF OCR parser: {context.config.ocr_parser}")
    if context.config.ai_parser == "docling":
        logger.info("Running Docling sidecar parser")
        DoclingAdapter().populate(builder)
    elif context.config.ai_parser != "none":
        raise ValueError(f"Unsupported PDF AI parser: {context.config.ai_parser}")
    logger.info("Building master manifest from extractor evidence")
    manifest = builder.build()
    logger.info("Normalizing PDF manifest")
    manifest = normalize_pdf_manifest(manifest)
    logger.info("Reviewing normalized PDF manifest")
    manifest = review_pdf_manifest(manifest)
    logger.info("Validating PDF manifest schema")
    validate_manifest(manifest)
    if builder.debug_evidence and not context.config.dry_run:
        manifest["_debug_evidence"] = builder.debug_evidence
    logger.info(
        "PDF manifest build completed: pages=%s raw_blocks=%s normalized_blocks=%s review_entries=%s",
        manifest.get("document_summary", {}).get("total_pages"),
        manifest.get("document_summary", {}).get("raw_block_count"),
        manifest.get("document_summary", {}).get("normalized_block_count"),
        len(manifest.get("review_entries", [])),
    )
    return manifest
