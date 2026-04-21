from __future__ import annotations

import sys

from .bootstrap import maybe_reexec_project_venv

maybe_reexec_project_venv()

from .cli import main


if __name__ == "__main__":
    sys.exit(main())
