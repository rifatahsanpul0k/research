# Phase 1E concept map

```text
observed assay matrix X_obs + obs/var/coordinates
        |
        +--> QC: library size, detected features, fragments, TSS, FRiP,
        |          background, coordinates, metadata, doublet/ambient flags
        |
        +--> declared filtering (rows/features; reversible record)
        |
        +--> modality-specific preprocessing
        |      RNA: size factors -> log1p or count model -> optional HVGs -> scale
        |      ADT: background/isotype reasoning -> CLR or other declared scale
        |      ATAC: peak matrix -> TF-IDF -> conceptual LSI/SVD
        |      spatial: frame/units/orientation/registration checks
        |
        +--> lineage + missingness mask + feature/observation alignment
                         |
                         `--> representation-neutral data prepared for Phase 2A
```

Every arrow can alter values, variance, sparsity, feature relations or distances. No arrow here chooses a model, builds a graph, or asserts biological equivalence.
