from __future__ import annotations

from typing import Any

from accessibility_by_manifest.inputs.pdf.extractors.common import safe_value
from accessibility_by_manifest.manifest.pdf_builder import ManifestBuilder, warning_entry


class PikepdfAdapter:
    """Enrich low-level PDF object, tag, structure, and content-stream evidence."""

    extractor_name = "pikepdf"

    def populate(self, builder: ManifestBuilder) -> None:
        try:
            import pikepdf
        except Exception as exc:
            builder.extractor_versions[self.extractor_name] = None
            builder.document_warning_entries.append(
                warning_entry("PIKEPDF_UNAVAILABLE", f"pikepdf could not be imported: {exc}", "document", severity="info", manual_review_required=False)
            )
            return

        builder.extractor_versions[self.extractor_name] = getattr(pikepdf, "__version__", None)
        try:
            with pikepdf.open(builder.input_path) as pdf:
                self._populate_from_pdf(builder, pdf)
        except Exception as exc:
            builder.document_warning_entries.append(warning_entry("PIKEPDF_OPEN_FAILED", f"pikepdf could not open the PDF: {exc}", "document"))

    def _populate_from_pdf(self, builder: ManifestBuilder, pdf: Any) -> None:
        root = pdf.Root
        raw_mark_info = root.get("/MarkInfo")
        mark_info = safe_value(raw_mark_info)
        struct_tree = root.get("/StructTreeRoot")
        names = root.get("/Names")
        acroform = root.get("/AcroForm")
        open_action = root.get("/OpenAction")
        document_language = safe_value(root.get("/Lang"))
        outlines = root.get("/Outlines")
        page_mode = root.get("/PageMode")
        page_layout = root.get("/PageLayout")
        viewer_preferences = root.get("/ViewerPreferences")

        if document_language:
            builder.metadata["language"] = document_language
        builder.document_accessibility.update(
            {
                "mark_info": mark_info,
                "tagged_pdf_detected": marked_pdf_detected(raw_mark_info, mark_info),
                "struct_tree_detected": struct_tree is not None,
            }
        )
        builder.document_navigation.update(
            {
                "viewer_preferences": safe_value(viewer_preferences),
                "page_layout": safe_value(page_layout),
                "page_mode": safe_value(page_mode),
            }
        )
        builder.document_interactivity.update(
            {
                "forms_present": bool(acroform) or builder.document_interactivity.get("forms_present"),
                "javascript_present": javascript_present(names, open_action),
                "javascript_actions": {
                    "names_javascript": safe_value(names.get("/JavaScript") if names else None),
                    "open_action": safe_value(open_action),
                },
                "xfa_present": bool(acroform and acroform.get("/XFA")),
            }
        )
        builder.extractor_evidence[self.extractor_name] = {
            "pdf_version": safe_value(getattr(pdf, "pdf_version", None)),
            "root_keys": safe_value(list(root.keys())),
            "trailer": safe_value(pdf.trailer),
            "acroform": safe_value(acroform),
            "names": safe_value(names),
            "struct_tree_root": safe_value(struct_tree),
            "document_language": document_language,
            "outlines": safe_value(outlines),
            "role_map": safe_value(struct_tree.get("/RoleMap") if struct_tree else None),
            "parent_tree": safe_value(struct_tree.get("/ParentTree") if struct_tree else None),
            "structure_children": safe_value(struct_tree.get("/K") if struct_tree else None),
        }

        for index, page in enumerate(pdf.pages, start=1):
            if index > len(builder.page_entries):
                break
            page_entry = builder.page_entries[index - 1]
            content_stream_evidence = content_stream_summary(page)
            page_entry["operator_evidence"] = content_stream_evidence
            page_entry["observed_source"]["operator_list_present"] = content_stream_evidence["content_stream_present"]
            page_entry["observed_source"]["struct_tree_present"] = struct_tree is not None
            page_entry["observed_source"]["xfa_present"] = bool(acroform and acroform.get("/XFA"))
            page_entry.setdefault("extractor_evidence", {})[self.extractor_name] = {
                "page_dict": safe_value(page.obj),
                "page_keys": safe_value(list(page.obj.keys())),
                "resources": safe_value(page.obj.get("/Resources")),
                "content_stream_evidence": content_stream_evidence,
                "struct_parents": safe_value(page.obj.get("/StructParents")),
            }


def javascript_present(names: Any, open_action: Any) -> bool:
    if names and names.get("/JavaScript"):
        return True
    return "/JavaScript" in str(open_action) or "/JS" in str(open_action)


def marked_pdf_detected(raw_mark_info: Any, mark_info: Any) -> bool:
    if hasattr(raw_mark_info, "get"):
        try:
            return bool(raw_mark_info.get("/Marked"))
        except Exception:
            pass
    if isinstance(mark_info, dict):
        return bool(mark_info.get("/Marked"))
    return False


def content_stream_summary(page: Any) -> dict[str, Any]:
    contents = page.obj.get("/Contents")
    streams = contents if isinstance(contents, list) else ([contents] if contents is not None else [])
    return {
        "content_stream_present": contents is not None,
        "stream_count": len(streams),
        "content_stream_refs": safe_value(streams),
    }
