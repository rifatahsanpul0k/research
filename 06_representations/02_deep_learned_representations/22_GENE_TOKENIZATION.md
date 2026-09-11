# Gene-token representations

Phase 2C · method study · studied_not_fitted · not_reproduced.

A computational token can combine identity and value information:
\[
h_{ig}=e_g+v(x_{ig})+c_i\in\mathbb R^{d_{\rm model}}.
\]
Here \(e_g\) is a gene-identity embedding, \(v\) maps a numeric value or bin to the same width, and \(c_i\) is optional observation context. This is a teaching template, not a claim that all single-cell transformers use additive encodings.

scGPT distinguishes gene identity from expression-value encoding; Geneformer instead ranks genes after corpus-dependent expression scaling and predicts masked gene identities. scFoundation uses an expression-aware design covering a fixed large gene set. Tokenization is therefore method- and checkpoint-specific.[^1][^2][^3]

| Choice | Information retained or altered |
| --- | --- |
| Fixed gene vocabulary | Preserves identities represented in that vocabulary; out-of-vocabulary genes need a rule |
| Rank ordering | Retains relative rank; loses some magnitude information |
| Value bins | Retains intervals; loses within-bin differences |
| Omit zero-valued genes | Shortens input but changes context and zero semantics |
| Truncate sequence | Drops features beyond the limit |
| Add metadata | Makes those covariates available and potentially influential |

Synthetic example: \((8,4,0)\) and \((80,40,0)\) share an ordinary rank order. A rank-only encoding cannot distinguish their absolute scales. This example does not assert that either real tokenizer omits normalization details.

**Project interpretation:** duplicated identifiers, mixed gene symbols/Ensembl IDs, species differences and zero/missing masks must be resolved explicitly. An unmeasured gene is not a measured zero. RNA gene tokens do not automatically encode peaks or antibodies. Changing order can change a model using positional embeddings even when the numeric multiset is unchanged.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Tokenization followed by an encoder; it is an input representation stage |
| Training objective | Mask/value prediction or other downstream pretraining loss |
| Biological prior | Vocabulary, order and normalization encode assumptions |
| Downstream model | Pooled observation or contextual feature embeddings feed tasks |
| Evaluation | Feature coverage, transfer and biological meaning |

## Evidence

[^1]: [SCGPT: original source and access notes](SOURCES.md#scgpt).
[^2]: [GENEFORMER_CODE: original source and access notes](SOURCES.md#geneformer_code).
[^3]: [SCFOUNDATION: original source and access notes](SOURCES.md#scfoundation).

