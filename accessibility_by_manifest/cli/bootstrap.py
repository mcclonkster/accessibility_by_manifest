from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path


REQUIRED_MODULES = ("pptx", "docx", "yaml")


def missing_required_modules() -> list[str]:
    return [module_name for module_name in REQUIRED_MODULES if importlib.util.find_spec(module_name) is None]


def project_venv_python() -> Path:
    return Path(__file__).resolve().parents[2] / ".venv" / "bin" / "python"


def maybe_reexec_project_venv() -> None:
    if not missing_required_modules():
        return

    venv_python = project_venv_python()
    if not venv_python.exists():
        return

    current_python = Path(sys.executable).absolute()
    target_python = venv_python.absolute()
    if current_python == target_python:
        return

    os.execv(str(target_python), [str(target_python), "-m", "accessibility_by_manifest.cli.pptx", *sys.argv[1:]])
