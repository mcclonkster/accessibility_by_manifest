## Codex Continuation Handoff

### Project Context

This transcript is part of a larger effort to design an **accessibility-oriented document conversion and review pipeline**, specifically moving from **presentation or PDF source formats into a DOCX companion/review artifact**. In this branch of work, the conversation began with PDF internals, accessibility requirements, and JavaScript tooling, then narrowed into a concrete design problem: how to adapt an existing **PPTX→DOCX accessibility manifest workflow** into a **PDF→DOCX accessibility manifest**.

The user uploaded **five JSON manifest files** that all share a common schema for a PPTX→DOCX workflow. Those manifests encode a pipeline organized around: source package, target package, run config, summary, slide entries, text block entries, visual entries, warnings, and projected DOCX output. The assistant analyzed those five manifests and identified the common structural pattern.  

The conversation then shifted from “what can various PDF tools do?” to “how should we design a **PDF→DOCX manifest and extraction pipeline** that preserves accessibility-relevant evidence, uncertainty, and review work rather than hiding it?” A literal draft JSON Schema for `pdf_to_docx_accessibility_manifest` v0.1 was produced, along with a human-readable field dictionary and a sample manifest instance. This is the current stage: **schema and workflow design is underway; implementation has not yet been built**.

There is also important surrounding project context from an earlier pasted markdown requirements/spec file that was discussed in-chat but **was not one of the five uploaded files**. That spec described a much stricter “generator by construction” accessibility model with explicit semantic source fields, reading order, artifact handling, tag mapping, rejection rules, and validation. The user did not ask to continue that spec directly here, but it strongly influenced the architectural direction of the PDF→DOCX manifest design. 

### User Goals

The user is trying to build a workflow that does **not** merely convert files mechanically. The real goal is to create a **reviewable, accessibility-aware DOCX companion** from a more difficult source format, while preserving provenance, ambiguity, and unresolved accessibility issues rather than pretending the conversion is semantically complete.

More specifically, the user wants:

- A robust understanding of **PDF accessibility requirements** at the level of actual document parts and behaviors, not vague generalities.
- A tool and architecture strategy using **open-source JavaScript** where possible.
- A realistic assessment of what **PDF.js** and other JS tools can actually extract from existing PDFs.
- A re-envisioned workflow built around:
  **input PDF → extract → interpret/normalize → attach review flags → output DOCX**
- A **literal manifest schema** that supports this workflow and treats accessibility-relevant data as first-class.
- A schema that is explicit about what was:

  * directly extracted,
  * inferred,
  * uncertain,
  * and still requiring manual review.

The user’s goals became clearer over time through repeated correction. At first the discussion wandered across PDF tooling generally, accessible PDF creation, remediation, and Adobe-based workflows. The user repeatedly forced the focus back to the real question: **what can be extracted from existing PDFs, what accessibility-relevant information should be captured, and how should that be encoded in a schema that supports a DOCX review workflow?**

### Reasoning That Must Be Preserved

Several hard-won conceptual distinctions emerged and must carry forward.

#### 1. Accessibility requirements must drive the design

The user provided accessibility docs not to force Adobe usage, but to establish the **requirement surface**: what an accessible PDF has to do, what information matters, and which conditions are machine-detectable vs human-judgment-heavy. The user repeatedly pushed for thinking in terms of **all the accessibility layers** rather than generic PDF editing.

This led to a durable insight: any serious schema or workflow needs to account for:

- real/searchable text,
- correct character mapping,
- tags/structure,
- reading order,
- headings/lists/tables/figures/links/forms,
- language/title metadata,
- permissions/security,
- navigation/bookmarks,
- OCR/image-only pages,
- figures and non-text alternatives,
- and explicit review states where automation cannot settle meaning.

#### 2. The right question is not “can a tool remediate PDFs?”

The assistant repeatedly drifted into remediation, Adobe, or creation-side tooling. The user corrected this several times. The user’s actual concern in this branch was **extraction and evidence capture from existing PDFs**, not “which tool can fix everything.”

That means the relevant logic is:

- what information can be extracted,
- how trustworthy that information is,
- and how it should be represented for downstream human review and DOCX projection.

This is why PDF.js became central: not because it is a universal PDF accessibility solution, but because it is the strongest **open-source JavaScript extractor/inspector** in the supported public API surface.

#### 3. Provenance must be explicit

One of the most important design insights is that a PDF→DOCX manifest cannot flatten “what we saw” and “what we think it means” into one layer.

