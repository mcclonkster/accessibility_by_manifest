"""Compatibility wrapper for the packaged CLI."""

from __future__ import annotations

import sys

from accessibility_by_manifest.cli.bootstrap import maybe_reexec_project_venv

maybe_reexec_project_venv()

from accessibility_by_manifest.cli.pptx import main


if __name__ == "__main__":
    sys.exit(main())
