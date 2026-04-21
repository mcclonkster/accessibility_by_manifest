from __future__ import annotations

import importlib.util
import shutil
from dataclasses import dataclass
from pathlib import Path

from .config import WorkflowOptions


DEFAULT_LIBREOFFICE = Path("/Applications/LibreOffice.app/Contents/MacOS/soffice")
DEFAULT_PDFTOPPM = Path("/opt/homebrew/bin/pdftoppm")


@dataclass(frozen=True)
class DependencyReport:
    errors: tuple[str, ...]
    warnings: tuple[str, ...] = ()

    @property
    def ok(self) -> bool:
        return not self.errors


def module_available(module_name: str) -> bool:
    return importlib.util.find_spec(module_name) is not None


def executable_available(path: Path, command_name: str) -> bool:
    return path.exists() or shutil.which(command_name) is not None


def check_dependencies(options: WorkflowOptions) -> DependencyReport:
    errors: list[str] = []

    required_modules = {
        "pptx": "python-pptx",
        "docx": "python-docx",
        "yaml": "PyYAML",
    }
    for module_name, package_name in required_modules.items():
        if not module_available(module_name):
            errors.append(f"Missing Python package '{package_name}' importable as '{module_name}'.")

    if options.auto_render_slide_images and not options.dry_run:
        if not executable_available(DEFAULT_LIBREOFFICE, "soffice"):
            errors.append(
                "Missing LibreOffice command for slide rendering. "
                f"Expected '{DEFAULT_LIBREOFFICE}' or a 'soffice' command on PATH."
            )
        if not executable_available(DEFAULT_PDFTOPPM, "pdftoppm"):
            errors.append(
                "Missing pdftoppm command for slide rendering. "
                f"Expected '{DEFAULT_PDFTOPPM}' or a 'pdftoppm' command on PATH."
            )

    return DependencyReport(errors=tuple(errors))
