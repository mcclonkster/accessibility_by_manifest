# PPTX to DOCX Remediation Manifest — Field Dictionary

## Top level

### manifest_version
- Type: string
- Required: yes
- Meaning: schema version of the manifest
- Allowed value: `1.0`
- Does not mean: script version or source-file version

### manifest_kind
- Type: string
- Required: yes
- Meaning: fixed label identifying this manifest type
- Allowed value: `pptx_to_docx_remediation_manifest`

### generated_at_utc
- Type: string
- Required: yes
- Meaning: UTC timestamp for manifest generation
- Format: `date-time`

### generator
- Type: object
- Required: yes
- Meaning: identifies the script that produced the manifest

#### generator.script_name
- Type: string
- Required: yes
- Meaning: generator script name

#### generator.script_version
- Type: string
- Required: yes
- Meaning: generator script version

---

## source_package

### source_package
- Type: object
- Required: yes
- Meaning: technical identity of the source package

#### source_package.format_family
- Type: string
- Required: yes
- Allowed value: `OOXML`

#### source_package.package_model
- Type: string
- Required: yes
- Allowed value: `OPC`

#### source_package.document_vocabulary
- Type: string
- Required: yes
- Allowed value: `PresentationML`

#### source_package.input_file_name
- Type: string
- Required: yes
- Meaning: source PPTX file name

#### source_package.input_file_path
- Type: string
- Required: yes
- Meaning: source PPTX path used by the run

---

## target_package

### target_package
- Type: object
- Required: yes
- Meaning: technical identity of the draft DOCX target

#### target_package.format_family
- Type: string
- Required: yes
- Allowed value: `OOXML`

#### target_package.package_model
- Type: string
- Required: yes
- Allowed value: `OPC`

#### target_package.document_vocabulary
- Type: string
- Required: yes
- Allowed value: `WordprocessingML`

#### target_package.draft_output_file_name
- Type: string
- Required: yes
- Meaning: output DOCX file name

#### target_package.draft_output_file_path
- Type: string
- Required: yes
- Meaning: output DOCX path

---

## run_config

### run_config
- Type: object
- Required: yes
- Meaning: extraction/projection settings that materially affect output meaning

#### run_config.include_preview_images
- Type: boolean
- Required: yes
- Meaning: whether preview images were enabled during extraction

#### run_config.preview_image_dir
- Type: string or null
- Required: yes
- Meaning: preview image folder path, if used

#### run_config.title_fallback_mode
- Type: string
- Required: yes
- Allowed values:
  - `FIRST_TEXT_LINE`
  - `UNTITLED_ONLY`

#### run_config.text_order_mode
- Type: string
- Required: yes
- Allowed value:
  - `TOP_LEFT`

#### run_config.slide_separator_mode
- Type: string
- Required: yes
- Allowed values:
  - `PAGE_BREAK`
  - `BLANK_LINE`

---

## manifest_summary

### manifest_summary
- Type: object
- Required: yes
- Meaning: high-level counts for the run

#### manifest_summary.total_slides
- Type: integer
- Required: yes
- Meaning: number of slides processed

#### manifest_summary.slides_with_warnings
- Type: integer
- Required: yes
- Meaning: count of slides with one or more warnings

#### manifest_summary.detected_visual_entries
- Type: integer
- Required: yes
- Meaning: count of visual entries created

#### manifest_summary.detected_visual_entries_missing_descriptions
- Type: integer
- Required: yes
- Meaning: count of visual entries whose description is missing

---

## manifest_warning_entries

### manifest_warning_entries
- Type: array of warning_entry
- Required: yes
- Meaning: manifest-level warnings not tied to just one slide

---

## slide_entries

### slide_entries
- Type: array
- Required: yes
- Meaning: one entry per slide in deck order

---

# Slide entry

## slide_number
- Type: integer
- Required: yes
- Meaning: 1-based slide index in deck order
- Minimum: 1

## observed_source
- Type: object
- Required: yes
- Meaning: source-side technical provenance for the slide

### observed_source.package_part
- Type: string
- Required: yes
- Meaning: slide XML part path, such as `ppt/slides/slide7.xml`

