# Tensor representations

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Axes must have compatible semantics

A tensor is an array with multiple axes. A proposed \(\mathcal X\in\mathbb R^{n\times p\times v}\) could mean observations×features×modalities only when each modality really uses the same p-feature schema and compatible observation IDs. A1's 18,085 genes and 31 ADTs cannot be stacked on one shared feature axis by numerical padding without a mapping and missingness semantics. Peak sets that differ across mouse stages similarly need alignment. A tuple of unequal matrices remains a legitimate alternative.

## CP and Tucker foundations

A rank-r CP approximation of an n×p×v tensor is
\[
\widehat{\mathcal X}_{ig m}=\sum_{\ell=1}^r A_{i\ell}B_{g\ell}C_{m\ell},
\]
where A:n×r, B:p×r, C:v×r. Each summand is an outer product across the three axes. A Tucker approximation is
\[
\widehat{\mathcal X}_{ig m}=\sum_{a=1}^{r_1}\sum_{b=1}^{r_2}\sum_{c=1}^{r_3}
\mathcal G_{abc}A_{ia}B_{gb}C_{mc},
\]
with core 𝓖:r₁×r₂×r₃ and A:n×r₁, B:p×r₂, C:v×r₃. CP ties components across modes; Tucker permits a core of interactions. Tensor order, matrix rank and tensor rank are distinct notions.[^1]

## Preservation and failure modes

Dense storage is O(npv); CP factors use O(r(n+p+v)), Tucker factors/core O(nr₁+pr₂+vr₃+r₁r₂r₃), excluding residuals and input data. Factorization is generally iterative; compact output does not guarantee a cheap or uniquely identified fit. CP has component scaling/permutation ambiguities, while Tucker allows changes of basis compensated by the core.

An observation×gene×stage tensor also requires comparable observational units across stages; anonymous spot 1 in different embryos is not one repeated cell. Structural missingness must be masked. Tensor Toolbox is linked from its official site and the foundational review; no tensor was assembled or decomposed from biological data.

## Evidence

[^1]: Kolda TG; Bader BW (2009). [Tensor Decompositions and Applications](https://www.math.ucdavis.edu/~saito/data/tensor/kolda-bader_tensor-decomp-siamrev.pdf). See [access record](SOURCES.md#tensor).
