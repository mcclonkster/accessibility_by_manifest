## Human-readable field dictionary

**`pdf_accessibility_manifest` v0.1**

This dictionary describes the **intent** of each field in the draft schema. It keeps the same overall manifest spine as the uploaded PPTX manifests — source package, target package, run config, summary, warnings, per-unit entries, and projected output — but adapts it for **PDF evidence + accessibility-first normalization**.     

---

## 1. Top-level manifest fields

### `manifest_version`

Schema version for this manifest format.

### `manifest_kind`

Fixed identifier for the manifest type.
Expected value: `pdf_accessibility_manifest`

### `source_package`

Describes the input PDF file and basic identity facts.

### `target_package`

Describes the projected DOCX output.

### `run_config`

Records pipeline settings used for this run.

### `document_summary`

Stores top-level counts and totals for the extraction run.

### `document_metadata`

Stores PDF metadata and document-level descriptive information.

### `document_accessibility`

Stores document-level accessibility signals and risks.

### `document_navigation`

Stores navigation-related information such as outline, page labels, and destinations.

### `document_security`

Stores permissions and access restrictions declared in the PDF.

### `document_interactivity`

Stores forms, JavaScript, XFA, and other interactive behaviors.

### `document_warning_entries`

Document-level warnings that affect the whole file.

### `page_entries`

Per-page evidence records.

### `raw_block_entries`

Low-level extracted text/content blocks before normalization.

### `normalized_block_entries`

Higher-level content blocks after interpretation/normalization.

### `projected_target`

Top-level DOCX projection settings.

---

## 2. `source_package`

### `format_family`

High-level format family of the input.
Expected value: `PDF`

### `input_file_name`

Original source PDF filename.

### `input_file_path`

Path or locator for the input PDF.

### `page_count`

Total number of pages in the source PDF.

### `document_fingerprints`

Stable identity tokens from the PDF engine, used for provenance and deduplication.

### `byte_length`

File size in bytes, when available.

---

## 3. `target_package`

### `format_family`

High-level format family of the output.
Expected value: `OOXML`

### `package_model`

Package model for the target file.
Expected value: `OPC`

### `document_vocabulary`

OOXML document vocabulary for the target.
Expected value: `WordprocessingML`

### `draft_output_file_name`

Projected DOCX filename.

### `draft_output_file_path`

Projected DOCX path or locator.

---

## 4. `run_config`

### `include_preview_images`

Whether preview page images were generated for review.

### `preview_image_dir`

Directory containing preview images, if generated.

### `page_separator_mode`

How page boundaries should be represented in DOCX.
Allowed values:

* `PAGE_BREAK`
* `SECTION_BREAK`
* `NONE`

### `include_warning_appendix`

Whether unresolved warnings should be included in the DOCX output.

### `include_page_traceback`

Whether DOCX output should preserve page traceability back to the source PDF.

### `prefer_outline_for_headings`

Whether outline/bookmark structure should be preferred when inferring headings.

---

## 5. `document_summary`

### `total_pages`

Total pages in the source PDF.

### `pages_with_warnings`

How many pages have one or more warnings.

### `raw_block_count`

Count of low-level extracted blocks.

### `normalized_block_count`

Count of normalized/interpreted blocks.

### `annotation_count`

Total annotations detected across the document.

### `form_field_count`

Total form fields detected across the document.

### `figure_candidate_count`

Total candidate figures/non-text objects flagged for review or processing.

---

## 6. `document_metadata`

### `info`

The PDF Info dictionary, preserved as extracted.

### `xmp_present`

Whether XMP metadata appears to be present.

### `title`

Document title, if available.

### `author`

Document author, if available.

### `subject`

Document subject, if available.

### `keywords`

Document keywords, if available.

### `language`

Document language, if available.

---

## 7. `document_accessibility`

### `mark_info`

The PDF MarkInfo object or extracted equivalent.

### `tagged_pdf_detected`

Whether the PDF appears to be tagged.

### `struct_tree_detected`

Whether a structure tree appears to exist at all.

### `image_only_pages_present`

Whether one or more pages appear to be image-only.

