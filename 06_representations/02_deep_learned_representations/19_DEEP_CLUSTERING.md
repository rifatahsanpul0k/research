# Deep clustering

Phase 2C · method study · studied_not_fitted · not_reproduced.

Deep clustering couples feature learning and a clustering objective, so the geometry itself changes as assignments are refined. DEC (Xie et al., 2016) uses an initialized neural embedding with soft Student-t assignments and a sharpened target distribution. Its optimization is different from running a clustering algorithm once on a fixed representation.[^1]

For \(z_i,\mu_k\in\mathbb R^d\), define
\[
q_{ik}\propto(1+\|z_i-\mu_k\|^2/\alpha)^{-(\alpha+1)/2},
\quad f_k=\sum_iq_{ik},\quad
p_{ik}=\frac{q_{ik}^2/f_k}{\sum_jq_{ij}^2/f_j},
\quad J=\sum_{ik}p_{ik}\log(p_{ik}/q_{ik}).
\]
Normalize \(q\) across clusters; \(\alpha>0\) is degrees of freedom and \(f_k>0\) is soft frequency. The target \(P\) is a model-derived sharpening of \(Q\), not biological truth.[^1]

scDeepCluster (Tian et al., 2019) combines explicit modeling of RNA counts with deep embedding/clustering; DESC (Li et al., 2020) studies iterative deep clustering with batch-effect removal. Their purposes are verified from original publications; this note makes no equivalence claim about their noise models or optimization schedules.[^2][^3]

**Original reasoning:** if a technical batch initially forms a compact group, sharpening its assignments can make the separation stronger. High silhouette after such optimization is not independent evidence of biological correctness. Conversely, a biological continuum need not have sharply separated groups.

The representation \(Z\), soft assignments \(Q\), refined targets \(P\) and final discrete labels are four different artifacts. Choosing a cluster count is a modeling decision. This phase neither chooses that count nor fits any of these models.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | DEC embedding plus cluster centers; scDeepCluster/DESC are distinct adaptations |
| Training objective | Self-refining clustering loss, with method-specific reconstruction stages |
| Biological prior | Cluster geometry assumptions; count assumptions for scDeepCluster |
| Downstream model | Discrete/soft cluster assignment; further annotation remains separate |
| Evaluation | Clustering scores, stability and biological evidence differ |

## Evidence

[^1]: [DEC: original source and access notes](SOURCES.md#dec).
[^2]: [SCDEEPCLUSTER: original source and access notes](SOURCES.md#scdeepcluster).
[^3]: [DESC: original source and access notes](SOURCES.md#desc).

