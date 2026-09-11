# Feature selection changes representation

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Selection map

For \(X\in\mathbb R^{n\times p}\), let \(J\subseteq\{1,\ldots,p\}\) contain r retained features. Then \(R=X_{[:,J]}\in\mathbb R^{n\times r}\). For a fixed J this is a linear coordinate projection; choosing J from data or labels is an additional, often nonlinear, mechanism. Unselected values cannot generally be recovered from R. Storing J preserves the meaning and ordering of retained columns.[^1]

| Rule | What determines J | Interpretation risk |
|---|---|---|
| Variance selection | Empirical dispersion | Large variance may reflect technical scale |
| Highly variable genes (HVGs) | Assay-aware mean–variance treatment | Not simply the largest raw count variances |
| Marker selection | Previously supported marker lists | Context, specificity and annotation circularity |
| Supervised selection | Association with a target | Target leakage and overfitting |
| Biological-prior selection | Pathway, regulator or other annotation | Incomplete and uneven prior coverage |

HVG and integration preprocessing affect what downstream methods can retain; they are not neutral cleaning operations.[^2] GO annotations explicitly carry evidence types, so prior-based inclusion should preserve those evidence records.[^3]

## Concrete consequence

For synthetic \(x_1=(4,0,1)^T\), \(x_2=(5,1,1)^T\), selecting only feature 3 makes both representations equal to 1, although the original vectors differ. Equality after projection establishes equality only on the retained coordinate. A low-variance feature may still matter for a task; this phase does not choose J.

Future supervised selection must be fitted on training observations, with donor/section-aware splits where appropriate, then applied unchanged to validation data. A training-derived J is part of the fitted representation. Selection costs depend on the rule: a single dense variance pass is O(np), output storage O(nr); label-based searches may cost substantially more. Missingness must be carried through, not replaced by zero.

## Evidence

[^1]: Boyd S; Vandenberghe L (2018). [Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares](https://stanford.edu/~boyd/vmls/). See [access record](SOURCES.md#vmls).
[^2]: Argelaguet R; Cuomo ASE; Stegle O; Marioni JC (2021). [Computational principles and challenges in single-cell data integration](https://www.nature.com/articles/s41587-021-00895-7). See [access record](SOURCES.md#integration).
[^3]: Official project maintainers (2026). [Guide to GO evidence codes](https://geneontology.org/docs/guide-go-evidence-codes/). See [access record](SOURCES.md#go).
