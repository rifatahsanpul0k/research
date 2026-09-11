# Integrative NMF and LIGER

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Shared and dataset-specific components

Classical iNMF uses nonnegative blocks \(X^{(m)}\in\mathbb R_+^{n_m\times p}\) with a **common feature axis**. Observations need not be the same across datasets. A row-oriented formulation is
\[
\min_{H_m,W,V_m\ge0}\sum_{m=1}^v\left\|X^{(m)}-H_m(W+V_m)\right\|_F^2
+\lambda\sum_{m=1}^v\|H_mV_m\|_F^2,
\]
where \(H_m:n_m\times k\), \(W,V_m:k\times p\), v is the number of datasets and \(\lambda\ge0\). W is shared; V_m is dataset-specific; H_m supplies observation coordinates. Penalizing the dataset-specific contribution regulates its use.[^1]

The official runINMF page writes features-by-observations and contains inconsistent prose about H's orientation. The products above explicitly transpose that convention and are dimensionally valid. The package distinguishes the nonnegative factorization from subsequent alignment procedures, and lists unshared-feature extensions separately.[^2]

## Interpretation and applicability

A shared loading structure expresses a modeling constraint, not demonstrated shared biology. Dataset-specific components can include real modality/tissue effects as well as technical differences. Increasing alignment pressure can remove differences one intended to study; no lambda is chosen here.

RNA and raw antibody panels do not automatically share features. An RNA–ATAC use of classical iNMF requires a justified common feature representation, such as a separately defined gene-linked accessibility quantity; that derived value is not measured RNA. Later unshared-feature LIGER extensions must not be silently attributed to this core objective.

For A1, paired spot IDs are useful metadata but do not make 18,085 RNA features identical to 31 antibody features. For mouse stages, differing ATAC peak sets remain a feature-harmonization problem. Missing modalities are not represented by setting X_m to zero. Storage is O(kΣn_m+vkp); iterative dense products cost roughly O(kpΣn_m) per pass. Initialization and model rank matter because fitting is nonconvex. The method and official code have been studied, not reproduced.

## Evidence

[^1]: Welch JD; Kozareva V; Ferreira A; Vanderburg C; Martin C; Macosko EZ (2019). [Single-Cell Multi-omic Integration Compares and Contrasts Features of Brain Cell Identity](https://macoskolab.com/wp-content/uploads/2019/06/liger_paper.pdf). See [access record](SOURCES.md#liger).
[^2]: Official project maintainers (2026). [Perform iNMF on scaled datasets — runINMF](https://welch-lab.github.io/liger/reference/runINMF.html). See [access record](SOURCES.md#liger_doc).