### `ocr_required`

Whether OCR is likely required for full text recovery.

### `ocr_detected`

Whether OCR-derived text appears to be present.

### `reading_order_source`

What primary source is being used for reading order.
Allowed values:

* `tag_tree`
* `layout_inference`
* `mixed`
* `unknown`

---

## 8. `document_navigation`

### `outline_present`

Whether a bookmark/outline tree is present.

### `outline_entries`

The extracted outline/bookmark tree.

### `page_labels`

Logical page labels, if present.

### `named_destinations_present`

Whether named destinations are present.

### `named_destinations`

Named destinations map, if extracted.

### `viewer_preferences`

Viewer preference settings declared in the PDF.

### `page_layout`

Requested page layout mode.

### `page_mode`

Requested page mode.

---

## 9. `document_security`

### `permissions`

Permission flags declared in the document.

---

## 10. `document_interactivity`

### `javascript_present`

Whether JavaScript actions appear to exist.

### `javascript_actions`

Extracted document-level JavaScript actions.

### `forms_present`

Whether forms appear to exist.

### `form_fields`

Extracted form field objects or equivalent field map.

### `calculation_order_ids`

IDs used in form calculation order, if present.

### `xfa_present`

Whether XFA is present at the document level.

### `is_pure_xfa`

Whether the PDF is effectively XFA-only.

### `all_xfa_html`

Full extracted XFA HTML-like object, if available.

---

## 11. `document_warning_entries`

This is a list of warning objects.

### `warning_code`

Short machine-readable identifier.

### `warning_message`

Human-readable explanation of the warning.

### `warning_scope`

What level the warning applies to.
Allowed values:

* `document`
* `page`
* `block`
* `annotation`
* `figure`
* `form`
* `navigation`
* `security`
* `metadata`
* `ocr`
* `reading_order`

### `warning_severity`

Severity label.
Allowed values:

* `info`
* `warning`
* `error`

### `manual_review_required`

Whether a human should review this issue.

---

## 12. `page_entries`

Each entry represents one source PDF page.

### `page_number`

1-based page number.

### `observed_source`

Low-level source evidence about the page.

### `struct_tree`

Extracted page-level structure tree, if any.

### `annotation_entries`

Annotations found on the page.

### `xfa_entries`

XFA content found on the page, if any.

### `operator_evidence`

Operator-list evidence for the page.

### `warning_entries`

Warnings specific to this page.

---

## 13. `page_entries[].observed_source`

### `page_ref`

Internal PDF reference for the page.

### `page_rotation`

Declared page rotation.

### `user_unit`

Scale factor for page units.

### `page_bbox`

Page bounding box.

### `viewport`

Viewport geometry/transforms used for layout interpretation.

### `struct_tree_present`

Whether page-level structure data exists.

### `text_layer_detected`

Whether extractable text seems present on the page.

### `image_only_page_suspected`

Whether the page appears to be mostly or entirely image-only.

### `ocr_text_detected`

Whether OCR text appears to be present.

### `annotation_count`

Count of annotations on the page.

### `form_field_count`

Count of form fields/widgets on the page.

### `xfa_present`

Whether page-level XFA content exists.

### `operator_list_present`

Whether page operator evidence was successfully extracted.

### `page_label`

Logical page label corresponding to this page, if any.

---

## 14. `annotation_entries`

Each entry represents one annotation or widget-like item found on a page.

### `annotation_subtype`

Subtype of the annotation, if known.

### `contents`

Annotation contents text, if present.

### `alt_text`

Alternative text or equivalent descriptive text, if present.

### `url`

External URL destination, if present.

### `dest`

Internal destination, if present.

### `manual_review_required`

Whether the annotation should be reviewed manually.

---

## 15. `raw_block_entries`

These are **low-level extracted blocks** before semantic normalization.

### `block_id`

Unique identifier for the raw block.

### `page_number`

Page on which the block was observed.

### `source_evidence_type`

What kind of source evidence produced the block.
Allowed values:

