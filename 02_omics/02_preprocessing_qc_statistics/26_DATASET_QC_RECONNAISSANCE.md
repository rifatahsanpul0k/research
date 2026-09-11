# Dataset-specific QC reconnaissance

The six supplied datasets were inspected read-only. A1: RNA 3,484×18,085 and ADT 3,484×31; D1: 3,359×18,085 and 31. E11/E13/E15: paired RNA 1,263/1,777/1,949×32,285 with ATAC 69,370/123,840/141,420 peaks. E18: RNA 2,129×32,285; ATAC unavailable. X is CSR float32; `obsm/spatial` is present with (n\times2) arrays. Paired modality observation IDs match in both membership and order for A1, D1, E11, E13 and E15.

Annotation CSVs have no missing barcodes or labels. A1 has 10 manual-annotation categories; D1 has 11; E11/E13/E15/E18 have 8/12/12/14 `cluster` categories, with an accompanying numeric cluster code. ATAC obs fields include fragments and TSS-related counts. Exact distributions and source paths are in `DATASET_STATISTICS.md` and `annotation_summary.json`. Labels are supplied/manual or source-derived, not perfect ground truth. Evidence: GEO GSE263617 [S29,S30,S31], SMART documentation [S33,S34], MISAR-seq [S27].
