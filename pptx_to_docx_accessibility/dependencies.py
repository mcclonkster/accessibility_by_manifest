from __future__ import annotations

import importlib.util
import shutil
from dataclasses import dataclass
from pathlib import Path

from .config import WorkflowConfig


@dataclass(frozen=True)
class DependencyReport:
    errors: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.errors


def module_available(module_name: str) -> bool:
    return importlib.util.find_spec(module_name) is not None


def executable_available(path: Path, command_name: str) -> bool:
    return path.exists() or shutil.which(command_name) is not None


def check_dependencies(config: WorkflowConfig) -> DependencyReport:
    errors: list[str] = []
    for module_name, package_name in {
        "pptx": "python-pptx",
        "docx": "python-docx",
        "yaml": "PyYAML",
    }.items():
        if not module_available(module_name):
            errors.append(f"Missing Python package '{package_name}' importable as '{module_name}'.")

    if config.include_slide_images and config.require_slide_images and not config.dry_run:
        if not executable_available(config.libreoffice_path, "soffice"):
            errors.append(f"Missing LibreOffice renderer: {config.libreoffice_path}")
        if not executable_available(config.pdftoppm_path, "pdftoppm"):
            errors.append(f"Missing pdftoppm renderer: {config.pdftoppm_path}")

    return DependencyReport(errors=tuple(errors))
