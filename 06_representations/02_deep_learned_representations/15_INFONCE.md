# InfoNCE

Phase 2C · method study · studied_not_fitted · not_reproduced.

Let anchor \(z_i\in\mathbb R^d\), positive \(z_i^+\in\mathbb R^d\), and candidate set \(C_i\) contain that positive and \(K-1\) negatives. Exclude the anchor's identical self-view unless explicitly intended:
\[
\ell_i=-\log\frac{\exp(s(z_i,z_i^+)/\tau)}
 {\sum_{j\in C_i}\exp(s(z_i,z_j)/\tau)} .
\]
The scalar \(s\) is a declared score (often dot product or cosine), \(\tau>0\) is temperature, and the denominator **includes the positive**. This is cross-entropy for identifying the positive candidate. InfoNCE originates in contrastive predictive coding; mutual-information-bound interpretations require the paper's sampling/density-ratio conditions, not arbitrary biological positive labels.[^1]

Synthetic scores \(s_+=1,s_-=0,\tau=1\) give
\(P_+=e/(e+1)=0.731059\), and
\(\ell=-\log P_+=\log(1+e^{-1})=0.313262\).
With one positive and two negatives both scoring zero, \(P_+=e/(e+2)\), so the loss changes just because the candidate set changes. Losses across different negative pools are not automatically comparable.

If all candidate scores are equal, the loss is \(\log K\). A lower loss may arise from identifying technical batch fingerprints rather than biology. The equation only sees scores and designated pairs.

**Project interpretation:** RNA and ADT from one spot supply an identity-linked positive, but this objective cannot decide whether their discordance reflects noise or complementary biological processes. Different features should not be forced equal to make a score large. No contrastive pairs were made from project data.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Any compatible encoder; objective does not specify architecture |
| Training objective | Log-softmax positive classification over explicit candidate set |
| Biological prior | Pair and negative-sampling assumptions |
| Downstream model | Separate task applied to z |
| Evaluation | Loss reduction differs from biological validation |

## Evidence

[^1]: [CPC: original source and access notes](SOURCES.md#cpc).

