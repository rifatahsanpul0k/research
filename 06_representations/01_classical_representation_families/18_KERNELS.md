# Kernel representations

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## A Gram matrix, not any affinity

A real symmetric kernel k is positive semidefinite (PSD) when every finite Gram matrix \(K_{ij}=k(x_i,x_j)\), \(K:n\times n\), satisfies \(a^TKa\ge0\) for every \(a\in\mathbb R^n\). This corresponds to an inner product \(k(x,y)=\langle\phi(x),\phi(y)\rangle\) in a feature space, which may be infinite-dimensional. Algorithms expressed through inner products can use K without constructing φ explicitly: the kernel trick.[^1]

For x,y∈Rᵖ:

| Kernel | Definition | Parameters |
|---|---|---|
| Linear | xᵀy | No extra parameter |
| Polynomial | \((\gamma x^Ty+c)^r\) | γ,c≥0; integer r≥1 |
| RBF | \(\exp[-\|x-y\|^2/(2\sigma^2)]\) | σ>0 |

Negative entries do not by themselves invalidate a PSD kernel; negative eigenvalues do. A symmetric matrix with entries in [0,1] is not automatically PSD. Similarly, adjacency matrices generally are not kernels merely because they describe relationships.

## Geometry and project interpretation

Kernel choice defines which nonlinear similarities are available to a later model. For an RBF, very large σ makes distinct points nearly equally similar; very small σ makes off-diagonal values tiny for separated points. These limiting observations follow directly from the exponential and are not parameter recommendations.

A linear Gram matrix loses original coordinate orientation; a nonlinear feature map may retain or discard different information. Even a PSD kernel does not validate a biological similarity assumption. Assay processing, feature choices and a coordinate reference frame still matter. Spatial and molecular kernels could coexist or be combined; a nonnegative weighted sum of PSD kernels on the same observation set remains PSD by the quadratic-form definition. This mathematical construction does not select weights or establish meaningful modality balance.

Dense kernel storage is O(n²), with O(n²p) direct RBF evaluation on dense p-dimensional data. Approximation changes representation and needs future error assessment. Missing entries require a defined kernel on available information; arbitrary pairwise deletion does not guarantee PSD. No kernel model or benchmark was run.

## Evidence

[^1]: Blum A; Hopcroft J; Kannan R (2020). [Foundations of Data Science](https://www.cs.cornell.edu/jeh/book.pdf). See [access record](SOURCES.md#bhk).
