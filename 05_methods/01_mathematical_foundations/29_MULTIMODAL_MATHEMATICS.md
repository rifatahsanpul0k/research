# 29. Multiview and multimodal mathematics

For paired views $X^{(1)}\in\mathbb R^{n\times p_1}$ and $X^{(2)}\in\mathbb R^{n\times p_2}$, shared rows refer to the same eligible observations. Parenthesized superscripts label views; $p_1,p_2$ are their feature counts. If pairing is unavailable, use different row counts $n_1,n_2$ rather than asserting correspondence. [Phase 1E pairing](../../02_omics/02_preprocessing_qc_statistics/26_DATASET_QC_RECONNAISSANCE.md)

| Mathematical relationship | Shape/definition | Question left open |
|---|---|---|
| Concatenation | $[X^{(1)}\;X^{(2)}]\in\mathbb R^{n\times(p_1+p_2)}$ | How are scales and feature identities handled? |
| Separate spaces | $Z^{(m)}\in\mathbb R^{n\times d_m}$ for view $m$ | Which relationships remain view-specific? |
| Common coordinates | $Z\in\mathbb R^{n\times d}$ with separate reconstructions | Is sharing supported, or is private signal lost? |
| Aligned spaces | $Z^{(1)},Z^{(2)}\in\mathbb R^{n\times d}$ with a declared correspondence | What makes axes or distances comparable? |
| Cross-covariance | $X_c^{(1)\top}X_c^{(2)}/(n-1)\in\mathbb R^{p_1\times p_2}$ | How much reflects biology versus depth/composition? |
| Shared factors | $X^{(m)}\approx ZB_m^\top$, $B_m:p_m\times d$ | Are factors identifiable? |
| Conditional distribution | $p(x_i^{(2)}\mid x_i^{(1)})$ | Is dependence predictive, causal or confounded? |

These are shape conventions and questions, not integration methods chosen for the project. [Linear maps](SOURCES.md#vmls), [probability](SOURCES.md#probability)

A1 has $p_1=18085$ RNA features and $p_2=31$ ADT features, so concatenation gives $3484\times18116$. There are about 583.39 RNA columns per ADT column. If each standardized feature contributed equal expected squared discrepancy, total RNA contribution would be much larger simply through feature count. Without standardization, magnitudes can reverse that balance; feature count alone does not determine dominance.

Spatial $S\in\mathbb R^{n\times2}$ is another observed table with units and geometry, not an automatic extra molecular view. E18 ATAC is absent locally. No concatenated matrix, shared factor fit or modality weights are produced.
