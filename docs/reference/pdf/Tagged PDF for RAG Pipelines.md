---
created: 2026-04-22T12:50:46 (UTC -05:00)
tags: []
source: https://opendataloader.org/docs/tagged-pdf-rag
author: 
---

# Tagged PDF for RAG Pipelines

> ## Excerpt
> Leverage PDF structure tags for higher-quality AI data extraction in RAG applications

---
Leverage PDF structure tags for higher-quality AI data extraction in RAG applications

## [Why Tagged PDFs Improve RAG Quality](https://opendataloader.org/docs/tagged-pdf-rag#why-tagged-pdfs-improve-rag-quality)

Retrieval-Augmented Generation (RAG) systems depend on accurate document parsing. When PDFs have proper structure tags, you get semantic ground truth instead of heuristic guesses.

**Tagged PDF advantages for RAG:**

-   **Exact reading order** — No algorithmic guessing about column layouts
-   **Semantic hierarchy** — Headings, lists, and sections are explicitly marked
-   **Table structure** — Row/column relationships are preserved
-   **Chunk boundaries** — Natural semantic units for vector embedding

|      Aspect      |     Tag-Blind (Heuristics)     | Tag-Aware (Structure Tree)  |
|------------------|--------------------------------|-----------------------------|
|  **Reading order**   |   Inferred from coordinates    |    Author-defined, exact    |
|   **Multi-column**   | Often fails on complex layouts |      Correct by design      |
|     **Headings**     |     Guessed from font size     | Semantically tagged (H1-H6) |
|      **Tables**      |   Cell boundaries estimated    | Row/column spans preserved  |
|      **Lists**       |  Detected by bullet patterns   |   List structure explicit   |
| **Processing speed** |    Slower (visual analysis)    | Faster (direct extraction)  |

### [Example: Multi-Column Document](https://opendataloader.org/docs/tagged-pdf-rag#example-multi-column-document)

```sql
Tag-Blind Result:                    Tag-Aware Result:
┌─────────────────────┐              ┌─────────────────────┐
│ Introduction The    │              │ Introduction        │
│ first column text   │              │                     │
│ continues here The  │              │ The first column    │
│ second column has   │              │ text continues here │
│ different content   │              │                     │
└─────────────────────┘              │ The second column   │
  ↑ Columns merged incorrectly       │ has different       │
                                     │ content             │
                                     └─────────────────────┘
                                       ↑ Correct reading order
```

## [Using Tagged PDFs in RAG Workflows](https://opendataloader.org/docs/tagged-pdf-rag#using-tagged-pdfs-in-rag-workflows)

### [Check if a PDF is Tagged](https://opendataloader.org/docs/tagged-pdf-rag#check-if-a-pdf-is-tagged)

Not all PDFs have structure tags. OpenDataLoader automatically detects and uses tags when available:

```python
import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="json,markdown",
    use_struct_tree=True                # Use tags if present
)
```

If the PDF lacks structure tags, OpenDataLoader logs a warning and falls back to the XY-Cut++ algorithm for reading order detection.

### [CLI Usage](https://opendataloader.org/docs/tagged-pdf-rag#cli-usage)

```sql
# Batch all files in one call — each invocation spawns a JVM process, so repeated calls are slow
opendataloader-pdf file1.pdf file2.pdf folder/ \
  --output-dir output/ \
  -f json,markdown \
  --use-struct-tree
```

## [Semantic Chunking with Tagged PDFs](https://opendataloader.org/docs/tagged-pdf-rag#semantic-chunking-with-tagged-pdfs)

Tagged PDFs enable semantic chunking—splitting documents by meaning rather than arbitrary character counts.

### [Strategy 1: Chunk by Heading Level](https://opendataloader.org/docs/tagged-pdf-rag#strategy-1-chunk-by-heading-level)

```csharp
import json

# Load extracted JSON
with open("output/document.json") as f:
    doc = json.load(f)

# Split into chunks by H1/H2 boundaries
chunks = []
current_chunk = []

for element in doc["kids"]:
    if element.get("type") == "heading" and element.get("heading level") in [1, 2]:
        if current_chunk:
            chunks.append(current_chunk)
        current_chunk = [element]
    else:
        current_chunk.append(element)

if current_chunk:
    chunks.append(current_chunk)
```

