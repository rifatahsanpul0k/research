# Read-only Phase 1D inspection

`inspect_h5ad.py INPUT.h5ad` emits JSON to stdout. It opens HDF5 in `r` mode, scans matrix values in bounded chunks, reports dense/CSR/CSC encodings, metadata categories, matrix shapes, selected spatial entries and scalar unstructured metadata. SHA-256 before/after verifies input preservation. It does not normalize, filter, train, build graphs or alter matrices.

Requires Python 3.11+, h5py and numpy. The temporary inspection environment used h5py 3.16.0 and numpy 2.4.6. Example: `python inspect_h5ad.py ../../04_datasets/DATASET/raw/adata_RNA.h5ad > inspection.json` (substitute the actual dataset path). Output must be outside `raw/`.

Scope limits: standard AnnData dense and CSR/CSC encodings only; no full AnnData validation. Sparse statistics describe stored entries, including explicit zeros; the script deliberately does not call this logical sparsity without checking duplicate coordinates. No biological count status is inferred from integer values or a filename. Large observation/feature metadata columns are read in memory; large matrices are not densified. JSON fails on unsupported/nonfinite metadata rather than silently fabricating a value.

Format reference: [AnnData on-disk specification](https://anndata.readthedocs.io/en/stable/fileformat-prose.html). Input dataset provenance belongs in each dossier's MANIFEST.md.

## Phase 1E utilities

- `summarize_matrices.py INPUT... --output OUT.json` computes CSR-safe logical sparsity, row totals/detections, value extrema and distribution summaries. It never densifies or changes input.
- `compare_features.py var|obs INPUT... --output OUT.json` compares identifier counts, duplicate counts, set overlap, union, order and pairwise overlap without harmonizing.
- `summarize_annotations.py CSV... --output OUT.json` records column missingness, cardinality and category counts for small categorical columns; identifier columns are cardinality-only.
- `inspect_coordinates.py INPUT... --output OUT.json` summarizes an `obsm` coordinate key (default `spatial`) without assigning physical units.

These utilities are descriptive and representation-neutral. Their outputs under `02_omics/02_preprocessing_qc_statistics/` are derived reports, not replacements for source H5AD files.

## Phase 2A synthetic arithmetic checks

`python3 code/data_inspection/check_phase2a_toys.py` runs from the repository root using NumPy. It checks the fixed examples in `05_methods/01_mathematical_foundations/TOY_CALCULATIONS.md` and emits a JSON report to stdout. All inputs are tiny synthetic arrays, probabilities or labels defined in the script. It reads no biological files, fits no research model, and constructs no neighborhood graph. The 59 checks cover arithmetic and selected edge cases; they do not validate biological interpretations or constitute a reusable benchmarking pipeline.
