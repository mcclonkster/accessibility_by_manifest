---
title: PowerPoint to Word Decision Matrix
filename: powerpoint-to-word-decision-matrix.md
type: working-document
status: draft
created: 2026-04-18
updated: 2026-04-18
origin: chat
tags:
  - accessibility
  - wcag
  - wcag2ict
  - pptx
  - docx
  - presentationml
  - wordprocessingml
  - transformation
topics: []
aliases:
  - PPTX to DOCX Decision Matrix
  - PresentationML to WordprocessingML Decision Matrix
sources: []
cssclasses: []
notes:
  - Uses plain-language transformation rules rather than internal-only labels.
---

# PowerPoint to Word Decision Matrix

## Purpose

This matrix defines how PowerPoint content should be handled when transforming extracted content into a Word document. It sits between the normalized workflow model and the Word output rules.

It is intended to guide:
- what Word structure to create
- when that structure is safe to create
- when to fall back to a simpler representation
- when human review is required

It does not determine final accessibility compliance on its own.

## Decision Matrix

| PowerPoint source pattern | What we know from extraction | Word output to create | Use this when | Otherwise do this | Human review needed |
|---|---|---|---|---|---|
| Title placeholder | The slide has a true title placeholder with text | Heading paragraph | The title placeholder is present and non-empty | Use the fallback title rule below | Usually no, unless the title looks wrong |
| No title placeholder, but there is a clear first text block | There is no title placeholder, but one text block is clearly the title candidate | Heading paragraph using that text | The first text block is short, near the top, and not obviously body text | Use “Untitled slide [number]” and flag it | Yes |
| Body placeholder text | Text comes from a body/content placeholder | Normal paragraphs or list paragraphs | The content reads like main slide content and the grouping is clear | Keep as plain paragraphs | Sometimes |
| Subtitle placeholder text | Text comes from a subtitle placeholder | Separate paragraph near the heading | The subtitle is clearly secondary to the title | Keep as plain paragraph and flag uncertainty if role is unclear | Sometimes |
| Standalone text box | Text comes from a text box that is not a placeholder | Separate paragraph block | By default | Do not merge it into nearby content automatically | Yes |
| Standalone text box near an image, chart, or diagram | The text may be acting like a caption, label, or callout | Separate paragraph near the relevant content, plus a note if needed | The relationship is obvious enough to place nearby | Keep it separate and note that layout meaning may be lost | Yes |
| Table cell text from a real PowerPoint table | Text comes from actual table cells | Real Word table | The table structure is clear and worth preserving as a table | Use structured paragraphs if table reconstruction is not reliable | Yes if the table matters |
| Plain paragraph | No list markers were observed | Normal paragraph | Always | None | Usually no |
| Bullet list item with clear grouping | Bullet marker is present and neighboring items clearly belong to one list | Real Word bulleted list | The items are clearly part of one list and nesting is clear enough | Use plain paragraphs with bullet characters | Sometimes |
| Bullet-like text from a standalone text box | Bullet markers are present, but the text box role is uncertain | Plain paragraphs with bullet characters | By default | Do not force it into a real Word list automatically | Yes |
| Numbered item with clear sequence | Numbering intent is present and the sequence is clearly reconstructable | Real Word numbered list | The ordered sequence is obvious and stable | Use plain paragraphs with a neutral marker | Yes if order matters |
| Numbered item with unclear sequence | Numbering intent is present, but the true sequence is not trustworthy | Plain paragraph with a neutral prefix such as “[numbered]” | By default when sequence is unclear | Do not create a real numbered list | Yes |
| Picture or chart with a real description | A picture or chart was detected and there is description metadata | Visual description paragraph | The metadata is usable | Keep the entry and revise the wording manually if it is weak | Yes |
| Picture or chart with only a title | A picture or chart was detected, but only title metadata exists | Visual description paragraph using the title, marked as weak | The title is the only available source text | Keep the entry and flag that the description may be weak | Yes |
| Picture or chart with no description | A picture or chart was detected, but no description metadata exists | Visual description paragraph with a placeholder | Always | Do not omit the visual entry | Yes |
| Grouped content | Shapes are grouped and the group may hide structure or meaning | Preserve what was extracted and add a warning | Always | Do not pretend grouped meaning was fully reconstructed | Yes |
| Shapes plus connectors or arrows | The slide appears to use relationships, flow, or connectors to convey meaning | Preserve text separately and add an explicit warning about relationship meaning | Always | Do not try to silently rebuild the diagram logic | Yes |
| Image-heavy slide with little extractable text | Most meaning may live in visuals rather than text | Preserve extracted text and visual entries, plus a strong warning | Always | Do not assume the draft fully represents the slide | Yes |
| Weak reading order | The slide layout is likely multi-column, callout-heavy, or visually structured | Keep deterministic output order and warn | Always when order confidence is low | Do not invent a smarter order without stronger evidence | Yes |
| Preview image available | A matching preview image exists | Optional preview image for reference | When previews are enabled | Omit preview if not needed | No |
| Multiple preview images match one slide | More than one preview image could belong to the slide | Use the first match and warn | If preview inclusion is still desired | Omit preview if the ambiguity is too risky | Yes |

## Rules Above the Matrix

### Real text beats image text

If the source gives extractable text, write real Word text. Do not leave important text only inside a screenshot or preview image.

### Placeholder content and standalone text boxes are not treated the same way

Placeholder content is usually safer to map into headings, body paragraphs, or list structures. Standalone text boxes are preserved more conservatively.

### Numbering intent is not the same thing as true ordered sequence

If the order cannot be trusted, do not build a real numbered list.

### A visual entry should still exist even when metadata is weak or missing

Missing description text is a reason to warn and add a placeholder, not a reason to silently drop the visual.

### Diagram and connector meaning is a warning case, not an automatic reconstruction case

If arrows, lines, grouping, or spatial arrangement carry the meaning, preserve the text you have and make the loss explicit.

### Final accessibility judgment still happens on the finished Word file

This matrix guides transformation decisions. It does not replace final review of the actual `.docx`.

## Working Summary

- Placeholder title becomes a heading.
- Placeholder body becomes body paragraphs or lists if grouping is clear.
- Standalone text box becomes a separate paragraph by default.
- Clear bullet list becomes a real Word bullet list.
- Unclear numbered sequence becomes plain text with a neutral marker.
- Picture or chart becomes a visual description entry even if the description is missing.
- Grouped or connector-based meaning is preserved as text where possible and flagged clearly when relationship meaning may be lost.