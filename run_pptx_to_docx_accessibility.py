"""Compatibility wrapper for the packaged CLI."""

from __future__ import annotations

import sys

from pptx_to_docx_accessibility.bootstrap import maybe_reexec_project_venv

maybe_reexec_project_venv()

from pptx_to_docx_accessibility.cli import main


if __name__ == "__main__":
    sys.exit(main())
