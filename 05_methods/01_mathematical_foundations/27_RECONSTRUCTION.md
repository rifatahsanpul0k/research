# 27. Reconstruction

Let $f:\mathbb R^p\to\mathbb R^d$ construct coordinates $z_i=f(x_i)$ and $g:\mathbb R^d\to\mathbb R^p$ reconstruct $\hat x_i=g(z_i)$. Across $n$ observations,
$$
X\ (n\times p)\xrightarrow{f}Z\ (n\times d)
\xrightarrow{g}\hat X\ (n\times p).
$$
“Encoder” and “decoder” name the two functions here; no architecture is specified. A squared reconstruction loss is $\|X-\hat X\|_F^2=\sum_{i,j}(x_{ij}-\hat x_{ij})^2$. The subscript $F$ resolves ambiguity in the prompt's matrix norm. [Low-rank mathematics](SOURCES.md#bhk)

Toy $x=(2,1,0)^\top$, $f(x)=(x_1,x_2)^\top$, $g(z)=(z_1,z_2,0)^\top$ reconstructs exactly. For $x=(8,7,6)^\top$, the same functions reconstruct $(8,7,0)^\top$, with squared error $6^2=36$. A map can look good for one observation while losing an entire feature for another.

Loss depends on units. Multiplying feature $j$ by $c$ multiplies its squared residual contribution by $c^2$. Centering, scaling and masking define what reconstruction means. Count likelihood losses and squared errors express different observation assumptions; no preferred loss is chosen.

Perfect reconstruction does not guarantee useful compression (the identity map is perfect), biological interpretation, artifact removal or held-out performance. It may reconstruct depth or contamination accurately. A small average loss may hide errors in a rare population. Latent size, feature weighting and uncertainty must accompany the score.

No research encoder or decoder is trained. The functions above are hand-defined demonstrations of the mathematics behind future representations.