* `tagged_text`
* `untagged_text`
* `ocr_text`
* `annotation_text`
* `form_field_text`
* `xfa_text`
* `outline_text`
* `artifact_text`
* `unknown`

### `source_ref`

Source-specific reference string for provenance.

### `bbox`

Bounding box for the block, if known.

### `text`

Block text after extraction.

### `text_items`

Underlying extracted text items.

### `style_hints`

Observed style clues such as font and size.

### `structure_hints`

Observed structural clues such as tag name or MCID.

### `role_basis`

Reasons or evidence used later for interpretation.

### `manual_review_required`

Whether the raw block already looks uncertain.

### `warning_entries`

Warnings specific to the raw block.

---

## 16. `text_items`

Represents individual extracted text pieces from PDF.js.

### `str`

Extracted string.

### `dir`

Text direction, if available.

### `width`

Rendered width estimate.

### `height`

Rendered height estimate.

### `fontName`

Font name as reported by the extractor.

### `transform`

Transformation matrix.

---

## 17. `style_hints`

### `font_name`

Observed font name.

### `font_size`

Observed font size.

### `font_weight`

Observed or inferred font weight.

### `font_style`

Observed or inferred style such as italic.

---

## 18. `structure_hints`

### `tag_name`

Observed structure tag, if any.

### `parent_tag_name`

Observed parent structure tag, if any.

### `mcid`

Marked-content ID, if available.

### `language`

Language override associated with this block, if available.

---

## 19. `normalized_block_entries`

These are **interpreted content blocks** built from one or more raw blocks.

### `block_id`

Identifier for the normalized block.

### `page_span`

Start and end page covered by the normalized block.

### `observed_source_refs`

References to the raw source blocks used to build this block.

### `normalized_workflow`

The interpreted semantic view of the block.

### `warning_entries`

Warnings specific to the normalized block.

### `projected_target`

How this normalized block should appear in the DOCX.

---

## 20. `normalized_workflow`

### `interpreted_role`

Semantic role assigned to the block.
Allowed values:

* `heading`
* `paragraph`
* `list`
* `list_item`
* `table`
* `table_row`
* `table_cell`
* `figure`
* `caption`
* `link`
* `form_field`
* `note`
* `artifact`
* `unknown`

### `heading_level`

Heading level if the role is a heading.

### `list_kind`

List style if the role is list-related.
Allowed values:

* `plain`
* `bullet`
* `number`
* `unknown`

### `role_confidence`

Confidence in the assigned role.
Allowed values:

* `high`
* `medium`
* `low`
* `unknown`

### `semantic_source_quality`

How trustworthy the semantic evidence is.
Allowed values:

* `high`
* `medium`
* `low`
* `unknown`

### `role_basis`

Evidence used to assign the role.

### `reading_order_index`

Position in normalized reading order.

### `reading_order_basis`

Evidence used to place the block in reading order.

### `manual_review_required`

Whether the interpreted block still needs human review.

---

## 21. `block_projected_target`

### `target_package_part`

Target DOCX package part, typically `word/document.xml`.

### `target_style`

Projected Word style, if any.

### `target_heading_text`

Heading text to use in the DOCX, if applicable.

### `target_list_kind`

Projected list type, if applicable.

### `target_table_id`

Target table grouping identifier, if applicable.

### `projection_status`

Status of this block’s DOCX mapping.
Allowed values:

* `planned`
* `appendix_only`
* `omitted`
* `unknown`

---

## 22. `projected_target` (top-level)

### `target_package_part`

Primary output package part.

### `document_title_strategy`

How the DOCX title should be chosen.
Allowed values:

* `metadata_title`
* `outline_title`
* `first_heading`
* `manual_review`

### `page_separator_mode`

How source page boundaries should be represented in DOCX.
Allowed values:

* `PAGE_BREAK`
* `SECTION_BREAK`
* `NONE`

### `include_warning_appendix`

Whether unresolved issues should be appended to the DOCX.

### `projection_status`

Overall projection state.
Allowed values:

* `planned`
* `drafted`
* `manual_review_required`

---

## Design logic in one line

This schema separates:

* **what the PDF literally gave us**
* **what we think it means**
* **how confident we are**
* **what Word output we plan to create**

