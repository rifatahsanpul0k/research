# totalVI

Phase 2C · method study · studied_not_fitted · not_reproduced.

**FACT:** totalVI (Gayoso et al., 2021) jointly models paired RNA and antibody-derived protein counts, including protein background and batch effects. It produces a shared probabilistic representation and decoded molecular estimates.[^1]

Let \(X\in\mathbb N_0^{n\times G}\) and \(Y\in\mathbb N_0^{n\times T}\) have exactly aligned observations. For \(z_i\in\mathbb R^d\) and batch \(s_i\), an RNA decoder supplies \(\rho_i\in\Delta^{G-1}\):
\[
x_{ig}\sim\operatorname{NB}(\ell_i\rho_{ig},\theta_g).
\]
For protein \(t\), let background rate \(\beta_{it}>0\), foreground multiplier \(\alpha_{it}\ge1\), background probability \(\pi_{it}\in[0,1]\), and inverse dispersion \(\psi_t>0\). Conditional on these,
\[
p(y_{it})=\pi_{it}\operatorname{NB}(y_{it};\beta_{it},\psi_t)
 +(1-\pi_{it})\operatorname{NB}(y_{it};\beta_{it}\alpha_{it},\psi_t).
\]
Background rates have batch-dependent log-normal priors; decoder networks parameterize foreground scaling and mixture probabilities. The joint encoder supports variational inference and ELBO-based learning. Current documentation distinguishes latent from observed RNA library handling.[^2]

This is a mixture of **two count distributions**, not a rule that all small protein values are missing. A denoised foreground estimate, foreground probability and raw ADT count are different quantities. Posterior variation is conditional on the model and observations, not automatic calibrated uncertainty about antibody specificity.[^1][^2]

## Why this exceeds concatenation

Concatenation creates \([X,Y]\in\mathbb R^{n\times(G+T)}\). It supplies no RNA likelihood, protein-specific mixture, latent posterior or batch-conditioned decoder. totalVI adds those modeling assumptions. A shared \(z\) can support both decoders without requiring RNA gene \(g\) to equal protein \(t\).

**Synthetic mixture calculation:** if \(\beta=2,\alpha=5,\pi=0.75\), the mixture mean is \(0.75(2)+0.25(10)=4\). The foreground mean is \(10\); neither value is the observed count. Reporting \(4\) as measured protein abundance would conflate an expectation with a measurement.

**Project interpretation:** A1/D1 motivate this study because RNA and ADT are recorded, but a spatial spot can mix cells and have spatially varying background. This note makes no compatibility verdict. Count provenance, antibody panel semantics, missing panels, matched rows and batch hierarchy must be verified before fitting. Strong RNA fit can coexist with poor protein background separation, especially where foreground/background overlap. Protein count abundance is not protein activity.

[scvi-tools](https://github.com/scverse/scvi-tools) is the official maintained implementation. No normalization, fitting, denoising or imputation was performed.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Joint RNA/ADT variational encoder; distinct RNA and protein decoders |
| Training objective | Joint likelihood ELBO with latent/background inference |
| Biological prior | RNA count and protein foreground/background assumptions; paired identity |
| Downstream model | Shared Z for tasks; denoising and DE use decoded distributions |
| Evaluation | Molecular fit, background separation, uncertainty and biological checks |

## Evidence

[^1]: [TOTALVI: original source and access notes](SOURCES.md#totalvi).
[^2]: [TOTALVI_DOC: original source and access notes](SOURCES.md#totalvi_doc).