### [Strategy 2: Preserve Semantic Units](https://opendataloader.org/docs/tagged-pdf-rag#strategy-2-preserve-semantic-units)

Keep related content together (e.g., a heading with its paragraphs):

```python
def semantic_chunk(elements, max_tokens=512):
    """Chunk while preserving semantic units."""
    chunks = []
    current = []
    current_tokens = 0

    for elem in elements:
        elem_tokens = len(elem.get("content", "").split())

        # Start new chunk at major headings (H1)
        is_h1 = elem.get("type") == "heading" and elem.get("heading level") == 1
        if is_h1 and current:
            chunks.append(current)
            current = [elem]
            current_tokens = elem_tokens
        # Or when exceeding token limit
        elif current_tokens + elem_tokens > max_tokens:
            chunks.append(current)
            current = [elem]
            current_tokens = elem_tokens
        else:
            current.append(elem)
            current_tokens += elem_tokens

    if current:
        chunks.append(current)

    return chunks
```

### [Strategy 3: Table-Aware Chunking](https://opendataloader.org/docs/tagged-pdf-rag#strategy-3-table-aware-chunking)

Never split tables across chunks:

```python
def table_aware_chunk(elements, max_tokens=512):
    """Keep tables intact during chunking."""
    chunks = []
    current = []
    current_tokens = 0

    for elem in elements:
        elem_tokens = len(elem.get("content", "").split())

        # Tables stay together regardless of size
        if elem.get("type") == "table":
            if current:
                chunks.append(current)
            chunks.append([elem])  # Table as its own chunk
            current = []
            current_tokens = 0
        elif current_tokens + elem_tokens > max_tokens:
            chunks.append(current)
            current = [elem]
            current_tokens = elem_tokens
        else:
            current.append(elem)
            current_tokens += elem_tokens

    if current:
        chunks.append(current)

    return chunks
```

## [Handling Mixed Documents](https://opendataloader.org/docs/tagged-pdf-rag#handling-mixed-documents)

Real-world PDF collections contain both tagged and untagged documents. OpenDataLoader handles this gracefully:

```python
import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="json,markdown",
    use_struct_tree=True                # Auto-fallback if no tags
)
```

**Behavior:**

-   If PDF has tags → Uses structure tree (exact)
-   If PDF lacks tags → Falls back to XY-Cut++ (heuristic)
-   Logs indicate which method was used

## [Future: Auto-Tagging Untagged PDFs](https://opendataloader.org/docs/tagged-pdf-rag#future-auto-tagging-untagged-pdfs)

Many legacy PDFs lack structure tags. Our upcoming Auto-Tagging Engine (Q2 2026) will generate tags automatically:

```graphql
# API shape preview — available Q2 2026
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    auto_tag=True                       # Generate structure tags
)
```

This enables RAG-quality extraction even for older documents.

## [Integration with RAG Frameworks](https://opendataloader.org/docs/tagged-pdf-rag#integration-with-rag-frameworks)

### [LangChain Integration](https://opendataloader.org/docs/tagged-pdf-rag#langchain-integration)

```python
from langchain_opendataloader_pdf import OpenDataLoaderPDFLoader

loader = OpenDataLoaderPDFLoader(
    file_path=["file1.pdf", "file2.pdf", "folder/"],
    format="text",
    use_struct_tree=True,
)
documents = loader.load()
```

## [Learn More](https://opendataloader.org/docs/tagged-pdf-rag#learn-more)

-   [Tagged PDF](https://opendataloader.org/docs/tagged-pdf) — Core Tagged PDF documentation
-   [RAG Integration](https://opendataloader.org/docs/rag-integration) — General RAG pipeline guide
-   [Accessibility Compliance](https://opendataloader.org/docs/accessibility-compliance) — Why Tagged PDFs are becoming standard
-   [Benchmark Metrics](https://opendataloader.org/docs/benchmark) — How we measure extraction quality
