from __future__ import annotations

from typing import Any

from accessibility_by_manifest.inputs.pdf.extractors.common import safe_value
from accessibility_by_manifest.manifest.pdf_builder import ManifestBuilder, warning_entry


class PypdfAdapter:
    """Enrich document-level metadata, navigation, security, and forms."""

    extractor_name = "pypdf"

    def populate(self, builder: ManifestBuilder) -> None:
        try:
            import pypdf
            from pypdf import PdfReader
        except Exception as exc:
            builder.extractor_versions[self.extractor_name] = None
            builder.document_warning_entries.append(
                warning_entry("PYPDF_UNAVAILABLE", f"pypdf could not be imported: {exc}", "document", severity="info", manual_review_required=False)
            )
            return

        builder.extractor_versions[self.extractor_name] = getattr(pypdf, "__version__", None)
        try:
            reader = PdfReader(str(builder.input_path))
        except Exception as exc:
            builder.document_warning_entries.append(warning_entry("PYPDF_OPEN_FAILED", f"pypdf could not open the PDF: {exc}", "document"))
            return

        metadata = safe_value(reader.metadata or {})
        normalized_metadata = normalize_metadata(metadata)
        builder.metadata.update({key: value for key, value in normalized_metadata.items() if value is not None})

        outline_entries = safe_outline(getattr(reader, "outline", None))
        page_labels = safe_value(getattr(reader, "page_labels", None))
        named_destinations = safe_value(getattr(reader, "named_destinations", None))
        builder.document_navigation.update(
            {
                "outline_present": bool(outline_entries),
                "outline_entries": outline_entries,
                "page_labels": page_labels,
                "named_destinations_present": bool(named_destinations),
                "named_destinations": named_destinations,
                "viewer_preferences": safe_value(getattr(reader, "viewer_preferences", None)),
                "page_layout": safe_value(getattr(reader, "page_layout", None)),
                "page_mode": safe_value(getattr(reader, "page_mode", None)),
            }
        )

        permissions = safe_value(getattr(reader, "user_access_permissions", None))
        builder.document_security.update({"permissions": permissions if permissions is None or isinstance(permissions, list) else [permissions]})

        fields = safe_value(reader.get_fields() if hasattr(reader, "get_fields") else None)
        builder.document_interactivity.update(
            {
                "forms_present": bool(fields),
                "form_fields": fields,
            }
        )
        if fields:
            builder.form_field_count = max(builder.form_field_count, len(fields))

        builder.extractor_evidence[self.extractor_name] = {
            "is_encrypted": bool(getattr(reader, "is_encrypted", False)),
            "metadata_raw": metadata,
            "trailer_keys": safe_value(list(getattr(reader, "trailer", {}).keys())),
            "page_count": len(reader.pages),
        }

        for page_number, page_entry in enumerate(builder.page_entries, start=1):
            if page_labels and page_number <= len(page_labels):
                page_entry["observed_source"]["page_label"] = page_labels[page_number - 1]
            page_entry.setdefault("extractor_evidence", {})[self.extractor_name] = {
                "page_object": safe_value(reader.pages[page_number - 1].indirect_reference if page_number - 1 < len(reader.pages) else None),
                "page_keys": safe_value(list(reader.pages[page_number - 1].keys()) if page_number - 1 < len(reader.pages) else []),
            }


def normalize_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
    return {
        "title": metadata.get("/Title") or metadata.get("Title"),
        "author": metadata.get("/Author") or metadata.get("Author"),
        "subject": metadata.get("/Subject") or metadata.get("Subject"),
        "keywords": metadata.get("/Keywords") or metadata.get("Keywords"),
        "creator": metadata.get("/Creator") or metadata.get("Creator"),
        "producer": metadata.get("/Producer") or metadata.get("Producer"),
        "creationDate": metadata.get("/CreationDate") or metadata.get("CreationDate"),
        "modDate": metadata.get("/ModDate") or metadata.get("ModDate"),
    }


def safe_outline(outline: Any) -> list[dict[str, Any]] | None:
    if not outline:
        return None

    def convert(items: Any) -> list[dict[str, Any]]:
        entries = []
        for item in items if isinstance(items, list) else [items]:
            if isinstance(item, list):
                entries.extend(convert(item))
                continue
            title = getattr(item, "title", None)
            if title is None and isinstance(item, dict):
                title = item.get("/Title") or item.get("title")
            entries.append(
                {
                    "title": str(title or ""),
                    "dest": safe_value(getattr(item, "page", None) or getattr(item, "destination", None)),
                    "url": safe_value(getattr(item, "uri", None)),
                    "items": [],
                }
            )
        return entries

    return convert(outline)
