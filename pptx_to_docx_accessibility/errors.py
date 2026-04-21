from __future__ import annotations


class WorkflowError(Exception):
    """Base class for user-facing workflow failures."""


class DependencyError(WorkflowError):
    """Raised when a required runtime dependency is unavailable."""


class RenderError(WorkflowError):
    """Raised when slide-image rendering fails and images are required."""


class ExtractionError(WorkflowError):
    """Raised when a PPTX cannot be read or extracted."""


class OutputWriteError(WorkflowError):
    """Raised when workflow outputs cannot be written."""
