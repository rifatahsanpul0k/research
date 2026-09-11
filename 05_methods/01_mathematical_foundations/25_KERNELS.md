# 25. Kernels

A kernel $K(x,y)$ evaluates a scalar from two inputs $x,y\in\mathbb R^p$. In positive-semidefinite kernel methods, every finite Gram matrix $G\in\mathbb R^{n\times n}$, with scalar entries $G_{ij}=K(x_i,x_j)$, must be symmetric and satisfy $a^\top Ga\ge0$ for all $a\in\mathbb R^n$. This corresponds to an inner product $K(x,y)=\langle\phi(x),\phi(y)\rangle$, where $\phi$ maps inputs into a possibly higher-dimensional feature space. Not every informal similarity is such a kernel. [BHK, §5.3](SOURCES.md#bhk), [Convex Optimization, positive-semidefinite matrices](SOURCES.md#convex)

The linear kernel is $K(x,y)=x^\top y$, so $G=XX^\top$ has shape $(n\times p)(p\times n)=n\times n$. It is sensitive to vector magnitude. The RBF kernel is
$$
K(x,y)=\exp\left(-\frac{\|x-y\|_2^2}{2\sigma^2}\right),\quad \sigma>0.
$$
Bandwidth $\sigma$ has the units of distance and controls how quickly similarity decreases. For distinct fixed points, $\sigma\to0$ gives near-zero similarity; $\sigma\to\infty$ gives near-one similarity. Identical points have value one for all positive bandwidths.

Toy rows 1 and 2 have squared distance 3. At $\sigma=1$, RBF is $e^{-3/2}\approx0.223130$; at $\sigma=2$, it is $e^{-3/8}\approx0.687289$. Neither number is the probability of equal cell type.

Changing units, normalization or features changes the kernel, even if $\sigma$ is unchanged. A kernel matrix can be dense when the input is sparse, and the RBF need not encode known biology. Kernels offer mathematical nonlinear similarities without requiring an explicit finite feature map; choosing or benchmarking a kernel representation is deferred. No real Gram matrix is constructed.
