# Measurement concept map

```text
biological specimen
  ↓ tissue/cell preparation
assay and molecular capture
  ↓ observation/sample/feature barcodes and UMIs
library preparation
  ↓ sequencing or instrument signal
raw reads/signals
  ↓ demultiplexing, mapping, annotation-based assignment
counts / intensities / fragments
  ↓ observation × feature matrix
metadata + identifiers + coordinates + supplied annotations
  ↓ documented QC and provenance
processed data
  ↓
future computational representation
  ↓
future ML model
```

At every arrow information can be lost, mixed, undersampled, misassigned, or introduced by processing. A row may be a cell, nucleus, spot, bin, or pixel-defined location; a column may be a gene, antibody, or genomic region. Pairing and coordinate frames are metadata claims that require evidence. Phase 1D stops before representation learning and ML.

**References:** [S01], [S02], [S06], [S09], [S11], [S13], [S22].
