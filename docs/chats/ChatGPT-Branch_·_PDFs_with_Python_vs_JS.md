# Branch · PDFs with Python vs JS

#### You:
Original custom instructions no longer available

#### You:
working with pdfs using python, working with pdfs using javascript

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m checking current PDF tooling so I can give you the field-standard options rather than a stale library list. I’m focusing on practical use: read/write, extract text/tables, generate PDFs, render pages, and edit/merge.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’ve got the current library landscape. The split is pretty clean: Python is strongest for extraction and repair-heavy workflows; JavaScript is strongest for browser-side rendering and client-side generation.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## The operative distinction

“Working with PDFs” splits into a few different jobs: generating new PDFs, editing existing PDFs, extracting text/tables/layout, and rendering pages for viewing. The best tool depends much more on that job than on the language alone. Based on the current mainstream open-source landscape, Python is stronger for extraction/analysis/repair workflows, while JavaScript is especially strong for browser rendering and client-side PDF generation/editing. citeturn744067search12turn744067search1turn744067search2turn744067search11turn566257search1turn566257search12turn566257search2turn642725search2

## Python

For **general-purpose PDF editing** in Python, the default mainstream choice is **pypdf**. Its docs describe it as a pure-Python library for splitting, merging, cropping, transforming pages, adding metadata/viewing options/passwords, and retrieving text/metadata. citeturn744067search12turn744067search0

For **lower-level PDF object work, repair, and more spec-near manipulation**, **pikepdf** is the sharper tool. It is built on **qpdf**, which its project describes as a mature, actively maintained C++ PDF library. That makes it a good fit when pypdf feels too high-level or too forgiving. citeturn744067search1

For **fast extraction, page rendering, conversion, and manipulation**, **PyMuPDF** is one of the strongest Python options. Its docs describe it as a high-performance library for extraction, analysis, conversion, and manipulation; its GitHub page also notes the open-source **AGPL** and commercial licensing model, which matters if you are shipping closed-source software. citeturn744067search11turn744067search3turn744067search7

For **text/layout/table extraction**, the usual Python names are **pdfplumber** and **pdfminer.six**. pdfplumber is built on pdfminer.six and is aimed at detailed access to characters, rectangles, and lines, plus table extraction and visual debugging; pdfminer.six is the lower-level text-analysis/extraction tool with access to positions, fonts, and colors. In practice, pdfplumber is usually the nicer first stop when you need structured extraction from machine-generated PDFs. citeturn744067search2turn744067search14turn642725search1turn642725search9

For **creating PDFs from scratch** in Python, **ReportLab** is still one of the standard names. Its docs describe it as a library for directly creating PDFs and graphics from Python. citeturn642725search12turn642725search0

## JavaScript

For **rendering/viewing PDFs in the browser**, the standard answer is **PDF.js**. Mozilla describes it as a general-purpose, web-standards-based platform for parsing and rendering PDFs, and the npm package **pdfjs-dist** is the prebuilt distribution most JS projects actually install. citeturn566257search1turn566257search5turn642725search3turn642725search19

For **creating and modifying PDFs in JavaScript across runtimes**, **pdf-lib** is one of the cleanest mainstream choices. Its docs state that it works in Node, browsers, Deno, and React Native, and supports creating PDFs from scratch or modifying existing ones. citeturn566257search0turn566257search12turn642725search22

For **programmatic PDF generation** in JS, **PDFKit** is a long-standing standard, especially on the Node side. Its project describes itself as a generation library for Node and the browser, with both low-level functions and higher-level abstractions; its docs also cover form creation. citeturn566257search2turn566257search6turn566257search18

For **browser-first PDF generation**, **jsPDF** is still widely used. It is explicitly aimed at generating PDFs in JavaScript on the client side. citeturn566257search3turn566257search23

For **declarative PDF generation** from structured content, **pdfmake** is a strong option. Its docs describe server-side and client-side generation in pure JavaScript with a document-definition style API. citeturn642725search2turn642725search6turn642725search10

## Best current defaults

If you want the shortest honest answer:

- **Python**
  - **pypdf** for merge/split/basic edits
  - **pikepdf** for lower-level repair/object manipulation
  - **PyMuPDF** for speed, rendering, and extraction-heavy workflows
  - **pdfplumber** for table/text/layout extraction
  - **ReportLab** for generating PDFs from scratch citeturn744067search12turn744067search1turn744067search11turn744067search2turn642725search12

- **JavaScript**
  - **PDF.js / pdfjs-dist** for viewing/rendering/parsing
  - **pdf-lib** for editing/filling/creating PDFs in app code
  - **PDFKit** or **pdfmake** for generated documents
  - **jsPDF** for browser-side export/download flows citeturn566257search1turn642725search3turn566257search12turn566257search2turn642725search2turn566257search3

## What professionals usually do

A very common real-world pattern is:

- **Frontend viewer**: PDF.js
- **Frontend edit/fill/stamp/merge**: pdf-lib
- **Backend extraction pipeline**: Python, often PyMuPDF and/or pdfplumber/pdfminer.six
- **Backend generated reports/invoices**: ReportLab in Python, or PDFKit/pdfmake in JS depending on the stack

That last point is an inference from the capabilities and positioning of these tools rather than a single source stating “the industry standard stack is X,” but it matches the current ecosystem pretty well. citeturn566257search1turn566257search12turn744067search11turn744067search2turn642725search1turn642725search12turn566257search2turn642725search2

## My blunt recommendation

If your goal is **serious PDF extraction or document forensics**, start with **Python**. If your goal is **browser-based viewing/editing/export**, start with **JavaScript**. If your goal is **full-stack PDF work**, the most practical combo is usually **PDF.js + pdf-lib on the JS side** and **PyMuPDF/pdfplumber/pypdf on the Python side**. citeturn566257search1turn566257search12turn744067search11turn744067search2turn744067search12

If you want, I can turn this into a tighter **task-by-task cheat sheet** like “extract text,” “fill forms,” “convert pages to images,” “merge/split,” “parse tables,” and “generate reports,” with the exact best library for each in Python and JS.


#### You:
What about python and javascript for this kind of stuff?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m checking what Python and JavaScript can actually do for **PDF accessibility work specifically**, not just generic PDF editing. The important line here is automation-friendly tasks versus the parts that still need real tagging and reading-order remediation.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
The honest answer is getting clearer: Python and JavaScript are useful here, but mostly for **detection, extraction, OCR, generation, and pipeline glue**. They are much weaker as a substitute for Acrobat-level remediation of real-world inaccessible PDFs.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## For **accessible PDF work specifically**

The blunt answer is: **Python and JavaScript can help a lot, but they do not replace the normal accessibility workflow for real PDFs**. The current guidance in the docs you uploaded is consistent on the big points: start with an accessible source document, preserve tags on export, prefer HTML or web forms when you can, and expect Acrobat Pro plus manual review for serious remediation work. Searchable text, tags, reading order, alt text, title/language, and accessible form behavior are all part of the job. fileciteturn2file0 fileciteturn2file2 fileciteturn1file17 citeturn653071search5turn653071search11

## What Python is good at

Python is strong for the **pipeline parts**:

- checking whether text is selectable
- OCRing scanned PDFs
- extracting text, images, metadata, outlines, and form fields
- batch auditing for obvious failures
- making repetitive low-risk fixes
- generating PDFs from structured data

That fits the uploaded guidance pretty well, because the first triage questions are often “is this just an image?” and “does it have tags?”, and OCR plus automated checks are useful early steps even though they are not sufficient for full remediation. fileciteturn2file0

For libraries, the current mainstream Python tools are still things like **pypdf**, **pikepdf**, and **PyMuPDF** for general PDF manipulation, inspection, repair, and extraction. PyMuPDF also exposes some lower-level tagged-PDF-related data such as `/MarkInfo`, which is useful if you are inspecting structure-related flags programmatically. citeturn635363search7turn589136search4

Where Python gets weaker is **true accessible-PDF authoring/remediation in the open-source mainstream**. The clearest officially documented Python options I found are commercial or partly commercial:

- **Aspose.PDF for Python via .NET** explicitly documents creating tagged PDFs, validating against **PDF/UA-1**, converting to PDF/UA with automatic tagging, and creating accessible tagged form fields. citeturn668866view0
- **ReportLab** has accessibility documentation, but its own docs say tagging is available in **ReportLab Plus** rather than the open-source edition. citeturn985471view1

So for Python, my honest read is:

- **excellent** for OCR, extraction, preflight, batch inspection, and glue code
- **possible** for accessible generation if you use a commercial stack like Aspose
- **not a great replacement** for Acrobat-level remediation of arbitrary existing PDFs fileciteturn2file0 citeturn668866view0turn985471view1

## What JavaScript is good at

JavaScript is strongest when the PDF work is tied to the **browser or app UI**.

- **PDF.js** is the standard viewer/parsing stack. Its own docs frame it as a core/display/viewer system for parsing and rendering PDFs, which makes it great for viewing, inspection tooling, and custom in-browser experiences. It is not primarily an accessibility-remediation engine. citeturn985471view5turn589136search7
- **PDFKit** is the most promising JavaScript option I found for **generating accessible PDFs from scratch**. Its docs explicitly have an accessibility section and document options for marked content, logical structure, Tagged PDF, and **PDF/UA** such as `tagged: true` and `subset: 'PDF/UA'`. citeturn985471view0turn970249search4

The big caution on the JS side is **editing existing tagged PDFs while preserving accessibility structure**. I would be careful with **pdf-lib** for that use case. Its GitHub issue tracker and discussions include reports that tagged accessibility structure can be lost when pages are copied or when a manipulated PDF is saved. That is not the same as an official “we do not support this” statement, but it is enough that I would not choose it for accessibility-preserving remediation. citeturn985471view2turn985471view3

So for JavaScript, my read is:

- **excellent** for viewing and app-side workflows
- **pretty good** for generating new accessible PDFs if you control the document structure and use PDFKit carefully
- **risky** for preserving accessibility tags during arbitrary PDF edits with general-purpose libraries like pdf-lib citeturn985471view0turn985471view2turn985471view3

## The practical boundary

The uploaded accessibility guidance matters more than the language choice:

- If the PDF is **scanned**, code can help with OCR, but OCR output usually still needs more work. fileciteturn2file0
- If the PDF lacks **tags** or has bad **reading order**, full remediation becomes much more manual and Acrobat-heavy. fileciteturn2file0 fileciteturn2file2
- If it is a **form**, accessible naming, labeling, and tab order are specialized work; the guidance you uploaded is pretty explicit that PDF forms usually require substantial Acrobat work. fileciteturn2file0
- Accessibility checkers help, but they do **not** reliably judge reading order quality or whether alt text is actually useful. fileciteturn2file0 citeturn653071search5

## My actual recommendation

If your goal is **batch analysis, OCR, preflight, and remediation support tooling**, I would lean **Python**.

If your goal is **creating new PDFs inside a web app**, I would lean **JavaScript with PDFKit**.

If your goal is **remediating messy real-world PDFs to accessible production quality**, I would use **code for triage and automation**, but still plan on **Acrobat Pro/manual QA** for the final accessibility work. That is the direction your uploaded sources point to, and I think they’re right. fileciteturn2file0 fileciteturn2file2 fileciteturn1file14

If you want, I can turn this into a **task-by-task matrix** like:

- detect inaccessible PDFs
- OCR scanned PDFs
- generate accessible PDFs from structured data
- preserve tags during edits
- accessible form workflows
- best Python stack
- best JavaScript stack


#### You:
You know how Office documents use OOXML, with their own ML per type of file? What does PDF use?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m checking the exact standards language here, because the answer is a little counterintuitive: PDF does have its own internal syntax and object model, but it is not “the PDF version of XML” in the way WordprocessingML or SpreadsheetML are.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## The distinction

Office files use **OOXML**, which is a **ZIP package of XML parts** like WordprocessingML, SpreadsheetML, and PresentationML.

**PDF does not work that way.** It does **not** have a parallel “PDFML” that serves as the main document format. The core format is just **PDF itself**, standardized as **ISO 32000** (current core spec: **PDF 2.0 / ISO 32000-2**). citeturn927809search0turn927809search1

## What PDF uses instead

PDF is best thought of as an **object-based page description format** with its own syntax, not an XML vocabulary. PDF Association describes it as an **object-based page description language**. A PDF file is made of PDF objects such as dictionaries, arrays, strings, numbers, streams, and indirect objects, plus cross-reference data that lets readers find those objects quickly. citeturn927809search4turn300958search1

The part that actually draws a page is the **content stream**. Adobe’s PDF Reference describes a content stream as a stream object containing a **sequence of instructions** that describe the graphical elements to paint on a page, interpreted sequentially according to PDF syntax rules. citeturn927809search34

So the closest honest mapping is:

- **DOCX/XLSX/PPTX** → ZIP container + XML parts
- **PDF** → native PDF object syntax + streams + operators + xref structure citeturn300958search1turn927809search34

## The closest things to “markup” inside PDF

There are a few things that look *somewhat* like separate sublanguages, but none of them are the main equivalent of OOXML:

- **Content stream operators**\
  These are the drawing/text operators inside page content streams. This is probably the closest thing to “PDF’s native page markup,” but it is not XML. citeturn927809search34

- **Tagged PDF structure**\
  For accessibility and logical structure, PDF can include a **structure tree** with tags and relationships. Adobe describes a logical tagged structure tree as the mechanism that provides meaningful reading order and defines structural elements and relationships. citeturn0file2

- **XMP metadata**\
  PDF often embeds **XMP**, which *is* XML-based metadata. But that is metadata inside the PDF, not the PDF document format itself. PDF Association notes that PDF supports an extensible metadata model, and embedded metadata in PDF is commonly XMP. citeturn927809search0turn927809search4

- **FDF / XFDF for forms data**\
  These are sidecar/interchange formats for PDF form data. **XFDF** is XML-based, but again, it is not the core PDF file format. citeturn927809search0

## So the direct answer

The PDF equivalent is **not an ML dialect like WordprocessingML**.

The real answer is:

**PDF uses the PDF file format itself** — an **ISO-standardized object-and-stream syntax** with **content streams** for page instructions, optional **tagged structure** for semantics/accessibility, and optional **XMP XML** for metadata. citeturn927809search0turn927809search1turn927809search34

## If you’re thinking like a developer

A useful mental model is:

- **OOXML** = “document as XML package”
- **PDF** = “document as serialized object graph plus drawing instruction streams”

That difference is why low-level PDF work feels closer to parsing a graphics/page-description format than walking an XML DOM. citeturn300958search1turn927809search34

If you want, I can do the next layer and show you the rough internal anatomy of a PDF file — header, indirect objects, streams, xref table/stream, trailer, page tree, and content stream operators — side by side with the OOXML mental model.


#### You:
Where do I find the guide for the object based page description format, language?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m pulling the primary specs and the most usable guides. There’s a difference between the official standard and the human-readable introductions, and you probably want both.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes. The **official guide** is the **PDF specification itself**: **ISO 32000-2:2020 (PDF 2.0)**. The PDF Association hosts it **at no cost**, and its page explicitly says this is the latest and most up-to-date core PDF specification for developers who create, read, or process PDF files. citeturn457451view0

For actual learning, I would not start with the full ISO spec cold unless you enjoy being hit with a brick made of standards prose. A better sequence is:

- **Start here for orientation:** the **PDF Association cheat sheets**. They are meant to help developers remember key PDF terms and concepts, but they explicitly say they are **not** a substitute for the core specification. citeturn938843search1
- **Then read this for the classic developer-facing explanation:** **Adobe PDF Reference 1.7** in the Acrobat SDK docs. Adobe still lists the PDF Reference documents in its developer docs, and the 1.7 reference is the old, widely used guide people still point to for understanding PDF internals. citeturn938843search8turn938843search31
- **Then use the real standard:** **ISO 32000-2** for the authoritative version of how PDF is defined now. The PDF Association page also notes that PDF 2.0 includes corrections and clarifications that help even when supporting earlier PDF versions. citeturn457451view0

If you want the shortest “where exactly do I go?” answer:

1. **PDF Association → ISO 32000-2** for the official spec. citeturn457451view0
2. **PDF Association → PDF Cheat Sheets** for a humane on-ramp. citeturn938843search1
3. **Adobe Acrobat SDK docs → PDF Reference 1.7** for the classic explanatory reference. citeturn938843search8turn938843search31

One more useful thing: the PDF Association page for ISO 32000-2 also points to **normative references** and a **technical index**, which is where you go once you start needing the surrounding standards and related documents. citeturn457451view0

If you want, I can map the PDF spec to the OOXML mental model next — like **Catalog ≈ package root**, **Page tree**, **indirect objects**, **streams**, **xref**, and **content operators** — so it becomes less alien.


#### You:
What javascript can extract and/or write at that level?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m checking which JavaScript tools actually operate at the **object/content-stream level**, as opposed to normal app-level “merge, fill, render” libraries. That distinction matters a lot here because the ecosystem gets much thinner at the truly low level.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## Yes, but the list gets much shorter

At the **object/content-stream level**, JavaScript has some real options, but not many. The strongest split is:

- **Read / inspect at low level**: **PDF.js**
- **Write / manipulate object graph in pure JS**: **pdf-lib**
- **Lower-level Node-side create/parse/manipulate with native bindings**: **MuhammaraJS**
- **Generate new PDFs with fairly low-level control**: **PDFKit** citeturn175901search3turn842924search1turn305842search3turn842924search3

## 1. PDF.js — best low-level reader/inspector in JavaScript

If your goal is **extracting what the PDF is doing**, **PDF.js** is the main open-source JavaScript choice. Its API exposes:

- `getOperatorList()` for the page’s **operator list**
- `getTextContent()` for extracted text plus positioning/style info
- `getStructTree()` for page structure tree access
- `getMarkInfo()` for document MarkInfo
- `getData()` for raw PDF bytes
- `saveDocument()` for saved document bytes in the PDF.js editing flow citeturn175901search4

That makes PDF.js the closest thing in JS to a **parser/viewer with access to page-level internals**. But its core identity is still a **reader/rendering platform**, not a general-purpose low-level writer. Mozilla describes it as a “general-purpose, web standards-based platform for parsing and rendering PDFs.” citeturn114434search1turn175901search1

### Good for

- parsing
- rendering
- inspecting text/layout/operators
- reading structure tree / marked content

### Not the best fit for

- arbitrary low-level PDF rewriting as your main write engine

## 2. pdf-lib — best pure-JS write/manipulate option

For **writing** at something closer to the object-model layer, **pdf-lib** is the most important pure-JS option. Its public API exposes a document `catalog` and a low-level `context`, which is a strong hint that you can work below the friendly page/text/form layer when needed. citeturn842924search4

This is the one I would reach for if you want:

- pure JS
- browser + Node + Deno portability
- object-level document manipulation
- creating/modifying PDFs without native dependencies citeturn114434search0turn842924search3

### Good for

- creating and modifying PDFs
- low-level-ish object access through `context`
- cross-runtime use

### Limits

It is not primarily documented as a **content-stream surgery toolkit** in the way a hardcore C/C++ PDF library would be. You can get lower than the friendly API, but that path is less ergonomic and less “officially tutorialized” than the mainstream use cases. That last sentence is an inference from the docs and API surface, not a vendor statement. citeturn842924search4turn114434search0

## 3. MuhammaraJS — closest to old-school low-level Node PDF hacking

If you are in **Node** and you want something more explicitly about **creating, parsing, and manipulating PDF files and streams**, **MuhammaraJS** is the most on-point answer I found. Its npm page describes it that way directly, and it is explicitly the maintained replacement for **HummusJS**. citeturn305842search3turn877228view0

HummusJS itself says support ended in 2019 and recommends moving to MuhammaraJS. citeturn877228view0

### Good for

- Node-only lower-level PDF work
- parsing/manipulating streams
- people who want something closer to “real PDF internals” than a browser library

### Limits

- native dependency stack, so less pleasant than pure JS
- not browser-first
- ecosystem/docs feel older than PDF.js/pdf-lib even if the replacement is still published citeturn305842search3turn877228view0

## 4. PDFKit — low-level generation, not low-level parsing

**PDFKit** is more of a **writer/generator** than a parser, but it does matter here because its docs explicitly say it includes **low level functions** as well as higher-level abstractions. It also has unusually serious documentation for **Tagged PDF / PDF/UA** generation, including marked content, logical structure, and document options like `tagged: true` and `subset: 'PDF/UA'`. citeturn842924search1turn842924search0

### Good for

- generating PDFs from scratch
- adding structure intentionally during generation
- accessible PDF generation in JS

### Not for

- deep extraction/parsing of arbitrary existing PDFs

## My blunt recommendation by job

### If you want to **extract/analyze page internals**

Use **PDF.js**. It is the strongest JS answer for reading operator lists, text content, structure trees, and similar internals. citeturn175901search4turn114434search1

### If you want to **write/manipulate at object level in pure JS**

Use **pdf-lib**. It is the cleanest mainstream choice with real low-level access points. citeturn842924search4turn114434search0

### If you want **Node-side lower-level PDF manipulation with streams/files**

Use **MuhammaraJS**. citeturn305842search3turn877228view0

### If you want to **generate structured PDFs from scratch**

Use **PDFKit**. citeturn842924search1turn842924search0

## The honest bottom line

If by “that level” you mean **the PDF object graph, page operators, marked content, structure tree, xref-ish internals**, JavaScript can do some of it, but the ecosystem is uneven:

- **PDF.js** is the best reader/inspector.
- **pdf-lib** is the best pure-JS writer/manipulator.
- **MuhammaraJS** is the more “PDF plumbing” Node option.
- **PDFKit** is the best generation-first writer with meaningful structure support. citeturn175901search4turn842924search4turn305842search3turn842924search0

If you want, I can do the next layer as a **capability matrix** with rows like:

- read raw objects
- inspect content stream operators
- extract text positions
- inspect structure tree/tags
- create new indirect objects
- rewrite existing streams
- preserve accessibility structure
- browser vs Node only


#### You:
Think about all the pieces of a pdf for accessibility 

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## A useful way to think about PDF accessibility

An accessible PDF is **not one thing**. It is several layers that all have to line up well enough that a screen reader, keyboard user, low-vision user, mobile user, and sighted mouse user can all get the same document in usable form.

The cleanest mental model is:

1. **Source document accessibility**
2. **Real text layer**
3. **Page content and visual layout**
4. **Semantic structure and tags**
5. **Reading order**
6. **Non-text alternatives**
7. **Tables, lists, headings, and links**
8. **Forms and interactive controls**
9. **Navigation aids**
10. **Document metadata and language**
11. **Security/settings that do not break assistive tech**
12. **Manual QA beyond automated checks**

That is basically the whole game. The sources you uploaded are pretty aligned on this: start with an accessible source file, preserve accessibility on export, make sure the PDF has real text and tags, then check reading order, alt text, metadata, and forms. fileciteturn0file0 fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

---

## 1. Source document accessibility

PDF is usually a **destination format**, not the best place to create accessibility from scratch. If the Word, PowerPoint, InDesign, or other source file is inaccessible, the PDF will usually inherit that damage, and fixing it later in Acrobat is much harder. The guidance you uploaded is explicit about this. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

This means the real first accessibility layer is:

- proper heading structure in the source
- real lists, not fake bullets
- real tables, not spaced text
- alt text in the source
- good color contrast
- descriptive links
- language and title
- sane reading order in the source layout

---

## 2. Real text layer

If the PDF is just an **image of text**, it is inaccessible until OCR creates searchable/selectable text. Multiple uploaded sources say this directly. A scanned image is not enough because assistive tech cannot reliably read or extract the words from the image itself. fileciteturn0file2 fileciteturn0file3

So one core piece is:

- **Does the PDF contain real machine-readable text?**

That breaks down into:

- selectable/searchable text exists
- OCR accuracy is good enough
- characters map correctly to Unicode
- fonts are extractable to text, not just visually renderable

Adobe’s overview explicitly calls out searchable text and fonts that allow correct character extraction as accessibility characteristics. fileciteturn0file2

---

## 3. Page content and visual layout

This is the part people usually notice first because it is what appears on screen. WebAIM frames a PDF as having a **visual layer**, a **content layer**, and a **tags layer**. That is a very useful model. fileciteturn0file4

The visual/page layer includes:

- text placement
- columns
- images
- lines and shapes
- headers/footers
- page breaks
- visual emphasis
- color and contrast

This layer matters because:

- low-vision users may zoom or reflow
- the visual order can differ from the semantic order
- what looks obvious visually may be meaningless to a screen reader unless tagged properly

---

## 4. Semantic structure and tags

This is one of the biggest pieces.

A PDF needs a **tag tree / structure tree** so assistive technology can tell what something *is*:

- heading
- paragraph
- list
- list item
- table
- row
- cell
- figure
- link
- form field
- artifact/decorative item

Without tags, a PDF may still look perfect and still be functionally broken for nonvisual use. Harvard and Colorado both treat “no tags” as a major failure point, and Adobe describes tagged structure as what defines reading order and structural relationships. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

This is where PDF starts to behave less like a picture and more like a document.

---

## 5. Reading order

A PDF can have all the right text and still be awful because the order is wrong.

Reading order is the sequence assistive tech follows through the tagged content. Harvard explicitly says to inspect the order of tags in the Tags panel and verify that it matches the order the document should be read. Colorado also points out that automated tools do not reliably judge reading order quality. fileciteturn0file1 fileciteturn0file3

This piece includes:

- correct order across columns
- figures appearing in sensible places
- sidebars inserted where they belong
- repeated headers/footers treated appropriately
- decorative items not interrupting content
- form fields in logical sequence

A visually pretty two-column PDF is one of the classic ways to destroy reading order.

---

## 6. Headings, lists, paragraphs, and document outline

A document needs recognizable structure, not just styled text.

That means:

- one logical heading hierarchy
- headings in proper nesting order
- real list tags for lists
- real paragraph tags for paragraphs
- no fake structure made only with font size or bold text

Harvard’s examples call out expected tags like `<H1>` through `<H6>`, `<L>`, `<LI>`, `<LBody>`, and `<P>`. fileciteturn0file1

This matters because structure is how users:

- skim
- navigate
- understand section relationships
- jump around efficiently

---

## 7. Tables

Tables are one of the most fragile parts of PDF accessibility.

An accessible table needs more than grid lines. It needs structure that communicates:

- this is a table
- these are rows and columns
- these are headers
- these data cells belong under these headers

If a table is visually present but semantically flattened into paragraphs or loose text objects, the information becomes much harder to interpret with assistive tech.

Even when your uploaded pages do not go deeply into table repair syntax, they repeatedly emphasize that data tables are part of the structural elements that should be defined in the source and preserved in the PDF. fileciteturn0file2

---

## 8. Images, figures, charts, and other non-text content

Non-text content needs a usable text alternative.

That means:

- meaningful images get alt text
- decorative images are marked decorative/artifacted appropriately
- charts/diagrams get enough description to preserve the informational value
- purely visual meaning is not left unexplained

Harvard says images should be tagged as `<Figure>` and given useful alt text or marked decorative where appropriate. Adobe likewise identifies alternative text descriptions for non-text elements as a core accessibility characteristic. fileciteturn0file1 fileciteturn0file2

This is not just “put words in a field.” The text has to convey what matters.

---

## 9. Links and navigation targets

Links are their own accessibility piece.

A usable PDF should have:

- real link objects/tags
- descriptive link text
- keyboard reachability
- sensible destinations
- no raw “click here” nonsense when context is missing

Harvard explicitly calls out link tags and descriptive link text. Adobe also includes hyperlinks and navigational aids as part of accessibility. fileciteturn0file1 fileciteturn0file2

---

## 10. Bookmarks and document navigation

For longer PDFs, navigation aids matter a lot:

- bookmarks
- table of contents
- heading-based structure
- internal links
- logical page progression

Adobe explicitly includes bookmarks, headings, links, and other navigational aids as accessibility-supporting features. fileciteturn0file2

These are not cosmetic extras. They help users avoid reading a long document linearly just to find one section.

---

## 11. Language, title, and metadata

There is a metadata layer that users do not always see directly but assistive tech needs.

Important pieces include:

- document title
- document language
- author/metadata where relevant
- “show document title” rather than only filename in title bar

Harvard explicitly instructs authors to set title, author, display the document title, and set the language. Adobe explains that document language helps screen readers pronounce content correctly and that title helps users identify the document. fileciteturn0file1 fileciteturn0file2

---

## 12. Color, contrast, and sensory dependence

PDF accessibility is not just about screen readers.

The document also needs:

- sufficient contrast
- no meaning conveyed by color alone
- no instructions that depend only on shape, color, or visual location
- readable text when zoomed/reflowed

Harvard calls out contrast checks, and Adobe includes sufficient contrast and avoiding reliance on color or sensory characteristics alone. fileciteturn0file1 fileciteturn0file2

---

## 13. Reflow and zoom behavior

This is an underappreciated piece.

WebAIM points out that PDFs have a content layer that can be presented in **Reflow** view, which can make enlarged or small-screen reading more usable. Adobe also notes that structure supports reflow and better viewing on mobile or at larger sizes. fileciteturn0file4 fileciteturn0file2

So accessibility is partly about whether the PDF remains usable when:

- zoomed heavily
- reflowed into a single column
- read on a phone or tablet
- stripped of its original visual layout cues

---

## 14. Forms and interactive controls

Forms are their own category of pain.

An accessible PDF form needs:

- interactive form fields
- proper labels/names/tooltips
- logical tab order
- meaningful error identification/help
- keyboard operation
- enough instructions to complete the form
- no inaccessible timing constraints unless extra time can be requested

Adobe explicitly lists interactive labeled form fields, accessible error handling, and tab order as core characteristics. Colorado says accessible PDF forms almost always require substantial Acrobat work and specialized training. fileciteturn0file2 fileciteturn0file3

This is one of the strongest arguments for using a web form instead of a PDF form when possible.

---

## 15. Artifacts and decorative content

Not everything on the page should be exposed as meaningful content.

Some items should be treated as decorative/artifacts, such as:

- purely decorative images
- repeating page decorations
- ornamental lines
- background graphics
- redundant visual flourishes

If these are left in the content flow, screen readers may announce useless junk.

Your uploaded pages imply this distinction through figure/decorative handling and through the overall need for a meaningful tag tree, even if they do not dwell on artifacting in detail. fileciteturn0file1 fileciteturn0file2

---

## 16. Security and permissions

Security settings can quietly wreck accessibility.

Adobe and Harvard both note that permissions should not prevent assistive technology from accessing the text. Harvard explicitly mentions the screen-reader text access checkbox under security settings. fileciteturn0file1 fileciteturn0file2

So one piece of the accessibility model is:

- the document can still be consumed by assistive technology even if other permissions are restricted

---

## 17. Automation versus human judgment

This is one of the most important distinctions.

Automated checking can help identify:

- no tags
- missing alt text fields
- missing title/language
- image-only PDFs
- some form issues
- obvious metadata/config problems

But the uploaded guidance is clear that automation does **not** reliably determine:

- whether reading order is actually sensible
- whether alt text is useful
- whether a table makes sense
- whether headings reflect the real structure
- whether the experience is actually usable

Colorado says passing baseline tests does not guarantee accessibility, and Acrobat’s checker does not assess many judgment-heavy issues well. fileciteturn0file3

---

## 18. The format choice itself

One of the most important “pieces” is upstream: **should this even be a PDF?**

Section508.gov, Harvard, and Colorado all lean in the same direction:

- prefer HTML when possible
- prefer web forms over PDF forms when possible
- use PDF when it is actually needed, not by reflex

That is not a side note. It is part of accessibility strategy. fileciteturn0file0 fileciteturn0file1 fileciteturn0file3

---

## The full implementation mental model

If I were compressing all of this into one technical model, I’d say an accessible PDF has to work across **five interacting layers**:

### 1. Source layer

The original document was authored accessibly.

### 2. Text/content layer

The PDF contains real, extractable, correctly encoded text.

### 3. Structure layer

The PDF has a meaningful tag tree with headings, paragraphs, lists, tables, figures, links, forms, and artifacts handled correctly.

### 4. Experience layer

Reading order, keyboard order, navigation, reflow, zoom, contrast, and form usability all hold up.

### 5. Metadata/control layer

Language, title, permissions, and related settings support rather than block accessibility.

If any one of those layers fails badly, the PDF may still *look* fine but be inaccessible.

---

## The shortest honest summary

A PDF is accessible when:

- it has **real text**
- it has **tags/structure**
- the **reading order** is right
- images and non-text content have **usable alternatives**
- headings, lists, tables, links, and forms are **semantically represented**
- title, language, navigation, and permissions are set correctly
- and the result still works under **screen reader, keyboard, zoom, and reflow** use

That is the whole machine.

If you want, I can turn this into a **PDF accessibility anatomy diagram** in plain English, or a **developer-facing checklist** that maps each accessibility piece to the underlying PDF construct.


#### You:
Right. And I’m asking you to think about available Python with all those layers 

#### Plugin (file_search):
Make sure to include fileciteturn0file0 in your response to cite this file, or to surface it as a link.
---
created: 2026-04-20T20:27:52 (UTC -05:00)
tags: []
source: https://www.section508.gov/create/pdfs/
author: Authoring Guides
---

# Create Accessible PDFs | Section508.gov

> ## Excerpt
> Learn how to create accessible Portable Document Format (PDF) documents that meet the Revised 508 Standards. This comprehensive guide includes step-by-step training videos, document authoring tips, downloadable testing guides, and agency-developed resources. Ideal for document authors, accessibility testers, and federal staff.

---
Learn how to create accessible Portable Document Format (PDF) documents that conform to the [Section 508 Standards](https://www.access-board.gov/ict/).

-   PDFs are still used across government, but they are often not the most accessible or mobile-friendly option. [Federal policy](https://bidenwhitehouse.archives.gov/omb/management/ofcio/m-24-08-strengthening-digital-accessibility-and-the-management-of-section-508-of-the-rehabilitation-act/#anchorD) requires agencies to prioritize HTML and use PDFs only when necessary. Choose formats that support accessibility, responsiveness, mobile-friendliness, and a digital-first user experience.
    

## Authoring Guides

-   [PDF Testing and Remediation Guide (DOCX)](https://assets.section508.gov/assets/files/PDF%20Testing%20and%20Remediation%20Guide-Adobe%20Acrobat%20DC%20Pro-AED%20COP.docx)
-   [PDF Testing Checklist (DOCX)](https://assets.section508.gov/assets/files/PDF-Printable-Accessiblility-Checklist.docx)

## Training Videos

___

[![How to Test and Remediate PDFs for Accessibility Using Adobe Acrobat DC](https://www.section508.gov/assets/images/thumbnails/training-video-pdf-series.jpg)](https://www.section508.gov/create/pdfs/training-videos/)

[How to Test and Remediate PDFs for Accessibility Using Adobe Acrobat DC](https://www.section508.gov/create/pdfs/training-videos/)

The Accessible Electronic Document Community of Practice (AED CoP) created this series of videos to explain and demonstrate the minimum steps needed to ensure your PDF is Section 508 conformant.

Duration 63m 51s | 5-part Video Series

___

## Agency-Developed Guidance

The resources in this section were developed by Federal agencies, and shared here for your convenience. Note, much of this guidance predates the [Revised 508 Standards](https://www.access-board.gov/guidelines-and-standards/communications-and-it/about-the-ict-refresh/final-rule/text-of-the-standards-and-guidelines).

-   [Resources for Developers and Document Authors](https://www.ssa.gov/accessibility/developer_resources.html) - Guidance on how to develop and author accessible electronic content
-   [Alternate Text For Images](http://www.ssa.gov/accessibility/files/SSA_Alternative_Text_Guide.pdf) (PDF, July 2011) - Developed by SSA
-   [Making a diagram screen reader friendly](https://blog-nrrd.doi.gov/beyond-auto/) - ONRR.gov

## Related Resources

-   [Create Accessible Digital Products](https://www.section508.gov/create)
-   Review [WebAIM Alternative Text](https://webaim.org/techniques/alttext/) for appropriate use of alternative text.
-   Review [W3C’s Alt Decision Tree](https://www.w3.org/WAI/tutorials/images/decision-tree/) for guidance on how to describe images.
-   [Adobe Acrobat accessibility support](https://helpx.adobe.com/acrobat/using/create-verify-pdf-accessibility.html)
-   [Web Accessibility Tutorials and Presentations](https://www.w3.org/WAI/train) - Guidance from the World Wide Web Consortium (W3C)

**Reviewed/Updated:** August 2025


#### Plugin (file_search):
Make sure to include fileciteturn0file1 in your response to cite this file, or to surface it as a link.
---
created: 2026-04-20T20:27:23 (UTC -05:00)
tags: []
source: https://accessibility.huit.harvard.edu/pdf
author: 
---

# Creating Accessible PDFs | Digital Accessibility Services

> ## Excerpt
> PDFs are a versatile and convenient way to share information. But PDFs are often not structured properly, which can create barriers for people who need to read and understand the information.Fortunate

---
PDFs are a versatile and convenient way to share information. But PDFs are often not structured properly, which can create barriers for people who need to read and understand the information.

Fortunately, there are accessibility best practices that can help make PDFs more accessible for everyone.

If you need an accessible doc fast, consider using [Harvard's preferred document remediation vendor, AbleDocs](https://accessibility.huit.harvard.edu/pdf-vendors).

**In this page:**

-   [Check if your PDF has tags](https://accessibility.huit.harvard.edu/pdf#check)
-   [Review Reading Order and Tags](https://accessibility.huit.harvard.edu/pdf#review)
-   [Ensure Image Accessibility](https://accessibility.huit.harvard.edu/pdf#images)
-   [Set File Properties](https://accessibility.huit.harvard.edu/pdf#properties)

___

## PDF Accessibility Best Practices

## PDF Accessibility Best Practices

-   **Start with an accessible source document:** Whether you start in Word, Google Docs, PowerPoint, or InDesign, we recommend making your source document as accessible as possible before converting to PDF. Review our [Creating Accessible Documents guidance](https://accessibility.huit.harvard.edu/accessible-documents) to ensure you're following best practices for your document type.
-   **Keep accessibility settings when you convert the document:** When converting to PDF, use settings that retain tags and accessibility formatting. Avoid "Print to PDF" settings as they will remove your tags and accessibility formatting.
-   **Does it really need to be a PDF?** Consider if a PDF is really the best way to share the information. Would a different format be easier to make accessible and work better for the content? Before you create a PDF, here are a few considerations:
    -   If your PDF is a form: consider using a Google or Qualtrics form instead. This allows for streamlined data collection, autofill access, and better version control. A web form is also easier to create and much more accessible than a PDF.
    -   If your PDF is informational: consider sharing the content on a web page. It’s much easier to maintain and update web pages, and HTML is generally more accessible than PDFs. Your audience is also more likely to read a web page than to download and read a PDF, especially on mobile.

## Check if your PDF has tags

### Open the Tags Panel

Tags provide structure for content in your document.

![tags button.](https://accessibility.huit.harvard.edu/sites/g/files/omnuum12446/files/online-accessibility-huit/files/pdf_-_tags-button.png)

 To see if your PDF has tags, open the Tags Panel. Navigate to View > Show/Hide > Navigation Panes > Tags.

### Fix “No Tags Available”

If you don't see any tags, you may have to add them!

![Autotag document button.](https://accessibility.huit.harvard.edu/sites/g/files/omnuum12446/files/online-accessibility-huit/files/pdf-autotag-document.png)

In the Accessibility panel select "Autotag Document." The tags will not be perfect, but they will be a good start!

## What Tags you might see

### Heading Tags

Headings provide structure and organization to your document. Generally, there should only be one Heading 1 (<H1>) for your document. Headings should be used in ascending numerical order. Don’t skip heading levels!

![heading tag.](https://accessibility.huit.harvard.edu/sites/g/files/omnuum12446/files/online-accessibility-huit/files/pdf-_tags_-_h1.png)

Tags: <H1>, <H2>, <H3>, <H4>, <H5>, <H6>

### List Tags

Lists help organize content and should be tagged with List <L> for the entire lit, List Item <LI> for each item in the list, and List Body <LBody> for the content of each list item.

![Tag tree with <l>, </l></p><li>, <lbody> tags.](https://accessibility.huit.harvard.edu/sites/g/files/omnuum12446/files/online-accessibility-huit/files/pdf-tags-list.png)

Tags: <L>, <LI>, <LBody>

### Paragraph Tags

Most text in your document will be tagged with a <P> tag. This indicates regular paragraph text.

![Paragraph tag.](https://accessibility.huit.harvard.edu/sites/g/files/omnuum12446/files/online-accessibility-huit/files/pdf-tags-paragraph.png)

Tags: <P>

### Link Tags

All links should have [descriptive link text](https://accessibility.huit.harvard.edu/write-helpful-links) and be tagged.

![Tag tree showing <link>, link-objr, and google.com.](https://accessibility.huit.harvard.edu/sites/g/files/omnuum12446/files/online-accessibility-huit/files/screen_shot_2022-11-14_at_11.37.30_am.png)

Tags: <Link> and Link-OBJR

## Review the Reading Order and Tags

### Reading Order

The order of the tags displayed in the Tags Panel is called the Reading Order.

Use your up and down arrow keys to navigate through the tags. As you do, content in your PDF will be highlighted. 

Make sure the order of the tags matches the order of content as you would read it visually.

![Tags panel showing h tags, p tags, and l tags.](https://accessibility.huit.harvard.edu/sites/g/files/omnuum12446/files/online-accessibility-huit/files/pdf_-_tags.png)

### How to move a tag in the reading order

If you need to move a tag you can right click on the tag and select “Cut” from the menu (or CMD/CTRL + X). After you cut the tag you can paste it where you like in the tag tree by right clicking the tag just before the correct location and select “Paste” (or CMD/CTRL + V). The cut tag will be placed next to the tag you highlighted.

### How to modify an existing tag

-   Right click on the tag you want to change
-   Go down to Properties
-   Object Properties box will pop up
-   “In the Tag tab, select the tag from the options in the ‘Type’ menu/list.

## Ensure image accessibility

![Set alternate text box for image 1 of 3.](https://accessibility.huit.harvard.edu/sites/g/files/omnuum12446/files/online-accessibility-huit/files/pdf-set-alt-text-2.png)

Image Tags: Images should be tagged as <figure> and they should have [useful alt text](https://accessibility.huit.harvard.edu/describe-content-images "Write helpful Alt Text to describe images").

Adding Alt Text: In Accessibility Panel, select “Set Alternate Text.” A pop up will guide you through your images in the document. You can add alt or edit alt text, or select “Decorative” for unimportant images.

Tags: <Figure>

## Check Color Contrast

 ![color contrast icon.](https://accessibility.huit.harvard.edu/sites/g/files/omnuum12446/files/styles/hwp_1_1__100x100_scale/public/online-accessibility-huit/files/icon_contrast_png_01.png?itok=g3isd9Vb)

Text and other elements in your PDF should have [sufficient color contrast](https://accessibility.huit.harvard.edu/use-sufficient-color-contrast) against the background. Color Contrast should be 4.5:1 or greater for standard size text. If you are using Adobe's Accessibility Checker you will always be prompted to check the color contrast. If you're not sure about the contrast, use a tool (such as the [Color Contrast Analyser](https://www.tpgi.com/color-contrast-checker/)) to check.

If you find contrast errors at this stage it is always better to go back to the source document to correct the contrast when possible. This is why it is so important to start with an accessible source document.

## Set File Properties

### Add or Verify Metadata

-   Add Title and Author (File > Properties>Description Tab)
-   Set Doc Title to Display (Properties> Initial View tab >Window Options > Show > Document Title)
-   Add Language (Properties>Advanced Tab > Reading Options >Language)

### Be Mindful of Security Settings

If using, check the “Enable text access to screen reader devices for the visually impaired” check box in the “Permissions” section of the security settings.

This applies to security settings that restrict permissions to the document (i.e. copy and paste) not just adding a password.

## Resources

-   [Tagged PDF Best Practices (PDF Association)](https://www.pdfa.org/wp-content/uploads/2019/06/TaggedPDFBestPracticeGuideSyntax.pdf)
-   [Video: Testing a PDF for Accessibility (Section 508.gov)](https://www.section508.gov/training/pdfs/aed-cop-pdf02/)

## Upcoming Documents Trainings

### Advanced PDF Accessibility

May 1, 2026

12:00PM - 1:00PM EDT

Virtual

### Creating Accessible Slides

May 6, 2026

1:00PM - 2:30PM EDT

Virtual

### Creating Accessible Documents

May 13, 2026

1:00PM - 2:30PM EDT

Virtual

## DAS Office Hours

Want to check your content accessibility with Digital Accessibility Services (DAS)? Stop by one of our upcoming virtual Office Hours!

### DAS Office Hours

Apr 24, 2026

10:00AM - 11:00AM EDT

Virtual

### DAS Office Hours

May 1, 2026

10:00AM - 11:00AM EDT

Virtual

### DAS Office Hours

May 8, 2026

10:00AM - 11:00AM EDT

Virtual


#### Plugin (file_search):
Make sure to include fileciteturn0file2 in your response to cite this file, or to surface it as a link.
---
created: 2026-04-20T20:27:57 (UTC -05:00)
tags: []
source: https://www.adobe.com/accessibility/pdf/pdf-accessibility-overview.html
author: 
---

# PDF Accessibility Overview

> ## Excerpt
> PDF Accessibility ReviewPDF file format accessibility features combined with Adobe® Acrobat® and Adobe Reader® allow universal access to documentsA document or application is considered accessible if 

---
## PDF Accessibility Review

## PDF file format accessibility features combined with Adobe® Acrobat® and Adobe Reader® allow universal access to documents

A document or application is considered accessible if meets certain technical criteria and can be used by people with disabilities. This includes access by people who are mobility impaired, blind, low vision, deaf, hard of hearing, or who have cognitive impairments. Accessibility features in Adobe Acrobat, Adobe Reader and in the Portable Document Format (PDF) make it easier for people with disabilities to use PDF documents and forms, with and without the aid of assistive technology software and devices such as screen readers, screen magnifiers, text-to-speech software, speech recognition software, alternative input devices, Braille embossers, and refreshable Braille displays.

The [Web Content Accessibility Guidelines](http://www.w3.org/TR/WCAG20/) (WCAG) 2.0 ([ISO/IEC 40500:2012](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=58625)) and the [PDF/UA (ISO 14289-1)](http://www.iso.org/iso/catalogue_detail.htm?csnumber=54564) standard cover a wide range of recommendations for making content more accessible to people with disabilities. One benefit of following these guidelines is that content becomes more usable for all users. For example, the underlying document structure that makes it possible for a screen reader to properly read a PDF out loud also makes it possible for a mobile device to correctly reflow and display the document on a small screen. Similarly, the preset tab order of an accessible PDF form helps all users—not just users who rely on the keyboard—complete the form more easily.

## Overview of Portable Document Format (PDF)

The PDF format is the native file format of the Adobe Acrobat family of products. The goal of this format and these products is to enable users to exchange and view electronic documents easily and reliably, independently of the environment in which they were created. PDF relies on the same imaging model as the PostScript® page description language to describe text and graphics in a device-independent and resolution-independent manner. To improve performance for interactive viewing, PDF defines a more structured format than that used by most PostScript language programs. PDF also includes objects, such as annotations and hypertext links, that are not part of the page itself but that are useful for interactive viewing and document interchange.

A logical tagged structure tree is used within each document to provide a meaningful reading order for content, as well as a method for defining structural elements role and relationship to page content. Within this tag structure, other properties such as alternative text and replacement text can be provided.

## Determine the Accessibility Path for each PDF Document

PDF files are created in a variety of ways, from a variety of applications, and for a variety of purposes. Achieving the desired accessibility goals for an individual PDF file requires understanding the nature of the PDF and its intended use. Adobe Acrobat Pro provides several tools including the Make Accessible Menu in the Action Wizard mode and the Accessibility Checker to assist authors in evaluating and fixing issues that can impact accessibility.

The Adobe Acrobat Pro Accessibility Guide: PDF Accessibility Repair Workflow document provides details on how to assess existing PDF files for accessibility. By following these procedures in the recommended order, authors can efficiently proceed through the analysis of a PDF file in a systematic fashion. Systematically ruling out or confirming certain characteristics found in a PDF file will guide the author to the most appropriate path for making an individual PDF document accessible.

## Start with an Accessible Document

The PDF format is a destination file format. PDF files are typically created in some other application. Optimally document accessibility should begin in the native document format. For example, many documents are created in a word processing or desktop publishing application, and then exported as PDF documents. There many things that can be done in native document applications to support accessibility, such as adding alternative text for images; defining structural headings, lists, and data tables; providing document language; and setting document properties such as titles. Adobe desktop publishing applications such as [Adobe InDesign](https://www.adobe.com/products/indesign.html) and [Framemaker](https://www.adobe.com/products/framemaker.html) support these features, as well as other word processing applications such as Microsoft Word. For information on building accessibility into documents created with Adobe products visit the [Adobe Accessibility website](https://www.adobe.com/accessibility.html). To gain assistance on adding accessibility into Microsoft Word documents prior to conversion to PDF format please visit the [Microsoft Enable website](http://www.microsoft.com/enable/). Making the native document accessible allows for less work when changes are made to the native document and the PDF document is regenerated.

If the native document is not available, in most cases, the document can still be made fully accessible. Without accessibility in the native format there will likely be more manual work required in the PDF to properly tag the document. There are some items such as choosing sufficient contrast between foreground and background colors that must be implemented in the native document.

## Characteristics of Accessible PDF files

Accessible PDFs include but are not limited to the following characteristics:

**Searchable text**

A document that consists of scanned images of text is inherently inaccessible because the content of the document is a graphic representing the letters on the page, not searchable text. Assistive technology software cannot read or extract the words in a graphical representation. Furthermore, users cannot select or edit the text or manipulate the PDF for accessibility. Scanned images of text must be converted into to searchable text using optical character recognition (OCR) before addressing accessibility in the document.

**Fonts that allow Characters to be Extracted to Text**

The fonts in an accessible PDF must contain enough information for Acrobat to correctly extract all of the characters to text for purposes other than displaying text on the screen. Acrobat extracts characters to Unicode text when you read a PDF with a screen reader or the Read Out Loud tool, or when you save as text for a Braille embosser. This extraction fails if Acrobat cannot determine how to map the font to Unicode characters.

**Interactive Labeled Form Fields with Accessible Error Messages and No Timing**

Some PDFs contain interactive forms that people fill out using a computer. To be accessible, form fields must be interactive; that is, a user must be able to enter values into the form fields. Interactive PDF forms also have a defined tab order which allows users of assistive technology to use the Tab key in order to progress from one form field or interactive control to the next in a logical manner. Refer to the document Adobe® Acrobat® Pro Accessibility Guide: Creating Accessible Forms for complete details. Forms must provide identification, give tips on proper completion, and prevent errors. Form entry should not be timed unless the user can request more time.

**Other Interactive Features: Hyperlinks and Navigational Aids**

Navigational aids in a PDF — such as links, bookmarks, headings, a table of contents, and a preset tab order for form fields — assist all users in using the document without having to read through the entire document, word by word. Bookmarks are especially useful and can be created from document headings. These features can be accessed using the keyboard without relying on the mouse, and allow for multiple way for users to navigation content.

**Document Language and Title Indication**

Specifying the document language in a PDF enables some screen readers to switch the current speech synthesizer to the appropriate language, allowing correct pronunciation of content in different languages. Providing a document title allows the user to locate and identify the document.

**Security that will not Interfere with Assistive Technology**

Some authors of PDFs restrict users from printing, copying, extracting, editing or adding comments to text. The text of an accessible PDF must be available to a screen reader. Acrobat’s security settings can be set to protect document content while not interfering with a screen reader’s ability to convert the on-screen text to speech or Braille.

**Document Structure Tags and Proper Reading Order**

To read a document’s text and present it in a way that makes sense to the user, a screen reader or other text-to-speech tool requires that the document be structured. Document structure tags in a PDF define the reading order and identify headings, paragraphs, sections, tables and other page elements. The tags structure also allows for documents to be resized and reflowed for viewing at larger sizes and on mobile devices.

**Alternative Text Descriptions for Non-Text Elements**

Document features such as images and interactive form fields cannot be understood by the user of a screen reader unless they have associated alternative text. Though link text is available to screen reader users, it is possible to provide more meaningful descriptions via replacement (actual) text. Alternative text for images and tooltips can aid many users, including those with learning disabilities. Equivalents for multimedia, including any audio and video elements, must also be present.

## Other Accessible Document Characteristics

There are additional characteristics of accessible documents including:

## Start with an Accessible Document

-   No reliance on color or sensory characteristics alone to convey meaning
-   Use of color combinations that provides a sufficient degree of contrast
-   Controls for audio
-   Use of text instead of images of text
-   No use of flashing or blinking elements
-   No focus changes without user initiation
-   Consistent navigation and identification of elements

## Adobe Acrobat and Adobe Acrobat Reader Accessibility Features

Accessibility features in Adobe Acrobat and Adobe Acrobat Reader fall into two broad categories: features that make the reading of PDF documents more accessible, and features that help create accessible PDF documents. To create accessible PDF documents, you must use Acrobat Pro.

**Features to Support the Reading of PDFs by People with Disabilities**

All versions of Adobe Acrobat, Adobe Acrobat Reader, Acrobat Standard and Acrobat Pro provide support for the accessible reading of PDF files by persons with disabilities:

-   Preferences and commands to optimize output for assistive technology software and devices, such as saving as accessible text for a Braille printer
-   Preferences and commands to make navigation of PDFs more accessible, such as automatic scrolling and opening PDFs to the last page read
-   An Accessibility Setup Assistant Wizard for easy setting of most preferences related to accessibility
-   Keyboard alternatives to mouse actions
-   Reflow capability to temporarily present the text of a PDF in a single, easy-to-read column
-   Read Out Loud text-to-speech conversion
-   Support for screen readers and screen magnifiers
-   Support for high contrast and alternative foreground and background colors

**Features to Support the Creation of Accessible PDFs**

-   Creation of tagged PDFs from authoring applications
-   Conversion of untagged PDFs to tagged PDFs from within Acrobat
-   Security settings that allow screen readers to access text while preventing users from copying, printing, editing and extracting text
-   Ability to add text to scanned pages to improve accessibility
-   Tools for editing reading order and document structure
-   Tools for creating accessible PDF forms
-   Ability to set document properties including title and expose them through the title bar of the application

Though Acrobat Standard provides some functionality for making existing PDFs accessible, Acrobat Pro must be used to perform most tasks — such as editing reading order or editing document structure tags — that are necessary to make PDF documents and forms accessible (For more information see Comparison of Accessibility Features in Adobe Acrobat Plans).

## The Acrobat Pro Accessibility Guide Series

Adobe has created a series of accessibility guides for Adobe Acrobat Pro to assist content authors in creating accessible PDF documents. There are four guides in this series:

**PDF Accessibility Overview (this document)**

The Adobe Acrobat Pro Accessibility Guide: PDF Accessibility Overview details what is meant by accessibility in the PDF file format. It distinguishes between the accessibility features of the file format, of Adobe Acrobat and of the Adobe Acrobat Reader application, and how the features of the software and the file format interact to achieve accessibility for people with disabilities.

**Acrobat Pro PDF Accessibility Repair Workflow**

The Adobe Acrobat Pro Accessibility Guide: PDF Accessibility Repair Workflow provides a step-by-step method for analyzing existing PDF files and making them accessible based upon that analysis. This workflow coincides with the workflow provided in the Make Accessible Action wizard and potential issues tested for in the Accessibility Checker tool.

**Using the Accessibility Checker in Acrobat Pro**

The Adobe Acrobat Pro Accessibility Guide: Using the Accessibility Checker describes the PDF accessibility checkers that are included in Adobe Acrobat Pro. Even if you generate an accessible PDF file from an authoring application such a word processor or desktop publishing program, you should then follow the steps in this guide in order to identify any items that may have been missed in the initial conversion, or to add PDF accessibility features that were not provided by the authoring tool.

**Creating Accessible PDF Forms with Acrobat Pro**

The guide entitled Adobe Acrobat Pro Accessibility Guide: Creating Accessible Forms describes how to use the forms tools within Adobe Acrobat Pro to add descriptions to form fields, tag untagged forms, set the tab order, manipulate tags and perform other PDF accessibility tasks. These techniques do not apply to PDF forms from Adobe LiveCycle Designer, as a separate process is provided for making LiveCycle forms accessible.


#### Plugin (file_search):
Make sure to include fileciteturn0file3 in your response to cite this file, or to surface it as a link.
---
created: 2026-04-20T20:28:35 (UTC -05:00)
tags: []
source: https://www.colorado.edu/digital-accessibility/pdfs
author: 
---

# Understanding PDF Accessibility | Digital Accessibility Office | University of Colorado Boulder

> ## Excerpt
> This page will teach you how to do some basic assessment of PDFs for accessibility, help you understand the process of creating an accessible PDF, and point you to additional resources that can help y

---
This page will teach you how to do some basic assessment of PDFs for accessibility, help you understand the process of creating an accessible PDF, and point you to additional resources that can help you learn more or experts who can help.

## PDFs and Accessibility

Making accessible PDFs or fixing accessibility problems in existing PDF files can be a complex and highly variable process. 

PDFs are typically created from a source document such as a Microsoft Word, Adobe InDesign, or Microsoft PowerPoint file, and then are exported into the PDF format. Alternatively, many PDF files are simply images of text that are created by scanning hard copy documents. Unfortunately, [image-based PDFs](https://www.colorado.edu/digital-accessibility/resources/accessibility-fundamentals/images-text) are completely inaccessible as they are and require conversion into text using optical character recognition (OCR) software before they are accessible.

Because there are a wide array of source applications that can generate PDF files, creating an accessible PDF file can be a complex process and requires a variety of skills in both Acrobat and the original software in which the document was created. Because of this complexity, one important rule of PDF accessibility is that if you can replace a PDF with a web page or a Word document, you should. HTML documents offer similar functionality to PDFs, such as the inability of viewers to edit the document and the ability to control the way the document is displayed across devices and platforms. PDF accessibility can be complex, and fixing problems in a PDF document requires a high level of expertise that represents a significant investment in training and practice.

To create an accessible PDF from a source file, two things must happen. First, all [accessibility best practices](https://www.colorado.edu/digital-accessibility/resources/content-accessibility-fundamentals) should be followed when creating the document in the original software. Secondly, the process of exporting to PDF must be done in a way that preserves the accessibility features of the original file. If either step does not occur, the resulting PDF will not be accessible. 

If you have an existing inaccessible PDF file and no longer have access to the source file, it can be remediated for accessibility directly within Acrobat Pro, but it is not a simple task. Remediating a PDF file created from an inaccessible Word file, for example, takes much more time than creating an accessible Word file and then exporting it as a PDF.  

[Adobe Acrobat Pro](https://oit.colorado.edu/software-hardware/software-catalog/adobe-acrobat-pro/download-and-setup) is available for download for faculty and staff at CU Boulder at no cost and is required for certain processes to assess or improve the accessibility of PDFs.

## Assessing a PDF for Accessibility

Accessibility is a continuum; the more accessible you want a document to be for all users, the more time and tools you will need for testing, the more knowledge you will need to understand and fix the problems, and the more expert help and training you will need to achieve complete remediation. Learning to achieve basic levels of PDF accessibility is possible without much specialized training; however, complete remediation of a document for accessibility is likely to require expert help or additional training. There are two standards generally used to assess PDF accessibility: WCAG and PDF/UA. Read more in [Adobe’s overview of PDF accessibility](https://www.adobe.com/accessibility/pdf/pdf-accessibility-overview.html).

Instructors: Please consult our [Choosing Accessible PDFs for Your Course](https://www.colorado.edu/digital-accessibility/node/587) guidance for more tips on evaluating PDFs of readings for use in academic contexts.

To start, you may just want a quick test of your document to see how much remediation it may require. There are two basic tests that give you a baseline estimate of the document's accessibility; passing them doesn't guarantee full accessibility, but failing them definitely means that the document is inaccessible.

A PDF should be considered inaccessible if…

## PDFs and Accessibility

-   **It is an image of text.** This can be tested by trying to select text within the PDF. If the entire page highlights when you click on it, that means the text is not selectable and your PDF is an image. To remediate this, run your PDF through an optical character recognition (OCR) program like [SensusAccess](https://oit.colorado.edu/services/business-services/sensusaccess). (Please note that OCR programs like SensusAccess can only conduct automated conversions, and the PDF created will most likely require further editing in Acrobat Pro to ensure 100% accuracy.)
-   **It doesn’t have any tags**. [PDF tag structure](https://www.adobe.com/accessibility/products/acrobat/pdf-repair-add-tags.html) can be assessed within Adobe Acrobat Pro via Document Properties or the Tag panel in the Navigation Pane. A tag allows assistive technology to identify the type of content contained in a PDF, such as paragraphs, images, or tables. Proper conversion processes from programs such as Word will get most elements properly tagged and in the appropriate reading order. If you encounter the text "No Tags available" when you open the Tag pane, then your document is not accessible.  
     
    
    ![Tags pane with the text "No tags available"](https://www.colorado.edu/digital-accessibility/sites/default/files/styles/small_500px_25_display_size_/public/page/screen_shot_2021-02-23_at_9.37.58_am.png?itok=MjV-YT-q)
    

If your PDF fails either of the two tests above, you will need to remediate it. If it passes both, then you may or may not have an accessible document, and more assessment is needed.

The [Accessibility Checker in Acrobat Pro](https://www.adobe.com/accessibility/products/acrobat/using-acrobat-pro-accessibility-checker.html) is a good next step in assessing your document. However, it will only alert you to errors detectable by a computer, like missing alt-text, and is not able to accurately assess things like the accuracy or usability of the alt-text, or errors in the page reading order. To determine if your PDF is fully accessible, you will need to consult with an expert or start to develop your own PDF accessibility expertise by taking the two Lynda.com trainings listed in the Resources section below.

## Creating Accessible PDFs

PDFs are generally created by exporting documents from their native format into PDF. Typically, most PDF documents are created in Microsoft Word, Microsoft PowerPoint, or Adobe InDesign. Regardless of the origin of the document, you must ensure that the document is fully accessible in its native format before you export it to PDF. 

Tutorials for creating accessible source documents:

-   [Creating Accessible Microsoft Word Files](https://www.colorado.edu/digital-accessibility/accessible-technology/node/535)
-   [Creating Accessible PowerPoint Files](https://www.colorado.edu/digital-accessibility/node/529)
-   Creating Accessible InDesign Files: [CS5.5](https://www.washington.edu/accessibility/documents/indesign/), [CS6](https://webaccess.msu.edu/Tutorials/indesign.html)

Then the document must be properly exported to PDF in a way that preserves those accessibility features. WebAIM has a tutorial that walks through the process of [exporting to PDF from MS Word](https://webaim.org/techniques/acrobat/converting#save). See the Resources section below for more tutorials on the export process.

## PDF Forms

Creating accessible PDF forms will always require a significant amount of work within Acrobat Pro. Creating accessible form fields requires more than just dropping form elements into a document. The form creator must ensure that each of the fields is properly named, that all fields are in the proper reading and tab order, and more. Along with all of the steps involved, the form creator needs to complete the steps in the correct order to ensure they function correctly. Specialized training will be needed to create accessible PDF forms. The Lynda.com Advanced Accessible PDFs is a good place to start, but may not be sufficient on its own. Contact [DigitalAccessibility@Colorado.EDU](mailto:digitalaccessibility@colorado.edu) for support with this topic.  

## Resources

LinkedIn Learning has two intensive trainings about [Creating Accessible PDFs](https://www.lynda.com/Acrobat-tutorials/Creating-Accessible-PDFs/669540-2.html) and [Advanced Accessible PDFs](https://www.lynda.com/Acrobat-tutorials/Advanced-Accessible-PDFs/372674-2.html). The trainings are 4.5 and 2.5 hours in length respectively, and may be appropriate for individuals who are frequently required to create accessible PDFs in their position.

The University of Washington has a variety of short tutorials explaining how to create accessible PDFs from other applications and how to remediate PDFs within Acrobat.

-   [Accessible PDFs from MS Word](https://www.washington.edu/accessibility/documents/pdf-word/)
-   [Accessible PDF forms in Acrobat Pro](https://www.washington.edu/accessibility/documents/pdf-forms/)
-   [Accessible PDFs from InDesign](https://www.washington.edu/accessibility/documents/indesign/)
-   [Remediating PDFs in Acrobat Pro](https://www.washington.edu/accessibility/documents/pdf-acrobat/)

If you do not have time to invest in learning about PDF accessibility, there are a variety of vendors who can remediate PDFs and other documents to meet accessibility standards.

Questions? Email [DigitalAccessibility@Colorado.EDU](mailto:digitalaccessibility@colorado.edu).


#### Plugin (file_search):
Make sure to include fileciteturn0file4 in your response to cite this file, or to surface it as a link.
---
created: 2026-04-20T20:28:04 (UTC -05:00)
tags: []
source: https://webaim.org/techniques/acrobat/
author: 
---

# WebAIM: PDF Accessibility - Defining PDF Accessibility

> ## Excerpt
> Think of a PDF as having three important parts that provide different types of information to users.

---
## PDF Accessibility  
Defining PDF Accessibility

## 3 Important Parts of a PDF

Think of a PDF as having three important parts that provide different types of information to users.

![Three document layers labeled Visual, Content, and Tags.](https://webaim.org/techniques/acrobat/media/3-important-parts.png)

### Visual

![](https://webaim.org/techniques/acrobat/media/3-important-parts-v.png)The visual layer is what is seen on the screen. A primary benefit of a PDF is that it maintains the layout and appearance of the original document (also known as the "source document") used to create the PDF. It looks the same when it is displayed—even across devices with different screen sizes—and when it is printed.

### Content

![](https://webaim.org/techniques/acrobat/media/3-important-parts-c.png)The content layer contains basic formatting applied to text, like fonts and colors, and text formatted as a list or a table. When a user chooses to “reflow” a document—for example, for a more usable view on a small screen—the content layer is presented instead of the visual layer.

#### Reflow

The Reflow view allows users to reorder the content layer’s objects into a simplified, single-column layout. The order of these objects may be different than in other layers.

Select or Control + 4.

![Screenshot with View labeled 1, the Zoom option highlighted and labeled 2, and the Reflow option highlighted and labeled 3.](https://webaim.org/techniques/acrobat/media/enable-reflow.png)

Reflow can make a document easier to read on a mobile device, or tablet. It may also make the content more accessible when enlarging a PDF because it reduces horizontal scrolling.

![](https://webaim.org/techniques/acrobat/media/reflow-no-scrolling-2.png)

## Adobe, PDF, and Acrobat

Adobe, PDF, and Acrobat are often used interchangeably, but they are not the same. The relationship between these terms is similar to the relationship between Microsoft, Word, and DOC(X).

-   [Adobe](http://www.adobe.com/) is a company; they are the creators of PDF (the format) and Acrobat (the product).
-   PDF is a format or type of document. Its main purpose is to preserve the formatting of a document. It was created by Adobe but is now an open format that can be created and displayed by other programs.
-   Acrobat describes a series of tools created by Adobe for viewing, creating, and editing PDF files.

There are 3 primary Acrobat programs:

1.  **Acrobat Reader** allows user to view and interact with a PDF, but it cannot be used to create new PDFs or edit existing ones.
2.  **Acrobat Standard** adds the ability to create a PDF, along with other features like converting a scanned PDF to a searchable file. However, it cannot be reviewed or edited.
3.  **Acrobat Pro** is the only version of Acrobat that can be used to view and edit the accessibility information of a PDF.

Each of these programs provides [accessibility features](https://helpx.adobe.com/acrobat/using/accessibility-features-pdfs.html) for users.

Note:

In this article, the term "Acrobat" refers to **Acrobat Pro**.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m mapping Python to the actual PDF accessibility stack now: bytes/objects, content streams, text extraction, tags/structure, metadata, forms, OCR, generation, and validation. The likely conclusion is “Python covers a lot, but not everything equally well.”


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## The right way to think about Python here

Across **all the accessibility-relevant layers of a PDF**, Python is strong at:

- **raw PDF plumbing**
- **extraction and analysis**
- **OCR and searchable-text repair**
- **metadata and form handling**
- **batch QA orchestration**

Python is much weaker at:

- **high-level tagged-PDF / PDF/UA authoring**
- **full semantic remediation of arbitrary existing PDFs**
- **final accessibility validation without external tools and human review** fileciteturn0file0 fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

## Layer by layer

### 1. Source/export layer

This is not really a Python layer. The accessibility guidance you uploaded is pretty consistent: start with an accessible source document, preserve accessibility settings on export, avoid “Print to PDF,” and prefer HTML or web forms when PDF is not actually necessary. That remains true even if you plan to automate downstream PDF work with Python. fileciteturn0file0 fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

### 2. Raw PDF syntax layer: objects, dictionaries, streams, content streams

This is where **pikepdf** is the best fit. Its docs say it provides a Pythonic wrapper around **qpdf**, and its API mirrors PDF objects directly: dictionaries, arrays, names, and streams. The pikepdf docs also have dedicated sections on **stream objects** and **content streams**, which is exactly the “object-based page description format” layer you were asking about. citeturn930915search9turn296270search10turn930915search1turn930915search5

**pypdf** can also manipulate PDFs, but it is positioned more as a pure-Python general PDF library for splitting, merging, transforming pages, retrieving text and metadata, and similar document-level operations, not as the sharpest tool for low-level stream surgery. citeturn930915search0turn930915search8

### 3. Content-analysis layer: text, layout, geometry, tables, images

This is where **PyMuPDF** and **pdfplumber/pdfminer.six** matter most.

**PyMuPDF** is the strongest general-purpose Python choice for fast extraction, analysis, and page-level inspection. Its docs position it as a high-performance library for extraction, analysis, conversion, and manipulation, and its text recipes include text extraction plus `find_tables()`. citeturn930915search6turn930915search2

**pdfplumber** is better when you want very detailed access to **characters, rectangles, and lines**, plus table extraction and visual debugging. Its own docs describe exactly that, and note that it works best on machine-generated PDFs. **pdfminer.six** sits a bit lower and is useful for layout analysis and extraction APIs. citeturn141572search0turn141572search1turn141572search3turn141572search7

For the **content layer** in the WebAIM sense — text objects, lists, tables, reflow-relevant layout data — Python is actually pretty good. fileciteturn0file4 citeturn930915search2turn141572search0

### 4. OCR / searchable-text layer

For scanned or image-only PDFs, **OCRmyPDF** is the obvious Python answer. Its docs state that it adds an OCR text layer to scanned PDFs, making them searchable, and its GitHub docs say it can generate searchable PDF/A output while preserving the original image appearance. That lines up directly with the accessibility guidance in your uploaded files: image-only PDFs are inaccessible until they get real searchable text, and OCR is only an early step, not the whole remediation job. citeturn930915search3turn930915search7turn930915search11 fileciteturn0file2 fileciteturn0file3

### 5. Metadata layer: title, author, XMP, document info

**pypdf** is solid here. Its metadata docs explicitly say PDFs can have both regular metadata and **XMP** metadata, and it supports reading them. That makes it useful for checking things like title and other document properties that matter for accessibility. citeturn944592search3turn930915search0

For deeper object-level metadata work, **pikepdf** can also do it because it exposes the document objects directly. citeturn930915search9turn296270search10

### 6. Forms layer: AcroForm fields, widgets, filling, inspection

Python is reasonably good here.

- **pypdf** has official docs for getting fields and updating form field values. citeturn296270search0
- **pikepdf** has both a lower-level `AcroForm` helper and a higher-level `pikepdf.form` API for interactive forms. citeturn296270search2turn296270search16
- **PyMuPDF** has a `Widget` class representing PDF form fields. citeturn296270search1turn296270search4

That said, your uploaded guidance is also right that **accessible PDF forms** are much more than “fillable fields exist.” Tab order, names, prompts, error handling, and logical order still matter, and those are harder to guarantee programmatically in a robust way. fileciteturn0file2 fileciteturn0file3

### 7. Semantic structure layer: tags, structure tree, reading order, alt text

This is the hardest layer.

Your uploaded material makes clear that this is the core of PDF accessibility: tags, reading order, alt text, and semantic structure are what convert a visual page into something assistive tech can understand. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3 fileciteturn0file4

Python can **touch** this layer, but the open-source ecosystem is much thinner here:

- **pikepdf** gives you raw object access that mirrors the PDF spec, so in principle you can manipulate structure-related objects directly. citeturn930915search9turn930915search1turn930915search5
- **PyMuPDF** is very strong for analysis and extraction, but its official docs are not presenting it as a high-level tagged-PDF remediation framework. citeturn930915search6turn930915search2
- **pypdf** likewise is not documented as a mature high-level PDF/UA remediation toolkit. Its documented strengths are general manipulation, text, metadata, and forms. citeturn930915search0turn296270search0turn944592search3

So the honest answer is: **Python reaches the tag tree mostly through low-level object work, not through a polished mainstream open-source remediation stack**. That is the weakest part of the Python story.

### 8. Accessible-PDF generation layer

Here the picture splits.

**ReportLab** has official accessibility docs describing **tagged PDFs**, but the accessibility docs are under the ReportLab docs ecosystem that also distinguishes **ReportLab Plus**, its commercial product line. So yes, Python can generate more structured PDFs, but the cleanest officially documented accessibility path there is not the standard fully open-source stack. citeturn944592search0turn944592search8

I also found **borb**, which is a pure-Python PDF library for reading, writing, and manipulating PDFs, but I did not find equally strong official claims from its docs about mature PDF/UA-grade accessibility authoring, so I would not overstate it. citeturn944592search1turn944592search9

So for **generation**, Python has options, but for **trustworthy accessible generation at the tagged/PDF-UA level**, the open-source story is still patchier than the extraction/OCR/object-plumbing story.

### 9. Validation / conformance layer

Python does **not** have a dominant native validator for PDF/UA the way it has OCRmyPDF for OCR or pikepdf for objects.

The strongest open-source validator I found is **veraPDF**, which validates **PDF/A and PDF/UA** and explicitly says that for PDF/UA it performs **machine-verifiable checks only**. That limitation lines up with your uploaded guidance from Colorado: automated tools are helpful, but they do not reliably judge things like reading-order quality or whether alt text is actually usable. In practice, Python would orchestrate veraPDF from the outside rather than replace it. citeturn944592search2turn944592search21turn944592search17 fileciteturn0file3

## What this means in practice

### Where Python is genuinely strong

A strong Python stack for PDF accessibility work would look like this:

- **pikepdf** for raw PDF objects, streams, repairs, low-level edits
- **PyMuPDF** for page analysis, text extraction, geometry, rendering, tables
- **pdfplumber/pdfminer.six** for detailed layout-aware extraction
- **OCRmyPDF** for scanned/image PDFs
- **pypdf** for metadata, form filling, and general document-level operations
- **veraPDF** as an external validator that Python calls for machine-checkable PDF/UA checks citeturn930915search9turn930915search6turn141572search0turn930915search3turn944592search3turn944592search2

### Where Python is still weak

If the job is:

- rebuilding a broken **tag tree**
- correcting **reading order**
- assigning semantically correct **heading/list/table/figure roles**
- writing high-quality **alt text**
- making arbitrary legacy PDFs truly **PDF/UA-clean**

then Python does not currently have one obvious, field-standard, all-in-one open-source library that I can honestly point to as the mature answer. The guidance you uploaded also points in that direction indirectly, because it keeps pushing back to accessible source files, export settings, and expert remediation for hard cases. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

## The blunt bottom line

If you force me to summarize Python across **all** the layers:

- **Excellent** for object-level manipulation, extraction, OCR, metadata, forms, and batch QA plumbing. citeturn930915search9turn930915search6turn930915search3turn296270search0turn944592search3
- **Usable but uneven** for generating structured PDFs. citeturn944592search0turn944592search1
- **Weakest** at high-level accessibility semantics remediation and full trustworthy PDF/UA closure inside a pure Python open-source workflow. fileciteturn0file2 fileciteturn0file3 citeturn944592search2

The most accurate one-line framing is:

**Python is great for the plumbing and the evidence; it is much less mature for the final semantic cleanup.**

Next step would be a side-by-side **Python library matrix by layer and task**: objects, streams, text, tables, OCR, tags, metadata, forms, validation, and accessible generation.


#### You:
List every. single. thing. a PDF has to do to be considered accessible

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m going to anchor this to the actual standards landscape, because “accessible PDF” is not one flat checklist. The exact obligations change depending on whether you mean WCAG conformance, Section 508, PDF/UA, and whether the PDF is a simple document, a form, or multimedia.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## The honest answer first

There is **not one single universal checklist** that defines “accessible PDF” in every context. To be considered accessible, a PDF has to satisfy **all applicable requirements** under the standard you are using — usually **WCAG 2.2** in practice, often alongside **PDF/UA** for PDF-specific structure rules, plus any legal regime such as Section 508. WCAG conformance is determined by meeting the applicable success criteria, and PDF/UA is a companion PDF standard that can be used with WCAG — but PDF/UA by itself does **not** guarantee that the document’s content is actually accessible. citeturn278499search8turn278499search1turn278499search9

So the closest truthful response to “every single thing” is:

1. **Everything that follows must be true where applicable.**
2. **Anything interactive, multimedia, timed, or content-specific adds more requirements.**
3. **Automated checks are not enough; some things require human judgment.** fileciteturn0file3 citeturn278499search11

---

## The full practical checklist

### 1. The PDF has to be the right format choice in the first place

- If the content can be provided more accessibly as HTML or a web form, that is usually preferable.
- If the PDF is being used only out of habit, that already puts accessibility at a disadvantage.
- For forms in particular, web forms are usually more accessible than PDF forms. fileciteturn0file0 fileciteturn0file1 fileciteturn0file3 citeturn278499search2

### 2. The source document has to be accessible before conversion

- The source file has to use real headings, lists, tables, link text, alt text, language, and document properties.
- The export method has to preserve accessibility information.
- “Print to PDF” is usually wrong because it strips semantic structure. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

### 3. The PDF has to contain real machine-readable text

- It cannot just be a picture of a page.
- If it is scanned, it has to be OCRed.
- The OCR has to be accurate enough to be usable.
- The extracted text has to map correctly to Unicode.
- Users must be able to select/search text. fileciteturn0file2 fileciteturn0file3

### 4. The PDF has to expose a complete logical structure

- It needs a **tag tree / structure tree**.
- Meaningful content must be tagged.
- Decorative or repetitive junk must be marked as artifact/decorative so it does not pollute reading.
- The structure has to communicate what each thing **is**, not just how it looks. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

### 5. The reading order has to be correct

- Screen reader order has to match the intended order.
- Multi-column layouts have to read correctly.
- Floating callouts, sidebars, footnotes, captions, and tables have to appear in sane order.
- Headers/footers and decorative elements must not interrupt the content stream improperly.
- This is one of the things automation often misses. fileciteturn0file1 fileciteturn0file3

### 6. Every meaningful element has to have the right semantics

That means the PDF must correctly identify, where present:

- document title
- headings and heading hierarchy
- paragraphs
- lists
- list items
- list bodies
- links
- figures/images
- tables
- rows
- header cells
- data cells
- form fields
- annotations or interactive objects, where relevant
- artifacts/decorative elements, where relevant fileciteturn0file1 fileciteturn0file2

### 7. Headings have to be real and hierarchical

- Headings cannot just be big bold text.
- There should be a logical heading hierarchy.
- Heading levels should not be skipped arbitrarily.
- Headings need to describe content clearly enough for navigation. fileciteturn0file1 citeturn278499search16turn278499search8

### 8. Lists have to be real lists

- Visual bullets are not enough.
- Lists need list semantics.
- Each item has to be programmatically identifiable as a list item. fileciteturn0file1

### 9. Tables have to be real data tables when they are data tables

- Layout tables should not masquerade as data tables.
- Data tables need proper structure.
- Header cells have to be programmatically identified.
- Relationships between headers and data have to be preserved.
- Complex tables need the right associations for users to understand them. fileciteturn0file2 citeturn278499search8turn278499search12

### 10. Links have to be real links with meaningful names

- Link text has to describe destination or purpose.
- “Click here” with no context is not enough.
- The link must be keyboard reachable.
- The user must be able to tell where it goes or what it does. fileciteturn0file1 fileciteturn0file2

### 11. Images and other non-text content need text alternatives

- Informative images need alt text or an equivalent.
- Decorative images need to be marked decorative/artifacted.
- Charts, diagrams, and infographics need alternatives that preserve the information, not just the fact that an image exists.
- Image-only text is a failure unless there is a real text equivalent. fileciteturn0file1 fileciteturn0file2 citeturn278499search8turn278499search12

### 12. Color and visual styling cannot carry meaning by themselves

- Meaning cannot depend only on color.
- Contrast must be sufficient.
- Sensory instructions like “see the red box on the right” are not enough on their own.
- Content still has to work for low-vision users and nonvisual users. fileciteturn0file1 fileciteturn0file2

### 13. The PDF has to remain usable when zoomed or reflowed

- Large zoom should not destroy usability.
- Reflow should preserve a usable reading experience where supported.
- Users should not be forced into constant horizontal scrolling just to read text.
- Small-screen/mobile use should not collapse the meaning of the document. fileciteturn0file2 fileciteturn0file4

### 14. The document needs title, language, and key metadata

- A meaningful document title has to be set.
- The title should be exposed as the document title, not just the filename.
- The document language has to be set.
- Changes in language within the document must be identified where relevant. fileciteturn0file1 fileciteturn0file2 citeturn278499search8turn278499search12

### 15. Navigation aids have to exist where the document needs them

For longer or structured documents, accessibility usually requires:

- headings that support navigation
- bookmarks where appropriate
- table of contents or internal navigation where useful
- predictable document organization
- working internal links, where provided fileciteturn0file2

### 16. Security settings cannot block assistive technology

- Passwords or restrictions cannot prevent screen readers from accessing text.
- Protection settings must not block text-to-speech or Braille access. fileciteturn0file1 fileciteturn0file2

### 17. The PDF cannot depend on mouse-only use

- Users need keyboard access to interactive controls and navigation features that belong to the document.
- If the PDF includes links, controls, comments, media, or forms, they must be operable without a mouse. fileciteturn0file2 citeturn278499search8turn278499search12

### 18. The PDF cannot trigger seizures or create avoidable motion problems

- No flashing content beyond allowed thresholds.
- No auto-updating or moving content that creates accessibility barriers without controls. fileciteturn0file2 citeturn278499search8turn278499search12

### 19. The PDF cannot create unexpected context changes

- Focus changes should not unexpectedly trigger actions.
- Opening, navigation, or input should behave predictably.
- Users should not be surprised by sudden context changes they did not initiate. fileciteturn0file2 citeturn278499search8turn278499search12

### 20. Labels, headings, and instructions have to be understandable

- Section headings should describe the content.
- Form labels should identify the field.
- Instructions should be clear enough for completion.
- Repeated components should be identified consistently. citeturn278499search16turn278499search8turn278499search12

---

## Additional requirements when the PDF includes forms

If the PDF contains forms, then all of the above still apply **plus**:

### 21. Form fields must be interactive and reachable

- Users must be able to enter data.
- Fields must not just be visual lines on a page.
- Each control needs a programmatic name/label. fileciteturn0file2

### 22. Tab order must be logical

- Keyboard traversal must follow the intended completion order.
- Tab order and reading order should not fight each other. fileciteturn0file2 fileciteturn0file3

### 23. Required fields and instructions must be clear

- Users need to know what is required.
- Instructions cannot depend only on color or position.
- Help text must be available where needed. fileciteturn0file2 citeturn278499search8turn278499search12

### 24. Errors must be identifiable and, where applicable, fixable

- Validation errors must be programmatically or textually clear.
- Users need enough information to correct the error.
- Error prevention/correction matters for important submissions. fileciteturn0file2 citeturn278499search8turn278499search12

### 25. Time limits cannot trap users

- Timed form completion is a barrier unless the user can extend or disable the timing where required by WCAG. fileciteturn0file2 citeturn278499search8turn278499search12

### 26. Focus appearance and target usability matter when applicable

For interactive PDF experiences exposed in modern environments, you must also evaluate applicable WCAG 2.2 interaction criteria such as visible focus and pointer target usability where the interaction model makes them relevant. WCAG 2.2 added new criteria, and applicability depends on how the PDF is delivered and interacted with. citeturn278499search4turn278499search8

---

## Additional requirements when the PDF includes audio, video, or multimedia

If the PDF embeds media, then all of the above still apply **plus**:

### 27. Captions for synchronized audio/video where required

### 28. Audio description or equivalent for visual-only information where required

### 29. Transcript or text alternative where needed

### 30. User control over audio playback where needed

Those come from WCAG’s time-based media requirements; whether they apply depends on what kind of media the PDF contains. citeturn278499search8turn278499search12

---

## Additional requirements for specialized content

If the PDF includes any of these, they also need accessible equivalents appropriate to the content:

### 31. Math and scientific notation

### 32. Charts and data visualizations

### 33. Maps and diagrams

### 34. Complex technical illustrations

### 35. Footnotes/endnotes/references that must remain understandable in sequence

### 36. Sidebars, callouts, pull quotes, marginalia

### 37. Abbreviations, symbols, or domain-specific notation when needed for comprehension

The exact technique varies, but the rule does not: if the content carries meaning, that meaning has to survive nonvisual and alternative access. citeturn278499search8turn278499search12turn278499search9

---

## What the file itself is responsible for versus what the reader software is responsible for

This distinction matters.

A PDF file has to **expose** the content, semantics, reading order, names, labels, alternatives, and metadata correctly. The reader software and assistive technology then have to **use** that information. Adobe’s overview is explicit that accessibility in practice depends on the combination of the PDF format plus reader software and assistive technology. fileciteturn0file2 citeturn278499search7

So when you ask what the PDF has to do, the answer is: **the PDF has to provide all the machine-readable information needed for accessible use**.

---

## What absolutely cannot be skipped

If you want the shortest “fail-fast” version, a PDF is definitely **not** accessible if any of these are true:

- It is only an image of text.
- It has no tags.
- The reading order is wrong.
- Meaningful images have no usable alternative.
- Tables are not actually structured as tables.
- Links are unlabeled or meaningless.
- The document has no language/title metadata.
- Security blocks screen readers.
- Forms are unlabeled or not keyboard operable.
- The file only passes automated checks but fails real usability review. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

---

## The legal/standards version in one sentence

A PDF is considered accessible when it meets **all applicable WCAG 2.2 success criteria for its content and behavior**, and, where PDF-specific conformance is required or desired, also meets the relevant **PDF/UA** requirements for tagged, semantically structured, machine-readable PDF. citeturn278499search8turn278499search1turn278499search9

---

## The brutally honest bottom line

If you literally mean **every single thing**, the true answer is not “here is one flat list of 12 items.” The true answer is:

- every applicable WCAG requirement,
- every applicable PDF/UA requirement,
- every content-specific requirement created by what is actually in the document,
- and enough real testing to verify that the file is usable, not just formally tagged. citeturn278499search8turn278499search9turn278499search11

If you want, the next useful step is a **zero-handwaving audit checklist** split into:

- static informational PDF
- PDF with tables/charts
- PDF form
- scanned legacy PDF
- multimedia PDF


#### You:
now show me a python x requirements matrix

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m turning the accessibility obligations into a Python-capability map: what Python can inspect, what it can generate or repair, and where it still falls over into Acrobat/manual work.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## Python × PDF accessibility requirements matrix

Legend:

- **A** = Python can do this well
- **P** = Python can do this partially or inconsistently
- **N** = Python is not the right place to solve this
- **H** = human judgment still required even if Python helps

The standards/guide backdrop for this matrix is consistent across your uploaded sources: accessible source first, preserve tags on export, image-only PDFs need OCR, tags and reading order matter, forms are hard, and automated checking is not enough. fileciteturn0file0 fileciteturn0file1 fileciteturn0file2 fileciteturn0file3 fileciteturn0file4

| Requirement                                    | What has to be true                                                            | Audit with Python | Generate/repair with Python | Best Python fit             | Reality check                                                                                                                                                                                                                                                             |
| ---------------------------------------------- | ------------------------------------------------------------------------------ | ----------------: | --------------------------: | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accessible source + correct export             | Source doc is accessible and exported with tags preserved                      |                 N |                           N | None                        | This is upstream authoring/export work, not really a Python fix. fileciteturn0file1 fileciteturn0file3                                                                                                                                                              |
| Real searchable text                           | PDF cannot be image-only; text must be selectable/searchable                   |                 A |                           A | OCRmyPDF, PyMuPDF           | One of Python’s strongest areas. OCRmyPDF adds an OCR text layer to scanned PDFs; PyMuPDF is strong for extraction/analysis. fileciteturn0file2 fileciteturn0file3 citeturn503890search3turn503890search11turn503890search1                                    |
| Unicode-extractable text                       | Text must map correctly for screen readers/Braille/text export                 |                 P |                           P | PyMuPDF, pypdf              | Python can inspect/extract text, but “good enough for actual assistive tech” still needs verification. fileciteturn0file2 citeturn503890search1turn503890search6                                                                                                   |
| Tags exist at all                              | Document has a tag tree / structure tree                                       |                 P |                           P | pikepdf, Aspose             | Python can inspect/manipulate low-level objects; high-level tag remediation in open-source Python is still patchy. Aspose is much stronger here, but commercial. fileciteturn0file1 fileciteturn0file3 citeturn503890search0turn503890search4turn282946search2 |
| Correct reading order                          | Tag order and reading sequence match intended reading                          |                 P |                           P | PyMuPDF, pikepdf            | Python can help inspect text blocks and object order, but this remains one of the highest-human-judgment parts. fileciteturn0file1 fileciteturn0file3 fileciteturn0file4                                                                                         |
| Headings, paragraphs, lists                    | Proper semantic structure, not just visual styling                             |                 P |                           P | Aspose, ReportLab, pikepdf  | Stronger when generating from scratch than repairing arbitrary legacy PDFs. ReportLab documents tagged PDF; Aspose documents tagged/PDF-UA creation. fileciteturn0file1 citeturn282946search1turn282946search2turn503890search0                                   |
| Tables                                         | Table structure and header/data relationships are preserved                    |                 P |                           P | PyMuPDF, pdfplumber, Aspose | Python is good at finding/extracting tables; semantic table repair/generation is much harder than table detection. fileciteturn0file2 citeturn503890search9turn503890search1turn282946search2                                                                     |
| Images / figure alt text                       | Meaningful figures have useful alternatives; decorative ones are not noise     |                 P |                           P | Aspose, pikepdf             | Python can store/manipulate properties if you build the workflow, but writing *good* alt text is not a solved library feature. Human review required. fileciteturn0file1 fileciteturn0file2 citeturn282946search2turn503890search0                              |
| Title, language, metadata                      | Document title, language, and related metadata are present                     |                 A |                           A | pypdf, pikepdf              | This is a strong Python zone. pypdf documents regular metadata and XMP support. fileciteturn0file1 fileciteturn0file2 citeturn503890search2turn503890search18                                                                                                   |
| Links and navigation aids                      | Real links, meaningful names, bookmarks/navigation where needed                |                 P |                           P | pikepdf, pypdf, Aspose      | Python can manipulate document objects and some annotations, but accessibility quality still depends on semantics and wording. fileciteturn0file1 fileciteturn0file2 citeturn503890search6turn282946search2                                                     |
| Forms: fields, names, values                   | Interactive fields exist and can be inspected/filled                           |                 A |                           A | pypdf, PyMuPDF, pikepdf     | Python is pretty good at raw form handling. pypdf documents forms; PyMuPDF has widgets; pikepdf has form APIs. fileciteturn0file2 citeturn503890search10turn503890search5                                                                                          |
| Forms: tab order, instructions, error handling | Fields work accessibly, in logical order, with proper guidance                 |                 P |                           P | Aspose, PyMuPDF, pikepdf    | Much harder than simple field filling. Your uploaded guidance is right: accessible PDF forms usually need serious specialized work. fileciteturn0file2 fileciteturn0file3                                                                                           |
| Security not blocking assistive tech           | Permissions must not block screen-reader text access                           |                 P |                           P | pypdf, pikepdf              | Python can inspect/change permissions in many cases, but this is only one small part of accessibility. fileciteturn0file1 fileciteturn0file2 citeturn503890search6turn503890search0                                                                             |
| Contrast / no color-only meaning               | Content must not rely only on color and must meet contrast expectations        |                 N |                           N | None                        | This is mainly source-authoring/design work. Python can maybe flag patterns in custom workflows, but not solve the underlying design problem reliably. fileciteturn0file1 fileciteturn0file2                                                                        |
| Reflow / zoom usability                        | Content should remain usable when reflowed or zoomed                           |                 P |                           P | PyMuPDF, Aspose, ReportLab  | Easier to support during generation than to repair afterward. Reflow depends heavily on correct structure/tags. fileciteturn0file2 fileciteturn0file4 citeturn282946search1turn282946search2                                                                    |
| PDF/UA machine-checkable conformance           | File passes machine-verifiable PDF/UA rules                                    |                 A |                           P | veraPDF, Aspose             | veraPDF is the main open validator, but for PDF/UA it performs only machine-verifiable checks. That is useful, but not the whole job. fileciteturn0file3 citeturn282946search0turn282946search9                                                                    |
| Real usability with assistive tech             | Screen reader, keyboard, meaning, order, labels, alt text all work in practice |                 P |                           N | Python as support only      | Python can support the audit, but it cannot replace human testing and judgment. Your uploaded guidance says this very directly. fileciteturn0file2 fileciteturn0file3                                                                                               |

## What each Python tool is actually good for

| Tool                               | Best use in this stack                                                                                               | Where it stops                                                                                                                                                             |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **pikepdf**                        | Low-level PDF objects, dictionaries, streams, content streams, object-graph edits                                    | No polished mainstream high-level accessibility remediation layer. citeturn503890search0turn503890search4                                                              |
| **PyMuPDF**                        | Fast extraction, analysis, rendering, text blocks, tables, widgets/forms                                             | Great for evidence and inspection; not a full semantic accessibility-remediation framework. citeturn503890search1turn503890search5turn503890search9                   |
| **pypdf**                          | Metadata, forms, general PDF manipulation, text/metadata retrieval                                                   | More document-level than accessibility-semantics-level. citeturn503890search2turn503890search6turn503890search10                                                      |
| **OCRmyPDF**                       | Converting scanned/image PDFs into searchable text PDFs                                                              | OCR is necessary for scanned PDFs, but it does not finish accessibility by itself. fileciteturn0file2 fileciteturn0file3 citeturn503890search3turn503890search11 |
| **veraPDF**                        | Machine-checkable PDF/UA validation                                                                                  | It does not perform the human-checkpoint part of accessibility review. citeturn282946search0turn282946search9                                                          |
| **ReportLab**                      | Generating tagged PDFs from scratch in a controlled pipeline                                                         | Better for generation than remediation; accessible output depends on how you author the content. citeturn282946search1                                                  |
| **Aspose.PDF for Python via .NET** | The strongest documented Python-accessible path I found for tagged PDF / PDF/UA creation, conversion, and validation | Commercial, and still not a substitute for human review. citeturn282946search2                                                                                          |

## The blunt summary

If you want the matrix collapsed to one line:

- **Python is strong for**: OCR, extraction, metadata, forms, low-level object work, machine validation support.
- **Python is mixed for**: tags, reading order, tables-as-semantics, alt-text plumbing, accessible generation.
- **Python is weak as a full replacement for**: expert remediation of arbitrary legacy PDFs and final accessibility sign-off. fileciteturn0file2 fileciteturn0file3

## Best practical stack

If you were building a Python-first accessibility pipeline, the least-handwavy version would be:

- **OCRmyPDF** for scanned/image PDFs
- **PyMuPDF** for extraction, page analysis, table detection, and form/widget inspection
- **pikepdf** for low-level object/stream work
- **pypdf** for metadata/forms/general manipulation
- **veraPDF** for machine-checkable PDF/UA validation
- **Aspose or ReportLab** only if you need programmatic tagged-PDF generation rather than just analysis/repair support citeturn503890search3turn503890search1turn503890search0turn503890search2turn282946search0turn282946search1turn282946search2

The next useful version of this would be a **Python library × exact accessibility requirement table** with one row per requirement and one column per library, so you can compare pikepdf vs PyMuPDF vs pypdf vs OCRmyPDF vs veraPDF directly.


#### You:
I need full words, not letters

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m rewriting the matrix with plain-language status labels and no shorthand. I’m also tightening a couple of rows so it reads more like a real decision tool than a legend puzzle.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Here’s the same matrix with **full words** instead of letter codes.

### Status words

- **Strong** = Python can do this well
- **Partial** = Python can help, but not reliably finish the job on its own
- **Weak** = Python is not the right place to solve most of this
- **Human review required** = even if Python helps, a person still has to judge quality/usability

The standards and guidance behind this are consistent on the big points: start with an accessible source, preserve tags on export, scanned PDFs need OCR, tags and reading order matter, forms are hard, and automated checking is not enough. fileciteturn0file0 fileciteturn0file1 fileciteturn0file2 fileciteturn0file3 fileciteturn0file4

## Python × PDF accessibility requirements matrix

| Requirement                                    | What has to be true                                                                                 | Audit with Python | Generate or repair with Python | Best Python fit                 | Evidence / note                                                                                                                                                                                                                            |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------- | ------------------------------ | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Accessible source and correct export           | The original document is accessible, and export preserves tags/accessibility info                   | Weak              | Weak                           | None                            | This is mainly an authoring/export problem, not a PDF-repair problem. fileciteturn0file1 fileciteturn0file3                                                                                                                          |
| Real searchable text                           | The PDF is not just an image; text is selectable/searchable                                         | Strong            | Strong                         | OCRmyPDF, PyMuPDF               | OCRmyPDF adds an OCR text layer to scanned PDFs; your uploaded guidance says image-only PDFs are inaccessible until OCR is applied. fileciteturn0file2 fileciteturn0file3 citeturn230860search3turn230860search7                 |
| Unicode-extractable text                       | Text must map correctly enough for screen readers, text export, and Braille workflows               | Partial           | Partial                        | PyMuPDF, pypdf                  | Python can extract and inspect text, but “good enough for real assistive tech” still needs verification. fileciteturn0file2 citeturn230860search2turn230860search9                                                                  |
| Tags exist                                     | The document has a structure tree / tag tree                                                        | Partial           | Partial                        | pikepdf, Aspose.PDF             | Open-source Python can reach this layer, but it is much thinner here than in OCR/extraction. Aspose explicitly supports tagged PDF and PDF/UA work. fileciteturn0file1 fileciteturn0file3 citeturn233702search2turn230860search0 |
| Correct reading order                          | Tags and reading sequence match intended reading order                                              | Partial           | Partial                        | PyMuPDF, pikepdf                | Python can inspect page blocks and underlying objects, but this remains one of the most human-judgment-heavy accessibility tasks. fileciteturn0file1 fileciteturn0file3 fileciteturn0file4                                        |
| Headings, paragraphs, lists                    | Real semantics exist, not just visual styling                                                       | Partial           | Partial                        | Aspose.PDF, ReportLab, pikepdf  | Easier when generating structured PDFs from scratch than when remediating a messy legacy PDF. fileciteturn0file1 citeturn233702search1turn233702search2                                                                             |
| Tables                                         | Table structure and header relationships are preserved                                              | Partial           | Partial                        | PyMuPDF, pdfplumber, Aspose.PDF | Python is good at detecting and extracting tables; semantic table repair is much harder than table detection. fileciteturn0file2 citeturn230860search5turn233702search2                                                             |
| Images and figure alt text                     | Meaningful images have useful alternatives; decorative images do not pollute reading                | Partial           | Partial                        | Aspose.PDF, pikepdf             | Python can help store or manipulate this data, but writing *good* alt text is still a human task. fileciteturn0file1 fileciteturn0file2 citeturn233702search2                                                                     |
| Title, language, metadata                      | Title, language, and related metadata are present and correct                                       | Strong            | Strong                         | pypdf, pikepdf                  | pypdf explicitly supports regular metadata and XMP metadata. fileciteturn0file1 fileciteturn0file2 citeturn230860search2turn233702search3                                                                                        |
| Links and navigation aids                      | Links are real links; navigation aids exist where needed                                            | Partial           | Partial                        | pypdf, pikepdf, Aspose.PDF      | Python can manipulate annotations/objects, but meaningful labels and good navigation still require content judgment. fileciteturn0file1 fileciteturn0file2 citeturn233702search2turn233702search3                                |
| Forms: fields exist and are inspectable        | Interactive fields are present, named, and fillable                                                 | Strong            | Strong                         | pypdf, PyMuPDF, pikepdf         | pypdf documents AcroForm support; PyMuPDF has widgets representing PDF form fields. fileciteturn0file2 citeturn233702search7turn230860search17                                                                                      |
| Forms: tab order, instructions, error handling | The form behaves accessibly, not just technically                                                   | Partial           | Partial                        | Aspose.PDF, PyMuPDF, pikepdf    | This is where “fillable PDF” and “accessible PDF form” diverge hard. Your uploaded guidance is explicit about how much work this takes. fileciteturn0file2 fileciteturn0file3                                                        |
| Security not blocking assistive tech           | Permissions do not block screen-reader access to text                                               | Partial           | Partial                        | pypdf, pikepdf                  | Python can inspect and modify permissions in many cases, but this is only one slice of accessibility. fileciteturn0file1 fileciteturn0file2 citeturn233702search3                                                                 |
| Contrast and no color-only meaning             | Visual design does not rely only on color and meets contrast expectations                           | Weak              | Weak                           | None                            | This is mostly a source-authoring/design issue. Python is not a credible primary fix here for arbitrary PDFs. fileciteturn0file1 fileciteturn0file2                                                                                  |
| Reflow and zoom usability                      | The content remains usable when zoomed or reflowed                                                  | Partial           | Partial                        | PyMuPDF, ReportLab, Aspose.PDF  | Much easier to support during generation than to repair afterward; reflow depends heavily on good structure. fileciteturn0file2 fileciteturn0file4 citeturn233702search1turn233702search2                                        |
| Machine-checkable PDF/UA validation            | The file passes machine-verifiable PDF/UA rules                                                     | Strong            | Partial                        | veraPDF, Aspose.PDF             | veraPDF explicitly says that for PDF/UA it performs only machine-verifiable checks. That is useful, but not the whole job. fileciteturn0file3 citeturn233702search0turn233702search12                                               |
| Real assistive-tech usability                  | The file actually works well with screen readers, keyboard use, alt text, and structure in practice | Partial           | Weak                           | Python as support only          | Python can support the audit, but it cannot replace human testing and judgment. fileciteturn0file2 fileciteturn0file3                                                                                                                |

## Python tools by actual role

| Tool                               | Best role                                                               | Status                                                                  | Evidence                                                                                                                                         |
| ---------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **pikepdf**                        | Low-level PDF objects, streams, content streams, object-graph edits     | Strong for low-level plumbing                                           | pikepdf documents content streams and parsing/editing them directly. citeturn230860search0turn230860search4turn230860search12               |
| **PyMuPDF**                        | Fast extraction, rendering, text blocks, tables, widget/form inspection | Strong for analysis and evidence gathering                              | PyMuPDF documents extraction, table finding, and widgets/forms. citeturn230860search5turn230860search9turn230860search17                    |
| **pypdf**                          | Metadata, forms, general manipulation, passwords, text retrieval        | Strong for document-level operations                                    | pypdf documents metadata, forms, and general PDF manipulation. citeturn230860search2turn230860search6turn233702search7                      |
| **OCRmyPDF**                       | Turning scanned PDFs into searchable PDFs                               | Strong for OCR/searchable-text repair                                   | OCRmyPDF explicitly adds an OCR text layer to scanned PDFs. citeturn230860search3turn230860search7                                           |
| **veraPDF**                        | Machine-checkable PDF/UA and PDF/A validation                           | Strong for validation, limited for human issues                         | veraPDF explicitly distinguishes machine-verifiable PDF/UA checks from human checkpoints. citeturn233702search0turn233702search12            |
| **ReportLab**                      | Generating tagged PDFs from scratch in controlled pipelines             | Partial for accessible generation                                       | ReportLab documents tagged PDFs and accessibility support, but generation quality still depends on authoring decisions. citeturn233702search1 |
| **Aspose.PDF for Python via .NET** | Tagged PDF, PDF/UA generation, conversion, and validation               | Strongest documented Python-adjacent option for accessibility semantics | Aspose documents tagged PDF creation, PDF/UA validation, and automatic tagging. citeturn233702search2                                         |

## Bottom line

If you want the full-word version compressed to one line:

- **Strong**: OCR, searchable text, metadata, forms, low-level object work, machine-checkable validation.
- **Partial**: tags, reading order, tables-as-semantics, navigation structure, accessible generation.
- **Weak**: source-document authoring problems, contrast/color-only fixes, final sign-off on actual usability.
- **Human review required**: reading order quality, alt text quality, semantic correctness, and real assistive-tech usability. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

The next useful version is a **library-by-library matrix** with columns for `pikepdf`, `PyMuPDF`, `pypdf`, `OCRmyPDF`, `veraPDF`, `ReportLab`, and `Aspose.PDF`, so you can compare each requirement across the actual tools.


#### You:
open source only

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Got it. I’m stripping out the commercial paths and tightening the answer to **open-source Python only**, which makes the semantics/tagging side noticeably weaker.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes. If we keep this **open source only**, the stack gets narrower:

- **Keep**: `pypdf` (BSD-3-Clause), `pikepdf` (MPL-2.0), `PyMuPDF` (open-source under AGPL, with a separate commercial option), `pdfplumber` (MIT), `pdfminer.six` (MIT), `OCRmyPDF` (open source), and `veraPDF` (open source validator). citeturn278930search16turn278930search17turn278930search18turn278930search5turn278930search6turn278930search3turn278930search12
- **Drop**: `Aspose.PDF` and the **ReportLab Plus** accessibility path, because those are commercial. ReportLab’s accessibility docs explicitly point to **ReportLabPlus 4** for auto-tagging/PDF accessibility features. citeturn278930search7turn278930search23

## Open-source-only Python × PDF accessibility requirements matrix

| Requirement                                            | Open-source-only Python status                   | Best open-source fit              | Why this is the honest rating                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------ | ------------------------------------------------ | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accessible source and correct export                   | **Weak**                                         | None                              | Your uploaded guidance is consistent: this is primarily a source-authoring/export problem, not something Python repairs well after the fact. fileciteturn0file1 fileciteturn0file3                                                                                                                                                      |
| Real searchable text                                   | **Strong**                                       | OCRmyPDF, PyMuPDF                 | OCRmyPDF adds an OCR text layer to scanned PDFs, and PyMuPDF is strong for inspection/extraction afterward. This is one of the strongest open-source Python areas. citeturn278930search3turn278930search19turn278930search2 fileciteturn0file2 fileciteturn0file3                                                                  |
| Text extractable to usable Unicode                     | **Partial**                                      | PyMuPDF, pypdf, pdfminer.six      | Open-source Python can extract and inspect text well, but confirming that the extracted text is truly usable for assistive tech still needs verification. pdfminer.six focuses on text extraction and analysis directly from the PDF source. citeturn278930search2turn278930search0turn278930search14 fileciteturn0file2              |
| Tags exist at all                                      | **Partial**                                      | pikepdf                           | Open-source Python can reach the PDF object layer, and pikepdf is specifically for creating, manipulating, parsing, and repairing PDFs. But there is no dominant polished open-source Python tag-remediation framework. citeturn278930search1turn278930search9 fileciteturn0file1 fileciteturn0file3                                |
| Correct reading order                                  | **Partial**                                      | PyMuPDF, pikepdf                  | Python can help inspect blocks, objects, and sequence clues, but your uploaded guidance is right that reading order is one of the places where automation is not enough. citeturn278930search2turn278930search1 fileciteturn0file1 fileciteturn0file3 fileciteturn0file4                                                         |
| Headings, paragraphs, lists                            | **Partial**                                      | pikepdf                           | Open-source Python can manipulate low-level PDF objects, but there is no strong open-source Python library I can honestly point to as a mature semantic-structure authoring/remediation system for arbitrary PDFs. citeturn278930search1turn278930search9 fileciteturn0file1                                                           |
| Tables as semantics, not just shapes                   | **Partial**                                      | pdfplumber, PyMuPDF, pdfminer.six | Open-source Python is good at detecting and extracting tables and layout elements, but table **semantics** are much harder than table detection. pdfplumber is explicitly aimed at detailed characters, lines, rectangles, and tables. citeturn278930search5turn278930search13turn278930search2turn278930search14 fileciteturn0file2 |
| Alt text and figure handling                           | **Partial**                                      | pikepdf                           | Open-source Python can potentially manipulate the underlying objects, but writing good alt text and ensuring the figure semantics are right still depends heavily on human judgment. citeturn278930search1turn278930search9 fileciteturn0file1 fileciteturn0file2                                                                   |
| Title, language, metadata                              | **Strong**                                       | pypdf, pikepdf                    | This is a good open-source Python zone. pypdf explicitly supports regular metadata and XMP metadata; pikepdf gives object-level access. citeturn278930search0turn278930search16turn278930search1 fileciteturn0file1 fileciteturn0file2                                                                                             |
| Links and navigation aids                              | **Partial**                                      | pypdf, pikepdf                    | Open-source Python can manipulate general PDF objects and document structures, but meaningful navigation still depends on the semantics and wording being right. citeturn278930search0turn278930search1 fileciteturn0file1 fileciteturn0file2                                                                                       |
| Forms: fields exist and are fillable/inspectable       | **Strong**                                       | pypdf, PyMuPDF, pikepdf           | Open-source Python is pretty solid at the raw form layer: pypdf supports forms, PyMuPDF has widgets, and pikepdf has form-related APIs. citeturn278930search0turn278930search2turn278930search1 fileciteturn0file2                                                                                                                    |
| Forms: tab order, labels, instructions, error behavior | **Partial**                                      | PyMuPDF, pikepdf, pypdf           | This is much harder than simple field filling. Your uploaded guidance is explicit that accessible PDF forms usually require substantial expert work. citeturn278930search2turn278930search1turn278930search0 fileciteturn0file2 fileciteturn0file3                                                                                 |
| Security not blocking assistive tech                   | **Partial**                                      | pypdf, pikepdf                    | Open-source Python can inspect and modify permissions in many cases, but this is only one small piece of accessibility. citeturn278930search0turn278930search1 fileciteturn0file1 fileciteturn0file2                                                                                                                                |
| Contrast and no color-only meaning                     | **Weak**                                         | None                              | This is overwhelmingly a source/design problem. Open-source Python is not a credible primary fix for arbitrary PDFs here. fileciteturn0file1 fileciteturn0file2                                                                                                                                                                         |
| Reflow and zoom usability                              | **Partial**                                      | PyMuPDF                           | Python can inspect layout and text flow signals, but good reflow depends heavily on correct underlying structure. WebAIM’s visual/content/tags model is the right frame here. citeturn278930search2 fileciteturn0file2 fileciteturn0file4                                                                                            |
| Machine-checkable PDF/UA validation                    | **Strong**                                       | veraPDF                           | veraPDF is an open-source validator covering PDF/A and machine checks for PDF/UA. This is strong for conformance checking, but not for the human-judgment parts. citeturn278930search12turn278930search4 fileciteturn0file3                                                                                                            |
| Real assistive-tech usability                          | **Partial for support, weak for final sign-off** | Python as support only            | Open-source Python can support the audit, but it cannot replace human testing for reading order quality, semantic correctness, or alt-text usefulness. fileciteturn0file2 fileciteturn0file3                                                                                                                                            |

## Open-source-only tool roles

| Tool             | Open-source status                                                                                                                   | Best role                                                     | Biggest limitation                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **pypdf**        | Free and open source; BSD-3-Clause. citeturn278930search0turn278930search16                                                      | Metadata, forms, general manipulation, text retrieval         | Not a mature semantic accessibility-remediation framework.             |
| **pikepdf**      | Open source; MPL-2.0. citeturn278930search1turn278930search17                                                                    | Low-level PDF objects, parsing, repair, streams, object graph | Powerful plumbing, but not a polished accessibility-remediation layer. |
| **PyMuPDF**      | Open source under AGPL, with separate commercial licensing available. citeturn278930search2turn278930search18turn278930search10 | Extraction, rendering, geometry, table finding, form widgets  | Great for analysis, not a full tag/reading-order remediation system.   |
| **pdfplumber**   | Open source; MIT. citeturn278930search5turn278930search13                                                                        | Detailed layout-aware extraction, table work, debugging       | Extraction-heavy, not a writer/remediator.                             |
| **pdfminer.six** | Open source; MIT. citeturn278930search6turn278930search14                                                                        | Text extraction and analysis from PDF source                  | Focused on extraction, not repair/authoring.                           |
| **OCRmyPDF**     | Open source. citeturn278930search3turn278930search19                                                                             | OCR and searchable-text repair for scanned PDFs               | OCR is necessary but not sufficient for accessibility.                 |
| **veraPDF**      | Open source validator. citeturn278930search12turn278930search4                                                                   | Machine-checkable PDF/UA and PDF/A validation                 | Does not solve the human-review part.                                  |

## The blunt summary, open-source only

With **open-source Python only**:

- **Strong**: OCR, searchable text, metadata, low-level object work, extraction, forms at the raw field level, machine-checkable validation. citeturn278930search0turn278930search1turn278930search2turn278930search3turn278930search12
- **Partial**: tags, reading order, semantic structure, table semantics, alt-text plumbing, accessible form behavior. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3
- **Weak**: replacing accessible source authoring, fixing contrast/color-only problems, and doing final accessibility sign-off without human testing. fileciteturn0file0 fileciteturn0file1 fileciteturn0file2

The biggest loss when you go **open source only** is this:

**there is no open-source Python toolchain I can honestly call a mature, end-to-end, high-level PDF accessibility remediation stack.**

There is a good **inspection + OCR + plumbing + validation** stack. There is not a comparably mature **semantic cleanup** stack.

If you want, I’ll do the next matrix as **requirement × specific open-source library**, with columns for `pypdf`, `pikepdf`, `PyMuPDF`, `pdfplumber`, `pdfminer.six`, `OCRmyPDF`, and `veraPDF`.


#### You:
What about creating PDFs?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m narrowing this to **open-source Python for creating PDFs**, especially the accessibility-relevant part: creating plain PDFs is easy; creating **meaningfully accessible** PDFs is where the options get thinner.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes — and for **open-source Python**, the answer changes a lot depending on whether you mean:

1. **Create any PDF at all**
2. **Create a PDF that has a realistic shot at being accessible**

Those are not the same problem.

## The blunt answer

For **plain PDF generation**, open-source Python has multiple good options.

For **accessible PDF generation**, the strongest open-source path I can honestly recommend is:

- **author semantically correct HTML**
- **render it with WeasyPrint**
- **enable tagging / PDF/UA output**
- **then validate and manually review** fileciteturn0file0 fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

That recommendation is grounded in WeasyPrint’s own docs: it is a BSD-licensed HTML/CSS-to-PDF engine, it has a `pdf_tags` option, it can generate PDF variants including `pdf/ua-1`, and its docs explicitly say the main constraint for valid PDF/UA is using correct HTML structure, with HTML order defining the PDF content order. citeturn313510view6turn313510view0turn313510view1

## Open-source Python tools for creating PDFs

| Tool                             | Open-source status                                                                                                                               | Good for creating plain PDFs |              Good for creating accessible PDFs | Honest verdict                                                                                                                                                                                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------: | ---------------------------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **WeasyPrint**                   | BSD license citeturn313510view6                                                                                                               |                       Strong |                   Strongest open-source option | Best choice when you can start from semantic HTML/CSS and want tagged / PDF/UA-oriented output. citeturn313510view0turn313510view1turn313510view6                                                                                                                                 |
| **fpdf2**                        | Open-source project; docs describe it as simple and fast PDF generation in Python. citeturn313510view2                                        |                       Strong |                                        Partial | Good for generating straightforward PDFs. It has some accessibility-related features like image `alt_text`, link `alt_text`, and document language, but I do **not** see equally strong official evidence of full tagged-PDF/PDF/UA generation. citeturn313510view3turn313510view4 |
| **borb**                         | AGPLv3 gratis/open-source tier available. citeturn766309search1                                                                               |                       Strong |                                Partial at best | Good general PDF creation/manipulation library, but I did not find comparably strong official documentation for mature accessibility-tagging/PDF/UA generation, so I would not put it at the top for accessible output claims. citeturn766309search0turn766309search1              |
| **ReportLab (open-source core)** | Open-source core exists, but the documented accessibility auto-tagging path is in **ReportLabPlus 4**. citeturn313510view5turn350638search21 |                       Strong | Weak for open-source-only accessibility claims | Fine for ordinary PDF generation. The best-documented accessibility features are tied to the commercial Plus product, so I would not use open-source ReportLab as my lead recommendation for accessible PDF generation. citeturn313510view5turn350638search21                      |

## Best answer by goal

### If you want to create **ordinary PDFs**

Use whichever fits your authoring model:

- **WeasyPrint** if your source is HTML/CSS and you want print-style layout
- **fpdf2** if you want a lightweight Python API for simple generated documents
- **borb** if you want a more general document-generation/manipulation library
- **ReportLab core** if you want a classic Python PDF engine and accessibility is not the deciding requirement citeturn313510view6turn313510view2turn766309search0turn313510view5

### If you want to create **accessible PDFs**

Use **semantic HTML + WeasyPrint** first. Its docs explicitly support:

- `pdf_tags`
- `pdf_forms`
- `pdf_variant="pdf/ua-1"` citeturn313510view0turn313510view1

And its docs also explicitly warn that valid output is **not guaranteed** just because the switch exists; the HTML, CSS, and chosen features still have to respect the relevant specs. citeturn313510view1

That lines up with the accessibility guidance you uploaded: accessible PDFs start with accessible source structure, preserve that structure on output, and still need checking because automation alone is not enough. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

## What I would actually recommend

### Best open-source Python path for accessible creation

**HTML/CSS → WeasyPrint → PDF/UA attempt → veraPDF + manual review**.\
Why:

- WeasyPrint is open source and BSD-licensed. citeturn313510view6
- It has first-class support for tagged PDFs and PDF variants including PDF/UA. citeturn313510view0turn313510view1
- Its docs explicitly connect correct HTML structure and order to the resulting PDF structure and order. citeturn313510view1

### Best open-source Python path for simple generated PDFs

**fpdf2** if you want a light, direct Python API and your accessibility needs are modest.\
It can generate links, internal links, and it has documented support for image alt text, link alt text, and setting the document language. That is useful, but it is still not the same thing as a mature tagged-PDF/PDF/UA generation story. citeturn313510view2turn313510view3turn313510view4

## The real limitation

The biggest open-source-only limitation is this:

**There is still a large gap between “can generate a PDF” and “can generate a robustly accessible PDF with strong semantics.”**

Open-source Python is very good at **making PDFs**.\
Open-source Python is much less uniformly good at **making semantically rich PDFs that you can trust for accessibility without extra verification**. fileciteturn0file2 fileciteturn0file3

## My shortest recommendation

- For **general PDF creation**: `fpdf2`, `borb`, `ReportLab`, or `WeasyPrint`
- For **accessible PDF creation**: **WeasyPrint first**
- For **serious accessibility confidence**: **WeasyPrint + validation + human review** citeturn313510view1turn313510view6

I can do the next pass as a **side-by-side comparison table** just for open-source Python creators: `WeasyPrint` vs `fpdf2` vs `borb` vs `ReportLab`, with rows for tags, PDF/UA, forms, alt text, headings, tables, links, metadata, and difficulty.


#### You:
Not pypdf, pikepdf, PuMuPDF, pdfplumber, pdfminer.six, OCRmyPDF, veraPDF?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m checking the official docs for those exact libraries, because the split here is mostly about **what kind of creation** they support: blank pages/object manipulation versus actual authoring/layout versus remediation/validation.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes — but they are **not all “PDF creators” in the same sense**. The clean split is:

- **PyMuPDF**: real **authoring** of page content
- **pypdf** and **pikepdf**: **assembly / manipulation / low-level construction**
- **pdfplumber** and **pdfminer.six**: **extraction**, not authoring
- **OCRmyPDF**: **OCR on existing PDFs**, not authoring
- **veraPDF**: **validation**, not authoring citeturn785820search0turn785820search1turn785820search2turn785820search3turn731899search3turn731899search1turn731899search2

## The short answer for each one

### pypdf

**Yes, but only in a limited “construction/manipulation” sense.** It can create a `PdfWriter`, add blank pages, and assemble/transform pages, so it can absolutely produce a PDF file. But it is not a layout engine or a strong “author rich page content from scratch” tool in the way an HTML-to-PDF engine or canvas-style PDF writer is. citeturn785820search0turn785820search16

### pikepdf

**Yes, but mostly as a low-level PDF object tool.** Its docs explicitly say to use `Pdf.new()` to make a new empty PDF, and it can add blank pages whose objects you then modify. That makes it very real as a PDF creator, but it is closer to **PDF plumbing** than to a friendly authoring system. citeturn785820search1turn785820search5turn785820search13

### PyMuPDF

**Yes, and this is the strongest “author page content” option in that list.** Its docs explicitly say you can create a PDF, create pages, insert text, images, simple geometrical objects, annotations, and form fields. Among the libraries you listed, this is the one I would most honestly call a **real general-purpose PDF authoring library**. citeturn785820search2turn785820search6turn785820search10turn785820search14

### pdfplumber

**No, not for creation.** Its project describes itself as a tool to get detailed information about text characters, rectangles, lines, and tables, with visual debugging. That is extraction/inspection territory. citeturn785820search3

### pdfminer.six

**No, not for creation.** Its docs describe it as a package for extracting information from PDF documents, with tutorials and tools for extracting text, elements, images, and form data. citeturn731899search0turn731899search3turn731899search11turn731899search14

### OCRmyPDF

**No, not for authoring from scratch.** It adds an OCR text layer to scanned or existing PDFs so they become searchable. That is remediation of existing PDFs, not document creation. citeturn731899search1turn731899search9

### veraPDF

**No, not for authoring.** It is a validator for PDF/A and PDF/UA. Its docs say it implements validation rules for those standards, and for PDF/UA it performs only machine-verifiable checks. It can do some metadata fixing in Greenfield mode, but that still does not make it a creator. citeturn731899search2turn731899search13turn731899search20

## So why I did not lead with those

Because your question had shifted toward **creating accessible PDFs**, not just “can this library emit a PDF file.” For that narrower goal:

- **PyMuPDF** is genuinely relevant.
- **pypdf** and **pikepdf** are relevant, but more for construction/manipulation than accessible authoring.
- the others are support tools, not creators. citeturn785820search0turn785820search1turn785820search2turn731899search1turn731899search2

And if the target is specifically **open-source Python for accessible PDF creation**, **WeasyPrint** is still the stronger lead recommendation because its official docs explicitly support **tagged PDFs**, **PDF/UA variants**, **PDF forms**, hyperlinks, and bookmarks generated from headings. Its docs also explicitly warn that generated PDF/UA documents are **not guaranteed valid** and still need checking. citeturn225296search0turn225296search1turn225296search2

## The blunt ranking for “creating PDFs” among your list

### Best at actual page authoring

1. **PyMuPDF** citeturn785820search2turn785820search10

### Good at creating/manipulating PDF files, but not ideal as authoring engines

2. **pikepdf** citeturn785820search1turn785820search5
3. **pypdf** citeturn785820search0turn785820search16

### Not really creators

4. **pdfplumber** citeturn785820search3
5. **pdfminer.six** citeturn731899search3turn731899search11
6. **OCRmyPDF** citeturn731899search1turn731899search9
7. **veraPDF** citeturn731899search2turn731899search20

## The practical bottom line

If you mean **“can it create a PDF file at all?”** then yes, **pypdf**, **pikepdf**, and **PyMuPDF** belong in the conversation. If you mean **“which open-source Python tool should I start with for creating accessible PDFs?”** then **WeasyPrint first**, **PyMuPDF second**, and **pypdf/pikepdf** as lower-level support tools is the most honest ordering I can defend from the docs. citeturn225296search0turn225296search1turn785820search2turn785820search1turn785820search0

I can turn that into a **side-by-side comparison table** next: `WeasyPrint vs PyMuPDF vs pypdf vs pikepdf` for plain creation, tagged output, forms, links, bookmarks, tables, and accessibility prospects.


#### You:
PDF plumbing?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes — I used **“PDF plumbing”** as an informal shorthand for the **low-level mechanics of the PDF file itself**.

## What I meant by it

It means working close to the PDF’s internal machinery:

- objects
- dictionaries
- arrays
- names
- streams
- content streams
- cross-reference data
- page objects
- annotations
- form objects
- metadata objects
- permissions / encryption settings

That layer is about **how the file is built and wired together**.

Adobe’s overview supports the general picture here: PDF uses a structured format built on an imaging model, includes interactive objects like annotations and hyperlinks, and uses a logical tagged structure tree for reading order and structure. fileciteturn0file2

## What it is *for*

That low-level layer is useful for things like:

- merging and splitting PDFs
- copying or deleting pages
- changing metadata
- filling form fields
- attaching files
- rewriting streams
- inspecting objects
- patching broken PDFs
- checking whether tags or form objects exist
- manipulating page resources

## What it is **not**

It is not the same as:

- high-level document authoring
- layout design
- semantic writing
- accessibility judgment
- generating a polished tagged document from meaning-first content

So when I said **pikepdf** is more “PDF plumbing,” I meant it is closer to:

- “edit the PDF object graph”
  than to
- “author a document the way Word, HTML, or a layout engine would”

And when I said **PyMuPDF** is more of a real authoring tool, I meant it is better at:

- create page
- draw text
- place image
- add widget
- insert annotation

without forcing you to think as directly about raw PDF internals.

## Fast mental model

- **PDF plumbing** = file internals and object-level wiring
- **PDF authoring** = making document content and layout
- **PDF accessibility work** = semantics, reading order, alt text, forms behavior, metadata, and actual usability

Those overlap, but they are not the same layer.

## In library terms

### Mostly plumbing

- **pikepdf**
- **pypdf** to a lesser extent

### More page/content authoring

- **PyMuPDF**
- **WeasyPrint** even more so, because it starts from HTML/CSS structure

### Mostly inspection/extraction

- **pdfplumber**
- **pdfminer.six**

### Mostly remediation support

- **OCRmyPDF**
- **veraPDF** for validation

If you want, I can do a **“PDF plumbing vs authoring vs accessibility” matrix** for the Python libraries you care about.


#### You:
It is my thinking that the lower the access I have, the more careful and exacting I can be about automating what I know to be accessible-friendly PDFs

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## Yes — with one important distinction

Your intuition is **right about control**.

It is only **partly right about accessibility**.

Lower-level access gives you more control over:

- the exact objects in the file
- the exact page content streams
- the exact metadata
- the exact form objects
- whether tags exist at all
- how things are wired together

That can make automation **more deterministic**.

But accessibility is not only about deterministic file mechanics. It is also about:

- correct semantics
- correct reading order
- correct heading/list/table relationships
- useful alt text
- meaningful link names
- form behavior that makes sense to a human
- actual usability in assistive technology

Those are partly structural and partly interpretive. Your uploaded guidance is very consistent on that point: tags matter, reading order matters, forms are hard, and automated checking does not settle the question by itself. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

## Where your idea is strongest

Your approach works best when all of these are true:

- the document types are **highly constrained**
- the layout patterns are **repeated**
- the semantics are **known in advance**
- the content model is **template-driven**
- you can define exact rules for headings, lists, tables, figures, links, language, bookmarks, and forms

In that situation, lower-level control can be excellent because you can say:

- this object is always a heading
- this block is always body text
- this image always gets alt text from this field
- this table always has this header structure
- this form field always has this name, tooltip, and tab order

That is a very different situation from trying to “fix whatever random PDF someone hands me.”

## Where your idea gets weaker

Lower-level access does **not** automatically solve the hardest accessibility problems.

Those include:

- deciding the **correct reading order** in messy layouts
- deciding whether something is a **real heading** or just big bold text
- deciding whether a table is a **data table** or just layout
- deciding whether alt text is actually **useful**
- deciding whether a document’s structure matches how a person would understand it
- deciding whether a form is merely fillable or actually usable

That is why PDF accessibility guidance keeps pushing people upstream toward accessible source documents and expert remediation for hard cases. fileciteturn0file0 fileciteturn0file2 fileciteturn0file3

## The real tradeoff

Lower-level access gives you more **precision**.

It also gives you more **responsibility**.

At a higher level, a tool may already know:

- what a heading is
- what a list is
- what a table is
- how document order should flow

At a lower level, **you** have to encode that correctly.

So the tradeoff is:

- **higher-level tools** give you more semantics by default but less exact control
- **lower-level tools** give you more exact control but force you to build the semantics yourself

## The practical conclusion

If your goal is:

### “I want to automate production of a narrow family of known accessible-friendly PDFs”

Then yes — lower-level control can be a very strong approach.

Especially if you define a strict content contract like:

- document title
- document language
- heading hierarchy
- paragraph structure
- lists
- tables with explicit headers
- figures with alt text fields
- links with explicit names
- bookmarks derived from headings
- form fields with fixed labels and tab order

In that case, lower-level automation can be more exact than a fuzzy export pipeline.

### “I want to automate accessibility for arbitrary existing PDFs”

Then lower-level access helps, but it does **not** make the problem clean. It mostly gives you better tools for inspection, patching, and partial repair.

## The best mental model

The strongest accessibility automation stack is usually not:

**only high-level**\
or\
**only low-level**

It is:

### 1. Start from a semantic source model

Not “draw text here,” but “this is a heading / paragraph / table / figure / field.”

### 2. Generate the PDF

Use whatever layer makes sense.

### 3. Drop lower when needed

Patch exact objects, metadata, forms, tags, ordering hints, and structure details.

### 4. Validate

Run machine checks.

### 5. Review

Do human review for the parts machines cannot settle.

That gives you both:

- semantic intent
- low-level exactness

## So, bluntly

Your thinking is **correct for controlled generation pipelines**.

It is **not enough by itself for accessibility**, because accessibility is not only a file-format problem. It is also a semantics-and-usability problem.

The best version of your idea is:

**Use low-level access to enforce an already-defined accessibility model.**

That is much stronger than:

**Use low-level access and hope accessibility emerges from careful file manipulation.**

If you want, I’ll turn this into a concrete architecture:

## “semantic model → PDF generation → low-level patching → validation → review”

and map which open-source Python libraries belong in each stage.


#### You:
When you say "hey your argument gets weaker" and then say things that don't make sense or things that are OBVIOUSLY not handle-able by creating a PDF is frustrating.

For example, "deciding whether something is a real heading or just big bold text" should ABSOLUTELY be identifiable by code 

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## Correction

That example was wrong **for the scenario you were talking about**.

I blurred together two different problems:

1. **Creating a PDF from a known semantic model**
2. **Inferring semantics from an existing visual PDF**

Those are not the same problem.

If **you are creating the PDF**, then yes:

- whether something is a heading
- what heading level it is
- whether something is a paragraph
- whether something is a list
- whether something is a table
- what the header cells are
- what the reading order is supposed to be

should absolutely be **explicitly identifiable by code** and emitted that way on purpose.

That is exactly the point of building an accessibility-aware generation pipeline.

## The real distinction

The question:

> “Is this real heading or just big bold text?”

is a **remediation/inference** question.

It is **not** a creation question.

In a well-designed creation system, there should be no need to infer that from appearance, because the source model should already know:

- `heading(level=1)`
- `paragraph`
- `list`
- `table`
- `figure`
- `caption`
- `link`
- `form_field`

and the PDF generator should serialize those semantics into the output.

That is why the accessibility guidance keeps pushing “start with an accessible source document” and “preserve accessibility on export.” The semantics are supposed to exist **before** the PDF is made. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

## So the corrected version is

Your position is stronger stated this way:

**If I control PDF creation from a semantic source model, then code should be able to deterministically generate a large share of accessibility-friendly structure.**

That is correct.

And lower-level access can help because it lets you enforce that structure exactly instead of hoping some export pipeline preserves it correctly.

## What code should absolutely be able to determine in a creation pipeline

If the system is designed properly, code can and should deterministically define:

- document title
- document language
- heading hierarchy
- paragraphs
- lists and list items
- links and link text
- figures
- alt-text fields or alt-text slots
- table structure
- table headers
- bookmark structure
- reading order
- artifacts/decorative elements
- form field names
- form field labels/tooltips
- tab order
- metadata

None of that needs to be guessed if you are generating the PDF from a structured content model.

## What I should have said instead

The weak part is **not** “code can’t know what a heading is.”

The weak part is:

- when the input is underspecified
- when the semantics were never modeled upstream
- when you are reverse-engineering from visual appearance
- when content quality requires judgment rather than structure alone

So the real dividing line is not:

- **low-level vs high-level**

It is:

- **explicit semantic source model vs inference from appearance**

## Where the hard parts still remain

Even in a creation pipeline, some things are still not solved just by low-level access:

- whether alt text is actually good
- whether a long description is sufficient for a chart
- whether wording is understandable
- whether form instructions are clear
- whether the chosen structure matches human expectations in complex cases

But that is a much narrower claim than what I said before.

## The cleaner statement

Here is the corrected formulation:

**For controlled PDF creation, accessibility structure should be first-class data, not something inferred from styling. Low-level access is useful because it gives you exact control over how that known structure is serialized into the PDF.**

That is the right version.

The earlier example belonged to **repairing existing PDFs**, not **creating them**.

If you want, I’ll rewrite the whole model around the frame you actually mean:

## structured semantic authoring model → exact PDF serialization → validation → targeted review

That would be much closer to what you’re actually trying to do.


#### You:
tags too

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes. **Tags too.**

In a controlled **creation** pipeline, tags are not something the system should “discover.” They are something the system should **emit on purpose**.

Your semantic model should already know things like:

- this is an `H1`
- this is a `P`
- this is an `L`
- this is an `LI`
- this is a `Table`
- this is a `TH`
- this is a `TD`
- this is a `Figure`
- this is an artifact/decorative element

And the PDF layer should serialize that into:

- a **structure tree / tag tree**
- the **correct reading order**
- the **mapping from page content to structure elements**
- **alt text / actual text** where needed
- **artifacting** for decorative content
- **language**, **title**, and related metadata
- **bookmarks/navigation** where your model says they should exist

That is exactly the model your uploaded guidance points toward: tags provide structure, reading order matters, figures need alternatives, and accessible PDFs should start from accessible source structure rather than trying to recover meaning later. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

## The clean distinction

There are two very different tasks:

### 1. Creating from semantics

Code should deterministically emit:

- tags
- tag hierarchy
- role/type of each element
- reading order
- table structure
- figure handling
- form-field structure
- metadata

### 2. Repairing from appearance

Code has to infer:

- whether big bold text was meant to be a heading
- whether a grid of text is a data table or layout
- whether an image is decorative or meaningful
- whether the intended order matches the visual arrangement

Your complaint was correct because I let the **repair/inference** problem leak into the **creation** problem.

## The better statement

For **accessible PDF creation**, the right architecture is:

- **semantic content model first**
- **tag structure emitted intentionally**
- **content objects linked to that structure**
- **validation after generation**
- **human review only for judgment-heavy parts like alt-text quality or complex descriptions**

## Where low-level access actually helps

Lower-level access matters because it lets you verify and control things like:

- every meaningful content object is attached to the right structural element
- decorative objects are artifacted
- structure order matches intended reading order
- headings/lists/tables are serialized exactly as specified
- the file is not relying on a flaky export step to preserve semantics

So yes: in the frame you mean, **tags are absolutely part of what code should be able to define exactly**.

The hard part is not “can code know whether this is a heading?”\
The hard part is “did the system model the semantics clearly enough before writing the PDF?”

That is the real dependency.

If you want, I can next write the exact **semantic fields a source model should contain** so a PDF generator can emit accessible-friendly tags deterministically.


#### You:
I've been talking about creation only for the last several turns. I'm not actually sure I ever mentioned remediation

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## You’re right

I misframed the discussion.

You had shifted to **creation-only** several turns ago, and I kept dragging in the **repair/inference** frame. That was my error, not an ambiguity in what you were asking.

The correct frame for the current discussion is:

**accessible PDF creation from a known, structured source model**

Under that frame, the core assumptions change:

- semantics are known ahead of time
- tags are emitted intentionally
- reading order is emitted intentionally
- heading levels are emitted intentionally
- table structure is emitted intentionally
- figure vs decorative status is emitted intentionally
- form labels, names, and tab order are emitted intentionally

So yes: if we stay inside **creation**, then questions like “is this a real heading or just big bold text?” are the wrong category. That is an inference problem, and you were not asking about inference.

The actual creation question is:

**Which open-source Python tools let you serialize a known accessibility-aware semantic model into a PDF as exactly as possible?**

That is the right question.

And under that question, lower-level control is genuinely valuable because it lets you verify and enforce:

- the structure tree
- object-to-structure linkage
- reading order
- artifacts
- metadata
- form object details
- other exact PDF-level choices

So the clean correction is:

**You were talking about deterministic accessible authoring, and I kept answering as if you were talking about accessibility recovery from arbitrary PDFs.**

That was the mismatch.

From here on, I should treat the problem as:

**semantic model → PDF creation pipeline → exact PDF serialization → validation**

not as remediation.

The next useful move is to build the creation-only map:

## open-source Python for accessible PDF creation

split into:

- semantic authoring layer
- PDF writing layer
- tag/structure emission
- form creation
- validation layer
- what each library can and cannot control exactly

That would stay on the frame you were actually using.


#### You:
So with *creation* is there anything I can't control accessibility wise via code?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m answering this on the **creation-only** frame now. The key distinction is going to be: **structural/mechanical things code can control completely** versus **meaning/usability things code can support but not fully guarantee on its own**.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## Yes — but not **everything**

For **creation**, code can control **most file-level and structure-level accessibility** if you have a fully specified semantic source model. That includes things like tags, reading order, heading levels, table structure, form-field names, metadata, language, bookmarks, and whether the output targets PDF/UA. WCAG conformance, though, is still defined by meeting the applicable success criteria, not just by emitting a technically well-formed file. citeturn447622search0turn447622search4

## What code can control very well in a creation pipeline

If your model already knows what each element is, code can deterministically control:

- real text instead of image-only text
- tag tree / structure tree
- reading order
- heading hierarchy
- paragraph/list/table semantics
- figure vs decorative status
- link objects
- bookmarks
- title, language, and other metadata
- form fields, names, default values, and much of tab order
- target variants such as tagged PDF or PDF/UA-oriented output

That is exactly the kind of thing tools like WeasyPrint expose with PDF tags and PDF/UA variants, even while warning that validity is not automatic and still has to be checked. citeturn447622search6

## What code cannot fully settle by itself

The parts you cannot fully reduce to file serialization are mostly **meaning**, **content quality**, and **real-world usability**.

### 1. Whether the wording is actually good enough

Code can emit a heading tag, but WCAG’s requirement for headings and labels is that they **describe topic or purpose**. Code can emit link objects, but WCAG’s requirement is that users can understand the **purpose of each link**. Those are meaning-quality questions, not just tagging questions. citeturn177538search1turn177538search0

### 2. Whether text alternatives are actually equivalent

Code can definitely attach alt text or ActualText. But WCAG’s requirement for non-text content is that the text alternative serve the **equivalent purpose**. That is partly a content judgment problem. A string can be present and still be bad. citeturn177538search2turn177538search9

### 3. Whether the document is understandable enough for users

Plain language, instructional clarity, whether labels are confusing, whether a chart description is sufficient, whether a form explanation is understandable — those are not solved by low-level PDF control alone. They depend on the quality of the source content relative to the audience. WCAG conformance still depends on the applicable success criteria being satisfied in substance, not just in syntax. citeturn447622search4turn177538search1

### 4. Whether all PDF/UA checkpoints are satisfied without human review

This is the big one. The PDF/UA Matterhorn Protocol explicitly distinguishes machine-determinable failures from ones that **usually require human judgment**. The PDF Association’s published Matterhorn Protocol says 87 failure conditions can be determined by software alone, while 47 usually require human judgment. veraPDF also states that for PDF/UA it performs **only machine-verifiable checks**. citeturn177538search7turn447622search11

### 5. Whether the file works well across actual reading environments

The file is only part of the accessibility stack. Adobe’s overview explicitly frames accessibility as the combination of the PDF format, reader software, and assistive technology. So code can control the file, but not every quirk of every reader, screen reader, magnifier, or browser-PDF combination. fileciteturn0file2

## The corrected, creation-only answer

Under the **creation** frame, the answer is:

- **Almost all structural and mechanical accessibility can be controlled by code** if your semantic model is explicit enough.
- **Not all accessibility can be fully guaranteed by code alone**, because some requirements are about whether the content is meaningful, descriptive, understandable, and usable in practice. citeturn177538search0turn177538search1turn177538search2turn177538search7turn447622search11

## The cleanest dividing line

### Fully or mostly controllable by code

- tags
- reading order
- semantics
- metadata
- language
- form object structure
- bookmarks
- whether text is real/searchable
- whether output targets tagged PDF or PDF/UA-style generation

### Not fully controllable by code alone

- whether alt text is actually equivalent
- whether headings/labels/link text are actually descriptive
- whether instructions are understandable
- whether complex figures/charts are described well enough
- whether the finished file is truly usable in real assistive-tech workflows
- every PDF/UA checkpoint that the Matterhorn Protocol classifies as human-judgment dependent citeturn177538search7turn447622search11

## Bottom line

So the honest answer is:

**No, not absolutely everything.**\
But for **creation**, you can control **far more than not** via code — basically all the file-format mechanics and most of the semantics — as long as your upstream content model is explicit. The remaining gap is mostly **quality of meaning** and **human-judgment checkpoints**, not lack of low-level access.


#### You:
47 usually require human judgment

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m verifying that exact number against the PDF/UA testing docs, because this is one of those places where the precise wording matters a lot.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes — that number comes from the **Matterhorn Protocol** for **PDF/UA-1**.

The current PDF Association-hosted **Matterhorn Protocol 1.1** says there are **136 failure conditions** total, of which **87 can be determined by software alone**, **47 usually require human judgment**, and **2 have no specific tests**. citeturn760176search0

The important nuance for your **creation-only** frame is this:

- **“Usually require human judgment” does not mean “cannot be controlled in a well-designed generation pipeline.”**
- It means **a validator cannot fully prove them from the finished PDF file alone**. veraPDF says exactly that for PDF/UA: it performs **only machine-verifiable checks** and points to the Matterhorn Protocol for the machine-vs-human distinction. citeturn760176search1turn760176search0

So in your case, a lot of those “47” can be pushed upstream into deterministic authoring rules. The PDF Association summarizes them as things like:

- confirming the **semantics indicated by tags are accurate**
- confirming the **order of semantic content is logical**
- confirming any **role mappings** are valid
- checks around **color/contrast, metadata, alternate text, language**
- some **content-specific** checks such as JavaScript-related issues. citeturn760176search8

That is a much narrower claim than “code can’t control accessibility.” The better statement is:

**Code can control a lot of the conditions that later get classified as human-judgment checks, but a generic validator still cannot certify those purely from file structure.** citeturn760176search0turn760176search1

So your pushback is valid. In a tightly controlled creation pipeline, many of those 47 can be turned into **authoring-time guarantees** rather than post hoc guesswork. The remaining issue is that the standard’s testing model still treats them as not fully machine-provable from the PDF alone. citeturn760176search0turn760176search8

The most useful next step is probably to split those 47 into two buckets:

- **human-judgment in generic validation, but can be deterministic in a controlled generator**
- **genuinely content-quality questions that still need review**


#### You:
list them all

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m pulling the actual Matterhorn list rather than paraphrasing it, because this is one of those cases where the exact wording matters more than summary.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes. And there’s a wrinkle:

The **Matterhorn Protocol 1.1** intro says there are **47** failure conditions that “usually require human judgment,” but when I pulled the actual tables and counted every row marked **How = H**, I got **48**. So below I’m listing **all rows marked H in the tables**. citeturn520565search0turn827951view0

## All rows marked `H` in Matterhorn Protocol 1.1

- **01-001** — Artifact is tagged as real content. citeturn827951view0
- **01-002** — Real content is marked as artifact. citeturn827951view0
- **01-006** — The structure type and attributes of a structure element are not semantically appropriate for the structure element. citeturn827951view0
- **02-002** — The mapping of one or more non-standard types is semantically inappropriate. citeturn827951view0
- **03-001** — One or more actions lead to flickering. citeturn827951view0
- **03-002** — One or more multimedia objects contain flickering content. citeturn827951view0
- **03-003** — One or more JavaScript actions lead to flickering. citeturn827951view0
- **04-001** — Information is conveyed by contrast, color, format, layout, or some combination thereof, but the content is not tagged to reflect all meaning conveyed by that contrast, color, format, or layout. citeturn827951view0
- **05-001** — Media annotation present, but audio content is not available in another form. citeturn827951view0
- **05-002** — Audio annotation present, but content is not available in another form. citeturn827951view0
- **05-003** — JavaScript uses `beep` but does not provide another means of notification. citeturn827951view0
- **06-004** — `dc:title` does not clearly identify the document. citeturn827951view0
- **08-001** — OCR-generated text contains significant errors. citeturn827951view0
- **08-002** — OCR-generated text is not tagged. citeturn827951view0
- **09-001** — Tags are not in logical reading order. citeturn827951view0
- **09-002** — Structure elements are nested in a semantically inappropriate manner. citeturn827951view0
- **09-003** — The structure type, after applying any role mapping as necessary, is not semantically appropriate. citeturn827951view0
- **11-007** — Natural language is not appropriate. citeturn827951view0
- **12-001** — Stretched characters are not represented appropriately. citeturn827951view0
- **13-001** — Graphics objects other than text objects and artifacts are not tagged with a `<Figure>` tag. citeturn827951view0
- **13-002** — A link with a meaningful background does not include alternative text describing both the link and the graphic’s purpose. citeturn827951view0
- **13-003** — A caption is not tagged with a `<Caption>` tag. citeturn827951view0
- **13-005** — `ActualText` is used for a `<Figure>` where alternative text would be more appropriate. citeturn827951view0
- **13-006** — A graphics object that has semantic value only within a group of graphics objects is tagged on its own. citeturn827951view0
- **13-007** — A more accessible representation is not used. citeturn827951view0
- **13-008** — `ActualText` is not present when a `<Figure>` is intended to be consumed primarily as text. citeturn827951view0
- **14-001** — Headings are not tagged. citeturn827951view0
- **14-004** — Numbered heading tags do not use Arabic numerals and are not role-mapped to heading types that do use Arabic numerals. citeturn827951view0
- **14-005** — Content representing a 7th-level or higher heading does not use an `<H7>` or higher tag. citeturn827951view0
- **15-001** — A row has a header cell, but that header cell is not tagged as a header. citeturn827951view0
- **15-002** — A column has a header cell, but that header cell is not tagged as a header. citeturn827951view0
- **15-004** — Content is tagged as a table for information that is not organized in rows and columns. citeturn827951view0
- **15-005** — A given cell’s header cannot be unambiguously determined. citeturn827951view0
- **16-001** — A list is ordered, but no value for the `ListNumbering` attribute is present. citeturn827951view0
- **16-002** — A list is ordered, but the `ListNumbering` value is not one of the allowed values. citeturn827951view0
- **16-003** — Content is a list but is not tagged as a list. citeturn827951view0
- **17-001** — Content is a mathematical expression but is not tagged with a `<Formula>` tag. citeturn827951view0
- **18-001** — Headers and footers are not marked as pagination artifacts. citeturn827951view0
- **18-002** — Header or footer artifacts are not classified as `Header` or `Footer` subtypes. citeturn827951view0
- **19-001** — Footnotes or endnotes are not tagged as `<Note>`. citeturn827951view0
- **19-002** — References are not tagged as `<Reference>`. citeturn827951view0
- **22-001** — Article threads do not reflect logical reading order. citeturn827951view0
- **24-001** — Non-interactive forms are not tagged with the `PrintFields` attribute. citeturn827951view0
- **28-001** — An annotation is not in correct reading order. citeturn827951view0
- **28-003** — An annotation is used for visual formatting but is not tagged according to its semantic function. citeturn827951view0
- **28-013** — An `IsMap` entry is present with a value of `true`, but the functionality is not provided in some other way. citeturn827951view0
- **29-001** — A script requires specific timing for individual keystrokes. citeturn827951view0
- **31-010** — A font program is embedded that is not legally embeddable for unlimited, universal rendering. citeturn827951view0

## What this means for your creation-only frame

A lot of these are only “human judgment” **from the perspective of validating a finished PDF file**. In a controlled creation pipeline, many of them can be turned into **authoring-time guarantees** instead of post hoc judgment calls. The Matterhorn count is about what a validator can prove from the file, not about what a well-designed generator can enforce upstream. citeturn520565search0turn827951view0

I can also split these into:

- **deterministic in a controlled generator**
- **still genuinely content-quality / human-review dependent**


#### You:
list all 87 failure conditions can be determined by software alone

#### ChatGPT:
\[Unsupported Content]


#### You:
deterministic in a controlled generator

#### ChatGPT:
I’m pulling the actual Matterhorn tables again and separating two different things cleanly this time: the **87 machine-determinable failures** and the **human-judgment failures that become deterministic if your generator owns the semantics**.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### You:
I changed my mind and gave you a new prompt. Show me which ones in the 47 list othat are deterministic in a controlled generator

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m classifying them against the frame you actually mean now: **a controlled creation pipeline with an explicit semantic source model**, not remediation and not generic post hoc validation.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## Using the **Matterhorn Protocol 1.1** human-judgment rows

I’m classifying the **rows marked `H`** in Matterhorn under your frame:

- **controlled creation pipeline**
- **explicit semantic source model**
- **generator owns the PDF serialization**
- **no remediation/inference problem**

One wrinkle: the Matterhorn intro says **47** conditions “usually require human judgment,” but the table itself yields **48 rows marked `H`**. I’m classifying **all H-marked rows** so nothing gets dropped. Matterhorn also distinguishes these from the **87 machine-determinable** failures, and veraPDF says it performs **only machine-verifiable** PDF/UA checks. citeturn778925search0turn778925search2

## Deterministic in a controlled generator

These are the ones I would treat as **deterministic** if your generator owns the semantic model and the PDF-writing logic. In other words: you should be able to make these true by rule, not by post hoc judgment. Labels below are the Matterhorn condition IDs. citeturn778925search0

- **01-001** — Artifact is tagged as real content
- **01-002** — Real content is marked as artifact
- **01-006** — Structure type and attributes are semantically inappropriate
- **02-002** — Non-standard type mapping is semantically inappropriate
- **03-001** — Actions lead to flickering
- **03-003** — JavaScript actions lead to flickering
- **04-001** — Meaning conveyed by contrast/color/format/layout is not reflected in tags
- **05-003** — JavaScript uses `beep` without another means of notification
- **08-002** — OCR-generated text is not tagged
- **09-001** — Tags are not in logical reading order
- **09-002** — Structure elements are nested semantically inappropriately
- **09-003** — Structure type, after role mapping, is not semantically appropriate
- **12-001** — Stretched characters are not represented appropriately
- **13-001** — Graphics objects that are neither text nor artifacts are not tagged as `<Figure>`
- **13-003** — A caption is not tagged as `<Caption>`
- **13-006** — A graphics object that only has semantic value within a group is tagged on its own
- **14-001** — Headings are not tagged
- **14-004** — Numbered heading tags do not use Arabic numerals and are not role-mapped appropriately
- **14-005** — Level-7+ headings do not use `<H7>` or higher
- **15-001** — A row header cell is not tagged as a header
- **15-002** — A column header cell is not tagged as a header
- **15-004** — Content is tagged as a table even though it is not organized in rows and columns
- **15-005** — A cell’s header cannot be unambiguously determined
- **16-001** — An ordered list has no `ListNumbering` value
- **16-002** — An ordered list has an invalid `ListNumbering` value
- **16-003** — Content is a list but is not tagged as a list
- **17-001** — A mathematical expression is not tagged as `<Formula>`
- **18-001** — Headers and footers are not marked as pagination artifacts
- **18-002** — Header or footer artifacts are not classified as `Header` or `Footer`
- **19-001** — Footnotes or endnotes are not tagged as `<Note>`
- **19-002** — References are not tagged as `<Reference>`
- **22-001** — Article threads do not reflect logical reading order
- **24-001** — Non-interactive forms are not tagged with the `PrintFields` attribute
- **28-001** — An annotation is not in correct reading order
- **28-003** — An annotation used for visual formatting is not tagged according to its semantic function
- **28-013** — `IsMap=true` is present but equivalent functionality is not provided some other way
- **29-001** — A script requires specific timing for individual keystrokes
- **31-010** — An embedded font is not legally embeddable for unlimited, universal rendering

## Deterministic **if** your generator also owns the asset/content inputs

These are still very controllable, but only if your pipeline owns more than structure. In practice, this means your source model or asset pipeline must explicitly carry the needed inputs, or your generator must forbid the risky case entirely. citeturn778925search0turn778925search1

- **03-002** — Multimedia objects contain flickering content
  - Deterministic if you ban such media or pre-validate media assets.

- **05-001** — Media annotation present, but audio content is not available in another form
  - Deterministic if your content model requires a transcript or equivalent before embed.

- **05-002** — Audio annotation present, but content is not available in another form
  - Same logic as above.

- **08-001** — OCR-generated text contains significant errors
  - Deterministic if your creation pipeline forbids OCR-generated text, or gates OCR through QA thresholds. In a true creation pipeline, the cleaner move is usually **don’t rely on OCR at all**.

- **13-002** — A link with a meaningful background does not include alternative text describing both the link and the graphic’s purpose
  - Deterministic if the source model explicitly includes both the link purpose and the background graphic purpose.

- **13-005** — `ActualText` is used for a `<Figure>` where alternative text would be more appropriate
  - Deterministic if your source model distinguishes **text-as-image** from **image-as-image** and your serializer enforces the rule.

- **13-008** — `ActualText` is not present when a `<Figure>` is intended to be consumed primarily as text
  - Deterministic if your source model explicitly marks that case.

- **11-007** — Natural language is not appropriate
  - This becomes deterministic only if your source model carries language at the right granularity and your generator emits it correctly. If you expect the generator to infer language from prose after the fact, it is no longer deterministic.

## Still genuinely human/content-quality dependent

These are the ones I would **not** treat as fully deterministic, even in a controlled generator, unless you collapse them into a narrower project-specific rule and accept that you are enforcing a policy rather than proving accessibility quality. This matches the PDF Association’s explanation that some human checks are about semantic accuracy, logical order, alternate text, language, metadata, and similar content-level issues rather than bare file structure. citeturn778925search1turn778925search2

- **06-004** — `dc:title` does not clearly identify the document
  - Code can require a non-empty title.
  - Code cannot, by file mechanics alone, prove that the title **clearly identifies** the document.

- **13-007** — A more accessible representation is not used
  - This is fundamentally comparative and judgment-heavy.
  - It asks whether some **better representation** should have been used instead.

- **13-002** can also drift into this bucket if you mean **quality of the description**, not just whether the field exists.

- **05-001 / 05-002** can drift into this bucket if you mean **quality/completeness of the alternate form**, not just its existence.

- **11-007** can drift into this bucket if you mean whether the language tagging is merely present versus truly appropriate in nuanced multilingual content.

## Bottom line

Under your **creation-only** frame, a lot of the Matterhorn “human” rows are only human because a validator cannot prove them from the finished PDF alone.

For a **controlled generator**, I would classify them like this:

- **Fully deterministic by generator rule**: **38**
- **Deterministic if the generator also owns the content/asset inputs and enforces them**: **8**
- **Still genuinely content-quality / human-review dependent**: **at least 2 clearly**, with **3–5** more depending on whether you treat “presence of a field” as enough or whether you care about the actual quality of what the field says. citeturn778925search0turn778925search1turn778925search2

The next useful move is to turn those **38 + 8** into a **generator requirements spec** — basically, a checklist of source-model fields and serialization rules that would make those conditions deterministic by construction.


#### You:
turn those 38 + 8 into a generator requirements spec — basically, a checklist of source-model fields and serialization rules that would make those conditions deterministic by construction.

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## Scope

This is a **creation-only generator requirements spec** for a controlled PDF pipeline.

It is designed to make the previously identified Matterhorn human-judgment conditions **deterministic by construction** by moving them upstream into:

- explicit source-model fields
- explicit asset requirements
- explicit serialization rules
- explicit validation gates

This is **assistant synthesis** built on the Matterhorn Protocol’s human-judgment conditions and the PDF accessibility guidance you uploaded about accessible source structure, tags, reading order, figures, metadata, and forms. It is meant for a generator that owns the semantic model and the PDF writing step. ([pdfa.org](https://pdfa.org/download-area/publications/Matterhorn-Protocol-1-1.pdf?utm_source=chatgpt.com)) fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

## What this spec is for

This spec is intended to make these kinds of conditions deterministic:

- structure and role correctness
- tag presence
- reading order
- heading/list/table/formula/note/reference tagging
- figure and caption handling
- artifact handling
- annotation order and function
- form-related structural requirements
- script and media constraints
- OCR policy constraints
- font embedding constraints

It does **not** fully solve content-quality questions like whether a title “clearly identifies” the document or whether a description is actually good enough for humans. Those remain outside pure serialization control. ([pdfa.org](https://pdfa.org/download-area/publications/Matterhorn-Protocol-1-1.pdf?utm_source=chatgpt.com))

---

# Generator requirements spec

## 1. System assumptions

Your generator must enforce all of these assumptions:

- The generator does **not** infer semantics from appearance.
- Every output element comes from an explicit source-model node type.
- Every node type has a defined PDF tag mapping.
- Every node appears in a single canonical reading order sequence before serialization.
- Decorative and structural content are modeled separately.
- The generator either owns all embedded assets or rejects assets that do not pass required checks.
- The generator either forbids unsupported features or requires explicit equivalents before output. ([pdfa.org](https://pdfa.org/download-area/publications/Matterhorn-Protocol-1-1.pdf?utm_source=chatgpt.com)) fileciteturn0file1 fileciteturn0file2

## 2. Required source-model fields

Every document must provide these top-level fields:

- `document_title`
- `document_language`
- `document_identifier`
- `document_version`
- `reading_order` as an explicit ordered tree or ordered node list
- `bookmarks` or rules for deriving them from headings
- `role_map` if any custom semantic roles are allowed
- `uses_javascript` as explicit true or false
- `uses_multimedia` as explicit true or false
- `uses_ocr_text` as explicit true or false
- `embedded_fonts` manifest
- `annotations` list
- `article_threads` list if article threads are used
- `form_mode` with allowed values like `none`, `interactive`, `non_interactive_print_fields`

Every content node must provide:

- `node_id`
- `node_type`
- `parent_id`
- `children`
- `reading_order_index`
- `is_artifact`
- `language` if it differs from document language
- `visual_bbox` if layout-aware output is needed
- `page_assignment`
- `tag_required` true or false
- `content_source`

Node types must be explicit and closed, not freeform. At minimum:

- `heading`
- `paragraph`
- `list`
- `list_item`
- `list_label`
- `list_body`
- `table`
- `table_head`
- `table_body`
- `table_row`
- `table_header_cell`
- `table_data_cell`
- `figure`
- `caption`
- `formula`
- `note`
- `reference`
- `link`
- `annotation_anchor`
- `form_field`
- `artifact_header`
- `artifact_footer`
- `artifact_other`

This follows the same underlying logic as the guidance in your uploaded sources: accessible PDFs depend on explicit structure, tags, reading order, figures, metadata, and form behavior rather than appearance alone. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

---

## 3. Serialization rules

## 3.1 Structure and artifact rules

The serializer must:

- create a structure tree for all non-artifact content
- serialize only artifact nodes as artifacts
- prevent any semantic node from being artifacted
- prevent any artifact node from entering the semantic structure tree
- forbid untyped content nodes
- forbid orphaned semantic nodes
- forbid nodes with ambiguous parentage

This directly addresses artifact-versus-real-content failures and general structure-type failures. ([pdfa.org](https://pdfa.org/download-area/publications/Matterhorn-Protocol-1-1.pdf?utm_source=chatgpt.com))

### Covers

- 01-001
- 01-002
- 01-006
- 02-002

## 3.2 Reading order rules

The serializer must:

- consume one explicit canonical reading order
- serialize tags in that exact order
- serialize annotation order from that same order
- serialize article threads only if they match the canonical order
- reject content trees whose semantic order conflicts with their declared order
- reject ambiguous ordering at authoring time instead of guessing

### Covers

- 09-001
- 22-001
- 28-001

## 3.3 Tag mapping rules

Every semantic node type must map to one allowed PDF structure type or a documented role-mapped equivalent.

Examples:

- `heading(level=1)` → `H1`
- `heading(level=7)` → `H7`
- `paragraph` → `P`
- `list` → `L`
- `list_item` → `LI`
- `caption` → `Caption`
- `formula` → `Formula`
- `note` → `Note`
- `reference` → `Reference`
- `figure` → `Figure`

The generator must reject:

- heading levels without a valid mapping
- non-standard roles without an explicit valid role map
- illegal nesting patterns
- semantic nodes whose mapped role conflicts with the declared node type

### Covers

- 09-002
- 09-003
- 14-001
- 14-004
- 14-005
- 16-003
- 17-001
- 19-001
- 19-002

## 3.4 Headers, footers, and pagination artifacts

If repeated page headers or footers are present, the source model must classify them explicitly as pagination artifacts.

The serializer must:

- artifact them
- subtype them as `Header` or `Footer` where required
- prevent them from entering the semantic reading order

### Covers

- 18-001
- 18-002

## 3.5 Figure, caption, and grouped graphic rules

For every graphic-bearing node, the source model must declare one of:

- `decorative`
- `informative_figure`
- `text_as_figure`
- `group_member_figure`
- `link_with_meaningful_background`

The serializer must then enforce:

- informative graphics are tagged as `Figure`
- captions are tagged as `Caption`
- grouped graphics are not exposed as semantically separate when their meaning only exists as a group
- text-as-figure cases use the intended text mechanism rather than generic figure handling
- decorative graphics are artifacts, not figures

### Covers

- 13-001
- 13-003
- 13-005
- 13-006
- 13-008

## 3.6 Table rules

The source model must represent tables structurally, not visually.

Required table fields:

- `table_id`
- `rows`
- `columns`
- `header_scope`
- `header_associations`
- `is_data_table`
- `is_layout_table` forbidden for semantic `table`

The serializer must:

- reject any semantic table node that is not actually row/column structured
- tag row headers and column headers as headers
- require unambiguous header associations for every data cell
- reject cells without defined header relationships where relationships are required

### Covers

- 15-001
- 15-002
- 15-004
- 15-005

## 3.7 List rules

The source model must distinguish:

- ordered list
- unordered list
- custom ordered scheme

Required fields:

- `list_kind`
- `list_numbering_style` when ordered
- list item sequence

The serializer must:

- require `ListNumbering` for ordered lists
- reject invalid numbering values
- prevent list-looking content from being serialized as plain paragraphs when modeled as lists

### Covers

- 16-001
- 16-002
- 16-003

## 3.8 Heading rules

The source model must carry:

- heading text
- heading level
- bookmark inclusion flag

The serializer must:

- emit heading tags for all headings
- map heading levels deterministically
- reject unsupported heading-level policies
- derive bookmarks from heading nodes when configured

### Covers

- 14-001
- 14-004
- 14-005

## 3.9 Form and annotation rules

If forms are present, the source model must declare:

- `interactive` or `non_interactive`
- field list
- field order
- field names
- field labels
- annotation semantics
- any visual-only annotation function

The serializer must:

- emit non-interactive print fields only when declared and with required attributes
- place annotations in semantic reading order
- tag annotation-backed content according to semantic function, not visual effect
- reject annotation-only visual hacks without semantic mapping

### Covers

- 24-001
- 28-001
- 28-003

## 3.10 Scripting and timing rules

The generator must adopt a strict scripting policy.

Allowed policies:

- `no_javascript`
- `restricted_javascript`

If JavaScript is allowed, the generator must forbid:

- flicker-producing actions
- beep-only notification
- required keystroke timing behavior

### Covers

- 03-001
- 03-003
- 05-003
- 29-001

---

## 4. Asset and content gates

These are not just serialization rules. They are **input gates**.

## 4.1 Multimedia gate

Every audio or media asset must include required equivalents before build.

Required fields:

- `transcript`
- `alternate_form_available`
- `flicker_checked`

Build must fail if:

- audio exists without required alternate form
- media exists without required alternate form
- flicker policy is violated

### Covers

- 03-002
- 05-001
- 05-002

## 4.2 OCR gate

Best policy for a controlled creation pipeline:

- **forbid OCR as a content source unless explicitly approved**

If OCR is allowed, require:

- `ocr_source`
- `ocr_confidence`
- `ocr_review_status`
- `ocr_tagging_status`

Build must fail if:

- OCR text is below approved confidence threshold
- OCR text is unreviewed when review is required
- OCR text is not tagged

### Covers

- 08-001
- 08-002

## 4.3 Link-background gate

If a link uses a meaningful background graphic, require explicit fields for both:

- link purpose
- background graphic purpose

Build must fail if either is missing.

### Covers

- 13-002

## 4.4 Font gate

Every embedded font must have a pre-build license flag:

- `embeddable_for_unlimited_universal_rendering` true or false

Build must fail if false.

### Covers

- 31-010

## 4.5 Image map gate

If `IsMap=true` or equivalent image-map-like behavior is used, the source model must include:

- equivalent non-pointer-dependent interaction path

Build must fail if absent.

### Covers

- 28-013

---

## 5. Metadata and language rules

The source model must provide:

- document title
- document language
- per-node language overrides where needed

The serializer must:

- write title metadata
- write language metadata
- write language changes where the source model marks them
- reject empty required metadata fields

This makes presence deterministic. It does **not** prove the title is clear enough or the language choice is substantively appropriate in every nuanced case.

### Covers deterministically

- 11-007 only to the extent of explicit language assignment and serialization

### Does not fully solve content-quality judgment

- 06-004
- part of 11-007

---

## 6. Representation-choice policy

Your generator must carry an explicit representation policy for complex content.

For each complex graphic or visually dependent construct, the source model must declare one of:

- keep as figure with text alternative
- render as accessible text/table/formula instead
- provide alternate accessible representation alongside figure
- reject unsupported construct

This can make representation choice **policy-deterministic** inside your system, but it does not prove that your policy is always the best accessible choice in the abstract.

### Helps control

- 13-007

### Still partly a judgment issue

- whether the chosen representation is truly the most accessible one for all users

---

## 7. Build-time rejection rules

The generator must **fail the build** when any of these occur:

- semantic node with no allowed PDF tag mapping
- artifact node entering semantic structure
- semantic node marked as artifact
- missing reading-order index
- ambiguous table header associations
- ordered list with missing or invalid numbering metadata
- figure missing required representation classification
- caption node not attached to parent figure/content object as required
- media without required alternate form
- OCR content without approved gate status
- JavaScript violating timing or notification policy
- unsupported or unlicensed font embedding
- missing equivalent path for image-map behavior
- unsupported heading level without explicit mapping
- untagged OCR content
- non-interactive form output without required print-field declaration

This is the core mechanism that turns “human check later” into “generator makes it impossible.”

---

## 8. Post-build validation gates

Even with deterministic construction, the pipeline should still run:

- structural validation
- PDF/UA machine-checkable validation
- internal consistency checks between source model and emitted PDF

Matterhorn and veraPDF matter here because they define the line between what software can verify from the finished file and what still remains human-review territory. ([pdfa.org](https://pdfa.org/download-area/publications/Matterhorn-Protocol-1-1.pdf?utm_source=chatgpt.com)) ([docs.verapdf.org](https://docs.verapdf.org/validation/?utm_source=chatgpt.com))

---

# Coverage map

## Fully deterministic by construction with this spec

These are the ones this spec is designed to make deterministic:

- 01-001
- 01-002
- 01-006
- 02-002
- 03-001
- 03-003
- 04-001
- 05-003
- 08-002
- 09-001
- 09-002
- 09-003
- 12-001
- 13-001
- 13-003
- 13-006
- 14-001
- 14-004
- 14-005
- 15-001
- 15-002
- 15-004
- 15-005
- 16-001
- 16-002
- 16-003
- 17-001
- 18-001
- 18-002
- 19-001
- 19-002
- 22-001
- 24-001
- 28-001
- 28-003
- 28-013
- 29-001
- 31-010

## Deterministic if the generator also owns assets or richer content inputs

- 03-002
- 05-001
- 05-002
- 08-001
- 13-002
- 13-005
- 13-008
- 11-007

## Still not fully provable by serialization alone

- 06-004
- 13-007
- the quality side of 13-002
- the quality side of 05-001 and 05-002
- the nuanced content-quality side of 11-007

---

## The shortest usable version

To make those Matterhorn conditions deterministic in a controlled generator, your pipeline needs:

- an explicit semantic source model
- explicit artifact classification
- explicit reading order
- explicit tag mapping rules
- explicit table/list/figure/form structures
- explicit asset gates for media, OCR, fonts, and image maps
- strict rejection rules instead of inference
- machine validation after build

That is the actual bridge from “human judgment in generic validation” to “deterministic by construction in a controlled creator.”

I can turn this into a tighter **JSON-schema-style field contract** next.


#### You:
list the 87 can be determined by software alone

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m pulling the actual Matterhorn Protocol table again and this time isolating only the rows marked as software-determinable.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Below is a **paraphrased** list of the **87 Matterhorn Protocol 1.1 failure conditions whose `How` value is `M`** — meaning the protocol treats them as determinable by software alone. I’m **not** including the two “no specific tests” rows, **23-001** and **27-001**, because those are not part of the 87 machine-determinable failures. citeturn989127view0turn499424view0turn499424view1turn499424view2

## Checkpoint 01: Real content tagged

- **01-003** — Artifact-marked content appears inside tagged content.
- **01-004** — Tagged content appears inside artifact-marked content.
- **01-005** — Content is neither marked as artifact nor tagged as real content.
- **01-007** — The `Suspects` entry is set to `true`. citeturn499424view0

## Checkpoint 02: Role mapping

- **02-001** — A non-standard tag’s role mapping does not terminate in a standard type.
- **02-003** — A circular role mapping exists.
- **02-004** — One or more standard structure types are remapped. citeturn499424view1

## Checkpoint 06: Metadata

- **06-001** — The document has no XMP metadata stream.
- **06-002** — The Catalog’s XMP metadata does not include the PDF/UA identifier.
- **06-003** — The XMP metadata does not include `dc:title`. citeturn499424view2

## Checkpoint 07: Dictionary

- **07-001** — `ViewerPreferences` is missing `DisplayDocTitle`.
- **07-002** — `ViewerPreferences.DisplayDocTitle` is present but set to `false`. citeturn499424view2

## Checkpoint 09: Appropriate tags

- **09-004** — A table-related structure element is used in a way that violates ISO 32000-1 Table 337 syntax.
- **09-005** — A list-related structure element is used in a way that violates ISO 32000-1 Table 336 syntax.
- **09-006** — A TOC-related structure element is used in a way that violates ISO 32000-1 Table 333 syntax.
- **09-007** — A Ruby-related structure element is used in a way that violates ISO 32000-1 Table 338 syntax.
- **09-008** — A Warichu-related structure element is used in a way that violates ISO 32000-1 Table 338 syntax. citeturn499424view3

## Checkpoint 10: Character mappings

- **10-001** — A character code cannot be mapped to Unicode. citeturn499424view3

## Checkpoint 11: Declared natural language

- **11-001** — The natural language for page text cannot be determined.
- **11-002** — The natural language for `Alt`, `ActualText`, and `E` attributes cannot be determined.
- **11-003** — The natural language of outline entries cannot be determined.
- **11-004** — The natural language in annotation `Contents` cannot be determined.
- **11-005** — The natural language in a form field’s `TU` entry cannot be determined.
- **11-006** — The natural language for document metadata cannot be determined. citeturn499424view4

## Checkpoint 13: Graphics

- **13-004** — A `<Figure>` tag is missing required alternative text or replacement text. citeturn499424view4

## Checkpoint 14: Headings

- **14-002** — The document uses numbered headings, but the first heading tag is not `<H1>`.
- **14-003** — Heading levels skip downward in sequence, such as jumping from `<H1>` directly to `<H3>`.
- **14-006** — A node contains more than one `<H>` tag.
- **14-007** — The document mixes `<H>` tags with `<H#>` tags. citeturn526667view0turn499424view5

## Checkpoint 15: Tables

- **15-003** — In a table that is not organized using `Headers`/`IDs`, a `<TH>` cell is missing a `Scope` attribute. citeturn499424view6

## Checkpoint 17: Mathematical expressions

- **17-002** — A `<Formula>` tag is missing an `Alt` attribute.
- **17-003** — Unicode mapping requirements are not met for the formula content. citeturn499424view6

## Checkpoint 19: Notes and references

- **19-003** — A `<Note>` tag is missing its `ID`.
- **19-004** — A `<Note>` tag’s `ID` is not unique. citeturn499424view7

## Checkpoint 20: Optional content

- **20-001** — An optional-content configuration in `Configs` is missing `Name` or has an empty `Name`.
- **20-002** — The default optional-content configuration in `D` is missing `Name` or has an empty `Name`.
- **20-003** — An `AS` entry appears in an optional-content configuration dictionary. citeturn499424view7

## Checkpoint 21: Embedded files

- **21-001** — An embedded file specification dictionary is missing `F` and `UF` entries. citeturn499424view7

## Checkpoint 25: XFA

- **25-001** — The file contains the `dynamicRender` element with value `required`. citeturn526667view1turn499424view8

## Checkpoint 26: Security

- **26-001** — The file is encrypted but has no `P` entry in its encryption dictionary.
- **26-002** — The file is encrypted, has a `P` entry, but the 10th bit of `P` is `false`. citeturn526667view1turn499424view8

## Checkpoint 28: Annotations

- **28-002** — An annotation other than Widget, Link, or PrinterMark is not a direct child of an `<Annot>` structure element.
- **28-004** — A non-Widget annotation lacks a `Contents` entry and also lacks an alternative description.
- **28-005** — A form field lacks a `TU` entry and also lacks an alternative description.
- **28-006** — An annotation with a subtype not defined in ISO 32000 fails the requirements of 7.18.1.
- **28-007** — A `TrapNet` annotation exists.
- **28-008** — A page containing an annotation has no `Tabs` entry.
- **28-009** — A page containing an annotation has a `Tabs` entry whose value is not `S`.
- **28-010** — A widget annotation is not nested inside a `<Form>` tag.
- **28-011** — A link annotation is not nested inside a `<Link>` tag.
- **28-012** — A link annotation lacks an alternate description in its `Contents` entry.
- **28-014** — The media clip data dictionary is missing `CT`.
- **28-015** — The media clip data dictionary is missing `Alt`.
- **28-016** — A file attachment annotation does not conform to checkpoint 7.11 requirements.
- **28-017** — A PrinterMark annotation is included in the logical structure.
- **28-018** — The appearance stream of a PrinterMark annotation is not marked as artifact. citeturn147919view0turn474159view0

## Checkpoint 30: XObjects

- **30-001** — A reference XObject is present.
- **30-002** — A Form XObject contains MCIDs and is referenced more than once. citeturn474159view0

## Checkpoint 31: Fonts

- **31-001** — In a Type 0 font with non-Identity encoding, the `Registry` values in the two `CIDSystemInfo` dictionaries do not match.
- **31-002** — In a Type 0 font with non-Identity encoding, the `Ordering` values in the two `CIDSystemInfo` dictionaries do not match.
- **31-003** — In a Type 0 font with non-Identity encoding, the CID font’s `Supplement` value is lower than the CMap’s `Supplement` value.
- **31-004** — A Type 2 CID font has neither a `CIDToGIDMap` stream nor `Identity` as the `CIDToGIDMap` value.
- **31-005** — A Type 2 CID font is missing `CIDToGIDMap`.
- **31-006** — A CMap is neither one of the standard listed CMaps nor embedded.
- **31-007** — The `WMode` in a CMap dictionary does not match the `WMode` in the CMap stream.
- **31-008** — A CMap references another CMap that is not on the standard list.
- **31-009** — A font program used for rendered text is not embedded.
- **31-011** — An embedded font program is missing one or more glyphs that the rendered text uses.
- **31-012** — An embedded Type 1 font’s `CharSet` omits at least one glyph that is present in the font program.
- **31-013** — An embedded Type 1 font’s `CharSet` names at least one glyph that is not present in the font program.
- **31-014** — An embedded CID font’s `CIDSet` omits at least one glyph that is present in the font program.
- **31-015** — An embedded CID font’s `CIDSet` names at least one glyph that is not present in the font program.
- **31-016** — Glyph width information in the font dictionary and the embedded font program differs by more than 1/1000 unit.
- **31-017** — A non-symbolic TrueType font is used for rendering, but the embedded font has no non-symbolic cmap.
- **31-018** — A non-symbolic TrueType font is used for rendering, but at least one rendered glyph cannot be looked up through any non-symbolic cmap.
- **31-019** — A non-symbolic TrueType font dictionary is missing `Encoding`.
- **31-020** — A non-symbolic TrueType font’s `Encoding` dictionary is missing `BaseEncoding`.
- **31-021** — For a non-symbolic TrueType font, `Encoding` or `BaseEncoding` is neither `MacRomanEncoding` nor `WinAnsiEncoding`.
- **31-022** — The `Differences` array in a non-symbolic TrueType font names one or more glyphs that are not in the Adobe Glyph List.
- **31-023** — A `Differences` array is present in a non-symbolic TrueType font, but the embedded font program lacks a `(3,1)` Microsoft Unicode cmap.
- **31-024** — A symbolic TrueType font dictionary contains an `Encoding` entry.
- **31-025** — An embedded symbolic TrueType font contains no cmap.
- **31-026** — An embedded symbolic TrueType font contains more than one cmap, but none is a `(3,0)` Microsoft Symbol cmap.
- **31-027** — A font dictionary lacks `ToUnicode`, and none of the protocol’s allowed exception cases applies.
- **31-028** — One or more Unicode values in the `ToUnicode` CMap are zero.
- **31-029** — One or more Unicode values in the `ToUnicode` CMap are `U+FEFF` or `U+FFFE`.
- **31-030** — One or more displayed text characters reference the `.notdef` glyph. citeturn474159view0turn147919view1

That is the full machine-determinable set: **87 rows marked `M`** in Matterhorn Protocol 1.1. citeturn989127view0turn147919view1

If you want the next pass, the useful one is: **which of these 87 are trivially enforceable in a controlled generator, which need low-level PDF checks, and which are mainly font/encoding edge cases**.


#### You:
which of these 87 are trivially enforceable in a controlled generator, which need low-level PDF checks, and which are mainly font/encoding edge cases

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## Primary bucket, not absolute truth

I’m treating these as the **best handling strategy in a controlled generator**:

- **Trivially enforceable** = easiest to guarantee by source-model rules, serializer rules, or outright feature bans.
- **Need low-level PDF checks** = even in a controlled generator, the safest way to close them is to inspect the emitted PDF internals.
- **Mainly font/encoding edge cases** = specialized font/CMap/Unicode/embedding territory.

One nuance: some items in the “low-level PDF checks” bucket can also be designed away by banning the risky feature. I’m classifying by the **most reliable closure path**, not by whether a clever generator could avoid them. This classification is based on the Matterhorn Protocol 1.1 machine-determinable rows and how those failures are expressed. veraPDF’s own docs are consistent with this split: it handles only machine-verifiable PDF/UA checks. citeturn0search0turn0search1

## Trivially enforceable in a controlled generator

These are mostly “always emit the required thing,” “never emit the forbidden thing,” or “use one safe pattern only.”

- **Artifact / real-content boundary**
  - 01-003
  - 01-004
  - 01-005
  - 01-007

- **Role mapping policy**
  - 02-001
  - 02-003
  - 02-004

- **Metadata and viewer settings**
  - 06-001
  - 06-002
  - 06-003
  - 07-001
  - 07-002

- **Declared language fields**
  - 11-001
  - 11-002
  - 11-003
  - 11-004
  - 11-005
  - 11-006

- **Required alt/replacement text presence**
  - 13-004
  - 17-002

- **Heading policy**
  - 14-002
  - 14-003
  - 14-006
  - 14-007

- **Note/reference ID policy**
  - 19-003
  - 19-004

- **Optional-content configuration policy**
  - 20-001
  - 20-002
  - 20-003

- **Embedded-file field presence**
  - 21-001

- **XFA policy**
  - 25-001

- **Encryption / permissions policy**
  - 26-001
  - 26-002

- **Annotation policy that is easy when you control all emitted annotations**
  - 28-002
  - 28-004
  - 28-005
  - 28-007
  - 28-008
  - 28-009
  - 28-010
  - 28-011
  - 28-012
  - 28-014
  - 28-015
  - 28-017
  - 28-018

These are the ones I would try to eliminate **by construction** with schema constraints, serializer assertions, and hard bans on unsupported features. citeturn0search0

## Need low-level PDF checks

These are the ones where the most reliable closure path is to inspect the emitted PDF structure, dictionaries, or object relationships after generation.

- **Structure-tree syntax against PDF tables**
  - 09-004
  - 09-005
  - 09-006
  - 09-007
  - 09-008

- **Character/text representation and table/formula internals**
  - 10-001
  - 12-001
  - 15-003
  - 17-003

- **Annotation and attachment internals**
  - 28-006
  - 28-016

- **XObject internals**
  - 30-001
  - 30-002

These are the ones I would not trust to “probably be fine” just because the source model was good. I would add post-build checks that read the actual PDF objects and verify the emitted internals. citeturn0search0turn0search1

## Mainly font/encoding edge cases

This entire family is primarily font, CMap, CID, glyph, embedding, ToUnicode, and encoding machinery:

- 31-001 through 31-009
- 31-011 through 31-030

Expanded explicitly:

- 31-001
- 31-002
- 31-003
- 31-004
- 31-005
- 31-006
- 31-007
- 31-008
- 31-009
- 31-011
- 31-012
- 31-013
- 31-014
- 31-015
- 31-016
- 31-017
- 31-018
- 31-019
- 31-020
- 31-021
- 31-022
- 31-023
- 31-024
- 31-025
- 31-026
- 31-027
- 31-028
- 31-029
- 31-030

These are the ones I would treat as a distinct subsystem with dedicated checks, because they are much more about font programs, encodings, Unicode maps, CMaps, glyph sets, and embedding correctness than about ordinary document semantics. citeturn0search0

## Practical reading of the split

- The **trivially enforceable** bucket is where generator design buys you the most.
- The **low-level PDF checks** bucket is where you still want object-level inspection after build.
- The **font/encoding** bucket is where a separate font-validation pass is the cleanest approach.

Next useful step is a **generator assertions spec** for the first bucket and a **post-build checker spec** for the second and third buckets.


#### You:
So now that you have a better idea of exactly how far down I'm digging and how comprehensive I plan to be in my planning, do another pass over available python for this project

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m doing a fresh pass with the **right frame** now: open-source Python, **creation-first**, accessibility-aware by design, and willing to go down to the object/stream level when needed. The question is no longer “what can touch PDFs,” it’s “what can support a controlled, semantics-first PDF generator.”


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## Re-pass, with the right frame

Your project is:

- **creation-only**
- **open-source Python only**
- **accessibility-aware by design**
- **semantic model first**
- willing to go **down to objects/streams** when needed
- comprehensive enough that you care about **Matterhorn-level closure**

Under that frame, the Python landscape looks much cleaner.

The accessibility guidance you uploaded still sets the outer rules: start with an accessible source model, preserve structure on output, image-only PDFs need OCR, tags and reading order matter, and automated checking is not enough by itself. fileciteturn0file0 fileciteturn0file1 fileciteturn0file2 fileciteturn0file3 fileciteturn0file4

## The short version

There is **no single open-source Python library** I can honestly recommend as the whole stack for this project.

The strongest realistic stack is:

- **WeasyPrint** for semantics-first document generation from HTML/CSS, including tagged/PDF/UA-oriented output. Its docs say it supports PDF/A and PDF/UA generation, including `pdf_variant="pdf/ua-1"`, but also explicitly say generated documents are **not guaranteed valid** and must be checked. citeturn125737search12turn916852search0turn796673search3
- **PyMuPDF** for precise page authoring, form widgets, inspection, and manipulation when you need direct page-level control. Its docs describe it as a high-performance library for extraction, analysis, conversion, and manipulation, and document page/widget APIs for text, images, annotations, links, and form fields. citeturn125737search5turn916852search2turn125737search13
- **pikepdf** for low-level PDF object and content-stream work. Its docs say it supports creating, manipulating, parsing, repairing, and reading/writing PDFs, including creation from scratch and parsing content streams. citeturn796673search13turn125737search2turn916852search11
- **pypdf** for assembly-style document operations: blank pages, metadata, forms, merging, transforms, passwords, viewing options. Its docs position it as a pure-Python general PDF library and document `PdfWriter`. citeturn796673search18turn125737search3turn796673search2
- **veraPDF** for machine-verifiable PDF/UA checking. Its docs explicitly say that for PDF/UA it performs **only machine-verifiable checks**. citeturn397010search3turn397010search15

If you want one sentence: **WeasyPrint is the best semantic generator, PyMuPDF is the best direct page author, pikepdf is the best plumbing layer, pypdf is the best assembly helper, and veraPDF is the validator.**

## The actual tool map

| Library          | Role in this project                                           | Keep or not                                   | Why                                                                                                                                                                                                                                                     |
| ---------------- | -------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **WeasyPrint**   | Primary generator when your source is semantic HTML/CSS        | **Keep, top tier**                            | BSD-licensed; designed to render HTML/CSS to PDF; supports tagged output and PDF/UA variants; strongest open-source semantics-first option I found. citeturn125737search4turn125737search12turn916852search0turn796673search3                     |
| **PyMuPDF**      | Direct page authoring, widgets/forms, inspection, manipulation | **Keep, top tier**                            | Best fit when you need exact placement and still want a real authoring/manipulation API. Open-source under AGPL, with separate commercial licensing available. citeturn125737search5turn916852search2turn796673search4                             |
| **pikepdf**      | Low-level objects, streams, repair, serialization checks       | **Keep, top tier**                            | Best open-source Python choice for “PDF plumbing.” MPL-2.0. Supports creating from scratch and content-stream parsing. citeturn796673search13turn125737search2turn916852search3turn796673search5                                                  |
| **pypdf**        | Assembly, metadata, forms, document-level ops                  | **Keep, second tier but useful**              | Great helper library, not the main semantic authoring engine. BSD-3-Clause. citeturn796673search18turn125737search3turn796673search2                                                                                                               |
| **fpdf2**        | Simple generated PDFs, lightweight programmatic authoring      | **Keep, situational**                         | Mature and actively maintained; good for simpler generation; docs show links and document language, but I do not see the same strong PDF/UA/tagged story as WeasyPrint. citeturn397010search0turn397010search4turn916852search1turn916852search13 |
| **borb**         | Pure-Python create/read/manipulate library                     | **Keep, exploratory**                         | Real creator/manipulator, but I do not have equally strong official evidence that it is the best accessibility-first core. citeturn397010search1turn397010search13                                                                                  |
| **pdfplumber**   | Layout-aware extraction/debugging                              | **Keep only as analysis support**             | Great for detailed extraction and debugging, not a creator. citeturn397010search1                                                                                                                                                                    |
| **pdfminer.six** | Text/layout extraction and analysis                            | **Keep only as analysis support**             | Extraction tool, not a creator.                                                                                                                                                                                                                         |
| **OCRmyPDF**     | OCR fallback for scanned inputs only                           | **Keep only if OCR ever enters the pipeline** | Strong for searchable-text repair on existing scanned PDFs, not a creator. citeturn397010search6turn397010search10                                                                                                                                  |
| **veraPDF**      | Post-build machine validation                                  | **Keep, required**                            | Best open-source validator in this stack for PDF/UA machine checks. citeturn397010search3turn397010search15                                                                                                                                         |

## What I would recommend as the core architecture

### Option A: semantics-first documents

Use this for reports, guides, handouts, policies, anything whose meaning is naturally hierarchical and document-like.

1. **Your own semantic source model**
   - headings
   - paragraphs
   - lists
   - tables
   - figures
   - captions
   - links
   - notes/references
   - metadata
   - language
   - artifact flags

2. **Render to semantic HTML/CSS**

3. **Generate PDF with WeasyPrint**
   - use PDF tags
   - target PDF/UA-oriented output where appropriate
   - derive bookmarks from headings if needed\
     WeasyPrint explicitly documents PDF/UA variants and supports generating specialized PDFs, but warns that conformance is not guaranteed just because the option exists. citeturn916852search0turn125737search12

4. **Inspect/patch low-level details with pikepdf where needed**
   - object structure
   - metadata quirks
   - content streams
   - post-generation cleanup

5. **Validate with veraPDF**

6. **Human review for the non-machine parts**
   - title quality
   - alt-text quality
   - wording quality
   - complex chart/figure sufficiency\
     That gap is consistent with Matterhorn/veraPDF and with the guidance you uploaded. citeturn397010search3turn397010search15 fileciteturn0file3

### Option B: exact page-authored PDFs

Use this when you need fine control over page composition, forms, or graphic placement.

1. **Your own semantic source model**
2. **Author pages in PyMuPDF**
   - create pages
   - place text/images
   - create links/annotations
   - create widgets/form fields\
     PyMuPDF documents page and widget APIs for this layer. citeturn125737search13turn916852search2
3. **Use pikepdf for lower-level object/stream/tag-adjacent work**
4. **Use pypdf for assembly/document operations if convenient**
5. **Validate with veraPDF**
6. **Human review**

This route gives you more exact control, but you will have to shoulder more of the semantics yourself instead of inheriting them from HTML.

## What I would *not* use as the primary core

### Not as the main semantic generator

- **pypdf**
- **pikepdf**

They are too low-level / assembly-oriented to be the main “author a semantically rich document” engine, even though they are extremely useful support layers. citeturn796673search13turn796673search18

### Not as the accessibility-first lead

- **fpdf2**
- **borb**

Both are real creation libraries, and fpdf2 in particular looks mature and pleasant. But based on the docs I found, neither has as strong an official accessibility/PDF/UA story as WeasyPrint. fpdf2 does expose some accessibility-relevant knobs like document language and image `alt_text`, which is good, just not the same thing as a strong tagged/PDF/UA-centered pipeline. citeturn397010search0turn397010search4turn916852search13

### Not for creation

- **pdfplumber**
- **pdfminer.six**
- **OCRmyPDF**
- **veraPDF**

They are support tools, not generators. citeturn397010search6turn397010search3

## The stack I would choose today

### If your documents are fundamentally document-like

**WeasyPrint + pikepdf + veraPDF**\
Add **pypdf** if you want convenient document assembly tasks.

Why:

- strongest semantics-first story
- open-source BSD core for WeasyPrint
- explicit PDF/UA-capable generation path
- low-level escape hatch through pikepdf
- machine validation through veraPDF citeturn125737search12turn916852search0turn796673search13turn397010search15

### If your documents are more canvas-like or form-heavy

**PyMuPDF + pikepdf + veraPDF**\
Optionally **pypdf** for assembly.

Why:

- more direct control over authored page content and widgets
- better fit when you need to own placement and object creation yourself
- still gives you the low-level and validation layers citeturn125737search5turn916852search2turn796673search13turn397010search15

## Licensing caveat you should care about

Since you said **open source only**, not “permissive only”:

- **WeasyPrint** is BSD-licensed. citeturn796673search3
- **pypdf** is BSD-3-Clause. citeturn796673search2
- **pikepdf** is MPL-2.0. citeturn796673search5
- **PyMuPDF** is open-source under **AGPL** unless you buy commercial terms. That still counts as open source, but it is a much stronger copyleft constraint than BSD/MPL. citeturn796673search4turn796673search0

That means PyMuPDF is technically in-bounds for your “open source only” rule, but it may or may not be in-bounds for your eventual distribution model.

## My updated recommendation

If I were planning this project with your level of comprehensiveness, I would treat the Python options like this:

### Core

- **WeasyPrint**
- **pikepdf**
- **veraPDF**

### Add when needed

- **PyMuPDF**
- **pypdf**

### Secondary / situational

- **fpdf2**
- **borb**

### Support only

- **pdfplumber**
- **pdfminer.six**
- **OCRmyPDF**

## Final blunt take

The biggest change from my earlier answers is this:

I would now stop thinking in terms of “one Python library to make accessible PDFs” and instead think in terms of **one semantic authoring path plus one low-level PDF path plus one validation path**.

For your project, that means:

- **semantic authoring path**: WeasyPrint
- **low-level PDF path**: pikepdf
- **page/form/control path when needed**: PyMuPDF
- **validation path**: veraPDF

That is the strongest open-source Python story I can defend from the current docs.

I can turn this into a **decision table** next — “if the document has X, use Y” — for reports, forms, tables, charts, mixed layouts, and exact page control.


#### You:
but which of those do ALL of it? 

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m answering this as a hard “single-library vs stack” question now, because that’s the real decision boundary.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## None of them

No **single** open-source Python library in this set does **all** of the following on its own:

- semantics-first document generation
- direct page/canvas authoring
- low-level PDF object and content-stream control
- forms
- metadata/document settings
- tagged/PDF/UA-oriented output
- PDF/UA validation

That is why the realistic answer is a **stack**, not one library. citeturn338621search1turn338621search2turn338621search3turn338621search4turn338621search5turn338621search18

## Closest single-library answers

### Closest to **semantics-first accessible creation**

**WeasyPrint**\
It gives you HTML/CSS-based generation and explicitly exposes `pdf_tags`, `pdf_forms`, and PDF variants including PDF/UA-oriented output. But it is not your low-level object/stream tool, and it is not your validator. citeturn338621search5

### Closest to **general page authoring**

**PyMuPDF**\
It can create PDFs, pages, links, annotations, and form widgets, so it is the strongest single-library answer for “I want to author pages directly in Python.” But it is not positioned as the full semantics-first PDF/UA generator, and it is not the validator. citeturn338621search1turn338621search11turn338621search16

### Closest to **low-level control**

**pikepdf**\
It is the best fit for direct access to PDF objects, streams, and content streams. But it is not the best high-level authoring engine and not the validator. citeturn338621search2turn338621search7turn338621search12turn338621search17

### Closest to **document assembly/helper work**

**pypdf**\
Good for writer-style document assembly, metadata, forms, merging, and transforms. But it is not the main semantic generator and not the validator. citeturn338621search3turn338621search8turn338621search13turn338621search18

### Closest to **validation**

**veraPDF**\
It is the validator. Its docs explicitly say that for PDF/UA it performs only machine-verifiable checks. But it does not create PDFs. citeturn338621search4turn338621search9

## So which one does “all of it”?

**None.**

## Best honest stack

- **WeasyPrint** for semantic generation
- **PyMuPDF** when you need direct page/form authoring
- **pikepdf** for low-level PDF plumbing
- **pypdf** for assembly/helper operations
- **veraPDF** for machine validation citeturn338621search1turn338621search2turn338621search3turn338621search4turn338621search5

## If you force me to pick just one

- For **accessible creation first**: **WeasyPrint**
- For **direct authored control first**: **PyMuPDF**
- For **deep internals first**: **pikepdf**

But a one-library plan would be a compromise, not the clean solution.


#### You:
you are giving me generalized answers instead of directly answering what i'm asking

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
You’re right. Direct answer:

## Which of those does **all of it**?

**None of them.**

Not one of these open-source Python tools, by itself, does all of:

- semantics-first accessible PDF generation
- direct page/canvas authoring
- low-level PDF object/content-stream control
- forms
- tagged/PDF/UA-oriented output
- PDF/UA validation

## The closest single-library answers

- **WeasyPrint**: best single library for **semantics-first accessible creation**. It explicitly supports `pdf_tags`, `pdf_forms`, and `pdf_variant="pdf/ua-1"`. It does **not** replace a low-level PDF object tool or a validator. citeturn0search0
- **PyMuPDF**: best single library for **direct page authoring/manipulation**. It can create PDFs, pages, text, images, links, annotations, and widgets/forms. I do **not** have official docs showing it as the one-library answer for full PDF/UA-oriented semantic generation plus validation. citeturn0search1
- **pikepdf**: best single library for **low-level PDF internals**. It can create/manipulate PDFs and parse/edit content streams. It is not the best single-library answer for semantics-first accessible authoring or validation. citeturn0search2
- **pypdf**: good for **writer/assembly operations**, metadata, forms, merging, transforms. It is not the one-library answer for semantics-first accessible authoring or validation. citeturn0search3
- **veraPDF**: does **validation only**. It does not create PDFs. citeturn0search4

## If you force a one-library choice

- For **accessible creation first**: **WeasyPrint**
- For **direct authored control first**: **PyMuPDF**
- For **deep PDF internals first**: **pikepdf**

## The blunt bottom line

If your question is literally:

> “Which one of those libraries can do the entire project alone?”

The answer is:

**None of them.**

If you want, I’ll do the next answer in the exact format:

## library name → what it covers → what it does not cover

with no extra framing.


#### You:
I didn't ask for forms.

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Correct. Forms were irrelevant to your question.

Stripped down to what you were actually asking:

## Without forms, which one does all of it?

Still **none of them**.

No single open-source Python library here does all of:

- semantics-first accessible PDF creation
- direct page authoring
- low-level PDF object/content-stream control
- tagged/PDF/UA-oriented output
- validation

## Closest single-library answers, without dragging forms into it

- **WeasyPrint**
  - Covers: semantics-first generation, tagged/PDF/UA-oriented output
  - Does not cover: deep low-level PDF internals, full validation

- **PyMuPDF**
  - Covers: direct page authoring, drawing, links/annotations, manipulation
  - Does not cover: strongest semantics-first tagged/PDF/UA generation story, full validation

- **pikepdf**
  - Covers: low-level PDF objects, streams, content-stream editing
  - Does not cover: high-level semantic document authoring, full validation

- **pypdf**
  - Covers: assembly/manipulation, metadata, writer-style operations
  - Does not cover: high-level semantic generation, full validation

- **veraPDF**
  - Covers: validation
  - Does not cover: creation

## Direct answer

If your question is:

> Which one of these can handle the entire creation project by itself?

The answer is:

**None.**

## Closest by priority

- If your priority is **semantic accessible creation**: **WeasyPrint**
- If your priority is **exact authored page control**: **PyMuPDF**
- If your priority is **deep PDF internals**: **pikepdf**

That’s the clean answer.


#### You:
*deep breath* do you see how your explanations of "closest" still do not have nearly enough information for me to figure out what can be used for what

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes. The useful answer here is a **real capability map**, not “closest.” I’m pulling the official docs again and I’ll turn it into a direct **library → exact jobs it can do / cannot do** matrix.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes. Here is the **direct capability map**.

## What each Python library can be used for in *your* project

Legend:

- **Yes** = it is a real fit for that job
- **Limited** = possible, but not a strong or primary fit
- **No** = not what that library is for
- **Not documented** = I did not find official docs supporting that use strongly enough to claim it

| Library          | Create PDFs from scratch | Semantic document generation | Direct page drawing / placement | Low-level PDF objects | Content-stream level work | Tagged / accessibility-oriented output | PDF/UA-oriented output | Metadata | Validation | Extraction / analysis | OCR |
| ---------------- | ------------------------ | ---------------------------- | ------------------------------- | --------------------- | ------------------------- | -------------------------------------- | ---------------------- | -------- | ---------- | --------------------- | --- |
| **WeasyPrint**   | Yes                      | Yes                          | No                              | No                    | No                        | Yes                                    | Yes                    | Limited  | No         | No                    | No  |
| **PyMuPDF**      | Yes                      | Limited                      | Yes                             | Limited               | Limited                   | Not documented                         | Not documented         | Limited  | No         | Yes                   | No  |
| **pikepdf**      | Yes                      | No                           | No                              | Yes                   | Yes                       | Limited                                | Not documented         | Yes      | No         | Limited               | No  |
| **pypdf**        | Yes                      | No                           | Limited                         | Limited               | Limited                   | Not documented                         | Not documented         | Yes      | No         | Yes                   | No  |
| **veraPDF**      | No                       | No                           | No                              | No                    | No                        | No                                     | No                     | No       | Yes        | Limited               | No  |
| **OCRmyPDF**     | No                       | No                           | No                              | No                    | No                        | No                                     | No                     | No       | No         | Limited               | Yes |
| **pdfplumber**   | No                       | No                           | No                              | No                    | No                        | No                                     | No                     | No       | No         | Yes                   | No  |
| **pdfminer.six** | No                       | No                           | No                              | No                    | No                        | No                                     | No                     | No       | No         | Yes                   | No  |

## What that means in plain English

### WeasyPrint

Use it for:

- **semantic, document-like PDFs**
- HTML/CSS as the source model
- tagged output
- PDF/UA-oriented output

Do **not** use it for:

- low-level PDF surgery
- object graph work
- content-stream editing
- validation

WeasyPrint’s official docs explicitly expose `pdf_tags` and PDF variants including `pdf/ua-1`. They describe WeasyPrint as an HTML/CSS rendering engine that exports to PDF, under a BSD license. citeturn215606search4turn215606search16

### PyMuPDF

Use it for:

- **direct page authoring**
- creating a PDF and new pages
- placing text, images, links, annotations
- manipulating existing pages
- extraction and inspection

Do **not** assume it is your best one-library answer for:

- semantics-first tagged/PDF/UA generation
- validation

Its docs explicitly describe it as a high-performance library for extraction, analysis, conversion, and manipulation, and show that it can create a new PDF and new pages. citeturn215606search1turn215606search5turn215606search9

### pikepdf

Use it for:

- **low-level PDF internals**
- creating a PDF from scratch
- object-level editing
- stream-level work
- content-stream parsing/unparsing
- repair / manipulation / serialization control

Do **not** use it as your main semantics-first authoring engine.

Its docs explicitly say it supports creating PDFs from scratch and parsing/editing content streams. citeturn215606search14turn215606search2turn215606search6

### pypdf

Use it for:

- **document assembly**
- writing PDFs
- blank pages
- merging/splitting
- metadata
- general writer-style manipulation
- text/metadata retrieval

Do **not** treat it as your main low-level stream tool or your main accessibility-oriented generator.

Its docs describe it as a free, open-source pure-Python PDF library for splitting, merging, cropping, transforming pages, adding data and viewing options, retrieving text and metadata, and they document `PdfWriter`. citeturn215606search7turn215606search15turn215606search19

### veraPDF

Use it for:

- **machine validation**
- PDF/UA and PDF/A checking

Do **not** use it to create PDFs.

veraPDF’s docs say that for PDF/UA it performs only machine-verifiable checks. citeturn0search0turn0search1

### OCRmyPDF

Use it for:

- **OCR on existing scanned PDFs**

Do **not** use it as a creator.

Its docs state that it adds an OCR text layer to scanned PDFs. citeturn0search2

### pdfplumber

Use it for:

- **layout-aware extraction**
- debugging characters, lines, rectangles, tables

Do **not** use it to create PDFs.

Its docs position it as an extraction and inspection tool. citeturn0search3

### pdfminer.six

Use it for:

- **text extraction and PDF analysis**

Do **not** use it to create PDFs.

Its docs position it as an extraction/analyzer tool. citeturn0search4

## If your question is “what can be used for what?”

Here is the same answer by **job**, not by library.

### Job: create a semantic, accessibility-oriented document PDF

Use:

- **WeasyPrint**

### Job: create pages directly, place text exactly, draw the document yourself

Use:

- **PyMuPDF**

### Job: inspect or modify raw PDF internals after generation

Use:

- **pikepdf**

### Job: assemble, merge, set metadata, do writer-style document operations

Use:

- **pypdf**

### Job: validate machine-checkable PDF/UA issues

Use:

- **veraPDF**

### Job: OCR scanned inputs

Use:

- **OCRmyPDF**

### Job: inspect extracted text/layout/tables from PDFs

Use:

- **pdfplumber**
- **pdfminer.six**
- **PyMuPDF**

## If your question is “which one covers the most of my project?”

In terms of **coverage**, not perfection:

1. **WeasyPrint**
   - Best for the **semantic generation** half
   - Weak for low-level internals and validation

2. **PyMuPDF**
   - Best for the **direct authoring/manipulation** half
   - Weaker for the semantics-first tagged/PDF/UA story

3. **pikepdf**
   - Best for the **low-level control** half
   - Weak for authoring semantics-first documents

## The actual decision boundary

If your project starts from a **semantic content model**, the closest fit is:

- **WeasyPrint** as generator
- **pikepdf** as low-level patch/check layer
- **veraPDF** as validator

If your project starts from **you wanting to explicitly compose every page**, the closest fit is:

- **PyMuPDF** as generator
- **pikepdf** as low-level patch/check layer
- **veraPDF** as validator

## Direct answer to the thing you were asking

You wanted enough information to tell **what can be used for what**.

So the clean answer is:

- **WeasyPrint** = semantic document generator
- **PyMuPDF** = direct page author/manipulator
- **pikepdf** = low-level PDF internals
- **pypdf** = document assembly/helper
- **veraPDF** = validator
- **OCRmyPDF** = OCR only
- **pdfplumber** = extraction/debugging only
- **pdfminer.six** = extraction only

If you want the next pass, the most useful one is an even harsher table:

## requirement in your project → single best library → second-best fallback → why the others are wrong for that requirement


#### You:
Semantic document generation?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes.

## What I mean by **semantic document generation**

It means you generate the PDF from a model of **what the content *is***, not just **where ink goes on the page**.

So instead of saying:

- put text at x=72, y=640
- draw a bold line here
- place an image here

you say:

- this is a **Heading 1**
- this is a **paragraph**
- this is an **ordered list**
- this is a **data table**
- this is a **figure**
- this is a **caption**
- this is **decorative**
- this is the **document language**
- this is the **reading order**

That is semantic document generation.

## The contrast

### Semantic generation

The source model is meaning-first.

Example mental model:

```json
{
  "title": "Quarterly Report",
  "language": "en-US",
  "content": [
    { "type": "heading", "level": 1, "text": "Quarterly Report" },
    { "type": "paragraph", "text": "This quarter..." },
    { "type": "table", "headers": ["Region", "Sales"], "rows": [["East", "12"], ["West", "9"]] },
    { "type": "figure", "src": "chart.png", "alt": "Bar chart showing..." }
  ]
}
```

Then the generator turns that into PDF structure, tags, reading order, bookmarks, etc.

### Page-drawing generation

The source model is appearance-first.

Example mental model:

- draw text here
- draw line here
- draw rectangle here
- place image here

That can still produce a visually nice PDF, but the semantics are weaker unless you add them deliberately afterward or alongside the drawing logic.

## Why this matters for accessibility

Your uploaded sources are all pushing the same basic idea:

- accessibility should start in the **source**
- PDFs need **tags**
- PDFs need correct **reading order**
- figures need alternatives
- source structure should survive export/remapping fileciteturn0file1 fileciteturn0file2 fileciteturn0file3

Semantic generation is the creation-side version of that principle.

It makes it much easier to deterministically emit:

- heading tags
- paragraph tags
- list structure
- table structure
- figure/caption structure
- bookmarks
- reading order
- language/title metadata
- artifacting for decorative content

## In library terms

When I called **WeasyPrint** “semantic document generation,” I meant:

- you give it **HTML/CSS**
- HTML already carries semantics like headings, paragraphs, lists, tables, captions, links
- the PDF generator can use that structure when producing output

So that is much closer to “author by meaning.”

When I called **PyMuPDF** direct page authoring, I meant:

- you are composing the page more explicitly
- you decide placement and drawing more directly
- semantics are not the natural starting point in the same way

## The shortest definition

**Semantic document generation = generating a PDF from structured meaning-first content, not from raw page-drawing instructions.**

If you want, I’ll do the next answer as:

## semantic generation vs page authoring vs low-level PDF control

with each of your Python libraries placed into exactly one or two buckets.


#### You:
so tagged?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes — **tagged is part of it, but not the whole thing**.

## The clean distinction

- **Semantic generation** = your source model knows what things **are**
  - heading
  - paragraph
  - list
  - table
  - figure
  - caption
  - decorative artifact

- **Tagged PDF** = the PDF output contains a **structure tree / tags** that encode that meaning for assistive tech and reading order

So:

**semantic generation is the upstream logic**\
**tagged PDF is one downstream result of doing that logic correctly**

## In other words

If your generator is truly semantic, then **yes, it should emit a tagged PDF**.

But “semantic generation” also includes other things besides tags, like:

- correct reading order
- figure vs decorative handling
- alt text / replacement text handling
- title and language metadata
- proper table relationships
- bookmarks/navigation when appropriate

Your uploaded guidance is explicit that tags provide structure, reading order matters, and accessible PDFs need more than just visual appearance. fileciteturn0file1 fileciteturn0file2 fileciteturn0file3 fileciteturn0file4

## Short answer

If you mean:

> “When you say semantic document generation, do you basically mean generation that produces a tagged PDF from known semantics?”

Then the answer is:

**Yes.**

But more precisely:

**semantic generation should produce correctly tagged output plus the other accessibility-relevant structure around it.**


#### You:
ugh it's so vague

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m going to pin the terms down in a way that lets you actually sort libraries into bins instead of drowning in fuzzy prose.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes. Non-vague version:

## Precise definitions

### Semantic document generation

A library qualifies only if it takes **meaning-first input** like:

- headings
- paragraphs
- lists
- tables
- figures
- captions
- links

and turns that into PDF output **as semantics**, not just page drawing.

In practical Python terms, that usually means **HTML/CSS-like input with real structure** and documented support for tagged/accessibility-oriented PDF output. WeasyPrint explicitly exposes `pdf_tags` and PDF variants including `pdf/ua-1`. citeturn369999search0

### Tagged PDF output

A library qualifies if it can emit a **PDF structure tree / tags**. Tagging is an **output property** of the file.

### Page authoring

A library qualifies if it lets you create pages and place content directly:

- text
- images
- shapes
- links
- annotations

PyMuPDF explicitly documents that it can create pages and add text, images, geometrical objects, annotations, and form fields. citeturn369999search1turn369999search11

### Low-level PDF control

A library qualifies if it lets you work with:

- PDF objects
- dictionaries
- streams
- content streams

pikepdf explicitly documents creating PDFs from scratch and parsing/unparsing content streams. citeturn369999search2turn369999search7turn369999search12

---

## Now the direct mapping

### WeasyPrint

- **Semantic document generation:** **Yes**
- **Tagged PDF output:** **Yes**
- **PDF/UA-oriented output:** **Yes**
- **Direct page authoring:** **No**
- **Low-level PDF control:** **No**
- **Validation:** **No**

Why: its documented model is HTML/CSS → PDF, and it explicitly exposes `pdf_tags` and `pdf/ua-1`. citeturn369999search0turn369999search5

### PyMuPDF

- **Semantic document generation:** **No, not in the strict sense**
- **Tagged PDF output:** **Not documented strongly enough for me to say yes**
- **PDF/UA-oriented output:** **Not documented strongly enough for me to say yes**
- **Direct page authoring:** **Yes**
- **Low-level PDF control:** **Some, but not its main identity**
- **Validation:** **No**

Why: its docs position it as creation/manipulation/extraction at the page/content level, not as a semantics-first tagged-PDF generator. citeturn369999search1turn369999search6turn369999search11

### pikepdf

- **Semantic document generation:** **No**
- **Tagged PDF output:** **Possible at low level, but not its documented primary model**
- **PDF/UA-oriented output:** **Not documented as a primary feature**
- **Direct page authoring:** **No, except very minimal create-blank-page style creation**
- **Low-level PDF control:** **Yes**
- **Validation:** **No**

Why: its docs explicitly say it can create PDFs from scratch, but also explicitly say it is **not primarily a PDF generation library**. It is the low-level objects/streams tool. citeturn369999search2turn369999search7turn369999search12

### pypdf

- **Semantic document generation:** **No**
- **Tagged PDF output:** **Not documented as a primary feature**
- **PDF/UA-oriented output:** **Not documented as a primary feature**
- **Direct page authoring:** **Very limited**
- **Low-level PDF control:** **Some, but not its main identity**
- **Validation:** **No**

Why: its docs show `PdfWriter`, blank pages, metadata, XMP, and document-level writing/manipulation. That is writer/assembly territory, not semantics-first generation. citeturn369999search3turn369999search8

### veraPDF

- **Semantic document generation:** **No**
- **Tagged PDF output:** **No**
- **PDF/UA-oriented output:** **No**
- **Direct page authoring:** **No**
- **Low-level PDF control:** **No**
- **Validation:** **Yes**

Why: its docs explicitly say it validates PDF/A and PDF/UA, and for PDF/UA performs only machine-verifiable checks. citeturn369999search4turn369999search9

---

## So, if the question is:

### “Which of these is a semantic document generator?”

**WeasyPrint only.** citeturn369999search0turn369999search5

### “Which of these can create a tagged/accessibility-oriented PDF from semantic input?”

**WeasyPrint is the only one here that I can say that about cleanly from the official docs.** citeturn369999search0

### “Which of these lets me author pages directly?”

**PyMuPDF.** citeturn369999search1turn369999search11

### “Which of these lets me get down into PDF objects and content streams?”

**pikepdf.** citeturn369999search2turn369999search7turn369999search12

### “Which of these is mainly a writer/assembler/helper?”

**pypdf.** citeturn369999search3turn369999search8

### “Which of these validates PDF/UA?”

**veraPDF.** citeturn369999search4turn369999search9

## Shortest possible answer

- **WeasyPrint** = semantic generator
- **PyMuPDF** = page author
- **pikepdf** = low-level PDF internals
- **pypdf** = writer/helper
- **veraPDF** = validator

That is the concrete split.


#### You:
Search for python packages that can extract information from PDFs at this deep level

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m treating “deep level” as: PDF objects, xref/object graph, dictionaries/streams, content streams/operators, structure/tags, fonts/CMaps/Unicode maps, annotations/forms, and metadata — not just “extract text.”


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes. I searched with your **deep-level** meaning in mind.

## The real shortlist

### 1. **pikepdf**

Use this when you want the PDF **object model itself**: dictionaries, arrays, names, streams, page resources, name trees, and content streams. Its docs describe it as a Python wrapper around **qpdf**, and its PyPI/docs explicitly say it gives direct access to PDF objects that mirror the spec. It also has dedicated docs for **stream objects**, **content streams** (`parse` / `unparse`), and **name trees**. citeturn218606search8turn218606search12turn218606search0turn218606search4turn393871search1

What it is best for:

- raw PDF objects
- stream dictionaries and bytes
- content stream operators
- page resources / XObjects
- name trees
- metadata and structural plumbing

What it is not best for:

- high-level text/layout analysis
- “what font/color/position is this text fragment?” style extraction

### 2. **PyMuPDF**

Use this when you want a very deep extractor **plus** practical page-level inspection. Its docs expose low-level interfaces like `xref_get_key()`, `xref_get_keys()`, `xref_object()`, `xref_stream()`, and `xref_stream_raw()`. The docs also explicitly note that you can access the **trailer** using those xref methods with `-1`, and the page/document APIs expose things like **links**, **images**, and **fonts**. citeturn325366search0turn325366search4turn325366search6turn325366search9turn325366search1turn325366search7

What it is best for:

- xref-level inspection
- raw object and raw stream access
- trailer access
- page resources
- annotations/links/images/fonts
- fast extraction plus practical manipulation

What it is not strongest for:

- spec-mirroring object work as cleanly as pikepdf
- text/layout analysis as deeply as pdfminer.six

### 3. **pdfminer.six**

Use this when you want the deepest **text/content parser**. Its official docs say it can **parse all objects into Python objects**, extract **tagged contents**, **table of contents**, images, and more, and supports many font types including **Type1, TrueType, Type3, and CID**. Its docs also show extraction of **font names and sizes per character**, and its PyPI/docs emphasize exact location, font, and color extraction from source-level page content. citeturn218606search3turn393871search2turn393871search6turn218606search19turn218606search7

What it is best for:

- text extraction from source content
- character-level positions
- font and color info
- layout analysis
- tagged contents
- TOC extraction
- font/CMap-heavy text work

What it is not best for:

- low-level PDF surgery
- raw object/stream editing as a primary mode

### 4. **pypdf**

Use this when you want a **general parser/writer** that still reaches below the surface. Its docs expose **generic PDF objects**, say that `PdfReader` reads the **cross-reference tables** into memory, and the developer docs describe parsed objects being stored in `resolved_objects`. Its text extraction docs also say extracting text requires parsing the **whole content stream**, and visitor hooks can be called for each **operator** or each **text fragment**. citeturn218606search1turn218606search5turn218606search13turn325366search2turn325366search5

What it is best for:

- balanced pure-Python parsing
- generic objects
- xref-aware reading
- content-stream-aware text extraction
- visitor-based extraction hooks
- document-level inspection

What it is not best for:

- deepest stream/object control compared with pikepdf
- deepest text/layout analysis compared with pdfminer.six

### 5. **pypdfium2**

This is the important extra one. If you are willing to use **PDFium bindings**, it belongs on the list. Its docs describe it as an ABI-level binding to **PDFium** for inspection/manipulation/creation, and the API layers include **Document**, **Page**, **Pageobjects**, **TextPage**, and **Attachment**. The page API exposes `get_textpage()`, `get_objects()`, `get_toc()`, page-as-XObject handling, and object insertion/removal; the docs also explicitly say there is a **raw PDFium API** layer available in addition to helper layers. citeturn319836search1turn319836search3turn721603search0turn721603search1turn721603search2

What it is best for:

- PDFium-backed inspection
- page-object enumeration
- text-page extraction
- bookmarks / TOC
- attachments
- lower-level binding access if you want to drop to raw API

What it is not best for:

- pure-Python portability
- “Pythonic spec mirror” ergonomics like pikepdf

## One layer up, not deepest

### **pdfplumber**

This is very good when you want a practical inspection layer for **characters, rectangles, lines, tables, and visual debugging**. Its own docs describe exactly that, and they also state it is built on **pdfminer.six** and works best on machine-generated PDFs. It is not the deepest raw-internals tool; it is a very useful **debugging/extraction layer** above pdfminer.six. citeturn687930search2turn687930search6

### **borb**

borb is a real read/write/manipulate library, and its PyPI page says it models PDFs in a **JSON-like structure** of nested lists, dictionaries, and primitives. That makes it relevant if you want a more uniform object model, but the same PyPI page also says it prioritizes **common PDF use cases**, and I did not find official docs strong enough to rank it above pikepdf, PyMuPDF, pdfminer.six, pypdf, or pypdfium2 for the specific “deep extraction” problem. citeturn687930search3turn687930search7

## Things I would **not** put in the extraction shortlist

### **OCRmyPDF**

Useful, but for a different job. Its docs say it adds an OCR text layer to scanned PDFs so they become searchable. That is remediation of image PDFs, not deep inspection of native PDF internals. citeturn687930search4

### **veraPDF**

Also useful, but for validation, not extraction. Its docs say it validates PDF/A and PDF/UA, and for PDF/UA performs only **machine-verifiable checks**. citeturn687930search1

### **pdfrw**

I would skip it for this project. Its own reader code says `PdfReader` parses the **top-level container objects** and **does not parse into streams**. That is exactly the wrong limitation for the depth you are talking about. citeturn319836search2turn319836search7

## The direct answer by layer

If you want to inspect:

- **raw objects / dictionaries / streams / name trees / content streams** → **pikepdf** citeturn218606search12turn218606search0turn393871search1
- **xref / trailer / raw object source / raw streams / page resources / annotations** → **PyMuPDF** citeturn325366search4turn325366search6turn325366search1
- **text layout / characters / fonts / colors / tagged contents / TOC** → **pdfminer.six** citeturn393871search2turn218606search19turn218606search7
- **general pure-Python object parsing plus content-stream-aware extraction hooks** → **pypdf** citeturn218606search13turn325366search2turn325366search5
- **PDFium-backed page objects / text pages / raw API escape hatch** → **pypdfium2** citeturn319836search1turn721603search0turn721603search1
- **chars / lines / rects / tables / visual debugging** → **pdfplumber** citeturn687930search2

## My blunt ranking for your use case

If you are digging **all the way down**, I would look at them in this order:

1. **pikepdf**
2. **PyMuPDF**
3. **pdfminer.six**
4. **pypdf**
5. **pypdfium2**
6. **pdfplumber**
7. **borb**

That is not “best library overall.” It is “best shortlist for deep inspection of PDF internals and near-internals.”

The most useful next cut is a **layer-by-layer matrix** with columns:

- objects
- xref/trailer
- streams
- content streams/operators
- tags/structure clues
- fonts/CMaps/Unicode
- annotations
- page objects
- text geometry
- TOC/bookmarks
- metadata

and rows for the packages above.


#### You:
Imagine we wanted to do this in Python:

Input
Extract
Interpret / normalize
Attach review flags
Project to DOCX

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m mapping this as a real pipeline now, not “PDF library shopping.” The key question is where you want the canonical model to live: raw PDF objects, normalized semantic blocks, or DOCX-ready document structure.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## Yes — that is a sane Python pipeline

For the workflow you described,

- **Input**
- **Extract**
- **Interpret / normalize**
- **Attach review flags**
- **Project to DOCX**

the cleanest approach is to treat the PDF as a **source of evidence**, build your own **canonical intermediate model**, and only then emit DOCX. That is because the Python PDF libraries are strongest at extraction or low-level inspection, while `python-docx` is strongest at writing Word structures like paragraphs, tables, styles, numbering, comments, and core properties. citeturn476064search0turn476064search1turn476064search2turn476064search3turn174814search0turn174814search1turn174814search2turn476064search8

## The best shape for the pipeline

### 1. Input

Take in:

- the PDF bytes
- file-level metadata
- optional policy/config for your extractor
- optional page ranges
- optional OCR policy

If the input may be scanned, add an OCR gate here. `OCRmyPDF` is specifically for adding an OCR text layer to scanned PDFs; it is not a general extractor or authoring library. citeturn476064search3

### 2. Extract

Do **not** rely on one extractor only. Use layered extraction depending on what you want:

- **pikepdf** for raw PDF objects, streams, and content streams
- **PyMuPDF** for xref-level access, page resources, blocks/spans/images/links, and practical page inspection
- **pdfminer.six** for text/layout analysis, tagged contents, TOC, font-aware extraction
- optionally **pdfplumber** when you want table/debug-style inspection on top of `pdfminer.six` citeturn476064search2turn476064search5turn476064search3turn476064search10turn476064search12

A useful rule is:

- if you care about **raw PDF structure**, start with `pikepdf`
- if you care about **page content and geometry**, start with `PyMuPDF`
- if you care about **reading-like text/layout recovery**, start with `pdfminer.six` citeturn476064search2turn476064search18turn476064search3turn476064search10

### 3. Interpret / normalize

This should be **your code**, not a library feature.

Build an intermediate representation with nodes like:

- document
- page
- heading
- paragraph
- list
- list item
- table
- table row
- table cell
- figure
- caption
- footnote
- reference
- unknown block

and attach evidence to each node, such as:

- page number
- bounding box
- font name/size/flags
- extraction source
- source confidence
- raw PDF references if needed

This is the stage where you turn “PDF evidence” into “document meaning.” `pdfminer.six` and `PyMuPDF` both expose block/line/span or layout-oriented information that is suitable for this normalization step, but neither one is your canonical semantic model for you. citeturn476064search16turn476064search18turn476064search19turn476064search1

### 4. Attach review flags

Also **your code**.

This is where you mark things like:

- heading confidence low
- list detection ambiguous
- table likely but not certain
- figure missing usable description
- reading order uncertain
- OCR source used
- non-Unicode text issue suspected
- manual review required

These flags should stay attached to the normalized nodes, not bolted on afterward. That way the DOCX projection can either:

- turn them into comments
- turn them into inline markers
- turn them into a review appendix/table

`python-docx` supports comments in the main document, and comment objects can contain paragraphs and tables, which makes it a good target for reviewer annotations. citeturn174814search0turn174814search3

### 5. Project to DOCX

Use `python-docx` here.

It is a library for **creating and updating** `.docx` files. It supports:

- opening and saving documents
- headings and paragraphs
- paragraph formatting
- built-in and custom styles
- numbering styles
- tables
- comments
- core properties like title, identifier, language, subject, version, etc. citeturn476064search0turn476064search4turn174814search2turn174814search7turn174814search1turn174814search3turn476064search8

That makes it the right endpoint for a reviewable Word projection.

## The strongest package mapping for your pipeline

### Input / raw inspection

- **pikepdf**
- **PyMuPDF**

### Extraction

- **PyMuPDF**
- **pdfminer.six**
- optional **pdfplumber** for table/debug passes

### Interpret / normalize

- **your own intermediate model**
- optional helper heuristics from `pdfminer.six` / `PyMuPDF`

### Review flags

- **your own rule engine**
- `python-docx` comments for human-visible review annotations

### DOCX projection

- **python-docx** citeturn476064search0turn476064search1turn476064search3turn174814search0turn174814search1

## What I would actually recommend

### Minimal serious version

- **Extract**
  - `PyMuPDF` for blocks/spans/images/links
  - `pdfminer.six` for text/layout cross-checks
- **Normalize**
  - your own JSON-like IR
- **Review flags**
  - your own deterministic rules
- **Project**
  - `python-docx`

This is the best balance if your goal is “practical and deep enough.”

### Heavier version

- add **pikepdf** if you also want:
  - raw object references
  - stream-level inspection
  - low-level PDF evidence preserved in the IR

That version makes sense if your review flags need to point back to PDF internals, not just page layout. citeturn476064search2turn476064search6

## The intermediate model matters more than the PDF library choice

This is the core design decision:

Do **not** project directly from extractor output to DOCX.

Instead:

- PDF
- extraction evidence
- **normalized document model**
- review flags
- DOCX projection

That separation will make the system much more stable, because PDF extraction libraries disagree at the edges, and DOCX is a structured authoring format with its own abstractions like paragraph styles, table styles, numbering, comments, and core properties. `python-docx` is built around those WordprocessingML-style structures rather than around PDF-like page operators. citeturn174814search2turn174814search4turn174814search8

## What “project to DOCX” should mean here

It should mean:

- headings become Word heading paragraphs/styles
- body text becomes paragraphs/runs
- lists become numbered or bulleted paragraphs
- tables become Word tables
- figures become images plus caption paragraphs
- review flags become comments or marked review text
- document metadata becomes DOCX core properties

`python-docx` explicitly supports paragraph, character, table, and numbering styles, tables, comments, and core document properties. citeturn174814search2turn174814search1turn174814search3turn476064search8

## The biggest limitation

The hard part is **Interpret / normalize**, not extraction and not DOCX writing.

Extraction libraries can give you:

- objects
- blocks
- spans
- fonts
- positions
- tagged contents
- content streams

and `python-docx` can write a real Word document.

But **you** still need to decide how PDF evidence becomes a normalized document structure. `pdfminer.six` explicitly notes that layout analysis is heuristic, and `PyMuPDF` notes that plain extraction may not come out in normal reading order without further work. citeturn476064search10turn476064search1

## Direct answer

If you wanted to do this in Python, I would use:

- **pikepdf** for raw PDF evidence when needed
- **PyMuPDF** as the main practical extractor
- **pdfminer.six** as the text/layout cross-checker
- **your own normalized IR**
- **your own review-flag rules**
- **python-docx** for DOCX output

That is the clean pipeline.

If you want, I’ll turn that into a **concrete field schema** for the normalized intermediate model.


#### You:
What about OCR AI models?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m checking the current OCR model landscape against your actual pipeline question: scanned PDFs, extraction quality, layout recovery, tables, and whether the models are local/open-source enough to fit the project.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## Yes — but only in the right place in the pipeline

For **your** pipeline, OCR AI models belong in **Input / Extract** as a **conditional branch for scanned or image-heavy PDFs**. They are not the default path for born-digital PDFs. Your uploaded guidance is explicit that image-based PDFs need OCR before they become accessible/useful, while PDFs created from accessible source documents should preserve real text and structure instead of being re-OCRed. fileciteturn0file2 fileciteturn0file3 fileciteturn0file1

So the clean rule is:

- **Born-digital PDF** → parse the PDF directly first.
- **Scanned / image PDF** → OCR model first, then normalize.
- **Mixed PDF** → direct parse for native text regions, OCR only for image regions/pages. fileciteturn0file2 fileciteturn0file3

## The best open-source OCR AI options for this project

### PaddleOCR

This is one of the strongest current open-source choices if you want a broad **document OCR + layout parsing** stack. The official docs and repo say it can convert PDFs and images into structured Markdown/JSON, and PP-StructureV3 is specifically for complex document parsing while preserving layout and hierarchy. citeturn481553search1turn481553search5turn481553search13

Use it for:

- scanned PDFs
- multilingual OCR
- layout-aware extraction
- tables and document structure
- producing intermediate Markdown/JSON before your own normalization layer citeturn481553search1turn481553search5

### Surya

Surya is a very strong fit for your kind of pipeline because it is not just OCR. Its official repo says it does OCR in 90+ languages, **layout analysis**, **reading order detection**, **table recognition**, and even **LaTeX OCR**. citeturn305442search4turn481553search2

Use it for:

- scanned/image PDFs
- mixed-layout pages
- reading-order-sensitive extraction
- tables and region classification
- feeding a normalized IR with stronger structural hints than plain OCR gives you citeturn481553search2

### docTR

docTR is a good open-source deep-learning OCR library when you want a more classic **detection + recognition** pipeline under your own control. Its official docs describe OCR as a two-stage process: detection and recognition, with configurable model choices. citeturn481553search0turn481553search4turn481553search12

Use it for:

- custom OCR pipelines
- projects where you want more control over detector/recognizer choices
- image/document OCR without needing a full PDF parsing platform around it citeturn481553search4turn481553search12

### olmOCR

olmOCR is very relevant for your project because it is explicitly about **PDF-to-clean-text linearization** with structured content preservation. The AllenAI repo describes it as a toolkit for converting PDFs and image-based document formats into clean readable text, and the paper says it preserves natural reading order plus structures like sections, tables, lists, and equations. citeturn481553search3turn481553search7turn481553search15

Use it for:

- large-scale PDF-to-text conversion
- difficult scanned or messy PDFs
- preserving reading order and structure in linearized text output
- a strong extraction branch before your normalize/review/DOCX stages citeturn481553search7turn481553search15

### GOT-OCR 2.0

GOT-OCR 2.0 is an end-to-end OCR model aimed at broader “OCR 2.0” tasks, not just plain text. The official repo and paper describe support for plain/formatted outputs and region-level OCR, with the model targeting text, formulas, tables, charts, and other structured visual content. citeturn305442search1turn305442search13

Use it for:

- experimental or advanced OCR-heavy pipelines
- structured visual content beyond plain text
- cases where you want one model to attempt broader perception tasks citeturn305442search13

### Nougat

Nougat is much narrower, but very good in its niche. The official repo and paper position it as an OCR/parser for **academic documents**, especially ones with math and tables, converting them into markup rather than plain text. citeturn305442search2turn305442search6turn305442search10

Use it for:

- research papers
- academic PDFs
- math-heavy scientific documents
- not as your universal OCR engine for all document types citeturn305442search2turn305442search6

### Marker

Marker is not “just an OCR model,” but it matters because it is a practical open-source document conversion pipeline. Its repo says it converts PDF and image inputs to Markdown/JSON/HTML and handles tables, forms, equations, links, references, and code blocks. But its own docs also say it works best on **digital PDFs** and uses limited OCR mainly to fix errors. citeturn305442search3turn305442search11

Use it for:

- digital PDFs first
- PDF-to-Markdown/JSON pipelines
- structured extraction before normalization
- not as your main heavy-scan OCR engine citeturn305442search11

## What I would actually use in your pipeline

### For scanned or image PDFs

The strongest candidates are:

- **PaddleOCR**
- **Surya**
- **olmOCR**

That is the serious shortlist for your use case, because they are aiming beyond plain OCR into layout, reading order, tables, and structured outputs. citeturn481553search1turn481553search5turn481553search2turn481553search7

### For born-digital PDFs

I would still **not** start with OCR models. I would start with native PDF extraction, then use OCR only where the PDF has image-only regions or missing text layers. Your uploaded accessibility guidance strongly supports that order. fileciteturn0file2 fileciteturn0file3

### For academic/scientific PDFs specifically

- **Nougat**
- sometimes **GOT-OCR 2.0**
- maybe **olmOCR** depending on whether you want plain-text linearization or markup-like reconstruction citeturn305442search2turn305442search13turn481553search7

## The main design warning

OCR AI models are good at:

- recovering text from images
- detecting lines/regions
- approximating reading order
- extracting tables and formulas in some cases

They are **not** your normalized semantic model. Even when a toolkit emits Markdown or JSON, I would still treat that as **extractor output**, not as your canonical representation. citeturn481553search5turn305442search3turn481553search7

So for your pipeline, the right architecture is still:

- **Input**
- **Native parse or OCR branch**
- **Interpret / normalize into your own IR**
- **Attach review flags**
- **Project to DOCX**

The OCR model sits in the extraction branch, not in the semantics layer. fileciteturn0file3

## Direct recommendation

If you want the shortest useful answer:

- **Best broad open-source OCR/document stack:** **PaddleOCR**
- **Best OCR + layout + reading order stack:** **Surya**
- **Best large-scale PDF linearization OCR stack:** **olmOCR**
- **Best academic-paper OCR stack:** **Nougat**
- **Best classic deep-learning OCR library:** **docTR**
- **Most experimental end-to-end OCR-2.0 option:** **GOT-OCR 2.0** citeturn481553search1turn481553search2turn481553search7turn305442search2turn481553search4turn305442search13

The next useful step is a matrix of these models against:

- scanned PDFs
- born-digital PDFs
- tables
- math
- reading order
- Markdown/JSON output
- local GPU friendliness
- where they fit in your pipeline


#### You:
And those use local AI models?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m checking which of those actually run with local weights versus calling hosted APIs, because that distinction matters a lot for how you architect the pipeline.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes — **most of the ones I listed are local-model tools**, meaning you can run the models on your own machine or your own server rather than calling a required hosted API.

## Direct breakdown

- **PaddleOCR** — **Yes**. It is an open-source toolkit with its own model library and docs for training, inference, and serving; the docs also explicitly mention **local deployment**. PaddleOCR also offers an API, but the core toolkit is runnable locally. citeturn197536search0turn197536search4turn197536search8
- **Surya** — **Yes**. The official repo presents it as a document OCR toolkit and separately mentions a managed API/on-prem platform, which implies the repo itself is the local/self-hosted path. citeturn197536search1
- **olmOCR** — **Yes**. The official repo is a toolkit you can run yourself, and there is also an online demo. There are current GitHub issues explicitly discussing differences between **online demo** and **local inference**, which confirms local runs are a real mode of use. citeturn197536search2turn197536search10turn197536search18
- **Nougat** — **Yes**. The official repo is the model/toolkit itself, and the project page describes it as a visual transformer OCR model for scientific documents. That is a local model workflow, even though there is also a Hugging Face Space demo. citeturn197536search3turn197536search7
- **docTR** — **Yes**. It is an open-source OCR library powered by PyTorch, and its docs show local inference directly in Python with `ocr_predictor(...)`. citeturn584741search0turn584741search2turn584741search6
- **GOT-OCR 2.0** — **Yes**. The official repo plus the Hugging Face model page both show local inference workflows, including running inference with Transformers on NVIDIA GPUs. citeturn584741search1turn584741search9

## The nuance that matters

“Uses local AI models” does **not** mean all of them are equally easy to run locally.

- **PaddleOCR** and **docTR** are more like conventional OCR toolkits/libraries. citeturn197536search4turn584741search2
- **Surya** is also a toolkit, but more document-layout-aware. citeturn197536search1
- **olmOCR**, **Nougat**, and **GOT-OCR 2.0** are more model-heavy and may be more GPU-hungry or specialized depending on the document type. The GOT-OCR 2.0 model page specifically documents GPU inference, and there are issues discussing CPU speed. citeturn197536search3turn584741search9turn584741search7

## The clean answer

If your actual question is:

> “Can these be part of a fully local pipeline instead of forcing me onto a hosted OCR API?”

Then the answer is:

**Yes — PaddleOCR, Surya, olmOCR, Nougat, docTR, and GOT-OCR 2.0 all have local/self-hosted model paths.** Some also offer demos or APIs, but they are not API-only products. citeturn197536search0turn197536search1turn197536search2turn197536search3turn584741search0turn584741search1

The most useful next step is probably a matrix of:

- **local CPU**
- **local GPU**
- **best for scanned PDFs**
- **best for born-digital PDFs**
- **best for tables/math/layout**
- **best output type: plain text vs Markdown vs JSON**


#### You:
how do I use each of them in python?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m checking the actual Python entry points for each one — some are true importable libraries, some are repo-first model code, and a couple are easier through scripts than a polished Python API.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes. Here’s the **direct Python usage map** for the local-model OCR tools we discussed.

## 1. PaddleOCR

### Install

```bash
pip install paddleocr
```

PaddleOCR’s current docs show a Python API centered on `PaddleOCR(...)` plus `.predict(...)`, and support passing a local config or local model directories. citeturn707030search3turn525746view0turn525746view1

### Minimal Python

```python
from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    # lang="en",           # optional
    # device="gpu",        # optional
)

results = ocr.predict("page.png")

for res in results:
    res.print()
    res.save_to_json("output")
    res.save_to_img("output")
```

### When to use it

Use PaddleOCR when you want a **document OCR toolkit** with a relatively polished Python API and structured output, especially for OCR-heavy extraction pipelines. citeturn525746view1turn525746view2

---

## 2. Surya

### Install

```bash
pip install surya-ocr
```

Surya’s repo says you need Python 3.10+ and PyTorch, and that model weights download automatically on first run. citeturn457853view1

### Minimal OCR in Python

```python
from PIL import Image
from surya.foundation import FoundationPredictor
from surya.recognition import RecognitionPredictor
from surya.detection import DetectionPredictor

image = Image.open("page.png")

foundation = FoundationPredictor()
recognizer = RecognitionPredictor(foundation)
detector = DetectionPredictor()

predictions = recognizer([image], det_predictor=detector)
```

### Layout analysis in Python

```python
from PIL import Image
from surya.foundation import FoundationPredictor
from surya.layout import LayoutPredictor
from surya.settings import settings

image = Image.open("page.png")

layout_predictor = LayoutPredictor(
    FoundationPredictor(checkpoint=settings.LAYOUT_MODEL_CHECKPOINT)
)
layout_predictions = layout_predictor([image])
```

### Table recognition in Python

```python
from PIL import Image
from surya.table_rec import TableRecPredictor

image = Image.open("page.png")
table_predictor = TableRecPredictor()
table_predictions = table_predictor([image])
```

### When to use it

Use Surya when you want **OCR + layout + reading-order/table signals** in one toolkit. Its repo explicitly presents those as core features. citeturn128876view0turn457853view0turn268635view3

---

## 3. olmOCR

### Install

For local GPU inference, the official repo documents:

```bash
pip install olmocr[gpu] --extra-index-url https://download.pytorch.org/whl/cu128
```

It also documents a lighter install for remote-inference mode:

```bash
pip install olmocr
```

and notes that local GPU inference needs a recent NVIDIA GPU with at least 12 GB VRAM and substantial disk space. citeturn457853view5turn895488view0

### Important caveat

The **official documented interface is CLI-first**, not a polished import-level Python API. The repo explicitly documents using:

- `olmocr ...`
- or `python -m olmocr.pipeline ...` citeturn457853view4turn895488view0

So in Python, the cleanest official path is to call it as a subprocess.

### Minimal Python via subprocess

```python
import subprocess

cmd = [
    "python", "-m", "olmocr.pipeline",
    "./localworkspace",
    "--markdown",
    "--pdfs", "input.pdf",
]
subprocess.run(cmd, check=True)
```

That will write results into the workspace directory, including Markdown output if `--markdown` is used. citeturn457853view4turn895488view0

### When to use it

Use olmOCR when you want **PDF/image → clean Markdown/plain-text linearization** with natural reading order and document cleanup. The repo explicitly frames it that way. citeturn128876view1turn895488view0

---

## 4. Nougat

### Install

```bash
pip install nougat-ocr
```

The official repo documents that package name directly. citeturn457853view7turn707030search2

### Option A: official CLI from Python

The official repo’s main usage path is CLI:

```python
import subprocess

subprocess.run(
    ["nougat", "paper.pdf", "-o", "output_dir"],
    check=True
)
```

The repo documents exactly that CLI pattern for PDF input. citeturn457853view7

### Option B: direct Python with Transformers

Hugging Face docs show Nougat being used as a `VisionEncoderDecoderModel` with `NougatProcessor`. That path works on **images/pages**, not directly on a PDF file object. citeturn878234view0

```python
from PIL import Image
from transformers import NougatProcessor, VisionEncoderDecoderModel
import torch

processor = NougatProcessor.from_pretrained("facebook/nougat-base")
model = VisionEncoderDecoderModel.from_pretrained("facebook/nougat-base")

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

image = Image.open("page.png").convert("RGB")
pixel_values = processor(image, return_tensors="pt").pixel_values.to(device)

outputs = model.generate(
    pixel_values,
    min_length=1,
    max_new_tokens=256,
    bad_words_ids=[[processor.tokenizer.unk_token_id]],
)

text = processor.batch_decode(outputs, skip_special_tokens=True)[0]
text = processor.post_process_generation(text, fix_markdown=False)
print(text)
```

### When to use it

Use Nougat for **academic/scientific PDFs**, especially when math and table understanding matter. The official repo explicitly says it is an academic document PDF parser and notes it works best on papers similar to arXiv/PMC content. citeturn128876view4turn878234view0

---

## 5. docTR

### Install

```bash
pip install python-doctr
```

The official docs and PyPI page both document `python-doctr` as the install name. citeturn707030search0turn707030search4

### Minimal Python

```python
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

model = ocr_predictor(pretrained=True)

doc = DocumentFile.from_pdf("input.pdf")
result = model(doc)

json_output = result.export()
print(json_output)
```

The official repo/docs also show:

- `DocumentFile.from_images(...)`
- `result.show()`
- `result.synthesize()` citeturn146504view2turn146504view3

### When to use it

Use docTR when you want a **clean Python OCR library** with a direct import API and a nested document output structure. It is one of the easiest to script directly in Python. citeturn128876view5turn146504view2

---

## 6. GOT-OCR 2.0

### Install

The official repo documents repo install rather than a simple pip package flow:

```bash
git clone https://github.com/Ucas-HaoranWei/GOT-OCR2.0.git
cd GOT-OCR2.0
pip install -e .
pip install ninja
pip install flash-attn --no-build-isolation
```

The repo also notes its environment assumptions around CUDA and Torch. citeturn146504view4

### Option A: official repo script from Python

The repo’s documented inference path is script-first:

```python
import subprocess

subprocess.run(
    [
        "python3", "GOT/demo/run_ocr_2.0.py",
        "--model-name", "/path/to/GOT_weights/",
        "--image-file", "page.png",
        "--type", "ocr",
    ],
    check=True
)
```

The repo documents `--type ocr`, `--type format`, region-box OCR, and render modes. citeturn146504view4

### Option B: direct Python with Transformers

Hugging Face documents direct Python inference with `AutoProcessor` and `AutoModelForImageTextToText`. It also notes that this Transformers implementation currently outputs **plain text**, even when the original task is richer. citeturn128876view8

```python
import torch
from transformers import AutoProcessor, AutoModelForImageTextToText

model_id = "stepfun-ai/GOT-OCR-2.0-hf"
device = "cuda" if torch.cuda.is_available() else "cpu"

processor = AutoProcessor.from_pretrained(model_id, use_fast=True)
model = AutoModelForImageTextToText.from_pretrained(model_id).to(device)

inputs = processor("page.png", return_tensors="pt").to(device)
outputs = model.generate(**inputs, max_new_tokens=256)
text = processor.batch_decode(outputs, skip_special_tokens=True)[0]
print(text)
```

### When to use it

Use GOT-OCR 2.0 when you want a **more general OCR-2.0 style model** that can target broader structured visual content, and you are comfortable with a heavier model workflow. citeturn128876view8turn146504view4

---

## Which ones feel most natural **inside Python**?

From easiest to most awkward as a Python import workflow:

1. **docTR**
2. **PaddleOCR**
3. **Surya**
4. **Nougat** via Transformers
5. **GOT-OCR 2.0** via Transformers
6. **olmOCR**
   - because the official path is really **CLI/subprocess-first**, not “import a stable predictor object” citeturn146504view2turn525746view1turn457853view0turn895488view0

## My practical recommendation for your pipeline

If you want a Python-native branch that feels least annoying:

- **docTR** for straightforward OCR-in-Python
- **Surya** if layout/reading order/tables matter more
- **PaddleOCR** if you want a broader OCR toolkit with a more productized API
- **Nougat** only for scientific PDFs
- **olmOCR** when you want a strong CLI-driven conversion stage
- **GOT-OCR 2.0** when you want a heavier general VLM-style OCR path citeturn128876view0turn146504view2turn525746view1turn128876view8

If you want, I’ll turn this into a **copy-paste starter file for each one** that takes `input.pdf` or `page.png` and emits JSON/text in a consistent schema.


#### You:
What about AI models for recognizing text and extracting text from images?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m answering this as the broader OCR-model question now, not just PDFs: plain OCR, scene text, document OCR, handwriting, layout-aware models, and multimodal “read the image” models.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes. The clean way to think about it is:

## There are three different model types

### 1. Classic OCR pipelines

These do:

- **text detection**: where the text is
- **text recognition**: what the text says

Best when you want:

- predictable OCR
- local use
- structured outputs
- speed

Main options:

- **PaddleOCR**\
  Broad document OCR toolkit. The official repo says it converts PDFs and images into structured data, and supports document orientation, layout parsing, tables, and OCR pipelines. citeturn333577search20

- **docTR**\
  A two-stage detection + recognition OCR library. Its docs explicitly describe “robust 2-stage (detection + recognition) OCR predictors” and a simple Python API. citeturn333577search5turn333577search1

- **EasyOCR**\
  A ready-to-use OCR library for images, with support for 80+ languages and both scene text and dense document text. citeturn241231search2turn241231search10

- **keras-ocr**\
  More classic detection/recognition pipeline territory. Its docs describe it as out-of-the-box OCR models plus an end-to-end training pipeline, built around CRAFT-style detection and CRNN-style recognition. citeturn241231search19turn241231search3

### 2. Document-understanding OCR toolkits

These go beyond “read text” and also try to recover:

- layout
- reading order
- tables
- region types
- sometimes formulas

Best when you want:

- OCR plus document structure
- scanned documents
- reviewable structured extraction

Main options:

- **Surya**\
  The official repo says it does OCR in 90+ languages, line-level text detection, layout analysis, reading order detection, table recognition, and LaTeX OCR. citeturn333577search0

- **PaddleOCR** again\
  It overlaps this category because it is more than a plain OCR recognizer; it also has document-structure capabilities. citeturn333577search20

- **Nougat**\
  Narrower, but strong for academic/scientific documents. Its official repo describes it as an academic document PDF parser that understands LaTeX math and tables. citeturn333577search2turn333577search6

### 3. End-to-end vision-language OCR models

These treat OCR less like “detect + recognize characters” and more like:

- “look at this image/document and produce text or markup”

Best when you want:

- harder document understanding
- math/tables/markup
- experimental broader visual parsing

Main options:

- **TrOCR**\
  Microsoft’s transformer OCR model. The official docs describe it as an end-to-end text recognition model using a vision encoder and text decoder. citeturn241231search1turn241231search13

- **GOT-OCR 2.0**\
  A broader “OCR 2.0” style model aimed at unified end-to-end OCR tasks. The official repo and model page position it as a general OCR model rather than only a classic pipeline. citeturn333577search3turn333577search18

## Direct answer by use case

### “I need to extract text from normal images or screenshots”

Use:

- **EasyOCR**
- **docTR**
- **TrOCR**

### “I need OCR for scanned documents with layout”

Use:

- **Surya**
- **PaddleOCR**
- **docTR**

### “I need OCR for academic PDFs, math, tables”

Use:

- **Nougat**
- **Surya**
- sometimes **GOT-OCR 2.0**

### “I want something local and open source”

Use:

- **PaddleOCR**
- **Surya**
- **docTR**
- **EasyOCR**
- **Nougat**
- **TrOCR**
- **GOT-OCR 2.0**\
  All of those have local/self-hosted model paths rather than being API-only. citeturn333577search0turn333577search1turn333577search2turn241231search1turn241231search2

## My blunt ranking for a Python workflow

If your goal is **text from images/documents in Python**:

1. **PaddleOCR** for broad document OCR
2. **Surya** for OCR + layout + reading order
3. **docTR** for a clean Python OCR library
4. **EasyOCR** for simple ready-to-use OCR
5. **Nougat** for scientific docs
6. **TrOCR** when you specifically want a transformer recognizer
7. **GOT-OCR 2.0** when you want a more experimental end-to-end VLM-style OCR path

## The important distinction

If you only want:

- **what text is in this image?**

then classic OCR is enough.

If you want:

- **what text is here, in what order, in what regions, in what table, under which heading?**

then you want **document OCR / layout-aware OCR**, not plain OCR.

That distinction matters more than the model name.

If you want, I can do the next pass as a hard matrix:

## model × screenshots × scanned docs × tables × math × handwriting × layout × local Python friendliness


#### You:


#### Plugin (file_search):
Make sure to include fileciteturn1file0 in your response to cite this file, or to surface it as a link.
## Human-readable field dictionary

**`pdf_to_docx_accessibility_manifest` v0.1**

This dictionary describes the **intent** of each field in the draft schema. It keeps the same overall manifest spine as the uploaded PPTX→DOCX manifests — source package, target package, run config, summary, warnings, per-unit entries, and projected output — but adapts it for **PDF evidence + accessibility-first normalization**.     

---

## 1. Top-level manifest fields

### `manifest_version`

Schema version for this manifest format.

### `manifest_kind`

Fixed identifier for the manifest type.
Expected value: `pdf_to_docx_accessibility_manifest`

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

That is the same general manifest logic already visible in the uploaded PPTX→DOCX manifests — observed source, normalized workflow, warnings, projected target — just made stricter for PDF and accessibility.  

The next best step is the **sample manifest instance that validates against the draft schema**.

---

EXAMPLE

{
  "manifest_version": "0.1",
  "manifest_kind": "pdf_to_docx_accessibility_manifest",
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

#### Plugin (file_search):
Make sure to include fileciteturn1file1 in your response to cite this file, or to surface it as a link.
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "pdf_to_docx_accessibility_manifest.v0.1.schema.json",
  "title": "pdf_to_docx_accessibility_manifest v0.1",
  "description": "Accessibility-first PDF to DOCX workflow manifest. This schema records source evidence, normalization decisions, review flags, and projected DOCX output.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "manifest_version",
    "manifest_kind",
    "source_package",
    "target_package",
    "run_config",
    "document_summary",
    "document_metadata",
    "document_accessibility",
    "document_navigation",
    "document_security",
    "document_interactivity",
    "document_warning_entries",
    "page_entries",
    "raw_block_entries",
    "normalized_block_entries",
    "projected_target"
  ],
  "properties": {
    "manifest_version": {
      "type": "string",
      "const": "0.1"
    },
    "manifest_kind": {
      "type": "string",
      "const": "pdf_to_docx_accessibility_manifest"
    },
    "source_package": {
      "$ref": "#/$defs/source_package"
    },
    "target_package": {
      "$ref": "#/$defs/target_package"
    },
    "run_config": {
      "$ref": "#/$defs/run_config"
    },
    "document_summary": {
      "$ref": "#/$defs/document_summary"
    },
    "document_metadata": {
      "$ref": "#/$defs/document_metadata"
    },
    "document_accessibility": {
      "$ref": "#/$defs/document_accessibility"
    },
    "document_navigation": {
      "$ref": "#/$defs/document_navigation"
    },
    "document_security": {
      "$ref": "#/$defs/document_security"
    },
    "document_interactivity": {
      "$ref": "#/$defs/document_interactivity"
    },
    "document_warning_entries": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/warning_entry"
      }
    },
    "page_entries": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/page_entry"
      }
    },
    "raw_block_entries": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/raw_block_entry"
      }
    },
    "normalized_block_entries": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/normalized_block_entry"
      }
    },
    "projected_target": {
      "$ref": "#/$defs/projected_target"
    }
  },
  "$defs": {
    "nullable_string": {
      "type": [
        "string",
        "null"
      ]
    },
    "nullable_boolean": {
      "type": [
        "boolean",
        "null"
      ]
    },
    "nullable_integer": {
      "type": [
        "integer",
        "null"
      ]
    },
    "nullable_number": {
      "type": [
        "number",
        "null"
      ]
    },
    "bbox": {
      "type": [
        "array",
        "null"
      ],
      "minItems": 4,
      "maxItems": 4,
      "items": {
        "type": "number"
      }
    },
    "warning_entry": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "warning_code",
        "warning_message",
        "warning_scope",
        "manual_review_required"
      ],
      "properties": {
        "warning_code": {
          "type": "string"
        },
        "warning_message": {
          "type": "string"
        },
        "warning_scope": {
          "type": "string",
          "enum": [
            "document",
            "page",
            "block",
            "annotation",
            "figure",
            "form",
            "navigation",
            "security",
            "metadata",
            "ocr",
            "reading_order"
          ]
        },
        "warning_severity": {
          "type": "string",
          "enum": [
            "info",
            "warning",
            "error"
          ],
          "default": "warning"
        },
        "manual_review_required": {
          "type": "boolean"
        }
      }
    },
    "source_package": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "format_family",
        "input_file_name",
        "input_file_path",
        "page_count",
        "document_fingerprints"
      ],
      "properties": {
        "format_family": {
          "type": "string",
          "const": "PDF"
        },
        "input_file_name": {
          "type": "string"
        },
        "input_file_path": {
          "type": "string"
        },
        "page_count": {
          "type": "integer",
          "minimum": 1
        },
        "document_fingerprints": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 1,
          "maxItems": 2
        },
        "byte_length": {
          "$ref": "#/$defs/nullable_integer"
        }
      }
    },
    "target_package": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "format_family",
        "package_model",
        "document_vocabulary",
        "draft_output_file_name",
        "draft_output_file_path"
      ],
      "properties": {
        "format_family": {
          "type": "string",
          "const": "OOXML"
        },
        "package_model": {
          "type": "string",
          "const": "OPC"
        },
        "document_vocabulary": {
          "type": "string",
          "const": "WordprocessingML"
        },
        "draft_output_file_name": {
          "type": "string"
        },
        "draft_output_file_path": {
          "type": "string"
        }
      }
    },
    "run_config": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "include_preview_images",
        "preview_image_dir",
        "page_separator_mode",
        "include_warning_appendix",
        "include_page_traceback",
        "prefer_outline_for_headings"
      ],
      "properties": {
        "include_preview_images": {
          "type": "boolean"
        },
        "preview_image_dir": {
          "$ref": "#/$defs/nullable_string"
        },
        "page_separator_mode": {
          "type": "string",
          "enum": [
            "PAGE_BREAK",
            "SECTION_BREAK",
            "NONE"
          ]
        },
        "include_warning_appendix": {
          "type": "boolean"
        },
        "include_page_traceback": {
          "type": "boolean"
        },
        "prefer_outline_for_headings": {
          "type": "boolean"
        }
      }
    },
    "document_summary": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "total_pages",
        "pages_with_warnings",
        "raw_block_count",
        "normalized_block_count",
        "annotation_count",
        "form_field_count",
        "figure_candidate_count"
      ],
      "properties": {
        "total_pages": {
          "type": "integer",
          "minimum": 1
        },
        "pages_with_warnings": {
          "type": "integer",
          "minimum": 0
        },
        "raw_block_count": {
          "type": "integer",
          "minimum": 0
        },
        "normalized_block_count": {
          "type": "integer",
          "minimum": 0
        },
        "annotation_count": {
          "type": "integer",
          "minimum": 0
        },
        "form_field_count": {
          "type": "integer",
          "minimum": 0
        },
        "figure_candidate_count": {
          "type": "integer",
          "minimum": 0
        }
      }
    },
    "document_metadata": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "info",
        "xmp_present",
        "title",
        "author",
        "subject",
        "keywords",
        "language"
      ],
      "properties": {
        "info": {
          "type": [
            "object",
            "null"
          ],
          "additionalProperties": true
        },
        "xmp_present": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "title": {
          "$ref": "#/$defs/nullable_string"
        },
        "author": {
          "$ref": "#/$defs/nullable_string"
        },
        "subject": {
          "$ref": "#/$defs/nullable_string"
        },
        "keywords": {
          "type": [
            "array",
            "null"
          ],
          "items": {
            "type": "string"
          }
        },
        "language": {
          "$ref": "#/$defs/nullable_string"
        }
      }
    },
    "document_accessibility": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "mark_info",
        "tagged_pdf_detected",
        "struct_tree_detected",
        "image_only_pages_present",
        "ocr_required",
        "ocr_detected",
        "reading_order_source"
      ],
      "properties": {
        "mark_info": {
          "type": [
            "object",
            "null"
          ],
          "additionalProperties": true
        },
        "tagged_pdf_detected": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "struct_tree_detected": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "image_only_pages_present": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "ocr_required": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "ocr_detected": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "reading_order_source": {
          "type": [
            "string",
            "null"
          ],
          "enum": [
            "tag_tree",
            "layout_inference",
            "mixed",
            "unknown",
            null
          ]
        }
      }
    },
    "document_navigation": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "outline_present",
        "outline_entries",
        "page_labels",
        "named_destinations_present",
        "named_destinations",
        "viewer_preferences",
        "page_layout",
        "page_mode"
      ],
      "properties": {
        "outline_present": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "outline_entries": {
          "type": [
            "array",
            "null"
          ],
          "items": {
            "$ref": "#/$defs/outline_entry"
          }
        },
        "page_labels": {
          "type": [
            "array",
            "null"
          ],
          "items": {
            "type": "string"
          }
        },
        "named_destinations_present": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "named_destinations": {
          "type": [
            "object",
            "null"
          ],
          "additionalProperties": true
        },
        "viewer_preferences": {
          "type": [
            "object",
            "null"
          ],
          "additionalProperties": true
        },
        "page_layout": {
          "$ref": "#/$defs/nullable_string"
        },
        "page_mode": {
          "$ref": "#/$defs/nullable_string"
        }
      }
    },
    "document_security": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "permissions"
      ],
      "properties": {
        "permissions": {
          "type": [
            "array",
            "null"
          ],
          "items": {
            "type": [
              "integer",
              "string"
            ]
          }
        }
      }
    },
    "document_interactivity": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "javascript_present",
        "javascript_actions",
        "forms_present",
        "form_fields",
        "calculation_order_ids",
        "xfa_present",
        "is_pure_xfa",
        "all_xfa_html"
      ],
      "properties": {
        "javascript_present": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "javascript_actions": {
          "type": [
            "object",
            "null"
          ],
          "additionalProperties": true
        },
        "forms_present": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "form_fields": {
          "type": [
            "object",
            "null"
          ],
          "additionalProperties": true
        },
        "calculation_order_ids": {
          "type": [
            "array",
            "null"
          ],
          "items": {
            "type": "string"
          }
        },
        "xfa_present": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "is_pure_xfa": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "all_xfa_html": {
          "type": [
            "object",
            "array",
            "null"
          ]
        }
      }
    },
    "outline_entry": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "title"
      ],
      "properties": {
        "title": {
          "type": "string"
        },
        "dest": {
          "type": [
            "string",
            "array",
            "null"
          ]
        },
        "url": {
          "$ref": "#/$defs/nullable_string"
        },
        "items": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/outline_entry"
          }
        }
      }
    },
    "page_entry": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "page_number",
        "observed_source",
        "struct_tree",
        "annotation_entries",
        "xfa_entries",
        "operator_evidence",
        "warning_entries"
      ],
      "properties": {
        "page_number": {
          "type": "integer",
          "minimum": 1
        },
        "observed_source": {
          "$ref": "#/$defs/page_observed_source"
        },
        "struct_tree": {
          "type": [
            "object",
            "array",
            "null"
          ]
        },
        "annotation_entries": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/annotation_entry"
          }
        },
        "xfa_entries": {
          "type": [
            "object",
            "array",
            "null"
          ]
        },
        "operator_evidence": {
          "type": [
            "object",
            "array",
            "null"
          ]
        },
        "warning_entries": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/warning_entry"
          }
        }
      }
    },
    "page_observed_source": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "page_ref",
        "page_rotation",
        "user_unit",
        "page_bbox",
        "viewport",
        "struct_tree_present",
        "text_layer_detected",
        "image_only_page_suspected",
        "ocr_text_detected",
        "annotation_count",
        "form_field_count",
        "xfa_present",
        "operator_list_present",
        "page_label"
      ],
      "properties": {
        "page_ref": {
          "$ref": "#/$defs/nullable_string"
        },
        "page_rotation": {
          "$ref": "#/$defs/nullable_number"
        },
        "user_unit": {
          "$ref": "#/$defs/nullable_number"
        },
        "page_bbox": {
          "$ref": "#/$defs/bbox"
        },
        "viewport": {
          "type": [
            "object",
            "null"
          ],
          "additionalProperties": true
        },
        "struct_tree_present": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "text_layer_detected": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "image_only_page_suspected": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "ocr_text_detected": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "annotation_count": {
          "type": "integer",
          "minimum": 0
        },
        "form_field_count": {
          "type": "integer",
          "minimum": 0
        },
        "xfa_present": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "operator_list_present": {
          "$ref": "#/$defs/nullable_boolean"
        },
        "page_label": {
          "$ref": "#/$defs/nullable_string"
        }
      }
    },
    "annotation_entry": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "annotation_subtype",
        "contents",
        "alt_text",
        "url",
        "dest",
        "manual_review_required"
      ],
      "properties": {
        "annotation_subtype": {
          "$ref": "#/$defs/nullable_string"
        },
        "contents": {
          "$ref": "#/$defs/nullable_string"
        },
        "alt_text": {
          "$ref": "#/$defs/nullable_string"
        },
        "url": {
          "$ref": "#/$defs/nullable_string"
        },
        "dest": {
          "type": [
            "string",
            "array",
            "null"
          ]
        },
        "manual_review_required": {
          "type": "boolean"
        }
      }
    },
    "raw_block_entry": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "block_id",
        "page_number",
        "source_evidence_type",
        "source_ref",
        "bbox",
        "text",
        "text_items",
        "style_hints",
        "structure_hints",
        "role_basis",
        "manual_review_required",
        "warning_entries"
      ],
      "properties": {
        "block_id": {
          "type": "string"
        },
        "page_number": {
          "type": "integer",
          "minimum": 1
        },
        "source_evidence_type": {
          "type": "string",
          "enum": [
            "tagged_text",
            "untagged_text",
            "ocr_text",
            "annotation_text",
            "form_field_text",
            "xfa_text",
            "outline_text",
            "artifact_text",
            "unknown"
          ]
        },
        "source_ref": {
          "$ref": "#/$defs/nullable_string"
        },
        "bbox": {
          "$ref": "#/$defs/bbox"
        },
        "text": {
          "type": "string"
        },
        "text_items": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/text_item"
          }
        },
        "style_hints": {
          "$ref": "#/$defs/style_hints"
        },
        "structure_hints": {
          "$ref": "#/$defs/structure_hints"
        },
        "role_basis": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "manual_review_required": {
          "type": "boolean"
        },
        "warning_entries": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/warning_entry"
          }
        }
      }
    },
    "text_item": {
      "type": "object",
      "additionalProperties": true,
      "properties": {
        "str": {
          "type": "string"
        },
        "dir": {
          "$ref": "#/$defs/nullable_string"
        },
        "width": {
          "$ref": "#/$defs/nullable_number"
        },
        "height": {
          "$ref": "#/$defs/nullable_number"
        },
        "fontName": {
          "$ref": "#/$defs/nullable_string"
        },
        "transform": {
          "type": [
            "array",
            "null"
          ],
          "items": {
            "type": "number"
          }
        }
      }
    },
    "style_hints": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "font_name",
        "font_size",
        "font_weight",
        "font_style"
      ],
      "properties": {
        "font_name": {
          "$ref": "#/$defs/nullable_string"
        },
        "font_size": {
          "$ref": "#/$defs/nullable_number"
        },
        "font_weight": {
          "$ref": "#/$defs/nullable_string"
        },
        "font_style": {
          "$ref": "#/$defs/nullable_string"
        }
      }
    },
    "structure_hints": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "tag_name",
        "parent_tag_name",
        "mcid",
        "language"
      ],
      "properties": {
        "tag_name": {
          "$ref": "#/$defs/nullable_string"
        },
        "parent_tag_name": {
          "$ref": "#/$defs/nullable_string"
        },
        "mcid": {
          "$ref": "#/$defs/nullable_integer"
        },
        "language": {
          "$ref": "#/$defs/nullable_string"
        }
      }
    },
    "normalized_block_entry": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "block_id",
        "page_span",
        "observed_source_refs",
        "normalized_workflow",
        "warning_entries",
        "projected_target"
      ],
      "properties": {
        "block_id": {
          "type": "string"
        },
        "page_span": {
          "type": "array",
          "minItems": 2,
          "maxItems": 2,
          "items": {
            "type": "integer",
            "minimum": 1
          }
        },
        "observed_source_refs": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "normalized_workflow": {
          "$ref": "#/$defs/normalized_workflow"
        },
        "warning_entries": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/warning_entry"
          }
        },
        "projected_target": {
          "$ref": "#/$defs/block_projected_target"
        }
      }
    },
    "normalized_workflow": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "interpreted_role",
        "heading_level",
        "list_kind",
        "role_confidence",
        "semantic_source_quality",
        "role_basis",
        "reading_order_index",
        "reading_order_basis",
        "manual_review_required"
      ],
      "properties": {
        "interpreted_role": {
          "type": "string",
          "enum": [
            "heading",
            "paragraph",
            "list",
            "list_item",
            "table",
            "table_row",
            "table_cell",
            "figure",
            "caption",
            "link",
            "form_field",
            "note",
            "artifact",
            "unknown"
          ]
        },
        "heading_level": {
          "$ref": "#/$defs/nullable_integer"
        },
        "list_kind": {
          "type": [
            "string",
            "null"
          ],
          "enum": [
            "plain",
            "bullet",
            "number",
            "unknown",
            null
          ]
        },
        "role_confidence": {
          "type": "string",
          "enum": [
            "high",
            "medium",
            "low",
            "unknown"
          ]
        },
        "semantic_source_quality": {
          "type": "string",
          "enum": [
            "high",
            "medium",
            "low",
            "unknown"
          ]
        },
        "role_basis": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "reading_order_index": {
          "$ref": "#/$defs/nullable_integer"
        },
        "reading_order_basis": {
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "manual_review_required": {
          "type": "boolean"
        }
      }
    },
    "block_projected_target": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "target_package_part",
        "target_style",
        "target_heading_text",
        "target_list_kind",
        "target_table_id",
        "projection_status"
      ],
      "properties": {
        "target_package_part": {
          "type": "string"
        },
        "target_style": {
          "$ref": "#/$defs/nullable_string"
        },
        "target_heading_text": {
          "$ref": "#/$defs/nullable_string"
        },
        "target_list_kind": {
          "$ref": "#/$defs/nullable_string"
        },
        "target_table_id": {
          "$ref": "#/$defs/nullable_string"
        },
        "projection_status": {
          "type": "string",
          "enum": [
            "planned",
            "appendix_only",
            "omitted",
            "unknown"
          ]
        }
      }
    },
    "projected_target": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "target_package_part",
        "document_title_strategy",
        "page_separator_mode",
        "include_warning_appendix",
        "projection_status"
      ],
      "properties": {
        "target_package_part": {
          "type": "string",
          "const": "word/document.xml"
        },
        "document_title_strategy": {
          "type": "string",
          "enum": [
            "metadata_title",
            "outline_title",
            "first_heading",
            "manual_review"
          ]
        },
        "page_separator_mode": {
          "type": "string",
          "enum": [
            "PAGE_BREAK",
            "SECTION_BREAK",
            "NONE"
          ]
        },
        "include_warning_appendix": {
          "type": "boolean"
        },
        "projection_status": {
          "type": "string",
          "enum": [
            "planned",
            "drafted",
            "manual_review_required"
          ]
        }
      }
    }
  }
}

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
These uploads are the first thing in this thread that actually feel like a **real canonical contract** for the pipeline.

## What they give us

They map almost exactly onto the workflow you described:

### Input

- `source_package`
- `target_package`
- `run_config` fileciteturn1file0 fileciteturn1file1

### Extract

- `document_metadata`
- `document_accessibility`
- `document_navigation`
- `document_security`
- `document_interactivity`
- `page_entries`
- `raw_block_entries` fileciteturn1file0 fileciteturn1file1

### Interpret / normalize

- `normalized_block_entries`
- `normalized_workflow`
- `interpreted_role`
- `role_confidence`
- `semantic_source_quality`
- `reading_order_index`
- `reading_order_basis` fileciteturn1file0 fileciteturn1file1

### Attach review flags

- `document_warning_entries`
- per-page `warning_entries`
- per-block `warning_entries`
- `manual_review_required` at multiple levels fileciteturn1file0 fileciteturn1file1

### Project to DOCX

- block-level `projected_target`
- top-level `projected_target`
- `target_style`
- `target_heading_text`
- `target_list_kind`
- `target_table_id`
- `document_title_strategy`
- `page_separator_mode` fileciteturn1file0 fileciteturn1file1

## Why this is actually good

The design logic in the field dictionary is the right one:

- **what the PDF literally gave us**
- **what we think it means**
- **how confident we are**
- **what DOCX output we plan to create** fileciteturn1file0

That is the correct separation. It prevents the classic mess where extraction evidence, interpretation, and output decisions get collapsed into one blurry intermediate blob.

## What this means for the Python stack

With this manifest as the contract, the tooling question gets much cleaner:

### Extraction layer

Best candidates:

- `PyMuPDF`
- `pdfminer.six`
- `pikepdf`

Because the schema explicitly wants evidence like:

- page refs
- page rotation / bbox / viewport
- struct tree presence
- operator evidence
- annotations
- XFA
- text items
- style hints
- structure hints
- MCIDs
- navigation and destinations fileciteturn1file0 fileciteturn1file1

### Interpretation layer

This should be **your code**, producing:

- `interpreted_role`
- `heading_level`
- `list_kind`
- `role_confidence`
- `semantic_source_quality`
- `reading_order_index`
- `manual_review_required` fileciteturn1file0 fileciteturn1file1

### DOCX projection layer

This should be **your code plus `python-docx`**, driven by:

- `target_style`
- `target_heading_text`
- `target_list_kind`
- `target_table_id`
- `projection_status` fileciteturn1file0 fileciteturn1file1

## My blunt read

This manifest is good enough to become the **canonical intermediate representation** for the project.

Not because it is perfect, but because it already has the right backbone:

- source evidence
- normalized meaning
- review flags
- projected output

That is the exact architecture we kept circling around.

## The next correct move

Use these files as the contract and stop talking abstractly.

Build the pipeline around this manifest:

1. **Extractor adapters** that populate the evidence fields.
2. **Normalizer rules** that turn raw blocks into normalized blocks.
3. **Review-flag rules** that populate warnings and `manual_review_required`.
4. **DOCX projector** that consumes only normalized blocks + projected target fields.

That gives you one canonical spine instead of tool-specific chaos.


#### You:
the manifest was created using what's available from PDF.js. We need the pyuthon version

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m translating the manifest from a **PDF.js-shaped evidence model** into a **Python extractor-shaped evidence model**. The key move is keeping the manifest spine and swapping out the fields that are accidentally tied to PDF.js APIs.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes. The current manifest is **PDF.js-shaped**, not extractor-neutral. Your own field dictionary says `text_items` are “individual extracted text pieces from PDF.js,” and the sample manifest also treats `operator_evidence` as PDF.js-style operator-list evidence. fileciteturn1file0 fileciteturn1file1

## The right fix

Do **not** make a “PyMuPDF manifest” or a “pdfminer manifest.”

Make a **Python extractor-neutral manifest** with:

- the same top-level spine you already have
- generic evidence field names
- per-extractor namespaces for raw evidence
- one normalized layer above them

That lets you use **PyMuPDF** for xref/page/resource evidence, **pikepdf** for object/stream evidence, **pypdf** for metadata/navigation/security, and **pdfminer.six** for character/layout evidence without distorting the schema around one library’s API. PyMuPDF exposes xref/object/stream access and page-level methods like `get_links()`, `get_images()`, and `get_fonts()`; pikepdf exposes content-stream parsing and PDF-object access; pypdf exposes metadata, outline, named destinations, page labels, and page layout; pdfminer.six exposes character/font/size/layout extraction. citeturn825997search0turn825997search1turn825997search2turn825997search3turn825997search4turn825997search5turn825997search7

## What to keep exactly as-is

These sections are already good and should stay:

- `source_package`
- `target_package`
- `run_config`
- `document_summary`
- `document_metadata`
- `document_accessibility`
- `document_navigation`
- `document_security`
- `document_interactivity`
- `document_warning_entries`
- `page_entries`
- `raw_block_entries`
- `normalized_block_entries`
- `projected_target` fileciteturn1file0 fileciteturn1file1

That spine is already the correct architecture:

- what the PDF literally gave us
- what we think it means
- how confident we are
- what DOCX we plan to create fileciteturn1file0

## What to rename because it is too PDF.js-specific

| Current field               | Problem                                                 | Python-native replacement                            | Primary source(s)         |
| --------------------------- | ------------------------------------------------------- | ---------------------------------------------------- | ------------------------- |
| `text_items`                | Explicitly defined as PDF.js items                      | `text_spans`                                         | `pdfminer.six`, `PyMuPDF` |
| `operator_evidence`         | Implies PDF.js operator list arrays                     | `content_stream_evidence`                            | `pikepdf`, `PyMuPDF`      |
| `viewport`                  | PDF.js rendering term                                   | `page_geometry`                                      | `PyMuPDF`, `pypdf`        |
| `operator_list_present`     | Tied to PDF.js operator list concept                    | `content_stream_parsed`                              | `pikepdf`, `PyMuPDF`      |
| `source_evidence_type` enum | Too centered on PDF.js-style text extraction categories | Keep field, expand enum and add extractor provenance | all                       |
| `structure_hints`           | Fine name, but too thin for Python evidence             | keep name, add extractor/object refs                 | `pikepdf`, `PyMuPDF`      |

The main reason for `text_spans` is that pdfminer.six gives you character- and layout-level objects like `LTChar` with font name and size, while PyMuPDF gives page/text extraction and tracing APIs; neither is literally returning PDF.js `textItems`. citeturn825997search3turn825997search7turn825997search0turn825997search4

## What to add

### 1. Add extractor provenance everywhere

At minimum add:

```json id="i5slce"
"extractor_provenance": {
  "primary_extractor": "pymupdf",
  "secondary_extractors": ["pdfminer.six", "pikepdf", "pypdf"],
  "extractor_versions": {},
  "notes": []
}
```

This matters because the same block may come from:

- pdfminer layout analysis
- PyMuPDF text extraction
- pikepdf structure/object inspection
- pypdf metadata/navigation inspection

### 2. Add per-extractor evidence namespaces

For pages and blocks, add:

```json id="znl6jp"
"extractor_evidence": {
  "pymupdf": {},
  "pdfminer": {},
  "pikepdf": {},
  "pypdf": {}
}
```

That prevents the manifest from forcing one extractor’s vocabulary onto all evidence.

### 3. Add stable PDF object references where possible

For page-level and block-level evidence, add fields like:

```json id="l9xsyu"
"object_ref": null,
"xref": null,
"mcid": null,
"content_stream_refs": [],
"struct_parent_ref": null
```

This is the Python version of “traceability back to the file internals.” PyMuPDF exposes xref/object/stream access, and pikepdf mirrors PDF objects closely enough that carrying object references makes sense. citeturn825997search0turn825997search5

## The Python-native replacements, section by section

### `page_entries[].observed_source`

Keep the section, but change the internal fields.

#### Replace

- `viewport`

#### With

- `page_geometry`
- `cropbox`
- `mediabox`
- `rotation`
- `user_unit`

Why: `viewport` is a PDF.js rendering abstraction. For Python, the stable concepts are PDF page geometry plus any renderer-specific transform if you actually rasterize the page. PyMuPDF and pypdf both expose page and document geometry/layout concepts without needing the PDF.js viewport vocabulary. citeturn825997search0turn825997search2

Suggested shape:

```json id="1pgipw"
"page_geometry": {
  "mediabox": [0, 0, 612, 792],
  "cropbox": [0, 0, 612, 792],
  "rotation": 0,
  "user_unit": 1
}
```

### `page_entries[].operator_evidence`

Rename to:

```json id="fkyjlwm"
"content_stream_evidence": {
  "content_stream_parsed": true,
  "extractor": "pikepdf",
  "stream_count": 1,
  "operator_summary": {},
  "raw_stream_refs": []
}
```

Why: pikepdf explicitly documents parsing page content streams with a `StreamParser`, and PyMuPDF exposes raw stream access via xref methods. That is the Python-native equivalent of “operator evidence,” but not in PDF.js terms. citeturn825997search1turn825997search0

### `raw_block_entries[].text_items`

Rename to:

```json id="0n0m6i"
"text_spans": [
  {
    "text": "Introduction",
    "bbox": [72, 700, 320, 728],
    "font_name": "ABCDEE+Helvetica-Bold",
    "font_size": 24,
    "direction": "ltr",
    "extractor": "pdfminer.six",
    "char_count": 12
  }
]
```

Why: pdfminer.six officially documents character-level extraction with `fontname` and `size`; this is the right conceptual model for Python evidence. citeturn825997search3turn825997search7

### `raw_block_entries[].style_hints`

Keep it, but expand it.

Add:

- `font_flags`
- `color`
- `render_mode`
- `writing_mode`

Those fields are much more natural for Python extraction than the current minimal hint set when you are trying to normalize headings, captions, or emphasized text.

### `raw_block_entries[].structure_hints`

Keep it, but add:

- `object_ref`
- `struct_parent_ref`
- `extractor`
- `tag_path`
- `struct_source`

Suggested shape:

```json id="dv7734"
"structure_hints": {
  "tag_name": "H1",
  "parent_tag_name": "Document",
  "mcid": 0,
  "language": "en-US",
  "object_ref": "12 0 R",
  "struct_parent_ref": "9 0 R",
  "extractor": "pikepdf",
  "tag_path": ["Document", "Sect", "H1"],
  "struct_source": "struct_tree"
}
```

That lets the manifest carry actual structure evidence rather than only the shallow PDF.js-style hint layer.

## Which Python library should populate which part

### PyMuPDF

Best for:

- page geometry
- page labels
- page links
- images/fonts on page
- xref-backed object/stream lookups
- practical page text extraction
- annotations and widgets citeturn825997search0turn825997search4

### pikepdf

Best for:

- raw PDF objects
- stream dictionaries
- content-stream parsing
- name trees
- low-level structure/object provenance citeturn825997search1turn825997search5

### pypdf

Best for:

- metadata
- outline/bookmarks
- named destinations
- page labels
- page layout / page mode
- general document-level dictionary access citeturn825997search2turn825997search9turn825997search11

### pdfminer.six

Best for:

- text spans
- character-level font evidence
- layout grouping
- heading/list/table heuristics based on typography and layout citeturn825997search3turn825997search7

## My concrete recommendation

Do **not** rewrite the whole manifest.

Do this instead:

### 1. Keep the manifest spine

Your current top-level design is already correct. fileciteturn1file0

### 2. Replace the PDF.js-shaped evidence fields

Specifically:

- `text_items` → `text_spans`
- `operator_evidence` → `content_stream_evidence`
- `viewport` → `page_geometry`
- `operator_list_present` → `content_stream_parsed`

### 3. Add extractor namespaces

So the manifest can carry Python evidence without pretending there is one canonical extractor vocabulary.

### 4. Make normalization extractor-neutral

Your `normalized_block_entries` and `projected_target` sections are already the right place for that. fileciteturn1file0turn1file1

## The shortest version

The Python version should be:

- **same manifest spine**
- **generic evidence names**
- **per-extractor raw evidence**
- **one normalized layer above them**

That gets you out of the PDF.js trap without throwing away the good architecture.

I can turn this into an actual **v0.2 schema patch list** next: field-by-field rename, add, remove, and migrate.


#### You:
It’s still v0.1

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes — keep it **v0.1**.

That was my mistake.

Both uploaded files are explicitly **v0.1**:

- the field dictionary says **`pdf_to_docx_accessibility_manifest` v0.1** fileciteturn1file0
- the JSON Schema fixes `manifest_version` to **`"0.1"`** and titles the schema **`pdf_to_docx_accessibility_manifest v0.1`** fileciteturn1file1

## Correct framing

What I should have said was:

- **keep the manifest at v0.1**
- make a **v0.1 patch pass**
- revise fields inside the current draft
- do **not** bump the version just because we are making it Python-native

## So the next step is

A **v0.1 schema patch list**, not a v0.2 rewrite.

That means:

- field rename recommendations inside v0.1
- field additions inside v0.1
- field removals inside v0.1
- migration notes from the current PDF.js-shaped evidence fields to Python-neutral evidence fields

## The clean wording

Instead of “Python version” as a new version number, the right phrase is:

**Python-native v0.1 patch**
or
**extractor-neutral v0.1 patch**

If you want, I’ll do the **v0.1 patch list** now in this format:

- keep
- rename
- add
- remove
- notes on back-compat


#### You:
Which package will you do first?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
**PyMuPDF first.**

Why:

- it gives the broadest **single-package coverage** for the manifest fastest
- it is strongest for the parts you need earliest:
  - `page_entries`
  - page geometry
  - text presence / image-only suspicion
  - links / annotations
  - images / fonts on page
  - practical raw block extraction
- it can also reach down far enough to support traceability:
  - xref access
  - raw object access
  - raw stream access

So if the goal is to get a **working Python-native v0.1 manifest** off the ground quickly, PyMuPDF is the best first package.

## Order I would do them

1. **PyMuPDF**
   - first pass for page evidence and raw blocks

2. **pypdf**
   - metadata
   - outline / bookmarks
   - named destinations
   - page labels
   - page mode / layout
   - some security/interactivity

3. **pikepdf**
   - deep object/stream/content-stream evidence
   - lower-level provenance
   - structure-adjacent and plumbing-heavy fields

4. **pdfminer.six**
   - refinement pass for text spans, font evidence, and normalization heuristics

So the first actual adapter I’d build is:

## `extract_with_pymupdf(...)`

and I’d use that to populate the first real Python-native draft of:

- `source_package`
- `document_summary`
- `document_metadata` (partial)
- `document_accessibility` (partial)
- `document_navigation` (partial)
- `page_entries`
- `raw_block_entries`

Then I’d layer the others in.

If you want, I’ll outline exactly which **v0.1 fields PyMuPDF can populate first-pass** versus which ones have to wait for `pypdf` or `pikepdf`.


#### You:
Yes

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m mapping the v0.1 schema field-by-field now against what PyMuPDF can fill on the first pass, and what should be deferred to pypdf or pikepdf so you don’t build the wrong adapter first.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes.

## First-pass field map for **PyMuPDF first**

This is the field-by-field split I would actually use for **v0.1**.

### Rule of thumb

- **PyMuPDF first** for:
  - page facts
  - page geometry
  - text-layer presence
  - image-only suspicion
  - links / annotations
  - practical raw blocks
  - xref/object/stream traceability

- **pypdf next** for:
  - metadata dictionaries
  - outline / bookmarks
  - named destinations
  - page labels
  - page layout / page mode
  - permissions

- **pikepdf after that** for:
  - content-stream evidence
  - raw PDF objects
  - object refs
  - stream refs
  - lower-level provenance and structure-adjacent evidence

- **pdfminer.six later** for:
  - richer text spans
  - font/size evidence
  - layout-based normalization heuristics

That split matches the actual documented strengths:

- PyMuPDF exposes document/page APIs plus low-level xref/object/stream access. citeturn844809search0turn417033search3
- pypdf exposes outline, page labels, page layout, page mode, named destinations, and user access permissions. citeturn417033search0turn417033search5turn844809search5turn417033search14
- pikepdf is explicitly a low-level PDF library with object lists, stream creation, content-stream filtering/parsing, pages/resources, outlines, name trees, metadata, and security topics. citeturn844809search2turn844809search6turn844809search8turn844809search12turn844809search11

---

## What **PyMuPDF can populate first-pass**

### `source_package`

**PyMuPDF first-pass:**

- `format_family`
- `input_file_name`
- `input_file_path`
- `page_count`
- `byte_length`

**PyMuPDF can also help generate:**

- `document_fingerprints`
  - but I would treat the exact fingerprint algorithm as **your code**, not a library feature

Why:

- PyMuPDF is strong at opening the file and exposing document/page counts and low-level document access. citeturn844809search0turn417033search1

---

### `run_config`

**Not extractor-owned.**
This is your pipeline config, not a PDF-library extraction problem. fileciteturn1file0turn1file1

So:

- `include_preview_images`
- `preview_image_dir`
- `page_separator_mode`
- `include_warning_appendix`
- `include_page_traceback`
- `prefer_outline_for_headings`

are **your code**, not PyMuPDF or any other extractor.

---

### `document_summary`

**PyMuPDF first-pass can populate directly or mostly directly:**

- `total_pages`
- `annotation_count`
- `form_field_count`
  - only if you care to count widgets now
- `figure_candidate_count`
  - first-pass heuristic only
- `raw_block_count`
  - from PyMuPDF block extraction
- `pages_with_warnings`
  - after your warning rules run
- `normalized_block_count`
  - after normalization, not extraction

So for this section:

- **PyMuPDF populates the raw evidence counts**
- **your code computes the interpretation-dependent counts**

PyMuPDF docs and change notes support page-level annotation/widget distinction and page/document access. citeturn417033search6turn844809search0

---

### `document_metadata`

**PyMuPDF first-pass:**

- `title`
- `author`
- `subject`
- `keywords`
- `language`
  - if present in accessible metadata or structure hints you extract
- `xmp_present`
  - yes/no detection
- `info`
  - **partial**, but not my preferred source

**Better deferred to pypdf:**

- `info` as canonical Info-dictionary extraction

Why:

- PyMuPDF can read standard metadata and raw XML metadata streams, but its docs explicitly say it cannot interpret or change XML metadata directly; it can only access the stream object. That makes it good for “XMP present?” and raw access, but not the cleanest canonical metadata layer. citeturn417033search3turn844809search0

So:

- **PyMuPDF first-pass** for quick metadata presence and convenience
- **pypdf second-pass** for canonical document metadata fields

---

### `document_accessibility`

**PyMuPDF first-pass:**

- `image_only_pages_present`
- `ocr_required`
- `ocr_detected`
  - heuristic only
- `reading_order_source`
  - initial guess only, probably `layout_inference`, `mixed`, or `unknown`

**Possible but weak with PyMuPDF alone:**

- `tagged_pdf_detected`
- `struct_tree_detected`
- `mark_info`

**Better deferred to pikepdf or pypdf:**

- `mark_info`
- `tagged_pdf_detected`
- `struct_tree_detected`

Why:

- PyMuPDF is very good at seeing whether pages have extractable text, page content, and raw PDF objects.
- But if you want a clean answer for `MarkInfo`, tag-tree existence, and structure-tree existence, that is closer to PDF-object inspection than page extraction. That is pikepdf territory. citeturn417033search3turn844809search2turn844809search6

So the practical rule is:

- **PyMuPDF first-pass** for:
  - “does this page look image-only?”
  - “is there a text layer?”
  - “does OCR seem to have happened?”
- **pikepdf second-pass** for:
  - “is this a tagged PDF?”
  - “is there a structure tree?”
  - “what does MarkInfo say?”

---

### `document_navigation`

**PyMuPDF first-pass:**

- `outline_present`
  - yes, if you use TOC extraction
- `outline_entries`
  - yes, first-pass
- `named_destinations_present`
  - maybe, but not my first choice
- `named_destinations`
  - maybe, but not my first choice

**Better deferred to pypdf:**

- `outline_entries` as canonical normalized bookmark tree
- `page_labels`
- `named_destinations_present`
- `named_destinations`
- `viewer_preferences`
- `page_layout`
- `page_mode`

Why:

- pypdf explicitly documents outline, page labels, named destinations, page layout, and page mode. That makes it the stronger canonical source for this section. citeturn417033search0turn417033search5turn844809search5

So:

- **PyMuPDF first-pass** can give you a quick TOC/outline presence signal
- **pypdf should own this section canonically**

---

### `document_security`

**Better deferred to pypdf.**

Canonical fields:

- `permissions`

Why:

- pypdf explicitly exposes user access permissions. pikepdf also has security APIs, but for your v0.1 manifest I would make pypdf the canonical extractor for this section and use pikepdf only if you need a second opinion or lower-level details. citeturn417033search14turn844809search11

PyMuPDF is not the library I would use first here.

---

### `document_interactivity`

**PyMuPDF first-pass can populate partially:**

- `forms_present`
- `form_fields`
  - if you later care to inspect widgets
- `javascript_present`
  - maybe via low-level object inspection, but not first-pass
- `xfa_present`
  - not my preferred first-pass source

**Better deferred to pypdf and/or pikepdf:**

- `javascript_present`
- `javascript_actions`
- `xfa_present`
- `is_pure_xfa`
- `all_xfa_html`
- `calculation_order_ids`

Why:

- PyMuPDF does distinguish annotations and widgets/forms at page level. citeturn417033search6
- But XFA and JavaScript are more document-dictionary/object-model territory than page-content territory.
- That makes them better fits for **pypdf** or **pikepdf** than for your first PyMuPDF adapter. citeturn844809search2turn844809search12

Given your current creation-focused discussion, you could also leave most of this section null/false in the first pass if the input class excludes interactive PDFs.

---

### `document_warning_entries`

**Not extractor-owned.**
These are your rule-engine outputs.

PyMuPDF contributes evidence that drives them, especially for:

- image-only suspicion
- text-layer detection
- annotation presence
- figure candidates
- reading-order uncertainty

But the warnings themselves are your code. fileciteturn1file0turn1file1

---

### `page_entries`

This is where **PyMuPDF first** makes the most sense.

#### `page_number`

- **PyMuPDF first-pass: yes**

#### `observed_source`

**PyMuPDF first-pass:**

- `page_ref`
  - if you record xref or your own page reference
- `page_rotation`
- `user_unit`
- `page_bbox`
- `struct_tree_present`
  - weak first-pass, better later from pikepdf
- `text_layer_detected`
- `image_only_page_suspected`
- `ocr_text_detected`
  - heuristic only
- `annotation_count`
- `form_field_count`
- `xfa_present`
  - not preferred here
- `operator_list_present`
  - replace this field later, but PyMuPDF can contribute raw-stream access evidence
- `page_label`
  - better from pypdf

**My recommendation here:**

- Let **PyMuPDF own almost all of `observed_source`**
- except:
  - `page_label` → **pypdf**
  - `struct_tree_present` final answer → **pikepdf**
  - `xfa_present` final answer → **pypdf/pikepdf**

#### `struct_tree`

- **Do not make PyMuPDF own this**
- Wait for **pikepdf**

#### `annotation_entries`

- **PyMuPDF first-pass: yes**
  - subtype
  - contents
  - URL / destination when obtainable
  - manual-review flags from your rules

This is one of the strongest reasons to start with PyMuPDF.

#### `xfa_entries`

- **wait for pypdf/pikepdf**

#### `operator_evidence`

- for the Python-native patch, this should become `content_stream_evidence`
- **wait for pikepdf** if you want it done right
- PyMuPDF can contribute raw stream/xref evidence, but pikepdf is the cleaner owner of this section. citeturn417033search3turn844809search8

#### `warning_entries`

- your code, driven by PyMuPDF evidence

---

### `raw_block_entries`

This is the other section PyMuPDF should own first-pass.

#### `block_id`

- your code

#### `page_number`

- **PyMuPDF first-pass: yes**

#### `source_evidence_type`

- **PyMuPDF first-pass: yes**, but with your classification logic

#### `source_ref`

- **PyMuPDF first-pass: yes**
  - page index
  - block index
  - xref if available

#### `bbox`

- **PyMuPDF first-pass: yes**

#### `text`

- **PyMuPDF first-pass: yes**

#### `text_items`

- For the Python-native patch, this should become `text_spans`
- **PyMuPDF first-pass: yes, but coarse**
- **pdfminer.six later** if you want better font/character-level evidence

#### `style_hints`

- **PyMuPDF first-pass: partial**
  - enough for a first useful pass
- **pdfminer.six later** for stronger typography evidence

#### `structure_hints`

- **PyMuPDF first-pass: limited**
- **pikepdf later** for real structure-adjacent provenance like object refs / MCIDs / tag path where recoverable

#### `role_basis`

- your code

#### `manual_review_required`

- your code

#### `warning_entries`

- your code

So the clean split is:

- **PyMuPDF owns the first useful raw blocks**
- **pdfminer.six improves text/style evidence**
- **pikepdf improves structure/object provenance**

---

### `normalized_block_entries`

This is **not** an extractor section.

PyMuPDF gives the raw evidence that feeds it, but the section itself is owned by your normalizer:

- `block_id`
- `page_span`
- `observed_source_refs`
- `normalized_workflow`
- `warning_entries`
- `projected_target` fileciteturn1file0turn1file1

The same goes for:

- `interpreted_role`
- `heading_level`
- `list_kind`
- `role_confidence`
- `semantic_source_quality`
- `reading_order_index`
- `reading_order_basis`
- `manual_review_required`

Those are **your code**, not PyMuPDF.

---

### `projected_target` (top-level and block-level)

Also **not extractor-owned**.

These belong to the DOCX projection layer:

- `target_package_part`
- `document_title_strategy`
- `page_separator_mode`
- `include_warning_appendix`
- `projection_status`
- `target_style`
- `target_heading_text`
- `target_list_kind`
- `target_table_id` fileciteturn1file0turn1file1

---

## The direct answer in one table

| Manifest section                  | PyMuPDF first-pass         | Better owner later                                        |
| --------------------------------- | -------------------------- | --------------------------------------------------------- |
| `source_package`                  | Most fields                | your fingerprint code                                     |
| `run_config`                      | No                         | your code                                                 |
| `document_summary`                | raw counts                 | your code for normalized counts                           |
| `document_metadata`               | partial                    | pypdf                                                     |
| `document_accessibility`          | page/text-layer heuristics | pikepdf                                                   |
| `document_navigation`             | partial outline signal     | pypdf                                                     |
| `document_security`               | no                         | pypdf                                                     |
| `document_interactivity`          | partial forms/annotations  | pypdf / pikepdf                                           |
| `document_warning_entries`        | evidence only              | your code                                                 |
| `page_entries.observed_source`    | most of it                 | pypdf for labels, pikepdf for structure/XFA final answers |
| `page_entries.struct_tree`        | no                         | pikepdf                                                   |
| `page_entries.annotation_entries` | yes                        | PyMuPDF stays owner                                       |
| `page_entries.xfa_entries`        | no                         | pypdf / pikepdf                                           |
| `page_entries.operator_evidence`  | weak/temporary             | pikepdf                                                   |
| `raw_block_entries`               | yes, first useful version  | pdfminer.six + pikepdf refinements                        |
| `normalized_block_entries`        | evidence only              | your code                                                 |
| `projected_target`                | no                         | your code                                                 |

---

## My actual build order

### Adapter 1: `extract_with_pymupdf()`

Populate first:

- `source_package`
- `document_summary` partial
- `document_metadata` partial
- `document_accessibility` partial
- `page_entries` except struct tree / XFA / canonical content-stream evidence
- `raw_block_entries`

### Adapter 2: `enrich_with_pypdf()`

Add:

- canonical metadata fields
- outline/bookmarks
- page labels
- named destinations
- page layout / page mode
- permissions

### Adapter 3: `enrich_with_pikepdf()`

Add:

- MarkInfo / tagged / struct tree detection
- content-stream evidence
- object refs / stream refs / lower-level provenance
- deeper interactivity / XFA / structure-adjacent evidence

### Adapter 4: `refine_with_pdfminer()`

Improve:

- `text_spans`
- `style_hints`
- normalization heuristics

That is the order I would actually implement.


#### You:
How would you implement it?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m turning this into an implementation plan, not another package survey: modules, adapters, manifest flow, normalization rules, and what I’d build first so you get a working spine instead of a theoretical stack.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I would implement it as a **typed ETL pipeline around your existing v0.1 manifest**, with the manifest as the canonical intermediate representation and each extractor as an adapter that fills only the fields it is best at. Your uploaded v0.1 files already have the right spine: source package, run config, document-level evidence, page-level evidence, raw blocks, normalized blocks, warnings, and projected DOCX output. fileciteturn1file0 fileciteturn1file1

## 1. Repository shape

```text id="repo-shape"
pdf_to_docx/
  pyproject.toml
  src/pdf_to_docx/
    cli.py
    pipeline.py

    manifest/
      schema_v0_1.json
      models.py
      builders.py
      validate.py

    extractors/
      pymupdf_adapter.py
      pypdf_adapter.py
      pikepdf_adapter.py
      pdfminer_adapter.py

    normalize/
      ir.py
      rules_headings.py
      rules_lists.py
      rules_tables.py
      rules_figures.py
      rules_reading_order.py
      normalizer.py

    review/
      warning_rules.py
      severity.py

    projectors/
      docx_projector.py
      style_map.py
      comments.py

    util/
      fingerprints.py
      ids.py
      geometry.py
      text.py
      logging.py

  tests/
    fixtures/
    test_manifest_validation.py
    test_pymupdf_adapter.py
    test_normalizer.py
    test_docx_projector.py
```

## 2. Core design choice

I would keep **v0.1** and make it **extractor-neutral**, not “PDF.js but in Python.” The manifest should stay the canonical contract, while the evidence fields become generic enough to accept PyMuPDF, pypdf, pikepdf, and pdfminer.six outputs. Your field dictionary already separates “what the PDF gave us,” “what we think it means,” “how confident we are,” and “what DOCX we plan to create,” which is exactly the right boundary. fileciteturn1file0

Concretely, I would keep the top-level sections unchanged and patch only the PDF.js-shaped evidence fields:

- `text_items` → `text_spans`
- `operator_evidence` → `content_stream_evidence`
- `viewport` → `page_geometry`
- `operator_list_present` → `content_stream_parsed` fileciteturn1file0 fileciteturn1file1

## 3. Execution flow

### Stage 1: open file and create empty manifest

- Create `source_package`, `target_package`, and `run_config`.
- Initialize empty arrays for pages, raw blocks, normalized blocks, and warnings. fileciteturn1file1

### Stage 2: PyMuPDF first pass

Use **PyMuPDF** as the first adapter because it gives the best single-package coverage for document/page access, text extraction, annotations, links, images, fonts, and low-level xref/object/stream inspection. Its docs describe it as a high-performance library for extraction, analysis, conversion, and manipulation, and it exposes document/page APIs plus low-level interfaces such as xref/object/stream access. citeturn578528search0turn578528search8turn578528search12

PyMuPDF adapter responsibilities:

- `source_package.page_count`, `byte_length`
- `document_summary.total_pages`
- `page_entries[].observed_source`
- `page_entries[].annotation_entries`
- coarse `raw_block_entries`
- first-pass signals for `text_layer_detected`, `image_only_page_suspected`, `annotation_count`, `form_field_count`

### Stage 3: pypdf enrichment

Use **pypdf** next for the document-level things it is explicitly good at: metadata, outline/bookmarks, page labels, page layout, page mode, and permissions. The `PdfReader` docs expose `outline`, `page_labels`, and `page_layout`, and pypdf is also the cleanest pure-Python place to pull document metadata. citeturn578528search1turn578528search5turn578528search13

pypdf enrichment responsibilities:

- `document_metadata.info`, `title`, `author`, `subject`, `keywords`
- `document_navigation.outline_present`, `outline_entries`, `page_labels`, `page_layout`, `page_mode`
- `document_security.permissions`

### Stage 4: pikepdf enrichment

Use **pikepdf** after that for low-level PDF internals: objects, dictionaries, name trees, streams, and content streams. Its docs explicitly say it allows creation, manipulation, and repair of PDFs, provides a wrapper around qpdf, and documents `Stream` objects and content streams directly. citeturn578528search6turn578528search14turn578528search2

pikepdf enrichment responsibilities:

- `document_accessibility.mark_info`
- `document_accessibility.tagged_pdf_detected`
- `document_accessibility.struct_tree_detected`
- `page_entries[].content_stream_evidence`
- object/stream refs attached to raw blocks and pages
- lower-level provenance fields such as `xref`, `object_ref`, `content_stream_refs`

### Stage 5: pdfminer.six refinement

Use **pdfminer.six** last on extraction, not first. Its docs are explicit that PDFs are only aware of characters and placement, so text interpretation is hard, but it also gives exactly the character/font/size/layout evidence you want for normalization. The docs show `extract_pages()` and character property extraction including font names and sizes. citeturn519735search2turn519735search6turn519735search0turn519735search16

pdfminer refinement responsibilities:

- enrich `raw_block_entries[].text_spans`
- improve `style_hints`
- improve heading/list heuristics
- improve reading-order confidence signals

## 4. Manifest builder pattern

I would not let adapters write directly to dicts all over the codebase. I would use:

- a typed `ManifestBuilder`
- typed helpers for `PageEntry`, `RawBlockEntry`, `WarningEntry`, `NormalizedBlockEntry`
- deterministic ID helpers for pages and blocks

Example:

```python id="builder-shape"
builder = ManifestBuilder.empty(
    input_path=pdf_path,
    output_path=docx_path,
    page_separator_mode="PAGE_BREAK",
)

PyMuPDFAdapter().populate(builder)
PypdfAdapter().enrich(builder)
PikepdfAdapter().enrich(builder)
PdfminerAdapter().refine(builder)

normalize_manifest(builder)
attach_review_flags(builder)
project_to_docx(builder)

manifest = builder.build()
validate_manifest(manifest)
```

## 5. Normalization layer

This is the real heart of the project.

I would create an internal IR separate from the manifest, then write the normalized results back into `normalized_block_entries`. The IR nodes would be things like:

```python id="ir-node"
@dataclass
class IRNode:
    id: str
    role: Literal[
        "heading", "paragraph", "list", "list_item",
        "table", "table_row", "table_cell",
        "figure", "caption", "link", "note", "artifact", "unknown"
    ]
    page_span: tuple[int, int]
    raw_block_ids: list[str]
    text: str | None
    bbox: tuple[float, float, float, float] | None
    heading_level: int | None = None
    list_kind: str | None = None
    role_confidence: str = "unknown"
    semantic_source_quality: str = "unknown"
    reading_order_index: int | None = None
    reading_order_basis: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
```

The normalizer would do:

1. Group raw blocks by page.
2. Sort by declared/tag order when reliable, otherwise by geometric order.
3. Promote obvious headings using:
   - tag evidence first
   - then font-size/style outliers
   - then outline/title alignment
4. Detect list runs.
5. Detect table groups.
6. Keep figures and captions separate.
7. Emit one normalized node per semantic unit. fileciteturn1file0turn1file1

## 6. Review flags

I would make review flags a dedicated rule engine, not ad hoc `if` statements spread everywhere. Your schema already has the right places for warnings and `manual_review_required`. fileciteturn1file0turn1file1

Examples:

- `IMAGE_ONLY_PAGE`
- `OCR_REQUIRED`
- `HEADING_CONFIDENCE_LOW`
- `LIST_DETECTION_AMBIGUOUS`
- `TABLE_HEADER_UNCERTAIN`
- `READING_ORDER_MIXED`
- `FIGURE_DESCRIPTION_REVIEW`
- `LINK_DEST_UNCLEAR`
- `STRUCT_TREE_MISSING`
- `TAGGED_PDF_NOT_DETECTED`

Each warning rule should take the manifest plus normalized nodes and append:

- `warning_code`
- `warning_message`
- `warning_scope`
- `warning_severity`
- `manual_review_required` fileciteturn1file1

## 7. DOCX projection

Use **python-docx** only after normalization is done. It is a library for creating and updating `.docx` files, and its docs cover headings, styles, tables, comments, and core properties. Comments are especially useful here because they can hold reviewer notes without altering the projected document text, and comments can themselves contain paragraphs and tables. citeturn669078search6turn669078search12turn669078search11turn669078search1turn669078search0turn669078search3turn578528search3

Projection rules:

- normalized `heading` → `add_heading()` or paragraph with `Heading 1` / `Heading 2` style
- normalized `paragraph` → normal paragraph
- normalized `list` / `list_item` → paragraph styles or list style map
- normalized `table` → `add_table()`
- normalized `figure` → placeholder paragraph + optional image + comment
- warnings → comments or appendix section
- metadata → core properties

I would explicitly separate:

- `target_style` selection
- content insertion
- comment insertion
- appendix generation

## 8. First milestone

The first milestone should be **small and complete**, not broad.

### Milestone 1

Build a pipeline that:

- opens a PDF
- runs **PyMuPDF only**
- emits a valid **v0.1 manifest**
- validates against the uploaded schema
- includes:
  - `source_package`
  - `document_summary` partial
  - `document_metadata` partial
  - `document_accessibility` partial
  - `page_entries`
  - `raw_block_entries`
  - no normalization yet except placeholder empty arrays where needed fileciteturn1file1 citeturn578528search0turn578528search12

That gives you a working spine immediately.

### Milestone 2

Add **pypdf** enrichment for metadata/navigation/security. citeturn578528search1turn578528search5turn578528search13

### Milestone 3

Add **pikepdf** enrichment for structure/streams/provenance. citeturn578528search6turn578528search14turn578528search2

### Milestone 4

Add **pdfminer.six** refinement plus first real normalization pass. citeturn519735search2turn519735search6turn519735search0

### Milestone 5

Add **python-docx** projection plus comments/appendix. citeturn669078search6turn669078search0turn669078search1turn578528search3

## 9. What I would write first

The first concrete file I would write is:

```python id="first-file"
# src/pdf_to_docx/extractors/pymupdf_adapter.py

class PyMuPDFAdapter:
    def populate(self, builder: ManifestBuilder) -> None:
        ...
```

Then:

```python id="second-file"
# src/pdf_to_docx/manifest/validate.py

def validate_manifest(manifest: dict) -> None:
    ...
```

Then:

```python id="third-file"
# src/pdf_to_docx/cli.py

def main():
    ...
```

That sequence gets you from “plan” to “one command that produces a schema-valid manifest.”

## Bottom line

I would implement it as:

- **one canonical v0.1 manifest**
- **multiple extractor adapters**
- **one normalizer**
- **one warning engine**
- **one DOCX projector**

And I would build it in this order:

1. PyMuPDF adapter
2. schema validation
3. pypdf enrichment
4. pikepdf enrichment
5. pdfminer refinement
6. normalization
7. DOCX projection

That is the version I would actually code first, not just describe.


#### You:
What if I wanted PDF -> PDF?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I’m treating this as a pipeline architecture question now: **PDF in, extract/normalize/review, PDF out**. The big decision is whether the output PDF is a lightly patched rewrite, a deeply repaired version, or a full regeneration from your normalized model.


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes. **PDF → PDF** is a different project from **PDF → DOCX**.

The key question is **which kind** of PDF → PDF you mean, because the implementation changes a lot. citeturn188966search0turn188966search5turn188966search11

## There are three real modes

### 1. Patch the existing PDF

This means you keep the original PDF as the substrate and modify it in place or rewrite it with changes. That is the best fit when you want to preserve most of the original file and adjust metadata, page content, objects, streams, annotations, or structure-adjacent details. **pikepdf** is the strongest open-source Python fit for this layer because it is explicitly for creating, manipulating, parsing, repairing, and reading/writing PDFs, including from scratch, and it documents content-stream parsing directly. **pypdf** also fits here for writer-style operations like cloning, incremental writing, merging, metadata, and other document-level changes. citeturn188966search5turn188966search9turn188966search6turn188966search10turn188966search14

### 2. Rebuild a new PDF from your normalized model

This means the source PDF is only evidence. You extract, interpret, normalize, attach review flags, then generate a **new** PDF from your semantic model. That is the better fit if your goal is “make the output PDF structurally clean and accessibility-aware by construction.” **WeasyPrint** is the strongest open-source Python choice for this because it is an HTML/CSS-to-PDF engine and explicitly supports tagged output and PDF/UA-oriented generation, including `pdf/ua-1`, though its docs also say validity is not guaranteed and must be checked. citeturn188966search11turn188966search3

### 3. Hybrid: rebuild most of it, then patch

This is the mode I would choose for your level of comprehensiveness. Generate the new PDF from the normalized semantic model, then use low-level tools to inspect and patch what the generator did. That gives you a cleaner semantic source while still letting you control PDF internals. In practice that means **WeasyPrint** for generation, **pikepdf** for low-level patching and content-stream/object inspection, and **veraPDF** for machine-verifiable validation. WeasyPrint covers semantic generation; pikepdf covers low-level PDF mechanics; veraPDF is the validator, and its docs are explicit that it performs only machine-verifiable PDF/UA checks. citeturn188966search3turn188966search5turn188966search9turn188966search0

## What I would do for your project

For **your** planning depth, I would implement **PDF → PDF** as:

1. **Input**
2. **Extract**
3. **Interpret / normalize**
4. **Attach review flags**
5. **Project to PDF**
6. **Validate**
7. **Optional low-level patch pass** citeturn188966search0turn188966search5turn188966search3

The normalized model stays the center of gravity. The only thing that changes from your DOCX pipeline is the **projector**: instead of `python-docx`, you build a **PDF projector**. citeturn188966search11turn188966search3

## Which package would own which stage

### Extract

- **PyMuPDF** first for pages, text/image extraction, links, annotations, fonts, and low-level xref/object/stream inspection. Its docs describe it as a high-performance library for extraction, analysis, conversion, and manipulation, and its page/document APIs support adding text/images and inspecting pages deeply. citeturn188966search0turn188966search4turn188966search15turn188966search18
- **pypdf** for metadata and document-level structures like metadata and writer-style page handling. citeturn188966search6turn188966search10turn188966search14
- **pikepdf** for low-level content streams, objects, and stream-level evidence. citeturn188966search5turn188966search9turn188966search19

### Interpret / normalize

This should still be **your code**, not a library feature. None of these libraries gives you your project’s canonical semantic model for free. The libraries give evidence; your pipeline decides what it means. citeturn188966search0turn188966search5

### Project to PDF

This is where the split matters:

- If you want **semantic rebuilding**, use **WeasyPrint**. It is the only one in this group that cleanly fits “semantic document generation” and explicitly supports tagged/PDF/UA-oriented output. citeturn188966search11turn188966search3
- If you want **exact page composition**, use **PyMuPDF**. It lets you create pages and add text, images, simple geometrical objects, annotations, and other page content directly. citeturn188966search4turn188966search15
- If you want **low-level rewrite**, use **pikepdf**. It can create from scratch and manipulate content streams and objects directly, but it is not the best semantics-first authoring engine. citeturn188966search5turn188966search9turn188966search19

### Validate

Use **veraPDF** for machine-verifiable PDF/UA checks. That should remain the validator regardless of whether you output DOCX or PDF. citeturn188966search3turn188966search0

## The direct package answer

If you want **PDF → PDF with semantic rebuilding**, I would use:

- **WeasyPrint** to generate the new PDF
- **pikepdf** to inspect/patch the emitted PDF
- **PyMuPDF** only if you need exact page-level insertions or post-generation page work
- **veraPDF** to validate citeturn188966search3turn188966search5turn188966search15turn188966search0

If you want **PDF → PDF as a rewrite of the original file**, I would use:

- **pikepdf** as the primary engine
- **pypdf** for helper/document-level operations
- **PyMuPDF** when you need page-level drawing/manipulation
- **veraPDF** to validate citeturn188966search5turn188966search6turn188966search15turn188966search0

## My blunt recommendation

For your project, I would **not** do “PDF → PDF” as a pure low-level rewrite unless preserving the original exact page appearance is the top priority.

I would do:

**PDF → extract → normalize → review flags → semantic rebuild to PDF → low-level patch pass → validate**

because that is the version that best matches your “explicit model, exact control, accessibility by construction” direction. citeturn188966search3turn188966search5turn188966search0

If you want, I’ll turn that into a concrete **PDF-projector plan** with:

- one branch for **WeasyPrint-based rebuild**
- one branch for **PyMuPDF-based page authoring**
- and exactly where `pikepdf` fits after generation.


#### You:
Accessibility Report

Filename:
finreport25.pdf
Report created by:
Kristen McConkey
Organization:
[Personal and organization information from the Preferences > Identity dialog.]

Summary

The checker found problems which may prevent the document from being fully accessible.

Needs manual check: 2
Passed manually: 0
Failed manually: 0
Skipped: 1
Passed: 20
Failed: 9
Detailed Report

Document
Rule Name	Status	Description
Accessibility permission flag	Passed	Accessibility permission flag must be set
Image-only PDF	Passed	Document is not image-only PDF
Tagged PDF	Passed	Document is tagged PDF
Logical Reading Order	Needs manual check	Document structure provides a logical reading order
Primary language	Passed	Text language is specified
Title	Failed	Document title is showing in title bar
Bookmarks	Failed	Bookmarks are present in large documents
Color contrast	Needs manual check	Document has appropriate color contrast
Page Content
Rule Name	Status	Description
Tagged content	Failed	All page content is tagged
Tagged annotations	Failed	All annotations are tagged
Tab order	Passed	Tab order is consistent with structure order
Character encoding	Passed	Reliable character encoding is provided
Tagged multimedia	Passed	All multimedia objects are tagged
Screen flicker	Passed	Page will not cause screen flicker
Scripts	Passed	No inaccessible scripts
Timed responses	Passed	Page does not require timed responses
Navigation links	Passed	Navigation links are not repetitive
Forms
Rule Name	Status	Description
Tagged form fields	Passed	All form fields are tagged
Field descriptions	Passed	All form fields have description
Alternate Text
Rule Name	Status	Description
Figures alternate text	Failed	Figures require alternate text
Nested alternate text	Passed	Alternate text that will never be read
Associated with content	Passed	Alternate text must be associated with some content
Hides annotation	Passed	Alternate text should not hide annotation
Other elements alternate text	Failed	Other elements that require alternate text
Tables
Rule Name	Status	Description
Rows	Passed	TR must be a child of Table, THead, TBody, or TFoot
TH and TD	Passed	TH and TD must be children of TR
Headers	Failed	Tables should have headers
Regularity	Failed	Tables must contain the same number of columns in each row and rows in each column
Summary	Skipped	Tables must have a summary
Lists
Rule Name	Status	Description
List items	Passed	LI must be a child of L
Lbl and LBody	Passed	Lbl and LBody must be children of LI
Headings
Rule Name	Status	Description
Appropriate nesting	Failed	Appropriate nesting
Back to Top

#### Plugin (file_search):
Make sure to include fileciteturn2file0 in your response to cite this file, or to surface it as a link.
<PARSED TEXT FOR PAGE: 1 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
ANNUAL FINANCIAL REPORT
AND
SINGLE AUDIT REPORT
FOR THE YEAR ENDED JUNE 30, 2025
<IMAGE FOR PAGE: 1 / 117>
![image](sediment://deb50b747c197b4#file_000000005b7c71f7b4b2a32a07acadeb#p_0.cc80615d77.jpg)
<PARSED TEXT FOR PAGE: 2 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
TABLE OF CONTENTS
Independent Auditor's Report 1 - 3
Independent Auditor’s Report on Internal Control over Financial Reporting and on
Compliance and Other Matters Based on an Audit of Financial Statements Performed in 
Accordance with Government Auditing Standards 4 - 5
MANAGEMENT’S DISCUSSION AND ANALYSIS
Management’s Discussion and Analysis 6a – 6h
BASIC FINANCIAL STATEMENTS
Statement of Net Position 7 - 8
Statement of Revenues, Expenses, and Changes in Net Position 9
Statement of Cash Flows 10
Notes to Financial Statements 11 - 52
REQUIRED SUPPLEMENTARY INFORMATION (UNAUDITED)
State Universities Retirement System of Illinois (SURS) Pension Plan – GASB 68:
Schedule of the College’s Proportionate Share of the Net Pension Liability 53
Schedule of College Contributions 53
Schedule of Changes in the College’s Total OPEB Liability and Related Ratios, 
College Plan – GASB 75 54
College Insurance Program (CIP) – GASB 75
 Schedule of the Employer’s Proportionate Share of the Collective Net OPEB Liability 55
Schedule of State Contributions 55
Notes to Required Supplementary Information 56 - 57
OTHER SUPPLEMENTAL INFORMATION (UNAUDITED)
Schedule of Assessed Valuations, Tax Rates, and Taxes Extended 58
Schedule of Legal Debt Margin 59
Certification of Per Capita Cost 60
<PARSED TEXT FOR PAGE: 3 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT #530
CARTERVILLE, ILLINOIS 
TABLE OF CONTENTS (CONTINUED)
UNIFORM FINANCIAL STATEMENTS (UFS)
All Funds Summary (UFS#1) 61
Reconciliation of the Uniform Financial Statement No. 1 to the 
Statement of Net Position 62
Reconciliation of the Uniform Financial Statement No. 1 to the 
Statement of Revenues, Expenses, and Changes in Net Position 63
Summary of Fixed Assets and Debt (UFS#2) 64
Operating Funds Revenues and Expenditures (UFS#3) 65 - 66
Restricted Purposes Fund Revenues and Expenditures (UFS#4) 67
Current Funds * Expenditures by Activity (UFS#5) 68
STATE COMPLIANCE SECTION
Independent Auditor's Report on Compliance with State Requirements for Adult 
Education and Family Literacy Grants 69 - 70
State Adult Education Restricted Funds
Balance Sheet 71
Statement of Revenues, Expenditures, and Changes in Fund Balance 72
Notes to Grant Program Financial Statements 73 - 74
ENROLLMENT DATA AND OTHER BASIS UPON WHICH CLAIM ARE FILED SECTION
Independent Accountant’s Report on the Schedule of Enrollment Data and Other Bases 
Upon Which Claims are Filed 75
Schedule of Enrollment Data and Other Bases upon Which Claims are Filed 76
Reconciliation of Total Reimbursable Semester Credit Hours 77
Documentation of Residency Verification Steps 78 - 80
<PARSED TEXT FOR PAGE: 4 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT #530
CARTERVILLE, ILLINOIS 
TABLE OF CONTENTS (CONTINUED)
STATE OF ILLINOIS CONSOLIDATED YEAR-END FINANCIAL REPORT
Independent Auditor’s Report on the State of Illinois Consolidated Year-End 
Financial Report 81
Consolidated Year-End Financial Report 82a – 82g
FEDERAL COMPLIANCE SECTION
Independent Auditor’s Report on Compliance for Each Major Federal Program and on 
Internal Control Over Compliance Required by the Uniform Guidance 83 - 85
Schedule of Expenditures of Federal Awards 86
Notes to the Schedule of Expenditures of Federal Awards 87
Schedule of Findings and Questioned Costs:
Section I – Summary of Auditor’s Results 88
Section II – Financial Statement Findings 89
Section III – Federal Award Findings and Questioned Costs 90
Summary Schedule of Prior Audit Findings 91
<PARSED TEXT FOR PAGE: 5 / 117>
INDEPENDENT AUDITOR’S REPORT
To the Board of Trustees
John A. Logan College
Community College District No. 530
Carterville, Illinois 62918
Report on the Audit of the Financial Statements
Opinions
We have audited the accompanying financial statements of the business-type activities and the discretely
presented component unit of John A. Logan College, Community College District No. 530 (the College),
as of and for the year ended June 30, 2025, and the related notes to the financial statements, which 
collectively comprise the College’s basic financial statements, as listed in the table of contents. 
In our opinion, the financial statements referred to above present fairly, in all material respects, the 
respective financial position of the business-type activities and the discretely presented component unit of 
John A. Logan College, Community College District No. 530 as of June 30, 2025, and the respective 
changes in financial position and, where applicable, cash flows thereof for the year then ended in 
accordance with accounting principles generally accepted in the United States of America.
Basis for Opinions
We conducted our audit in accordance with auditing standards generally accepted in the United States of 
America and the standards applicable to financial audits contained in Government Auditing Standards, 
issued by the Comptroller General of the United States. Our responsibilities under those standards are 
further described in the Auditor’s Responsibilities for the Audit of the Financial Statements section of our 
report. We are required to be independent of the College and to meet our other ethical responsibilities, in 
accordance with the relevant ethical requirements relating to our audit. We believe that the audit evidence 
we have obtained is sufficient and appropriate to provide a basis for our audit opinions. The financial 
statements of the discretely presented component unit were not audited in accordance with Government 
Auditing Standards. 
Change in Accounting Principle
As described in Note 16 to the financial statements, the College adopted the Governmental Accounting 
Standards Board (GASB) Statement No. 101, Compensated Absences, for the year ended June 30, 2025. 
The implementation of this guidance resulted in changes to the accrual of compensated absence balances 
and a restatement of beginning net position. Our opinion was not modified with respect to this matter. 
Responsibilities of Management for the Financial Statements
Management is responsible for the preparation and fair presentation of these financial statements in 
accordance with accounting principles generally accepted in the United States of America, and for the
design, implementation, and maintenance of internal control relevant to the preparation and fair 
presentation of financial statements that are free from material misstatement, whether due to fraud or 
error.
1
 3401 Professional Park Drive ▪ Marion, IL 62959 
Phone: (618) 997-3055 Fax: (618) 997-5121 kempercpa.com
~~t41KEMPER 
.i:iiCPA GROUPLLP 
Certified Public Accountants and Consultants 
<IMAGE FOR PAGE: 5 / 117>
![image](sediment://1b4f4531f2ad4a8#file_000000005b7c71f7b4b2a32a07acadeb#p_1.f8a3087354.jpg)
<PARSED TEXT FOR PAGE: 6 / 117>
In preparing the financial statements, management is required to evaluate whether there are conditions or 
events, considered in the aggregate, that raise substantial doubt about the College’s ability to continue as a 
going concern for twelve months beyond the financial statement date, including any currently known 
information that may raise substantial doubt shortly thereafter.
Auditor’s Responsibilities for the Audit of the Financial Statements
Our objectives are to obtain reasonable assurance about whether the financial statements as a whole are 
free from material misstatement, whether due to fraud or error, and to issue an auditor’s report that 
includes our opinions. Reasonable assurance is a high level of assurance but is not absolute assurance and 
therefore is not a guarantee that an audit conducted in accordance with generally accepted auditing 
standards and Government Auditing Standards will always detect a material misstatement when it exists. 
The risk of not detecting a material misstatement resulting from fraud is higher than for one resulting 
from error, as fraud may involve collusion, forgery, intentional omissions, misrepresentations, or the 
override of internal control. Misstatements are considered material if there is a substantial likelihood that, 
individually or in the aggregate, they would influence the judgment made by a reasonable user based on 
the financial statements.
In performing an audit in accordance with generally accepted auditing standards and Government 
Auditing Standards, we:
• Exercise professional judgment and maintain professional skepticism throughout the audit.
• Identify and assess the risks of material misstatement of the financial statements, whether due to 
fraud or error, and design and perform audit procedures responsive to those risks. Such 
procedures include examining, on a test basis, evidence regarding the amounts and disclosures in 
the financial statements.
• Obtain an understanding of internal control relevant to the audit in order to design audit 
procedures that are appropriate in the circumstances, but not for the purpose of expressing an 
opinion on the effectiveness of the College’s internal control. Accordingly, no such opinion is 
expressed.
• Evaluate the appropriateness of accounting policies used and the reasonableness of significant 
accounting estimates made by management, as well as evaluate the overall presentation of the 
financial statements.
• Conclude whether, in our judgment, there are conditions or events, considered in the aggregate, 
that raise substantial doubt about the College’s ability to continue as a going concern for a 
reasonable period of time.
We are required to communicate with those charged with governance regarding, among other matters, the 
planned scope and timing of the audit, significant audit findings, and certain internal control-related 
matters that we identified during the audit.
Required Supplementary Information
Accounting principles generally accepted in the United States of America require that the management’s 
discussion and analysis, the pension schedules, and other postemployment benefit (OPEB) schedules, as 
listed in the table of contents, be presented to supplement the basic financial statements. Such information 
is the responsibility of management and, although not a part of the basic financial statements, is required 
by the Governmental Accounting Standards Board who considers it to be an essential part of financial
reporting for placing the basic financial statements in an appropriate operational, economic, or historical 
context. We have applied certain limited procedures to the required supplementary information in 
accordance with auditing standards generally accepted in the United States of America, which consisted 
of inquiries of management about the methods of preparing the information and comparing the
information for consistency with management’s responses to our inquiries, the basic financial statements,
2
<PARSED TEXT FOR PAGE: 7 / 117>
and other knowledge we obtained during our audit of the basic financial statements. We do not express an 
opinion or provide any assurance on the information because the limited procedures do not provide us 
with sufficient evidence to express an opinion or provide any assurance.
Supplementary Information
Our audit was conducted for the purpose of forming opinions on the financial statements that collectively 
comprise John A. Logan College, Community College District No. 530’s basic financial statements. The 
Uniform Financial Statements, as required by the Illinois Community College Board, and the Schedule of 
Expenditures of Federal Awards, as required by Title 2 U.S. Code of Federal Regulations Part 200, 
Uniform Administrative Requirements, Cost Principles, and Audit Requirements for Federal Awards, are 
presented for purposes of additional analysis and are not a required part of the basic financial statements. 
Such information is the responsibility of management and was derived from and relates directly to the 
underlying accounting and other records used to prepare the basic financial statements. The information
has been subjected to the auditing procedures applied in the audit of the basic financial statements and 
certain additional procedures, including comparing and reconciling such information directly to the 
underlying accounting and other records used to prepare the basic financial statements or to the basic 
financial statements themselves, and other additional procedures in accordance with auditing standards 
generally accepted in the United States of America. In our opinion, the Uniform Financial Statements and
the Schedule of Expenditures of Federal Awards are fairly stated, in all material respects, in relation to the 
basic financial statements taken as a whole.
Other Information
Management is responsible for the Other Supplemental Information included in the annual report. The 
Other Supplemental Information, as listed in the table of contents, does not include the basic financial 
statements and our auditor’s report thereon. Our opinions on the basic financial statements do not cover 
the Other Supplemental Information, and we do not express an opinion or any form of assurance thereon.
In connection with our audit of the basic financial statements, our responsibility is to read the Other 
Supplemental Information and consider whether a material inconsistency exists between the Other 
Supplemental Information and the basic financial statements, or the Other Supplemental Information 
otherwise appears to be materially misstated. If, based on the work performed, we conclude that an 
uncorrected material misstatement of the Other Supplemental Information exists, we are required to 
describe it in our report.
Other Reporting Required by Government Auditing Standards
In accordance with Government Auditing Standards, we have also issued our report dated February 19, 
2026, on our consideration of the College’s internal control over financial reporting and on our tests of its 
compliance with certain provisions of laws, regulations, contracts, and grant agreements, and other 
matters. The purpose of that report is solely to describe the scope of our testing of internal control over 
financial reporting and compliance and the results of that testing, and not to provide an opinion on the 
effectiveness of the College’s internal control over financial reporting or on compliance. That report is an 
integral part of an audit performed in accordance with Government Auditing Standards in considering the 
College’s internal control over financial reporting and compliance.
KEMPER CPA GROUP LLP
Certified Public Accountants and Consultants
Marion, Illinois
February 19, 2026
3
<PARSED TEXT FOR PAGE: 8 / 117>
INDEPENDENT AUDITOR’S REPORT ON INTERNAL CONTROL OVER 
FINANCIAL REPORTING AND ON COMPLIANCE AND OTHER MATTERS 
BASED ON AN AUDIT OF FINANCIAL STATEMENTS PERFORMED IN 
ACCORDANCE WITH GOVERNMENT AUDITING STANDARDS
To the Board of Trustees
John A. Logan College 
Community College District No. 530
Carterville, Illinois 62918
We have audited, in accordance with auditing standards generally accepted in the United States of 
America and the standards applicable to financial audits contained in Government Auditing Standards
issued by the Comptroller General of the United States, the financial statements of the business-type 
activities and the discretely presented component unit of John A. Logan College, Community College
District No. 530 (the College) as of and for the year ended June 30, 2025, and the related notes to the 
financial statements, which collectively comprise the College’s basic financial statements, and have 
issued our report thereon dated February 19, 2026. The financial statements of the John A. Logan College 
Foundation (the Foundation), a discretely presented component unit, were not audited in accordance with 
Government Auditing Standards and, accordingly, this report does not include reporting on internal 
control over financial reporting or instances of reportable noncompliance associated with the Foundation.
Report on Internal Control Over Financial Reporting
In planning and performing our audit of the financial statements, we considered the College’s internal 
control over financial reporting (internal control) as a basis for designing audit procedures that are 
appropriate in the circumstances for the purpose of expressing our opinions on the financial statements, 
but not for the purpose of expressing an opinion on the effectiveness of the College’s internal control. 
Accordingly, we do not express an opinion on the effectiveness of the College’s internal control.
A deficiency in internal control exists when the design or operation of a control does not allow 
management or employees, in the normal course of performing their assigned functions, to prevent, or 
detect and correct, misstatements on a timely basis. A material weakness is a deficiency, or a 
combination of deficiencies, in internal control, such that there is a reasonable possibility that a material 
misstatement of the entity’s financial statements will not be prevented or detected and corrected on a 
timely basis. A significant deficiency is a deficiency, or a combination of deficiencies, in internal control 
that is less severe than a material weakness, yet important enough to merit attention by those charged with 
governance.
Our consideration of internal control was for the limited purpose described in the first paragraph of this 
section and was not designed to identify all deficiencies in internal control that might be material 
weaknesses or significant deficiencies. Given these limitations, during our audit we did not identify any 
deficiencies in internal control that we consider to be material weaknesses. However, material weaknesses 
or significant deficiencies may exist that were not identified. 
4
 3401 Professional Park Drive ▪ Marion, IL 62959 
Phone: (618) 997-3055 Fax: (618) 997-5121 kempercpa.com
~~t41KEMPER 
.i:iiCPA GROUPLLP 
Certified Public Accountants and Consultants 
<IMAGE FOR PAGE: 8 / 117>
![image](sediment://0c2706aab318b38#file_000000005b7c71f7b4b2a32a07acadeb#p_2.4247b4cf9b.jpg)
<PARSED TEXT FOR PAGE: 9 / 117>
Report on Compliance and Other Matters
As part of obtaining reasonable assurance about whether the College’s financial statements are free from
material misstatement, we performed tests of its compliance with certain provisions of laws, regulations, 
contracts, and grant agreements, noncompliance with which could have a direct and material effect on the 
financial statements. However, providing an opinion on compliance with those provisions was not an 
objective of our audit, and accordingly, we do not express such an opinion. The results of our tests 
disclosed no instances of noncompliance or other matters that are required to be reported under 
Government Auditing Standards.
Purpose of this Report
The purpose of this report is solely to describe the scope of our testing of internal control and compliance 
and the results of that testing, and not to provide an opinion on the effectiveness of the entity’s internal 
control or on compliance. This report is an integral part of an audit performed in accordance with 
Government Auditing Standards in considering the entity’s internal control and compliance. 
Accordingly, this communication is not suitable for any other purpose. 
KEMPER CPA GROUP LLP
Certified Public Accountants and Consultants
Marion, Illinois
February 19, 2026
5
<PARSED TEXT FOR PAGE: 10 / 117>
MANAGEMENT’S DISCUSSION AND ANALYSIS
<PARSED TEXT FOR PAGE: 11 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT #530
CARTERVILLE, ILLINOIS
MANAGEMENT’S DISCUSSION AND ANALYSIS
JUNE 30, 2025
(Unaudited)
This section of John A. Logan College’s Annual Comprehensive Financial Report presents management’s 
discussion and analysis of the College’s financial activity during the fiscal years ended June 30, 2025 and 
2024. Management’s discussion and analysis is designed to focus on current activities, resulting change, and 
currently known facts. Please read it in conjunction with the College’s audited basic financial statements and 
the notes to financial statements. Responsibility for the completeness and fairness of this information rests with 
management of the College.
Using the Annual Comprehensive Financial Report
The basic financial statements focus on the College as a whole and are designed to emulate corporate 
presentation models whereby all College activities are consolidated into one total. The focus of the Statement 
of Net Position is designed to reflect the College’s financial position at a certain date. This statement combines 
and consolidates current financial resources (short-term spendable resources) with capital assets. Net position 
is one indicator of the current financial condition of the College, while the change in net position is another 
indicator of whether the overall financial condition has improved or deteriorated during the year. 
The Statement of Revenues, Expenses, and Changes in Net Position presents the College’s financial results for 
the fiscal year. This statement includes the College’s revenues and expenses, both operating and non-operating.
Operating revenues and expenses are those for which the College directly exchanges goods and services. The 
primary operating revenues for the College are tuition and fees (net of scholarship allowances) and auxiliary 
services (net). Non-operating revenues and expenses are those that exclude specific, direct exchanges of goods 
and services. The major components of the College’s non-operating revenues include local property taxes and 
government grants and contracts. The reporting model classifies these revenues as non-operating because no 
direct exchange of goods and services are received from local taxpayers or the government, respectively. This 
approach is intended to summarize and simplify the user’s analysis of costs of various College services to 
students and the public. 
Financial Highlights
The College implemented GASB Statement No. 101 – Compensated Absences during the year ended June 30, 
2025. This implementation resulted in recalculation of the College’s current- and non-current liabilities for 
compensated absences. This change resulted in a restatement of the June 30, 2024 ending net position as 
described in Note 16 to the financial statements. 
The College’s net position increased $8.6 million from $56.8 million at June 30, 2024, as restated, to $65.4
million at June 30, 2025. The total increase in the College’s net position was split between a $6.6 million 
increase in net investment in capital assets, a $2.2 million increase in unrestricted net position, and a $0.2 
million decrease in restricted net position. Net position represents the balance in the College’s assets and 
deferred outflows of resources after liabilities and deferred inflows of resources are deducted. 
6a
<PARSED TEXT FOR PAGE: 12 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT #530
CARTERVILLE, ILLINOIS
MANAGEMENT’S DISCUSSION AND ANALYSIS (CONTINUED)
JUNE 30, 2025
Financial Highlights (Concluded)
Operating revenues decreased $0.7 million from fiscal year 2024 to 2025. Non-operating revenues and 
expenses, net, increased $1.8 million. State on-behalf revenues, which increased by $0.4 million, are included 
in non-operating revenues. These on-behalf revenues represent the College’s proportionate share of pension 
and other post-employment benefit (OPEB) contributions made on-behalf of the College by the State of Illinois 
to the State University Retirement System (SURS) and State of Illinois College Insurance Program (CIP). 
Total revenues and capital contributions, excluding State on-behalf contributions, increased $2.6 million from 
$48.5 million to $51.1 million in fiscal years 2024 and 2025, respectively. This increase is primarily due to an 
increase in capital contributions of $2.1 million, an increase in property taxes of $0.6 million, an increase in 
federal grants and contacts of $0.6 million, and an increase in nongovernmental gifts, grants, and bequests of 
$0.5 million. These increases were partially offset by a decrease in student tuition and fees, net of scholarships 
and allowances, of $0.9 million, and a decrease in corporate personal property replacement taxes of $0.4 
million.
Total College expenses increased $2.5 million from $46.9 million to $49.4 million in fiscal years 2024 and 
2025, respectively. More discussion of the change in operating expenses is available on the following pages.
Financial Analysis of the College as a Whole
Net Position as of June 30
(in millions)
2024 Increase Percent
2025 (as restated) (Decrease) Change
Current assets $ 38.3 $ 38.2 $ 0.1 0.3 %
Non-Current
Restricted assets 24.2 26.6 (2.4) (9.0)
Tangible and intangible capital assets, net 66.0 60.0 6.0 10.0
Total assets 128.5 124.8 3.7 3.0
Deferred Outflows of Resources 1.1 1.8 (0.7) (38.9)
Current liabilities 11.3 9.6 1.7 17.7
Non-current liabilities 26.6 32.3 (5.7) (17.6)
Total liabilities 37.9 41.9 (4.0) (9.5)
Deferred Inflows of Resources 26.3 27.9 (1.6) (5.7)
Net Position
Net investment in capital assets 53.4 46.8 6.6 14.1
Restricted 23.1 23.3 (0.2) (0.9)
Unrestricted (11.1) (13.3) 2.2 (16.5)
Total net position $ 65.4 $ 56.8 $ 8.6 15.1
6b
<PARSED TEXT FOR PAGE: 13 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT #530
CARTERVILLE, ILLINOIS
MANAGEMENT’S DISCUSSION AND ANALYSIS (CONTINUED)
JUNE 30, 2025
Financial Analysis of the College as a Whole (Continued)
The College’s statement of net position, as summarized in the above schedule, is presented on the accrual basis 
of accounting whereby assets are capitalized and depreciated or amortized and deferred outflows and inflows 
of resources are recognized.
Current assets increased $0.1 million during the year ended June 30, 2025. Within current assets, cash and cash 
equivalents increased $0.3 million, prepaid expenses increased $0.1 million, and receivables decreased $0.4
million. The decrease in total receivables was driven by a decrease of $0.8 million in net tuition and fees 
receivable, offset partially by an increase of $0.5 million in governmental claims. Current assets account for 
approximately 30% of total assets.
Non-current assets increased $3.6 million due to a $6.0 million increase in tangible and intangible capital 
assets, net of depreciation and amortization, partially offset by a $2.4 million decrease in restricted assets. The 
use of restricted cash for the construction of the Harrison Bruce Player Development Center, the Career and 
Technical Center, the C and E Wing renovations and HVAC replacement, and the elevator project is reflected 
in a reduction in restricted cash and cash equivalents and an increase in construction in progress within capital 
assets. Restricted assets account for 19% of total assets and tangible and intangible capital assets, net, account 
for 51% of total assets.
Current liabilities increased $1.7 million, which was primarily driven by increases of $0.9 million in 
compensated absences due in one year (compared to the restated balance at June 30, 2024 of $0.1 million), 
$0.8 million in accounts payable, $0.4 million in subscription liabilities due in one year, $0.1 million in the 
current portion of bonds payable, offset partially by decreases of $0.3 million in accrued expenses and $0.3 
million in refundable advances. Current liabilities represent 30% of total liabilities. 
Non-current liabilities decreased $5.7 million to $26.6 million on June 30, 2025, compared to $32.3 million 
on June 30, 2024, as restated. $10.7 million of the total non-current liabilities are those associated with the 
long-term portion of bonds payable. This debt is the result of past-year bond financing that has been assumed 
to take advantage of favorable market conditions and to allow the College to finance needed expansion of 
facilities and to maximize investment potential.
Deferred outflows of resources decreased $0.7 million due to decreases in OPEB plan related amounts. 
Deferred inflows of resources decreased $1.6 million due to a $1.8 million decrease in OPEB plan related 
amounts, offset partially by a $0.3 million increase in deferred property tax revenue.
6c
<PARSED TEXT FOR PAGE: 14 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT #530
CARTERVILLE, ILLINOIS
MANAGEMENT’S DISCUSSION AND ANALYSIS (CONTINUED)
JUNE 30, 2025
Financial Analysis of the College as a Whole (Continued)
Operating Results for the Years Ended
(in millions)
Increase Percent
Operating Income (Loss) 2025 2024 (Decrease) Change
Operating revenues
Student tuition and fees, net $ 3.9 $ 4.8 $ (0.9) (18.8)%
Auxiliary enterprises revenue 1.2 1.0 0.2 20.0
Other operating revenue 0.5 0.5 - -
Total operating revenue 5.6 6.3 (0.7) (11.1)
Less operating expenses 48.8 46.3 2.5 5.4
Operating income (loss) (43.2) (40.0) (3.2) (8.0)
Non-Operating Revenues (Expenses)
Property taxes 16.9 16.3 0.6 3.7
Corporate personal property replacement taxes 0.9 1.3 (0.4) (30.8)
State grants and contracts 12.4 12.2 0.2 1.6
Federal grants and contracts 9.9 9.3 0.6 6.5
Nongovernmental gifts, grants and bequests 1.3 0.8 0.5 62.5
On-behalf revenues – SURS & CIP 6.9 6.5 0.4 6.2
Investment income 1.6 1.9 (0.3) (15.8)
Bond premium amortization 
 (interest expense), net (0.5) (0.7) 0.2 28.6
Total non-operating revenues (expenses) 49.4 47.6 1.8 3.8
Capital Contributions 2.5 0.4 2.1 525.0
Change in Net Position $ 8.7 $ 8.0 $ 0.7 8.7
When reviewing the operating results, it should be noted the tuition and fees amount has been adjusted for 
scholarship discounts and allowances. Scholarship discounts and allowances represent the portion of tuition 
and fees that the College does not collect because it has granted financial aid that has been applied directly to 
those charges. Scholarship discounts and allowances for the fiscal years 2025 and 2024 were $6.6 million and 
$5.7 million, respectively. The fiscal year 2025 scholarship discounts and allowances includes $3.4 million 
institutional scholarships and waivers, $3.0 million federal Pell grants, and $0.2 million other federal and state 
grants. If tuition and fees were presented on a gross basis, a greater dependence on tuition and fees would be 
noted.
6d
<PARSED TEXT FOR PAGE: 15 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT #530
CARTERVILLE, ILLINOIS
MANAGEMENT’S DISCUSSION AND ANALYSIS (CONTINUED)
JUNE 30, 2025
Financial Analysis of the College as a Whole (Continued)
The following are graphic illustrations of total revenue, including capital contributions, and operating 
expenses, including payments made by the State of Illinois on behalf of the College, for the year ended 
June 30, 2025:
6e
Property 
taxes/CPPRT
31%
Other
5%
State grants & 
contracts
25%
State on-behalf
12%
Federal grants & 
contracts
17%
Investment
3% Net tuition & fees
7%
Revenue by Source
Public 
service/continuing 
education
7%
Academic support
7%
Student services
8%
Instruction
24%
Institutional support
20%
Operation and 
maintenance
of plant
12%
Auxiliary enterprise
4%
Scholarships, student 
grants, and waivers
10%
Depreciation and 
amortizaiton
8%
Operating Expenses
<IMAGE FOR PAGE: 15 / 117>
![image](sediment://9347c57ef4ae3db#file_000000005b7c71f7b4b2a32a07acadeb#p_3.bed99994a3.jpg)
<PARSED TEXT FOR PAGE: 16 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT #530
CARTERVILLE, ILLINOIS
MANAGEMENT’S DISCUSSION AND ANALYSIS (CONTINUED)
JUNE 30, 2025
Financial Analysis of the College as a Whole (Continued)
Operating Expenses for the Years Ended
(in millions)
Increase Percent
2025 2024 (Decrease) Change
Instruction $ 11.9 $ 10.8 $ 1.1 10.2 %
Academic support 3.4 3.1 0.3 9.7
Student services 4.0 4.1 (0.1) (2.4)
Public service/continuing education 3.5 3.6 (0.1) (2.8)
Operation and maintenance of plant 5.8 5.6 0.2 3.6
Institutional support 9.5 9.2 0.3 3.3
Auxiliary enterprise 1.8 1.6 0.2 12.5
Scholarships, student grants, and waivers 5.0 4.6 0.4 8.7
Depreciation and amortization 3.9 3.7 0.2 5.4
Total operating expenses $ 48.8 $ 46.3 $ 2.5 5.4
Operating Expenses, Excluding State On-behalf Payments, for the Years Ended
(in millions)
Increase Percent
Excluding On-Behalf Payments 2025 2024 (Decrease) Change
Instruction $ 9.3 $ 8.5 $ 0.8 9.4 %
Academic support 2.9 2.5 0.4 16.0
Student services 3.2 3.3 (0.1) (3.0)
Public service/continuing education 3.0 3.0 - -
Operation and maintenance of plant 4.8 4.7 0.1 2.1
Institutional support 8.2 8.1 0.1 1.2
Auxiliary enterprise 1.6 1.4 0.2 14.3
Scholarships, student grants, and waivers 5.0 4.6 0.4 8.7
Depreciation and amortization 3.9 3.7 0.2 5.4
Total operating expenses $ 41.9 $ 39.8 $ 2.1 5.3
Total operating expenses for the year ended June 30, 2025 increased $2.5 million compared to the year ended 
June 30, 2024. Included in total operating expenses are $6.9 million of combined pension and OPEB expenses 
paid on-behalf of the College by the State of Illinois, which are allocated pro-rata across operating expense 
programs based on salary expenses. These on-behalf expenses represent the College’s portion of the SURS 
pension and CIP OPEB contributions. The State of Illinois has the legal obligation to make contributions 
directly to the SURS pension plan. The College recognizes revenue and a corresponding employee benefit 
expense for the College’s proportionate share of the State’s payments. The revenues and expenses recorded 
for these payments do not pass through the College. These on-behalf payments occur annually, and amounts 
may fluctuate significantly year to year. The CIP on-behalf amounts for both fiscal years 2024 and 2025 were
net OPEB benefits, which reduce the total on-behalf expense. For the year ended June 30, 2025, the College 
recognized revenue and expense of $9.2 million for on-behalf SURS pension contributions, offset by $2.3
million on-behalf CIP OPEB benefits.
6f
<PARSED TEXT FOR PAGE: 17 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT #530
CARTERVILLE, ILLINOIS
MANAGEMENT’S DISCUSSION AND ANALYSIS (CONTINUED)
JUNE 30, 2025
Financial Analysis of the College as a Whole (Concluded)
Excluding these on-behalf expense allocations, operating expenses increased $2.1 million compared to the year 
ended June 30, 2024. The largest increase was in instructional expenses, which increased $0.8 million largely 
due to a $0.6 million increase in combined salaries and benefits and a $0.4 million increase in materials and 
supplies, offset partially by a $0.2 million decrease in other expenses. The increase in materials and supplies 
occurred in the restricted purposes fund and was supported by grants and donations, primarily for the allied 
health and career and technical education programs.
Across all programs, total salaries increased $0.1 million and the cost of employee benefits decreased $0.2
million. Contractual services increased $0.3 million, depreciation increased $0.2 million, utilities increased 
$0.1 million, general materials and supplies increased $0.4 million, fixed charges decreased $0.4 million, and 
conference and meeting expenses remained flat. The effect of pensions and other post-employment benefit 
plans, excluding state on-behalf payments, remained consistent from fiscal year 2024 to fiscal year 2025.
Capital and Debt Activities
Capital Assets, Net, as of June 30
(in millions)
Increase Percent
Capital Assets 2025 2024 (Decrease) Change
Site and site improvements $ 6.6 $ 6.6 $ - - %
Buildings and improvements 95.8 95.4 0.4 0.4
Equipment and other 12.5 11.3 1.2 10.6
Intangible assets 2.9 0.8 1.4 175.0
Construction in progress 6.9 1.1 5.8 527.3
Total historical cost 124.7 115.2 9.5 8.2
Less accumulated depreciation
 and amortization 58.7 55.2 3.5 6.3
Net capital assets $ 66.0 $ 60.0 $ 6.0 10.0 %
Net capital assets increased by $6.0 million, or 10.0%. Depreciation expense increased by $0.2 million. During 
the year ended June 30, 2025, the College completed the B-Wing basement level renovations for the allied 
health program. Construction in progress, with an increase of $5.8 million from June 30, 2024, contains several 
other significant construction projects, including the Harrison Bruce Player Development Center, the Career 
and Technical Center project, C- and E-Wing renovations, C-Wing HVAC upgrades, the west entry elevator, 
the Logan Hall expansion, electrical system and transformer upgrades, and several other smaller projects. See 
Note 15 of the notes to the financial statements for a list of these projects and the estimated remaining project 
commitments as of June 30, 2025.
Instructional, office, and service equipment of $1.5 million was placed into service during the year. The net 
book value of asset disposals during the fiscal year was not significant. Intangible capital assets increased by 
$1.4 million. The College’s intangible capital assets are comprised of right-to-use leased equipment and 
subscription-based information technology arrangements (SBITAs). 
6g
<PARSED TEXT FOR PAGE: 18 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT #530
CARTERVILLE, ILLINOIS
MANAGEMENT’S DISCUSSION AND ANALYSIS (CONCLUDED)
JUNE 30, 2025
Capital and Debt Activities (Concluded)
The College’s debt activity for the year consisted of:
Bonds payable, July 1, 2024 $ 18,890,000
Bonds issued -
Bonds retired (4,360,000)
Bonds payable, June 30, 2025 $ 14,530,000
Bond retirements of $4.4 million occurred during the year in accordance with the original debt retirement 
schedules of previously issued bonds.
Lease liability, July 1, 2024 $ 142,765
Increases -
Decreases (41,633)
Lease liability, June 30, 2025 $ 101,132
Subscription liability, July 1, 2024 $ 316,664
Increases 1,645,796
Decreases (124,746)
Subscription liability, June 30, 2025 $ 1,837,714
See Note 5 in the notes to the financial statements for a list of additional changes in general long-term debt.
6h
<PARSED TEXT FOR PAGE: 19 / 117>
BASIC FINANCIAL STATEMENTS
<PARSED TEXT FOR PAGE: 20 / 117>
Assets
Current Assets
Cash and Cash Equivalents $ 16,125,463 $ 583,538
Receivables
Property Taxes 17,415,783 -
Governmental Claims 1,739,363 -
Tuition and Fees, Net of Allowance for 
Doubtful Accounts of $823,253 1,058,722 -
Other 1,042,293 1,728
Inventories 48,277 -
Prepaid Expenses 866,007 3,250
Total Current Assets 38,295,908 588,516
Non-Current Assets
Restricted Cash and Cash Equivalents 24,165,982 -
Investments - 11,300,455
Tangible and Intangible Capital Assets, Net 65,993,566 -
Total Non-Current Assets 90,159,548 11,300,455
Total Assets 128,455,456 11,888,971
Deferred Outflows of Resources
College OPEB Plan Related Amounts 269,522 -
CIP OPEB Plan Related Amounts 446,963 -
Pension Related Amounts 193,240 -
Deferred Loss on Refunded Bonds Payable 205,730 -
Total Deferred Outflows of Resources 1,115,455 -
Liabilities
Current Liabilities
Accounts Payable 2,328,042 247,673
Accrued Expenses 1,711,596 -
Refundable Advances 1,032,464 3,400
Accrued Bond Interest 46,824 -
Accrued Compensated Absences, Due in One Year 1,019,366 -
Lease Liability, Due in One Year 47,362 -
Subscription Liability, Due in One Year 574,430 -
Bonds Payable, Due in One Year 4,495,000 -
Total Current Liabilities 11,255,084 251,073
JUNE 30, 2025
John A. Logan 
College
John A. Logan 
College Foundation
Component Unit
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
STATEMENT OF NET POSITION
CARTERVILLE, ILLINOIS
The accompanying notes are an integral part of these financial statements.
7
<PARSED TEXT FOR PAGE: 21 / 117>
Non-Current Liabilities
Accrued Compensated Absences $ 2,659,880 $ -
Net OPEB Liability 11,845,443 -
Lease Liability 53,770 -
Subscription Liability 1,263,284 -
Bonds Payable, Net of Unamortized Premium of $696,534 10,731,534 -
Total Non-Current Liabilities 26,553,911 -
Total Liabilities 37,808,995 251,073
Deferred Inflows of Resources
College OPEB Plan Related Amounts 275,796 -
CIP OPEB Plan Related Amounts 7,475,228 -
Deferred Property Tax Revenue 17,268,114 -
Deferred Tuition and Fees 463,961 -
Deferred Pepsi Agreement 845,000 -
Total Deferred Inflows of Resources 26,328,099 -
Net Position
Net Investment in Capital Assets 53,438,916 -
Restricted for
Debt Service 376,557 -
Capital Projects 11,804,391 -
Employee Benefits 1,569,818 -
Liability Protection 1,773,377 -
Working Cash 7,535,685 -
Other 54,173 -
Without Donor Restrictions - 1,717,295
With Donor Restrictions - 9,920,603
Unrestricted (11,119,100) -
Total Net Position $ 65,433,817 $ 11,637,898
Component Unit
John A. Logan 
College
John A. Logan 
College Foundation
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
STATEMENT OF NET POSITION (Concluded)
JUNE 30, 2025
The accompanying notes are an integral part of these financial statements.
8
<PARSED TEXT FOR PAGE: 22 / 117>
Revenues
Operating Revenues:
Student Tuition and Fees, Net of Scholarships and 
Allowances of $6,619,514 $ 3,923,330 $ -
Contributions of Financial Assets - 972,828
Contributions of Nonfinancial Assets - 441,521
Auxiliary Enterprise Revenue 1,247,069 -
Other 465,826 61,863
Total Operating Revenues 5,636,225 1,476,212
Expenses
Operating Expenses:
Instruction 11,860,486 105,000
Academic Support 3,434,277 -
Student Services 4,003,982 1,545,616
Public Service/Continuing Education 3,524,087 -
Operation and Maintenance of Plant 5,762,250 -
Institutional Support 9,497,182 191,168
Auxiliary Enterprise 1,838,859 -
Scholarships, Student Grants, and Waivers 5,017,935 -
Depreciation and amortization 3,872,793 -
Total Operating Expenses 48,811,851 1,841,784
Operating Income (Loss) (43,175,626) (365,572)
Non-Operating Revenues (Expenses)
Property Taxes 16,912,602 -
Corporate Personal Property Replacement Taxes 856,341 -
State Grants and Contracts 12,381,740 -
Federal Grants and Contracts 9,905,727 -
Nongovernmental Gifts, Grants, and Bequests 1,332,583 -
On-Behalf Revenues - SURS & CIP 6,929,451 -
Investment Income 1,621,895 361,335
Bond Premium Amortization (Interest Expense), Net (552,122) -
Realized Capital Gains (Losses) - (21,249)
Unrealized Capital Gains (Losses) - 840,580
Total Non-Operating Revenues (Expenses) 49,388,217 1,180,666
Income before Capital Contributions 6,212,591 815,094
Capital Contributions 2,464,608 -
Change in Net Position 8,677,199 815,094
Net Position, July 1, 2024 (as restated) 56,756,618 10,822,804
Net Position, June 30, 2025 $ 65,433,817 $ 11,637,898
John A. Logan 
College
John A. Logan 
College Foundation
STATEMENT OF REVENUES, EXPENSES, AND CHANGES IN NET POSITION
FOR THE YEAR ENDED JUNE 30, 2025
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
Component Unit
CARTERVILLE, ILLINOIS
The accompanying notes are an integral part of these financial statements.
9
<PARSED TEXT FOR PAGE: 23 / 117>
Cash Flows from Operating Activities
Tuition and Fees $ 4,728,949
Payments to Suppliers (10,514,471)
Payments to and Benefits for Employees (29,508,435)
Auxiliary Enterprise Charges 1,247,069
Other Receipts 319,735
Net Cash Provided (Used) by Operating Activities (33,727,153)
Cash Flows from Noncapital Financing Activities
Property Taxes 16,964,431
Corporate Personal Property Replacement Taxes 924,956
Grants, Contracts, Gifts, and Bequests 20,858,361
Net Cash Provided (Used) by Noncapital Financing Activities 38,747,748
Cash Flows from Capital and Related Financing Activities
Capital Grants, Contracts, Gifts, and Bequests 4,762,442
Principal Paid on Bonds (4,360,000)
Principal Paid on Lease Liabilities (41,633)
Principal Paid on SBITAs (124,746)
Interest Paid on Debt (676,347)
Purchases of Capital Assets (8,291,523)
Net Cash Provided (Used) by Capital and Related Financing Activities (8,731,807)
Cash Flows from Investing Activities
Interest Income 1,621,895
Net Cash Provided (Used) by Investing Activities 1,621,895
Net Increase (Decrease) in Cash and Cash Equivalents (2,089,317)
Cash and Cash Equivalents, July 1, 2024 42,380,762
Cash and Cash Equivalents, June 30, 2025 $ 40,291,445
Reconciliation of Operating Income (Loss) to Net
Cash Provided (Used) by Operating Activities:
Operating Income (Loss) $ (43,175,626)
Adjustments to Reconcile Operating Income (Loss) to
Net Cash Provided (Used) by Operating Activities:
On-Behalf - SURS & CIP 6,929,451
Depreciation Expense 3,872,793
Loss on Disposed Capital Assets 21,347
Change in Assets, Liabilities, and Deferred Outflows (Inflows):
Tuition and Fees Receivables (net) 767,771
Other Receivables 179,921
Inventories (9,495)
Prepaid Expenses (141,737)
Net College OPEB-Related Deferred Outflows/Inflows 795,899
Net CIP OPEB-Related Deferred Outflows/Inflows (1,922,191)
Pension Related Deferred Outflows 19,208
Net OPEB Liability (1,258,342)
Accounts Payable 791,988
Accrued Expenses (309,976)
Deferred Tuition and Fees (17,958)
Refundable Advances (270,206)
Net Cash Provided (Used) by Operating Activities $ (33,727,153)
Noncash Capital and Related Financing Activities
During the year ended June 30, 2025, the College entered into three new subscription-based information
technology arrangements (SBITAs) as detailed in Note 12. The total cost of these SBITAs was $2,155,269,
with a related subscription liability of $1,645,796 recorded at commencement of these SBITAs. A cash
downpayment of $509,473 was made on these SBITAs.
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
STATEMENT OF CASH FLOWS
FOR THE YEAR ENDED JUNE 30, 2025
The accompanying notes are an integral part of these financial statements.
10
<PARSED TEXT FOR PAGE: 24 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS
JUNE 30, 2025
NOTE 1: SUMMARY OF SIGNIFICANT ACCOUNTING POLICIES
John A. Logan College, Community College District No. 530 (the College) is organized under the Illinois 
Public Community College Act with partial funding by the Illinois Community College Board. The 
College encompasses parts of five counties in Southern Illinois. 
The accounting policies of the College conform to accounting principles generally accepted in the United 
States of America (GAAP) as applicable to colleges and universities as well as those prescribed by the 
Illinois Community College Board (ICCB). The College reports are based on all applicable Government 
Accounting Standards Board (GASB) pronouncements. 
The following is a summary of the more significant accounting policies followed by the College.
A. Reporting Entity
The accompanying financial statements include all entities for which the elected, eight-member Board of 
Trustees of the College has financial accountability. 
The College has developed criteria to determine whether other entities are component units of the 
College. Component units are legally separate organizations for which the elected officials of the College 
are financially accountable. The College would be considered financially accountable if it appoints a 
voting majority of the organization’s governing body and (1) it is able to impose its will (significantly 
influence the programs, projects, activities, or level of services performed or provided by the 
organization) on the organization or (2) there is a potential for the organization to provide specific 
financial benefits to, or impose specific financial burdens on, the College (i.e., entitled to or can access 
the organization’s resources, is legally obligated or has otherwise assumed the obligation to finance 
deficits of, or provide financial support to the organization, or is obligated in some manner for the debt of 
the organization). If an organization is fiscally dependent on the College, the College is considered 
financially accountable regardless of whether the organization has (1) a separately elected governing 
board, (2) a governing board appointed by a higher level of government, or (3) a jointly appointed board.
Additionally, organizations that raise and hold economic resources for the direct benefit of the College are 
considered to be component units.
Based on the foregoing criteria, the following organization is considered to be a component unit and is 
discretely presented in the basic financial statements.
The John A. Logan College Foundation (the Foundation) is a legally separate, tax-exempt component unit 
of the College. The Foundation acts primarily as a fundraising organization to supplement the resources 
that are available to the College. The Foundation is governed by a separate board of directors and consists 
of graduates and friends of the College. Although the College does not control the timing or amount of 
receipts from the Foundation, the resources, or income thereon, which the Foundation holds and invests 
are restricted for the benefit of the College, its students, and its programs. Because the restricted resources 
held by the Foundation can only be used by, or for the benefit of, the College, the Foundation is 
considered to be a component unit of the College. 
11
<PARSED TEXT FOR PAGE: 25 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 1: SUMMARY OF SIGNIFICANT ACCOUNTING POLICIES (CONTINUED)
A. Reporting Entity (Concluded)
The Foundation is a private nonprofit organization that reports its financial results under Financial 
Accounting Standards Board (FASB) Statements. Most significant to the Foundation’s operations and 
reporting model is FASB Accounting Standards Codification 958-205, Presentation of Financial 
Statements for Not-For-Profit Entities. As such, certain revenue recognition criteria and presentation 
differ from GASB revenue recognition criteria and presentation. No modifications have been made to the 
Foundation’s financial information in the College’s financial reporting entity for these differences; 
however, significant note disclosures (see Component Unit Notes 1W & 18) to the Foundation’s financial 
statements have been incorporated into the College’s notes to the financial statements. 
Separate financial statements for the Foundation can be obtained from the Foundation office at 700 Logan 
College Drive, Carterville, IL 62918.
B. Measurement Focus, Basis of Accounting, and Financial Statement Presentation
As a public institution, the College is considered a special-purpose government under the provisions of 
GASB Statement No. 35, Basic Financial Statements – and Management’s Discussion and Analysis – for 
Public Colleges and Universities – An Amendment of GASB Statement No. 34. The College records 
revenue in part from tuition, fees, and other charges for services to external users, and, accordingly, has 
chosen to present its financial statements using the reporting model for special-purpose governments 
engaged in business-type activities. This model allows for all financial information of the College to be 
reported in a single column in each of the financial statements, accompanied by a separate column for its 
discretely presented component unit. All significant internal activity between funds has been eliminated 
from these financial statements.
The accompanying financial statements have been prepared using the economic resources measurement 
focus and the accrual basis of accounting in accordance with accounting principles generally accepted in 
the United States of America. Revenues from exchange transactions are recorded when earned and 
expenses are recorded when a liability is incurred, regardless of the timing of related cash flows.
Intergovernmental revenues, such as federal, state, and local grants, and state shared revenues generally 
meet the definition of non-exchange transactions and are accounted for as non-operating revenues, with 
the exception of intergovernmental revenues used for capital assets which are accounted for as capital 
contributions. Revenue from these sources is recognized when all applicable eligibility requirements 
have been met. Eligibility requirements include timing requirements, which specify the year when the 
resources are required to be used or the fiscal year when use is first permitted; matching requirements, in 
which the College must provide local resources to be used for a specific purpose; and expenditure 
requirements, in which the resources are provided to the College on a reimbursement basis. Receivables 
are reported for these amounts for which revenue has been recognized but the related payments have not 
been received.
12
<PARSED TEXT FOR PAGE: 26 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 1: SUMMARY OF SIGNIFICANT ACCOUNTING POLICIES (CONTINUED)
B. Measurement Focus, Basis of Accounting, and Financial Statement Presentation (Concluded)
Property tax revenues are reported in accordance with National Council on Governmental Accounting 
(NCGA) Interpretation No. 3, Revenue Recognition – Property Taxes, GASB Statement No. 33, 
Accounting and Financial Reporting for Nonexchange Transactions, and GASB Interpretation No. 5, 
Property Tax Revenue Recognition in Governmental Funds. Consequently, under the accrual basis of 
accounting, property tax revenue is recognized in the period for which the taxes are levied. Property tax 
receivables are reported when the College has an enforceable legal claim to the taxes, which is considered 
to be the lien date. 
The accounting and reporting policies of the College conform to generally accepted accounting principles 
applicable to government units and Illinois community colleges. The GASB is the accepted standard 
setting body for establishing accounting and financial reporting principles. These authoritative 
pronouncements are consistent with the accounting practices prescribed or permitted by the Illinois 
Community College Board (ICCB), as set forth in the ICCB Fiscal Management Manual. The following 
is a summary of the more significant policies.
C. Budgets
Although the College adopts an expanded operational budget, the budget legally required by the Illinois 
Community College Board contains only a statement of cash on hand at the beginning of the fiscal year, 
an estimate of the cash expected to be received during such fiscal year from all sources, an estimate of the 
expenditures contemplated for such fiscal year, and a statement of the estimated cash expected to be on 
hand at the end of such year.
D. Estimates
The preparation of financial statements in conformity with accounting principles generally accepted in the 
United States of America requires the use of management’s estimates and assumptions that affect certain 
reported amounts and disclosures. Accordingly, actual results may differ from those estimates.
13
<PARSED TEXT FOR PAGE: 27 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 1: SUMMARY OF SIGNIFICANT ACCOUNTING POLICIES (CONTINUED)
E. Cash and Cash Equivalents
Cash includes deposits held at banks and small amounts of cash held for change funds. Cash equivalents 
include deposits held in the Illinois Funds Money Market Fund due to its liquidity and/or short-term 
nature.
The College’s investment policy allows for cash deposits to be invested in accordance with those 
securities allowed for by statute. Chapter 122, Section 103.47 of the Illinois Public Community College 
Act and Chapter 85, Sections 901-907 of the Investment of the Public Funds Act allow current operating 
funds, special funds, interest and sinking funds, and other funds belonging to or in the custody of a 
community college, including restricted and non-restricted funds, to be invested in U.S. Treasury and U.S. 
Agencies, repurchase agreements, certificates of deposit, the Illinois School District Liquid Asset Fund 
Plus, and the Illinois Treasurers’ Investment Pool (Illinois Funds).
The Illinois Funds is an investment pool managed by the State of Illinois, Office of the Treasurer, which 
allows governments in the State to pool their funds for investment purposes. Illinois Funds is not 
registered with the Securities and Exchange Commission (SEC) as an investment company. Illinois 
Funds does meet all the criteria in GASB Statement No. 79, paragraph 4, which allows the reporting of its 
investments at amortized cost. Investments in Illinois Funds are valued at share price, which is the price 
the investment could be sold for. 
The College’s investment policy reduces the risk related to cash deposits through requiring deposits in 
excess of the federally insured amount to be appropriately collateralized to the extent of 110% and such 
collateralization shall be evidenced by an approved written agreement.
F. Restricted Cash and Cash Equivalents
Cash that is externally restricted to make debt service payments, or to purchase or construct capital or 
other noncurrent assets, is classified as noncurrent assets in the Statement of Net Position.
G. Receivables
Receivables consist of tuition and fee charges to students, auxiliary enterprise fees for services provided 
to students, faculty, and staff, the majority of each residing in Illinois, and property tax receivables. 
These receivables are recorded net of estimated uncollectible amounts, which is based on management’s 
assessment of collectability of specific students’ accounts and the aging of the accounts receivable. If the 
actual defaults are higher than the historical experience, management’s estimates of the recoverability of 
amounts due could be adversely affected. All accounts, or portions thereof, deemed to be uncollectible or 
to require an excessive collection cost are written-off to the allowance for doubtful accounts.
Receivables also include amounts due from various state and federal granting agencies. These amounts 
are considered to be 100% collectible.
14
<PARSED TEXT FOR PAGE: 28 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 1: SUMMARY OF SIGNIFICANT ACCOUNTING POLICIES (CONTINUED)
H. Inventories
Inventories are stated at the lower of cost or net realizable value on the first in, first out (FIFO) basis. 
Inventories represent items held for resale by the College’s auxiliary enterprises. 
I. Prepaid Expenses
Prepaid expenses represent current expenditures which benefit future periods.
J. Capital Assets
Capital assets include property, improvements to property, vehicles, and equipment. Capital assets are 
defined by the College as assets with an initial cost of $5,000 or more and an estimated useful life in 
excess of one year. Certain assets have higher capitalization thresholds, including leasehold 
improvements of $20,000, site of $25,000, building improvements and site improvements of $50,000, and 
buildings of $100,000. Such assets are recorded at historical cost or estimated historical cost if purchased 
or constructed. Donated capital assets are recorded at estimated fair market value at the date of donation. 
The costs of normal maintenance and repairs that do not add to the value of an asset or materially extend 
the asset’s life are not capitalized. Major outlays for capital assets and improvements are capitalized as 
projects are constructed. 
Depreciation is computed by the straight-line method over the estimated useful lives as follows:
Buildings and Improvements 50 Years
Leasehold Improvements 15 Years
Site Improvements 10 Years
Equipment 8 Years
Vehicles 5 Years
Computer Software 3 Years
K. Leases
The College is a lessee for a noncancelable lease of copiers. The College recognizes a lease liability and 
an intangible right-to-use lease asset in the government-wide financial statements. 
At the commencement of a lease, the College initially measure the lease liability at the present value of 
payments expected to be made during the lease term. Subsequently, the lease liability is reduced by the 
principal portion of the lease payments made. The right-to-use asset is initially measured as the initial 
amount of the lease liability adjusted for lease payments made at or before the lease commencement date, 
plus certain initial direct costs. Right-to-use lease assets useful lives are determined by the length of the 
lease period and are amortized using the straight-line method. The College has elected to use a 
capitalization threshold for leased assets of $25,000. 
15
<PARSED TEXT FOR PAGE: 29 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 1: SUMMARY OF SIGNIFICANT ACCOUNTING POLICIES (CONTINUED)
K. Leases (Concluded)
Key estimates and judgments include how the College determines the discount rate and lease term it uses 
to discount the expected lease payments to present value. The College uses the market rate of interest at 
lease inception as the discount rate for leases. Lease term includes the noncancelable period of the lease. 
Lease payments included in the measurement of the lease payable are composed of fixed payments as 
outlined in the lease agreements. 
L. Subscription-Based Information Technology Agreements (SBITAs)
The College obtains the right to use vendor’s information technology software through various long-term 
contracts. The College recognizes a subscription liability and an intangible right-to-use subscription asset 
in the government-wide financial statements.
At the commencement of a subscription, the College initially measures the subscription liability at the 
present value of payments expected to be made during the subscription term. Subsequently, the 
subscription liability is reduced by the principal portion of the subscription payments made. The right-to￾use asset is initially measured as the initial amount of the subscription liability adjusted for subscription 
payments made at or before the subscription commencement date, plus certain initial implementation 
costs. Right-to-use subscription assets’ useful lives are determined by the length of the subscription 
period and are amortized using the straight-line method. The College has elected to use a capitalization 
threshold for subscription assets of $25,000. 
Key estimates and judgments include how the College determines the discount rate and subscription term 
it uses to discount the expected subscription payments to present value. The College uses the market rate 
of interest at the subscription’s inception as the discount rate. The subscription’s term includes the 
noncancelable period of the subscription. Subscription payments included in the measurement of the 
subscription payable are composed of fixed payments as outlined in the subscription.
M. Amortization of Debt Issuance Premiums
The College amortizes debt issuance premiums by the straight-line method over the period the related 
debt issue is outstanding. The debt premium is amortized by using the same interest rate as the related 
debt issue, and the current period amortization is shown as a decrease to current period interest expense. 
Bond issuance costs are expensed at the time debt is issued. 
16
<PARSED TEXT FOR PAGE: 30 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 1: SUMMARY OF SIGNIFICANT ACCOUNTING POLICIES (CONTINUED)
N. Deferred Outflows (Inflows) of Resources
Deferred outflows are defined under GASB Statement No. 63 as a consumption of net assets by the 
College that is applicable to a future reporting period and should be reported as having a similar impact 
on net position as assets. For the College, pension payments related to employees with federally funded 
positions and made subsequent to the pension liability measurement date are considered to be deferred 
outflows in accordance with GASB Statement No. 71, Pension Transition for Contributions Made 
Subsequent to the Measurement Date – An Amendment of GASB Statement No. 68. Changes in 
assumptions and differences between expected and actual experience of the College’s other 
postemployment benefit (OPEB) plans are considered to be deferred outflows. Changes in proportion and 
differences between employer contributions and actual contributions and its proportionate share of 
contributions to the plan relative to all employers is also considered to be a deferred outflow. Deferred 
outflows also include losses on debt refundings, which are amortized over the remaining life of the new 
debt, or refunded debt, whichever is shorter. 
Deferred inflows of resources are defined under GASB Statement No. 63 as acquisitions of net assets that 
are applicable to a future reporting period and should be reported as having a similar impact on net 
position as liabilities. At June 30, 2025, deferred inflows of resources included tax levies accrued that are 
levied for use in the next fiscal year, student tuition and fees that were collected or accrued for the next 
academic year, the unamortized portion of the net difference between projected and actual earnings on 
OPEB investments, and the unrecognized portion of revenues from a long-term vendor contract.
O. Net Position
The College’s net position is classified as follows:
Net Investment in Capital Assets – This represents the College’s total investment in capital assets, net of 
accumulated depreciation and reduced by the outstanding balances of any bonds, mortgages, notes, or 
other borrowings that are attributable to the acquisition, construction, or improvement of those assets.
Restricted – This represents assets/resources that are legally or contractually obligated to be spent in 
accordance with restrictions imposed by external third parties, reduced by liabilities and deferred inflow 
resources related to those assets. Sources of restricted revenue include federal, state, and private grants 
and contracts. Externally restricted funds may be utilized only in accordance with the purpose established 
by the source of such funds and are in contrast with unrestricted funds over which the Board of Trustees 
retains full control to use in achieving any of its institutional purposes. When both restricted and 
unrestricted resources are available for use, it is the College’s policy to use restricted resources first, then 
unrestricted resources when they are needed.
Unrestricted – This represents unrestricted assets/resources derived from student tuition and fees, state 
appropriations, and sales and services of educational departments and auxiliary enterprises. These 
resources are used for transactions relating to the educational and general operations of the College and 
may be used at the discretion of the Board of Trustees to meet current expenses for any lawful purpose.
17
<PARSED TEXT FOR PAGE: 31 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 1: SUMMARY OF SIGNIFICANT ACCOUNTING POLICIES (CONTINUED)
P. Classification of Revenues and Expenses
Operating revenue includes activities that have the characteristics of exchange transactions such as 
(1) student tuition and fees, net of scholarship allowances, and (2) sales and services of auxiliary 
enterprises. Non-operating revenue includes activities that have the characteristics of non-exchange 
transactions, such as (1) local property taxes, (2) state appropriations, (3) most federal, state, and local 
grants and contracts and federal appropriations, and (4) gifts and contributions. Operating expenses are 
those expenses directly attributable to the operations of the College. Incidental expenses are classified as 
non-operating expenses.
Q. Scholarship Discounts and Allowances
Student tuition and fee revenues, and certain other revenues from students, are reported net of scholarship 
discounts and allowances in the Statement of Revenues, Expenses, and Changes in Net Position. 
Scholarship discounts and allowances are the difference between the stated charge for goods and services 
provided by the College, and the amount that is paid by students or third parties making payments on the 
students’ behalf. Certain governmental grants, such as Pell grants, and other federal, state, or 
nongovernmental programs, are recorded as nonoperating revenues in the College’s financial statements. 
To the extent that revenues from such programs are used to satisfy tuition and fees and other student 
charges, the College has recorded a scholarship discount and allowance.
R. Property Taxes
The 2024 property tax extension has been deferred to comply with GASB Statement No. 33 since it was 
levied to finance activities of the 2025/2026 academic year. In accordance with these guidelines, property 
tax revenue is to be recognized in the period the levy is intended to finance. 
The College must file its tax levy ordinance by the last Tuesday in December of each year. The College’s 
property tax is levied each year on all taxable real property located within the District. These taxes attach 
an enforceable lien on real property as of January 1 and are payable in two installments; due dates vary by 
county. The College receives significant property tax receipts from July through November.
S. Federal Financial Assistance Programs
The College participates in federally funded PELL Grants, FSEOG Grants, and Federal Work-Study. 
Federal programs are audited in accordance with Title 2 U.S. Code of Federal Regulations (CFR) Part 
200, Uniform Administrative Requirements, Cost Principles, and Audit Requirements for Federal Awards 
(Uniform Guidance), Federal Awarding Agency Regulatory Implementation of Office Management and 
Budget’s Uniform Administrative Requirements, Cost Principles, and Audit Requirements for Federal 
Awards, Audit of States, Local Governments and Non-Profit Organizations, and the Compliance 
Supplement. 
18
<PARSED TEXT FOR PAGE: 32 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 1: SUMMARY OF SIGNIFICANT ACCOUNTING POLICIES (CONTINUED)
T. Pensions
For purposes of measuring the net pension liability, deferred outflows of resources and deferred inflows 
of resources related to pensions, and pension expense, information about the plan net position of the State 
Universities Retirement System (SURS or the System) and additions to/deductions from SURS plan net 
position has been determined on the same basis as they are reported by SURS. For this purpose, benefit 
payments (including refunds of employee contributions) are recognized when due and payable in 
accordance with the benefit terms. Investments are reported at fair value.
For financial reporting purposes, the State of Illinois (State) and its public universities and community 
colleges are under a special funding situation. A special funding situation exists when a non-employer 
entity (the State) is legally responsible for making contributions directly to a pension plan that is used to 
provide pensions to the employees of another entity (John A. Logan College) and the non-employer (the 
State) is the only entity with a legal obligation to make contributions directly to a pension plan. John A. 
Logan College recognizes its proportionate share of the State’s pension expense relative to John A. Logan 
College’s employees as non-operating revenue and pension expense, with the expense further allocated to 
the related function by employees. 
U. Other Postemployment Benefits (OPEB)
For purposes of measuring the other postemployment benefits (OPEB) obligations, deferred outflows of 
resources and deferred inflows of resources related to OPEB, and benefits expense, information about the 
net position of the OPEB plans and additions to and deductions from the OPEB plans’ net positions have 
been determined on the same basis as they are reported by the OPEB plans. For this purpose, benefit 
payments (including refunds of employee contributions) are recognized when due and payable in 
accordance with the benefit terms. Investments are reported at fair value.
V. Insurance Coverage
The College is exposed to various risks of loss including, but not limited to torts; theft of, damage to, and 
destruction of assets; errors and omissions; injuries to employees; and natural disasters. To limit exposure 
to these risks, the College has obtained coverage from commercial insurance companies for all major 
programs: property, liability, and workmen’s compensation. Expenditures and claims are recognized in 
the year in which they are notified of the loss. During the current fiscal year, there were no significant 
reductions in insurance coverage. Also, there have been no settlements which have exceeded insurance 
coverage during the past three fiscal years. 
W. Component Unit
The Foundation is required to report information regarding its financial position and activities based on 
the existence or absence of donor or grantor-imposed restrictions. Accordingly, net assets and changes 
therein are classified and reported as follows:
19
<PARSED TEXT FOR PAGE: 33 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 1: SUMMARY OF SIGNIFICANT ACCOUNTING POLICIES (CONCLUDED)
W. Component Unit (Concluded)
Net Assets Without Donor Restrictions – Net assets available for use in general operations and not subject 
to donor (or certain grantor) restrictions.
Net Assets With Donor Restrictions – Net assets subject to donor (or certain grantor) imposed restrictions. 
Some donor-imposed restrictions are temporary in nature, such as those that will be met by the passage of 
time or other events specified by the donor. Other donor-imposed restrictions are perpetual in nature, 
where the donor stipulates that resources be maintained in perpetuity. Donor-imposed restrictions are 
released when a restriction expires, that is, when the stipulated time has elapsed, when the stipulated 
purpose for which the resource was restricted has been fulfilled, or both. 
X. Subsequent Events
The College has evaluated subsequent events through February 19, 2026, the date which the financial 
statements were available to be issued.
NOTE 2: CASH AND CASH EQUIVALENTS
At June 30, 2025, the carrying amount and bank balance of the College’s deposits is as follows:
Carrying Bank
Amount Balance
Cash and Cash Equivalents
 Cash Accounts $ 19,183,812 $ 19,278,934
 US Treasury Obligations 2,202,806 2,202,806
 Illinois Funds Money Market Fund 18,904,827 18,898,239
Total Cash and Cash Equivalents $ 40,291,445 $ 40,379,979
Carrying Bank
Amount Balance
Current Assets:
 Cash and Cash Equivalents $ 16,125,463 $ 16,213,997
Noncurrent Assets:
 Restricted Cash and Cash Equivalents 24,165,982 24,165,982
$ 40,291,445 $ 40,379,979
Custodial Credit Risk
With respect to deposits, custodial credit risk refers to the risk that, in the event of a bank failure, the 
College’s deposits may not be returned to it. The College’s investment policy limits the exposure to 
deposit custodial credit risk by requiring all deposits in excess of Federal Deposit Insurance Corporation 
(FDIC) insurable limits to be secured by collateral and held at an independent, third-party institution, in 
the name of the College. As of June 30, 2025, the bank balances of the College’s deposits with financial 
institutions were all fully insured or collateralized by securities pledged by the College’s financial 
institution’s agent in the College’s name. There were no investments exposed to custodial credit risk.
20
<PARSED TEXT FOR PAGE: 34 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 2: CASH AND CASH EQUIVALENTS (CONCLUDED)
Interest Rate Risk
Interest rate risk is the risk that the fair value of investments will decrease as a result of an increase in 
interest rates. The College’s investment policy does not limit the maturities of investments as a means of 
managing its exposure to fair value losses arising from increasing interest rates. 
The Illinois Funds are measured at net asset value (NAV) amortized cost. There are no limitations on 
redemption frequency or redemption notice. Redemption frequency is daily and redemption notice period 
is one day. 
Credit Risk
Credit risk is the risk that the College will not recover its investments due to the ability of the 
counterparty to fulfill its obligation. Illinois statutes authorize the College to invest in obligations of the 
US Treasury and US Agencies, interest-bearing savings accounts, interest-bearing time deposits, money 
market mutual funds registered under the Investment Company Act of 1940 (limited to US Government 
obligations), shares issued savings and loan associations (provided the investments are insured by the 
FSLIC, short term discount obligations issued by the FNMA), share accounts of certain credit unions, 
investments in the Illinois Funds Money Market Fund, and certain repurchase agreements.
The College is also authorized to invest in short-term obligations of corporations organized in the United 
States with assets exceeding $500,000 if such obligations are rated at the time of purchase within the three 
highest classifications established by two or more standard rating services, the obligations mature within 
180 days, no more than 1/3 of the total average balances from all funds available at the end of each month 
is invested in such obligations at any time, and such purchases do not exceed 10% of a corporation’s 
outstanding obligations. Investments may be made only in banks, which are insured by the FDIC.
The College’s investment policy does not further limit its investment choices. The College’s investments 
in the Illinois Funds Money Market Fund were rated AAAmmf by Fitch’s at June 30, 2025.
Concentration of Credit Risk
Concentration of credit risk is the risk of loss attributed to the magnitude of investment in any one single 
issuer. The College’s investment policy limits the amount the College may invest in any one issuer to 
75% of the College’s total invested funds. The College is considered to have a concentration of credit 
risk of its investments if any one single issuer is greater than 5% of the total fixed income investments. 
At June 30, 2025, the College did not have a concentration of credit risk.
21
<PARSED TEXT FOR PAGE: 35 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 3: CAPITAL ASSETS
The following is a schedule of changes in capital asset categories for the fiscal year ended June 30, 2025. 
The investment in capital assets is determined by reducing historical cost by accumulated depreciation
and amortization. Depreciation and amortization expense for June 30, 2025 was $3,872,793.
Primary Government/Business-Type Activity
Balance Balance
07/01/24 Additions Deletions 06/30/25
Historical Cost:
Tangible Capital Assets, 
 Not Being Depreciated:
 Site $ 346,427 $ - $ - $ 346,427
 Construction in Progress 1,069,623 5,989,317 (125,239) 6,933,701
1,416,050 5,989,317 (125,239) 7,280,128
Tangible Capital Assets, 
 Being Depreciated:
 Site Improvements 6,341,773 - - 6,341,773
 Buildings and Improvements 95,445,503 376,594 - 95,822,097
 Equipment 11,252,335 1,541,376 (336,959) 12,456,752
113,039,611 1,917,970 (336,959) 114,620,622
 
 Intangible Capital Assets, 
 Being Amortized:
 Right to Use Leased Equipment 211,084 - - 211,084
 Right to Use SBITAs 539,805 2,155,270 - 2,695,075
750,889 2,155,270 - 2,906,159
Total Capital Assets: 115,206,550 10,062,557 (462,198) 124,806,909
Less Accumulated Depreciation for 
Tangible Capital Assets:
Site Improvements 2,434,926 513,990 - 2,948,916
Buildings and Improvements 44,412,060 1,860,025 - 46,272,085
Equipment 8,195,476 781,055 (315,614) 8,660,917
55,042,462 3,155,070 (315,614) 57,881,918
Less Accumulated Amortization for
 Intangible Capital Assets:
 Right to Use Leased Equipment 68,319 41,633 - 109,952
 Right to Use SBITAs 145,383 676,090 - 821,473
213,702 717,723 - 931,425
 
Capital Assets, Net $ 59,950,386 $ 65,993,566
22
<PARSED TEXT FOR PAGE: 36 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 4: ACCRUED EXPENSES
Accrued expenses consisted of the following at June 30, 2025:
Accrued Payroll $ 1,614,748
Accrued Benefits 38,248
Accrued Expenses - Other 58,600
$ 1,711,596
NOTE 5: CHANGES IN GENERAL LONG-TERM DEBT
The following is a summary of long-term debt transactions of the College for the year ended June 30, 
2025:
Balance
July 1, 2024, Balance
as restated Additions Deletions June 30, 2025
Bonds Payable $ 18,890,000 $ - $ 4,360,000 $ 14,530,000
Bond Premium 855,484 - 158,950 696,534
Accrued Compensated Absences
 (net change) 3,647,592 31,654 - 3,679,246
Lease Liability 142,765 - 41,633 101,132
Subscription Liability 316,664 1,645,796 124,746 1,837,714
Net OPEB Liability (net change) 13,103,785 - 1,258,342 11,845,443
Total $ 36,956,290 $ 1,677,450 $ 5,943,671 $ 32,690,069
Amount Due
Within
One Year
Bonds Payable $ 4,495,000
Accrued Compensated Absences 1,019,366
Lease Liability 47,362
Subscription Liability 574,430
Total $ 6,136,158
23
<PARSED TEXT FOR PAGE: 37 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 6: BONDS PAYABLE
Bonds payable consists of the following at June 30, 2025:
On February 29, 2016 the College issued $5,035,000 of Taxable General 
Obligation Community College Bonds, Series 2016B to refund the College’s 
Series 2015 bonds. Principal is payable December 1st of each year beginning 
on December 1, 2016. Interest is payable on these bonds on June 1st and 
December 1st of each year at 3.00% to 3.75%. The final maturity date of these 
bonds is December 1, 2030. The money is restricted for making future OPEB 
contributions. $ 2,315,000
On April 25, 2017, the College issued $13,265,000 of General Obligation 
Community College Bonds, Series 2017A to advance refund the College’s 
Series 2007 bonds. Principal is payable December 1st of each year beginning 
on December 1, 2023. Interest is payable on these bonds on June 1st and 
December 1st of each year at 3.25% to 5.00%. The final maturity date of these 
bonds is December 1, 2029. 10,125,000
On December 29, 2020, the College issued General Obligation Community 
College Bonds, Series 2020A, which created an obligation against the College 
in order to pay off the General Obligation (Limited Tax) Debt Certificates, 
Series 2020A-D. $10,160,000 was the bond issue, of which $98,235 was bond 
issuance costs, $10,058,184 paid off the Debt Certificates, and $3,581 was 
deposited in College funds. Principal is payable December 1st of each year 
beginning on December 1, 2021. Interest is payable on these bonds on June 
1
st and December 1st of each year at 1.15%. The final maturity date of these 
bonds is December 1, 2025. 2,090,000
Total Bonds Payable $ 14,530,000
24
<PARSED TEXT FOR PAGE: 38 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 6: BONDS PAYABLE (CONCLUDED)
At June 30, 2025, the College’s future cash flow requirements of long-term debt obligations by fiscal year 
were as follows:
Year Ending June 30, Principal Interest Total
 2026 4,495,000 519,278 5,014,278
 2027 2,520,000 390,879 2,910,879
 2028 2,645,000 267,988 2,912,988
 2029 2,775,000 138,355 2,913,355
 2030 1,675,000 43,779 1,718,779
 2031 420,000 7,875 427,875
14,530,000 $ 1,368,154 $ 15,898,154
 Unamortized Bond Premium 696,534
$ 15,226,534
NOTE 7: DEFINED BENEFIT PENSION PLAN
General Information about the Pension Plan
Plan Description
John A. Logan College, Community College District No. 530 contributes to the State Universities 
Retirement System of Illinois (SURS), a cost-sharing multiple-employer defined benefit plan with a 
special funding situation whereby the State of Illinois (the State) makes substantially all actuarially 
determined required contributions on behalf of the participating employers. SURS was established 
July 21, 1941, to provide retirement annuities and other benefits for staff members and employees of state 
universities and community colleges, certain affiliated organizations, and certain other state educational 
and scientific agencies and for survivors, dependents, and other beneficiaries of such employees. SURS is 
considered a component unit of the State’s financial reporting entity and is included in the State’s 
Comprehensive Annual Financial Report (CAFR) as a pension trust fund. SURS is governed by Chapter 
40, Act 5, Article 15 of the Illinois Compiled Statutes. SURS issues a publicly available financial report 
that includes financial statements and required supplementary information. That report may be obtained 
by accessing the website at www.surs.org.
Benefits Provided
A traditional benefit plan was established in 1941. Public Act 90-0448 enacted effective January 1, 1998, 
established an alternative defined benefit program known as the portable benefit package. Tier I of the 
traditional and portable plan Tier 1 refers to members that began participation prior to January 1, 2011. 
Public Act 96-0889 revised the traditional and portable benefit plans for members who began 
participation on or after January 1, 2011, and who do not have other eligible reciprocal system service. 
The revised plan is referred to as Tier 2. New employees are allowed six months after their date of hire to 
make an irrevocable election whether to participate in either the traditional or portable benefit plans. A 
summary of the benefit provisions as of June 30, 2024, can be found in the Financial Section of SURS 
ACFR.
25
<PARSED TEXT FOR PAGE: 39 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 7: DEFINED BENEFIT PENSION PLAN (CONTINUED)
General Information about the Pension Plan (Concluded)
Contributions
The State is primarily responsible for funding SURS on behalf of the individual employers at an 
actuarially determined amount. Public Act 88-0593 provides a statutory funding plan consisting of two 
parts: (i) a ramp-up period from 1996 to 2010 and (ii) a period of contributions equal to a level percentage 
of the payroll of active members within SURS to reach 90% of the total Actuarial Accrued Liability by 
the end of fiscal year 2045. Employer contributions from “trust, federal, and other funds” are provided 
under Section 15-155(b) of the Illinois Pension Code and require employers to pay contributions which 
are sufficient to cover the accruing normal costs on behalf of applicable employees. The employer normal 
cost for fiscal year 2024 and fiscal year 2025, respectively, was 12.53% and 11.98% of employee payroll. 
The normal cost is equal to the value of current year’s pension benefit and does not include any allocation 
for the past unfunded liability or interest on the unfunded liability. Plan members are required to 
contribute 8.0% of their annual covered salary except for police officers and fire fighters who contribute 
9.5% of their earnings. The contribution requirements of plan members and employers are established 
and may be amended by the State’s General Assembly.
Participating employers make contributions toward separately financed specific liabilities under Section 
15.139.5(e) of the Illinois Pension Code (relating to contributions payable due to the employment of 
“affected annuitants” or specific return to work annuitants), Section 15.155(g) (relating to contributions 
payable due to earning increases exceeding 6% during the final rate of earnings period), and Section 15-
155(j-5) (relating to contributions payable due to earnings exceeding the salary set for the Governor).
Pension Liabilities, Expense, and Deferred Outflows of Resources and Deferred Inflows of Resources 
Related to Defined Benefit Pensions
Net Pension Liability
The net pension liability (NPL) was measured as of June 30, 2024. At June 30, 2024, SURS defined 
benefit plan reported a NPL of $30,230,907,727. 
Employer Proportionate Share of Net Pension Liability
The amount of the proportionate share of the NPL to be recognized for the College is $0. The 
proportionate share of the State’s NPL associated with the College is $137,237,740 or 0.4540%. John A. 
Logan College’s proportionate share changed by (0.0103%) from 0.4643% since the last measurement 
date on June 30, 2023. This amount is not recognized in the College’s financial statements. The NPL and 
total pension liability as of June 30, 2024 was determined based on the June 30, 2023 actuarial evaluation 
rolled forward. The basis of allocation used in the proportionate share of the net pension liability is the 
actual reported pensionable contributions made to SURS defined benefit plan during fiscal year 2023. 
26
<PARSED TEXT FOR PAGE: 40 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 7: DEFINED BENEFIT PENSION PLAN (CONTINUED)
Pension Liabilities, Expense, and Deferred Outflows of Resources and Deferred Inflows of Resources 
Related to Defined Benefit Pensions (Continued)
Defined Benefit Pension Expense
For the year ending June 30, 2024, SURS defined benefit plan reported a collective net pension expense 
of $1,996,285,670.
Employer Proportionate Share of Defined Benefit Pension Expense
The employer proportionate share of collective defined benefit pension expense is recognized as 
nonoperating revenue with matching operating expense (compensation and benefits) in the financial 
statements. The basis of allocation used in the proportionate share of collective pension expense is the 
actual reported pensionable contributions made to SURS defined benefit plan during fiscal year 2023. As 
a result, the College recognized revenue and defined benefit pension expense of $9,062,438 from this 
special funding situation during the year ended June 30, 2025.
Deferred Outflows of Resources and Deferred Inflows of Resources Related to Defined Benefit Pensions
Deferred outflows of resources are the consumption of net position by SURS that is applicable to future 
reporting periods. Conversely, deferred inflows of resources are the acquisition of net position by SURS 
that is applicable to future reporting periods. 
SURS Collective Deferred Outflows and Deferred Inflows of Resources by Sources:
Deferred Outflows
of Resources
Deferred Inflows 
of Resources
Difference between expected and actual experience $ 305,114,071 $ -
Changes in assumptions 483,809,428 -
Net difference between projected and actual earnings 
 on pension plan investments - 27,577,324
 Total $ 788,923,499 $ 27,577,324
27
<PARSED TEXT FOR PAGE: 41 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 7: DEFINED BENEFIT PENSION PLAN (CONTINUED)
Pension Liabilities, Expense, and Deferred Outflows of Resources and Deferred Inflows of Resources 
Related to Defined Benefit Pensions (Concluded)
SURS Collective Deferred Outflows and Deferred Inflows of Resources by Year to be Recognized in 
Future Pension Expenses:
Net Deferred 
Outflows (Inflows) 
of Resources
Years ending June 30,
2025 $ 126,531,380
2026 756,545,086
2027 (49,545,529)
2028 (72,184,762)
2029 -
Thereafter -
Total $ 761,346,175
Employer Deferral of Fiscal Year June 30, 2025 Contributions
The College paid $193,240 in federal, trust or grant contributions to SURS defined benefit pension plan 
during the year ended June 30, 2025. These contributions were made subsequent to the pension liability 
measurement date of June 30, 2024, and are recognized as deferred outflows of resources as of June 30, 
2025. 
Assumptions and Other Inputs
Actuarial Assumptions
 
The actuarial assumptions used in the June 30, 2024 valuation were based on the results of an actuarial 
experience study for the period June 30, 2020 through June 30, 2023. The total pension liability in the 
June 30, 2024 actuarial valuation was determined using the following actuarial assumptions, applied to all 
periods included in the measurement:
Inflation 2.40%
Salary increases 3.15% to 15%, including inflation
Investment rate of return 6.50%
Mortality rates were based on the Pub-2010 employee and retiree gender district tables with projected 
generational mortality and a separate mortality assumption for disabled participants. 
28
<PARSED TEXT FOR PAGE: 42 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 7: DEFINED BENEFIT PENSION PLAN (CONTINUED)
Assumptions and Other Inputs (Continued)
The long-term expected rate of return on pension plan investments was determined using a building-block 
method in which best-estimate ranges of expected future real rates of return (expected returns, net of 
pension plan investment expense and inflation) are developed for each major asset class. These ranges 
are combined to produce the long-term expected rate of return by weighting the expected future real rates 
of return by the target allocation percentage and by adding expected inflation. Best estimates of arithmetic 
real rates of return were adopted by the plan’s trustees after considering input from the plan’s investment 
consultants and actuary. For each major asset class that is included in the pension plan’s target asset 
allocation as of June 30, 2024, these best estimates are summarized in the following table:
Asset Class Target Allocation
Weighted Average Long-Term 
Expected Real Rate of Return
Traditional Growth – Global Public Equity 36.0% 7.13%
Stabilized Growth
 Core Real Assets 8.0% 5.06%
 Public Credit Fixed Income 6.5% 4.10%
 Private Credit 2.5% 7.36%
Non-Traditional Growth
 Private Equity 11.0% 10.92%
 Non-Core Real Assets 4.0% 9.09%
Inflation Sensitive – US TIPS 5.0% 2.12%
Principal Protection – Core Fixed Income 10.0% 1.34%
Crisis Risk Offset
 Systematic Trend Following 10.0% 2.90%
 Alternative Risk Premia 3.0% 2.62%
 Long Duration 2.0% 2.84%
 Long Volatility/Tail Risk 2.0% (1.22%)
 Total 100% 5.63%
 Inflation 2.80%
 Expected Arithmetic Return 8.43%
Discount Rate
A single discount rate of 6.35% was used to measure the total pension liability. This single discount rate 
was based on an expected rate of return on pension plan investments of 6.50% and a municipal bond rate 
of 3.97% (based on the Fidelity 20-Year Municipal GO AA Index as of June 30, 2024). The projection of 
cash flows used to determine this single discount rate were the amounts of contributions attributable to 
current plan members and assumed that plan member contributions will be made at the current 
contribution rate and that employer contributions will be made at rates equal to the statutory contribution 
rates under SURS funding policy. Based on these assumptions, the pension plan’s fiduciary net position 
and future contributions were sufficient to finance the benefit payments through the year 2075. As a 
result, the long-term expected rate of return on pension plan investments was applied to projected benefit 
payments through the year 2075, and the municipal bond rate was applied to all benefit payments after 
that date.
29
<PARSED TEXT FOR PAGE: 43 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 7: DEFINED BENEFIT PENSION PLAN (CONCLUDED)
Assumptions and Other Inputs (Concluded)
Sensitivity of SURS Net Pension Liability to Changes in the Discount Rate
Regarding the sensitivity of the net pension liability to changes in the single discount rate, the following 
presents the State’s net pension liability, calculated using a single discount rate of 6.35%, as well as what 
the State’s net pension liability would be if it were calculated using a single discount rate that is 1-
percentage-point lower or 1-percentage-point-higher:
1% Decrease
5.35%
Current Single Discount 
Rate Assumption 
6.35%
1% Increase
7.35%
$ 36,700,168,358 $ 30,230,907,727 $ 24,839,790,537
Additional information regarding the SURS basic financial statements, including the plan’s net position, 
can be found in SURS Comprehensive Annual Financial Report by accessing the website at
www.SURS.org.
NOTE 8: DEFINED CONTRIBUTION PENSION PLAN
General Information about the Pension Plan
Plan Description
The College contributes to the Retirement Savings Plan (RSP) administered by the State Universities 
Retirement System (SURS), a cost-sharing multiple-employer defined contribution pension plan with a 
special funding situation whereby the State of Illinois (State) makes substantially all required 
contributions on behalf of the participating employers. SURS was established July 21, 1941, and provides
retirement annuities and other benefits for staff members and employees of state universities and 
community colleges, certain affiliated organizations, and certain other state educational and scientific 
agencies and for survivors, dependents, and other beneficiaries of such employees. SURS is governed by 
Chapter 40, Act 5, Article 15 of the Illinois Compiled Statutes. SURS issues a publicly available financial 
report that includes financial statements and required supplementary information. That report may be 
obtained by accessing the website at www.surs.org. The RSP and its benefit terms were established and 
may be amended by the State’s General Assembly.
Benefits Provided
A defined contribution pension plan, originally called the Self-Managed Plan, was added to SURS benefit 
offerings as a result of Public Act 90-0448 enacted effective January 1, 1998. The plan was renamed the 
RSP effective September 1, 2020, after an extensive plan redesign. New employees are allowed six 
months after their date of hire to make an irrevocable election whether to participate in either the 
traditional or portable defined benefit pension plans or the RSP. A summary of the benefit provisions as 
of June 30, 2024, can be found in SURS Annual Comprehensive Financial Report- Notes to the Financial 
Statements.
30
<PARSED TEXT FOR PAGE: 44 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 8: DEFINED CONTRIBUTION PENSION PLAN (CONCLUDED)
General Information about the Pension Plan (Concluded)
Contributions 
All employees who have elected to participate in the RSP are required to contribute 8.0% of their annual 
covered earnings. Section 15-158.2(h) of the Illinois Pension Code provides for an employer contribution 
to the RSP of 7.6% of employee earnings. The State is primarily responsible for contributing to the RSP 
on behalf of the individual employers. Employers are required to make the 7.6% contribution for 
employee earnings paid from “trust, federal, and other funds” as described in Section 15-155(b) of the 
Illinois Pension Code. The contribution requirements of plan members and employers were established 
and may be amended by the State’s General Assembly.
Forfeitures 
Employees are not vested in employer contributions to the RSP until they have attained five years of 
service credit. Should an employee leave SURS-covered employment with less than five years of service 
credit, the portion of the employee’s RSP account designated as employer contributions is forfeited. 
Employees who later return to SURS-covered employment will have these forfeited employer 
contributions reinstated to their account, so long as the employee’s own contributions remain in the 
account. Forfeited employer contributions are managed by SURS and are used both to reinstate 
previously forfeited contributions and to fund a portion of the State’s contributions on behalf of the 
individual employers. The vesting and forfeiture provisions of the RSP were established and may be 
amended by the State’s General Assembly.
Pension Expense Related to Defined Contribution Pensions
Defined Contribution Pension Expense
For the year ended June 30, 2024, the State’s contributions to the RSP on behalf of individual employers
totaled $96,741,887. Of this amount, $89,857,115 was funded via an appropriation from the State and 
$6,884,772 was funded from previously forfeited contributions.
Employer Proportionate Share of Defined Contribution Pension Expense
The employer proportionate share of collective defined contribution pension expense is recognized as 
nonoperating revenue with matching operating expense (compensation and benefits) in the financial 
statements. The basis of allocation used in the proportionate share of collective defined contribution 
pension expense is the actual reported pensionable contributions made to the RSP during fiscal year 2024. 
The College’s share of pensionable contributions was 0.1597%. As a result, the College recognized 
revenue and defined contribution pension expense of $154,502 from this special funding situation during 
the year ended June 30, 2025, of which $10,995 constituted forfeitures.
31
<PARSED TEXT FOR PAGE: 45 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 9: POSTEMPLOYMENT BENEFITS OTHER THAN PENSIONS 
The College participates in two postemployment benefit (OPEB) plans: the State of Illinois’ College 
Insurance Program (CIP) and an OPEB plan provided by the College. 
A. State of Illinois’ College Insurance Program
Plan Description
The College contributes to the Community College Health Insurance Security Fund (CCHISF) (also 
known as the College Insurance Program “CIP”) that was established under the State Employees Group 
Insurance Act of 1971, as amended, 5 ILCS 375/6.9(f), which became effective July 1, 1999. The CIP is 
a cost-sharing, multiple-employer defined benefit OPEB Trust Fund, which has a special funding 
situation as described in 40 ILCS 15/1.4. A non-employer (the State) is required by statute to contribute a 
defined percentage of participant payroll directly to the OPEB plan, which is administered through the 
trust. 
CIP has no component units and is not a component unit of any other entity. However, because CIP is 
not legally separate from the State of Illinois, the financials statements of the CIP are included in the 
financial statements of the State of Illinois as a pension (and other employee benefit) trust fund. This 
fund is a non-appropriated trust fund held outside the State Treasury, with the State Treasurer as 
custodian. Additions deposited into the Trust are for the sole purpose of providing health benefits to 
retirees, as established under the plan and associated administrative cost.
Benefits Provided
Through the trust the State provides health, dental, vision, and life insurance benefits for retirees and their 
dependents. Substantially all State employees become eligible for post-employment benefits if they 
eventually become annuitants of one of the State sponsored pension plans. Health, dental and vision 
benefits include basic benefits for annuitants and their dependents under the State’s self-insurance plan 
and insurance contracts currently in force. Annuitants may be required to contribute towards health, 
dental, and vision benefits with the amount based on factors such as date of retirement, years of credited 
service with the State, whether the annuitant is covered by Medicare, and whether the annuitant has 
chosen a managed health care plan. Annuitants who retired prior to January 1, 1998, and who are vested 
in the State Employees’ Retirement System do not contribute towards health, dental, and vision benefits. 
For annuitants who retire on or after January 1, 1998, the annuitant’s contribution amount is reduced five 
percent for each year of credited service with the State allowing those annuitants with twenty or more 
years of credited service to not have to contribute towards health, dental, and vision benefits. Annuitants 
also receive life insurance coverage equal to the annual salary of the last day of employment until age 60, 
at which time the benefit becomes $5,000.
32
<PARSED TEXT FOR PAGE: 46 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 9: POSTEMPLOYMENT BENEFITS OTHER THAN PENSIONS (CONTINUED)
A. State of Illinois’ College Insurance Program (Continued)
Benefits Provided (Concluded)
The State pays for a portion of the employer costs for the benefits provided. The total cost of the State’s 
portion of the health, dental, vision, and life insurance benefits of all members, including post￾employment health, dental, vision, and life insurance benefits, is recognized as an expenditure by the 
State in the Illinois Comprehensive Annual Financial Report. The State finances the costs on a pay-as￾you-go basis. The total costs incurred for health, dental, vision, and life insurance benefits are not 
separated by department or component unit for annuitants and their dependents nor active employees and 
the dependents.
A summary of post-employment benefit provision, changes in benefit provisions, employee eligibility 
requirements including eligibility for vesting, and the authority under which benefit provisions are 
established are included as an integral part of the financial statements of the Department of Central 
Management Services. A copy of the financial statements of the Department of Central Management 
Services, may be obtained by writing to the Department of Central Management Services, Stratton Office 
Building, 401 South Spring Street, Springfield, IL 62706.
Contributions
The State Employees Group Insurance Act of 1971 (5 ILCS 375/6.10) requires every active contributor of 
the State Universities Retirement System (SURS), who is a full-time employee of a community college 
district or an association of community college boards, to make contributions to the plan at the rate of 
0.5% of salary. The same section of statute requires every community college district or association of 
community college boards that is an employer under the SURS, to contribute to the plan an amount equal 
to 0.5% of the salary paid to its full-time employees who participate in the plan. The State Pension Funds 
Continuing Appropriation Act (40 ILCS15/1.4) requires the State to make an annual appropriation to the 
fund in an amount certified by the SURS Board of Trustees. The State Employees Group Insurance Act 
of 1971 (5 ILCS 375/6.9) requires the Director of the Department to determine the rates and premiums for 
annuitants and dependent beneficiaries and establish the cost-sharing parameter, as well as funding. At 
the option of the board of trustees, the college districts may pay all or part of the balance of the cost of 
coverage for retirees from the district. Administrative costs are paid by the CIP. At June 30, 2025, the 
College’s policy was not required to subsidize health insurance premiums of their retirees. 
Employers participating in a cost-sharing OPEB plan, and any non-employer contributing entities that 
meet the definition of a special funding situation, are required to recognize their proportionate share of the 
collective OPEBs amounts for the OPEB benefits provided to members through the CIP plan. During 
fiscal year 2025, the College recognized OPEB contributions of $169,688. 
33
<PARSED TEXT FOR PAGE: 47 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 9: POSTEMPLOYMENT BENEFITS OTHER THAN PENSIONS (CONTINUED)
A. State of Illinois’ College Insurance Program (Continued)
OPEB Liabilities, OPEB Expense, and Deferred Outflows of Resources and Deferred Inflows of 
Resources Related to OPEB
The collective net OPEB liability was measured as of June 30, 2024. At June 30, 2024, the CIP reported 
a net OPEB liability of $665,190,300.
At June 30, 2024, the College reported a liability for its proportionate share of the net OPEB liability that 
is reflected as a reduction for State OPEB support provided to the College. The collective net OPEB 
liability was measured as of June 30, 2024, and the total OPEB liability used to calculate the collective 
net OPEB liability was determined by an actuarial valuation as of that date. The College’s proportion of 
the collective net OPEB liability was based on a projection of the College’s long-term share of 
contributions to the OPEB plan relative to the projected contributions of the College, actuarially 
determined. At June 30, 2024, the College’s proportion was $6,034,549 (0.907%), which was a decrease 
of 0.050% from its proportion measured as of June 30, 2023 of $6,758,784 (0.957%). The State’s support 
and total are for disclosure purposes only. The amount recognized by the College as its proportionate 
share of the net OPEB liability, the related State support, and the total portion of the net OPEB liability 
that was associated with the College were as follow:
College’s proportionate share of the collective net OPEB liability $ 6,034,549
State’s proportionate share of the collective net OPEB liability 
 associated with the employer 6,034,549
$ 12,069,098
For the year ending June 30, 2025, the College recognized OPEB revenue and expense of ($2,287,489)
for support provided on-behalf by the State. At June 30, 2025, the College reported deferred outflows of 
resources and deferred inflows of resources related to OPEB from the following sources:
Deferred Outflows 
of Resources
Deferred Inflows 
of Resources
Difference between expected and actual experience $ 76,503 $ (1,818,180)
Changes in assumptions 44,623 (4,384,465) 
Net difference between projected and actual 
 earnings on OPEB plan investments - (2,992)
Changes in proportion and differences between 
 employer contributions and proportionate share of 
 contributions 156,149 (1,269,591)
 Total deferred amounts to be recognized in
 expense in future periods 277,275 (7,475,228)
Employer contributions subsequent to the 
 measurement date 169,688 -
 Total $ 446,963 $ (7,475,228)
34
<PARSED TEXT FOR PAGE: 48 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 9: POSTEMPLOYMENT BENEFITS OTHER THAN PENSIONS (CONTINUED)
A. State of Illinois’ College Insurance Program (Continued)
OPEB Liabilities, OPEB Expense, and Deferred Outflows of Resources and Deferred Inflows of 
Resources Related to OPEB (Concluded)
The College reported $169,688 as deferred outflows of resources related to OPEB resulting from College 
contributions subsequent to the measurement date that will be recognized as a reduction of the net OPEB 
liability for the measurement period ended June 30, 2025. Other amounts reported as deferred outflows 
of resources and deferred inflows of resources related to CIP will be recognized in OPEB expense as 
follows:
Years ending June 30,
Net Deferred 
Outflows (Inflows) 
of Resources
2025 $ (3,797,822)
2026 (2,746,117)
2027 (709,033)
2028 37,642
2029 17,377
Total $ (7,197,953)
Actuarial Assumptions
The total OPEB liability was determined by an actuarial valuation as of June 30, 2023, using the 
following actuarial assumptions, applied to all periods included in the measurement date, unless otherwise 
specified:
Inflation 2.25%
Salary increases Depends on age and service and ranges from 12.75% at less than 1 
year of service to 3.50% at 34 or more years of service for 
employees under 50 and ranges from 12.00% at less than one 1 year 
of service to 3.00% at 34 or more years of service for employees 
over 50. Salary increase includes a 3.00% wage inflation 
assumption.
Investment rate of return 0%, net of OPEB plan investment expense, including inflation, for 
all plan years.
Healthcare cost trend rates Trend rates for plan year 2025 are based on actual premium 
increases. For non-Medicare costs, trend rates start at 8.00% for plan 
year 2026 and decrease gradually to an ultimate rate of 4.25% in 
2041. For MAPD costs, trend rates are based on actual premium 
increases for 2025, 15.00% in 2026 to 2030, and 7.00% in 2013, 
declining gradually to an ultimate rate of 4.25% in 2041.
35
<PARSED TEXT FOR PAGE: 49 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 9: POSTEMPLOYMENT BENEFITS OTHER THAN PENSIONS (CONTINUED)
A. State of Illinois’ College Insurance Program (Continued)
Actuarial Assumptions (Concluded)
Mortality rates for retirement and beneficiary annuitants were based on the Pub-2010 Healthy Retiree 
Mortality Table and PubT-2010 Healthy Retiree Mortality Table. For disabled annuitants, mortality rates 
were based on the Pub-2010 Disabled Retiree Mortality Table. Mortality rates for pre-retirement 
annuitants were based on the Pub-2010 Employee Mortality Table and PubT-2010 Employee Mortality 
Table. Tables are adjusted for SURS experience. All tables reflect future mortality improvements using 
Projection Scale MP-2020.
The actuarial assumptions used in the June 30, 2023 valuation were based on the results of an actuarial 
experience study for the period June 30, 2017 to June 30, 2020.
Projected benefit payments were discounted to their actuarial present values using a Single Discount Rate 
that reflects (1) a long-term expected rate of return on OPEB plan investments (to the extent that the 
plan’s fiduciary net position is projected to be sufficient to pay benefits), and (2) tax-exempt municipal 
bond rate based on an index of 20-year general obligation bonds with an average AA credit rating as of 
the measurement date (to the extent that the contributions for use with the long-term expected rate of 
return are not met). Since the CIP fund is financed on a pay-as-you-go basis, a discount rate consistent 
with fixed income municipal bonds with 20 years to maturity that include only federally tax-exempt
municipal bonds as reported in Fidelity’s index’s “20-year Municipal GO AA Index” has been selected. 
The discount rates are 3.97% as of June 30, 2024, and 3.86% as of June 30, 2023. The increase in the 
single discount rate from 3.86% to 3.97% caused the trust’s total OPEB liability to decrease by 
approximately $6.3 million from 2023 to 2024.
The actuarial valuation was based on the Entry Age Normal cost method. Under this method, the normal 
cost and actuarial accrued liability are directly proportional to the employee’s salary. The normal cost 
rate equals the present value of future benefits at entry age divided by the present value of the future 
salary at entry age. The normal cost at the member’s attained age equals the normal cost rate at entry age 
multiplied by the salary at attained age. The actuarial accrued liability equals the present value of the 
benefits at attained age less present value of future salaries at attained age multiplied by normal cost rate 
at entry age. 
During the plan year ending June 30, 2024, the trust earned $277,000 in interest and due to a significant 
benefit payable, the market value of assets at June 30, 2024, is a negative $103.6 million. Given the 
significant benefit payable, negative asset value and pay-as-you-go funding policy, the long-term 
expected rate of return assumptions was set to zero.
36
<PARSED TEXT FOR PAGE: 50 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 9: POSTEMPLOYMENT BENEFITS OTHER THAN PENSIONS (CONTINUED)
A. State of Illinois’ College Insurance Program (Continued)
Sensitivity of the Employer’s Proportionate Share of the Collective Net OPEB Liability to Changes in the 
Single Discount Rate 
The following table presents the College’s proportionate share of the collective net OPEB liability as of 
June 30, 2024, calculated using a single discount rate of 3.97% as well as what the College’s 
proportionate share of the collective net OPEB liability would be if it were calculated using a discount 
rate that is 1-percentage-point lower (2.97%) or 1-percentage-point higher (4.97%) than the current 
discount rate:
1% Decrease
2.97%
Current Discount Rate 
3.97%
1% Increase
4.97%
Employer’s proportionate share of
 the collective net OPEB liability $ 6,592,894 $ 6,034,549 $ 5,556,640
Sensitivity of the Employer’s Proportionate Share of the Collective Net OPEB Liability to Changes in the 
Healthcare Cost Trend Rates
The following table presents the College’s collective net OPEB liability as of June 30, 2024, calculated 
using the healthcare cost trend rates as well as what the College’s OPEB liability would be if it were 
calculated using a healthcare cost trend rate that is 1-percentage-point higher or lower, than the current 
healthcare cost trend rates. The key trend rates are 15.00% in 2026 decreasing to an ultimate trend rate of 
4.25% in 2041:
1% Decrease (a)
Healthcare Cost
Trend Rates
Assumptions
1% Increase (b)
Employer’s proportionate share of
 the collective net OPEB liability $ 5,422,063 $ 6,034,549 $ 6,776,657
(a) One percentage point decrease in current healthcare trend rates - Pre-Medicare per capita costs: 8.02% in 2025, 7.00% in 
2026, decreasing by 0.25% per year to an ultimate rate of 3.25% in 2041. Post-Medicare per capital costs: based on actual 
increase in 2025, 14.00% from 2026 to 2030, 6.00% in 2031 decreasing ratably to an ultimate trend rate of 3.25% in 2041.
(b) One percentage point increase in current healthcare trend rates - Pre-Medicare per capita costs: 10.02% in 2025, 9.00% in 
2026, decreasing by 0.25% per year to an ultimate rate of 5.25% in 2041. Post-Medicare per capital costs: based on actual 
increase in 2025, 16.00% from 2026 to 2030, 8.00% in 2031 decreasing ratably to an ultimate trend rate of 5.25% in 2041. 
Payable to the OPEB Plan
The College had no outstanding contributions payable to the CIP plan for the year ended June 30, 2025.
37
<PARSED TEXT FOR PAGE: 51 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 9: POSTEMPLOYMENT BENEFITS OTHER THAN PENSIONS (CONTINUED)
A. State of Illinois’ College Insurance Program (Concluded)
Request for information
The State of Illinois’ Comprehensive Annual Financial Report may be obtained by writing to the State 
Comptroller’s office, Division of Financial Reporting, 325 West Adams Street, Springfield, Illinois, 
62704-1871.
B. John A. Logan College Single Employer Defined Benefit Postemployment Benefit Healthcare Plan
Retirees’ Health Insurance Reimbursement
In addition to the pension benefits described in Note 8, the College provides a subsidy to eligible retirees 
to bring their cost of health insurance to current active employee levels. Eligibility is based on board 
policy or the applicable union contract, depending on the employee group. At the death of a retired 
employee, coverage will be extended to the spouse if previously covered. Retirees from the College will
qualify for health insurance coverage under the College Insurance Program (Plan) offered through the 
State office of Central Management Services. Qualifying individuals receive reimbursement of varying 
amounts from the College in order to keep retirees’ net contributions equal to the contribution of a current 
active employee with similar coverage. The College finances the Plan on a pay-as-you go basis.
Employees Covered by the Benefit Term
As of June 30, 2025, the following employees were covered by the benefit term:
Active employees 82
Inactive employees entitled to but not receiving benefits -
Inactive employees currently receiving benefits 94
 Total 176
Total OPEB Liability
The College’s total OPEB liability of $5,810,894 was measured as of June 30, 2025 and was determined 
by an actuarial valuation as of June 30, 2024, rolled forward to June 30, 2025.
38
<PARSED TEXT FOR PAGE: 52 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 9: POSTEMPLOYMENT BENEFITS OTHER THAN PENSIONS (CONTINUED)
B. John A. Logan College Single Employer Defined Benefit Postemployment Benefit Healthcare Plan 
(Continued)
Actuarial Assumptions
The total OPEB liability in the June 30, 2025 actuarial valuation was determined using the following 
actuarial assumptions and other inputs, applied to all periods included in the measurement, unless 
otherwise specified:
Inflation 3.00%
Salary rate increase 4.00%
Discount rate 4.81% 
Healthcare cost trend rates 6.36%, managed care option, 6.36% CCHP option for 
2025 decreasing to an ultimate rate of 4.50% for 2039
and later years
Retirees’ share of benefit-related costs Same as healthcare trend
Since the Plan is financed on a pay-as-you-go basis, a long-term rate of return was not used, and the 
discount rate used to measure the total OPEB liability was a 20-year tax-exempt general obligation 
municipal bond index rate. The discount rate was based on the S&P Municipal Bond 20-Year High-Grade 
Rate Index as of June 30, 2025. The discount rate as of June 30, 2025 was 4.81%, which was an increase 
from the June 30, 2024 rate of 4.21%.
Mortality rates were based on the PubT.H-2010 Mortality Table for males and females, as appropriate.
Changes in the Total OPEB Liability
Balance as of June 30, 2024 $ 6,345,001
Changes for the year:
 Service cost 14,191
 Interest 259,606
 Changes of benefit terms -
 Difference between expected and actual experience -
 Changes in assumptions and other inputs (450,718)
 Benefit payments (357,186)
 Other changes -
 Net changes (534,107)
Balance as of June 30, 2025 $ 5,810,894
39
<PARSED TEXT FOR PAGE: 53 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 9: POSTEMPLOYMENT BENEFITS OTHER THAN PENSIONS (CONTINUED)
B. John A. Logan College Single Employer Defined Benefit Postemployment Benefit Healthcare Plan 
(Continued)
Sensitivity of the Total OPEB Liability to Changes in the Discount Rate and Healthcare Cost Trend Rates
The following is a sensitivity analysis of the OPEB liability to changes in the discount rate and the 
healthcare cost trend rates. 
The table below presents the OPEB liability of the College calculated using a discount rate of 4.81% as 
well as what the College’s OPEB liability would be if it were calculated using a discount rate that is 1-
percentage-point lower (3.81%) or 1-percentage-point higher (5.81%) than the current rate:
1% Decrease
3.81%
Current 
Discount Rate 
4.81%
1% Increase
5.81%
Employer’s proportionate share of
 the collective net OPEB liability $ 6,540,854 $ 5,810,894 $ 5,211,097
The table below presents the College’s OPEB liability, calculated using the healthcare cost trend rates as 
well as what the College’s OPEB liability would be it if were calculated using a healthcare cost trend rate 
that is 1-percentage-point higher or lower, than the current healthcare cost trend rates. The key trend rates 
are 6.36%, managed care option, and 6.36%, CCHP option, decreasing to an ultimate trend rate of 4.50% 
in 2039:
1% Decrease (a)
Healthcare Cost
Trend Rates
Assumptions 1% Increase (b)
Employer’s proportionate share of
 the collective net OPEB liability $ 5,201,015 $ 5,810,894 6,542,995
(a) One percentage point decrease in healthcare trend rates is 5.36%, managed care option, and 5.36%, CCHP option, in 2025
decreasing to an ultimate trend rate of 3.50% in 2039.
(b) One percentage point increase in healthcare trend rates is 7.36%, managed care option, and 7.36%, CCHP option, in 2025
decreasing to an ultimate trend rate of 5.50% in 2039.
40
<PARSED TEXT FOR PAGE: 54 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 9: POSTEMPLOYMENT BENEFITS OTHER THAN PENSIONS (CONCLUDED)
B. John A. Logan College Single Employer Defined Benefit Postemployment Benefit Healthcare Plan 
(Concluded)
OPEB Expense, Deferred Outflows of Resources, and Deferred Inflows of Resources Related to OPEB
For the year ended June 30, 2025, the College recognized OPEB expense of $618,978. At June 30, 2025, 
the College reported deferred outflows of resources and deferred inflows of resources related to OPEB 
from the following sources:
Deferred Outflows 
of Resources
Deferred Inflows 
of Resources
Difference between expected and actual experience $ 95,757 $ -
Changes in assumptions 173,765 (275,796) 
Net difference between projected and actual 
 earnings on OPEB plan investments - -
Total deferred amounts to be recognized in
 expense in future periods $
 
269,522 $ (275,796)
Amounts reported as deferred outflows of resources and deferred inflows of resources related to OPEB 
will be recognized in OPEB expense as follows:
Net Deferred 
Outflows (Inflows) 
of Resources
Years ending June 30,
2026 $ 67,032
2027 (73,306)
Total $ (6,274)
NOTE 10: INTERGOVERNMENTAL AGREEMENT
In September 2017, the College entered into an educational partnership agreement (Community College 
Education Agreement) with 36 other Illinois community colleges to provide additional educational 
programs to the citizens of each district. The cooperating institutions in this agreement will be treated as 
in district in relation to admission policies for their programs. Colleges sending students to any receiving 
cooperating institution will no longer pay chargebacks to the receiving college.
41
<PARSED TEXT FOR PAGE: 55 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 11: LEASES
The College is the lessee in a lease agreement with the following terms:
Operating Lease – On September 27, 2022, the College entered into an operating lease with Konica 
Minolta for copiers. The lease term is 60 months, the interest rate is 4.70%, and the monthly lease 
payment is $3,955. The leased equipment and accumulated amortization of the right-to-use assets are 
outlined in Note 3 and below. 
Balance Balance
July 1, 2024 Additions Deletions June 30, 2025
Copier Lease $ 211,084 $ - $ - $ 211,084
Less: Accumulated Amortization (68,319) (41,633) - (109,952)
 Right-of-Use Assets, Net $ 142,765 $ (41,633) $ - $ 101,132
The following is a maturity analysis of annual undiscounted cash flows for lease liabilities as of June 30, 
2025:
Year Ending June 30, Principal Interest Total
 2026 $ 47,362 $ 3,821 $ 51,183
 2027 41,999 1,726 43,725
 2028 11,771 92 11,863
$ 101,132 $ 5,639 $ 106,771
NOTE 12: SUBSCRIPTION-BASED INFORMATION TECHNOLOGY ARRANGEMENTS
The College has entered into seven qualifying subscription-based technology agreements (SBITAs) 
involving:
• Cybersecurity software, 
• Enterprise resource planning software,
• Fitness center management software,
• Budgeting software, 
• Disaster recovery and risk management software, and
• Learning management software.
42
<PARSED TEXT FOR PAGE: 56 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 12: SUBSCRIPTION-BASED INFORMATION TECHNOLOGY ARRANGEMENTS
(CONCLUDED)
Balance Balance
July 1, 2024 Additions Deletions June 30, 2025
SBITAs $ 539,805 $ 2,155,270 $ - $ 2,695,075
Less: Accumulated Amortization (145,383) (676,090) - (821,473)
 Right-of-Use Assets, Net $ 394,422 $ 1,479,180 $ - $ 1,873,602
The future subscription payments under SBITA arrangements are as follows:
Year Ending June 30, Principal Interest Total
 2026 $ 574,430 $ 99,247 $ 673,677
 2027 531,396 67,515 598,911
 2028 346,801 39,977 386,778
 2029 385,087 21,034 406,121
$ 1,837,714 $ 227,773 $ 2,065,487
NOTE 13: PEPSI AGREEMENT
On October 23, 2018, the College entered into an agreement with Pepsi MidAmerica Co. (Pepsi) in which
Pepsi will be the exclusive beverage and line snack provider for a period of 20 years. In accordance with 
the agreement, Pepsi made an upfront payment to the College for $130,000 for the first two years of the 
agreement. Pepsi will then make payments of $65,000 per year for years 3-20 of the agreement. The 
total monetary payments over the contract will be $1,300,000. During the year ended June 30, 2025, the 
College recognized $65,000 as revenue, accounts receivable of $845,000, and $845,000 as a deferred 
inflow of resources related to this contract.
NOTE 14: RELATED PARTIES
For the year ended June 30, 2025, there were no related party transactions. 
NOTE 15: CONTINGENT LIABILITIES AND COMMITMENTS
Federal and State Grants
The College has received a number of Federal and State grants from specific purposes which are subject 
to review and audit by grantor agencies. Such audits may result in requests for reimbursement to granting 
agencies for expenditures disallowed under the terms of the grants. Based on prior experience, College 
management believes that such disallowances, if any, will not be material.
Compensated Absences – Vacation and Sick Leave
As of June 30, 2025, employees had earned but not taken vacation and sick leave, which at salary rates in 
effect at the end of the year, totaled $3,679,246. The College has accrued this liability and considers 
$1,019,366 of the liability to be payable within one year. The remaining liability of $2,659,880 is 
considered to be long-term.
43
<PARSED TEXT FOR PAGE: 57 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 15: CONTINGENT LIABILITIES AND COMMITMENTS (CONCLUDED)
Construction in Progress
At June 30, 2025, the College had construction project commitments totaling approximately $34,460,000. 
These commitment totals include the grant funded portions, as applicable, and are detailed below:
Approved prior to June 30, 2025:
 Career and Technical Center Project $ 14,702,000
 West lobby expansion 8,346,000
 G wing labs first floor moisture mitigation 3,404,000
 B wing 3rd floor nursing renovation 1,835,000
 G building chiller replacement 1,218,000
 Communications cooling tower replacement 1,065,000
 F wing roof replacement 795,000
 C and E wing renovations and upper C wing HVAC upgrades 663,000
 D wing roof replacement 491,000
 Boiler replacement 418,000
 Elevator 412,000
 Julia Harrison-Bruce Prairie Museum 400,000
 Harrison Bruce Player Development Center 400,000
 Highway construction careers program building – Phase 1 192,000
 H building main breaker replacement 50,000
 F wing building envelope project 48,000
 Fitness Center exercise room renovation 21,000
Total construction commitments $ 34,460,000
NOTE 16: RESTATEMENT
During the year ended June 30, 2025, the College implemented GASB Statement No. 101 – Compensated 
Absences. This implementation resulted in recalculation of the College’s liabilities for compensated 
absences. The effects of this change in accounting principle are detailed below:
Government-wide – Business-type Activities
 Net Position – July 1, 2024, as previously reported $ 58,723,952
 Restatement – GASB 101 implementation (1,967,334)
 Net Position – July 1, 2024, as restated $ 56,756,618
NOTE 17: SUBSEQUENT EVENTS
On October 20, 2025, the College issued $6,740,000 in General Obligation Community College Bonds 
with an interest rate of 5.00%. The bonds mature on December 1, 2035. The net proceeds of $7,001,383 
(after reoffering premium of $625,385, issuance costs of $157,121, and capitalized interest of $206,881) 
were used to increase the College’s Working Cash Fund which was abated in November 2025. The funds 
will be used for the purpose of improving District facilities. 
44
<PARSED TEXT FOR PAGE: 58 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 17: SUBSEQUENT EVENTS (CONCLUDED)
On January 26, 2026, the College issued $3,030,000 in Taxable General Obligation Debt Certificates 
(Limited Tax), Series 2026A and $17,150,000 in General Obligation Debt Certificates (Limited Tax), 
Series 2026B with interest rates ranging from 4.95% - 6.50% and 3.50% - 5.00%, respectively. These 
debt certificates mature June 1, 2031 and June 1, 2026, respectively. The net proceeds of $3,000,107
(after issuance costs of $29,893) and $17,004,239 (after issuance costs of $145,761) will be used to pay 
the cost of improving District facilities. The College intends to issue refunding bonds to repay these debt 
certificates in April 2026. 
NOTE 18: DISCRETELY PRESENTED COMPONENT UNIT
The Foundation’s notes to the financial statements are as follows:
A. Summary of Significant Accounting Policies
John A. Logan College Foundation (the Foundation) is organized exclusively for educational and 
charitable purposes. The Foundation provides financial support to the educational programs and services 
at John A. Logan College (the College) to assist in increasing and enhancing the physical and cultural 
environment of the College; to broaden the educational opportunities and services for its students, alumni, 
and citizens of the District; and to provide funds to implement scholarships and various awards. 
Basis of Accounting – The financial statements of the Foundation have been prepared on the accrual basis 
of accounting in accordance with U.S. generally accepted accounting principles (GAAP) and, 
accordingly, reflect all significant receivables, payables, and other liabilities. The Foundation has 
presented its assets and liabilities on its Statement of Financial Position in an unclassified manner, but in 
order of liquidity.
Basis of Presentation – The Foundation classifies its net assets, revenues, gains, and other support on the 
existence or absence of donor or grantor imposed restrictions. Accordingly, net assets and changes therein 
are classified and reported as follows:
Net Assets Without Donor Restrictions – Net assets available for use in general operations and not 
subject to donor (or certain grantor) restrictions. The governing board has designated, from net 
assets without donor restrictions, net assets for various purposes, including quasi-endowments. 
Net Assets With Donor Restrictions – Net assets subject to donor (or certain grantor) imposed 
restrictions. Some donor-imposed restrictions are temporary in nature, such as those that will be 
met by the passage of time or other events specified by the donor. Other donor-imposed 
restrictions are perpetual in nature, where the donor stipulates that resources be maintained in 
perpetuity. Donor-imposed restrictions are released when a restriction expires, that is, when the 
stipulated time has elapsed, when the stipulated purpose for which the resource was restricted has 
been fulfilled, or both.
45
<PARSED TEXT FOR PAGE: 59 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 18: DISCRETELY PRESENTED COMPONENT UNIT (CONTINUED)
A. Summary of Significant Accounting Policies (Continued)
Cash Equivalents – For the purpose of the Statement of Cash Flows, cash equivalents consist of highly￾liquid short-term investments including money market account deposits with original maturity of three 
months or less from the date of purchase. 
Contributions of Financial Assets – Contributions of financial assets, including unconditional pledges, are 
recognized in the appropriate category of net assets in the period received. The Foundation evaluates 
contributions for criteria indicating the existence of measurable barriers to entitlement for the contribution 
and the right of return to the donor. When a barrier to entitlement exists, the contribution is treated as a 
conditional contribution. If both the barrier to entitlement and right of return do not exist, the 
contribution is unconditional. Conditional pledges are not recognized until the conditions on which they 
depend are substantially met. Contributions of financial assets other than cash are recorded at estimated 
fair value. Contributions to be received after one year are discounted and recorded at the present value 
using a risk-adjusted rate of return. Amortization of the discount is recorded as additional contribution 
revenue in accordance with donor-imposed restrictions, if any, on the contributions. There were no 
contributions to be received after one year at June 30, 2025 or 2024. An allowance for uncollectible 
pledges is recognized based on historical experience, as necessary. No allowance for uncollectible 
pledges was recognized for the year ended June 30, 2025 or 2024.
Contributions of financial assets received in the same year in which the restriction is met are recorded as 
contributions with donor restrictions and released from restriction.
Contributions of Nonfinancial Assets – Contributions of nonfinancial assets are provided to the 
Foundation by the College and include office space, accounting and record-keeping services, and 
necessary administrative services. The rental value of the office space is recorded at fair rental value 
equivalent to similar facility space. Other amounts have been recorded based on actual cost to the College 
for the services. The services would typically need to be purchased if not provided by donation by the 
College. See Note 16F below. 
Investments – Investments are reported at fair value. Investment income, gains and losses, and any 
investment-related expenses are recorded as changes in net assets without donor restrictions in the 
Statement of Activities unless their use is temporarily or permanently restricted by explicit donor 
stipulations or laws. In the absence of donor stipulations or law to the contrary, losses on the investments 
of donor-restricted endowment funds are recognized as reductions of net assets with donor restrictions to 
the extent that donor-imposed restrictions on net appreciation of the funds have not been met before the 
loss occurs. Any remaining loss reduces net assets without donor restrictions. 
Investment Expenses – Investment expenses, including custodial fees and investment advisory fees, 
relating to investment income amounted to $47,602 and have been netted with investment income in the 
accompanying Statement of Activities. 
46
<PARSED TEXT FOR PAGE: 60 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 18: DISCRETELY PRESENTED COMPONENT UNIT (CONTINUED)
A. Summary of Significant Accounting Policies (Continued)
Fair Value – The Foundation follows FASB ASC 820-10 "Fair Value Measurements," which provides a 
framework for measuring fair value under U.S. generally accepted accounting principles. FASB ASC 
820-10 defines fair value as the exchange price that would be received for an asset or paid to transfer a 
liability in an orderly transaction between market participants on the measurement date. FASB ASC 820-
10 requires that valuation techniques maximize the use of observable inputs and minimize the use of 
unobservable inputs. FASB ASC 820-10 also establishes a fair value hierarchy, which prioritizes the 
valuation inputs into three broad levels as described below.
Level 1: Inputs to the valuation methodology derived from unadjusted quoted prices for identical 
assets or liabilities in active markets. 
Level 2: Other observable inputs including quoted prices for similar assets or liabilities in active 
or inactive markets, and inputs that are principally derived from or corroborated by observable 
market data by correlation or other means. 
Level 3: Inputs to the valuation methodology which are unobservable and significant to the fair 
value measurements. These inputs are only used when Level 1 or Level 2 inputs are not available.
Income Taxes – The Foundation is recognized as exempt from federal income taxes under section 
501(c)(3) of the Internal Revenue Code. The Foundation may be subject to federal and state income taxes 
on any net income from unrelated business activities. The Foundation files a form 990 (Return of 
Organization Exempt from Income Tax) annually, and unrelated business income (UBI) is reported on 
Form 990-T, as appropriate. Management has evaluated the Foundation’s material tax positions, which 
include such matters as the tax-exempt status of each entity and various positions relative to potential 
sources of UBI. As of June 30, 2025, there were no uncertain tax benefits identified and recorded as a 
liability. The Foundation is no longer subject to U.S. federal or state income tax authorities for the years 
ending prior to June 30, 2022.
Use of Estimates – The preparation of financial statements in conformity with United States generally 
accepted accounting principles requires the use of management’s estimates and assumptions that affect 
the reported amount of assets and liabilities at the date of the financial statements and the reported amount 
of revenues and expenses during the reporting period. Accordingly, actual results may differ from those 
estimates.
47
<PARSED TEXT FOR PAGE: 61 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 18: DISCRETELY PRESENTED COMPONENT UNIT (CONTINUED)
A. Summary of Significant Accounting Policies (Concluded)
Functional Allocation of Expenses – The costs of providing various programs and other activities have 
been summarized on a functional basis in the Statements of Activities. The Statement of Functional 
Expenses presents the natural classification detail of expenses by function. Accordingly, certain costs 
have been allocated among the programs and supporting services benefited. This presentation requires 
allocation of expenses on a reasonable basis that is consistently applied. Expenses are allocated based on 
the Foundation’s best estimate of the time spent by employees on program services vs. supporting 
services functions. Directly identifiable expenses are charged to the appropriate program or supporting 
service. Management and general expenses include those expenses that are not directly identifiable with 
any other specific function but provide the overall support and direction of the Foundation. 
Date of Management’s Review – Management has reviewed subsequent events through February 19, 
2026, the date the financial statements were available to be issued. 
B. Investments and Fair Value Measurements
The Foundation’s investments are held by the trust and custody division of a national bank and managed 
by an investment advisor in accordance with the terms of an investment advisor agreement. Investments 
detailed below were measured at fair value as described in Note 15A.
Investments as of June 30, 2025 consisted of the following:
Fair Value
Quoted Significant
Active Markets Other
for Identical Observable
Assets Inputs
Cost (Level 1) (Level 2) Total
Mutual Funds
 Equity $ 519,573 $ 579,650 $ - $ 579,650
 Fixed Income 2,903,492 2,700,283 - 2,700,283
 Exchange-traded Funds 3,769,410 4,631,076 - 4,631,076
Corporate Stock 1,898,559 3,187,702 - 3,187,702
Certificates of Deposit 199,800 - 201,744 201,744
Total Investments $ 9,290,834 $ 11,098,711 $ 201,744 $ 11,300,455
There were no transfers between Levels 1, 2, or 3 of the fair value hierarchy during the year ended 
June 30, 2025.
C. Net Assets with Donor Restrictions
The Foundation reports gifts of cash and other assets as restricted if they are received with donor 
stipulations that limit the use of the donated assets. When donor restrictions expire, net assets with donor 
restrictions are reclassified to net assets without donor restrictions and reported in the Statement of 
Activities as net assets released from restrictions.
48
<PARSED TEXT FOR PAGE: 62 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 18: DISCRETELY PRESENTED COMPONENT UNIT (CONTINUED)
C. Net Assets with Donor Restrictions (Concluded)
The Foundation reports gifts of cash and other assets as restricted if they are received with donor 
stipulations that limit the use of the donated assets. When donor restrictions expire, net assets with donor 
restrictions are reclassified to net assets without donor restrictions and reported in the Statement of 
Activities as net assets released from restrictions.
At June 30, 2025, the Foundation held $9,920,603 in net assets with donor restrictions. These assets will 
be used for scholarships for students of the College as well as grants benefiting the College in amounts as 
follows:
Scholarships
 Endowment $ 8,310,596
 Non-endowed 648,437
Athletics
Endowment 205,796
Non-endowed 313,647
Other
Endowment 170,222
Non-endowed 271,905
Total $ 9,920,603
During the year ended June 30, 2025, $1,219,128 was released from restrictions and used for the 
following purposes:
Scholarships $ 758,778
Athletics 331,897
Fundraising 21,035
Other Student Support 107,127
Management & General 291
Total $ 1,219,128
D. Endowment Funds
The Foundation’s endowment consists of funds established for a variety of purposes. Its endowment 
includes both donor-restricted funds and funds designated by the Board of Directors to function as 
endowments. As required by generally accepted accounting principles, net assets associated with 
endowment funds, including funds designated by the Board of Directors to function as endowments, are 
classified and reported based on the existence or absence of donor-imposed restrictions. 
Interpretation of Relevant Law: The Board of Directors of the Organization, through obtaining a legal 
opinion and committee review, has interpreted the Uniform Prudent Management of Institutional Funds 
Act (UPMIFA) as requiring the preservation of the fair value of the original gift as of the gift date of the 
donor-restricted endowment funds absent explicit donor stipulations to the contrary. As a result of this
49
<PARSED TEXT FOR PAGE: 63 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 18: DISCRETELY PRESENTED COMPONENT UNIT (CONTINUED)
D. Endowment Funds (Continued)
interpretation, the Foundation classifies as net assets with donor restrictions to be held in perpetuity (a)
the original value of gifts donated to the permanent endowment, (b) the original value of subsequent gifts 
to the permanent endowment, and (c) accumulations to the permanent endowment made in accordance 
with the direction of the applicable donor gift instrument at the time the accumulation is added to the
fund. The remaining portion of the donor-restricted endowment fund that is not considered to be held in 
perpetuity, is also classified as net assets with donor restrictions until those amounts are appropriated for
expenditure by the Foundation in a manner consistent with the standard of prudence prescribed by 
UPMIFA. In accordance with UPMIFA, the Foundation considers the following factors in making a 
determination to appropriate or accumulate donor-restricted endowment funds: 
1. The duration and preservation of the funds;
2. The purposes of the Foundation and the donor-restricted endowment fund;
3. General economic conditions;
4. The possible effect of inflation and deflation;
5. The expected total return from income and the appreciation of investments;
6. Other resources of the Foundation; and 
7. The Foundation’s investment policies. 
Spending Policy. The Foundation has a policy in which any accumulated earnings in excess of a 
calculated reserve are available for distribution each year. In establishing this policy, the Foundation 
considered the long-term expected return on its investment assets, the nature and duration of the 
individual endowment funds, many of which must be maintained in perpetuity because of donor￾restrictions, and the possible effects of inflation. The Foundation expects the current spending policy to 
allow its endowment funds to grow at a nominal average rate of 4% annually. This is consistent with the 
Foundation’s objective to maintain the purchasing power of the endowment assets as well as to provide 
additional real growth through new gifts and investment return. The Board-approved spending was 
$485,164 for the fiscal year ended June 30, 2025.
Investment Return Objectives, Risk Parameters and Strategies. The Foundation has adopted investment 
and spending policies, approved by the Board of Directors, for endowment assets that attempt to provide a 
predictable stream of funding to programs supported by its endowment funds while also maintaining the 
purchasing power of those endowment assets over the long-term. Accordingly, the investment process 
seeks to achieve an after-cost total real rate of return, including investment income as well as capital 
appreciation, which exceeds the annual distribution with acceptable levels of risk. Endowment assets are 
invested in a well-diversified asset mix, which includes equity and debt securities, that is intended to 
preserve and increase the real principal value of the fund over the long-term. The investment objective is 
to earn an average annual rate of return over a 10-15 year period which exceeds the average annual 
change in the Consumer Price Index by 4%. Actual returns in any given year may vary from this amount. 
Investment risk is measured in terms of the total endowment fund; investment assets and allocation 
between asset classes and strategies are managed to not expose the fund to unacceptable levels of risk. 
50
<PARSED TEXT FOR PAGE: 64 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONTINUED)
JUNE 30, 2025
NOTE 18: DISCRETELY PRESENTED COMPONENT UNIT (CONTINUED)
D. Endowment Funds (Concluded)
Endowment net assets as June 30, 2025 are as follows:
Total 
Without Donor With Donor Endowment
Restrictions Restrictions Net Assets
Donor-restricted Endowment Funds $ - $ 8,686,614 $ 8,686,614
Board-designated Endowment Funds 1,714,683 - 1,714,683
$ 1,714,683 $ 8,686,614 $ 10,401,297
Changes in endowment net assets as of June 30, 2025 are as follows:
Total
Without Donor With Donor Endowment
Restrictions Restrictions Net Assets
Endowment Net Assets, Beginning of Year $ 1,658,723 $ 8,062,362 $ 9,721,085
Contributions - 80,000 80,000
Investment Income, Net of Fees 56,752 273,018 329,770
Realized Net Gain (Loss) (3,436) (16,108) (19,544)
Unrealized Net Gain (Loss) 135,506 639,644 775,150
Amounts Appropriated for Expenditures (132,862) (352,302) (485,164)
Endowment Net Assets, End of Year $ 1,714,683 $ 8,686,614 $ 10,401,297
E. Liquidity and Availability
The Foundation’s financial assets available for general expenditures, that is, without donor restrictions or 
other limitations, such as Board designations, within one year of the Statement of Net Position date, 
comprise the following:
Cash and Cash Equivalents $ 583,538
Investments 11,300,455
Contributions Receivable 1,728
Less: Amount Designated or Restricted for Specific Purposes (11,376,518)
Total $ 509,203
The Foundation’s endowment funds consist of donor-restricted endowments and funds designated by the 
board as endowments. Income from donor-restricted endowments is restricted for specific purposes, with 
the exception of the amounts available for general use. Donor-restricted endowment funds are not 
available for general expenditures.
Board-designated endowments of $1,228,719 are reserved for special purposes. Most of these board￾designated endowments are subject to annual spending limit as described in Note 18D. Although the 
Foundation does not intend to spend from the board-designated endowments (other than amounts 
appropriated for general expenditures as part of the Board’s annual approved budget), these amounts 
could be made available if necessary. 
51
<PARSED TEXT FOR PAGE: 65 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO FINANCIAL STATEMENTS (CONCLUDED)
JUNE 30, 2025
NOTE 18: DISCRETELY PRESENTED COMPONENT UNIT (CONCLUDED)
E. Liquidity and Availability (Concluded)
As part of the Foundation’s liquidity management plan, cash in excess of the Foundation’s daily 
requirements are invested in short-term investments, certificates of deposit, and money market funds as 
determined by the Foundation’s investment committee. 
F. Relationship to John A. Logan College and Related Transactions
As part of the Foundation efforts, donations are accepted for the purchase of equipment to be used at the 
College or to fund construction projects as the College. The College makes the initial purchase and 
submits invoices to the Foundation for reimbursement. The amounts reimbursed to the College are 
expensed as title to the assets remains with the College. 
The College furnishes the Foundation with certain services and facilities at no charge. The total value of 
the services and facilities provided by the College during the year ended June 30, 2025 is recognized as 
contributions revenue in the Statement of Activities as detailed below:
Occupancy $ 18,000
Contractual Services 23,811
Supplies, Materials, and Travel 9,258
Personnel 390,452
Total $ 441,521
The total value of the services and the facilities provided by the College during the year ended June 30, 
2025 is also recognized as expenses as follows:
Scholarships $ 100,631
Other Student Services 57,116
Management and General 112,731
Fundraising 171,043
Total $ 441,521
G. Concentrations of Credit Risk
The Foundation maintains cash and cash equivalents at its financial institutions that are insured by the 
Federal Deposit Insurance Corporation (FDIC) up to $250,000. At June 30, 2025, the Foundation had 
cash and cash equivalents totaling $155,867 that were exposed to custodial credit risk but were 
collateralized by securities pledged by the Foundation’s financial institution on-behalf of the Foundation.
52
<PARSED TEXT FOR PAGE: 66 / 117>
REQUIRED SUPPLEMENTARY INFORMATION
<PARSED TEXT FOR PAGE: 67 / 117>
FY2025* FY2024* FY2023* FY2022* FY2021* FY2020* FY2019* FY2018* FY2017* FY2016*
College's proportionate percentage of the collective net pension liability 0.0000% 0.0000% 0.0000% 0.0000% 0.0000% 0.0000% 0.0000% 0.0000% 0.0000% 0.0000%
College's proportionate amount of the collective net pension liability $ - $ - $ - $ - $ - $ - $ - $ - $ - $ -
State's proportionate share of collective net pension liability associated with the College 137,237,740 136,715,113 144,216,097 143,278,856 153,781,255 146,156,442 141,981,891 132,756,562 150,631,522 142,796,497
Total $ 137,237,740 $ 136,715,113 $ 144,216,097 $ 143,278,856 $ 153,781,255 $ 146,156,442 $ 141,981,891 $ 132,756,562 $ 150,631,522 $ 142,796,497
College's DB covered payroll $ 18,378,557 $ 18,156,618 $ 17,709,871 $ 18,485,610 $ 18,661,907 $ 18,387,517 $ 18,444,296 $ 18,370,903 $ 20,970,430 $ 21,977,912
College's proportionate share of collective net pension liability as a percentage of its
DB covered payroll 746.73% 752.98% 814.33% 775.08% 824.04% 794.87% 769.79% 722.65% 718.30% 649.73%
SURS plan fiduciary net position as a percentage of the total pension liability 44.60% 44.06% 43.65% 45.45% 39.05% 40.71% 41.27% 42.04% 39.57% 42.37%
*The amounts presented were determined as of the prior fiscal year end.
FY2025 FY2024 FY2023 FY2022 FY2021 FY2020 FY2019 FY2018 FY2017 FY2016
Federal, trust, grant and other contributions (required contributions) $ 193,240 $ 212,448 $ 236,546 $ 149,463 $ 155,757 $ 153,469 $ 148,117 $ 159,156 $ 161,062 $ 167,235
Contributions in relation to required contributions 193,240 212,448 236,546 149,463 155,757 153,469 148,117 159,156 161,062 167,235
Contributions deficiency (excess) $ - $ - $ - $ - $ - $ - $ - $ - $ - $ -
College's covered payroll $ 1,613,022 $ 1,695,515 $ 1,843,694 $ 1,213,174 $ 1,226,434 $ 1,178,720 $ 1,205,183 $ 1,277,335 $ 1,285,411 $ 1,317,849
Contributions as a percentage of covered payroll 11.98% 12.53% 12.83% 12.32% 12.70% 13.02% 12.29% 12.46% 12.53% 12.69%
FY2025 FY2024 FY2023 FY2022 FY2021 FY2020 FY2019 FY2018 FY2017 FY2016
On-behalf payments for Community College Health Insurance Program $ 169,688 $ 144,236 $ 94,643 $ 92,291 $ 92,522 $ 89,969 $ 86,591 $ 85,396 $ 84,297 $ 100,481
Fiscal Year 2025 Total DB Contributions: $1,501,774
Fiscal Year 2025 Total RSP Contributions: $203,271
SCHEDULE OF COLLEGE CONTRIBUTIONS
State Universities Retirement System - Unaudited
JOHN A. LOGAN COLLEGE
CARTERVILLE, ILLINOIS 
SCHEDULE OF THE COLLEGE'S PROPORTIONATE SHARE OF THE NET PENSION LIABILITY
State Universities Retirement System - Unaudited
COMMUNITY COLLEGE DISTRICT NO. 530
STATE UNIVERSITIES RETIREMENT SYSTEM OF ILLINOIS (SURS) PENSION PLAN - GASB 68 
53
<IMAGE FOR PAGE: 67 / 117>
![image](sediment://0217c570aab6471#file_000000005b7c71f7b4b2a32a07acadeb#p_4.403275d877.jpg)
<PARSED TEXT FOR PAGE: 68 / 117>
Fiscal Year Ended 2025 2024 2023 2022 2021 2020 2019 2018
Total OPEB Liability
Service Cost $ 14,191 $ 16,441 $ 4,831 $ 9,148 $ 6,793 $ 5,389 $ 17,357 $ 17,620
Interest on Total OPEB Liability 259,606 204,751 208,735 127,088 148,082 158,767 169,959 148,927
Changes of Benefit Terms - - - 31,247 - - - -
Differences Between Expected and Actual Experience - 499,084 - 188,844 - (94,383) - 497,910
Changes of Assumptions or Other Inputs (450,718) 833,823 (20,569) (760,638) 380,555 107,469 162,832 116,522
Benefit Payments (357,186) (333,527) (344,213) (299,561) (245,817) (368,328) (373,937) (475,247)
Other Changes - - - - - 6,269 8,234 349,370
Net Change in Total OPEB Liability (534,107) 1,220,572 (151,216) (703,872) 289,613 (184,817) (15,555) 655,102
Total OPEB Liability - Beginning 6,345,001 5,124,429 5,275,645 5,979,517 5,689,904 5,874,721 5,890,276 5,235,174
Total OPEB Liability - Ending $ 5,810,894 $ 6,345,001 $ 5,124,429 $ 5,275,645 $ 5,979,517 $ 5,689,904 $ 5,874,721 $ 5,890,276
Covered Payroll $ 6,118,663 $ 5,883,129 $ 7,435,428 $ 7,435,428 $ 10,868,249 $ 10,868,249 $ 13,411,239 $ 13,411,239
Total OPEB Liability as a Percentage of Covered Payroll 94.97% 107.85% 68.92% 70.95% 55.02% 52.35% 43.80% 43.92%
Notes to Schedule
The information in this schedule will accumulate until a full 10-year trend is presented as required by GASB Statement No. 75.
SCHEDULE OF CHANGES IN THE COLLEGE'S TOTAL OPEB LIABILITY AND RELATED RATIOS
COLLEGE PLAN - GASB 75 - UNAUDITED
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS 
54
<PARSED TEXT FOR PAGE: 69 / 117>
FY2025 FY2024 FY2023 FY2022 FY2021 FY2020 FY2019 FY2018 FY2017
College's proportion of the collective net OPEB liability 0.907000% 0.956883% 0.978650% 0.995086% 0.978269% 0.964645% 0.977891% 0.971646% 1.108664%
College's proportionate share of the collective net OPEB liability $ 6,034,549 $ 6,758,784 $ 6,699,449 $ 17,270,036 $ 17,831,530 $ 18,217,715 $ 18,435,712 $ 18,011,609 $ 20,177,182
State's proportionate share of the collective net OPEB liability associated with the College 6,034,549 6,758,784 6,699,449 17,270,036 17,831,530 18,217,617 18,435,620 23,653,716 21,023,006
Total $ 12,069,098 $ 13,517,568 $ 13,398,898 $ 34,540,072 $ 35,663,060 $ 36,435,332 $ 36,871,332 $ 41,665,325 $ 41,200,188
College's covered payroll $ 33,937,600 $ 28,847,200 $ 18,928,600 $ 18,458,200 $ 18,504,390 $ 17,993,700 $ 17,318,296 $ 17,078,749 $ 16,859,262
College's proportionate share of the collective net OPEB liability
as a percentage of its covered payroll 17.8% 23.4% 35.4% 93.6% 96.4% 101.2% 106.5% 105.5% 119.7%
Plan fiduciary net position as a percentage of the total OPEB liability -15.58% -15.16% -18.05% -6.00% -4.83% -3.96% -3.42% -2.81% N/A
†The information in this schedule will accumulate until a full 10-year trend is presented as required by GASB Statement No. 75.
FY2025 FY2024 FY2023 FY2022 FY2021 FY2020 FY2019 FY2018 FY2017
Statutorily Required Contributions** $ 169,688 $ 144,236 $ 94,643 $ 92,291 $ 92,522 $ 89,969 $ 86,591 $ 85,396 $ 84,297
Contributions in relation to the College's covered payroll 0.50% 0.50% 0.50% 0.50% 0.50% 0.50% 0.50% 0.50% 0.50%
Annual contribution deficiency (excess)** N/A N/A N/A N/A N/A N/A N/A N/A N/A
**Statutorily required contributions = actual contributions
†The information in this schedule will accumulate until a full 10-year trend is presented as required by GASB Statement No. 75.
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS 
SCHEDULE OF THE EMPLOYER'S PROPORTIONATE SHARE OF THE COLLECTIVE NET OPEB LIABILITY†
COLLEGE INSURANCE PROGRAM (CIP) - GASB 75
SCHEDULE OF STATE CONTRIBUTIONS†
College Insurance Program (CIP) - Unaudited
College Insurance Program (CIP) - Unaudited
55
<PARSED TEXT FOR PAGE: 70 / 117>
NOTE 1: SURS PENSION PLAN
•
•
•
•
•
•
•
•
•
•
Special Funding Situation
Changes of Benefit Terms. 
Investment Return: The investment return is assumed to be 6.50%. This reflects an assumed real rate
of return to 4.10% and assumed price inflation of 2.40%.
For the purposes of financial reporting, the State of Illinois and participating employers are considered to be
under a special funding situation. A special funding situation is defined as a circumstance in which a
nonemployer entity is legally responsible for making contributions directly to a pension plan that is used to
provide pensions to the employees of another entity or entities and either (1) the amount of the contributions for
which the nonemployer entity is legally responsible is not dependent upon one or more events unrelated to
pensions or (2) the nonemployer is the only entity with a legal obligation to make contributions directly to a
pension plan. The State of Illinois is considered a nonemployer contributing entity. Participating employers are
considered employer contributing entities. The State is responsible for the collective net pension liability of the
plan with the exception of federal, trust, or grant contributions made by the College that are recognized as
deferred outflows of resources.
Effective Rate of Interest (ERI): The long-term assumption for the ERI for crediting the money
purchase accounts is 7.00%.
Public Act 103-0548, effective August 11, 2023, made changes to the calculation of service and eliminated the
part-time adjustment for participants on or after September 1, 2024. This change was first reflected in the Total
Pension Liability as of June 30, 2024.
Changes of Assumptions. 
Turnover Rates: Assumed rates maintain the pattern of decreasing termination rates as years of
service increase, with separate rates for academic and non-academic positions.
Disability Rates: Separate rates are assumed for members in academic positions, non-academic 
positions and public safety positions, as well as for males and females. Public safety disability 
incidence is assumed to be 50.00% line-of-duty related and 50.00% ordinary.
Mortality Rates: Use of Pub-2010 mortality tables reflects its high applicability to public pensions.
The projection scale utilized is the MP-2021 scale, with separate rates for academic, non-academic,
and public safety members.
Salary Increase: The overall assumed rates of salary increase range from 3.15% to 15.00% based on
years of service, with an underlying wage inflation rate of 2.40%. Separate rates of increase are
assumed for members in academic and non-academic positions.
Normal Retirement Rates: Separate rates are assumed for members in academic positions, non￾academic positions, and public safety positions. Rates are generally highest for public safety positions
and lowest for academic positions.
Plan Election: For new non-academic members, assumed plan election are 75% for Tier 2 and 25%
for Retirement Savings Plan (RSP). For new academic members, assumed plan election rates are 55%
for Tier 2 and 45% Retirement Savings Plan (RSP).
Cost of living adjustment: Annual annuity increases are assumed to be 3.00% for Tier 1 members and 
1.20% for Tier 2 members.
In accordance with Illinois Complied Statutes, an actuarial review is to be performed at least once every three
years to determine the reasonableness of actuarial assumptions regarding the retirement, disability, mortality,
turnover, interest, and salary of the members and benefit recipients of SURS. An experience review for the
years June 30, 2020 to June 30, 2023 was performed in Spring 2024, resulting in the adoption of new
assumptions as of June 30, 2024. These assumptions are listed below.
Early Retirement Rates: Separate rates are assumed for members in academic positions, non-academic
positions, and public safety positions. Rates are generally higher for non-academic positions.
LOGAN, JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO REQUIRED SUPPLEMENTARY INFORMATION - UNAUDITED
JUNE 30, 2025
56
<PARSED TEXT FOR PAGE: 71 / 117>
Valuation Date June 30, 2023
Measurement Date June 30, 2024
Sponsor's Fiscal Year-End June 30, 2025
Actuarial Cost Method
Contribution Policy
Asset Valuation Method
Investment Rate of Return
Inflation
Salary Increases
Retirement Age
Mortality
Healthcare Cost Trend Rates
Aging Factors
Expenses
Trend rates for plan year 2025 are based on actual premium increases. For non-Medicare
costs, trends start at 8.00% for plan year 2026 and decrease gradually to an ultimate rate of
4.25% in 2041. For MAPD costs, trend rates are based on actual premium increases for 2025,
15.00% in 2026 to 2030, and 7.00% in 2031, declining gradually to an ultimate rate of 4.25%
in 2041. 
Based on the 2013 SOA Study "Health Care Costs - From Birth to Death"
Health administrative expenses are included in the development of the per capita claims costs.
Operating expenses are included as a component of the Annual OPEB Expense.
Entry Age Normal, used to measure the Total OPEB Liability
Benefits are financed on a pay-as-you-go basis. Retired members contribute a percentage of
premium rates based on service at retirement. The sponsor contributes claims and expenses in
excess of retired member contributions. The goal of the policy is to finance current year costs
plus a margin for incurred but not paid plan costs.
Not applicable
Not applicable
2.25%
Depends on service and ranges from 12.75% at less than 1 year of service to 3.50% at 20 or
more years of service for employees under 50, and ranges from 12.00% at less than 1 year of
service to 3.00% at 20 or more years of service, for employees over 50 years of age. Salary
increases include a 3.00% wage inflation assumption.
Experience-based table of rates that are specific to the type of eligibility condition. Last
updated for the June 30, 2021 actuarial valuation of SURS.
Retirement and Beneficiary Annuitants: Pub-2010 Healthy Mortality Table and PubT-2010
Healthy Retiree Mortality Table. Disabled Annuitants: Pub-2010 Disabled Retiree Mortality
Table. Pre-Retirement: Pub-2010 Employee Mortality Table and PubT-2010 Employee
Mortality Table. Tables are adjusted for SURS experience. All tables reflect future mortality
improvements using Projection Scale MP-2020.
Methods and Assumptions Used to Determine Actuarial Liability and Contributions:
LOGAN, JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO REQUIRED SUPPLEMENTARY INFORMATION (CONCLUDED) - UNAUDITED
JUNE 30, 2025
NOTE 2: COLLEGE INSURANCE PLAN
57
<PARSED TEXT FOR PAGE: 72 / 117>
OTHER SUPPLEMENTAL INFORMATION
Other
<PARSED TEXT FOR PAGE: 73 / 117>
Assessed Valuation (by County)
Franklin County $ 126,172,144 $ 118,558,177 $ 107,333,205
Jackson County 905,987,227 815,831,864 760,945,209
Perry County 146,154,443 137,218,927 122,807,353
Randolph County 17,820,629 16,448,447 15,316,113
Williamson County 1,497,252,132 1,351,320,160 1,213,714,414
$ 2,693,386,575 $ 2,439,377,575 $ 2,220,116,294
Tax Rates
(Per $100 of Assessed Valuation)
Education 0.27016 0.27592 0.29345
Operations and Maintenance 0.04503 0.04798 0.04887
Bond and Interest 0.18679 0.20686 0.22848
Audit 0.00308 0.00277 0.00270
Liability, Protection, and Settlement 0.09006 0.10230 0.10809
Health, Life, and Safety 0.04266 0.04717 0.04625
Prior Year Adjustment 0.00717 0.00296 0.00033
 0.64495 0.68596 0.72817
Taxes Extended
Education $ 7,462,889 $ 6,899,328 $ 6,580,851
Operations and Maintenance 1,243,934 1,189,235 1,096,344
Bond and Interest 5,161,738 5,196,670 5,147,355
Audit 85,164 69,644 60,958
Liability, Protection, and Settlement 2,488,017 2,568,975 2,434,588
Health, Life, and Safety 1,178,515 1,177,193 1,041,718
Prior Year Adjustment (324,504) (134,128) (80,233)
$ 17,295,753 $ 16,966,917 $ 16,281,581
*
Payable in 2024* Payable in 2023*
Tax rates vary by county. Williamson County rates are reflected in the table. Tax extended represents actual
extensions from all counties. Therefore, rate times assessed valuation does not compute to taxes extended.
LEVY YEARS 2022, 2023 AND 2024
SCHEDULE OF ASSESSED VALUATIONS, TAX RATES, AND TAXES EXTENDED
Payable in 2025*
COMMUNITY COLLEGE DISTRICT NO. 530
JOHN A. LOGAN COLLEGE
UNAUDITED
2024 Levy 2023 Levy 2022 Levy 
 58
<PARSED TEXT FOR PAGE: 74 / 117>
Assessed Valuation - 2023 Levy
Franklin County $ 118,558,177
Jackson County 815,831,864
Perry County 137,218,927
Randolph County 16,448,447
Williamson County 1,351,320,160
$ 2,439,377,575
Debt Limit, 2.875% of Assessed Valuation (50 ILCS 405/1) $ 70,132,105
Less: Total Indebtedness (16,468,846)
Legal Debt Margin $ 53,663,259
FOR THE YEAR ENDED JUNE 30, 2025
SCHEDULE OF LEGAL DEBT MARGIN
COMMUNITY COLLEGE DISTRICT NO. 530
JOHN A. LOGAN COLLEGE
UNAUDITED
CARTERVILLE, ILLINOIS
 59
<IMAGE FOR PAGE: 75 / 117>
![image](sediment://5c6595ed446daf0#file_000000005b7c71f7b4b2a32a07acadeb#p_5.51d4de7521.jpg)
<PARSED TEXT FOR PAGE: 76 / 117>
UNIFORM FINANCIAL STATEMENTS
<PARSED TEXT FOR PAGE: 77 / 117>
Fund Balance, July 1, 2024, Restated $ 14,067,777 $ 1,291,503 $ 12,479,513 $ 276,263 $ 418,110 $ 3,892,997 $ 7,535,685 $ 9,112 $ 1,546,312 $ 41,517,272
Revenues
Local Tax Revenue 7,681,060 1,176,533 1,164,505 5,137,963 - - - 68,856 2,540,026 17,768,943
All Other Local Revenue - - - - - - - - - -
ICCB Grants 6,597,263 3,194,721 - - - 1,466,549 - - - 11,258,533
All Other State Revenue 237,663 101,855 1,635,514 - - 1,406,049 - - - 3,381,081
Federal Revenue 245,377 105,162 183,248 - - 9,578,674 - - - 10,112,461
Student Tuition and Fees 10,524,864 - - - 261,740 17,980 - - - 10,804,584
On-Behalf CIP - - - - - (2,287,489) - - - (2,287,489)
On-Behalf SURS - - - - - 9,216,940 - - - 9,216,940
All Other Revenue 2,336,176 248,786 373,877 23,773 1,086,730 1,416,179 293,904 4,151 390,601 6,174,177
Total Revenues 27,622,403 4,827,057 3,357,144 5,161,736 1,348,470 20,814,882 293,904 73,007 2,930,627 66,429,230
Expenditures
Instruction 9,001,273 - - - - 4,383,266 - - - 13,384,539
Academic Support 2,716,309 - - - - 996,853 - - - 3,713,162
Student Services 2,771,970 - - - - 1,480,343 - - - 4,252,313
Public Service/Continuing Education 625,430 12,593 - - 1,094,117 2,020,557 - - - 3,752,697
Auxiliary Services - - - - 1,795,091 2,621,769 - - - 4,416,860
Operations and Maintenance - 4,426,645 - - - 984,044 - - 763,429 6,174,118
Institutional Support 7,888,814 569,047 4,304,374 5,014,618 116,336 2,000,956 - 76,300 1,940,133 21,910,578
Scholarships, Grants, and Waivers 2,919,066 - - - 461,881 8,148,575 - - - 11,529,522
Total Expenditures 25,922,862 5,008,285 4,304,374 5,014,618 3,467,425 22,636,363 - 76,300 2,703,562 69,133,789
Net Transfers (2,209,782) 146,952 - - 2,077,355 279,379 (293,904) - - -
Fund Balance, June 30, 2025 $ 13,557,536 $ 1,257,227 $ 11,532,283 $ 423,381 $ 376,510 $ 2,350,895 $ 7,535,685 $ 5,819 $ 1,773,377 $ 38,812,713
(Restricted)
CARTERVILLE, ILLINOIS
Fund Fund
JOHN A. LOGAN COLLEGE
FISCAL YEAR ENDED JUNE 30, 2025
UNIFORM FINANCIAL STATEMENT #1
ALL FUNDS SUMMARY
COMMUNITY COLLEGE DISTRICT NO. 530
Operations and
Operations
Fund
Restricted
Fund
Purposes
Total
Bond and
Interest
Fund Fund Fund Fund
Audit
Liability,
Protection
and
Education Fund Cash Settlement
Maintenance Auxiliary Working
Maintenance Enterprises
and
 61
<IMAGE FOR PAGE: 77 / 117>
![image](sediment://24607ce51ed664c#file_000000005b7c71f7b4b2a32a07acadeb#p_6.c4998cae3a.jpg)
<PARSED TEXT FOR PAGE: 78 / 117>
Total Fund Balance - Uniform Financial Statement No. 1 $ 38,812,713
Amounts reported in the basic financial statements for net position are different because: 
64,018,832
1,974,734
193,240
169,688
(696,534)
205,730
(7,204,227)
Bonds payable (14,530,000)
Lease liability (101,132)
Subscription liablilty (1,837,714)
Postemployment benefits (11,845,443)
Compensated absences (3,679,246)
Accrued interest (46,824)
Net Position - Statement of Net Position $ 65,433,817
JUNE 30, 2025
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
RECONCILIATION OF THE UNIFORM FINANCIAL STATEMENT NO. 1 
TO THE STATEMENT OF NET POSITION
Some liabilities reported in the Statement of Net Position do not require the use of current
financial resources and therefore are not reported as liabilities in the Uniform Financial
Statements. These liabilities consist of:
Capital assets used in College activities are not current financial resources and therefore are
not reported in the Uniform Financial Statements.
Pension contributions made after the actuarial valuation date are considered expenditures in
the Uniform Financial Statements but are deferred outflows of resources in the basic financial
statements.
OPEB contributions made after the actuarial measurement date are considered expenditures in
the Uniform Financial Statements but are deferred outflows of resources in the basic financial
statements.
Premiums on fixed debt are other financial sources in the Uniform Financial Statements but
are liabilities that are amortized over the life of the fixed debt in the basic financial statements.
Deferred losses on refunded fixed debt are other financing uses in the Uniform Financial
Statements but are reported as deferred outflows of resources that are amortized over the life
of the fixed debt in the basic financial statements.
Changes in assumptions, experiences, and other calculations are reported as deferred
outflows/inflows in the basic financial statements; however, they are not recorded in the
Uniform Financial Statements.
Right-of-use assets used in College activities are not current financial resources and therefore
are not reported in the Uniform Financial Statements.
 62
<PARSED TEXT FOR PAGE: 79 / 117>
Net Change in Fund Balances - Uniform Financial Statement No. 1 $ (2,704,559)
Capital outlays $ 9,937,318
Depreciation and amortization expense (3,872,793)
6,064,525
(21,347)
(19,208)
169,688
 (1,645,796)
Bonds payable, including amortization of bond premiums 4,473,750
Lease liability 41,633
SBITA liability 124,746
Postemployment benefits 2,214,946
Compensated absences (31,654)
Accrued interest 10,475
Increase in Net Position - Statement of Revenues, Expenses, and Changes in Net Position $ 8,677,199
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
RECONCILIATION OF THE UNIFORM FINANCIAL STATEMENT NO. 1 
FOR THE YEAR ENDED JUNE 30, 2024
TO THE STATEMENT OF REVENUES, EXPENSES, AND CHANGES IN NET POSITION
Some expenses reported in the Uniform Financial Statements use current financial resources to
reduce long-term liabilities reported on the basic financial statements. These activities consist
of:
Amounts reported in the general-purpose Statement of Revenues, Expenses, and Changes in Net
Position are different because: 
The Uniform Financial Statements report capital outlays as expenditures paid while the basic
financial statements report depreciation expense to allocate those expenditures over the lives of
the assets. This is the amount by which capital outlays exceeded depreciation in the current
period:
Net book value of disposed capital assets is not reported in the Uniform Financial Statements.
Contributions to pension funds are recognized as expenditures when paid to the pension fund
on the Uniform Financial Statements. These expenses are recorded on the basic financial
statements based on the pension expense, corresponding with the most recent measurement
period. This is the difference between these amounts.
Contributions to the OPEB plans are recognized as expenditures when paid to the plans on the
Uniform Financial Statements. These expenses are recorded on the basic financial statements
based on the OPEB expense, corresponding with the most recent measurement period. This is
the difference between these amounts.
Proceeds from long-term debt are recognized as other local revenue in the Uniform Financial
Statements but have no impact on net assets in the Statement of Revenues, Expenses, and
Changes in Net Position.
 63
<PARSED TEXT FOR PAGE: 80 / 117>
Fixed Assets
Site $ 346,427 $ - $ - $ 346,427
Construction in Progress 1,069,623 5,989,317 (125,239) 6,933,701
Site Improvements 6,341,773 - - 6,341,773
Buildings and Improvements 95,445,503 376,594 - 95,822,097
Equipment 11,252,335 1,541,376 (336,959) 12,456,752
Right to Use Leased Equipment 211,084 211,084
Right to Use SBITAs 539,805 2,155,270 2,695,075
Total Fixed Assets 115,206,550 10,062,557 (462,198) 124,806,909
Less: Accumulated Depreciation
 and Amortization 55,256,164 3,872,793 (315,614) 58,813,343
Net Fixed Assets $ 59,950,386 $ 6,189,764 $ (146,584) $ 65,993,566
Fixed Debt
Bonds Payable $ 18,890,000 $ - $ (4,360,000) $ 14,530,000
Bond Premium 855,484 - (158,950) 696,534
Accrued Compensated Absences 1,680,257 1,998,989 - 3,679,246
Lease Liability 142,765 - (41,633) 101,132
Subscription Liability 316,664 1,645,796 (124,746) 1,837,714
Net OPEB Liability 13,103,785 - (1,258,342) 11,845,443
Total Fixed Debt $ 34,988,955 $ 3,644,785 $ (5,943,671) $ 32,690,069
Asset/Debt
Additions Deletions
Account
Asset/Debt
July 1, 2024
Groups
June 30, 2025
Groups
Account
JOHN A. LOGAN COLLEGE
UNIFORM FINANCIAL STATEMENT #2
SUMMARY OF FIXED ASSETS AND DEBT
COMMUNITY COLLEGE DISTRICT NO. 530
Fixed Fixed
FISCAL YEAR ENDED JUNE 30, 2025
CARTERVILLE, ILLINOIS 
 64
<PARSED TEXT FOR PAGE: 81 / 117>
Operating Revenues by Sources
Local Government Revenues:
Local Taxes $ 6,824,719 $ 1,176,533 $ 8,001,252
Corporate Personal Property Replacement Tax 856,341 - 856,341
Total Local Government 7,681,060 1,176,533 8,857,593
State Government:
ICCB Base Operating Grant 2,057,498 1,013,394 3,070,892
ICCB Equalization Grant 4,205,349 2,071,291 6,276,640
ICCB Career and Technical Education 223,406 110,036 333,442
ICCB Performance Grant 20,355 - 20,355
Other ICCB Unrestricted Grants not listed above 90,655 - 90,655
Other State not listed above 237,663 101,855 339,518
Total State Government 6,834,926 3,296,576 10,131,502
Federal Government:
Department of Education 36,300 15,558 51,858
Department of Labor - - -
Department of Health & Human Services 208,793 89,482 298,275
Other 284 122 406
Total Federal Government 245,377 105,162 350,539
Student Tuition and Fees:
Tuition 9,803,043 - 9,803,043
Fees 721,821 - 721,821
Total Student Tuition and Fees 10,524,864 - 10,524,864
Other Sources:
Sales and Service Fees 219,009 - 219,009
Facilities Revenue - 140,622 140,622
Investment Revenue 740,061 82,703 822,764
Non-Governmental Grants 6,566 - 6,566
Other 1,370,540 25,461 1,396,001
Total Other Sources 2,336,176 248,786 2,584,962
Total Revenue 27,622,403 4,827,057 32,449,460
Less Non-Operating Items:* - - -
Adjusted Revenue $ 27,622,403 $ 4,827,057 $ 32,449,460
*Intercollege revenues that do not generate related local college credit hours are subtracted to allow for statewide
comparisons.
JOHN A. LOGAN COLLEGE
FISCAL YEAR ENDED JUNE 30, 2025
UNIFORM FINANCIAL STATEMENT #3
OPERATING FUNDS REVENUES AND EXPENDITURES
COMMUNITY COLLEGE DISTRICT NO. 530
Operations
CARTERVILLE, ILLINOIS
Operating
Total
Fund
Maintenance
and
Fund
Education
Funds
65
<PARSED TEXT FOR PAGE: 82 / 117>
Operating Expenditures
By Program:
Instruction $ 9,001,273 $ - $ 9,001,273
Academic Support 2,716,309 - 2,716,309
Student Services 2,771,970 - 2,771,970
Public Service/Continuing Education 625,430 12,593 638,023
Auxiliary Services - - -
Operations and Maintenance - 4,426,645 4,426,645
Institutional Support 7,888,814 569,047 8,457,861
Scholarships, Grants, and Waivers 2,919,066 - 2,919,066
Total Expenditures 25,922,862 5,008,285 30,931,147
Less Non-Operating Items:* - - -
Adjusted Expenditures $ 25,922,862 $ 5,008,285 $ 30,931,147
By Object:
Salaries $ 15,789,143 $ 2,787,065 $ 18,576,208
Employee Benefits 2,089,526 387,303 2,476,829
Contractual Services 1,501,984 185,755 1,687,739
General Materials and Supplies 1,065,681 432,986 1,498,667
Library Materials** 25,208 - 25,208
Conference and Meeting Expenses 373,101 4,386 377,487
Fixed Charges 142,558 552 143,110
Utilities 9,909 1,135,003 1,144,912
Capital Outlay 1,983,037 75,002 2,058,039
Other 2,967,923 233 2,968,156
Student Grants and Scholarships** 2,919,066 - 2,919,066
Total Expenditures 25,922,862 5,008,285 30,931,147
Less Non-Operating Items:* - - -
Adjusted Expenditures $ 25,922,862 $ 5,008,285 $ 30,931,147
**Non-add line
*Intercollege expenditures that do not generate related local college credit hours are subtracted to allow for
statewide comparisons.
Fund
Education
Total
Operating
Fund Funds
Maintenance
and
Operations
CARTERVILLE, ILLINOIS
JOHN A. LOGAN COLLEGE
FISCAL YEAR ENDED JUNE 30, 2025
UNIFORM FINANCIAL STATEMENT #3
OPERATING FUNDS REVENUES AND EXPENDITURES
COMMUNITY COLLEGE DISTRICT NO. 530
66
<PARSED TEXT FOR PAGE: 83 / 117>
Revenues by Source
Total Local Government $ -
State Government:
ICCB - Adult Education 142,034
ICCB - Other 1,324,515
On-Behalf CIP (2,287,489)
On-Behalf SURS 9,216,940
Other 1,406,049
Total State Government 9,802,049
Federal Government:
Department of Education 8,316,569
Department of Labor 107,122
Department of Health and Human Services 1,048,973
Other 106,010
Total Federal Government 9,578,674
Other Sources:
Tuition and Fees 17,980
Other 1,416,179
Total Other Sources 1,434,159
Total Restricted Purposes Fund Revenues $ 20,814,882
Expenditures By Program
Instruction $ 4,383,266
Academic Support 996,853
Student Services 1,480,343
Public Service/Continuing Education 2,020,557
Auxiliary Services 2,621,769
Operations and Maintenance 984,044
Institutional Support 2,000,956
Scholarships, Grants, and Waivers 8,148,575
Total Restricted Purposes Fund Expenditures $ 22,636,363
Expenditures By Object
Salaries $ 2,000,014
Employee Benefits (Including SURS & CIP On-Behalf) 7,757,287
Contractual Services 192,374
General Materials and Supplies 1,056,899
Library Materials* - 
Travel & Conference/Meeting Expenses 74,482
Fixed Charges 89,560
Utilities 24,742
Capital Outlay 3,126,928
Other 8,314,077
Scholarships, Grants, and Waivers* 8,148,575
Total Restricted Purposes Fund Expenditures $ 22,636,363
*Non-add line
Fund
Purposes
Restricted
JOHN A. LOGAN COLLEGE 
UNIFORM FINANCIAL STATEMENT #4
RESTRICTED PURPOSES FUND REVENUES AND EXPENDITURES
COMMUNITY COLLEGE DISTRICT NO. 530
FISCAL YEAR ENDED JUNE 30, 2025
CARTERVILLE, ILLINOIS
 67
<PARSED TEXT FOR PAGE: 84 / 117>
Instruction
Instructional Programs $ 13,224,669
Other 159,870
Total Instruction 13,384,539
Academic Support
Library Center 308,473
Instructional Materials Center 93,099
Academic Computing Support 403,493
Academic Administration and Planning 2,459,547
Other 448,550
Total Academic Support 3,713,162
Student Services
Admissions and Records 503,647
Counseling and Career Guidance 2,383,115
Financial Aid Administration 496,410
Other 869,141
Total Student Services Support 4,252,313
Public Service/Continuing Education
Community Education 351,647
Customized Training (Instructional) 232,229
Community Services 3,153,826
Other 14,995
Total Public Service/Continuing Education 3,752,697
Auxiliary Services 4,416,860
Operations and Maintenance of Plant
Maintenance 1,246,812
Custodial 2,070,234
Grounds 765,533
Campus Security 950,909
Transportation -
Utilities 1,135,003
Administration -
Other 5,627
Total Operations and Maintenance of Plant 6,174,118
Institutional Support
Executive Management 1,402,679
Fiscal Operations 1,254,780
Community Relations 1,053,455
Administrative Support Services 1,035,047
Board of Trustees 103,779
General Institution 2,000,702
Institutional Research 355,501
Administrative Data Processing 4,987,306
Other 398,337
Total Institutional Support 12,591,586
Scholarships, Student Grants, and Waivers 11,529,522
Total Current Funds Expenditures $ 59,814,797
*Current Funds include the Education; Operations and Maintenance; Auxiliary Enterprises;
Restricted Purposes; Audit; Liability, Protection, and Settlement; and PBC Operations and
Maintenance Funds.
COMMUNITY COLLEGE DISTRICT NO. 530
JOHN A. LOGAN COLLEGE
FISCAL YEAR ENDED JUNE 30, 2025
UNIFORM FINANCIAL STATEMENT #5
CURRENT FUNDS * EXPENDITURES BY ACTIVITY
CARTERVILLE, ILLINOIS
68
<PARSED TEXT FOR PAGE: 85 / 117>
STATE COMPLIANCE SECTION
Illinois Community College Board
State Grants Financial Compliance Section
<PARSED TEXT FOR PAGE: 86 / 117>
INDEPENDENT AUDITOR'S REPORT ON COMPLIANCE WITH STATE REQUIREMENTS 
FOR ADULT EDUCATION AND FAMILY LITERACY GRANTS
To the Board of Trustees
John A. Logan College
Community College District No. 530
Carterville, Illinois 62918
Opinion
We have audited the accompanying financial statements of the Adult Education and Family Literacy
Grants (State Basic and Performance) (grant program) of John A. Logan College, Community College 
District No. 530 (the College) as of June 30, 2025, and the related notes to the grant program financial 
statements as listed in the table of contents. 
In our opinion, the financial statements referred to above present fairly, in all material respects, the 
respective financial position of the Adult Education and Family Literacy Grants (State Basic and 
Performance) of John A. Logan College, Community College District No. 530 as of June 30, 2025, and 
the respective changes in financial position for the year then ended in conformity with accounting 
principles generally accepted in the United States of America.
Basis for Opinion 
We conducted our audit in accordance with auditing standards generally accepted in the United States of 
America. Our responsibilities under those standards are further described in the Auditor's Responsibilities 
for the Audit of the Financial Statements section of our report. We are required to be independent of the 
College, and to meet our other ethical responsibilities, in accordance with the relevant ethical 
requirements relating to our audit. We believe that the audit evidence we have obtained is sufficient and 
appropriate to provide a basis for our audit opinions.
Emphasis of Matter
The grant program financial statements on pages 71-72 are intended to present the financial position and 
changes in financial position of the Adult Education and Family Literacy Grants. They do not purport to, 
and do not, present fairly the financial position of the College as of June 30, 2025, or the changes in 
financial position for the year then ended in accordance with accounting principles generally accepted in 
the United States of America. Our opinion is not modified with respect to this matter.
Management’s Responsibility for the Financial Statements
Management is responsible for the preparation and fair presentation of these grant program financial 
statements in accordance with accounting principles general accepted in the United States of America, 
and for the design, implementation, and maintenance of internal control relevant to the preparation and 
fair presentation of the financial statements that are free from material misstatement, whether due to fraud 
or error.
69
 3401 Professional Park Drive ▪ Marion, IL 62959 
Phone: (618) 997-3055 Fax: (618) 997-5121 kempercpa.com
~~t41KEMPER 
.i:iiCPA GROUPLLP 
Certified Public Accountants and Consultants 
<IMAGE FOR PAGE: 86 / 117>
![image](sediment://39338fa0c540b72#file_000000005b7c71f7b4b2a32a07acadeb#p_7.56a9644e92.jpg)
<PARSED TEXT FOR PAGE: 87 / 117>
Auditor's Responsibilities for the Audit of the Financial Statements 
Our objectives are to obtain reasonable assurance about whether the financial statements as a whole are 
free from material misstatement, whether due to fraud or error, and to issue an auditor's report that 
includes our opinions. Reasonable assurance is a high level of assurance but is not absolute assurance and 
therefore is not a guarantee that an audit conducted in accordance with generally accepted auditing 
standards will always detect a material misstatement when it exists. The risk of not detecting a material 
misstatement resulting from fraud is higher than for one resulting from error, as fraud may involve 
collusion, forgery, intentional omissions, misrepresentations, or the override of internal control. 
Misstatements are considered material if there is a substantial likelihood that, individually or in the 
aggregate, they would influence the judgment made by a reasonable user based on the financial 
statements. 
In performing an audit in accordance with generally accepted auditing standards, we:
• Exercise professional judgment and maintain professional skepticism throughout the audit.
• Identify and assess the risks of material misstatement of the financial statements, whether due to 
fraud or error, and design and perform audit procedures responsive to those risks. Such 
procedures include examining, on a test basis, evidence regarding the amounts and disclosures in 
the financial statements.
• Obtain an understanding of internal control relevant to the audit in order to design audit 
procedures that are appropriate in the circumstances, but not for the purpose of expressing an 
opinion on the effectiveness of the College's internal control. Accordingly, no such opinion is 
expressed.
• Evaluate the appropriateness of accounting policies used and the reasonableness of significant 
accounting estimates made by management, as well as evaluate the overall presentation of the 
financial statements.
We are required to communicate with those charged with governance regarding, among other matters, the 
planned scope and timing of the audit, significant audit findings, and certain internal control-related 
matters that we identified during the audit.
Other Reporting Required by Government Auditing Standards
In accordance with Government Auditing Standards, we have also issued our report dated February 19, 
2026, on our consideration of the College’s internal control over financial reporting and on our tests of its 
compliance with certain provisions of laws, regulations, contracts, and grant agreements, and other 
matters. The purpose of that report is solely to describe the scope of our testing of internal control over 
financial reporting and compliance and the results of that testing, and not to provide an opinion on the 
effectiveness of the College’s internal control over financial reporting or on compliance. That report is an 
integral part of an audit performed in accordance with Government Auditing Standards in considering the 
College’s internal control over financial reporting and compliance.
KEMPER CPA GROUP LLP
Certified Public Accountants and Consultants
Marion, Illinois
February 19, 2026
70
<PARSED TEXT FOR PAGE: 88 / 117>
Assets
Current Assets
Cash Held by John A. Logan College $ 9,513 $ 4,043 $ 13,556
Total Assets $ 9,513 $ 4,043 $ 13,556
Liabilities and Fund Balances
Current Liabilities
Accounts Payable $ 5,265 $ 2,123 $ 7,388
Accrued Expenses 4,248 1,920 6,168
 Total Liabilities 9,513 4,043 13,556
Fund Balance
Reserved - - - 
Total Liabilities and Fund Balances $ 9,513 $ 4,043 $ 13,556
CARTERVILLE, ILLINOIS
JOHN A. LOGAN COLLEGE
JUNE 30, 2025
BALANCE SHEET
STATE ADULT EDUCATION RESTRICTED FUNDS
COMMUNITY COLLEGE DISTRICT NO. 530
State
Total 
(Memorandum 
Basic Performance Only)
The accompanying notes are an integral part of these financial statements.
71
<PARSED TEXT FOR PAGE: 89 / 117>
Revenues
Grant $ 92,039 $ 49,995 $ 142,034
Expenditures by Program
Personnel Services 70,068 38,100 108,168
Fringe Benefits 11,250 5,820 17,070
Travel 1,310 209 1,519
Supplies 7,731 3,137 10,868
Contractual Services - - - 
Occupancy - 1,200 1,200
Telecommunications 742 - 742
Training and Education - 1,529 1,529
Miscellaneous 938 - 938
Total Expenditures 92,039 49,995 142,034
Excess of Revenues
Over (Under) Expenditures - - - 
Fund Balance, July 1, 2024 - - - 
Fund Balance, June 30, 2025 $ - $ - $ - 
CARTERVILLE, ILLINOIS
JOHN A. LOGAN COLLEGE
FOR THE YEAR ENDED JUNE 30, 2025
STATEMENT OF REVENUES, EXPENDITURES, AND CHANGES IN FUND BALANCE
STATE ADULT EDUCATION RESTRICTED FUNDS
COMMUNITY COLLEGE DISTRICT NO. 530
State
Total 
(Memorandum 
Basic Performance Only)
The accompanying notes are an integral part of these financial statements.
72
<PARSED TEXT FOR PAGE: 90 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO GRANT PROGRAM FINANCIAL STATEMENTS 
JUNE 30, 2025
NOTE 1: PROGRAM DESCRIPTIONS
The College is responsible for administering the programs listed below in accordance with “Policy 
Guidelines for Restricted Grant Expenditures and Reporting” set forth by ICCB in its Fiscal Management 
Manual. Program funds are accounted for in the College’s current restricted fund. 
Adult Education and Family Literacy Grant Program
ICCB awards funding to eligible applicants to develop, implement, and improve adult education and 
literacy activities. The provider must use the grant to establish or operate programs that provide services 
or instruction in one or more of the following categories:
• Adult education and literacy services (including workplace), 
• Family literacy services, and/or
• English literacy programs.
ICCB provides funding for adult education and family literacy from State and federal sources. State 
funds include three categories (1) State Basic, (2) State Public Assistance, and (3) State Performance. 
Federal funds include two categories: (1) Federal Basic and (2) Federal EL/Civics. Funding is allocated 
through a competitive process. The funding source determined the applicable statutory regulations, 
policies, and guidelines, including allowable costs. State Performance – Grants are awarded to adult 
education and family literacy providers based upon performance outcomes.
NOTE 2: SUMMARY OF SIGNIFICANT ACCOUNTING POLICIES
A. Basis of Accounting
The statements have been prepared on the modified accrual basis. 
Expenditures are reported when services are rendered or when goods are received. The grant funds shall 
be expended or obligated prior to June 30 each year, the last day of the fiscal year. Grant funds should be 
accounted for in the same period as in the credit hour claiming process. Unexpended funds shall be 
returned to ICCB by October 15 following the end of the fiscal year. 
Grant revenues are reported in these grant program financial statements when allowable grant 
expenditures are made. Expenditures are allowable if they comply with “Policy Guidelines for Restricted 
Grant Expenditures and Reporting” set forth in ICCB’s Fiscal Management Manual. Grant funds should 
be accounted for in the same period as in the credit hour claiming process.
These grant program financial statements cover only the State Adult Education Grant Programs. They are 
not intended to, and do not, present the financial position or results of operations of the College in its 
entirety.
73
<PARSED TEXT FOR PAGE: 91 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO GRANT PROGRAM FINANCIAL STATEMENTS (CONCLUDED)
JUNE 30, 2025
NOTE 2: SUMMARY OF SIGNIFICANT ACCOUNTING POLICIES (CONCLUDED)
B. Cash Held by John A. Logan College
To facilitate sound management, substantially all grant program cash for the State Adult Education Grant 
Program is pooled with the College.
C. Receivables – Governmental Claims
A receivable is recorded for the funds to be received from ICCB at June 30, 2025, for reimbursement of 
allowable expenditures incurred during the fiscal year. These amounts are considered to be 100% 
collectible. 
D. Due to Other Funds
This account presents the amount to be reimbursed to other funds for the use of the other funds’ resources 
to pay for the expenses incurred by the grant program. 
E. Capital Assets
Acquisitions of capital assets, if any, are reported as capital assets in the College’s financial statements. 
They are recorded as capital outlay and are not capitalized in the grant program financial statements. 
There were no capital assets purchased with the grant funds during the fiscal year ended June 30, 2025.
F. Use of Estimates
The preparation of the grant program financial statements in conformity with accounting principles 
generally accepted in the United States of America requires management to make estimates and 
assumptions that could affect certain reported amounts and disclosures. Actual results could differ from 
those estimates and assumptions. 
74
<PARSED TEXT FOR PAGE: 92 / 117>
ENROLLMENT DATA AND OTHER BASES
UPON WHICH CLAIMS ARE FILED
<PARSED TEXT FOR PAGE: 93 / 117>
INDEPENDENT ACCOUNTANT'S REPORT ON THE SCHEDULE 
OF ENROLLMENT DATA AND OTHER BASES UPON 
WHICH CLAIMS ARE FILED
To the Board of Trustees
John A. Logan College
Community College District No. 530
Carterville, Illinois 62918
We have examined the accompanying Schedule of Enrollment Data and Other Bases Upon Which Claims 
are Filed of John A. Logan College, Community College District No. 530 for the year ended June 30, 
2025 (the Schedule). The College’s management is responsible for preparing the Schedule in accordance 
with the guidelines of the Illinois Community College Board’s Fiscal Management Manual. Our 
responsibility is to express an opinion on the Schedule based on our examination.
Our examination was conducted in accordance with attestation standards established by the 
American Institute of Certified Public Accountants. Those standards require that we plan and perform the 
examination to obtain reasonable assurance about whether the Schedule referred to above is in accordance 
with the guidelines of the Illinois Community College Board’s Fiscal Management Manual, in all 
material respects. The nature, timing, and extent of the procedures selected depend on our judgment, 
including an assessment of the risks of material misstatement of the Schedule referred to above, whether 
due to fraud or error. We believe that the evidence we obtained is sufficient and appropriate to provide a 
reasonable basis for our opinion. 
We are required to be independent and to meet our other ethical responsibilities in accordance with 
relevant ethical requirements relating to the engagement. 
In our opinion, the Schedule is presented in accordance with the guidelines of the Illinois Community 
College Board’s Fiscal Management Manual in all material respects.
The supplementary information on pages 78-80 discusses the College’s residency verification steps and is 
the responsibility of the College’s management. This information has not been subjected to the audit 
procedures applied in the audit of the Schedule, and accordingly, we do not express an opinion or provide 
any assurance on it. 
KEMPER CPA GROUP LLP
Certified Public Accountants and Consultants
Marion, Illinois 
February 19, 2026
75
 3401 Professional Park Drive ▪ Marion, IL 62959 
Phone: (618) 997-3055 Fax: (618) 997-5121 kempercpa.com
~~t41KEMPER 
.i:iiCPA GROUPLLP 
Certified Public Accountants and Consultants 
<IMAGE FOR PAGE: 93 / 117>
![image](sediment://92af06a23b8f254#file_000000005b7c71f7b4b2a32a07acadeb#p_8.9a8c680105.jpg)
<IMAGE FOR PAGE: 94 / 117>
![image](sediment://5f62662aedabd20#file_000000005b7c71f7b4b2a32a07acadeb#p_9.ae4dfe0379.jpg)
<PARSED TEXT FOR PAGE: 95 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
RECONCILIATION OF TOTAL REIMBURSABLE SEMESTER CREDIT HOURS
FOR THE YEAR ENDED JUNE 30, 2025
Total Total
Unrestricted Restricted
Total Credit Hours Total Credit Hours
Unrestricted Certified to Restricted Certified to
Categories Credit Hours the ICCB Difference Credit Hours the ICCB Difference
Baccalaureate 36,223.0 36,223.0 - 258.5 258.5 -
Business Occupational 5,449.5 5,449.5 - 68.0 68.0 -
Technical Occupational 6,426.5 6,426.5 - 308.5 308.5 -
Health Occupational 7,665.5 7,665.5 - 13.5 13.5 -
Remedial Developmental 1,114.0 1,114.0 - - - -
Adult Education 515.0 515.0 - 2,525.5 2,525.5 -
Total 57,393.5 57,393.5 - 3,174.0 3,174.0 -
FOR THE YEAR ENDED JUNE 30, 2025
Total Total
Attending Attending
(Unrestricted As Certified
and Restricted) To The ICCB Difference
Reimbursable In-District Residents 52,762.0 52,762.0 -
Reimbursable Out-of-District on
Chargeback or Contractual Agreement 2,686.0 2,686.0 -
Total 55,448.0 55,448.0 -
Total
Reimbursable
Total Certified to
Reimbursable ICCB Difference
Dual Credit 6,007.0 6,007.0 -
Dual Enrollment 2,673.0 2,673.0 -
Total 8,680.0 8,680.0 -
FOR THE YEAR ENDED JUNE 30, 2025
Total
Reimbursable
Total Correctional
Reimbursable Credit Hours
Correctional Certified to
Categories Credit Hours The ICCB Difference
Baccalaureate - - -
Business Occupational - - -
Technical Occupational - - -
Health Occupational - - -
Remedial Development - - -
Adult Education - - -
Total - - -
RECONCILIATION OF IN-DISTRICT/CHARGEBACK AND COOPERATIVE/CONTRACTUAL AGREEMENT CREDIT HOURS
RECONCILIATION OF TOTAL CORRECTIONAL SEMESTER CREDIT HOURS
CARTERVILLE, ILLINOIS
 77
<PARSED TEXT FOR PAGE: 96 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
DOCUMENTATION OF RESIDENCY VERIFICATION STEPS
JUNE 30, 2025
In-District Student
Description: A student who has lived in Franklin, Jackson, Perry, Randolph, or Williamson counties for 
at least 30 days prior to the beginning of the semester. 
Residency Code: In-district
Acceptable Documentation: Includes driver’s license, voter registration card, or a property tax statement, 
and the proof must show an in-district address. 
If none of the above items are available, the student may establish proof of in-district residency by 
providing a notarized statement signed by the student and his/her parents stating that the student’s 
residence is within the boundaries of the district. In the event that parents are not appropriate or available 
as co-signers on a notarized statement, such a statement can be co-signed by a city clerk or the county 
clerk in the city or county where the student has a permanent address.
Tuition Charge: Current in-district tuition charge
Student Employed Full-Time in the District
Description: An Illinois resident who lives outside the College’s district but works at least 35 hours per 
week at a business or industry located in the district.
Residency Code: Out-of-district
Acceptable Documentation: A signed letter from employer verifying that the student works at least 35 
hours in the district.
Tuition Charge: Current in-district tuition charge
Out-of-District Student
Description: A student who has lived outside the district boundaries but within the State of Illinois for at 
least 30 days prior to the beginning of the semester.
Residency Code: Out-of-district
Acceptable Documentation: Includes driver’s license, voter registration card, or property tax statement. 
Tuition Charge: Current out-of-district tuition charge
78
<PARSED TEXT FOR PAGE: 97 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
DOCUMENTATION OF RESIDENCY VERIFICATION STEPS (CONTINUED)
JUNE 30, 2025
Chargeback Student
Description: A student who lives in Illinois outside the district boundaries but attends the College 
because his/her home Community College does not offer a specific degree/certificate program.
Residency Code: Out-of-district
Acceptable Documentation: A signed chargeback agreement from the home community college.
Tuition Charge: Current out-of-district tuition charge, but a waiver is processed for the difference 
between in-district and out-of-district
Reciprocal Agreement Student
Description: A student who lives in the Shawnee College, Rend Lake College, or Southeastern Illinois 
Community College district but attends John A. Logan College for the purpose of enrolling in a specific 
course not offered by the home community college. Since this is an agreement made among these four 
colleges, a chargeback request is not required.
Residency Code: Out-of-district
Acceptable Documentation: A letter of reciprocity from the home community college.
Tuition Charge: Current in-district tuition charge
Out-of-State Student
Description: A student who lives outside the State of Illinois.
Residency Code: Out-of-state
Acceptable documentation: None is required.
Tuition Charge: Current out-of-state tuition charge
79
<PARSED TEXT FOR PAGE: 98 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
DOCUMENTATION OF RESIDENCY VERIFICATION STEPS (CONCLUDED)
JUNE 30, 2025
International Student
Description: A student who lives outside of the United States.
Residency Code: Foreign
Acceptable Documentation: None, other than the typical international student admission paperwork 
which is completed with the Director of Counseling.
Tuition Charge: Current out-of-state tuition charge
International Athlete
Description: A student who lives outside of the United States but who attends the College for the 
purpose of playing collegiate sports.
Residency Code: Foreign
Acceptable Documentation: None, other than the typical international student admission paperwork 
which is completed with the Director of Counseling.
Tuition Charge: Current in-district tuition charge
International Student with U.S. In-District Sponsor
Description: A student whose permanent residence is outside of the United States but who lives with and 
is financially sponsored by a resident within the college district.
Residency Code: Out-of-country
Acceptable Documentation: A signed letter from an in-district resident verifying financial sponsorship.
Tuition Charge: Current in-district tuition charge
80
<PARSED TEXT FOR PAGE: 99 / 117>
STATE OF ILLINOIS CONSOLIDATED YEAR-END FINANCIAL REPORT
<PARSED TEXT FOR PAGE: 100 / 117>
INDEPENDENT AUDITOR’S REPORT ON 
THE STATE OF ILLINOIS 
CONSOLIDATED YEAR-END FINANCIAL REPORT
To the Board of Trustees
John A. Logan College
Community College District No. 530
Carterville, Illinois 62918
We have audited the financial statements of John A. Logan College, Community College District No. 530 
(the College) as of and for the year ended June 30, 2025, and have issued our report thereon dated 
February 19, 2026, which expressed an unmodified opinion on those financial statements, and appears on 
pages 1-3. 
Our audit was conducted for the purpose of forming an opinion on the financial statements as a whole. 
The “Consolidated Year-End Financial Report” for the State of Illinois on pages 82a-82l, for the fiscal 
year ended June 30, 2025, is presented for purposes of additional analysis, as required by the State of 
Illinois, and is not a required part of the financial statements. Such information is the responsibility of 
management and was derived from and relates directly to the underlying accounting and other records 
used to prepare the financial statements. The information has been subjected to the auditing procedures 
applied in the audit of the financial statements and certain additional procedures, including comparing and 
reconciling such information directly to the underlying accounting and other records used to prepare the 
financial statements or to the financial statements themselves, and other additional procedures in 
accordance with auditing standards generally accepted in the United States of America. In our opinion, 
the information is fairly stated in all material respects in relation to the financial statements as a whole.
This report is intended solely for the information and use of management of the College and the State of 
Illinois and is not intended to be and should not be used by anyone other than those specified parties.
KEMPER CPA GROUP LLP
Certified Public Accountants and Consultants
Marion, Illinois
February 19, 2026
81
 3401 Professional Park Drive ▪ Marion, IL 62959 
Phone: (618) 997-3055 Fax: (618) 997-5121 kempercpa.com
~~t41KEMPER 
.i:iiCPA GROUPLLP 
Certified Public Accountants and Consultants 
<IMAGE FOR PAGE: 100 / 117>
![image](sediment://61c01ea9be8001b#file_000000005b7c71f7b4b2a32a07acadeb#p_10.4495600110.jpg)
<PARSED TEXT FOR PAGE: 101 / 117>
Grantee Name John A Logan College
ID Numbers Audit:57935 Grantee:673225 UEI:JFLWC7MNURM5 FEIN:370905504
Audit Period 7/1/2024 12:00:00 AM - 6/30/2025 12:00:00 AM
Last Update 1/6/2026 1:58:26 PM
Program Count 6
EXPENDITURES BY PROGRAM
CSFA # Program Name State Federal Total Match
684-01-1625 Adult Education and Literacy Basic Grants -
Federal and State
142,034.00 69,597.00 211,631.00 0.00
444-84-2884 Child Care Resource and Referral Program - Child
Care Assistance Program
435,482.21 1,346,919.42 1,782,401.63 0.00
420-35-3071 Energy Transition Community Grant Program 272,769.00 0.00 272,769.00 0.00
601-00-1591 Nurse Educator Fellowship Program 10,000.00 0.00 10,000.00 0.00
684-00-0465 Postsecondary Perkins Basic Grants - Federal CTE 0.00 347,414.53 347,414.53 0.00
586-13-0542 Truants' Alternative/Optional Ed 153,867.00 0.00 153,867.00 0.00
All other federal expenditures 8,348,530.05 8,348,530.05
TOTALS 1,014,152.21 10,112,461.00 11,126,613.21 0.00
EXPENDITURES BY CATEGORY
Amount Category
1,081,097.16 Personal Services (Salaries and Wages)
317,767.64 Fringe Benefits
20,903.88 Travel
23,486.36 Equipment
220,318.62 Supplies
20,173.36 Contractual Services
10,000.00 Consultant (Professional Services)
103,200.00 Occupancy - Rent and Utilities
742.36 Telecommunications
1,734.00 Training and Education
140,921.30 Miscellaneous Costs
411,102.48 Indirect Costs
153,867.00 Expenditure-Grant Projects during the Audit Period
272,769.00 Expenditures for all budget lines for DCEO grants
2,778,083.16 TOTAL
Illinois Grant Accountability and Transparency 
Consolidated Year-End Financial Report
Page 1 of 7 01/06/26
<IMAGE FOR PAGE: 101 / 117>
![image](sediment://f5267c6fb79050c#file_000000005b7c71f7b4b2a32a07acadeb#p_11.1244d48448.jpg)
<PARSED TEXT FOR PAGE: 102 / 117>
State Agency Illinois Community College Board
CSFA Number 684-01-1625
Program Name Adult Education and Literacy Basic Grants - Federal and State
Popular Name Adult Education Grant
Program Contact Name:Kathy Olesen-Tracey Phone:2175572740 Email:kathy.olesen-tracey@illinois.gov
State Amount Expended 142034.00
Federal Amount Expended 69597.00
Expenditures by Category
163,910.76 Personal Services (Salaries and Wages)
24,396.15 Fringe Benefits
1,519.46 Travel
14,680.54 Supplies
2,400.00 Occupancy - Rent and Utilities
742.36 Telecommunications
1,529.00 Training and Education
2,452.73 Miscellaneous Costs
211,631.00 TOTAL
Illinois Grant Accountability and Transparency 
Consolidated Year-End Financial Report
Page 2 of 7 01/06/26
<IMAGE FOR PAGE: 102 / 117>
![image](sediment://9f4c5bf01e1b2e5#file_000000005b7c71f7b4b2a32a07acadeb#p_12.f223353cde.jpg)
<PARSED TEXT FOR PAGE: 103 / 117>
State Agency Department Of Human Services
CSFA Number 444-84-2884
Program Name Child Care Resource and Referral Program - Child Care Assistance Program
Popular Name Child Care Resource and Referral Program
Program Contact Name:Hollie Hoole Phone:217/785-2559 Email:Hollie.Hoole@illinois.gov
State Amount Expended 435482.21
Federal Amount Expended 1346919.42
Expenditures by Category
838,324.38 Personal Services (Salaries and Wages)
281,674.11 Fringe Benefits
1,626.73 Travel
5,053.34 Supplies
11,775.00 Contractual Services
10,000.00 Consultant (Professional Services)
100,800.00 Occupancy - Rent and Utilities
138,468.57 Miscellaneous Costs
394,679.50 Indirect Costs
1,782,401.63 TOTAL
Illinois Grant Accountability and Transparency 
Consolidated Year-End Financial Report
Page 3 of 7 01/06/26
<IMAGE FOR PAGE: 103 / 117>
![image](sediment://96c06d93eb7b682#file_000000005b7c71f7b4b2a32a07acadeb#p_13.2c0ff3b6bc.jpg)
<PARSED TEXT FOR PAGE: 104 / 117>
State Agency Department Of Commerce And Economic Opportunity
CSFA Number 420-35-3071
Program Name Energy Transition Community Grant Program
Popular Name Energy Transition Community Grant Program
Program Contact Name:Matthew Swaine Phone:217-720-
5910 Email:CEO.CEJACommTransition@illinois.gov
State Amount Expended 272769.00
Federal Amount Expended 0.00
Expenditures by Category
272,769.00 Expenditures for all budget lines for DCEO grants
272,769.00 TOTAL
Illinois Grant Accountability and Transparency 
Consolidated Year-End Financial Report
Page 4 of 7 01/06/26
<PARSED TEXT FOR PAGE: 105 / 117>
State Agency Board Of Higher Education
CSFA Number 601-00-1591
Program Name Nurse Educator Fellowship Program
Popular Name Nurse Educator Fellowship Program
Program Contact Name:Brook Stewart Phone:217-866-1473 Email:stewart@ibhe.org
State Amount Expended 10000.00
Federal Amount Expended 0.00
Expenditures by Category
8,729.01 Personal Services (Salaries and Wages)
1,270.99 Fringe Benefits
10,000.00 TOTAL
Illinois Grant Accountability and Transparency 
Consolidated Year-End Financial Report
Page 5 of 7 01/06/26
<PARSED TEXT FOR PAGE: 106 / 117>
State Agency Illinois Community College Board
CSFA Number 684-00-0465
Program Name Postsecondary Perkins Basic Grants - Federal CTE
Popular Name Perkins Grant
Program Contact Name:Janelle Washington Phone:217-785-0068 Email:janelle.washington@illinois.gov
State Amount Expended 0.00
Federal Amount Expended 347414.53
Expenditures by Category
70,133.01 Personal Services (Salaries and Wages)
10,426.39 Fringe Benefits
17,757.69 Travel
23,486.36 Equipment
200,584.74 Supplies
8,398.36 Contractual Services
205.00 Training and Education
16,422.98 Indirect Costs
347,414.53 TOTAL
Illinois Grant Accountability and Transparency 
Consolidated Year-End Financial Report
Page 6 of 7 01/06/26
<IMAGE FOR PAGE: 106 / 117>
![image](sediment://25c0ae8cf6276f4#file_000000005b7c71f7b4b2a32a07acadeb#p_14.b8b1def6a0.jpg)
<PARSED TEXT FOR PAGE: 107 / 117>
State Agency State Board Of Education
CSFA Number 586-13-0542
Program Name Truants' Alternative/Optional Ed
This program was added by the grantee
Popular Name Truants' Alternative and Optional Education Program (TAOEP); Truants'
Alternative/Optional Ed
Program Contact Name:Brian Houser Phone:217-782-5270 Email:bhouser@isbe.net
State Amount Expended 153867.00
Federal Amount Expended 0.00
Expenditures by Category
153,867.00 Expenditure-Grant Projects during the Audit Period
153,867.00 TOTAL
Illinois Grant Accountability and Transparency 
Consolidated Year-End Financial Report
Page 7 of 7 01/06/26
<PARSED TEXT FOR PAGE: 108 / 117>
FEDERAL COMPLIANCE SECTION
<PARSED TEXT FOR PAGE: 109 / 117>
INDEPENDENT AUDITOR'S REPORT ON COMPLIANCE 
FOR EACH MAJOR FEDERAL PROGRAM AND ON INTERNAL CONTROL OVER 
COMPLIANCE REQUIRED BY THE UNIFORM GUIDANCE
To the Board of Trustees
John A. Logan College
Community College District No. 530
Carterville, Illinois 62918
Report on Compliance for Each Major Federal Program
Opinion on Each Major Federal Program
We have audited John A. Logan College, Community College District No. 530’s (the College) 
compliance with the types of compliance requirements identified as subject to audit in the OMB 
Compliance Supplement that could have a direct and material effect on each of the College’s major 
federal programs for the year ended June 30, 2025. The College’s major federal programs are identified 
in the summary of auditor’s results section of the accompanying schedule of findings and questioned 
costs. 
In our opinion, the College complied, in all material respects, with the compliance requirements referred 
to above that could have a direct and material effect on each of its major federal programs for the year 
ended June 30, 2025. 
Basis for Opinion on Each Major Federal Program
We conducted our audit of compliance in accordance with auditing standards generally accepted in the 
United States of America; the standards applicable to financial audits contained in Government Auditing 
Standards issued by the Comptroller General of the United States; and the audit requirements of Title 2 
U.S. Code of Federal Regulations Part 200, Uniform Administrative Requirements, Cost Principles, and 
Audit Requirements for Federal Awards (Uniform Guidance). Our responsibilities under those standards 
and the Uniform Guidance are further described in the Auditor’s Responsibilities for the Audit of 
Compliance section of our report.
We are required to be independent of the College and to meet our other ethical responsibilities, in 
accordance with relevant ethical requirements relating to our audit. We believe that the audit evidence we 
have obtained is sufficient and appropriate to provide a basis for our opinion on compliance for each 
major federal program. Our audit does not provide a legal determination of the College’s compliance with 
the compliance requirements referred to above.
Responsibilities of Management for Compliance
Management is responsible for compliance with the requirements referred to above and for the design, 
implementation, and maintenance of effective internal control over compliance with the requirements of 
laws, statutes, regulations, rules, and provisions of contracts or grant agreements applicable to the 
College’s federal programs.
83
 3401 Professional Park Drive ▪ Marion, IL 62959 
Phone: (618) 997-3055 Fax: (618) 997-5121 kempercpa.com
~~t41KEMPER 
.i:iiCPA GROUPLLP 
Certified Public Accountants and Consultants 
<IMAGE FOR PAGE: 109 / 117>
![image](sediment://6fef78dd210e765#file_000000005b7c71f7b4b2a32a07acadeb#p_15.3bd0b6713c.jpg)
<PARSED TEXT FOR PAGE: 110 / 117>
Auditor’s Responsibilities for the Audit of Compliance
Our objectives are to obtain reasonable assurance about whether material noncompliance with the 
compliance requirements referred to above occurred, whether due to fraud or error, and express an 
opinion on the College’s compliance based on our audit. Reasonable assurance is a high level of 
assurance but is not absolute assurance and therefore is not a guarantee that an audit conducted in 
accordance with generally accepted auditing standards, Government Auditing Standards, and the Uniform 
Guidance will always detect material noncompliance when it exists. The risk of not detecting material 
noncompliance resulting from fraud is higher than for that resulting from error, as fraud may involve 
collusion, forgery, intentional omissions, misrepresentations, or the override of internal control. 
Noncompliance with the compliance requirements referred to above is considered material if there is a 
substantial likelihood that, individually or in the aggregate, it would influence the judgment made by a 
reasonable user of the report on compliance about the College’s compliance with the requirements of each 
major federal program as a whole.
In performing an audit in accordance with generally accepted auditing standards, Government Auditing 
Standards, and the Uniform Guidance, we:
• Exercise professional judgment and maintain professional skepticism throughout the audit.
• Identify and assess the risks of material noncompliance, whether due to fraud or error, and design 
and perform audit procedures responsive to those risks. Such procedures include examining, on a 
test basis, evidence regarding the College’s compliance with the compliance requirements 
referred to above and performing such other procedures as we considered necessary in the 
circumstances.
• Obtain an understanding of the College’s internal control over compliance relevant to the audit in 
order to design audit procedures that are appropriate in the circumstances and to test and report on 
internal control over compliance in accordance with the Uniform Guidance, but not for the 
purpose of expressing an opinion on the effectiveness of the College’s internal control over 
compliance. Accordingly, no such opinion is expressed.
We are required to communicate with those charged with governance regarding, among other matters, the 
planned scope and timing of the audit and any significant deficiencies and material weaknesses in internal 
control over compliance that we identified during the audit.
Report on Internal Control Over Compliance
A deficiency in internal control over compliance exists when the design or operation of a control over 
compliance does not allow management or employees, in the normal course of performing their assigned 
functions, to prevent, or detect and correct, noncompliance with a type of compliance requirement of a 
federal program on a timely basis. A material weakness in internal control over compliance is a 
deficiency, or combination of deficiencies, in internal control over compliance, such that there is a 
reasonable possibility that material noncompliance with a type of compliance requirement of a federal 
program will not be prevented, or detected and corrected, on a timely basis. A significant deficiency in 
internal control over compliance is a deficiency, or a combination of deficiencies, in internal control over 
compliance with a type of compliance requirement of a federal program that is less severe than a material 
weakness in internal control over compliance, yet important enough to merit attention by those charged 
with governance. 
84
<PARSED TEXT FOR PAGE: 111 / 117>
Our consideration of internal control over compliance was for the limited purpose described in the 
Auditor’s Responsibilities for the Audit of Compliance section above and was not designed to identify all 
deficiencies in internal control over compliance that might be material weaknesses or significant 
deficiencies in internal control over compliance. Given these limitations, during our audit we did not 
identify any deficiencies in internal control over compliance that we consider to be material weaknesses, 
as defined above. However, material weaknesses or significant deficiencies in internal control over 
compliance may exist that were not identified. 
Our audit was not designed for the purpose of expressing an opinion on the effectiveness of internal 
control over compliance. Accordingly, no such opinion is expressed.
The purpose of this report on internal control over compliance is solely to describe the scope of our 
testing of internal control over compliance and the results of that testing based on the requirements of the 
Uniform Guidance. Accordingly, this report is not suitable for any other purpose.
KEMPER CPA GROUP LLP
Certified Public Accountants and Consultants
Marion, Illinois
February 19, 2026
85
<PARSED TEXT FOR PAGE: 112 / 117>
Assistance Contract or
Listing Pass-Through
Number Identifying Number
U.S. Department of Education
Direct Grant
TRIO Cluster
TRIO Student Support Services 84.042A P042A200753-23 $ - $ 44,833
TRIO Student Support Services 84.042A P042A200753-24 - 297,892
Total TRIO Cluster - 342,725
Student Financial Assistance Cluster
Federal Pell Grant Program (M) 84.063 P063P230542 - 526,896
Federal Pell Grant Program (M) 84.063 P063P240542 - 6,836,931
Federal Supplemental Educational Opportunity Grants (M) 84.007 P007A231184 - 7,357
Federal Supplemental Educational Opportunity Grants (M) 84.007 P007A241184 - 120,413
Federal Work-Study Program (M) 84.033 P033A231184 - 8,526
Federal Work-Study Program (M) 84.033 P033A241184 108,567
Total Student Financial Assistance Cluster - 7,608,690
Adult Education - Basic Grants to States 84.002 AE-53001-25 - 69,597
Career and Technical Education - Basic Grants to States 84.048 CTE-530-25 - 347,415
Total U.S. Department of Education - 8,368,427
U.S. Department of Labor
Passed through Parkland College
Strengthening Community Colleges Training Grant 17.261 CC-38940-22-60-A-17 - 107,122
Total U.S. Department of Labor - 107,122
U.S. Department of Health and Human Services
Direct Grant
Congressional Directives 93.493 6 CE1HS53756-01-03 - 4,533
Passed through the Illinois Department of Human Services:
Child Care and Development Fund Cluster
Child Care Mandatory and Matching Funds of the Child Care
 and Development Fund 93.596 FCSDI04632 - 1,346,919
Total Child Care and Development Fund Cluster - 1,346,919
Passed through Southern Illinois University Carbondale
Biomedical Research and Research Training 93.859 SIUC 20-02 - 328
Total U.S. Department of Health and Human Services - 1,351,780
U.S. Department of Veterans Affairs
Direct Grant
Post-9/11 Veterans Education Assistance - GI Bill Chapter 33 64.028 N/A - 106,416
Total U.S. Department of Veterans Affairs - 106,416
U.S. Department of Commerce
Direct Grant
Economic Development Cluster
Investments for Public Works and Economic Development Facilities 11.300 06-01-06399 - 178,716
Total Economic Development Cluster - 178,716
Total U.S. Department of Commerce - 178,716
Total Federal Awards $ - $ 10,112,461
Federal Grantor/Pass-Through Grant/Program or Cluster Title Expenditures
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
SCHEDULE OF EXPENDITURES OF FEDERAL AWARDS
FOR THE YEAR ENDED JUNE 30, 2025
Provided to Federal
Subrecipients
The accompanying notes are an integral part of this schedule.
 86
<PARSED TEXT FOR PAGE: 113 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
NOTES TO THE SCHEDULE OF EXPENDITURES OF FEDERAL AWARDS
FOR THE YEAR ENDED JUNE 30, 2025
NOTE 1: BASIS OF PRESENTATION
A. General
The accompanying Schedule of Expenditures of Federal Awards (the Schedule) includes the federal 
award activity of John A. Logan College, Community College District No. 530 (the College) under
programs of the federal government for the year ended June 30, 2025. The information in this Schedule is 
presented in accordance with the requirements of Title I U.S. Code of Federal Regulation (CFR) Part 200, 
Uniform Administrative Requirements, Cost Principles, and Audit Requirements for Federal Awards 
(Uniform Guidance). Because the Schedule presents only a selected portion of the operations of the 
College, it is not intended to and does not present the financial position, changes in net position, or cash 
flows of the College. 
B. Basis of Accounting
Expenditures reported on the Schedule are reported on the accrual basis of accounting. Such expenditures 
are recognized following the cost principles contained in the Uniform Guidance, wherein certain types of 
expenditures are not allowable or limited as to reimbursements. 
NOTE 2: SUBRECIPIENTS
No federal awards were provided to subrecipients for the year ended June 30, 2025 as detailed on the 
Schedule.
NOTE 3: NONCASH AWARDS
There were no noncash awards reported on the Schedule for the year ended June 30, 2025.
NOTE 4: LOANS OR LOAN GUARANTEES OUTSTANDING
There were no loan programs for the year ended June 30, 2025.
NOTE 5: INDIRECT COST RATE
The College has a plan for allocation of common and indirect costs related to grant programs in 
accordance with the Uniform Guidance. The indirect cost rate used to allocate amounts to grant programs 
during the fiscal year ended June 30, 2025, is primarily based on a federally negotiated higher education 
rate agreement. The College has elected not to use the 10% de Minimis indirect cost rate. 
87
<PARSED TEXT FOR PAGE: 114 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
SCHEDULE OF FINDINGS AND QUESTIONED COSTS
FOR THE YEAR ENDED JUNE 30, 2025
SECTION I – SUMMARY OF AUDITOR’S RESULTS
Financial Statements
1. Type of auditor’s report issued: Unmodified
2. Internal control over financial reporting:
a.) Material weaknesses identified? No
b.) Significant deficiencies identified that are not considered
to be material weaknesses? None Reported
c.) Noncompliance material to the financial statements noted? No
Federal Awards
1. Internal control over major program:
a.) Material weaknesses identified? No
b.) Significant deficiencies identified that are not considered 
to be material weaknesses? None Reported
2. Type of auditor’s report issued on compliance for major programs: Unmodified
3. Any audit findings disclosed that are required to be reported in
accordance with section 510 (a) of the Uniform Guidance? No
4. Identification of major programs:
CFDA Number Name of Federal Program
Student Financial Assistance Cluster:
84.007 Federal Supplemental Educational Opportunity Grants
84.033 Federal Work-Study Program
84.063 Federal Pell Grant Program
5. Dollar threshold used to distinguish between Type A and Type B programs: $750,000
6. Auditee qualified as a low-risk auditee? Yes
88
<PARSED TEXT FOR PAGE: 115 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
SCHEDULE OF FINDINGS AND QUESTIONED COSTS (CONTINUED)
FOR THE YEAR ENDED JUNE 30, 2025
SECTION II – FINANCIAL STATEMENT FINDINGS
None Reported
89
<PARSED TEXT FOR PAGE: 116 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
SCHEDULE OF FINDINGS AND QUESTIONED COSTS (CONTINUED)
FOR THE YEAR ENDED JUNE 30, 2025
SECTION III – FEDERAL AWARD FINDINGS AND QUESTIONED COSTS
None Reported
90
<PARSED TEXT FOR PAGE: 117 / 117>
JOHN A. LOGAN COLLEGE
COMMUNITY COLLEGE DISTRICT NO. 530
CARTERVILLE, ILLINOIS
SUMMARY SCHEDULE OF PRIOR AUDIT FINDINGS 
FOR THE YEAR ENDED JUNE 30, 2025
Finding No. Condition Current Status
2024-001 During the compliance testing of “Special Tests and Not Repeated
Provisions” requirements related to Enrollment Reporting, 
we noted the following exceptions: Two (2) students
were not reported to the Clearinghouse after withdrawing
from the institution. 
91

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes — this report is useful, and it also shows exactly why **“Tagged PDF: Passed” does not mean “actually accessible PDF.”**

## What the report is really saying

This file already has **some accessibility scaffolding**:

- accessibility permission flag passed
- image-only PDF passed
- tagged PDF passed
- primary language passed
- character encoding passed
- scripts/timed responses/flicker passed

But the document is still **materially broken in several important ways**:

- title is not showing in the title bar
- bookmarks are missing
- not all page content is tagged
- not all annotations are tagged
- figures need alt text
- other elements need alt text
- tables lack headers
- tables are structurally irregular
- heading nesting is wrong
- reading order still needs manual check
- color contrast still needs manual check

That combination means: **the file has a tag tree, but the semantics are incomplete and inconsistent.**

## Does that fit the actual PDF?

Yes.

This is a **117-page annual financial report** with a real table of contents near the front, lots of long financial tables, repeated report pages, logos, charts, schedules, and government/audit appendices. That is exactly the kind of PDF where a basic tag pass can exist while the file is still accessibility-fragile. The document starts with a cover page, then a table of contents on pages 2–4, then many long statement/note/schedule sections and multiple table-heavy pages later in the file. fileciteturn2file0

## What the failures most likely mean in this specific file

### 1. **Bookmarks failed**

That failure makes sense. This is a long document with a real table of contents on pages 2–4, so the absence of a corresponding bookmark outline is a real usability loss in a 117-page report. fileciteturn2file0

### 2. **Tagged content failed**

Also believable. “Tagged PDF: Passed” only means a tag structure exists somewhere. “All page content is tagged” failing usually means some visible content is left untagged or artifacting is inconsistent.

In this file, likely candidates include:

- decorative but visible cover elements on page 1
- repeated logo/header/footer material on report pages like 5, 8, 86, 93, and 100
- page-number/footer/header debris
- chart labels or chart graphics on page 15
- image-only table/schedule pages like page 75 and page 77, where the rendered page clearly shows structured tabular material that may not map cleanly into the semantic layer fileciteturn2file0

### 3. **Tagged annotations failed**

Also plausible. This report includes URLs, email addresses, and likely link annotations in several places, including visible contact info on report pages and grant-contact pages in the later section. Those annotations may exist visually or functionally but not be correctly nested/tagged in the structure tree. fileciteturn2file0

### 4. **Figures alternate text failed / other elements alternate text failed**

That absolutely tracks.

The document includes at least:

- logos and branded graphics
- pie charts on page 15
- image-rendered schedule/certification pages like page 75 and page 77
- other graphic/table-like rendered pages later in the file

The **pie charts on page 15** are especially obvious candidates for meaningful alternative text, because they communicate actual financial information, not decoration. fileciteturn2file0

### 5. **Tables failed: headers and regularity**

This is one of the strongest and most believable findings.

This file has many dense financial tables and schedules, including:

- Statement of Net Position on pages 20–21
- Statement of Revenues, Expenses, and Changes in Net Position on page 22
- Cash Flows on page 23
- pension/OPEB schedules on pages 67–69
- large multi-column schedules on pages 73–84 and later federal schedules around pages 112 onward

These are exactly the kinds of tables that often look fine visually but fail semantic header association, cell regularity, or both. fileciteturn2file0

### 6. **Appropriate nesting failed**

Also believable.

This report has many layered section transitions:

- cover
- table of contents
- independent auditor reports
- management discussion and analysis
- basic statements
- notes
- required supplementary information
- other supplemental information
- compliance sections
- schedules and appendices

That kind of structure often produces heading/tag nesting problems if the authoring/export path was inconsistent across sections or if tags were repaired after export. fileciteturn2file0

### 7. **Logical reading order needs manual check**

That is the right manual flag.

The highest-risk pages for reading-order trouble are probably:

- the cover page
- the table of contents pages
- chart pages like page 15
- image-heavy or rendered schedule pages like page 75 and page 77
- any page with multi-column or visually grouped financial content fileciteturn2file0

### 8. **Color contrast needs manual check**

Also sensible.

The biggest likely contrast-risk areas are:

- the dark/gold cover design on page 1
- chart labels/colors on page 15
- any faint gray linework or thin rule text in schedules/images later in the file fileciteturn2file0

## The practical severity order

If I were triaging this file, I would prioritize fixes in this order:

1. **Tables**
2. **Heading nesting**
3. **All page content tagged**
4. **Tagged annotations**
5. **Alt text for informative figures and non-text elements**
6. **Bookmarks**
7. **Title shown in title bar**
8. **Manual reading-order review**
9. **Manual contrast review**

Why that order:

- tables, headings, content tagging, and annotation tagging affect core navigability and comprehension
- bookmarks and title are easier wins
- reading order and contrast still need human review even after structural fixes

## What this means for your pipeline

For your manifest/workflow, this file would almost certainly produce something like:

- `tagged_pdf_detected: true`
- `struct_tree_detected: true`
- `image_only_pages_present: false`
- `reading_order_source: mixed` or `tag_tree`
- `document_warning_entries` including:
  - `BOOKMARKS_MISSING`
  - `TITLE_BAR_NOT_SET`
  - `UNTAGGED_PAGE_CONTENT_PRESENT`
  - `UNTAGGED_ANNOTATIONS_PRESENT`
  - `FIGURE_ALT_TEXT_MISSING`
  - `NONFIGURE_ALT_TEXT_MISSING`
  - `TABLE_HEADERS_MISSING`
  - `TABLE_STRUCTURE_IRREGULAR`
  - `HEADING_NESTING_INVALID`
  - `READING_ORDER_MANUAL_CHECK`
  - `COLOR_CONTRAST_MANUAL_CHECK`

That is a good example of why your manifest needs to separate:

- what the file structurally has
- what the checker flags
- what still requires human review

## Bottom line

This report does **not** say the file is close to done.

It says the file is:

- **not image-only**
- **already tagged in some form**
- but still **semantically incomplete enough that real accessibility is not yet trustworthy**

That is a much more useful reading than “it mostly passed.”

If you want, the next useful step is for me to turn this exact report into a **document-level and page-level warning set** in your manifest vocabulary.


#### You:
But how would ourplanned code tkae something like this pdf and turn it into something normalized I can work with?

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
Yes. The code would do it by **reducing the PDF into evidence, then into normalized blocks, then into reviewable structure**.

Not by “figuring out the whole PDF out in one shot.”

## The actual mechanism

For a file like `finreport25.pdf`, the pipeline would be:

1. **Read the PDF as evidence**
2. **Create raw page/block records**
3. **Assign provisional semantic roles**
4. **Merge those into normalized units**
5. **Attach uncertainty and accessibility flags**
6. **Give you a manifest full of blocks you can actually work with**

That matches the manifest spine you already built: source evidence, normalized workflow, warnings, projected target. fileciteturn1file0 fileciteturn1file1

---

## What “normalized” means here

It means the code stops treating the file as:

- characters
- spans
- bounding boxes
- PDF objects
- page operators

and starts treating it as:

- heading
- paragraph
- table
- table row
- table cell
- figure
- caption
- note
- link
- artifact
- unknown

with:

- page span
- reading-order index
- confidence
- evidence basis
- manual-review flags

That is exactly what your `normalized_block_entries` and `normalized_workflow` are for. fileciteturn1file0 fileciteturn1file1

---

## How it would work on **this specific PDF**

This file is a good test case because it has several different content types:

- cover page
- table of contents
- narrative audit reports
- management discussion
- dense financial statement tables
- chart page
- schedule pages
- some visually rendered/image-heavy pages later in the document

You can see all of those in the parsed PDF itself:

- cover page on page 1
- table of contents on pages 2–4
- auditor report pages starting on page 5
- management discussion starting page 11
- pie charts on page 15
- statement tables on pages 20–23
- schedule/image-heavy pages like page 75 and page 77 fileciteturn2file0

---

## Step 1: extract **raw evidence**

The code would first produce **page-level** and **raw block-level** evidence, not semantic conclusions.

### Document-level evidence

Populate things like:

- page count
- metadata
- whether tags seem present
- whether a structure tree seems present
- outline/bookmark presence
- language
- permissions
- forms/JavaScript/XFA presence if any

This goes into:

- `source_package`
- `document_metadata`
- `document_accessibility`
- `document_navigation`
- `document_security`
- `document_interactivity` fileciteturn1file0 fileciteturn1file1

### Page-level evidence

For each page, store:

- page number
- page geometry
- text layer present or not
- image-only suspicion
- annotation count
- form field count
- raw content-stream evidence if available
- page-level warnings

This goes into:

- `page_entries[].observed_source`
- `page_entries[].annotation_entries`
- `page_entries[].warning_entries` fileciteturn1file0 fileciteturn1file1

### Raw block-level evidence

For each detected text/image block, store:

- page number
- bbox
- extracted text
- text spans
- font/size/style hints
- structure hints
- source references
- role basis evidence
- manual review flag if already suspicious

This goes into:

- `raw_block_entries` fileciteturn1file0 fileciteturn1file1

---

## Step 2: classify pages into broad page types

Before block normalization, I would run a **page classifier**.

For this PDF, it would probably label pages like this:

- **page 1** → `cover`
- **pages 2–4** → `table_of_contents`
- **pages 5–9** → `narrative_report`
- **pages 11–18** → `management_discussion`
- **pages 20–23** → `financial_statement_table`
- **page 15** → `chart_page`
- **pages 67–69** → `schedule_table`
- **page 75** → `image_or_rendered_page`
- **pages 101–107** → `grant_report_table_pages` fileciteturn2file0

That classification is not the final semantic output. It just helps the normalizer choose the right rules.

---

## Step 3: normalize blocks page by page

This is the real answer to your question.

The code would **not** try to normalize the whole PDF globally first. It would normalize **page by page**, then stitch the pages together into document order.

### Example: page 5

Page 5 has:

- report title: **INDEPENDENT AUDITOR’S REPORT**
- addressee block
- section heading: **Report on the Audit of the Financial Statements**
- subheading: **Opinions**
- paragraph text
- visual logo/header/footer material fileciteturn2file0

The raw extractor might give you many separate spans/blocks.

The normalizer would turn that into something like:

```json id="page5-normalized"
[
  {
    "interpreted_role": "heading",
    "heading_level": 1,
    "text": "INDEPENDENT AUDITOR’S REPORT",
    "role_confidence": "high",
    "reading_order_index": 1,
    "role_basis": ["all_caps_heading", "font_size_outlier", "top_of_page", "centered_title"]
  },
  {
    "interpreted_role": "paragraph",
    "text": "To the Board of Trustees ... Carterville, Illinois 62918",
    "role_confidence": "high",
    "reading_order_index": 2,
    "role_basis": ["body_block", "left_aligned", "intro_address_block"]
  },
  {
    "interpreted_role": "heading",
    "heading_level": 2,
    "text": "Report on the Audit of the Financial Statements",
    "role_confidence": "high",
    "reading_order_index": 3,
    "role_basis": ["section_heading_pattern"]
  },
  {
    "interpreted_role": "heading",
    "heading_level": 3,
    "text": "Opinions",
    "role_confidence": "high",
    "reading_order_index": 4,
    "role_basis": ["subheading_pattern", "italic_or_bold_emphasis"]
  },
  {
    "interpreted_role": "paragraph",
    "text": "We have audited the accompanying financial statements ...",
    "role_confidence": "high",
    "reading_order_index": 5,
    "role_basis": ["body_paragraph_sequence"]
  }
]
```

And the logo/footer junk would either become `artifact` or a figure candidate with review flags.

### Example: page 15

Page 15 is a chart page with two pie charts:

- **Revenue by Source**
- **Operating Expenses** fileciteturn2file0

The normalizer should produce:

- narrative paragraph introducing the charts
- figure block for first chart
- figure block for second chart
- likely `manual_review_required: true` because the chart meaning needs text equivalent

Something like:

```json id="page15-normalized"
[
  {
    "interpreted_role": "paragraph",
    "text": "The following are graphic illustrations of total revenue ...",
    "role_confidence": "high"
  },
  {
    "interpreted_role": "figure",
    "text": null,
    "role_confidence": "medium",
    "manual_review_required": true,
    "warning_entries": [
      {
        "warning_code": "FIGURE_DESCRIPTION_REVIEW",
        "warning_scope": "figure"
      }
    ],
    "role_basis": ["chart_graphic_detected", "chart_title:Revenue by Source"]
  },
  {
    "interpreted_role": "figure",
    "text": null,
    "role_confidence": "medium",
    "manual_review_required": true,
    "warning_entries": [
      {
        "warning_code": "FIGURE_DESCRIPTION_REVIEW",
        "warning_scope": "figure"
      }
    ],
    "role_basis": ["chart_graphic_detected", "chart_title:Operating Expenses"]
  }
]
```

### Example: pages 20–23

These are financial statement pages with structured tables:

- Statement of Net Position
- Statement of Revenues, Expenses, and Changes in Net Position
- Statement of Cash Flows fileciteturn2file0

The extractor will likely give many text blocks.

The normalizer should:

1. detect the title of the statement
2. detect that the body is a table
3. recover rows and columns
4. try to infer headers
5. flag uncertainty when headers or regularity are weak

So a page becomes:

- heading block
- table block
- maybe footnote/note block

And the table block can either:

- stay aggregated as one normalized `table` with substructure stored in auxiliary fields, or
- emit `table`, `table_row`, `table_cell` units depending on how granular you want normalization to be

Given your schema already allows `table`, `table_row`, and `table_cell`, I would support the more granular version. fileciteturn1file0turn1file1

### Example: page 75

Page 75 looks like a visually rendered certification page with signatures and sparse text layout. It appears as an image-rendered page in the loaded file. fileciteturn2file0

This is exactly where the code should **not pretend certainty**.

The normalizer should emit something like:

- heading if extractable
- one or more figure/image-rendered page blocks
- `manual_review_required: true`
- maybe `OCR_PAGE_REVIEW`
- maybe `SIGNATURE_REGION_PRESENT`

That is the whole point of the warning layer.

---

## Step 4: assign role confidence and semantic source quality

This is where the pipeline becomes usable.

Each normalized block should carry two different judgments:

### `role_confidence`

How confident are we that this block is really a heading / paragraph / table / figure / note?

### `semantic_source_quality`

How trustworthy is the evidence we used?

Examples:

- A heading directly supported by a tag tree + font size + outline alignment → `high`
- A figure inferred from image bbox and chart title but no alt text → `medium`
- A rendered page that needed OCR or only had image evidence → `low`

Your schema already has both fields, which is good. fileciteturn1file0turn1file1

---

## Step 5: attach review flags

This file’s own accessibility report tells you what some of the obvious document-level review flags should be:

- title not showing in title bar
- bookmarks missing
- logical reading order needs manual check
- color contrast needs manual check
- not all content tagged
- not all annotations tagged
- figures need alternate text
- other elements need alternate text
- tables lack headers
- table regularity problems
- heading nesting problems

So your code would convert those kinds of signals into warning objects attached at the right level:

### document-level

- `BOOKMARKS_MISSING`
- `TITLE_BAR_NOT_SET`
- `READING_ORDER_MANUAL_CHECK`
- `COLOR_CONTRAST_MANUAL_CHECK`

### page-level

- `UNTAGGED_CONTENT_SUSPECTED`
- `ANNOTATION_TAGGING_REVIEW`
- `IMAGE_ONLY_PAGE_SUSPECTED`

### block-level

- `FIGURE_DESCRIPTION_REVIEW`
- `TABLE_HEADERS_UNCERTAIN`
- `HEADING_LEVEL_UNCERTAIN`
- `READING_ORDER_BREAK`
- `OCR_CONFIDENCE_LOW`

That goes into:

- `document_warning_entries`
- `page_entries[].warning_entries`
- `raw_block_entries[].warning_entries`
- `normalized_block_entries[].warning_entries` fileciteturn1file0turn1file1

---

## Step 6: produce something you can actually work with

At the end, you would not work with raw PDF objects.

You would work with a manifest that lets you do things like:

- “show me every heading in order”
- “show me low-confidence blocks”
- “show me all figure candidates needing alt text”
- “show me all tables with uncertain headers”
- “show me pages where reading order was mixed”
- “project only high-confidence narrative blocks to DOCX/PDF”
- “append review-only blocks to an appendix”

That is what “normalized” buys you.

---

## The actual implementation shape

If I were coding this now, I would do:

### `extract_with_pymupdf(pdf_path) -> partial_manifest`

Produces:

- page entries
- raw block entries
- annotation entries
- geometry
- text layer and image-only suspicion

### `enrich_with_pypdf(manifest, pdf_path) -> manifest`

Adds:

- metadata
- outline/bookmarks
- page labels
- named destinations
- permissions

### `enrich_with_pikepdf(manifest, pdf_path) -> manifest`

Adds:

- MarkInfo
- structure-tree detection
- content-stream evidence
- object refs / xref provenance

### `normalize_manifest(manifest) -> manifest`

Does:

- page classification
- block merging
- role assignment
- reading-order indexing
- confidence assignment

### `attach_warning_rules(manifest) -> manifest`

Does:

- document/page/block warnings

Then either:

- `project_to_docx(manifest)`
  or
- `project_to_pdf(manifest)`

---

## The most important design choice

The code should **never** overwrite the raw evidence with the normalized interpretation.

You need both.

That is why the manifest is good:

- `raw_block_entries` preserve what the PDF literally yielded
- `normalized_block_entries` preserve what your code thinks it means fileciteturn1file0turn1file1

That separation is what makes the pipeline trustworthy.

---

## Shortest answer

The code would turn a PDF like this into something normalized by:

1. extracting raw page/block evidence,
2. classifying page types,
3. merging low-level blocks into semantic units,
4. attaching confidence and review flags,
5. storing both the raw evidence and normalized interpretation in the manifest.

So instead of “117 pages of PDF,” you end up with something like:

- 1 document
- 117 page records
- maybe 2,000 raw blocks
- maybe 600 normalized blocks
- each normalized block labeled as heading/paragraph/table/figure/etc.
- each one carrying page span, reading order, confidence, and warnings

That is the usable layer.

If you want, I’ll make this concrete by sketching the exact normalization rules for just **this one file type** — narrative sections, TOC pages, chart pages, and financial table pages.


#### You:
You are ChatGPT.

Your task is to read this entire chat transcript and produce a **continuation handoff for Codex**.

Codex is the receiver of your output.  
You are not Codex.  
You are preparing a transfer document that carries forward the real work already done in this chat so Codex can continue without starting over.

## Purpose

This conversation contains substantial project labor already completed:
- brainstorming
- reasoning
- iterative refinement
- corrections
- partial structures
- rejected approaches
- accepted decisions
- open threads
- unfinished implementation paths

Your job is to turn that accumulated work into a **high-fidelity handoff document for Codex**.

Do not write a generic summary.
Do not flatten the conversation into a neat recap that loses the thinking.
Do not over-focus on the assistant’s wording.
Preserve the user’s reasoning, priorities, corrections, and decision logic above all else.

## What to extract and preserve

Read the chat from start to finish and recover:

### 1. Project context
What the overall project is, what kind of work has been happening, and what stage the work seems to be in.

### 2. User goals
What the user is trying to accomplish, including how those goals became clearer or more precise over time.

### 3. Reasoning that matters
The hard-won thinking that should carry forward:
- why certain approaches were preferred
- why certain approaches failed
- what tradeoffs were identified
- what distinctions the user kept enforcing
- what the user was trying to protect from being lost

### 4. Constraints and non-negotiables
Important requirements, standards, boundaries, style expectations, process rules, and failure modes the next agent must respect.

### 5. Decisions and status
Separate clearly:
- what is settled
- what is tentatively leaning in a direction
- what was explored but not committed
- what was rejected or corrected

### 6. Reusable work
Any frameworks, schemas, draft structures, workflows, terminology decisions, design patterns, or partial outputs worth carrying forward.

### 7. Open threads
What remains unfinished, unresolved, blocked, or likely to be the next continuation point.

## Priority rules

- User messages outweigh assistant messages.
- Repeated user corrections are high-signal and must be preserved.
- Later refinements override earlier assumptions.
- Moments of frustration often mark where fidelity was lost, so pay close attention there.
- Preserve nuance instead of over-compressing.
- Do not invent consensus where none exists.
- Do not silently erase exploratory ideas that may still matter.

## Output format

Write the result as a handoff document using exactly this structure:

## Codex Continuation Handoff

### Project Context
[What this project is and what kind of work this transcript contains.]

### User Goals
[What the user is trying to accomplish.]

### Reasoning That Must Be Preserved
[The important distinctions, tradeoffs, conceptual logic, and iterative refinements that should carry forward.]

### Constraints and Non-Negotiables
[The requirements, preferences, quality standards, and failure modes Codex must respect.]

### Established Decisions
[What appears settled enough to build on.]

### Tentative but Valuable Directions
[Ideas that were developed enough to matter, but were not fully locked.]

### Rejected or Corrected Directions
[Wrong turns, discarded framings, assistant failures, or approaches the user pushed back on.]

### Reusable Assets
[Frameworks, schemas, structures, terminology decisions, workflows, partial drafts, or other material Codex should inherit.]

### Open Threads and Next Actions
[Unfinished work, unresolved questions, pending decisions, and likely next steps.]

### Guidance for Codex
[Brief direct guidance to Codex on how to continue the work without repeating mistakes or restarting settled thinking.]

## Style requirements

- Be detailed.
- Be factual and continuation-oriented.
- Paraphrase instead of quoting unless a precise phrase is essential.
- Preserve the user’s reasoning more than the assistant’s performance.
- Make the output genuinely useful as a cold-start transfer artifact for Codex.
- Do not write a generic executive summary.
- Do not omit tension, correction, ambiguity, or unresolved problems.
- Do not add invented conclusions.

## Success criterion

The final document should let Codex enter the project cold and still understand:
- what the user actually wants
- how that understanding evolved
- what decisions are already made
- what mistakes should not be repeated
- what reusable thinking already exists
- where the work should continue next

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
## Codex Continuation Handoff

### Project Context

This transcript is part of a larger project about **deep, accessibility-aware PDF handling in Python**, with an emphasis on **open-source tools**, **local/self-hosted models where AI is involved**, and **rigorous, semantics-first processing** rather than shallow convenience conversion.

The conversation began broadly with PDF internals, JavaScript vs Python, accessibility layers, and low-level PDF access. It then narrowed into a more concrete architecture problem:

- how to work with PDFs at the **object / content-stream / structure / accessibility** level
- how to build a **Python pipeline**
- how to normalize extracted PDF evidence into something the user can actually work with
- how to use that normalized representation for **PDF → DOCX**
- how that architecture would differ for **PDF → PDF**
- which packages and OCR/document AI models are relevant
- what belongs in code versus what still requires human review

The transcript later became much more concrete because the user uploaded:

- a **field dictionary** for a draft manifest: `pdf_to_docx_accessibility_manifest v0.1` fileciteturn1file0
- a matching **JSON Schema** for that same manifest, explicitly fixed at **v0.1** fileciteturn1file1
- a real test PDF, `finreport25.pdf`, which is a 117-page annual financial report with many distinct page types and accessibility challenges fileciteturn2file0

By the end of the transcript, the project was no longer abstract package comparison. It had become:

- a **manifest-centered pipeline design**
- a **Python-native replacement for a PDF.js-shaped manifest**
- an **implementation plan**
- and a likely next step of actually building the first extractor adapter against the v0.1 manifest.

### User Goals

The user is trying to build a **serious, comprehensive PDF processing system** in Python that can operate at deep PDF levels while preserving or enforcing accessibility-aware structure.

The goals became progressively clearer:

- early on, the user wanted to understand the PDF format at a deep level, including accessibility implications
- then the focus shifted toward **Python specifically**
- then the user clarified that the relevant frame was **creation**, not remediation
- then the user made explicit that they want **deterministic, code-driven control** over accessible output wherever possible
- then the focus broadened to a **pipeline**:
  - input
  - extract
  - interpret / normalize
  - attach review flags
  - project to DOCX
- then the manifest upload anchored the project around a **canonical intermediate representation**
- then the user raised the possibility of **PDF → PDF**
- then the user brought in **OCR / document AI models** as extraction helpers, especially for image/scanned content
- then the user asked how the planned code would take a real PDF like `finreport25.pdf` and turn it into something normalized and workable

The user’s actual target is not “find one magic library.” It is to build a **reliable, inspectable, explicit, accessibility-aware system** where:

- the source evidence is preserved
- the semantic interpretation is explicit
- uncertainty is tracked
- manual review is isolated to the right places
- output projection is driven from normalized structure, not raw PDF fragments

### Reasoning That Must Be Preserved

Several distinctions were hard-won in the transcript and must not be lost.

#### 1. Creation and remediation are different problems

This was the biggest correction in the conversation.

The assistant repeatedly drifted into “repairing arbitrary existing PDFs” and “inferring semantics from appearance,” but the user clarified multiple times that they were talking about **creation-only** for several turns and may never have mentioned remediation at all.

The preserved distinction is:

- **Creation**: semantics are known ahead of time, so tags, reading order, headings, table structure, figure handling, metadata, and related accessibility structure should be **emitted intentionally**
- **Remediation**: semantics must be inferred from a visually authored or partially tagged PDF

For this project, the user’s reasoning strongly favors the **creation / controlled-pipeline** frame whenever discussing what code can control.

#### 2. Lower-level access is valuable because it increases determinism

The user’s position is that lower-level access is useful because it gives exact control over how accessibility-friendly structure is serialized into the PDF.

Important nuance:

- lower-level access does **not** magically solve content-quality questions
- but in a **controlled generation pipeline**, it should absolutely let code control things like:
  - tags
  - structure tree
  - reading order
  - heading roles and levels
  - table/header associations
  - artifacting
  - metadata
  - form-field semantics if relevant

The assistant eventually corrected itself and accepted that for creation, questions like “is this a heading or just bold text?” are the wrong category. That is a remediation/inference question, not a generation question.

The preserved takeaway is:

- **explicit semantic model first**
- then **exact serialization**
- then validation
- then targeted review for the parts that are still content-quality / human-judgment questions

#### 3. Accessibility is not only file mechanics

The user was pushing hard toward exact structural control, and the assistant eventually refined the answer to the correct boundary:

- code can control **most file-level and structure-level accessibility** in a controlled pipeline
- code cannot fully guarantee:
  - whether a title clearly identifies the document
  - whether alt text is actually good
  - whether chart descriptions are sufficient
  - whether instructions are understandable
  - whether some content choice was truly the most accessible representation

This became important when discussing the Matterhorn Protocol’s “human judgment” conditions.

#### 4. The Matterhorn “human judgment” category is partly a validator limitation, not only a generator limitation

The transcript moved into PDF/UA and Matterhorn.

The assistant identified that many of the conditions marked “usually require human judgment” are only human from the perspective of **post hoc validation of the finished PDF file**, not from the perspective of a **controlled generator** that owns:

- the semantic model
- the serializer
- the asset gating rules

This led to an important intermediate result:

- a classification of the human-judgment items into:
  - **fully deterministic in a controlled generator**
  - **deterministic if the generator also owns the relevant content/asset inputs**
  - **still genuinely content-quality / human-review dependent**

This reasoning matters because it underlies the later **generator requirements spec**.

#### 5. There is no single open-source Python package that “does all of it”

The assistant was repeatedly pushed to answer this directly.

The settled answer is:

- **none** of the open-source Python libraries discussed can do **all** of:
  - semantics-first accessible PDF generation
  - direct page authoring
  - low-level PDF object/content-stream control
  - metadata / assembly / helper operations
  - validation

Instead, packages fall into distinct roles.

#### 6. “Semantic document generation” needed a strict definition

The user found the phrase vague, and the assistant eventually pinned it down.

Preserved meaning:

- **Semantic document generation** means generation from **meaning-first input** such as:
  - heading
  - paragraph
  - list
  - table
  - figure
  - caption
  - link
  - decorative artifact

rather than generation from raw page drawing instructions.

The assistant also clarified that:

- semantic generation should lead to **tagged output**
- but “semantic generation” is broader than tags alone

#### 7. The manifest is the project spine

Once the user uploaded the field dictionary and schema, the project moved from conceptual architecture to a much more grounded state.

A major reasoning result is that the manifest already has the correct structural separation:

- what the PDF literally gave us
- what we think it means
- how confident we are
- what output we plan to create

This separation must be preserved. The assistant repeatedly argued that raw extraction evidence should **not** be overwritten by interpretation.

#### 8. The manifest is currently PDF.js-shaped and needs a Python-native patch, not a new version

The user explicitly corrected the assistant when it casually suggested a version bump.

The manifest is still **v0.1**, and the correct task is a **v0.1 patch pass**, not a new version. Both uploaded files explicitly identify the manifest as v0.1. fileciteturn1file0 fileciteturn1file1

The assistant recognized that the manifest should become **extractor-neutral** and **Python-native**, not tied to PDF.js field conventions.

### Constraints and Non-Negotiables

The following were either explicitly stated or repeatedly reinforced by the user.

- **Open-source only** for the Python tooling discussed in this thread.
- User later also asked specifically about **local AI models**, which means OCR/document AI tools should have local/self-hosted execution paths, not require hosted APIs.
- Stay in the **creation-only frame** unless the user explicitly reopens remediation.
- Do **not** answer with vague “closest” language without concrete capability mapping.
- Do **not** give generalized package surveys when the user is asking for exact job-to-package mapping.
- Do **not** smuggle irrelevant categories back in. A notable example: the assistant kept bringing up forms when the user had not asked about forms, and the user explicitly corrected that.
- Use **full words**, not letter legends, in matrices. The user explicitly rejected shorthand like single-letter status codes.
- Preserve the distinction between:
  - raw extraction evidence
  - normalized interpretation
  - review flags
  - projected output
- Keep the manifest at **v0.1** unless the user explicitly decides otherwise.
- Do **not** build the schema around one extractor’s worldview, especially not PDF.js.
- User repeatedly wants direct answers that make it possible to tell **what can be used for what** without interpretive fog.
- User values **comprehensiveness and deep planning** and is digging down to:
  - PDF objects
  - content streams
  - structure/tags
  - Matterhorn-level accessibility logic
- When discussing OCR and AI models, the relevant criterion is not just “does it OCR,” but:
  - local run path
  - where it fits in the pipeline
  - whether it is appropriate for born-digital PDFs versus scanned/image PDFs

### Established Decisions

These appear settled enough to build on.

#### 1. No single package does the whole job

This is settled.

#### 2. Package role split

The clearest package-role mapping established in the transcript is:

- **WeasyPrint** = semantic document generator
- **PyMuPDF** = direct page author / manipulator
- **pikepdf** = low-level PDF internals / “PDF plumbing”
- **pypdf** = writer/helper/assembly/document-level metadata and navigation work
- **veraPDF** = validator
- **pdfplumber** = extraction/debugging support only
- **pdfminer.six** = extraction / text-layout support only
- **OCRmyPDF** = OCR support only

This role map was one of the stronger corrections away from vague “closest” language.

#### 3. Manifest-centered architecture

The project should be built around the uploaded **v0.1 manifest** as the canonical intermediate representation. fileciteturn1file0 fileciteturn1file1

#### 4. Python-native, extractor-neutral v0.1 patch

The manifest should keep the same spine but patch the PDF.js-shaped evidence fields.

The explicit proposed replacements were:

- `text_items` → `text_spans`
- `operator_evidence` → `content_stream_evidence`
- `viewport` → `page_geometry`
- `operator_list_present` → `content_stream_parsed`

The assistant also proposed adding:

- extractor provenance
- per-extractor evidence namespaces
- stable object references / xref / content stream refs where available

#### 5. Adapter implementation order

This was explicitly settled:

1. **PyMuPDF first**
2. **pypdf second**
3. **pikepdf third**
4. **pdfminer.six fourth**

The reasoning was:

- PyMuPDF gives the broadest useful first-pass coverage for page evidence and raw blocks
- pypdf cleanly owns metadata/navigation/security
- pikepdf owns deeper structure/object/content-stream evidence
- pdfminer.six refines text spans, font/style evidence, and normalization heuristics

#### 6. PyMuPDF should be the first extractor adapter implemented

This was directly answered and confirmed by the user.

#### 7. Output architecture for PDF → DOCX

The project should use:

- extraction evidence
- normalized semantic model
- review flags
- DOCX projection

rather than trying to project directly from raw PDF extraction output to DOCX.

#### 8. OCR/document AI belongs in a conditional extraction branch

For born-digital PDFs, parse native PDF content first.

For scanned/image-heavy PDFs, OCR/document AI models can be inserted into the extraction stage.

This is established and aligned with the uploaded accessibility guidance.

### Tentative but Valuable Directions

These were developed enough to matter, but are not fully locked.

#### 1. Two output families

The transcript developed both:

- **PDF → DOCX**
- **PDF → PDF**

The common architecture is:

- input
- extract
- interpret / normalize
- attach review flags
- project to target format

For PDF → PDF, the assistant proposed three modes:

- patch the existing PDF
- rebuild a new PDF from the normalized model
- hybrid rebuild + low-level patch

The favored direction for the user’s goals was the **hybrid semantic rebuild + patch + validate** path, but this was not locked as final.

#### 2. Generator requirements spec from Matterhorn

A substantial generator requirements spec was drafted in prose, based on the classification of the “human judgment” PDF/UA conditions that become deterministic in a controlled generator.

This included:

- system assumptions
- source-model fields
- serialization rules
- asset/content gates
- build-time rejection rules
- validation gates
- coverage mapping for deterministic conditions

This is clearly valuable and likely reusable, but it was not turned into code or a finalized artifact in the transcript.

#### 3. OCR/document AI model shortlist

The assistant identified these as the most relevant local/open-source model/toolkit options:

- **PaddleOCR**
- **Surya**
- **olmOCR**
- **Nougat**
- **docTR**
- **GOT-OCR 2.0**
- plus **EasyOCR**, **keras-ocr**, **TrOCR** in a broader OCR context

The strongest shortlist for the user’s pipeline seemed to be:

- PaddleOCR
- Surya
- olmOCR

but the exact adoption decision was not locked.

#### 4. Page-type classification before normalization

The assistant proposed classifying pages into coarse page types before block normalization, using `finreport25.pdf` as an example:

- cover
- table\_of\_contents
- narrative\_report
- management\_discussion
- financial\_statement\_table
- chart\_page
- image\_or\_rendered\_page
- grant\_report\_table\_pages

This is a good direction and likely useful in implementation, but it remains conceptual.

#### 5. Use of comments and appendices in DOCX output

The assistant proposed using `python-docx` comments and warning appendices for review-facing DOCX projection. This fits the manifest design but was not deeply discussed beyond proposal level.

### Rejected or Corrected Directions

This section matters a lot because the user repeatedly corrected the assistant.

#### 1. Repeated drift into remediation/inference

This is the most important failure mode to avoid. The user explicitly called out that they had been talking about **creation only** and the assistant kept answering as if the task were remediation or inference from arbitrary PDFs.

Do not repeat that.

#### 2. Claims that code could not know things that are known in a controlled generator

The assistant gave a bad example suggesting that deciding whether something is a real heading or just big bold text is not something code can fully handle. The user directly objected, correctly pointing out that in a creation pipeline this should absolutely be identifiable by code.

That correction is essential:

- in **creation**, semantics should be explicit and serialized intentionally
- questions like “is this really a heading?” belong to remediation/inference, not generation

#### 3. Vague “closest” package answers

The user explicitly rejected answers framed in terms of “closest” without enough concrete information to determine what each package can actually do.

Avoid capability blur. Use direct job-to-package mapping and explicit yes/no/limited distinctions.

#### 4. Overly vague “semantic generation” language

The user reacted negatively to vagueness around “semantic document generation.” The assistant eventually pinned it down, but the important correction is: define terms precisely and operationally.

#### 5. Casual version bump to v0.2

The user corrected the assistant when it tried to treat the Python-native patch as a new version. The manifest is still v0.1.

#### 6. Bringing in forms when not asked

The user explicitly objected that they had not asked about forms. Forms are not forbidden as a topic, but do not expand scope casually.

#### 7. Generalized answers instead of direct answers

The user explicitly said the assistant was answering in generalized ways instead of directly answering what was asked. This is a core failure mode. Codex should answer concretely and with direct mapping to implementation decisions.

### Reusable Assets

These should be inherited, not recreated from scratch.

#### 1. Uploaded manifest field dictionary

`pdf_to_docx_accessibility_manifest v0.1` human-readable dictionary. This is the clearest articulation of the current intended manifest spine and field meanings. fileciteturn1file0

#### 2. Uploaded v0.1 JSON Schema

This is the current machine-readable schema contract for the manifest. fileciteturn1file1

#### 3. Proposed Python-native v0.1 patch direction

Not yet formalized, but explicitly developed:

- keep the top-level manifest spine
- rename PDF.js-shaped fields
- add extractor provenance
- add per-extractor evidence namespaces
- add low-level object/content-stream traceability fields

#### 4. Field ownership map by package

The assistant produced a field-by-field ownership map for:

- what PyMuPDF should populate first-pass
- what should be deferred to pypdf
- what should be deferred to pikepdf
- what should be refined with pdfminer.six

This is highly reusable for implementation planning.

#### 5. Implementation architecture

A concrete repository/module layout was proposed, including:

- `manifest/`
- `extractors/`
- `normalize/`
- `review/`
- `projectors/`
- typed builder / validator
- adapter pattern
- CLI entry point

This is not locked, but it is reusable.

#### 6. Normalization framing

A normalized IR concept was proposed with fields like:

- role
- page span
- raw block refs
- bbox
- heading level
- list kind
- role confidence
- semantic source quality
- reading order index
- reading order basis
- warnings

This is strongly aligned with the manifest’s `normalized_block_entries`.

#### 7. Generator requirements spec

A long prose spec was drafted to make many Matterhorn “human” conditions deterministic by construction.

This includes:

- assumptions
- source-model requirements
- serialization rules
- content/asset gates
- build-time rejection rules
- validation strategy

This should not be thrown away.

#### 8. Matterhorn classifications

The transcript contains useful categorization work:

- all H-marked rows were listed
- they were classified into deterministic / conditional / still human
- the 87 machine-verifiable failures were listed and then grouped into:
  - trivially enforceable in a controlled generator
  - requiring low-level PDF checks
  - font/encoding edge cases

That work is useful if Codex needs to align implementation with PDF/UA logic.

#### 9. Real-world test input and accessibility findings

`finreport25.pdf` and the pasted Acrobat accessibility report are valuable fixtures.

The assistant already reasoned about how this file should normalize:

- many page types
- tagged but still materially accessibility-broken
- likely document/page/block warning sets
- likely figure/table/heading/bookmark issues

`finreport25.pdf` should be treated as a test fixture and normalization target, not just an example. fileciteturn2file0

### Open Threads and Next Actions

These are the most likely continuation points.

#### 1. Formalize the Python-native v0.1 patch

The assistant proposed the direction, but the actual patch list or updated schema was not produced in final form.

Likely next step:

- produce a **v0.1 patch list**:
  - keep
  - rename
  - add
  - remove
  - migration notes

#### 2. Build the first extractor adapter

This appears to be the most concrete next engineering step.

Likely target:

- `extract_with_pymupdf(...)`
- populate:
  - `source_package`
  - partial `document_summary`
  - partial `document_metadata`
  - partial `document_accessibility`
  - `page_entries`
  - `raw_block_entries`

#### 3. Add schema validation around the manifest

This was proposed as an early deliverable but not implemented in the transcript.

#### 4. Turn the `finreport25.pdf` accessibility report into manifest warnings

The assistant already reasoned that the report maps naturally to document/page/block-level warnings in the manifest. This is a concrete follow-on task.

#### 5. Define normalization rules for this document family

The user explicitly asked how the code would take a PDF like this and normalize it. The assistant answered conceptually, but not in concrete rule code.

Useful next step:

- define normalization rules for:
  - cover pages
  - TOC pages
  - narrative report pages
  - chart pages
  - financial statement tables
  - schedule/image-heavy pages

using `finreport25.pdf` as a real test case.

#### 6. Decide current target priority

Both PDF → DOCX and PDF → PDF were explored. It is not yet fully explicit which one should be implemented first in code, though the manifest itself currently names `pdf_to_docx_accessibility_manifest`, which suggests DOCX remains the anchored target.

Codex should not assume PDF → PDF has superseded PDF → DOCX unless the user says so.

#### 7. Possibly wire in OCR/document AI later

This is not the first implementation step. The user asked about OCR/document AI models, but the immediate implementation focus should still be:

- native PDF extraction
- manifest
- normalization

AI OCR belongs later as a conditional branch for scanned/image-heavy inputs.

### Guidance for Codex

- Treat this project as **creation-/generation-oriented**, not remediation-oriented, unless the user explicitly changes the frame.
- Do **not** restart the package discussion from scratch. The role split is already established.
- Do **not** answer vaguely. The user has explicitly rejected generalized or fuzzy package descriptions.
- Keep the manifest at **v0.1** and work on a **v0.1 patch**, not a version bump.
- Use the uploaded field dictionary and schema as the current contract. Patch them surgically rather than replacing them wholesale. fileciteturn1file0 fileciteturn1file1
- Preserve the distinction between:
  - raw extraction evidence
  - normalized semantic interpretation
  - review flags
  - projected output
- The most concrete next engineering move is to implement the **PyMuPDF first-pass adapter** and schema validation around it.
- Use `finreport25.pdf` and the pasted Acrobat accessibility report as a real fixture for:
  - extractor testing
  - normalization testing
  - warning-rule testing
- If you continue design work, stay grounded in implementation artifacts:
  - field maps
  - adapter responsibilities
  - normalization rules
  - warning rules
  - schema patches
- Avoid reintroducing mistakes the user already corrected:
  - remediation drift
  - vague “closest” language
  - irrelevant forms expansion
  - casual version bumping
  - generic summaries that lose the actual decision logic


#### You:
Codex has some questions:

The most useful chats would be the ones that explain decisions, not just generated code.

What would help most:

1. **Project intent**
   - What problem this project is really solving
   - Who the output is for
   - What “good enough” means for v0.1 versus later

2. **Manifest philosophy**
   - Why the manifest is central
   - What fields are considered canonical
   - Which fields are evidence versus interpretation versus projection
   - Any schema decisions you already argued through

3. **Input/output scope**
   - Which inputs matter first: PPTX, PDF, DOCX, HTML, Markdown, etc.
   - Which outputs matter first: DOCX, Markdown, PDF, JSON manifest
   - Whether outputs are meant to be final accessible docs or review artifacts

4. **Accessibility standards**
   - WCAG expectations
   - PDF/UA expectations
   - Word accessibility expectations
   - Color/contrast rules
   - Alt text conventions
   - Manual review rules

5. **Workflow decisions**
   - Extraction order
   - Normalization strategy
   - Warning/review model
   - When to fail versus warn
   - How much automation is acceptable

6. **Library choices**
   - Why PyMuPDF first
   - What pypdf/pikepdf/pdfminer should own
   - What python-docx should own
   - Any tools you rejected and why

7. **Examples**
   - A sample “bad input”
   - A sample desired manifest
   - A sample desired DOCX/Markdown output
   - A before/after explanation

8. **Naming and architecture decisions**
   - Why `accessibility_by_manifest`
   - Whether package/module names should eventually change
   - Whether we’re keeping separate adapters or moving toward one unified CLI

Best format: give me the chat exports as Markdown files or paste the relevant sections. If they’re long, I’d prefer a folder of `.md` files and I can read/summarize them locally.

Highest-value files would be named something like:

```text
project_intent.md
manifest_design.md
pdf_pipeline_decisions.md
pptx_pipeline_decisions.md
accessibility_requirements.md
desired_outputs.md
```

I do not need every back-and-forth. I need the parts where conclusions were reached, tradeoffs were discussed, or requirements were clarified.

#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
\[Unsupported Content]


#### ChatGPT:
I put the Codex-facing notes into a bundle of Markdown files:

- [codex\_handoff\_bundle.zip](sandbox:/mnt/data/codex_handoff_bundle.zip)

Individual files:

- [project\_intent.md](sandbox:/mnt/data/codex_handoff_bundle/project_intent.md)
- [manifest\_design.md](sandbox:/mnt/data/codex_handoff_bundle/manifest_design.md)
- [pdf\_pipeline\_decisions.md](sandbox:/mnt/data/codex_handoff_bundle/pdf_pipeline_decisions.md)
- [accessibility\_requirements.md](sandbox:/mnt/data/codex_handoff_bundle/accessibility_requirements.md)
- [desired\_outputs.md](sandbox:/mnt/data/codex_handoff_bundle/desired_outputs.md)
- [library\_and\_architecture\_decisions.md](sandbox:/mnt/data/codex_handoff_bundle/library_and_architecture_decisions.md)
- [pptx\_pipeline\_decisions.md](sandbox:/mnt/data/codex_handoff_bundle/pptx_pipeline_decisions.md)

I kept `pptx_pipeline_decisions.md` as a scope note, because this transcript did not materially develop PPTX logic. The highest-value files here are the first six.
