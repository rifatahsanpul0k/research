# 3. Barcodes and UMIs

A sample barcode (index) identifies a pooled library; a cell or spot barcode identifies an observation; a UMI is a short random molecular label intended to identify original tagged molecules; a feature barcode identifies a measured feature such as an antibody tag. A conceptual read can therefore contain `sample + observation + molecule + biological sequence` [S01][S03][S04][S20].

PCR copies one original molecule into many reads. Counting reads can therefore overstate molecules. Grouping reads by observation, feature, and UMI estimates molecule counts, but barcode collisions, sequencing errors, saturation, and UMI reuse make the estimate imperfect. A UMI is not a cell barcode, and deduplication is an assay-specific inference rather than proof of molecular identity [S03][S04].

In a matrix (X_{ij}), (i) is an observation and (j) a feature; an integer often represents assigned UMIs (RNA/ADT) or fragments (ATAC), but the file must establish that meaning. Barcode suffixes and shared IDs can link modalities only when the experiment documents common observation identities.

**Evidence:** [S01], [S03], [S04], [S20].
