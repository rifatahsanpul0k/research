# Sources and evidence for Phase 2A

These references support definitions and limits, not representation rankings. Examples in these notes are original synthetic derivations. Source verification distinguishes an accessible full text from an author landing page or abstract. Access date: 2026-09-11. No textbook has been claimed read cover-to-cover.

## vmls

Stephen Boyd and Lieven Vandenberghe (2018). *Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares*. Cambridge University Press. [Author page](https://stanford.edu/~boyd/vmls/); [author-hosted book](https://stanford.edu/~boyd/vmls/vmls.pdf). Full text accessible. Locators: chapters 1–3 (vectors, linear functions, norm/distance), 5–8 (basis, matrices, maps), 10 (multiplication), 13.2 (validation). Supports notation, vector algebra and shape reasoning. Registry ID: MATH_VMLS_2018.

## bhk

Avrim Blum, John Hopcroft and Ravindran Kannan (2020). *Foundations of Data Science*. Cambridge University Press. [Author-hosted manuscript](https://www.cs.cornell.edu/jeh/book.pdf). Full text accessible; the accessed manuscript is dated 4 January 2018, distinct from the 2020 published edition. Locators: chapter 2, “High-Dimensional Space”; chapter 3, “Best-Fit Subspaces and Singular Value Decomposition,” especially best rank-k approximations and singular vectors/eigenvectors. Used for geometry, SVD and low-rank foundations; audit verification also checked section 5.3 (manuscript pp. 132–134) for feature maps, linear and Gaussian kernels, without studying or running its classifiers. Mathematical caveat: eigenvalues of a general symmetric matrix may be negative; singular values are their absolute values, not always equal. Registry ID: MATH_BHK_2020.

## convex

Stephen Boyd and Lieven Vandenberghe (2004). *Convex Optimization*. Cambridge University Press. ISBN 9780521833783. [Author page](https://web.stanford.edu/~boyd/cvxbook/); [full text](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf). Accessible full text. Locators: chapters 2–4 (convex sets/functions/problems), §6.3 (regularization), §7.1 (statistical estimation), chapter 9 (gradient-based minimization). Used for optimization definitions and limitations, not advanced algorithms. Registry ID: MATH_CONVEX_2004.

## probability

Joseph K. Blitzstein and Jessica Hwang (2019). *Introduction to Probability*, second edition. Chapman & Hall/CRC. [Harvard course and author-book link](https://stat110.hsites.harvard.edu/); [course syllabus](https://projects.iq.harvard.edu/files/stat110/files/stat110harvarditunesusyllabus.pdf). Locators: conditional probability/Bayes, random variables, expectation, discrete/continuous families, joint distributions and covariance. The course/syllabus and book identity were verified; the linked book redirects to a Drive viewer that did not expose full text to this browser. This is an authoritative textbook reference, with that access limit retained. Registry ID: MATH_BLITZSTEIN_HWANG_2019.

## mml

Marc Peter Deisenroth, A. Aldo Faisal and Cheng Soon Ong (2020). *Mathematics for Machine Learning*. Cambridge University Press. [Author-maintained site and table of contents](https://mml-book.github.io/); [book PDF](https://mml-book.github.io/book/mml-book.pdf). Locators: chapters 2–7 (linear algebra, geometry, decomposition, calculus, probability, optimization) and chapter 8 (models and data). Used as a mathematical reference for probabilistic notation and latent/model versus measured variables; no family tutorial executed. Author page and table of contents accessible; browser extraction of the approximately 17 MB book failed due to size, so full-text review is not claimed. The audit replaced the unverified missingness attribution with Seaman et al. and the broad kernel locator with the directly checked BHK section 5.3. Registry ID: MATH_MML_2020.

## information

Robert M. Gray (2023 correction of the 1990 first edition). *Entropy and Information Theory*. Author-hosted corrected first edition, dated June 26, 2023; original publisher Springer-Verlag. [Full text](https://www-ee.stanford.edu/~gray/it.pdf). Accessible full text. Locators: chapter 1 (probability, distributions, expectation), chapter 2 (entropy and information), chapter 5 (relative entropy). Used for basic definitions and support conditions only; no coding-theory study. Registry ID: MATH_GRAY_INFORMATION_2023.

## hubert

Lawrence Hubert and Phipps Arabie (1985). “Comparing partitions.” *Journal of Classification* 2:193–218. DOI [10.1007/BF01908075](https://doi.org/10.1007/BF01908075). Publisher metadata/abstract accessible; full article behind access controls. Supports the origin and fixed-marginal chance-adjustment framework; formulas/conventions cross-checked using official metric documentation. Registry ID: MATH_HUBERT_ARABIE_1985.

## vinh

Nguyen Xuan Vinh, Julien Epps and James Bailey (2010). “Information Theoretic Measures for Clusterings Comparison: Variants, Properties, Normalization and Correction for Chance.” *Journal of Machine Learning Research* 11(95):2837–2854. [Journal page](https://www.jmlr.org/papers/v11/vinh10a.html); [full article](https://www.jmlr.org/papers/volume11/vinh10a/vinh10a.pdf). Full text accessible. Locators: definitions of entropy/MI, normalized variants, chance correction. Used to distinguish NMI variants and unadjusted versus adjusted agreement, not to adopt the paper's preferred measure. Registry ID: MATH_VINH_2010.

## rousseeuw

Peter J. Rousseeuw (1987). “Silhouettes: A graphical aid to the interpretation and validation of cluster analysis.” *Journal of Computational and Applied Mathematics* 20:53–65. DOI [10.1016/0377-0427(87)90125-7](https://doi.org/10.1016/0377-0427%2887%2990125-7). Publisher metadata/abstract accessible. Formula, eligibility and singleton convention cross-checked in official documentation below. No numeric threshold from this source is adopted. Registry ID: MATH_ROUSSEEUW_1987.

## cluster-metrics

Scikit-learn developers. [Clustering performance evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation). Official documentation, accessed 2026-09-11 (page displayed version 1.9.1; no package installed or benchmark run). Locators: adjusted Rand index, mutual-information-based scores and silhouette coefficient. Used for edge cases and stated range/normalization conventions; software conventions are distinguished from mathematical definitions and biological truth. Registry ID: MATH_SKLEARN_CLUSTER_DOC.

## metrics

Scikit-learn developers. [Metrics and scoring: quantifying the quality of predictions](https://scikit-learn.org/stable/modules/model_evaluation.html). Official documentation, accessed 2026-09-11. Locators: accuracy; precision, recall and F measures; averaging conventions. Used only for metric definitions. Registry ID: MATH_SKLEARN_EVAL_DOC.

## testing

Cosma Rohilla Shalizi (2019-02-07). “Significance Testing etc.” Carnegie Mellon University 36-402 course notes. [Official notes](https://www.stat.cmu.edu/~cshalizi/uADA/19/lectures/2019-02-07.html). Full page accessible. Locators: hypotheses, sampling model, test statistic and p-value, confidence sets. Supports the distinction between effect magnitude, uncertainty and significance. Registry ID: MATH_SHALIZI_TESTING_2019.

## bh

Yoav Benjamini and Yosef Hochberg (1995). “Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing.” *Journal of the Royal Statistical Society, Series B* 57(1):289–300. DOI [10.1111/j.2517-6161.1995.tb02031.x](https://rss.onlinelibrary.wiley.com/doi/10.1111/j.2517-6161.1995.tb02031.x). Publisher abstract/metadata located; original independence condition retained. Used for the definition of FDR and introductory step-up rule, not real-gene testing. Registry ID: MATH_BH_1995.

## bio

Two existing registry entries are reused without duplication:
- Hafemeister C; Satija R (2019). *Normalization and variance stabilization of single-cell RNA-seq data using regularized negative binomial regression*. Genome Biology 20:296. DOI [10.1186/s13059-019-1874-1](https://link.springer.com/article/10.1186/s13059-019-1874-1). Accessible primary paper; introductory count/technical-variation rationale only. Registry ID SCT_2019.
- Zimmerman KD; Espeland MA; Langefeld CD (2021). *A practical solution to pseudoreplication bias in single-cell studies*. Nature Communications 12:738. DOI [10.1038/s41467-021-21038-1](https://www.nature.com/articles/s41467-021-21038-1). Prior verified project source; fresh browser request hit a redirect/access error, so no new full-text reading was claimed then. During this audit the article text was accessible; Results/Discussion passages on within-individual correlation and pseudoreplication were checked. Registry ID ZIMMERMAN_PSEUDOREPLICATION_2021.

Biological interpretation is also linked to the already sourced Phase 1B/1C notes. [Phase 1E data statistics](../../02_omics/02_preprocessing_qc_statistics/DATASET_STATISTICS.md) and companion JSON provide local shape evidence; derived $p/n$ ratios and rank bounds are arithmetic, not experiments. E18 ATAC remains unverified locally.

## missingness

Shaun Seaman, John Galati, Dan Jackson and John Carlin (2013). “What Is Meant by ‘Missing at Random’?” *Statistical Science* 28(2):257–268. DOI [10.1214/13-STS415](https://doi.org/10.1214/13-STS415); [author-deposited electronic reprint](https://arxiv.org/pdf/1306.2812). The reprint identifies the journal publication and notes pagination differences. Sections 2 and 5 were checked for observation indicators and inference assumptions. Added during the governance audit to replace an unsupported source attribution, not to begin imputation-method study. Registry ID: MATH_SEAMAN_MISSING_2013. Accessed 2026-09-11; reprint text accessible, publisher PDF extraction unavailable.

## Evidence limits

The original missing-governance-file limitation is resolved by [ASTRA_OPERATING_RULES.md](../../ASTRA_OPERATING_RULES.md) and the [operating-rules audit](OPERATING_RULES_AUDIT.md). Textbook references are not synthetic paper cards, and reference counts are not quality targets. Access limits above do not prevent checking elementary algebra independently, but must not be represented as full source review.
