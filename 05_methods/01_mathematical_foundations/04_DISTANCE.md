# 04. Distance

For aligned vectors $x,y\in\mathbb R^p$, define
$$
d_2(x,y)=\sqrt{\sum_{j=1}^p(x_j-y_j)^2},\qquad
d_1(x,y)=\sum_{j=1}^p|x_j-y_j|.
$$
The Minkowski family uses exponent $a\ge1$:
$$
d_a(x,y)=\left(\sum_j|x_j-y_j|^a\right)^{1/a}.
$$
Here $p$ denotes feature count; $a$ avoids overloading it with the norm exponent. The prompt's $d_p$ uses $p$ in that second sense. Exponents below one generally fail the triangle inequality and are not metrics. [VMLS](SOURCES.md#vmls)

A metric has nonnegativity, identity of indiscernibles, symmetry and the triangle inequality. For toy rows $x_1=(2,1,0)^\top$, $x_2=(3,0,1)^\top$, the difference is $(-1,1,-1)^\top$: Euclidean distance $\sqrt3$, Manhattan distance 3. Squared Euclidean distance is useful as a loss but is not itself a metric: for points 0,1,2, $4>1+1$.

Changing one feature's units multiplies its squared contribution by the square of that factor. Multiplying all features by a positive constant preserves distance ordering but scales distance magnitudes; feature-specific scaling can change ordering. Log transforms, filtering and normalization can all change ordering. Discarding zero entries in sparse storage must not discard differences where only one observation has a nonzero value.

With many noisy dimensions, aggregate distances may be dominated by noise and concentrate; this needs distributional assumptions, not merely large $p$. [High-dimensional foundations](SOURCES.md#bhk)

A small molecular distance does not establish common ancestry, cell identity, regulatory coupling or spatial proximity. Distance measures the specified numerical space. For $S$, it represents physical distance only with a calibrated frame. The assumptions and feature alignment come before any biological interpretation.
