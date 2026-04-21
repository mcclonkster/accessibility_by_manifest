---
title: Project Full Report
filename: project-full-report.md
type: project-report
status: active
created: 2026-04-18
updated: 2026-04-18
origin: chat
tags:
  - accessibility
  - wcag
  - wcag2ict
  - docx
  - pptx
  - ooxml
  - presentationml
  - wordprocessingml
  - automation
  - remediation
topics: []
aliases:
  - Full Project Report
sources: []
cssclasses: []
notes:
  - Full report on the PowerPoint-to-DOCX accessibility workflow project.
---

# Executive Summary

This project is establishing a structured workflow for turning PowerPoint content into a DOCX artifact that can support accessibility remediation and final review. The work has progressed from an initial conversion idea into a more rigorous workflow architecture grounded in three technical layers: source-side PresentationML, a normalized workflow model, and target-side WordprocessingML. The resulting design is intended to support a disciplined remediation process rather than a simplistic one-step conversion.

The project has reached a meaningful design milestone. The two-script model is now defined. Script 1 is responsible for extraction, preservation, and warning generation. Script 2 is responsible for controlled reconstruction and remediation of the DOCX. A normalized manifest, serialized authoritatively as JSON, has been selected as the process truth that links those stages. That decision is the central organizing feature of the current project state.

Implementation remains incomplete. Script 1 has been drafted and iteratively improved, but it still requires a final integrated pass to align it with the latest schema and output requirements. Script 2 remains at the design stage. The project is therefore best described as architecturally mature but not yet implementation-complete.

# Project Background

The original problem space centered on the idea of moving from PowerPoint to Word in a way that would support accessibility goals. Early discussion surfaced a critical distinction: producing a DOCX file is not the same thing as producing a DOCX artifact that can be trusted in an accessibility workflow.

That realization drove the project away from a simple “export or convert” mindset and toward a process model with explicit stages:

- extraction
- preservation
- warning generation
- remediation
- final review

This reframing was necessary because the source and target document systems are structurally different. PowerPoint stores content in a presentation-shaped object model. Word stores content in a document-flow model. Accessibility review, meanwhile, is ultimately concerned with the final artifact that is posted or distributed, not merely with the source or the conversion logic.

# Objective

The project objective is to build a workflow that supports creation and remediation of final DOCX artifacts derived from PowerPoint while preserving source provenance, structural hints, uncertainty, and known areas of likely meaning loss.

The project is not attempting to automate accessibility certification. Its goal is to support a workflow in which automation prepares and improves the artifact, while final review remains focused on the actual DOCX output and its readiness for accessibility review under the relevant standards framework.

# Standards and Accessibility Context

The standards framing reached in the project is now clear.

The final DOCX is treated as a non-web document. WCAG supplies the criteria set. WCAG2ICT is used as the interpretation guide for applying those criteria to non-web documents. Word-specific remediation practices and final manual review are treated as the implementation layer.

The project also clarified the legal nuance that may apply in a public community college setting. The likely federal baseline in that context is the DOJ Title II web/mobile rule, which uses WCAG 2.1 AA for covered web content and many posted electronic documents. That legal baseline is related to, but not identical with, a stricter internal technical target. The project is therefore grounded in a workflow model that is standards-aware without pretending that the scripts themselves determine legal compliance.

# Technical Architecture

## Source Layer

The source-side representation is an OOXML package using OPC as the packaging model and PresentationML as the document vocabulary. DrawingML is relevant within that package because text, shapes, and graphics often rely on DrawingML structures.

This source layer is object-oriented and slide-shaped. It is well suited to authoring and rendering presentations, but it is not a good direct workflow contract for remediation.

## Middle Layer

The middle layer is the normalized workflow model. This is the central architectural choice of the project.

The normalized model is not a mirror of OOXML. It is a workflow representation designed to preserve the information that the process actually needs. That includes source provenance, normalized meaning, target projection, and warnings. This layer exists because neither the raw PPTX nor the draft DOCX is sufficient as the sole process truth.

## Target Layer

The target-side representation is a DOCX package using WordprocessingML. This layer is document-flow oriented and more suitable for accessible structure, headings, lists, paragraphs, and remediation-oriented output.

The project treats WordprocessingML not as a passive output file format but as the structure that Script 2 is meant to improve deliberately and cautiously.

# Two-Script Workflow

## Script 1: Extraction and Preservation

Script 1 is responsible for ingesting the PPTX and producing workflow-ready outputs.

Its intended outputs are:

- a companion DOCX draft
- a review-notes Markdown file
- an authoritative JSON manifest
- a YAML mirror of that manifest
- a Markdown extract report

Its role is to preserve what can be extracted, preserve provenance and source-role distinctions, carry forward warnings and uncertainty, and generate a draft artifact that can enter remediation. It is not designed to certify accessibility or to claim that the resulting DOCX is final.

## Script 2: Remediation and Reconstruction

Script 2 is responsible for consuming Script 1 outputs and improving the DOCX artifact where the preserved evidence supports stronger structure.

Its role is to reconstruct better Word semantics where confidence is high, preserve caution where confidence is low, and produce a remediated DOCX plus remediation reporting. Script 2 is therefore not merely a release gate. It is the reconstruction layer that stands between raw extraction and final human review.

# Manifest Strategy

A central project decision is that the authoritative process truth should be the normalized manifest, not the PPTX and not the draft DOCX.

## Authoritative format

