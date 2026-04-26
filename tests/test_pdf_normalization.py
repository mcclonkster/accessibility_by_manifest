from accessibility_by_manifest.normalize.pdf import normalize_pdf_manifest
from accessibility_by_manifest.normalize.pdf_accessibility_model import normalize_pdf_manifest_to_accessibility_model
from accessibility_by_manifest.review.pdf import review_pdf_manifest


def test_pdf_normalization_identifies_repeated_artifacts_and_table_cells() -> None:
    manifest = {
        "document_accessibility": {"struct_tree_detected": False},
        "document_metadata": {"title": "Report", "language": "en"},
        "document_summary": {"pages_with_warnings": 0, "figure_candidate_count": 0},
        "document_warning_entries": [],
        "review_entries": [],
        "projected_target": {"projection_status": "planned"},
        "page_entries": [
            page_entry(1),
            page_entry(2),
            page_entry(3),
        ],
        "raw_block_entries": [
            raw_block("p0001_b0001", 1, "RUNNING HEADER", [20, 20, 180, 35]),
            raw_block("p0002_b0001", 2, "RUNNING HEADER", [20, 20, 180, 35]),
            raw_block("p0002_b0002", 2, "Category Amount", [72, 180, 210, 195]),
            raw_block("p0002_b0003", 2, "Assets $1,000", [72, 200, 210, 215]),
            raw_block("p0002_b0004", 2, "Liabilities $500", [72, 220, 225, 235]),
            raw_block("p0002_b0005", 2, "Total $500", [72, 240, 190, 255]),
            raw_block("p0002_b0006", 2, "Enrollment 1,200", [72, 500, 210, 515]),
            raw_block("p0003_b0001", 3, "RUNNING HEADER", [20, 20, 180, 35]),
        ],
    }

    manifest = review_pdf_manifest(normalize_pdf_manifest(manifest))

    roles_by_id = {
        block["block_id"]: block["normalized_workflow"]["interpreted_role"]
        for block in manifest["normalized_block_entries"]
    }
    assert roles_by_id["n_p0001_b0001"] == "artifact"
    assert roles_by_id["n_p0002_b0002"] == "table_cell"
    table_ids_by_id = {
        block["block_id"]: block["projected_target"]["target_table_id"]
        for block in manifest["normalized_block_entries"]
    }
    assert table_ids_by_id["n_p0002_b0002"] == table_ids_by_id["n_p0002_b0005"]
    assert table_ids_by_id["n_p0002_b0006"] != table_ids_by_id["n_p0002_b0002"]
    assert manifest["normalized_table_entries"]
    first_table = manifest["normalized_table_entries"][0]
    assert first_table["row_entries"]
    assert first_table["header_candidate_row_indexes"] == [1]
    assert first_table["row_entries"][0]["header_candidate"] is True
    assert any(entry["issue_code"] == "TABLE_HEADERS_UNCERTAIN" for entry in manifest["review_entries"])
    assert any(warning["warning_code"] == "TABLE_STRUCTURE_REVIEW" for warning in manifest["document_warning_entries"])
    assert any(warning["warning_code"] == "TABLE_HEADERS_UNCERTAIN" for warning in manifest["document_warning_entries"])


def test_pdf_normalization_can_emit_shared_accessibility_model() -> None:
    manifest = {
        "manifest_kind": "pdf_accessibility_manifest",
        "manifest_version": "0.1",
        "source_package": {
            "input_file_name": "report.pdf",
            "input_file_path": "/tmp/report.pdf",
            "sha256": "abc123",
            "format_family": "PDF",
        },
        "document_accessibility": {"struct_tree_detected": False},
        "document_metadata": {"title": "Report", "language": "en"},
        "document_summary": {"pages_with_warnings": 0, "figure_candidate_count": 0, "total_pages": 3},
        "document_warning_entries": [],
        "review_entries": [],
        "projected_target": {"projection_status": "planned"},
        "page_entries": [
            page_entry(1),
            page_entry(2),
            page_entry(3),
        ],
        "raw_block_entries": [
            raw_block("p0001_b0001", 1, "RUNNING HEADER", [20, 20, 180, 35]),
            raw_block("p0002_b0001", 2, "RUNNING HEADER", [20, 20, 180, 35]),
            raw_block("p0002_b0002", 2, "Category Amount", [72, 180, 210, 195]),
            raw_block("p0002_b0003", 2, "Assets $1,000", [72, 200, 210, 215]),
            raw_block("p0002_b0004", 2, "Liabilities $500", [72, 220, 225, 235]),
            raw_block("p0002_b0005", 2, "Total $500", [72, 240, 190, 255]),
            raw_block("p0002_b0006", 2, "Enrollment 1,200", [72, 500, 210, 515]),
            raw_block("p0003_b0001", 3, "RUNNING HEADER", [20, 20, 180, 35]),
        ],
    }

    manifest = review_pdf_manifest(normalize_pdf_manifest(manifest))
    document = normalize_pdf_manifest_to_accessibility_model(manifest)

    assert document.view_kind == "normalized_accessibility_model"
    assert document.source_format == "PDF"
    assert document.source_manifest_kind == "pdf_accessibility_manifest"
    assert document.document.document_id == "sha256:abc123"
    assert document.summary.unit_count == len(document.unit_entries)
    assert any(unit.unit_type == "artifact" for unit in document.unit_entries)
    assert any(unit.unit_type == "table_cell" for unit in document.unit_entries)
    assert document.table_entries
    assert document.table_entries[0].header_candidate_row_indexes == [1]
    assert any(entry.issue_code == "TABLE_HEADERS_UNCERTAIN" for entry in document.review_entries)
    assert document.unit_entries[0].provenance.source_refs
    assert document.unit_entries[0].projection_hints.preferred_output_roles


def page_entry(page_number: int) -> dict:
    return {
        "page_number": page_number,
        "observed_source": {"image_only_page_suspected": False},
        "warning_entries": [],
    }


def raw_block(block_id: str, page_number: int, text: str, bbox: list[float]) -> dict:
    return {
        "block_id": block_id,
        "page_number": page_number,
        "source_ref": f"page:{page_number}/block:{block_id}",
        "bbox": bbox,
        "text": text,
        "style_hints": {"font_size": 11.0, "font_weight": None},
        "structure_hints": {"tag_name": None, "mcid": None},
        "extractor_evidence": {"pymupdf": {}},
    }
