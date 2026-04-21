from pathlib import Path

from pptx_to_docx_accessibility.paths import discover_pptx_files, plan_runs


def test_discover_pptx_files_skips_powerpoint_lock_files(tmp_path: Path) -> None:
    deck = tmp_path / "deck.pptx"
    lock_file = tmp_path / "~$deck.pptx"
    nested = tmp_path / "nested"
    nested.mkdir()
    nested_deck = nested / "other.pptx"
    deck.write_text("not a real pptx", encoding="utf-8")
    lock_file.write_text("lock", encoding="utf-8")
    nested_deck.write_text("not a real pptx", encoding="utf-8")

    assert discover_pptx_files(tmp_path, recursive=True) == [deck, nested_deck]
    assert discover_pptx_files(tmp_path, recursive=False) == [deck]


def test_plan_runs_uses_single_output_dir_for_file_input(tmp_path: Path) -> None:
    deck = tmp_path / "Deck Name.pptx"
    output_root = tmp_path / "out"
    deck.write_text("not a real pptx", encoding="utf-8")

    runs = plan_runs([deck], deck, output_root)

    assert len(runs) == 1
    assert runs[0].output_dir == output_root
