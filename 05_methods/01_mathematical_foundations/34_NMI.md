# 34. Normalized mutual information

Let $C$ be cluster labels and $Y$ reference labels for the same $n$ observations. From contingency counts $n_{ab}$, probabilities are $P(C=a,Y=b)=n_{ab}/n$. Marginals are row/column sums divided by $n$. Mutual information is
$$
I(C;Y)=\sum_{a,b}P(a,b)\log\frac{P(a,b)}{P(a)P(b)}.
$$
Adopt the arithmetic-mean normalization
$$
NMI(C,Y)=\frac{2I(C;Y)}{H(C)+H(Y)}.
$$
Entropy $H$ and log-base conventions are defined in [information theory](26_INFORMATION_THEORY.md). Other definitions use geometric mean, minimum or maximum entropy, so report the normalization. [Vinh–Epps–Bailey](SOURCES.md#vinh)

For $Y=(A,A,B,B)$ and $C=(u,u,v,v)$, each label entropy is $\log2$, MI is $\log2$, so NMI=1. For crossed $C=(u,v,u,v)$, all joint probabilities are $1/4$ and marginal products $1/4$, so each log ratio is zero and NMI=0.

For $C=(u,u,u,v)$, contingency cells are $(2,1;0,1)$ with rows indexed by $u,v$ and columns $A,B$. Then $I\approx0.215762$, $H(C)\approx0.562335$, $H(Y)\approx0.693147$, giving arithmetic NMI $\approx0.343711$. Intermediate terms appear in the toy document.

With nonzero denominator, this NMI lies in $[0,1]$. Label names do not matter. Both constant labelings require a convention (commonly 1); one constant and one nonconstant gives zero. Unadjusted MI/NMI are not corrected for finite-sample chance agreement and can favor fragmented solutions. Adjusted MI is a distinct metric, not the formula above.

High NMI means statistical agreement with labels. It does not certify biological truth, preserve within-region variation or show causal mechanisms. No annotation is treated as perfect ground truth and no method is scored on our datasets.
