# Phase 2A concept map

This diagram connects concepts; it is not a graph constructed from biological observations.

~~~mermaid
flowchart TD
    A["Omics matrix: units, rows, features, masks"] --> B["Vectors and matrix shapes"]
    B --> C["Geometry and probability"]
    C --> D["Distance, similarity and dependence"]
    D --> E["Linear algebra: maps, rank, eigenvectors, SVD"]
    E --> F["Dimension, compression and information loss"]
    F --> G["Constructed or inferred latent coordinates"]
    G --> H["Objectives, gradients and regularization"]
    H --> I["Computational, statistical and biological evaluation"]
    R["RNA"] --> J["Future representation learning: no family selected"]
    P["ADT"] --> J
    T["ATAC"] --> J
    S["XY coordinates: units and frame"] --> J
    I --> J
    M["Pairing, missingness, provenance and held-out design"] --> J
~~~

Read [topics 01–12](01_DATA_AS_MATHEMATICAL_OBJECTS.md) for observation-to-probability language, [13–24](13_RANK_AND_BASIS.md) for linear structure, optimization and geometry, and [25–36](25_KERNELS.md) for kernels, information, latent variables and evaluation. [Toy calculations](TOY_CALCULATIONS.md) connect the definitions through numerical steps.

## Notation conventions

| Symbol | Meaning and domain |
|---|---|
| $\mathbb R,\mathbb N_0$ | Real numbers; nonnegative integers |
| $n,p,q,r$ | Observation count; RNA/general feature count; ADT feature count; ATAC feature count |
| $i,j$ | Observation and feature indices, within stated axis limits |
| $X,x_i,x_{ij}$ | $n\times p$ matrix; $p$-column vector; scalar entry; matrix row is $x_i^\top$ |
| $S$ | $n\times2$ coordinate array, with frame metadata |
| $\mu,s_j,\widehat\Sigma$ | Feature mean vector; sample standard deviation; sample covariance |
| $X_c$ | Column-centered $n\times p$ data |
| $W,b,Z$ | $k\times p$ map; $k$-bias; $n\times k$ coordinates in the linear-map notes |
| $U,D,V$ | SVD factors; $D$ is the singular-value matrix also commonly called $\Sigma$ |
| $\rho,h,k,d$ | Exact rank; $\min(n,p)$; retained/output dimension; generic latent/parameter dimension, defined locally |
| $\theta,\eta,\lambda$ | Parameters; gradient step size; eigenvalue or penalty weight, defined locally |
| $P,Q,E,H,I$ | Probability laws; expectation; entropy; mutual information, with local subscripts |
| $M,\Omega$ | Entry-availability mask; observed index set |
| $C,Y$ | Proposed partition and reference partition |
| $\top,\odot,\|\cdot\|_F$ | Transpose; element-wise product; Frobenius matrix norm |

Symbols have different conventional meanings across disciplines. Each note disambiguates locally: covariance $\widehat\Sigma$ versus SVD $D$, feature count $p$ versus Minkowski exponent $a$, eigenvalue $\lambda$ versus penalty $\lambda$, bandwidth $\sigma$ versus standard deviation.

Standard operators: $\sum$ sums and $\prod$ multiplies over the displayed indices; $\in$ denotes membership, $\subseteq$ inclusion, $|\cdot|$ scalar absolute value or set cardinality according to its argument, and $\binom mt=m!/[t!(m-t)!]$ counts size-$t$ subsets. Factorial $m!$ is the product of integers 1 through $m$, with $0!=1$. $\log$ is natural logarithm unless another base is stated; $\exp(t)=e^t$ uses Euler's number $e$. In a Gaussian density, $\pi$ is the circle constant; in Bernoulli/multinomial notation $\pi$ or $\pi_j$ is a probability. $\operatorname{sign}$ returns $-1,0,1$ according to sign; $\operatorname{diag}$ forms a diagonal matrix. A hat marks an estimate or reconstruction; a star marks an optimum; neither denotes a directly measured biological entity.

Summation indices range over the declared matrix axes or distribution support when limits are suppressed. $k$ in a neighborhood is its size, rather than a latent dimension. $m$ denotes trial count, number of views, or number of hypotheses as defined in the corresponding note. $P,Q$ are probability laws; lowercase $p(\cdot)$ can denote a density or mass function, separately from the feature-count symbol. $E[\cdot]$ is expectation; $E$ in ARI is a particular expected pair count. These local conventions avoid implying that every occurrence of the same letter names one project quantity.

In the eigenvalue toy, $\det(A)$ denotes the determinant of a square matrix $A$, a scalar. For $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$, $\det(A)=ad-bc$, where $a,b,c,d$ are its four entries. Thus $\det(A-\lambda I)=0$ expresses that $A-\lambda I$ is singular, so it has a nonzero vector in its null space. [Linear algebra](SOURCES.md#vmls)

## Permanent distinctions

Measured feature → constructed coordinate requires a stated operation. Constructed coordinate → biological mechanism requires additional evidence. Distance, similarity, correlation, dependence and biological relatedness are different claims.

Reconstruction, ARI/NMI agreement and silhouette cannot replace biological validation. Every future evaluation must consider computational **and** statistical **and** biological evidence; see [the permanent principle](36_BIOLOGICAL_VS_COMPUTATIONAL_EVALUATION.md).

Phase 2B remains unstarted.
