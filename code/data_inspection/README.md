# Read-only Phase 1D inspection

`inspect_h5ad.py INPUT.h5ad` emits JSON to stdout. It opens HDF5 in `r` mode, scans matrix values in bounded chunks, reports dense/CSR/CSC encodings, metadata categories, matrix shapes, selected spatial entries and scalar unstructured metadata. SHA-256 before/after verifies input preservation. It does not normalize, filter, train, build graphs or alter matrices.

Requires Python 3.11+, h5py and numpy. The temporary inspection environment used h5py 3.16.0 and numpy 2.4.6. Example: `python inspect_h5ad.py ../../04_datasets/DATASET/raw/adata_RNA.h5ad > inspection.json` (substitute the actual dataset path). Output must be outside `raw/`.

Scope limits: standard AnnData dense and CSR/CSC encodings only; no full AnnData validation. Sparse statistics describe stored entries, including explicit zeros; the script deliberately does not call this logical sparsity without checking duplicate coordinates. No biological count status is inferred from integer values or a filename. Large observation/feature metadata columns are read in memory; large matrices are not densified. JSON fails on unsupported/nonfinite metadata rather than silently fabricating a value.

Format reference: [AnnData on-disk specification](https://anndata.readthedocs.io/en/stable/fileformat-prose.html). Input dataset provenance belongs in each dossier's MANIFEST.md.
