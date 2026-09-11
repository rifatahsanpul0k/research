# Log transformation

The common transform (x'=\log(1+x)) compresses large values and keeps zero at zero. For 0, 1, 3, and 8 it gives 0, 0.693, 1.386, and 2.197 (natural log). It changes additive differences and variance, reduces the leverage of very abundant features, and does not make a count matrix Gaussian or remove depth by itself. Applying it before or after normalization produces different quantities and must be recorded.

For RNA, log1p is often used for exploratory summaries after size adjustment; ADT and other modalities may need background-aware alternatives. ATAC pipelines commonly use TF-IDF rather than log1p alone. The transform preserves row/column shape and zero positions but changes distances and feature weighting, which later affects similarity. A log-transformed value must never be described as a molecule count. Evidence: OSCA [S38], SCnorm [S40], and sctransform’s explicit comparison with pseudocount/log heuristics [S37].
