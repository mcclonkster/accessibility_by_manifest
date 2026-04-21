# Extracted chat artifacts

These files were extracted from fenced code blocks in `ChatGPT-WCAG_2.2_PPTX_to_PDF.md`.

Extraction rule:
- If a code block ID appeared multiple times, the latest occurrence in the transcript was used.
- File names come from the `code-block-id-to-filename-mapping` block in the transcript.
- Cleaner alias names for the two scripts were also added:
  - pptx_extract_and_manifest.py
  - docx_remediation_transformer.py

## Normal usage

Use the packaged CLI instead of editing the config constants in Script 1 or
Script 2.

Use the project virtualenv Python shown below. Plain `python` or `python3` may
point to a different interpreter that does not have `python-pptx` or
`python-docx` installed. `--help` works without those packages, but actual
conversion requires the virtualenv dependencies.

One file:

```bash
cd /Users/computerk/Library/CloudStorage/Dropbox/0_VSCode/extracted_chat_artifacts
/Users/computerk/Library/CloudStorage/Dropbox/0_VSCode/.venv/bin/python \
  -m pptx_docx_workflow \
  "/path/to/deck.pptx" \
  --overwrite
```

Folder of PPTX files:

```bash
cd /Users/computerk/Library/CloudStorage/Dropbox/0_VSCode/extracted_chat_artifacts
/Users/computerk/Library/CloudStorage/Dropbox/0_VSCode/.venv/bin/python \
  -m pptx_docx_workflow \
  "/path/to/folder" \
  --overwrite
```

By default, folder mode searches recursively, skips PowerPoint lock files
starting with `~$`, renders slide images automatically, runs both Script 1 and
Script 2, and writes one `<deck>_workflow_output` folder per deck.

The top-level `run_pptx_docx_workflow.py` file is kept as a compatibility
wrapper around the packaged CLI.

Run tests:

```bash
cd /Users/computerk/Library/CloudStorage/Dropbox/0_VSCode/extracted_chat_artifacts
/Users/computerk/Library/CloudStorage/Dropbox/0_VSCode/.venv/bin/python \
  -m unittest discover -s tests -v
```
