# 30. Missing data mathematics

Let $M\in\{0,1\}^{n\times p}$ record which entries of $X$ are observed: $M_{ij}=1$ for measured entry, $0$ for unavailable entry. Define observed-index set $\Omega=\{(i,j):M_{ij}=1\}$. A masked squared loss is
$$
\mathcal L_\Omega=\frac1{|\Omega|}
\sum_{(i,j)\in\Omega}(x_{ij}-\hat x_{ij})^2,
$$
for $|\Omega|>0$, where $|\Omega|$ counts observed entries. This uses observed values only; it does not impute the others. A separate modality mask $A\in\{0,1\}^{n\times m}$ can indicate availability of each of $m$ views. The loss is a defined teaching objective; the observed/missing indicator convention is supported by [Seaman et al., §2](SOURCES.md#missingness).

| State | Mathematical record | Meaning |
|---|---|---|
| Observed zero | $M_{ij}=1,\ x_{ij}=0$ | A recorded measurement, with assay-specific detection limits |
| Missing feature value | $M_{ij}=0$ | No measured value available |
| Missing modality | $A_{i,m}=0$ | Whole view unavailable; reason retained |
| Excluded observation | $i\notin I_{\rm retained}$ | Row omitted by a documented rule |
| Structurally undefined feature | Separate schema/status | Not necessarily a meaningful zero or ordinary missing value |

In the synthetic row $(2,\text{missing},0)$, mask is $(1,0,1)$; its observed mean is $(2+0)/2=1$. Filling the missing entry with zero instead changes the all-three mean to $2/3$. Multiplying NaN by zero can still produce NaN in software; selecting $\Omega$ is safer than assuming a mask multiplication fixes arithmetic.

Here $I_{\rm retained}$ is the set of retained observation identifiers, and $\hat x_{ij}$ is a proposed reconstruction of an entry. Missingness completely at random, conditional on observed variables, or dependent on unobserved values lead to different inference assumptions. None is established just from the mask. [Seaman et al., §§2 and 5](SOURCES.md#missingness) E18 ATAC's local transfer unavailability is not evidence of biologically closed chromatin.

Across-stage ATAC intervals require schema alignment before a zero-filled union could even be interpreted. No missing value is inferred or imputed in Phase 2A.
