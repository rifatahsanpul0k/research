# 24. Neighborhoods as sets

For $n$ observations with a specified metric $d$, nearest neighbor of $i$ minimizes $d(x_i,x_j)$ over $j\ne i$. A $k$-nearest-neighbor set $N_k(i)$ contains the $k$ closest eligible observations, where $1\le k\le n-1$. State exclusion rules and a deterministic tie policy; “all tied at the cutoff” can produce more than $k$ members. No adjacency matrix or graph is required to define this set. [Distance foundations](SOURCES.md#vmls)

A radius neighborhood is $N_\epsilon(i)=\{j\ne i:d(x_i,x_j)\le\epsilon\}$, with radius $\epsilon\ge0$. Its size varies with local density; a fixed-$k$ neighborhood instead varies its physical radius. Mutual neighbors satisfy $j\in N_k(i)$ and $i\in N_k(j)$. One-direction membership alone need not be mutual.

For points $a=0,b=2,c=3$ on a line and $k=1$, $N_1(a)=\{b\}$, $N_1(b)=\{c\}$, $N_1(c)=\{b\}$. Only $b,c$ are mutual. For $\epsilon=1$, $a$ has an empty radius neighborhood while $b,c$ contain each other. These are explicit mathematical sets, not a constructed research graph.

More fully,
$$
N_k(i)=f(X,\text{feature identities},\text{metric},k,
\text{preprocessing},\text{eligibility},\text{tie rule}).
$$
Here $f$ denotes the selection procedure, not a fitted model. A reference neighbor set computed before preprocessing may differ afterward. Across specimens, coincident barcode strings do not identify the same observation.

Spatial neighbors use calibrated positions, molecular neighbors use aligned features, and shared neighborhood membership does not imply signaling, lineage or matching cell types. KNN methods and graph representations remain for later phases.