### observed_source.relationships_part
- Type: string or null
- Required: yes
- Meaning: relationships part path for the slide

### observed_source.presentationml_root
- Type: string
- Required: yes
- Allowed value: `p:sld`

### observed_source.common_slide_path
- Type: string or null
- Required: no
- Meaning: path hint for the common slide model

### observed_source.shape_tree_path
- Type: string or null
- Required: no
- Meaning: path hint for the slide shape tree

### observed_source.notes_part_present
- Type: boolean
- Required: no
- Meaning: whether a notes part was present

### observed_source.preview_image_candidates
- Type: array of strings
- Required: no
- Meaning: preview image candidates seen for this slide

## normalized_workflow
- Type: object
- Required: yes
- Meaning: workflow-level interpretation of the slide

### normalized_workflow.chosen_title
- Type: string
- Required: yes
- Meaning: final title used for the slide

### normalized_workflow.title_source
- Type: string
- Required: yes
- Allowed values:
  - `TITLE_PLACEHOLDER`
  - `FIRST_TEXT_LINE`
  - `UNTITLED_FALLBACK`

### normalized_workflow.grouped_content_detected
- Type: boolean
- Required: yes
- Meaning: grouped shapes were detected on the slide

### normalized_workflow.reading_order_low_confidence
- Type: boolean
- Required: yes
- Meaning: reading order may be weak or unstable

### normalized_workflow.skipped_shape_content_detected
- Type: boolean
- Required: yes
- Meaning: some shape content may not be represented by the extractor

### normalized_workflow.preview_match_ambiguous
- Type: boolean
- Required: yes
- Meaning: multiple preview candidates matched

### normalized_workflow.connector_relationship_warning
- Type: boolean
- Required: yes
- Meaning: relationship meaning may depend on connectors or shape arrangement

### normalized_workflow.manual_review_required
- Type: boolean
- Required: yes
- Meaning: human review is still required for this slide

## projected_target
- Type: object
- Required: yes
- Meaning: intended Word-side representation for the slide

### projected_target.target_package_part
- Type: string
- Required: yes
- Allowed value: `word/document.xml`

### projected_target.projected_slide_heading_text
- Type: string
- Required: yes
- Meaning: heading text intended for the DOCX

### projected_target.projected_slide_heading_style
- Type: string
- Required: yes
- Meaning: Word paragraph style name for the slide heading

### projected_target.projected_slide_separator_mode
- Type: string
- Required: yes
- Allowed values:
  - `PAGE_BREAK`
  - `BLANK_LINE`

### projected_target.projection_status
- Type: string
- Required: yes
- Allowed values:
  - `planned`
  - `written`
  - `omitted`
  - `manual_only`

## warning_entries
- Type: array of warning_entry
- Required: yes
- Meaning: slide-level warnings

## text_block_entries
- Type: array
- Required: yes
- Meaning: extracted text blocks for the slide

## visual_entries
- Type: array
- Required: yes
- Meaning: detected visual entries for the slide

---

# Text block entry

## observed_source
- Type: object
- Required: yes
- Meaning: source-side provenance for one extracted text block

### observed_source.package_part
- Type: string
- Required: yes
- Meaning: source slide part path

### observed_source.shape_tree_path
- Type: string
- Required: yes
- Meaning: source shape-tree path for the block

### observed_source.shape_kind
- Type: string
- Required: yes
- Meaning: source shape kind, such as `p:sp`

### observed_source.shape_id
- Type: integer or null
- Required: no
- Meaning: shape identifier if available

### observed_source.shape_name
- Type: string
- Required: yes
- Meaning: source shape name

### observed_source.placeholder_type
- Type: string or null
- Required: no
- Meaning: placeholder role if available

### observed_source.geometry
- Type: object
- Required: yes
- Meaning: source coordinates and size

#### observed_source.geometry.x
- Type: integer
- Required: yes

#### observed_source.geometry.y
- Type: integer
- Required: yes

#### observed_source.geometry.cx
- Type: integer
- Required: yes

#### observed_source.geometry.cy
- Type: integer
- Required: yes

### observed_source.text_body_path
- Type: string or null
- Required: no
- Meaning: path hint to the text body

