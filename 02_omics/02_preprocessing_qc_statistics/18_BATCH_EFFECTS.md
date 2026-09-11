# Batch effects

A useful decomposition is (X=\text{biology}+\text{technical effect}+\text{noise}), with technical effects from donor, library, chemistry, operator, section, sequencing depth or processing. Batch is a design attribute, not a pattern discovered from a matrix. Stage, region or tissue may be biological, technical, or both; stage is not automatically a batch [S16,S43].

Record batch variables before attempting correction and preserve biological contrasts that are confounded with them. If every E11 observation comes from a distinct preparation from every E13 observation, stage and preparation cannot be separated by statistics alone. In spatial data, section and position can be coupled; in multimodal assays, modality-specific QC can differ by batch. We do not estimate correction factors. Evidence: Luecken & Theis [S16], Stuart et al. [S43], Zimmerman et al. on hierarchical sampling [S17].
