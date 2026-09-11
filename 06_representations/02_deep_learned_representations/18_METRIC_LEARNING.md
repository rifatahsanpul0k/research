# Metric learning

Phase 2C · method study · studied_not_fitted · not_reproduced.

A Siamese architecture applies shared encoder parameters to two inputs. A triplet objective adds an anchor \(a\), positive \(p\), negative \(n\), and margin \(m>0\):
\[
\ell=\max(0,d(f(a),f(p))-d(f(a),f(n))+m).
\]
The distance \(d\) must be specified, including whether it is squared Euclidean distance. FaceNet is a foundational triplet-embedding example; biological applications require a separate definition of positive and negative.[^1]

For squared distances \(d(a,p)=1,\ d(a,n)=4,\ m=2\), loss is \(\max(0,-1)=0\). If the negative distance is instead \(2\), loss is \(1\). Zero loss only certifies that this triplet's margin condition holds; it says nothing about unseen pairs.

A linear embedding \(z=Wx\), \(W\in\mathbb R^{d\times p}\), induces squared distance \((x-y)^\top W^\top W(x-y)\). \(W^\top W\) is positive semidefinite. If \(W\) has a nullspace, distinct inputs can have zero embedded distance, so the induced function on original inputs is not necessarily a strict metric.

**Project interpretation:** marker-based positive labels can omit state, stage and donor effects. Incorrect negatives can repel related transitional observations. Choosing triples from an already fitted clustering can make the model reproduce its errors. A large margin does not establish cellular equivalence, and an encoder trained on human immune cells is not automatically transferable to embryonic mouse tissue.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Shared-weight Siamese/triplet encoder |
| Training objective | Margin or pair-based distance objective |
| Biological prior | Positive/negative biological semantics supplied externally |
| Downstream model | Nearest-neighbor retrieval, classifier or clustering |
| Evaluation | Held-out relations and biological validity; no run |

## Evidence

[^1]: [FACENET: original source and access notes](SOURCES.md#facenet).

