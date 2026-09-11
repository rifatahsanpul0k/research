# 07. Correlation and independence

For features $j,k$ with positive sample standard deviations $s_j,s_k$, Pearson correlation is $r_{jk}=s_{jk}/(s_js_k)$, in $[-1,1]$. It is covariance on standardized scales. $r=1$ means an exact positive affine relationship in the sample; $r=-1$ an exact negative affine relationship. Both concern linear association. [VMLS](SOURCES.md#vmls)

Spearman correlation is Pearson correlation of ranks, using average ranks for ties. It detects monotonic relationships, including nonlinear ones. For $u=(1,2,3)$ and $v=(1,4,9)$ the ranks are identical, so Spearman is 1 while Pearson is less than 1. In sparse counts many tied zeros reduce rank resolution. Constant variables make either coefficient undefined.

Zero correlation does not imply independence. Let random variable $A$ be uniform on $\{-1,0,1\}$ and $B=A^2$. $E[A]=0$, $E[B]=2/3$, and $E[AB]=E[A^3]=0$, giving covariance zero. Yet $B$ is determined by $A$, so they are dependent. Independence implies zero covariance when the required moments exist; the reverse needs extra assumptions, such as joint Gaussianity. [Probability foundations](SOURCES.md#probability)

Two genes may correlate through a common upstream cause, tissue composition, depth, batch or a direct relationship. Correlation has no arrow and no intervention. The [Phase 1B enhancer–promoter note](../../01_biology/02_gene_regulation/11_ENHANCER_PROMOTER_INTERACTIONS.md) distinguishes association, physical proximity and perturbation-supported function. RNA–ATAC correlation additionally requires observation pairing and a justified region-to-gene mapping. No regulatory interaction is inferred here.

A future analysis must report whether correlation is across observations or across features, its transform, missing-value policy and reference population. A coefficient without those choices is incomplete.
