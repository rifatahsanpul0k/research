# MOFA and MOFA+ multimodal factor models

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Shared observations, different feature spaces

For v modalities with aligned observation identities, write the Gaussian-view mean model
\[
X^{(m)}\approx ZW^{(m)},\quad X^{(m)}:n\times p_m,
\quad Z:n\times k,\quad W^{(m)}:k\times p_m.
\]
MOFA combines a latent factor model with view-specific weights, likelihoods and sparsity/relevance structure. Gaussian, Bernoulli and Poisson likelihoods allow different observation types; the product is a linear predictor, not necessarily raw reconstructed counts for every likelihood. The original model accommodates missing entries and whole missing views for observations.[^1]

MOFA+ extends the framework to groups, with \(Z^{(g)}:n_g\times k\), view weights and group/view relevance parameters. Its variational inference is designed for larger multi-modal single-cell collections. Shared factors can contribute strongly to one view and weakly to another. “Shared” therefore does not mean equally informative in every modality.[^2]

## What missing-view handling means

A mask \(\Omega^{(m)}:n\times p_m\) identifies available entries. Observations absent from a view do not contribute that view's likelihood terms. The official FAQ says missing values are ignored in the likelihood rather than secretly imputed before fitting. It also cautions about input normalization and view dimensional imbalance.[^3]

**Mathematical limitation:** if two modalities are measured on completely disjoint observations, with no linking information, a shared row index cannot be manufactured. Independent rotations/relabelings of disconnected latent blocks can leave observed likelihoods unchanged. Support for incomplete paired views is not an automatic solution to arbitrary unpaired matching. Any inferred missing-view values are model-dependent predictions, not new measurements.

## Interpretation and project boundary

For A1, verified pairing can establish the same spot index across RNA and ADT, while each modality keeps its own feature axis. Different p_m are permitted by the mathematical model; equal relevance is not guaranteed. E18 ATAC remains unavailable; missing-view capability cannot verify its biology or acquisition provenance. A latent factor may capture technical variation, mixtures or state variation; pathway interpretations remain hypotheses requiring external support.

Keep factor scores, view-specific loadings, masks, preprocessing and model uncertainty together. A single factor score is not a measured regulator. Spatial position is not intrinsically encoded by this baseline formulation; spatial extensions are separate methods. Approximate storage is O(k(n+Σp_m)) plus data/masks and variational parameters; Gaussian updates often involve O(nkΣp_m) work per pass, with non-Gaussian and grouped details affecting cost. Original papers and official MOFA2 documentation were read; no factors were fitted. Official MOFA and MOFA2/mofapy2 provenance is recorded without claiming software reproduction.

## Evidence

[^1]: Argelaguet R; Velten B; Arnol D; Dietrich S; Zenz T; Marioni JC; Buettner F; Huber W; Stegle O (2018). [Multi-Omics Factor Analysis—a framework for unsupervised integration of multi-omics data sets](https://link.springer.com/article/10.15252/msb.20178124). See [access record](SOURCES.md#mofa).
[^2]: Argelaguet R; Arnol D; Bredikhin D; Deloro Y; Velten B; Marioni JC; Stegle O (2020). [MOFA+: a statistical framework for comprehensive integration of multi-modal single-cell data](https://link.springer.com/article/10.1186/s13059-020-02015-1). See [access record](SOURCES.md#mofa_plus).
[^3]: Official project maintainers (2026). [MOFA2 documentation and FAQ](https://biofam.github.io/MOFA2/faq.html). See [access record](SOURCES.md#mofa_doc).
