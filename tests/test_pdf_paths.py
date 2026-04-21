from pathlib import Path

from accessibility_by_manifest.inputs.pdf.paths import discover_pdf_files, output_paths, plan_runs


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


def test_plan_runs_uses_manifest_output_suffix_for_pdf_folder_input(tmp_path: Path) -> None:
    pdf = tmp_path / "Document Name.pdf"
    pdf.write_text("not a real pdf", encoding="utf-8")

    runs = plan_runs([pdf], tmp_path, None)

    assert len(runs) == 1
    assert runs[0].output_dir == tmp_path / "Document Name_manifest_output"


def test_pdf_output_paths_include_extractor_manifest_names(tmp_path: Path) -> None:
    pdf = tmp_path / "Financial Report.pdf"
    pdf.write_text("not a real pdf", encoding="utf-8")
    run = plan_runs([pdf], pdf, tmp_path / "out")[0]

    paths = output_paths(run)

    assert paths.manifest_json == tmp_path / "out" / "Financial Report_manifest.json"
    assert paths.extractor_manifest_dir == tmp_path / "out" / "Financial Report_extractor_manifests"
    assert paths.normalized_manifest_json == tmp_path / "out" / "Financial Report_normalized_manifest.json"
    assert paths.review_queue_json == tmp_path / "out" / "Financial Report_review_queue.json"
    assert paths.extractor_manifest_json("pdfminer.six") == tmp_path / "out" / "Financial Report_extractor_manifests" / "Financial Report_pdfminer_six_manifest.json"
