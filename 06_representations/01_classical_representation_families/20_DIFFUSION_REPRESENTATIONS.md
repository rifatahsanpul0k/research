# Diffusion representations

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## A random walk constructed from relationships

Let \(B:n\times n\) be symmetric and nonnegative, with positive row sums \(d_i=\sum_jB_{ij}\). Let \(D_d=\operatorname{diag}(d_1,\ldots,d_n)\), \(P=D_d^{-1}B\). Then P is row-stochastic: P_ij is a one-step transition probability and \((P^t)_{ij}\) a t-step probability for integer t≥1. This constructed random walk is not an observed cell movement process.[^1]

For a connected reversible chain, stationary weights are \(\pi_i=d_i/\sum_jd_j\). Define
\[
D_t^2(i,\ell)=\sum_{j=1}^n\frac{((P^t)_{ij}-(P^t)_{\ell j})^2}{\pi_j}.
\]
With right eigenvectors \(\psi_r:n\) orthonormal under π and eigenvalues λ_r, the nonconstant coordinates \(\lambda_r^t\psi_r(i)\) express this diffusion geometry. Keeping k components gives n×k coordinates; retaining all nonconstant components gives the spectral distance identity under these assumptions.[^1]

## Interpretation and limits

Two observations can have similar multi-step transition profiles through intermediates even without a strong direct affinity. Bandwidth, normalization and diffusion time determine which connections matter. Disconnected components need separate treatment; isolated observations have no defined row normalization. A normalization intended to reduce sampling-density effects is another model choice.

The word diffusion here denotes a mathematical operator. It is neither measured molecular diffusion nor a GNN. No message-passing neural model is studied. A graph is one interpretation of the affinity, while P and the diffusion coordinates are separate representation objects.

In this project, RNA relationships and spatial connectivity may disagree. A constructed random walk can traverse numerical bridges caused by mixtures or noise; it does not prove a developmental trajectory. Dense affinities store O(n²), a sparse neighbor operator O(nk_neighbor), and eigensolver cost depends on sparsity and the retained rank. Computing all powers Pᵗ densely is unnecessary for eigen-coordinate construction. Truncation loses fast-decaying spectral components, and t is not embryonic time. No project diffusion map was fitted.

Official implementation context: [destiny: diffusion maps](https://bioconductor.org/packages/release/bioc/html/destiny.html).[^2]

## Evidence

[^1]: Coifman RR; Lafon S (2006). [Diffusion maps](https://www.math.ucdavis.edu/~strohmer/courses/270/diffusion_maps.pdf). See [access record](SOURCES.md#diffusion).

[^2]: Official documentation. [destiny: diffusion maps](https://bioconductor.org/packages/release/bioc/html/destiny.html); [access record](SOURCES.md#destiny).