JSON has been selected as the authoritative machine-readable manifest because it is deterministic, structured, and easier to validate safely.

## Parallel views

YAML is treated as a human-friendly mirror of the same data. Markdown is treated as a rendered inspection view derived from that same data. Neither replaces the JSON manifest as the automation contract.

## Object model

The manifest uses a three-band structure for meaningful objects:

- observed source
- normalized workflow
- projected target

Warnings are represented explicitly, not implied.

## Object classes

The project has conceptually defined this model for:

- slide entries
- text block entries
- paragraph entries
- visual entries
- warning entries

A draft JSON Schema exists conceptually to formalize that contract, and example valid and invalid manifests plus a field dictionary have also been defined conceptually.

# Source-Role Modeling

One of the most important mid-project corrections concerned text-bearing objects that are not tied to slide-layout placeholders.

Earlier drafts preserved their text but did not preserve their role distinctions strongly enough. This was identified as a significant weakness because standalone text boxes often behave differently from placeholder-driven content. They may function as captions, labels, callouts, floating notes, or layout-dependent annotations.

The project has now decided that those objects must be modeled explicitly.

## Required distinctions

The source text container classes now identified as necessary are:

- placeholder text
- standalone text box
- table cell

## Required integrated fields

The following fields have been identified as necessary across extraction, schema, and mapping:

- `has_placeholder_semantics`
- `placeholder_type`
- `source_text_container_type`
- `interpreted_text_role`
- `role_confidence`
- `auto_merge_allowed`

This decision is important because it prevents standalone text boxes from being treated as generic text and then silently merged into stronger semantics downstream.

# Script 1 Revision History and Current Maturity

Script 1 has undergone several rounds of conceptual revision. Through those iterations, the project significantly improved:

- safety behavior
- error handling
- atomic writes
- dry-run logic
- review-note handling
- contract language honesty
- metadata-source distinctions
- duplicate preview warning behavior
- slide separation
- list-hint preservation
- warning quality

However, Script 1 still requires one more integrated pass. The current conceptual architecture is ahead of the current implementation. The next revision must unify the existing script direction with the latest manifest design, schema work, and source-role distinctions.

# Script 2 Maturity

Script 2 has not yet been implemented, but its role is now much clearer than it was earlier in the project.

It is no longer being framed as a pure release-decision script. It is now defined as a remediation transformer that should consume the authoritative manifest and use it to rebuild stronger DOCX structure where that can be done safely.

The key dependency for Script 2 is therefore the quality and completeness of Script 1’s manifest output.

# Work Completed

The project has completed the following conceptual work.

## Completed design work

- reframed the project around final-artifact accessibility workflow
- established the two-script architecture
- selected the normalized manifest as the process truth
- selected JSON as the authoritative machine-readable format
- selected YAML and Markdown as parallel human-readable outputs
- defined the three-band source/workflow/target model
- clarified the accessibility and WCAG/WCAG2ICT framing
- identified the need to explicitly model standalone text boxes
- drafted a literal JSON Schema conceptually
- drafted example valid and invalid manifests conceptually
- drafted a field dictionary conceptually

## Partially completed implementation work

- multiple Script 1 drafts were produced and improved conceptually
- practical behaviors such as dry run, atomic write, and warning handling were explored and refined
- but the current implementation does not yet fully match the latest architecture

# Outstanding Work

## Integrated Script 1 pass

Script 1 must be revised in one integrated pass so that it:

- emits the authoritative JSON manifest
- emits the YAML mirror
- emits the Markdown extract report
- fully incorporates standalone text box distinctions
- aligns its data model with the current schema contract

## Script 2 contract and implementation

Script 2 still needs:

- a locked implementation contract
- mapping rules
- confidence and loss policy
- writeback rules
- code implementation

## Transformation governance artifacts

The project has identified the need for several formal artifacts that still remain to be written:

- source inventory
- target inventory
- mapping decision matrix
- confidence and loss policy
- writeback strategy
- test corpus

These are now understood to be the real guidance layer for actual PresentationML-to-WordprocessingML decisions.

# Risks and Constraints

## Representation risk

The project cannot eliminate all meaning loss because some slide meaning is inherently layout-driven, diagram-driven, or visually implied. That risk must remain explicit in warnings and manual review expectations.

## Integration risk

There is a real risk of drift because the conceptual architecture has continued to improve after earlier script drafts. That makes an integrated Script 1 revision necessary before Script 2 can be built cleanly.

## Overclaim risk

The project must continue to resist language that suggests the scripts determine accessibility compliance automatically.

## Scope risk

There remains a risk of accidental expansion into OCR, rendering, or over-ambitious reconstruction. Those remain outside the intended current phase.

# Recommended Next Phase

The next phase should begin with a full integrated revision of Script 1. That revision should implement the current architecture rather than introducing new theory.

The recommended order is:

1. Align Script 1 outputs with the authoritative manifest strategy.
2. Integrate standalone text box distinctions into extraction and manifest output.
3. Align Script 1 with the latest schema field definitions.
4. Lock Script 2’s contract against the actual Script 1 outputs.
5. Write the mapping matrix and confidence/loss rules.
6. Implement Script 2.

# Overall Assessment

The project is well advanced conceptually. It has a coherent architecture, a mature standards-aware framing, and a credible path from extraction to remediation. The current gap is not conceptual confusion. The current gap is integration and implementation discipline.

The project is ready to move out of broad architecture work and into a focused implementation phase, beginning with an integrated Script 1 revision and followed by the build-out of Script 2.