### observed_source.from_group
- Type: boolean
- Required: yes
- Meaning: whether the block came from grouped content

## normalized_workflow
- Type: object
- Required: yes
- Meaning: normalized treatment of the text block

### normalized_workflow.source_kind
- Type: string
- Required: yes
- Allowed values:
  - `text`
  - `table_cell`

### normalized_workflow.source_name
- Type: string
- Required: yes
- Meaning: workflow display name for the source container

### normalized_workflow.ordered_position
- Type: integer
- Required: yes
- Meaning: final block order used by the workflow

### normalized_workflow.reading_order_sort_key
- Type: object
- Required: no
- Meaning: top/left sort coordinates used in ordering

#### normalized_workflow.reading_order_sort_key.top
- Type: integer
- Required: yes if object exists

#### normalized_workflow.reading_order_sort_key.left
- Type: integer
- Required: yes if object exists

## projected_target
- Type: object
- Required: yes
- Meaning: intended Word-side projection for the text block

### projected_target.target_package_part
- Type: string
- Required: yes
- Allowed value: `word/document.xml`

### projected_target.target_object_kind
- Type: string
- Required: yes
- Allowed value:
  - `paragraph_sequence`

### projected_target.target_path_hint
- Type: string
- Required: yes
- Meaning: path hint to the target body location

### projected_target.projection_status
- Type: string
- Required: yes
- Allowed values:
  - `planned`
  - `written`
  - `omitted`
  - `manual_only`

## warning_entries
- Type: array of warning_entry
- Required: yes

## paragraph_entries
- Type: array
- Required: yes
- Meaning: paragraph-level records within this text block

---

# Paragraph entry

## observed_source
- Type: object
- Required: yes
- Meaning: paragraph-level source hints from DrawingML

### observed_source.drawingml_paragraph_path
- Type: string
- Required: yes
- Meaning: source path for the paragraph in DrawingML

### observed_source.paragraph_level_raw
- Type: integer or null
- Required: no
- Meaning: raw level from source markup if available

### observed_source.list_markup_kind
- Type: string or null
- Required: no
- Meaning: source list markup type, such as `a:buAutoNum`

### observed_source.list_markup_value
- Type: string or null
- Required: no
- Meaning: source list markup value, such as `arabicPeriod`

## normalized_workflow
- Type: object
- Required: yes
- Meaning: normalized paragraph meaning

### normalized_workflow.text
- Type: string
- Required: yes
- Meaning: extracted paragraph text

### normalized_workflow.level
- Type: integer
- Required: yes
- Meaning: normalized indentation/list level

### normalized_workflow.list_kind
- Type: string
- Required: yes
- Allowed values:
  - `plain`
  - `bullet`
  - `number`

### normalized_workflow.list_marker_hint
- Type: string
- Required: yes
- Meaning: visible marker hint or neutral hint used by the workflow

### normalized_workflow.ordered_sequence_reconstructable
- Type: boolean
- Required: yes
- Meaning: whether true ordered-list reconstruction is considered safe

## projected_target
- Type: object
- Required: yes
- Meaning: intended Word-side rendering of the paragraph

### projected_target.target_package_part
- Type: string
- Required: yes
- Allowed value: `word/document.xml`

### projected_target.target_object_kind
- Type: string
- Required: yes
- Allowed values:
  - `paragraph`
  - `list_paragraph`

### projected_target.target_path_hint
- Type: string
- Required: yes
- Meaning: path hint to the target paragraph location

### projected_target.paragraph_style
- Type: string or null
- Required: yes
- Meaning: intended Word paragraph style

### projected_target.numbering_plan
- Type: object
- Required: yes
- Meaning: intended numbering/list strategy for Word output

#### projected_target.numbering_plan.mode
- Type: string
- Required: yes
- Allowed values:
  - `plain`
  - `bullet_list`
  - `ordered_list`
  - `plain_fallback`

#### projected_target.numbering_plan.num_id
- Type: integer or null
- Required: yes
- Meaning: Word numbering definition id if used

#### projected_target.numbering_plan.ilvl
- Type: integer or null
- Required: yes
- Meaning: Word list indent level if used

