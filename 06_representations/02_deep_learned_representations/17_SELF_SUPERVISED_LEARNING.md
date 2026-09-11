# Self-supervised learning

Phase 2C · method study · studied_not_fitted · not_reproduced.

Self-supervision constructs a learning target from available data rather than requiring an externally curated label for every observation. Targets can be a held-out feature, a second view, context, the original input, or a model-generated pseudo-label. These choices define different objectives, even with the same encoder.[^1][^2]

| Target | What is learned | Main interpretive risk |
| --- | --- | --- |
| Reconstruct input | Information useful for reconstruction | Technical variation may be reconstructed |
| Predict masked feature | Conditional structure among measured features | Artificial masks may differ from assay missingness |
| Contrast views | Agreement under a declared transformation | Relevant variation may be removed |
| Predict graph context | Structure conditional on supplied edges | Edge errors become learning targets |
| Predict pseudo-label | Agreement with current assignments | Errors can reinforce themselves |

For a feature mask \(M\in\{0,1\}^{n\times p}\), define a masked-prediction loss only on held-out entries, for example \(\sum_{ig:M_{ig}=0}(x_{ig}-\widehat x_{ig})^2\). Here zero in **M** denotes withholding by this convention; zero in **X** remains a measured numeric value. State the convention explicitly because software can use the opposite mask polarity.

Biological labels are limited and sometimes uncertain, making self-generated targets attractive, but removing annotation requirements does not remove assumptions. Feature order, selected genes, view corruption and graph construction are forms of supervision or prior structure.

**Project interpretation:** self-supervised means no externally supplied target for that objective. It does not mean unbiased, biologically validated or unable to leak information across donors. Pseudo-labels should be recorded as model outputs. No labels or masks are generated for our observations here.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Encoder chosen independently of self-supervision |
| Training objective | Reconstruction, masking, contrast, context or pseudo-label loss |
| Biological prior | The target-generation rule supplies inductive assumptions |
| Downstream model | Task head or analysis added after representation learning |
| Evaluation | Target prediction and later biology are separate |

## Evidence

[^1]: [DAE: original source and access notes](SOURCES.md#dae).
[^2]: [DEC: original source and access notes](SOURCES.md#dec).

