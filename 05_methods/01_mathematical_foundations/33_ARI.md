# 33. Adjusted Rand Index

ARI compares partitions $C$ and $Y$ of the same $n$ items through unordered pairs. Pairs may be together in both partitions, separate in both, or disagree. Rand Index is the fraction of agreeing pairs among $T=\binom n2=n(n-1)/2$. Agreement from many separate pairs can be high by chance. [Hubert–Arabie](SOURCES.md#hubert)

Let contingency count $n_{ab}=|\{i:C_i=a,Y_i=b\}|$, row margin $r_a=\sum_bn_{ab}$, and column margin $c_b=\sum_an_{ab}$. Define
$$
J=\sum_{ab}\binom{n_{ab}}2,\quad
A=\sum_a\binom{r_a}2,\quad B=\sum_b\binom{c_b}2,\quad
E=AB/T.
$$
$J$ counts pairs together in both, $A,B$ together in each partition, and $E$ is expected together agreement under random reassignment with fixed partition sizes. Then
$$
ARI=\frac{J-E}{(A+B)/2-E}.
$$
This expectation model is specific, not a correction for every possible biological null.

Tiny example: $Y=(A,A,B,B)$, $C=(u,v,u,v)$. All four contingency cells equal 1; margins are 2. Among six pairs, 12 and 34 agree only in $Y$, 13 and 24 only in $C$, and 14 and 23 are separate in both. Rand Index is $2/6=1/3$. Here $J=0$, $A=B=2$, $E=4/6=2/3$, so $ARI=(-2/3)/(4/3)=-1/2$. [Full pair table](TOY_CALCULATIONS.md)

ARI=1 means identical partition membership up to relabeling; expected ARI under the fixed-marginal chance model is zero when the denominator is defined. Negative values mean less agreement than that reference. The standard range is $[-0.5,1]$, with tighter attainable bounds for particular size patterns. Degenerate identical partitions (all singleton or all one cluster) produce a zero denominator in this formula; software convention commonly returns 1. [Official conventions](SOURCES.md#cluster-metrics)

A high score can reproduce a mistaken reference, and pair weighting can obscure errors in rare groups. It measures agreement, not spatial coherence, causal regulation or completeness of a biological taxonomy.
