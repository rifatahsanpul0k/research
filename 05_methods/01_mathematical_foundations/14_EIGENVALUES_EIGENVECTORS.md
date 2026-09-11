# 14. Eigenvalues and eigenvectors

For square $A\in\mathbb R^{p\times p}$, a nonzero vector $v\in\mathbb R^p$ and scalar $\lambda$ satisfy $Av=\lambda v$ when $v$ is an eigenvector and $\lambda$ its eigenvalue. The vector's direction remains on the same line: positive $\lambda$ scales, negative $\lambda$ reverses direction, zero collapses it. Eigenvectors can be rescaled arbitrarily; normalization fixes length, not sign. [BHK, spectral foundations](SOURCES.md#bhk)

Use
$$
A=\begin{bmatrix}2&1\\1&2\end{bmatrix},\quad
v_+=\frac1{\sqrt2}\begin{bmatrix}1\\1\end{bmatrix},\quad
v_-=\frac1{\sqrt2}\begin{bmatrix}1\\-1\end{bmatrix}.
$$
$Av_+=3v_+$ and $Av_-=v_-$. The first direction describes coordinated changes; the second describes a contrast. These are arithmetic interpretations, not inferred gene programs.

Real symmetric matrices have real eigenvalues and an orthonormal eigenbasis. A covariance matrix $\widehat\Sigma\in\mathbb R^{p\times p}$ is symmetric positive semidefinite, so its eigenvalues are nonnegative. For unit eigenvector $v$, the sample variance of centered scores $X_cv\in\mathbb R^n$ is $v^\top\widehat\Sigma v=\lambda$. This connects a direction to variance in the selected preprocessing scale.

General nonsymmetric real matrices can have complex eigenvalues and may lack a full eigenbasis. Repeated eigenvalues make basis vectors within the corresponding eigenspace nonunique. Covariance eigenvectors can be dominated by technical covariation; the largest eigenvalue does not mean the most important biological mechanism. This is a prerequisite for later PCA study, not a PCA implementation.
