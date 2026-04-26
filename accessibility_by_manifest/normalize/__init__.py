"""Normalization passes that turn evidence manifests into document models."""

from accessibility_by_manifest.normalize.accessibility_model import (
    MODEL_VERSION,
    NormalizedAccessibilityDocument,
    NormalizedBBox,
    NormalizedDocumentMetadata,
    NormalizedProjectionHints,
    NormalizedProvenance,
    NormalizedReviewEntry,
    NormalizedSourcePackage,
    NormalizedSummary,
    NormalizedTableCell,
    NormalizedTableEntry,
    NormalizedTableRow,
    NormalizedUnit,
)
from accessibility_by_manifest.normalize.docx_accessibility_model import (
    docx_ir_to_accessibility_model,
    normalize_docx_manifest_to_accessibility_model,
)
from accessibility_by_manifest.normalize.pdf_accessibility_model import normalize_pdf_manifest_to_accessibility_model

__all__ = [
    "MODEL_VERSION",
    "NormalizedAccessibilityDocument",
    "NormalizedBBox",
    "NormalizedDocumentMetadata",
    "NormalizedProjectionHints",
    "NormalizedProvenance",
    "NormalizedReviewEntry",
    "NormalizedSourcePackage",
    "NormalizedSummary",
    "NormalizedTableCell",
    "NormalizedTableEntry",
    "NormalizedTableRow",
    "NormalizedUnit",
    "docx_ir_to_accessibility_model",
    "normalize_docx_manifest_to_accessibility_model",
    "normalize_pdf_manifest_to_accessibility_model",
]
