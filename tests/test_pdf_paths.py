from pathlib import Path

from pdf_to_docx_accessibility.paths import discover_pdf_files, plan_runs


def test_discover_pdf_files_skips_non_pdf_and_lock_files(tmp_path: Path) -> None:
    pdf = tmp_path / "document.pdf"
    lock_pdf = tmp_path / "~$document.pdf"
    nested = tmp_path / "nested"
    nested.mkdir()
    nested_pdf = nested / "nested.pdf"
    text = tmp_path / "notes.txt"
    for path in (pdf, lock_pdf, nested_pdf, text):
        path.write_text("content", encoding="utf-8")

    assert discover_pdf_files(tmp_path, recursive=True) == [pdf, nested_pdf]
    assert discover_pdf_files(tmp_path, recursive=False) == [pdf]


def test_plan_runs_uses_single_output_dir_for_pdf_file_input(tmp_path: Path) -> None:
    pdf = tmp_path / "Document Name.pdf"
    output_root = tmp_path / "out"
    pdf.write_text("not a real pdf", encoding="utf-8")

    runs = plan_runs([pdf], pdf, output_root)

    assert len(runs) == 1
    assert runs[0].output_dir == output_root
