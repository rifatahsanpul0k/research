# Transformers

Phase 2C · method study · studied_not_fitted · not_reproduced.

A transformer block combines multi-head attention, a position-wise feed-forward network, residual connections and normalization. Multiple heads use different Q/K/V projections; their \(L\times d_v\) outputs concatenate to \(L\times(hd_v)\), then an output matrix maps back to residual width \(d_{\rm model}\). Thus residual addition requires matching \(L\times d_{\rm model}\) shapes.[^1]

A schematic pre-normalized block is
\[
H'=H+\operatorname{MHA}(\operatorname{LN}(H)),\qquad
H''=H'+\operatorname{FFN}(\operatorname{LN}(H')).
\]
Here \(H\in\mathbb R^{L\times d_{\rm model}}\); LN normalizes features within a token, and FFN applies a shared nonlinear map to each token. This illustrates a common variant; the original 2017 transformer uses a different normalization placement. Architecture details must be version-specific.

Positional/context encoding informs the network about order or structure. Without such encodings and with appropriately permuted masks, self-attention is permutation equivariant: permuting input tokens permutes output tokens. A pooling operation can then create an invariant observation vector. A sequence position should not silently mean genomic distance if the tokens were ordered by expression.

**Project interpretation:** a gene token's contextual embedding can vary between observations even though its identity embedding is fixed. Averaging gene embeddings into a cell/spot embedding is another operation, not an automatic biological summary. An RNA-pretrained transformer needs explicit feature-vocabulary and value-encoding contracts before another assay can enter it.

Transformers are not necessarily generative or probabilistic. Masked classification, reconstruction and contrastive objectives can use similar blocks. The next notes address the specific tokenization and training choices.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Multi-head attention, FFN, residual and normalization blocks |
| Training objective | Task-dependent; architecture does not select a loss |
| Biological prior | Order/context encodings; biological prior optional |
| Downstream model | Pooling and task head chosen separately |
| Evaluation | Transfer/task and biological validation |

## Evidence

[^1]: [ATTENTION: original source and access notes](SOURCES.md#attention).
[^2]: [DEEPSETS: original source and access notes](SOURCES.md#deepsets).

