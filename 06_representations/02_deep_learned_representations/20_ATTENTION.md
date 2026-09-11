# Attention

Phase 2C · method study · studied_not_fitted · not_reproduced.

Let \(H_Q\in\mathbb R^{L_q\times d_{\rm in,Q}}\), \(H_K\in\mathbb R^{L_k\times d_{\rm in,K}}\). Learned projections form \(Q=H_QW_Q\in\mathbb R^{L_q\times d_k}\), \(K=H_KW_K\in\mathbb R^{L_k\times d_k}\), \(V=H_KW_V\in\mathbb R^{L_k\times d_v}\). Scaled dot-product attention is
\[
P=\operatorname{softmax}_{\rm rows}(QK^\top/\sqrt{d_k}),\qquad O=PV\in\mathbb R^{L_q\times d_v}.
\]
Each row of \(P\) sums to one across allowed keys; an additive mask can exclude keys before softmax. Queries request context, keys determine scores, and values supply the aggregated vectors.[^1]

In self-attention, queries/keys/values derive from one input. In cross-attention they may come from different modalities. Tokens can represent genes, modalities, observations or neighbors; these are different constructions with different axis meanings.

**Synthetic calculation:** for one query, key scores \((0,\log3)\) give weights \((1/4,3/4)\). Values \((2,6)\) yield output \(5\). If the second value is instead \(-2\), the same attention weights yield \(-1\). Weight size alone does not tell the final effect.

Attention weights are conditional on the query, competing keys and learned projections. They are not automatically feature importance or biological causality. Primary interpretability work shows why attention-based explanation requires tests; it does not imply that attention can never be informative.[^2]

**Project interpretation:** assigning large weight to a neighboring spot cannot establish signaling. High ADT attention could reflect usefulness for the training objective, a scale effect or a technical cue. Full attention over \(L\) tokens creates \(L^2\) scores; state what the tokens are.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Learned Q/K/V weighting module, not an entire task model |
| Training objective | Inherited from the surrounding model |
| Biological prior | Allowed keys and context encoding; no causal prior inherent |
| Downstream model | Task head uses attention outputs |
| Evaluation | Prediction and interpretation require separate checks |

## Evidence

[^1]: [ATTENTION: original source and access notes](SOURCES.md#attention).
[^2]: [ATTN_EXPLAIN: original source and access notes](SOURCES.md#attn_explain).

