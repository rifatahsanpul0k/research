# 20. Primary dataset reconnaissance

## Verified file-level facts

All six supplied Drive folders were accessible in the browser. Each contains two H5AD matrices and one annotation CSV (`annotation.csv` for the lymph-node folders; `anno.csv` for the four mouse folders). The downloaded files are unchanged copies recorded in `DOWNLOAD_MANIFEST.json`; raw directories are ignored by Git. H5AD structure was inspected read-only with `inspect_h5ad.py`.

The A1 lymph-node RNA file is 3,484 × 18,085 with CSR `float32` X, integer-valued stored entries, and `obsm/spatial` shape 3,484 × 2. Its ADT file is 3,484 × 31 with CSR X and the same coordinate shape; example features include `CD163`, `CR2`, `PCNA`, `VIM`, and `KRT5`. A1 annotation preview has `Barcode, manual-anno` and region labels including cortex, follicle, capsule, medulla cords/sinuses, hilum, and pericapsular adipose tissue.

The public GEO record GSE263617 identifies the source study as 10x Visium RNA and protein co-profiling and reports A1 as 3,484 spots, 18,085 genes, and 31 proteins; D1 is reported as 3,359 spots with the same feature counts [S28][S29]. SMART’s source documentation independently reports A1’s two AnnData shapes and says H&E-based annotations are ground truth for its study [S33]. These publication facts support the mirror’s dimensions and intended pairing, while the local files remain processed H5ADs.

The mouse folders contain RNA and ATAC H5ADs plus cluster annotation CSVs. Read-only inspection verified E11 RNA 1,263 × 32,285 and ATAC 1,263 × 69,370; E13 RNA 1,777 × 32,285 and ATAC 1,777 × 123,840; and E18 RNA 2,129 × 32,285. All inspected matrices are CSR `float32` with `obsm/spatial` shape matching the observation count. SMART’s E18.5 tutorial reports 2,129 observations, 32,285 RNA features, and 117,473 ATAC features for its documented processed example [S34]; the local E11/E13/E18 files therefore must not be silently substituted for that tutorial’s ATAC object. The MISAR-seq publication reports spatial RNA/accessibility profiling at E11.0, E13.0/13.5, E15.0/15.5, and E18.0/18.5 stages [S27]. Exact local count/fragment semantics, donor/embryo relationships, and annotation provenance remain open.

## Unknowns retained

The Drive folders do not themselves establish raw FASTQ availability, library chemistry/version, donor identifiers, section thickness, genome annotation release, coordinate units, filtering history, checksum provenance beyond this download, licensing terms, or whether every local X entry is a raw count. The supplied filenames are identifiers, not evidence. E15 ATAC is complete and passes H5AD inspection; E18 ATAC was visible in Drive but is not available as a complete local copy and remains `UNKNOWN`.

**Evidence:** [S27], [S28], [S29], [S33], [S34], Drive folder manifests in `REMOTE_FILES.json` and `DOWNLOAD_MANIFEST.json`.
