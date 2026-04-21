from __future__ import annotations

import unittest
from pathlib import Path
from unittest.mock import patch

from pptx_docx_workflow.config import WorkflowOptions
from pptx_docx_workflow.dependencies import check_dependencies


class DependencyTests(unittest.TestCase):
    def test_render_tools_are_not_required_when_slide_images_are_disabled(self) -> None:
        options = WorkflowOptions(input_path=Path("deck.pptx"), include_slide_images=False)

        with patch("pptx_docx_workflow.dependencies.module_available", return_value=True), patch(
            "pptx_docx_workflow.dependencies.executable_available", return_value=False
        ) as executable_available:
            report = check_dependencies(options)

        self.assertTrue(report.ok)
        executable_available.assert_not_called()

    def test_render_tools_are_required_for_auto_rendering(self) -> None:
        options = WorkflowOptions(input_path=Path("deck.pptx"), include_slide_images=True, preview_dir=None)

        with patch("pptx_docx_workflow.dependencies.module_available", return_value=True), patch(
            "pptx_docx_workflow.dependencies.executable_available", return_value=False
        ):
            report = check_dependencies(options)

        self.assertFalse(report.ok)
        self.assertEqual(len(report.errors), 2)

    def test_preview_dir_avoids_render_tool_requirement(self) -> None:
        options = WorkflowOptions(input_path=Path("deck.pptx"), include_slide_images=True, preview_dir=Path("images"))

        with patch("pptx_docx_workflow.dependencies.module_available", return_value=True), patch(
            "pptx_docx_workflow.dependencies.executable_available", return_value=False
        ) as executable_available:
            report = check_dependencies(options)

        self.assertTrue(report.ok)
        executable_available.assert_not_called()


if __name__ == "__main__":
    unittest.main()
