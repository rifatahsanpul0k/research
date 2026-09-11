# Cross-modal translation and BABEL

Phase 2C · method study · studied_not_fitted · not_reproduced.

Translation estimates a target modality from a source:
\[
x_i^{(A)}\in\mathbb R^{p_A}
\xrightarrow{f_A}z_i\in\mathbb R^d
\xrightarrow{g_B}\widehat x_i^{(B)}\in\mathbb R^{p_B}.
\]
Integration instead seeks a common representation for joint analysis. A method may support both, but a small target prediction error does not prove successful unpaired observation matching.

BABEL (Wu et al., 2021) uses interoperable RNA and ATAC encoders/decoders trained on paired measurements. Within-modality and cross-modality reconstruction paths encourage a common code. Its RNA decoder uses count reconstruction and ATAC output models accessibility; training requires a relevant paired reference. The original paper and author repository identify translation as the central task.[^1]

**Original teaching example:** a paired training table may provide \(X_R\in\mathbb R^{100\times3}\) and \(X_A\in\mathbb R^{100\times4}\). An RNA encoder and ATAC decoder compose a \(3\to d\to4\) map. All four paths \(R\to R,\ R\to A,\ A\to R,\ A\to A\) are dimensionally valid, but their targets and statistical losses differ. If two RNA-indistinguishable observations have different ATAC profiles, a deterministic RNA-only map cannot recover both individual targets exactly.

**Project interpretation:** an inferred peak profile is conditional prediction, not the observation's measured chromatin state. Correlation between modalities does not establish a regulatory mechanism. Generalization across human/mouse, stages or feature vocabularies is a separate question; this phase does not translate our data.

Official code: [wukevin/babel](https://github.com/wukevin/babel). Code identity is checked; weights, training environment and reproducibility are not evaluated.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | BABEL interoperable modality-specific encoders/decoders |
| Training objective | Within- and cross-modality reconstruction |
| Biological prior | Paired measurement and learnable cross-modal dependence |
| Downstream model | Target-modality prediction; distinct downstream tasks |
| Evaluation | Held-out translation with uncertainty/support considerations; no run |

## Evidence

[^1]: [BABEL: original source and access notes](SOURCES.md#babel).