That is the same general manifest logic already visible in the uploaded PPTX manifests — observed source, normalized workflow, warnings, projected target — just made stricter for PDF and accessibility.  

The next best step is the **sample manifest instance that validates against the draft schema**.

---

EXAMPLE

{
  "manifest_version": "0.1",
  "manifest_kind": "pdf_accessibility_manifest",
  "source_package": {
    "format_family": "PDF",
    "input_file_name": "sample_accessible_article.pdf",
    "input_file_path": "/example/input/sample_accessible_article.pdf",
    "page_count": 1,
    "document_fingerprints": [
      "abc123def4567890"
    ],
    "byte_length": 245812
  },
  "target_package": {
    "format_family": "OOXML",
    "package_model": "OPC",
    "document_vocabulary": "WordprocessingML",
    "draft_output_file_name": "sample_accessible_article_companion.docx",
    "draft_output_file_path": "/example/output/sample_accessible_article_companion.docx"
  },
  "run_config": {
    "include_preview_images": true,
    "preview_image_dir": "/example/output/sample_accessible_article_page_images",
    "page_separator_mode": "PAGE_BREAK",
    "include_warning_appendix": true,
    "include_page_traceback": true,
    "prefer_outline_for_headings": true
  },
  "document_summary": {
    "total_pages": 1,
    "pages_with_warnings": 1,
    "raw_block_count": 3,
    "normalized_block_count": 3,
    "annotation_count": 1,
    "form_field_count": 0,
    "figure_candidate_count": 1
  },
  "document_metadata": {
    "info": {
      "Title": "Sample Accessible Article",
      "Author": "Example Author",
      "Subject": "Demonstration PDF",
      "Keywords": "accessibility, pdf, sample"
    },
    "xmp_present": true,
    "title": "Sample Accessible Article",
    "author": "Example Author",
    "subject": "Demonstration PDF",
    "keywords": [
      "accessibility",
      "pdf",
      "sample"
    ],
    "language": "en-US"
  },
  "document_accessibility": {
    "mark_info": {
      "Marked": true,
      "UserProperties": false,
      "Suspects": false
    },
    "tagged_pdf_detected": true,
    "struct_tree_detected": true,
    "image_only_pages_present": false,
    "ocr_required": false,
    "ocr_detected": false,
    "reading_order_source": "tag_tree"
  },
  "document_navigation": {
    "outline_present": true,
    "outline_entries": [
      {
        "title": "Introduction",
        "dest": [
          {
            "num": 5,
            "gen": 0
          },
          {
            "name": "XYZ"
          },
          72,
          720,
          null
        ],
        "url": null,
        "items": []
      }
    ],
    "page_labels": [
      "1"
    ],
    "named_destinations_present": true,
    "named_destinations": {
      "intro": [
        {
          "num": 5,
          "gen": 0
        },
        {
          "name": "XYZ"
        },
        72,
        720,
        null
      ]
    },
    "viewer_preferences": {
      "DisplayDocTitle": true
    },
    "page_layout": "SinglePage",
    "page_mode": "UseOutlines"
  },
  "document_security": {
    "permissions": [
      "PRINT",
      "COPY",
      "MODIFY_CONTENTS"
    ]
  },
  "document_interactivity": {
    "javascript_present": false,
    "javascript_actions": null,
    "forms_present": false,
    "form_fields": null,
    "calculation_order_ids": null,
    "xfa_present": false,
    "is_pure_xfa": false,
    "all_xfa_html": null
  },
  "document_warning_entries": [
    {
      "warning_code": "FIGURE_DESCRIPTION_REVIEW",
      "warning_message": "Figure candidate detected on page 1. Verify that descriptive text is sufficient for the DOCX companion.",
      "warning_scope": "figure",
      "warning_severity": "warning",
      "manual_review_required": true
    }
  ],
  "page_entries": [
    {
      "page_number": 1,
      "observed_source": {
        "page_ref": "5R",
        "page_rotation": 0,
        "user_unit": 1,
        "page_bbox": [
          0,
          0,
          612,
          792
        ],
        "viewport": {
          "width": 612,
          "height": 792,
          "rotation": 0,
          "scale": 1
        },
        "struct_tree_present": true,
        "text_layer_detected": true,
        "image_only_page_suspected": false,
        "ocr_text_detected": false,
        "annotation_count": 1,
        "form_field_count": 0,
        "xfa_present": false,
        "operator_list_present": true,
        "page_label": "1"
      },
      "struct_tree": {
        "role": "Document",
        "children": [
          {
            "role": "H1",
            "children": [
              {
                "type": "content",
                "id": "p1_mcid_0"
              }
            ]
          },
          {
            "role": "P",
            "children": [
              {
                "type": "content",
                "id": "p1_mcid_1"
              }
            ]
          },
          {
            "role": "Figure",
            "children": [
              {
                "type": "content",
                "id": "p1_mcid_2"
              }
            ]
          }
        ]
      },
      "annotation_entries": [
        {
          "annotation_subtype": "Link",
          "contents": "Open example website",
          "alt_text": "Example website link",
          "url": "https://example.org",
          "dest": null,
          "manual_review_required": false
        }
      ],
      "xfa_entries": null,
      "operator_evidence": {
        "fnArray_length": 128,
        "argsArray_length": 128
      },
      "warning_entries": [
        {
          "warning_code": "CAPTION_FIGURE_ASSOCIATION_UNCERTAIN",
          "warning_message": "Figure-like content appears on page 1, but caption association should be reviewed before DOCX export.",
          "warning_scope": "page",
          "warning_severity": "warning",
          "manual_review_required": true
        }
      ]
    }
  ],
  "raw_block_entries": [
    {
      "block_id": "p1_b1",
      "page_number": 1,
      "source_evidence_type": "tagged_text",
      "source_ref": "page=1;mcid=0",
      "bbox": [
        72,
        700,
        320,
        728
      ],
      "text": "Introduction",
      "text_items": [
        {
          "str": "Introduction",
          "dir": "ltr",
          "width": 112.4,
          "height": 24,
          "fontName": "F1",
          "transform": [
            24,
            0,
            0,
            24,
            72,
            700
          ]
        }
      ],
      "style_hints": {
        "font_name": "ABCDEE+Helvetica-Bold",
        "font_size": 24,
        "font_weight": "bold",
        "font_style": "normal"
      },
      "structure_hints": {
        "tag_name": "H1",
        "parent_tag_name": "Document",
        "mcid": 0,
        "language": "en-US"
      },
      "role_basis": [
        "tag_tree:H1",
        "font_size_outlier",
        "top_of_page_position"
      ],
      "manual_review_required": false,
      "warning_entries": []
    },
    {
      "block_id": "p1_b2",
      "page_number": 1,
      "source_evidence_type": "tagged_text",
      "source_ref": "page=1;mcid=1",
      "bbox": [
        72,
        650,
        520,
        682
      ],
      "text": "This sample PDF demonstrates how extracted source evidence can be normalized into a reviewable DOCX companion.",
      "text_items": [
        {
          "str": "This sample PDF demonstrates how extracted source evidence can be normalized into a reviewable DOCX companion.",
          "dir": "ltr",
          "width": 430.2,
          "height": 12,
          "fontName": "F2",
          "transform": [
            12,
            0,
            0,
            12,
            72,
            650
          ]
        }
      ],
      "style_hints": {
        "font_name": "ABCDEE+Helvetica",
        "font_size": 12,
        "font_weight": "normal",
        "font_style": "normal"
      },
      "structure_hints": {
        "tag_name": "P",
        "parent_tag_name": "Document",
        "mcid": 1,
        "language": "en-US"
      },
      "role_basis": [
        "tag_tree:P"
      ],
      "manual_review_required": false,
      "warning_entries": []
    },
    {
      "block_id": "p1_b3",
      "page_number": 1,
      "source_evidence_type": "tagged_text",
      "source_ref": "page=1;mcid=2",
      "bbox": [
        72,
        450,
        300,
        610
      ],
      "text": "[Figure content detected]",
      "text_items": [
        {
          "str": "[Figure content detected]",
          "dir": "ltr",
          "width": 160,
          "height": 12,
          "fontName": "F2",
          "transform": [
            12,
            0,
            0,
            12,
            72,
            450
          ]
        }
      ],
      "style_hints": {
        "font_name": "ABCDEE+Helvetica",
        "font_size": 12,
        "font_weight": "normal",
        "font_style": "normal"
      },
      "structure_hints": {
        "tag_name": "Figure",
        "parent_tag_name": "Document",
        "mcid": 2,
        "language": "en-US"
      },
      "role_basis": [
        "tag_tree:Figure"
      ],
      "manual_review_required": true,
      "warning_entries": [
        {
          "warning_code": "FIGURE_ALT_TEXT_NOT_VERIFIED",
          "warning_message": "Figure structure was detected, but useful equivalent description has not yet been verified.",
          "warning_scope": "figure",
          "warning_severity": "warning",
          "manual_review_required": true
        }
      ]
    }
  ],
  "normalized_block_entries": [
    {
      "block_id": "n1",
      "page_span": [
        1,
        1
      ],
      "observed_source_refs": [
        "p1_b1"
      ],
      "normalized_workflow": {
        "interpreted_role": "heading",
        "heading_level": 1,
        "list_kind": null,
        "role_confidence": "high",
        "semantic_source_quality": "high",
        "role_basis": [
          "tag_tree:H1",
          "font_size_outlier",
          "top_of_page_position"
        ],
        "reading_order_index": 1,
        "reading_order_basis": [
          "tag_tree_order"
        ],
        "manual_review_required": false
      },
      "warning_entries": [],
      "projected_target": {
        "target_package_part": "word/document.xml",
        "target_style": "Heading1",
        "target_heading_text": "Introduction",
        "target_list_kind": null,
        "target_table_id": null,
        "projection_status": "planned"
      }
    },
    {
      "block_id": "n2",
      "page_span": [
        1,
        1
      ],
      "observed_source_refs": [
        "p1_b2"
      ],
      "normalized_workflow": {
        "interpreted_role": "paragraph",
        "heading_level": null,
        "list_kind": "plain",
        "role_confidence": "high",
        "semantic_source_quality": "high",
        "role_basis": [
          "tag_tree:P"
        ],
        "reading_order_index": 2,
        "reading_order_basis": [
          "tag_tree_order"
        ],
        "manual_review_required": false
      },
      "warning_entries": [],
      "projected_target": {
        "target_package_part": "word/document.xml",
        "target_style": "BodyText",
        "target_heading_text": null,
        "target_list_kind": "plain",
        "target_table_id": null,
        "projection_status": "planned"
      }
    },
    {
      "block_id": "n3",
      "page_span": [
        1,
        1
      ],
      "observed_source_refs": [
        "p1_b3"
      ],
      "normalized_workflow": {
        "interpreted_role": "figure",
        "heading_level": null,
        "list_kind": null,
        "role_confidence": "medium",
        "semantic_source_quality": "medium",
        "role_basis": [
          "tag_tree:Figure"
        ],
        "reading_order_index": 3,
        "reading_order_basis": [
          "tag_tree_order",
          "layout_position"
        ],
        "manual_review_required": true
      },
      "warning_entries": [
        {
          "warning_code": "FIGURE_DESCRIPTION_REVIEW",
          "warning_message": "Projected DOCX should include figure placeholder and reviewer-facing note for description verification.",
          "warning_scope": "figure",
          "warning_severity": "warning",
          "manual_review_required": true
        }
      ],
      "projected_target": {
        "target_package_part": "word/document.xml",
        "target_style": "Figure",
        "target_heading_text": null,
        "target_list_kind": null,
        "target_table_id": null,
        "projection_status": "appendix_only"
      }
    }
  ],
  "projected_target": {
    "target_package_part": "word/document.xml",
    "document_title_strategy": "metadata_title",
    "page_separator_mode": "PAGE_BREAK",
    "include_warning_appendix": true,
    "projection_status": "planned"
  }
}