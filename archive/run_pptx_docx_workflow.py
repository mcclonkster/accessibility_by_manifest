"""Compatibility wrapper for the packaged workflow CLI."""

from __future__ import annotations

import sys

from pptx_docx_workflow.bootstrap import maybe_reexec_project_venv

maybe_reexec_project_venv()

from pptx_docx_workflow.cli import main


if __name__ == "__main__":
    sys.exit(main())