For PDF especially, the same piece of text could come from:

- a real tag tree,
- positioned untagged text,
- OCR,
- a form field,
- an annotation,
- outline/bookmarks,
- or other page-level evidence.

So the workflow must separate:

- **observed source evidence**
- **normalized interpretation**
- **warning/review state**
- **projected target**

This mirrors the pattern already present in the five PPTX→DOCX manifests, where source evidence, normalized workflow, warnings, and projected target are distinct layers. 

#### 4. PDF needs stronger provenance and confidence than PPTX

A PPTX file offers authoring clues like title placeholders, body placeholders, text boxes, and table cells. The existing manifests exploit those signals and flag uncertainty when role inference becomes weak. For example, the manifests explicitly distinguish `placeholder_text`, `standalone_text_box`, and `table_cell`, and attach warning codes like `STANDALONE_TEXT_BOX_ROLE_UNCERTAIN` or `TABLE_CELL_TEXT_EXTRACTED`.  

For PDF, those authoring cues are much weaker or absent. So the PDF version needs stronger fields for:

- source evidence type,
- role basis,
- semantic source quality,
- reading order basis,
- OCR-related uncertainty,
- and review flags.

This is one of the biggest conceptual leaps in the transcript and should remain central.

#### 5. Accessibility-related fields belong in v0.1 even when unknown

A strong later decision: **if a field is accessibility-related, it belongs in v0.1**, even if the pipeline can only set it to `null`, `unknown`, or `manual_review_required`. The user did not want a minimal schema that postpones accessibility concerns. The assistant adjusted accordingly and expanded the proposed v0.1 to include accessibility-relevant sections rather than deferring them.

This is a major design rule: **absence of certainty is not a reason to omit the field**.

#### 6. The output DOCX is a review artifact, not just a converted document

The target is not slide fidelity or raw page dumping. The DOCX is meant to be a **linearized, editable, reviewable semantic companion** where accessibility issues can be seen, corrected, and carried forward.

That logic was already present in the PPTX manifests, where each slide projects into Word headings and page breaks, with warnings attached. The PDF version is meant to do the analogous thing, but at document/section/block level rather than naive page dumping.

### Constraints and Non-Negotiables

The user enforced many constraints and corrections that Codex must respect.

#### Technical and architectural constraints

- **Open-source JavaScript only** was an explicit constraint for the tooling discussion.
- The user does **not** want Adobe assumed as the solution path.
- PDF.js is the main extraction engine under consideration because it can extract a large public-surface set of document and page information from existing PDFs.
- OCR is outside PDF.js’s public extraction surface and would require another tool; this absence must be modeled explicitly, not hand-waved away.
- Public API distinctions matter to the user, but only insofar as they affect what is actually available and stable. Earlier assistant over-focus on remediation and API caveats caused confusion.

#### Process constraints

- Do not answer nearby questions instead of the actual one.
- Do not drift into remediation when the user is asking about extraction.
- Do not say “I didn’t check” where careful checking is required; the user explicitly rejected that standard as unacceptable, especially for tagging/structure questions.
- Do not overgeneralize from one file; compare the actual uploaded manifests.
- Do not miscount the uploaded files. The user corrected the assistant: **there were five uploaded manifest files**, not six.
- Preserve uncertainty explicitly rather than smoothing it away.

#### Style and fidelity constraints

- The user repeatedly pushed back against:

  * letter-based matrix legends instead of full words,
  * assistant overfocus on Adobe,
  * confusing shifts into remediation,
  * and flattening nuanced requirements into generic summaries.
- The user wants **continuation-quality fidelity**. That means carrying forward the real reasoning, not just polished recaps.
- The user’s corrections are high signal and must be treated as project decisions.

### Established Decisions

These points appear settled enough to build on.

#### 1. Existing PPTX→DOCX manifests share one schema

The five uploaded JSON files share the same manifest family and overall structure: top-level manifest metadata, source package, target package, run config, summary, warnings, and slide entries with nested text/visual evidence and projected output.  

#### 2. The workflow spine is correct

The user agreed with the distilled logic:

**input → extract → interpret/normalize → attach review flags → output DOCX**

This is the core architectural spine for the PDF re-envisioning.

#### 3. PDF.js is the primary extraction engine for v0.1

The assistant eventually produced a careful inventory of what PDF.js can extract via its **public Display-layer API**, including document metadata, MarkInfo, outline, destinations, permissions, forms, JavaScript flags/actions, page geometry, page text, structure trees, annotations, XFA, operator lists, and more. This was accepted as the central extraction basis for the v0.1 manifest.

