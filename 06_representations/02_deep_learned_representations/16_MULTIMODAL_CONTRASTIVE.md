# Multimodal contrastive representations

Phase 2C · method study · studied_not_fitted · not_reproduced.

For paired observations, let \(Z_R=f_R(X_R)\) and \(Z_P=f_P(X_P)\), both \(n\times d\). An \(n\times n\) score matrix \(S_{ij}=s(z_{Ri},z_{Pj})/\tau\) can identify \(i=j\) pairs using row-wise cross-entropy, optionally symmetrized with the reverse direction. This adapts the paired-view contrastive principle; it is a conceptual objective, not a proposed omics model.[^1]

The row index is the shared identity anchor; gene and antibody columns do not correspond one-to-one. RNA \(G\)-vectors and ADT \(T\)-vectors can map into a common \(d\)-space without \(G=T\). A shared coordinate system is learned using an assumption about what paired observations share.

**Permanent distinction:** paired modalities as positives encode shared observation identity, not proof that all modality information should align. An RNA-only regulatory response and a stable protein panel could disagree for legitimate biological reasons; the objective alone cannot distinguish this possibility from error. Shared/private decompositions make the desired retained information explicit but do not automatically identify it.[^2]

**Project interpretation:** pairing must come from verified IDs and row ordering. Matching observations merely by their similar numerical vectors would build the desired conclusion into the training labels. If two spots overlap spatially or share donor effects, treating them as unrelated negatives may also be misleading. Entirely missing ADT cannot provide a measured positive, and an imputed ADT vector is not independent evidence.

Memory for a full in-batch pair matrix is \(O(n_b^2)\), where \(n_b\) is minibatch size, not the number of genes. See [scalability](62_SCALABILITY.md).

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Two modality encoders with compatible output widths |
| Training objective | Paired-view contrastive objective; optional bidirectionality |
| Biological prior | Shared observation identity, declared invariances |
| Downstream model | Cross-modal retrieval or separate joint tasks |
| Evaluation | Pair provenance and biological preservation |

## Evidence

[^1]: [SIMCLR: original source and access notes](SOURCES.md#simclr).
[^2]: [DISENTANGLE: original source and access notes](SOURCES.md#disentangle).

