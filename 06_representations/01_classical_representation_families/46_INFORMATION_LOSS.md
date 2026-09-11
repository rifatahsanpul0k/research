# A framework for information loss

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Ask what the map identifies as the same

For a deterministic map \(f\), the preimage \(f^{-1}(r)=\{x:f(x)=r\}\) contains all inputs producing representation r. Multiple distinct inputs in a preimage demonstrate loss of distinctions. This is an exact mathematical statement and does not determine whether those distinctions matter for a future biological task.

| Family class | Potentially preserved | Removed or changed |
|---|---|---|
| Raw/concatenated with full metadata | Stored values/feature names | No new biological information acquired |
| Selection/low-rank coordinates | Selected axes/subspace | Unselected values or residual directions |
| Distance/kernel relationships | Defined geometry/similarity | Named orientation or quantities invariant under the rule |
| Neighbors/ranks/graphs | Selected relations/order | Gaps, nonedges and feature details unless retained |
| Couplings | Model-based correspondence/mass constraints | Not a measurement-preserving inverse map |
| Sets/prototypes/clusters | Membership or reference-relative summary | Magnitudes or within-summary variation |
| Priors/regions/time categories | A chosen biological vocabulary | Unannotated, continuous or context-specific detail |

For random variables X,T and deterministic R=f(X), data processing gives I(T;R)≤I(T;X) when these mutual informations are defined: transformation cannot create information about T absent from X. It can make useful information more accessible to a constrained estimator, or incorporate new information if external priors/metadata enter f; those are different statements.[^1]

## A future assessment record

For each family, document what is preserved, removed, distorted, easier to model and harder to interpret. State the task and uncertainty before calling loss beneficial. Good reconstruction can preserve nuisance; a highly lossy label may serve one task while hiding another. No task-based effectiveness is measured here.

The [unranked registry/framework](REPRESENTATION_COMPARISON_FRAMEWORK.md) gives family-specific loss and failure-mode fields. For this project, zero versus missing, spot versus cell, shared versus modality-specific variation and chronological stage versus inferred progression must survive as explicit distinctions. A compact representation is not inherently a better biological representation.

## Evidence

[^1]: Gray RM (2023). [Entropy and Information Theory, first edition corrected June 26 2023](https://www-ee.stanford.edu/~gray/it.pdf). See [access record](SOURCES.md#info).
