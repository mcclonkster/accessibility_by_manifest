from accessibility_by_manifest.inputs.pptx.text_utils import clean_text


def test_clean_text_removes_xml_illegal_control_characters() -> None:
    assert clean_text("good\x00 text\x08\nnext") == "good text next"


def test_clean_text_normalizes_whitespace() -> None:
    assert clean_text("  one\t\t two \n three  ") == "one two three"
