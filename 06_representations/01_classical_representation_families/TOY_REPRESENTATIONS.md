# One synthetic matrix, eleven representations

All observations and features here are invented for arithmetic teaching. O1–O5 are fixed synthetic observation IDs, not cells from our project; F1–F3 are arbitrary features. No biological significance, model ranking or experimental result follows. Values are dimensionless. The same input is used throughout. Only PCA's small eigensystem is numerically solved to verify the displayed manual derivation; no research model or project representation is fitted.

## 1. Raw vectors

\[
X=\begin{bmatrix}4&0&1\\5&1&1\\0&5&4\\1&6&5\\3&2&2\end{bmatrix}\in\mathbb R^{5\times3}.
\]

Row O1 is x₁ᵀ=(4,0,1); columns retain the named feature amounts. Identity representation R=X preserves the input. An observed 0 is not an unmeasured entry; this toy has no missing values. In a real table, row-unit and feature-identity metadata are essential.

## 2. Standardized vectors

Use **sample** standard deviations (denominator n−1=4), not population ones:

\[
\mu=(13/5,14/5,13/5)=(2.6,2.8,2.6),\qquad
X_c=\begin{bmatrix}1.4&-2.8&-1.6\\2.4&-1.8&-1.6\\-2.6&2.2&1.4\\-1.6&3.2&2.4\\0.4&-0.8&-0.6\end{bmatrix}.
\]

For F1, sum of squared deviations is 1.96+5.76+6.76+2.56+0.16=17.2, giving variance 4.3. F2 and F3 give 26.8/4=6.7 and 13.2/4=3.3. Thus s=(√4.3,√6.7,√3.3)≈(2.073644,2.588436,1.816590).

Define T_ig=(X_ig−μ_g)/s_g, T:5×3. For O1,F1: (4−2.6)/2.073644=0.675140. All entries are:

~~~text
          F1         F2         F3
O1    0.675140  -1.081734  -0.880771
O2    1.157383  -0.695401  -0.880771
O3   -1.253831   0.849934   0.770675
O4   -0.771589   1.236268   1.321157
O5    0.192897  -0.309067  -0.330289
~~~

Means are zero and sample variances one. Negative entries are centered coordinates, not negative molecule counts. With μ and s retained the transformation is reversible. Using T for distances would change their weighting. All later distances below use **raw X**, while PCA uses **centered raw X_c**, to keep each choice explicit.[^1]

## 3. Actual PCA coordinates from the toy covariance

Compute C=X_cᵀX_c/4:

\[
C=\begin{bmatrix}4.3&-4.85&-3.45\\-4.85&6.7&4.65\\-3.45&4.65&3.3\end{bmatrix}.
\]

For C₁₂, the products sum to −3.92−4.32−5.72−5.12−0.32=−19.4; dividing by four gives −4.85. For C₂₃: 4.48+2.88+3.08+7.68+0.48=18.6, so C₂₃=4.65.

A first direction w:3×1 maximizes wᵀCw subject to wᵀw=1. The Lagrange equation gives Cw=λw. The characteristic polynomial is

\[
\det(\lambda I_3-C)=\lambda^3-14.3\lambda^2+8.0625\lambda-0.3375.
\]

Intermediate checks: tr(C)=14.3; the principal 2×2 minors sum to (28.81−23.5225)+(14.19−11.9025)+(22.11−21.6225)=8.0625; det(C)=0.3375. Here det denotes determinant, tr denotes trace and I₃ is the 3×3 identity. Solving the cubic numerically yields

\[
(\lambda_1,\lambda_2,\lambda_3)\approx(13.713887,0.540589,0.045525).
\]

Normalize solutions of (C−λ_jI)w_j=0 and choose positive first coefficients as a sign convention. For λ₁, setting the first coefficient to one gives ratios approximately (1,−1.29426,−0.90919); normalizing gives w₁. The resulting direction matrix, columns ordered by decreasing eigenvalue, is

~~~text
W = [ 0.534389   0.842232   0.071224
     -0.691637   0.484160  -0.535936
     -0.485866   0.237137   0.841249 ]
~~~

WᵀW≈I₃. As a check, Cw₁≈(7.328550,−9.485031,−6.663112)ᵀ≈λ₁w₁, with differences from rounding. Scores Z=X_cW have shape 5×3:

~~~text
          PC1         PC2         PC3
O1     3.462115   -0.555941    0.254336
O2     3.304867    0.770451   -0.210377
O3    -3.591227   -0.792661   -0.186492
O4    -4.234341    0.770869    0.190044
O5     1.058585   -0.192717   -0.047511
~~~

