# Identifiability of latent representations

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Same observations, different latent descriptions

A model is identifiable when its observable distribution determines its parameters, subject to explicitly permitted symmetries. A fitted optimum can be numerically unique under one algorithm while the model remains statistically nonidentifiable. Conversely, an identifiable model can be difficult to estimate from limited/noisy data.

For \(X\approx ZW\), Z:n×k, W:k×p, any invertible Q:k×k gives \(ZW=(ZQ)(Q^{-1}W)\). Additional constraints restrict Q but do not automatically eliminate ambiguity.[^1]

| Family | Ambiguity to acknowledge |
|---|---|
| PCA | Simultaneous sign changes; rotations within repeated-eigenvalue eigenspaces |
| Gaussian factor analysis | Orthogonal rotations of loadings/latent factors under isotropic latent prior |
| ICA | Scaling and permutation under standard source assumptions |
| NMF | Positive component scaling, permutation and potentially other factorizations |
| Tucker | Factor-basis changes compensated in the core |

ICA's stronger distributional assumptions and NMF's nonnegativity provide different constraints, not universal identification of biological programs.[^2][^3]

## A tangible symmetry

If one NMF column W[:,j] doubles while row H[j,:] halves, their contribution to WH is unchanged. A researcher could report a doubled “program score” without any change in the represented measurements. Normalization conventions must therefore accompany interpretations.

For this project, a factor name must be supported by feature weights, uncertainty and independent biological evidence; factor index and sign are not biological identities. A shared multimodal factor can describe covariance without identifying a causal regulator. Disconnected missing-view patterns can add alignment ambiguities.

Addressing identifiability may require constraints, anchors, priors or independent measurements, each with assumptions and cost. No arbitrary orientation is selected as biological truth. Phase 2B documents these issues before any deep representation study or model fitting, and makes no novelty claim about resolving them.

## Evidence

[^1]: Boyd S; Vandenberghe L (2018). [Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares](https://stanford.edu/~boyd/vmls/). See [access record](SOURCES.md#vmls).
[^2]: Hyvärinen A; Oja E (2000). [Independent Component Analysis: Algorithms and Applications](https://www.cs.helsinki.fi/u/ahyvarin/papers/NN00new.pdf). See [access record](SOURCES.md#ica).
[^3]: Lee DD; Seung HS (1999). [Learning the parts of objects by non-negative matrix factorization](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/lee-nature-99.pdf). See [access record](SOURCES.md#nmf).
