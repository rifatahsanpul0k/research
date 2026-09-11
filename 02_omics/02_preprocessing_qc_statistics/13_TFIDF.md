# TF-IDF for sparse accessibility counts

For accessibility counts (X_{ij}), term frequency is often (TF_{ij}=X_{ij}/\sum_kX_{ik}). Let (df_j=\sum_i1(X_{ij}>0)) be the number of observations containing peak (j); inverse document frequency is a decreasing function such as (IDF_j=\log(n/df_j)) (implementations may add a pseudocount). The product (TF_{ij}IDF_j) downweights peaks seen in nearly every observation and emphasizes peaks informative for subsets [S44,S45].

Toy: with n=4 and df=(4,1), IDF=(0,log 4); the ubiquitous peak receives zero under this formula while the rare peak is retained. This is a statistical reweighting, not a claim that ubiquitous chromatin is unimportant. Choices of denominator, smoothing and matrix orientation must be recorded. TF-IDF is not RNA normalization and does not repair missing modality or poor library quality. We explain the transformation only; no SVD or benchmark is performed. Evidence: Cusanovich et al. [S44], Stuart et al. [S45].
