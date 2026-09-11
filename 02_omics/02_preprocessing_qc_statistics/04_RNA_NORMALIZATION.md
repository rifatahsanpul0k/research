# RNA library-size normalization

For nonnegative matrix entries, library-size scaling is

\[
\tilde X_{ij}=X_{ij}/L_i\times c,
\]

where (c) is a declared target (for example, a synthetic 10,000). It assumes that most features do not change compositionally enough to make total RNA a misleading denominator; strong global shifts, unequal capture, and zero-rich observations challenge that assumption [S40,S41]. It changes row totals and the relative influence of depth, while preserving zero locations and within-row ratios when (L_i>0). It does not recover molecule counts or remove all technical effects.

Example: row (8,0,3), (L=11,c=10) becomes (7.27,0,2.73). The values are scaled abundances, not counts. Pool-based scran size factors and model-based sctransform address different assumptions; no best method is selected here. In spatial and multimodal data, denominators may reflect footprint, antibody background or fragments rather than RNA capture. Fit any estimated normalization parameters on training data only in predictive settings. Evidence: SCnorm [S40], scran [S41], sctransform [S37], OSCA [S38].
