from pathlib import Path

import pytest

from pptx_to_docx_accessibility.config import WorkflowConfig
from pptx_to_docx_accessibility.errors import RenderError
from pptx_to_docx_accessibility.rendering import render_slide_images


def test_render_failure_is_warning_when_images_are_optional(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    def fail_render(*args: object, **kwargs: object) -> object:
        raise RenderError("boom")

    monkeypatch.setattr("pptx_to_docx_accessibility.rendering._render_slide_images", fail_render)
    config = WorkflowConfig(input_path=tmp_path / "deck.pptx", require_slide_images=False)

    result = render_slide_images(tmp_path / "deck.pptx", tmp_path / "images", config)

    assert result.images_by_slide == {}
    assert result.warnings[0].code == "SLIDE_IMAGE_RENDER_FAILED"


def test_render_failure_raises_when_images_are_required(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    def fail_render(*args: object, **kwargs: object) -> object:
        raise RenderError("boom")

    monkeypatch.setattr("pptx_to_docx_accessibility.rendering._render_slide_images", fail_render)
    config = WorkflowConfig(input_path=tmp_path / "deck.pptx", require_slide_images=True)

    with pytest.raises(RenderError):
        render_slide_images(tmp_path / "deck.pptx", tmp_path / "images", config)
