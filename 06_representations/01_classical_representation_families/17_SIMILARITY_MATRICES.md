# Pairwise similarity matrices

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Similarity is an object with a definition

Write \(B_{ij}=s(x_i,x_j)\), \(B:n\times n\), for \(X:n\times p\). B avoids confusing this matrix with spatial S. Examples are cosine similarity \(x_i^Tx_j/(\|x_i\|\|x_j\|)\), correlation of the two feature profiles, or Gaussian affinity \(\exp[-\|x_i-x_j\|^2/(2\sigma^2)]\), σ>0. Norm-zero and constant-profile cases require explicit handling rather than invented similarities.[^1]

Unlike a feature table, column j of B means relation to reference observation j. A score of 0.9 has no universal biological interpretation: it depends on the similarity definition, input units and reference preparation. Correlation may be negative; Gaussian affinity is positive. A similarity need not be a metric, probability, or positive-semidefinite kernel.

## What is retained and lost

Cosine similarity discards individual vector magnitudes. For example (1,2,3) and (2,4,6) have similarity 1 although their feature amounts differ. Correlation also removes each vector's additive mean. These invariances can be deliberate, but they do not prove that the removed amounts are biologically irrelevant. Gaussian affinity retains Euclidean distances mathematically when σ is known and positive affinities are stored exactly: \(d_{ij}=\sqrt{-2\sigma^2\log B_{ij}}\). Thresholding or numerical underflow can destroy that reversibility.

Dense B uses O(n²) storage; direct pairwise evaluation of p-dimensional features typically costs O(n²p). Sparse thresholding changes the represented relationships. Row-normalizing B gives transition probabilities only if entries are nonnegative and row sums positive; the resulting matrix need not be symmetric or retain the kernel property.

In this project, molecular and spatial similarities should retain their distinct provenance. Combining them requires a declared mechanism; high similarity is not biological equivalence, signaling, lineage or regulatory evidence. Missing modalities cannot receive a fabricated similarity of zero or one. See [kernels](18_KERNELS.md) for the additional PSD requirement.

## Evidence

[^1]: Blum A; Hopcroft J; Kannan R (2020). [Foundations of Data Science](https://www.cs.cornell.edu/jeh/book.pdf). See [access record](SOURCES.md#bhk).
