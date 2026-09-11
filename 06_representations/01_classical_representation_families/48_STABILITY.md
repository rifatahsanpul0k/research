# Representation stability

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Stability is sensitivity under a specified change

A representation can change with random initialization, resampling, measurement perturbation, preprocessing, feature selection or parameter choice. Specify what changes, what stays fixed and how the resulting objects are compared. A fixed seed addresses one computational variation source; it does not establish sampling or biological stability.

For two aligned score tables Z,Z′:n×k with rotational ambiguity, a possible discrepancy is \(\min_{Q^TQ=I}\|Z-Z'Q\|_F\), with Q:k×k. This compares coordinates after an allowable orthogonal change of basis. It is an assessment definition, not a score computed here. More general factor models may require scale/permutation alignment rather than only rotations. ICA's ambiguity and PCA's basis dependence explain why raw coordinate differences can mislead.[^1][^2]

Neighborhood stability could compare set overlap on a common reference universe; cluster stability must allow label permutation; coupling stability requires common mass/identity conventions. None measures the same property as reconstruction or biological correctness.

## Project implications

A feature close to a selection threshold may enter or leave J under slight perturbation. A near-tied distance may swap KNN membership. PCA directions may move substantially when eigenvalues are close even if the leading subspace changes little. These mechanisms motivate the future choice of a comparison object rather than proving instability of any project result.

Sampling units matter: resampling spots within one section does not simulate independent embryos. Processing all data before a split can make apparent stability optimistic. External priors can be stable because they are fixed while still being inappropriate for a tissue.

Stability assessment adds repeated-fit/search cost and storage for comparison objects; no resampling, benchmarking or sensitivity experiment occurs now. A future authorized study must distinguish numerical repeatability, statistical robustness and biological evidence. Stable nuisance structure is still nuisance; an unstable component is not automatically meaningless.

## Evidence

[^1]: Hyvärinen A; Oja E (2000). [Independent Component Analysis: Algorithms and Applications](https://www.cs.helsinki.fi/u/ahyvarin/papers/NN00new.pdf). See [access record](SOURCES.md#ica).
[^2]: Deisenroth MP; Faisal AA; Ong CS (2020). [Mathematics for Machine Learning](https://mml-book.github.io/). See [access record](SOURCES.md#mml).
