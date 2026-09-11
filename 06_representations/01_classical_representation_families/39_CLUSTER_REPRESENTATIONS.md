# Hard and soft cluster assignments

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Different summaries

A hard assignment \(z_i\in\{1,\ldots,k\}\) gives one category per observation. One-hot encoding has shape n×k with one 1 per row. Cluster numbers have no intrinsic order or distance: assigning cluster 3 does not mean three times cluster 1.

A soft representation \(P:n\times k\) satisfies P_ij≥0 and \(\sum_jP_{ij}=1\). It may be a model posterior \(P_{ij}=\Pr(z_i=j\mid x_i)\), or merely normalized membership weights. These meanings must be separated. In a mixture model,
\[
\Pr(z_i=j\mid x_i)=\frac{\pi_j f_j(x_i)}{\sum_\ell\pi_\ell f_\ell(x_i)},
\]
where π_j are prior mixture weights summing to one and f_j are component densities. Probabilities are conditional on that model.[^1]

## Loss and biological interpretation

Hard labels lose within-cluster variation; soft weights preserve relative membership uncertainty only under their stated construction. Neither retains all feature detail. Cluster permutations leave the partition unchanged. A numerical cluster is not automatically a cell type, spatial domain, disease subtype or developmental state.

High ARI/NMI/silhouette is not biological correctness. Agreement with annotations can be circular if those annotations helped select the representation. For spots, cluster structure may reflect mixtures or technical variation rather than a homogeneous cell population.

Hard label storage is O(n); dense soft memberships O(nk), plus parameters. Choosing k and fitting memberships requires a model/algorithm whose cost and randomness must be reported separately. Missing data support belongs to that estimator, not to the label format. In the toy, soft weights are explicitly constructed from prototype distances and are **not calibrated posteriors**. No project clustering, biological label assignment or validation score is computed.

## Evidence

[^1]: Blitzstein JK; Hwang J (2019). [Introduction to Probability, second edition](https://stat110.hsites.harvard.edu/). See [access record](SOURCES.md#prob).
