# 26. Information theory

Let discrete random variables $A,B$ have probability mass functions $P(a)$ and joint $P(a,b)$. Natural logarithms give nats; base-two logarithms give bits. Adopt $0\log0=0$ by continuity. Entropy is
$$
H(A)=-\sum_aP(a)\log P(a),
$$
the expected negative log probability under $P$. A uniform binary variable has entropy $\log2$ nats or one bit; a constant variable has entropy zero. This quantifies uncertainty, not biological importance. [Information theory](SOURCES.md#information)

For another distribution $Q$ on the same support,
$$
H(P,Q)=-\sum_aP(a)\log Q(a),\qquad
D_{\rm KL}(P\|Q)=\sum_aP(a)\log\frac{P(a)}{Q(a)}
=H(P,Q)-H(P).
$$
Cross-entropy measures predictive log loss under data distribution $P$. KL is nonnegative and zero when distributions coincide (on their support). If $P(a)>0$ but $Q(a)=0$, KL is infinite. It is generally asymmetric and is not a distance metric. [Vinh et al.](SOURCES.md#vinh)

Mutual information is
$$
I(A;B)=\sum_{a,b}P(a,b)\log\frac{P(a,b)}{P(a)P(b)}
=D_{\rm KL}(P_{AB}\|P_AP_B).
$$
It is symmetric, nonnegative, and zero exactly for independence of the discrete variables. It also equals $H(A)+H(B)-H(A,B)$. Dependence is broader than linear correlation but still does not imply causation.

Cross-entropy connects to negative log-likelihood. KL compares probabilistic descriptions; mutual information describes shared statistical dependence. Later representation or contrastive objectives may use these quantities or bounds/estimators, whose sampling assumptions need separate study. Cross-modality dependence can reflect shared biology, shared technical effects or paired specimen identity. Maximizing dependence alone does not guarantee useful biological alignment.

The [toy calculations](TOY_CALCULATIONS.md) give finite probability tables with exact support. Continuous differential entropy is not interchangeable with discrete entropy; discretization and estimation in thousands of dimensions require deeper study. No MI estimator is applied to omics data.
