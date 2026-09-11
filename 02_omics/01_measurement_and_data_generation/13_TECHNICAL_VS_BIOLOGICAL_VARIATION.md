# 13. Technical versus biological variation

Biological variation includes cell type/state, tissue region, developmental stage, donor/specimen, and condition. Technical variation includes library size, sequencing depth, chemistry, capture efficiency, handling, ambient RNA/antibody, and doublets [S16].

Metadata tables should keep these axes separate: `cell_type`, `state`, `region`, `stage`, `donor` versus `library_size`, `batch`, `chemistry`, `capture`, and QC flags. A strong batch or depth signal can be easier for a model to learn than a biological signal, producing apparent similarity that reflects processing.

The same biological state can have different measurements across libraries; different states can appear similar under shallow sampling. Donor cells are subsamples rather than independent donors, so hierarchy matters for later generalization [S17]. This phase introduces no correction method.

**Evidence:** [S16], [S17].
