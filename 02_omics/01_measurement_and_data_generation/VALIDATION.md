# Phase 1D validation

- [x] Measurement is distinguished from biological truth and processed representation.
- [x] Reads, molecules, fragments, UMIs, cell/spot barcodes, and sample indexes are distinct.
- [x] RNA, ADT/protein, and ATAC quantities and limits are distinguished.
- [x] Spots/bins are not automatically called cells; spatial coordinates are not image features.
- [x] Fully paired, partially paired, unpaired, and mosaic designs are defined.
- [x] Zeros and sparsity are given assay-dependent interpretations.
- [x] Raw, count, filtered, normalized, transformed, reduced, and learned levels are separated.
- [x] Feature identifiers, versions, mappings, and coordinate conventions are recorded as provenance concerns.
- [x] Six Drive folders were inspected; metadata not established remains `UNKNOWN` with reasons in the reconnaissance note and dossiers.
- [x] Read-only H5AD inspector reports shape, dtype, keys, sparse encoding, metadata examples, spatial examples, and checksum preservation.
- [x] `papers.csv` and `datasets.csv` parse; source index and local links resolve.
- [x] E11/E13/E15 ATAC download completion and exact local matrix summaries were verified read-only; E18 ATAC is explicitly unavailable locally and remains UNKNOWN rather than being inferred.

Phase boundary: no preprocessing algorithm, normalization benchmark, dimensionality reduction, graph construction, representation learning, model implementation, experiment, or novelty analysis was begun.

Final project checks: `repomix . --compress` completed with 183 files and no suspicious files; `graphify . --code-only` completed with 4 code files represented as 9 nodes and 17 edges in 2 communities. `git diff --check` passed. These are context/structure checks, not scientific validation.
