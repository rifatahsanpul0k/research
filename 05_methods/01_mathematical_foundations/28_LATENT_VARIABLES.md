# 28. Latent variables

A latent coordinate $z_i\in\mathbb R^d$, usually $d\ll p$, is constructed or inferred from observations. It is not directly measured by the assay. Stack $z_i^\top$ to obtain $Z\in\mathbb R^{n\times d}$. A deterministic embedding sets $z_i=f(x_i)$; a probabilistic model treats an unobserved variable through a conditional distribution such as $p(z_i\mid x_i)$. These are distinct uses of “latent.” [MML, probabilistic models](SOURCES.md#mml)

For a linear reconstruction $X\approx ZB^\top$, loadings $B\in\mathbb R^{p\times d}$ map latent axes back to features. If $R\in\mathbb R^{d\times d}$ is invertible, define $Z'=ZR$ and $B'=BR^{-\top}$. Then
$$
Z'B'^\top=(ZR)(R^{-1}B^\top)=ZB^\top.
$$
The same reconstruction can have different latent coordinates. Constraints may reduce ambiguity but need not grant a unique biological interpretation.

Measured feature $\ne$ latent variable $\ne$ biological mechanism. An axis associated with a marker set might be a candidate state score; it could also capture depth, mixed populations or batch. Biological interpretation requires independent context and evidence. [Measurement and replication limits](SOURCES.md#bio)

Sign flips, permutations and rotations mean that coordinate labels should not be treated as stable molecular identities without alignment and justification. An inferred “shared factor” also does not prove a direct RNA-to-protein or accessibility-to-expression mechanism.

Future study must ask how coordinates are identified, how uncertainty is represented, which observations fit them and whether their interpretation replicates. No factor model or neural latent model is implemented.