### projected_target.projection_status
- Type: string
- Required: yes
- Allowed values:
  - `planned`
  - `written`
  - `omitted`
  - `manual_only`

## warning_entries
- Type: array of warning_entry
- Required: yes

---

# Visual entry

## observed_source
- Type: object
- Required: yes
- Meaning: source-side provenance for a detected visual

### observed_source.package_part
- Type: string
- Required: yes

### observed_source.relationships_part
- Type: string or null
- Required: no

### observed_source.shape_tree_path
- Type: string
- Required: yes

### observed_source.shape_kind
- Type: string
- Required: yes

### observed_source.shape_id
- Type: integer or null
- Required: no

### observed_source.shape_name
- Type: string
- Required: yes

### observed_source.geometry
- Type: object or null
- Required: yes
- Meaning: source coordinates and size if available

### observed_source.related_part
- Type: object or null
- Required: yes
- Meaning: relationship target information for media/chart part if available

#### observed_source.related_part.relationship_id
- Type: string
- Required: yes if object exists

#### observed_source.related_part.target_part
- Type: string
- Required: yes if object exists

### observed_source.non_visual_properties
- Type: object or null
- Required: yes
- Meaning: source `descr` and `title` metadata values if available

#### observed_source.non_visual_properties.descr
- Type: string
- Required: yes if object exists

#### observed_source.non_visual_properties.title
- Type: string
- Required: yes if object exists

### observed_source.from_group
- Type: boolean
- Required: yes

## normalized_workflow
- Type: object
- Required: yes
- Meaning: workflow treatment of the visual

### normalized_workflow.label
- Type: string
- Required: yes
- Meaning: stable label such as `Visual 1`

### normalized_workflow.visual_type
- Type: string
- Required: yes
- Allowed values:
  - `chart`
  - `photo`
  - `screenshot`
  - `table image`
  - `diagram`
  - `icon set`
  - `other detected visual`

### normalized_workflow.description
- Type: string
- Required: yes
- Meaning: description text copied or normalized by the workflow

### normalized_workflow.description_source
- Type: string
- Required: yes
- Allowed values:
  - `descr`
  - `title`
  - `missing`

### normalized_workflow.manual_review_required
- Type: boolean
- Required: yes
- Meaning: whether human review is still required for this visual

## projected_target
- Type: object
- Required: yes
- Meaning: intended Word-side projection for the visual entry

### projected_target.target_package_part
- Type: string
- Required: yes
- Allowed value: `word/document.xml`

### projected_target.target_object_kind
- Type: string
- Required: yes
- Allowed value:
  - `visual_description_paragraph`

### projected_target.target_path_hint
- Type: string
- Required: yes
- Meaning: target path hint for the visual description paragraph

### projected_target.associated_drawing_reference
- Type: object or null
- Required: yes
- Meaning: associated Word-side drawing/media reference if applicable

#### projected_target.associated_drawing_reference.word_relationship_id
- Type: string
- Required: yes if object exists

#### projected_target.associated_drawing_reference.word_media_part
- Type: string
- Required: yes if object exists

### projected_target.projection_status
- Type: string
- Required: yes
- Allowed values:
  - `planned`
  - `written`
  - `omitted`
  - `manual_only`

## warning_entries
- Type: array of warning_entry
- Required: yes

---

# Warning entry

## warning_entry
- Type: object
- Required: yes when used
- Meaning: explicit uncertainty, loss, ambiguity, or manual-review signal

### warning_entry.warning_code
- Type: string
- Required: yes
- Meaning: stable machine-readable warning identifier

### warning_entry.warning_message
- Type: string
- Required: yes
- Meaning: human-readable warning text

### warning_entry.warning_scope
- Type: string
- Required: yes
- Allowed values:
  - `manifest`
  - `slide`
  - `text_block`
  - `paragraph`
  - `visual`

### warning_entry.manual_review_required
- Type: boolean
- Required: yes
- Meaning: whether the warning requires human review

---

# Governing interpretation rule

For every object in the manifest, the reviewer should be able to answer:

1. Where did this come from technically?
2. What does the workflow think it means?
3. How is it intended to be represented in Word?
4. What is still uncertain or lossy?

That is the purpose of this schema.