For example z₁₁=1.4(0.534389)+(−2.8)(−0.691637)+(−1.6)(−0.485866)=3.462115. The first two columns give a 5×2 reduced representation. Explained variance fractions are approximately 0.959013, 0.037803, 0.003184. The first two retain 0.996816 of this toy's variance; this is **not biological preservation or method superiority**.

Reconstruct with \(\widehat X_2=Z_{[:,1:2]}W_{[:,1:2]}^T+\mathbf1_5\mu^T\). The omitted centered component is z_i3 w₃ᵀ. For O1 it is approximately 0.254336(0.071224,−0.535936,0.841249)=(0.018115,−0.136308,0.213960), so \(\widehat x_1\approx(3.981885,0.136308,0.786040)\). Sum-squared reconstruction error is 4λ₃≈0.182098. With all three PCs, X=ZWᵀ+1μᵀ to floating-point tolerance. Thin SVD X_c=UΣWᵀ gives the same scores UΣ and λ_j=σ_j²/4.[^2]

## 4. Pairwise Euclidean distances

For O1 and O2, D₁₂²=(4−5)²+(0−1)²+(1−1)²=2. For O1 and O3, D₁₃²=16+25+9=50. Define D:5×5 with D_ij=||x_i−x_j||₂. The exact squared distances are

\[
D^{\circ2}=\begin{bmatrix}0&2&50&61&6\\2&0&50&57&6\\50&50&0&3&22\\61&57&3&0&29\\6&6&22&29&0\end{bmatrix}.
\]

Take the square root **entrywise**, not a matrix square root:

~~~text
D = [0        1.414214 7.071068 7.810250 2.449490
     1.414214 0        7.071068 7.549834 2.449490
     7.071068 7.071068 0        1.732051 4.690416
     7.810250 7.549834 1.732051 0        5.385165
     2.449490 2.449490 4.690416 5.385165 0       ]
~~~

Rows/columns now identify observations, not genes. Original axis orientation is lost. Small D does not prove biological equivalence.[^1]

## 5. Cosine similarity

Norm squares are (17,27,41,62,17). The dot product x₁ᵀx₂=21, so B₁₂=21/√(17·27)=0.980196. Define B_ij=x_iᵀx_j/(||x_i||||x_j||), B:5×5:

~~~text
B = [1        0.980196 0.151511 0.277218 0.823529
     0.980196 1        0.270501 0.391059 0.886844
     0.151511 0.270501 1        0.991704 0.681799
     0.277218 0.391059 0.991704 1        0.770051
     0.823529 0.886844 0.681799 0.770051 1       ]
~~~

No norm is zero. B compares direction, discarding magnitude. This B happens to be a normalized linear Gram matrix and is PSD; arbitrary similarities need not be PSD. B is not spatial S or a calibrated probability matrix.[^1]

## 6. KNN sets

Use k=2, raw Euclidean D, exclude self. Sort by distance and then ascending observation ID to resolve ties. The ordered neighbor lists are:

| Observation | Two nearest IDs | Their squared distances |
|---|---|---|
| O1 | O2, O5 | 2, 6 |
| O2 | O1, O5 | 2, 6 |
| O3 | O4, O5 | 3, 22 |
| O4 | O3, O5 | 3, 29 |
| O5 | O1, O2 | 6, 6 |

The set N₂(3)={4,5} forgets its order; the list (4,5) retains it. The tie at O5 is explicitly resolved. N₂(3) includes O5 but N₂(5) excludes O3, demonstrating asymmetry. We have not yet specified a graph.[^3]

## 7. A simple adjacency encoding

Now define a directed graph on these five synthetic IDs only, A_ij=1 if j∈N₂(i), otherwise zero, and no self-loops:

\[
A=\begin{bmatrix}0&1&0&0&1\\1&0&0&0&1\\0&0&0&1&1\\0&0&1&0&1\\1&1&0&0&0\end{bmatrix}.
\]

There are 10 directed edges. A is not symmetric. Union symmetrization uses max(A,Aᵀ); mutual symmetrization uses min(A,Aᵀ), here both entrywise. The union includes {3,5} and {4,5}; the mutual graph excludes them. Thus direction/symmetrization changes representation. A zero means “not selected by this rule,” not proof of no biological relationship. This is the sole authorized toy graph; it does not authorize a project-data graph.[^3]

## 8. RBF kernel matrix