#### 4. Accessibility-related fields must be in v0.1

Anything accessibility-related should be modeled in v0.1, even if some values are not directly extractable and must be represented as unknown or review-required.

#### 5. The PDF manifest should not just rename slide concepts to page concepts

A naive port from PPTX slide manifests to PDF page manifests is not enough. The PDF version needs:

- page-level evidence,
- document-level accessibility/navigation/interactivity metadata,
- raw extracted blocks,
- normalized interpreted blocks,
- explicit provenance and confidence,
- and review warnings.

#### 6. A draft JSON Schema and sample instance now exist

A literal JSON Schema draft for `pdf_to_docx_accessibility_manifest` v0.1 was produced, followed by:

- a human-readable field dictionary,
- and a sample manifest instance designed to validate against it.

This is the most concrete current artifact to continue from.

### Tentative but Valuable Directions

These directions were developed enough to matter, but are not fully locked.

#### 1. Use page-level evidence plus normalized block-level structure

The likely architecture is:

- top-level document sections for metadata/accessibility/navigation/interactivity,
- `page_entries` for page-local evidence,
- `raw_block_entries` for low-level text/content blocks,
- `normalized_block_entries` for interpreted semantic blocks,
- and `projected_target` for DOCX mapping.

This direction is strong and probably right, but the exact final field set may still evolve.

#### 2. Distinguish extracted semantics from inferred semantics

The schema draft already leans toward fields like:

- `source_evidence_type`
- `role_basis`
- `role_confidence`
- `semantic_source_quality`
- `reading_order_basis`

This should almost certainly stay, though exact vocabularies may change.

#### 3. Warning taxonomy will likely expand

A first batch of PDF-specific warning ideas emerged, such as:

- no tag tree,
- OCR detected/required,
- reading order ambiguous,
- image-only page suspected,
- figure description missing,
- form label uncertainty,
- caption-figure association uncertainty.

These warnings were conceptual and partly reflected in the schema draft, but not fully stabilized.

#### 4. Some public PDF.js extractables may be overkill for v0.1

The assistant separated core vs nice-to-have vs overkill extractables. That triage is useful, but because the user explicitly wants all accessibility-related fields in v0.1, some earlier “medium/low priority” exclusions may need reconsideration if they impact accessibility.

### Rejected or Corrected Directions

These are important because they mark repeated failure modes and project boundaries.

#### 1. Over-focusing on remediation

The assistant repeatedly brought the discussion back to remediation, Acrobat, or creation-side completeness. The user explicitly corrected this multiple times. This branch is about **extraction/inspection/schema design for existing PDFs**, not full remediation capability.

#### 2. Assuming Adobe as the frame

The user explicitly said the accessibility docs were about requirements, **not** about assuming Adobe must be used. Any continuation that treats Acrobat as the default center of gravity will repeat a mistake.

#### 3. Using vague or incomplete tool claims

The user rejected “I didn’t check” as an acceptable standard when discussing tagging and structure. For claims about tool capability, especially accessibility-relevant extraction or tagging, Codex should verify carefully and speak only to what has actually been checked.

#### 4. Flattening the uploaded file set incorrectly

The assistant incorrectly counted six files because it mixed in an earlier markdown spec. The user corrected this. For the current file-based schema discussion, the relevant uploaded set is **five JSON manifests**.

#### 5. Letter-coded capability matrices

The user objected to single-letter shorthand in tables and wanted full words. More broadly, they want clarity and directness over compact but opaque notations.

#### 6. Treating page-level PDF structure as equivalent to document-level semantics

The user found it weird that PDF.js’s public structure-tree extraction is page-level when the PDF structure tree is fundamentally document-level. This mismatch matters. Codex should preserve that distinction and not gloss over it.

### Reusable Assets

There is substantial reusable work already produced.

#### 1. The five PPTX→DOCX manifest examples

These are the strongest empirical artifacts for understanding the existing conversion-manifest pattern. They provide:

- the manifest spine,
- nesting patterns,
- warning object structure,
- observed vs normalized vs projected layering,
- and examples of how uncertainty is preserved.  

#### 2. The extracted shared schema for those five manifests

The assistant already consolidated the five-manifest common structure:

- top-level manifest fields,
- shared nested objects,
- text block layout,
- paragraph layout,
- visual entries,
- warning entry shape.

That work can be reused as the conceptual ancestor for the PDF manifest.

