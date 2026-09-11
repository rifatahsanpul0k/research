# Neural representation foundations

Phase 2C · method study · studied_not_fitted · not_reproduced.

For one observation let \(h^{(0)}=x\in\mathbb R^p\) be a **column vector**. A layer is
\[
h^{(\ell+1)}=\sigma(W^{(\ell)}h^{(\ell)}+b^{(\ell)}),
\quad W^{(\ell)}\in\mathbb R^{d_{\ell+1}\times d_\ell},
\quad b^{(\ell)}\in\mathbb R^{d_{\ell+1}}.
\]
Weights mix features; biases translate the preactivation; \(\sigma\) acts elementwise, for example \(\operatorname{ReLU}(a)=\max(0,a)\). A multilayer perceptron composes these maps. For observations in **rows**, the equivalent expression is \(H'= \sigma(HW^\top+\mathbf1 b^\top)\), with \(H\in\mathbb R^{n\times d_\ell}\). These conventions must not be mixed. Neural encoders parameterize deterministic maps or the parameters of distributions.[^1]

The embedding \(z=f_\phi(x)\in\mathbb R^d\) is an output of the fitted encoder, not the weights \(\phi\), reconstructed input, or task label. Multiple affine layers without nonlinear activations collapse algebraically to one affine map: \(W_2(W_1x+b_1)+b_2=(W_2W_1)x+W_2b_1+b_2\). Nonlinearity changes the available function class; it does not certify that its variation is biological.

**Project interpretation:** a row can be a spatial spot. The same equation can encode a mixture, and cannot convert it into a cell. Large gene panels also create many first-layer parameters: a hypothetical \(p=1000,d_1=20\) layer has \(1000(20)+20=20{,}020\) parameters. This arithmetic says nothing about the sample size needed for biological generalization. Fixed feature identity/order and preprocessing are part of the input contract.

See [the fixed toy](TOY_DEEP_REPRESENTATIONS.md) for one forward pass and [scalability](62_SCALABILITY.md) for width, minibatch and sparse-input costs.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | MLP encoder; task-specific head or decoder |
| Training objective | Chosen separately: reconstruction, likelihood, contrastive or supervised loss |
| Biological prior | None inherent; any biological constraint must be specified |
| Downstream model | Separate classifier, clustering procedure or regression head |
| Evaluation | Held-out task evidence and biological checks; no evaluation run |

## Evidence

[^1]: [AEVB: original source and access notes](SOURCES.md#aevb).