Choose σ²=5 **for illustration only**. K_ij=exp(−D_ij²/10) gives K₁₂=e^(−0.2)=0.818731 and K₁₃=e^(−5)=0.006738:

~~~text
K = [1        0.818731 0.006738 0.002243 0.548812
     0.818731 1        0.006738 0.003346 0.548812
     0.006738 0.006738 1        0.740818 0.110803
     0.002243 0.003346 0.740818 1        0.055023
     0.548812 0.548812 0.110803 0.055023 1       ]
~~~

K:5×5 is a PSD Gram matrix for this RBF definition. It differs from binary A and is not row-normalized. No kernel PCA, SVM or benchmark is performed. Keeping σ² and exact positive entries allows recovery of D²=−10 log K, but not the original gene-axis orientation.[^1]

## 9. Prototype-distance vectors

Choose illustrative groups G_A={O1,O2,O5}, G_B={O3,O4}, without any clustering algorithm. Their means are

\[
c_A=((4+5+3)/3,(0+1+2)/3,(1+1+2)/3)=(4,1,4/3),
\quad c_B=(1/2,11/2,9/2).
\]

For O1, ||x₁−c_A||²=0²+(−1)²+(−1/3)²=10/9; ||x₁−c_B||²=3.5²+(−5.5)²+(−3.5)²=54.75. The 5×2 squared-distance table is

~~~text
       to c_A       to c_B
O1      10/9        54.75
O2      10/9        52.75
O3     352/9         0.75
O4     427/9         0.75
O5      22/9        24.75
~~~

Taking square roots gives prototype-distance representation R:

~~~text
O1   1.054093   7.399324
O2   1.054093   7.262920
O3   6.253888   0.866025
O4   6.887993   0.866025
O5   1.563472   4.974937
~~~

The prototype vocabulary and reference profiles are now part of the representation. It is not identical to PCA despite also having two columns.[^1]

## 10. Hard assignments

Assign each observation to its nearer prototype, with a stated tie rule if needed. There are no assignment ties here:

~~~text
O1 A
O2 A
O3 B
O4 B
O5 A
~~~

Equivalent one-hot rows are (1,0),(1,0),(0,1),(0,1),(1,0). They collapse all within-group variation. A and B are arbitrary synthetic groups, not cell types, tissue regions or biological labels.

## 11. Soft memberships

Define illustrative normalized weights
\[
p_{ij}=\frac{\exp(-R_{ij}^2/10)}{\sum_{\ell\in\{A,B\}}\exp(-R_{i\ell}^2/10)},\quad P:5\times2.
\]

The denominator 10 is a chosen temperature in squared-distance units, not estimated uncertainty. For O5, unnormalized weights are exp(−(22/9)/10)≈0.783139 and exp(−24.75/10)≈0.084163; dividing by their sum gives (0.902960,0.097040).

~~~text
          A          B
O1    0.995339   0.004661
O2    0.994313   0.005687
O3    0.021122   0.978878
O4    0.009290   0.990710
O5    0.902960   0.097040
~~~

Each row sums to one. These are normalized affinities, **not calibrated posterior cell-type probabilities**. Their magnitudes change with temperature even though X is unchanged. Hard assignments can be recovered by argmax here, but the original feature amounts cannot be recovered from hard labels alone.

## What the chain establishes

The five input rows remain fixed. Each representation changes what a coordinate or relationship means, which information it retains, and what a later model can use. None is declared best. The arithmetic demonstrates representation dependence, not biological equivalence. For real data, cell/spot unit, sampling design, missingness, technical variation and independent annotations would still need biological validation.

[verify_toy.py](verify_toy.py) checks these fixed numbers, eigen identities, memberships, tie policy, adjacency and reconstruction. It has no dataset input argument and performs no model training, search or benchmark.

[^1]: Boyd & Vandenberghe (2018), [Introduction to Applied Linear Algebra](https://stanford.edu/~boyd/vmls/); Blum, Hopcroft & Kannan (2020), [Foundations of Data Science](https://www.cs.cornell.edu/jeh/book.pdf). [Source records](SOURCES.md).
[^2]: Deisenroth, Faisal & Ong (2020), [Mathematics for Machine Learning](https://mml-book.github.io/), PCA chapter. [PCA note](04_PCA.md).
[^3]: [Official neighbor documentation](https://scikit-learn.org/stable/modules/neighbors.html); [NetworkX graph types](https://networkx.org/documentation/stable/reference/classes/index.html). Rules above are explicitly chosen for this toy.
