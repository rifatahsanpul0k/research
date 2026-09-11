# Raw feature space

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Definition and preserved information

With \(X\in\mathbb R^{n\times p}\), the identity representation is \(R=X\). Keeping the matrix, identifiers, missingness mask and measurement metadata preserves the stored entries exactly. It does not recover molecules that were never measured. “Raw” must identify a level: sequencer reads, quantified counts and an already processed H5AD X are different objects. Do not relabel a processed matrix as counts from its filename or integer-looking entries.

Dense storage requires \(np\) numbers; CSR storage requires values and feature indices for nonzeros plus \(n+1\) row pointers. Algebraic sparsity and biological absence are different. A stored zero remains an observed numerical value; an unmeasured entry needs a mask. Direct feature vectors retain explicit gene/peak/antibody identities and can be used for inspection or models whose likelihood expects the original measurement scale.[^1]

## Geometry, usefulness and limits

For Euclidean distance, \(\|x_i-x_j\|_2^2=\sum_{g=1}^p(x_{ig}-x_{jg})^2\). Multiplying one feature by c multiplies its contribution by \(c^2\). Thus named axes are interpretable, but geometry depends on units and transformations. Many features can accumulate measurement noise; large p alone does not prove all distances are unreliable. High-dimensional behavior needs assumptions about dependence, noise and relevant signal.[^2]

A raw representation remains useful when exact feature traceability or a measurement-aware model is required. Dimensional reduction is not a prerequisite. For this project, a raw RNA block and an ADT block may coexist as separate tables. Treating their union as one metric space requires a stated weighting and pairing rule; merely storing them does not supply one. No raw data were modified. Conditional benefits here are mathematical properties, not performance claims for A1 or the mouse stages.

## Evidence

[^1]: Boyd S; Vandenberghe L (2018). [Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares](https://stanford.edu/~boyd/vmls/). See [access record](SOURCES.md#vmls).
[^2]: Blum A; Hopcroft J; Kannan R (2020). [Foundations of Data Science](https://www.cs.cornell.edu/jeh/book.pdf). See [access record](SOURCES.md#bhk).
