# Desired Outputs

Supporting reference only.

The first output is the manifest.

For PDF, the current expected outputs are:

- master JSON manifest
- per-extractor JSON manifests

Near-term PDF outputs should be review-oriented:

- normalized block views
- review reports
- DOCX or Markdown projections for inspection and editing

Later outputs may include:

- accessible DOCX
- accessible PDF
- validation reports
- richer reviewer bundles

The project should avoid treating early projected outputs as final accessible
deliverables. They are traceable process artifacts unless explicitly promoted by
validation and review.

The CLI direction should be both unified and modular:

- one user-facing CLI family
- separate input adapters
- separate output adapters
- shared manifest and pipeline primitives
