# 35. Silhouette score

For a declared partition and metric $d$, let $C(i)$ be the cluster containing observation $i$. For $|C(i)|>1$,
$$
a(i)=\frac1{|C(i)|-1}\sum_{\substack{j\in C(i)\\j\ne i}}d(x_i,x_j).
$$
For every other nonempty cluster $B$, compute its mean distance from $i$; take the smallest:
$$
b(i)=\min_{B\ne C(i)}\frac1{|B|}\sum_{j\in B}d(x_i,x_j),\qquad
s(i)=\frac{b(i)-a(i)}{\max(a(i),b(i))}.
$$
$b(i)$ is not the nearest individual-point distance. [Rousseeuw](SOURCES.md#rousseeuw)

Positive $s(i)$ indicates greater average distance to the nearest other cluster than to its own; values near zero indicate similar averages; negative values suggest closer average affiliation elsewhere. Scores lie in $[-1,1]$ when defined. The dataset score is usually the mean over observations, so large clusters contribute more observations.

For the synthetic four-row matrix and hand-assigned groups $\{1,2\},\{3,4\}$, $a(1)=\sqrt3$. Distances to group 2 are $\sqrt{108}$ and $\sqrt{123}$; hence $b(1)=(\sqrt{108}+\sqrt{123})/2\approx10.741421$ and $s(1)\approx0.838750$. All four scores average to approximately 0.835703. No clustering algorithm produced these toy groups.

A singleton has no within-cluster pair average; the conventional silhouette contribution is zero. The all-identical case $a=b=0$ also requires a convention, typically zero. Evaluation ordinarily needs between 2 and $n-1$ clusters. [Software conventions](SOURCES.md#cluster-metrics)

Silhouette depends on representation, feature scale and metric. It can favor compact separated groups over continua or irregular structures and can reward technical batches. It needs no external labels and therefore cannot alone certify correct biological populations.
