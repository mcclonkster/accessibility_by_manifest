from __future__ import annotations


class ManifestError(Exception):
    """Base class for user-facing manifest pipeline failures."""


class DependencyError(ManifestError):
    """Raised when a required runtime dependency is unavailable."""


class RenderError(ManifestError):
    """Raised when slide-image rendering fails and images are required."""


class ExtractionError(ManifestError):
    """Raised when a PPTX cannot be read or extracted."""


class OutputWriteError(ManifestError):
    """Raised when manifest outputs cannot be written."""