#### 3. The PDF.js extraction inventory

A detailed inventory was built of what PDF.js can extract from its public API, including:

- document metadata,
- MarkInfo,
- outline/bookmarks,
- named destinations,
- page labels,
- viewer preferences,
- permissions,
- attachments,
- optional content/layers,
- form fields,
- calculation order,
- JavaScript actions,
- page text,
- page structure trees,
- annotations,
- XFA,
- operator lists,
- page geometry and references.

This inventory is directly reusable for implementing or refining the manifest fields.

#### 4. The drafted JSON Schema for `pdf_to_docx_accessibility_manifest` v0.1

A literal draft schema was produced. It includes:

- source package,
- target package,
- run config,
- document summary,
- document metadata,
- document accessibility,
- document navigation,
- document security,
- document interactivity,
- document warnings,
- page entries,
- raw block entries,
- normalized block entries,
- projected target.

This is likely the main artifact Codex should continue refining.

#### 5. The human-readable field dictionary

A continuation-friendly explanation of the draft schema was produced. This is reusable as documentation and as a logic map for implementation.

#### 6. The sample manifest instance

A concrete sample instance was created to demonstrate intended use and validation behavior. This is reusable for testing, schema refinement, and implementation scaffolding.

#### 7. The earlier generator-by-construction spec

Although not one of the five uploaded manifests, the earlier markdown spec contains important conceptual assets:

- explicit reading order,
- explicit node typing,
- explicit artifact classification,
- explicit tag mapping,
- rejection rules instead of guessing,
- and machine-checkable vs human-judgment boundaries. 

This should remain a conceptual north star for the PDF manifest, even if the current work is only building an evidence/review pipeline rather than a full generator.

### Open Threads and Next Actions

The work is not finished. The likely next continuation points are:

#### 1. Validate and refine the JSON Schema draft

The current schema draft needs inspection for:

- consistency,
- required-vs-optional decisions,
- whether any accessibility-relevant fields are still missing,
- whether any “nice to have” fields should be promoted into v0.1,
- and whether the structure is too strict or not strict enough for real data.

#### 2. Check whether the sample instance actually validates

A sample manifest instance was written, but no actual validation step happened in the transcript. That needs to be done.

#### 3. Reconcile field design with actual PDF.js outputs

Some schema fields are clearly proposed normalization/review fields rather than direct extractor outputs. Codex should map:

- which fields PDF.js fills directly,
- which are derived,
- which must begin as `null`/`unknown`,
- and which would need secondary tooling (especially OCR).

#### 4. Decide the first implementation boundary

A key next decision is whether the first implementation should:

- only generate the manifest JSON,
- generate manifest + draft DOCX projection,
- or generate manifest + review appendix + preview artifacts.

#### 5. Define the warning taxonomy more concretely

The warning system is central. The schema already includes generic warning entries, but the actual PDF-specific warning codes and their trigger logic need more formalization.

#### 6. Decide how much document-level structure to reconstruct from page-level extraction

Because PDF.js exposes page-level structure trees publicly, Codex will likely need to decide how to assemble those into document-level normalized structure. This is both a technical and conceptual open thread.

#### 7. Determine whether the manifest should be page-first or section/block-first

The current draft includes both page entries and normalized block entries, which is probably right, but Codex may need to finalize the authoritative organizing principle.

### Guidance for Codex

Do not restart this as a generic “how do we handle PDFs?” discussion. The user already did the narrowing work.

Continue from these settled points:

- The workflow spine is **input PDF → extract → interpret/normalize → attach review flags → output DOCX**.
- The project is **extraction/evidence/schema design**, not remediation.
- **Open-source JavaScript** remains the working constraint.
- **PDF.js** is the main extraction engine for v0.1.
- **Accessibility-relevant fields must be present in v0.1**, even when unresolved.
- Preserve the separation between:

  * raw source evidence,
  * normalized interpretation,
  * review flags,
  * projected DOCX output.

Avoid the assistant’s earlier failure modes:

- do not drift back into Adobe/remediation unless the user explicitly changes scope,
- do not make unchecked claims about tool capability,
- do not compress uncertainty away,
- do not conflate uploaded files with earlier in-chat pasted specs,
- and do not flatten the reasoning into a neat but lossy recap.

The most productive continuation is probably:

1. validate the current schema and sample instance,
2. refine any weak or inconsistent fields,
3. map the schema precisely to PDF.js outputs and derived fields,
4. and then sketch or implement the first extraction prototype.
