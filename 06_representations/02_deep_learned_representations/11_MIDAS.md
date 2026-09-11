# MIDAS

Phase 2C · method study · studied_not_fitted · not_reproduced.

MIDAS (He et al., 2024) addresses mosaic RNA/ADT/ATAC integration with variational inference, modality alignment and information-theoretic disentanglement. Its intended biological factor \(c\) and technical factor \(u\) are **not** interchangeable with a generic shared/private modality decomposition.[^1]

The paper factorizes
\[
p(x,s,c,u)=p(c)p(u)p(s\mid u)\prod_{m\in O_i}p(x^{(m)}\mid c,u).
\]
Here \(O_i\) is the observed modality set, \(c\in\mathbb R^{d_c}\), \(u\in\mathbb R^{d_u}\), and \(s\) is categorical batch identity. Both priors are standard Gaussians; a batch decoder uses \(u\). Published observation likelihoods are **Poisson for RNA and ADT and Bernoulli for ATAC**. Product-of-experts inference combines available inputs; self-supervised posterior regularization aligns modalities. The integrated observation embedding is the posterior mean of \(c\), not the full concatenation of technical and intended biological factors.[^1]

**Original reasoning:** if every embryo at one stage belongs to one batch, reconstructing batch from \(u\) and discouraging batch information in \(c\) may allocate stage information to \(u\). The factorization specifies desired roles but does not prove their biological identification. More data of the same confounded design do not logically disambiguate the factors.

For a hypothetical observation with RNA and ADT, \(O_i=\{R,P\}\); there is no ATAC likelihood term for that observation. A decoded ATAC vector has length \(p_A\), but it remains conditional generation. Dropping an observed modality during training is a modeling exercise, not an experiment measuring its absence.

Official code is [labomics/midas](https://github.com/labomics/midas). Mosaic integration, missing-feature generation and knowledge transfer are reported capabilities, with no performance conclusion transferred to our datasets. Feature provenance, shared populations, batch confounding and count-model adequacy remain unresolved project questions.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Modality encoders, product-of-experts inference and count/batch decoders |
| Training objective | ELBO, self-supervised modality alignment and information constraints |
| Biological prior | Intended biological/technical separation; conditional independence |
| Downstream model | Posterior mean of c; separate mapping or predictive tasks |
| Evaluation | Disentanglement, preservation and transfer need distinct evidence |

## Evidence

[^1]: [MIDAS: original source and access notes](SOURCES.md#midas).

