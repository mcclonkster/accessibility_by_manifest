# Remediation Report

## Summary

- Runtime input DOCX: /Users/computerk/Library/CloudStorage/Dropbox/0_VSCode/extracted_chat_artifacts/test_outputs/Disorders_in_the_DSM5TR_Presentation_companion.docx
- Runtime input manifest: /Users/computerk/Library/CloudStorage/Dropbox/0_VSCode/extracted_chat_artifacts/test_outputs/Disorders_in_the_DSM5TR_Presentation_manifest.json
- Remediated DOCX target: /Users/computerk/Library/CloudStorage/Dropbox/0_VSCode/extracted_chat_artifacts/test_outputs/Disorders_in_the_DSM5TR_Presentation_final.docx
- Source PPTX from manifest: Disorders_in_the_DSM5TR_Presentation.pptx
- Total slides: 28
- Slides with warnings: 4
- Total carried-forward warnings: 6
- Script 1 review notes present: Yes

## What this script improved automatically

- Rebuilt the final DOCX from the authoritative manifest rather than guessing from the draft DOCX alone.
- Preserved the slide image in the final DOCX for each slide where an image could be resolved.
- Re-applied heading structure from preserved title information.
- Reconstructed list structure where confidence was high enough.
- Preserved fallback handling where ordered sequence or role interpretation remained uncertain.
- Carried unresolved warnings forward into the remediated artifact and this report.

## Remaining manual review needs

- Review all connector and relationship warnings.
- Review all standalone text box role uncertainties.
- Review visuals with missing or weak metadata.
- Review any slide where reading order confidence is low.
- Review any slide where the slide image could not be resolved or inserted.

## Slide 2. Defining Abnormal

- VISUAL_TYPE_UNCERTAIN — Visual type for 'Picture 3' is uncertain.

## Slide 4. Causes of Mental Illness

- READING_ORDER_LOW_CONFIDENCE — Reading-order heuristic may be weak for this slide.

## Slide 5. The Stress-Vulnerability Model

- VISUAL_TYPE_UNCERTAIN — Visual type for 'Picture 3' is uncertain.

## Slide 13. Schizophrenia Simulation

- SKIPPED_SHAPE_CONTENT_DETECTED — Shape 'Online Media 2' of type 'MEDIA' may carry meaning that this extractor does not represent.
- STANDALONE_TEXT_BOX_ROLE_UNCERTAIN — Standalone text box role is uncertain.
- STANDALONE_TEXT_BOX_NOT_MERGED — Standalone text box was preserved separately and not auto-merged.
