# Sources used in Phase 2B

Access notes distinguish original-paper full text, abstracts/metadata, and official implementation documentation. These sources support conceptual study only; no project data were fitted or transformed.

The machine-readable bibliographic records are in the root `papers.csv`; official implementations are in `codebases.csv`.

<a id="spca"></a>
## SPCA
- **Sparse Principal Component Analysis** — Zou H; Hastie T; Tibshirani R (2006), Journal of Computational and Graphical Statistics 15(2):265–286.
- DOI: `10.1198/106186006X113430`; [publication/source](https://web.stanford.edu/~hastie/Papers/spc_jcgs.pdf); code: https://cran.r-project.org/package=elasticnet.
- Access: Author-hosted full paper; regression formulation and sparse loadings
- Registry ID: `REP_SPCA`.

<a id="ica"></a>
## ICA
- **Independent Component Analysis: Algorithms and Applications** — Hyvärinen A; Oja E (2000), Neural Networks 13(4–5):411–430.
- DOI: `10.1016/S0893-6080(00)00026-5`; [publication/source](https://www.cs.helsinki.fi/u/ahyvarin/papers/NN00new.pdf); code: https://www.cs.helsinki.fi/u/ahyvarin/software.shtml.
- Access: Author-hosted full paper; model, assumptions and ambiguities
- Registry ID: `REP_ICA`.

<a id="nmf"></a>
## NMF
- **Learning the parts of objects by non-negative matrix factorization** — Lee DD; Seung HS (1999), Nature 401:788–791.
- DOI: `10.1038/44565`; [publication/source](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/lee-nature-99.pdf); code: https://github.com/scikit-learn/scikit-learn.
- Access: University-hosted original full paper; nonnegative factorization
- Registry ID: `REP_NMF`.

<a id="liger"></a>
## LIGER
- **Single-Cell Multi-omic Integration Compares and Contrasts Features of Brain Cell Identity** — Welch JD; Kozareva V; Ferreira A; Vanderburg C; Martin C; Macosko EZ (2019), Cell 177:1873–1887.e17.
- DOI: `10.1016/j.cell.2019.05.006`; [publication/source](https://macoskolab.com/wp-content/uploads/2019/06/liger_paper.pdf); code: https://github.com/welch-lab/liger.
- Access: Author-hosted full paper; shared and dataset-specific metagenes
- Registry ID: `REP_LIGER`.

<a id="mofa"></a>
## MOFA
- **Multi-Omics Factor Analysis—a framework for unsupervised integration of multi-omics data sets** — Argelaguet R; Velten B; Arnol D; Dietrich S; Zenz T; Marioni JC; Buettner F; Huber W; Stegle O (2018), Molecular Systems Biology 14:e8124.
- DOI: `10.15252/msb.20178124`; [publication/source](https://link.springer.com/article/10.15252/msb.20178124); code: https://github.com/bioFAM/MOFA.
- Access: Original full text; Methods factor model, likelihoods and missing entries
- Registry ID: `REP_MOFA`.

<a id="mofa_plus"></a>
## MOFA_PLUS
- **MOFA+: a statistical framework for comprehensive integration of multi-modal single-cell data** — Argelaguet R; Arnol D; Bredikhin D; Deloro Y; Velten B; Marioni JC; Stegle O (2020), Genome Biology 21:111.
- DOI: `10.1186/s13059-020-02015-1`; [publication/source](https://link.springer.com/article/10.1186/s13059-020-02015-1); code: https://github.com/bioFAM/MOFA2.
- Access: Original full text; Methods, group/view model, likelihoods and code availability
- Registry ID: `REP_MOFA_PLUS`.

<a id="pmd"></a>
## PMD
- **A penalized matrix decomposition, with applications to sparse principal components and canonical correlation analysis** — Witten DM; Tibshirani R; Hastie T (2009), Biostatistics 10(3):515–534.
- DOI: `10.1093/biostatistics/kxp008`; [publication/source](https://hastie.su.domains/public/Papers/PMD_Witten.pdf); code: https://cran.r-project.org/package=PMA.
- Access: Author-hosted full paper; penalized decomposition and sparse CCA
- Registry ID: `REP_PMD`.

<a id="mnn"></a>
## MNN
- **Batch effects in single-cell RNA-sequencing data are corrected by matching mutual nearest neighbors** — Haghverdi L; Lun ATL; Morgan MD; Marioni JC (2018), Nature Biotechnology 36:421–427.
- DOI: `10.1038/nbt.4091`; [publication/source](https://www.nature.com/articles/nbt.4091); code: https://bioconductor.org/packages/release/bioc/html/batchelor.html.
- Access: Publisher abstract and official batchelor documentation; full author PDF fetch failed
- Registry ID: `REP_MNN`.

<a id="harmony"></a>
## HARMONY
- **Fast, sensitive and accurate integration of single-cell data with Harmony** — Korsunsky I; Millard N; Fan J; Slowikowski K; Zhang F; Wei K; Baglaenko Y; Brenner M; Loh PR; Raychaudhuri S (2019), Nature Methods 16:1289–1296.
- DOI: `10.1038/s41592-019-0619-0`; [publication/source](https://www.nature.com/articles/s41592-019-0619-0); code: https://github.com/immunogenomics/harmony.
- Access: Paper identity on official project site; official method documentation read; publisher failed and PMC CAPTCHA
- Registry ID: `REP_HARMONY`.

<a id="scanorama"></a>
## SCANORAMA
- **Efficient integration of heterogeneous single-cell transcriptomes using Scanorama** — Hie B; Bryson B; Berger B (2019), Nature Biotechnology 37:685–691.
- DOI: `10.1038/s41587-019-0113-3`; [publication/source](https://www.nature.com/articles/s41587-019-0113-3); code: https://github.com/brianhie/scanorama.
- Access: Publisher abstract and code availability; author repository API documentation; publisher body paywalled
- Registry ID: `REP_SCANORAMA`.

<a id="diffusion"></a>
## DIFFUSION
- **Diffusion maps** — Coifman RR; Lafon S (2006), Applied and Computational Harmonic Analysis 21(1):5–30.
- DOI: `10.1016/j.acha.2006.04.006`; [publication/source](https://www.math.ucdavis.edu/~strohmer/courses/270/diffusion_maps.pdf); code: not_applicable.
- Access: University-hosted original full paper; sections 2–3 diffusion operator and distance
- Registry ID: `REP_DIFFUSION`.

<a id="tsne"></a>
## TSNE
- **Visualizing Data using t-SNE** — van der Maaten L; Hinton G (2008), Journal of Machine Learning Research 9(86):2579–2605.
- DOI: `not_assigned`; [publication/source](https://www.jmlr.org/papers/v9/vandermaaten08a.html); code: https://lvdmaaten.github.io/tsne/.
- Access: Journal landing page and full PDF; sections 2–3 neighborhood probabilities and objective
- Registry ID: `REP_TSNE`.

<a id="umap"></a>
## UMAP
- **UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction** — McInnes L; Healy J; Melville J (2018), arXiv:1802.03426; v3 revised 2020.
- DOI: `10.48550/arXiv.1802.03426`; [publication/source](https://arxiv.org/abs/1802.03426); code: https://github.com/lmcinnes/umap.
- Access: Author preprint abstract/identity and official algorithm documentation; not a journal article
- Registry ID: `REP_UMAP`.

<a id="ot"></a>
## OT
- **Computational Optimal Transport** — Peyré G; Cuturi M (2019), Foundations and Trends in Machine Learning 11(5–6):355–607.
- DOI: `10.1561/2200000073`; [publication/source](https://arxiv.org/abs/1803.00567); code: https://github.com/PythonOT/POT.
- Access: Author preprint metadata/overview and book site; detailed solver equations supported by POT documentation; full PDF exceeds tool size
- Registry ID: `REP_OT`.

<a id="sinkhorn"></a>
## SINKHORN
- **Sinkhorn Distances: Lightspeed Computation of Optimal Transportation Distances** — Cuturi M (2013), Advances in Neural Information Processing Systems 26:2292–2300.
- DOI: `not_assigned`; [publication/source](https://arxiv.org/abs/1306.0895); code: https://github.com/PythonOT/POT.
- Access: Author preprint identity and abstract; Sinkhorn equations checked against official POT documentation
- Registry ID: `REP_SINKHORN`.

<a id="pot"></a>
## POT
- **POT: Python Optimal Transport** — Flamary R; Courty N; Gramfort A; Alaya MZ; Boisbunon A; Chambon S; Chapel L; Corenflos A; Fatras K; Fournier N; Gautheron L; Gayraud NT; Janati H; Rakotomamonjy A; Redko I; Rolet A; Schutz A; Seguy V; Sutherland DJ; Tavenard R; Tong A; Vayer T (2021), Journal of Machine Learning Research 22(78):1–8.
- DOI: `not_assigned`; [publication/source](https://jmlr.org/papers/v22/20-451.html); code: https://github.com/PythonOT/POT.
- Access: Original journal software paper and official POT documentation
- Registry ID: `REP_POT`.

<a id="multilayer"></a>
## MULTILAYER
- **Multilayer networks** — Kivelä M; Arenas A; Barthelemy M; Gleeson JP; Moreno Y; Porter MA (2014), Journal of Complex Networks 2(3):203–271.
- DOI: `10.1093/comnet/cnu016`; [publication/source](https://arxiv.org/abs/1309.7233); code: not_applicable.
- Access: Author preprint metadata and overview; structural terminology only
- Registry ID: `REP_MULTILAYER`.

<a id="pathsim"></a>
## PATHSIM
- **PathSim: Meta Path-Based Top-K Similarity Search in Heterogeneous Information Networks** — Sun Y; Han J; Yan X; Yu PS; Wu T (2011), Proceedings of the VLDB Endowment 4(11):992–1003.
- DOI: `unknown`; [publication/source](https://www.vldb.org/pvldb/vol4/p992-sun.pdf); code: not_applicable.
- Access: Original journal full PDF; typed information-network schema and meta-path definitions
- Registry ID: `REP_PATHSIM`.

<a id="higher"></a>
## HIGHER
- **Networks beyond pairwise interactions: Structure and dynamics** — Battiston F; Cencetti G; Iacopini I; Latora V; Lucas M; Patania A; Young JG; Petri G (2020), Physics Reports 874:1–92.
- DOI: `10.1016/j.physrep.2020.05.004`; [publication/source](https://arxiv.org/abs/2006.01764); code: not_applicable.
- Access: Author preprint identity/abstract; full PDF exceeds tool size; formal structures also supported by HyperNetX documentation
- Registry ID: `REP_HIGHER`.

<a id="tensor"></a>
## TENSOR
- **Tensor Decompositions and Applications** — Kolda TG; Bader BW (2009), SIAM Review 51(3):455–500.
- DOI: `10.1137/07070111X`; [publication/source](https://www.math.ucdavis.edu/~saito/data/tensor/kolda-bader_tensor-decomp-siamrev.pdf); code: https://www.tensortoolbox.org/.
- Access: University-hosted original full review; sections 2–4 tensor, CP and Tucker definitions
- Registry ID: `REP_TENSOR`.

<a id="gsva"></a>
## GSVA
- **GSVA: gene set variation analysis for microarray and RNA-Seq data** — Hänzelmann S; Castelo R; Guinney J (2013), BMC Bioinformatics 14:7.
- DOI: `10.1186/1471-2105-14-7`; [publication/source](https://link.springer.com/article/10.1186/1471-2105-14-7); code: https://bioconductor.org/packages/release/bioc/html/GSVA.html.
- Access: Original full article; nonparametric gene-set scoring and Methods
- Registry ID: `REP_GSVA`.

<a id="scenic"></a>
## SCENIC
- **SCENIC: single-cell regulatory network inference and clustering** — Aibar S; González-Blas CB; Moerman T; Huynh-Thu VA; Imrichova H; Hulselmans G; Rambow F; Marine JC; Geurts P; Aerts J; van den Oord J; Atak ZK; Wouters J; Aerts S (2017), Nature Methods 14:1083–1086.
- DOI: `10.1038/nmeth.4463`; [publication/source](https://www.nature.com/articles/nmeth.4463); code: https://github.com/aertslab/SCENIC.
- Access: Publication identity and workflow verified through official author repository; publisher fetch failed
- Registry ID: `REP_SCENIC`.

<a id="chromvar"></a>
## CHROMVAR
- **chromVAR: inferring transcription-factor-associated accessibility from single-cell epigenomic data** — Schep AN; Wu B; Buenrostro JD; Greenleaf WJ (2017), Nature Methods 14:975–978.
- DOI: `10.1038/nmeth.4401`; [publication/source](https://pubmed.ncbi.nlm.nih.gov/28825706/); code: https://github.com/GreenleafLab/chromVAR.
- Access: PubMed abstract and figure captions; official author repository documentation
- Registry ID: `REP_CHROMVAR`.

<a id="sk_decomp"></a>
## SK_DECOMP
- **Decomposing signals in components** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://scikit-learn.org/stable/modules/decomposition.html); code: https://github.com/scikit-learn/scikit-learn.
- Access: Official user guide; PCA, ICA, NMF, factor analysis, sparse PCA and kernel PCA sections
- Registry ID: `REP_SK_DECOMP`.

<a id="sk_cross"></a>
## SK_CROSS
- **Cross decomposition** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://scikit-learn.org/stable/modules/cross_decomposition.html); code: https://github.com/scikit-learn/scikit-learn.
- Access: Official user guide; CCA and PLS variants
- Registry ID: `REP_SK_CROSS`.

<a id="mofa_doc"></a>
## MOFA_DOC
- **MOFA2 documentation and FAQ** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://biofam.github.io/MOFA2/faq.html); code: https://github.com/bioFAM/MOFA2.
- Access: Official FAQ read: missing likelihood entries, views, factors, groups and successor code
- Registry ID: `REP_MOFA_DOC`.

<a id="liger_doc"></a>
## LIGER_DOC
- **Perform iNMF on scaled datasets — runINMF** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://welch-lab.github.io/liger/reference/runINMF.html); code: https://github.com/welch-lab/liger.
- Access: Official objective and input/output documentation; prose contains inconsistent H orientation, corrected in our explicit row convention
- Registry ID: `REP_LIGER_DOC`.

<a id="umap_doc"></a>
## UMAP_DOC
- **How UMAP Works** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html); code: https://github.com/lmcinnes/umap.
- Access: Official algorithm explanation; fuzzy neighborhoods and embedding optimization
- Registry ID: `REP_UMAP_DOC`.

<a id="pot_doc"></a>
## POT_DOC
- **POT user guide** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://pythonot.github.io/); code: https://github.com/PythonOT/POT.
- Access: Official overview and solver documentation; OT, entropic OT and Gromov-Wasserstein
- Registry ID: `REP_POT_DOC`.

<a id="go"></a>
## GO
- **Guide to GO evidence codes** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://geneontology.org/docs/guide-go-evidence-codes/); code: not_applicable.
- Access: Official evidence-code guide read; evidence provenance and inferred annotations
- Registry ID: `REP_GO`.

<a id="reactome"></a>
## REACTOME
- **Reactome Userguide** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://reactome.org/userguide); code: not_applicable.
- Access: Official user guide: reactions, pathways, species comparison and computationally inferred events
- Registry ID: `REP_REACTOME`.

<a id="string"></a>
## STRING
- **STRING functional protein association networks — Help** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://string-db.org/cgi/info); code: not_applicable.
- Access: Official Info/FAQ: functional versus physical settings and evidence channels; old download examples not used
- Registry ID: `REP_STRING`.

<a id="vmls"></a>
## VMLS
- **Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares** — Boyd S; Vandenberghe L (2018), Cambridge University Press.
- DOI: `not_applicable`; [publication/source](https://stanford.edu/~boyd/vmls/); code: not_applicable.
- Access: https://stanford.edu/~boyd/vmls/
- Registry ID: `MATH_VMLS_2018`.

<a id="bhk"></a>
## BHK
- **Foundations of Data Science** — Blum A; Hopcroft J; Kannan R (2020), Cambridge University Press.
- DOI: `not_applicable`; [publication/source](https://www.cs.cornell.edu/jeh/book.pdf); code: not_applicable.
- Access: https://www.cs.cornell.edu/jeh/book.pdf
- Registry ID: `MATH_BHK_2020`.

<a id="mml"></a>
## MML
- **Mathematics for Machine Learning** — Deisenroth MP; Faisal AA; Ong CS (2020), Cambridge University Press.
- DOI: `not_applicable`; [publication/source](https://mml-book.github.io/); code: not_applicable.
- Access: https://mml-book.github.io/
- Registry ID: `MATH_MML_2020`.

<a id="prob"></a>
## PROB
- **Introduction to Probability, second edition** — Blitzstein JK; Hwang J (2019), Chapman & Hall/CRC.
- DOI: `not_applicable`; [publication/source](https://stat110.hsites.harvard.edu/); code: not_applicable.
- Access: https://stat110.hsites.harvard.edu/
- Registry ID: `MATH_BLITZSTEIN_HWANG_2019`.

<a id="info"></a>
## INFO
- **Entropy and Information Theory, first edition corrected June 26 2023** — Gray RM (2023), Author revision of Springer-Verlag first edition (1990).
- DOI: `not_applicable`; [publication/source](https://www-ee.stanford.edu/~gray/it.pdf); code: not_applicable.
- Access: https://www-ee.stanford.edu/~gray/it.pdf
- Registry ID: `MATH_GRAY_INFORMATION_2023`.

<a id="integration"></a>
## INTEGRATION
- **Computational principles and challenges in single-cell data integration** — Argelaguet R; Cuomo ASE; Stegle O; Marioni JC (2021), Nature Biotechnology.
- DOI: `10.1038/s41587-021-00895-7`; [publication/source](https://www.nature.com/articles/s41587-021-00895-7); code: not_applicable.
- Access: Nature Biotechnology
- Registry ID: `ARGELAGUET_NATBIOTECH_2021`.

<a id="paste"></a>
## PASTE
- **Alignment and integration of spatial transcriptomics data** — Zeira R; Land M; Strzalkowski A; Raphael BJ (2022), Nature Methods.
- DOI: `10.1038/s41592-022-01459-6`; [publication/source](https://www.nature.com/articles/s41592-022-01459-6); code: https://github.com/raphael-group/paste.
- Access: Nature Methods
- Registry ID: `ZEIRA_NATMETHODS_2022`.

<a id="ensembl"></a>
## ENSEMBL
- **Ensembl Stable IDs (June 2026 archive)** — Ensembl (2026), Ensembl documentation.
- DOI: `not_applicable`; [publication/source](https://jun2026.archive.ensembl.org/info/genome/stable_ids/index.html); code: not_applicable.
- Access: https://jun2026.archive.ensembl.org/info/genome/stable_ids/index.html
- Registry ID: `ENSEMBL_STABLEIDS_2026`.

<a id="pca"></a>
## PCA
- **Principal component analysis: a review and recent developments** — Jolliffe IT; Cadima J (2016), Philosophical Transactions of the Royal Society A 374:20150202.
- DOI: `10.1098/rsta.2015.0202`; [publication/source](https://pubmed.ncbi.nlm.nih.gov/26953178/); code: https://github.com/scikit-learn/scikit-learn.
- Access: PubMed identity/abstract; publisher forbidden and PMC CAPTCHA; derivations also supported by MML and official decomposition guide
- Registry ID: `REP_PCA`.

<a id="cca"></a>
## CCA
- **Relations between two sets of variates** — Hotelling H (1936), Biometrika 28(3–4):321–377.
- DOI: `10.1093/biomet/28.3-4.321`; [publication/source](https://academic.oup.com/biomet/article-abstract/28/3-4/321/220073); code: https://github.com/scikit-learn/scikit-learn.
- Access: Publisher abstract/identity; modern formulation supported by Witten and official cross-decomposition documentation
- Registry ID: `REP_CCA`.

<a id="pls"></a>
## PLS
- **PLS-regression: a basic tool of chemometrics** — Wold S; Sjöström M; Eriksson L (2001), Chemometrics and Intelligent Laboratory Systems 58(2):109–130.
- DOI: `10.1016/S0169-7439(01)00155-1`; [publication/source](https://www.sciencedirect.com/science/article/pii/S0169743901001551); code: https://github.com/scikit-learn/scikit-learn.
- Access: Publisher abstract/introduction; PLS variants checked in official cross-decomposition documentation
- Registry ID: `REP_PLS`.

<a id="kpca"></a>
## KPCA
- **Nonlinear Component Analysis as a Kernel Eigenvalue Problem** — Schölkopf B; Smola A; Müller KR (1998), Neural Computation 10(5):1299–1319.
- DOI: `10.1162/089976698300017467`; [publication/source](https://is.mpg.de/en/publications/1509); code: https://github.com/scikit-learn/scikit-learn.
- Access: Author institution search-index record; direct page returned 403; exact eigencoordinate formulation supported by official decomposition guide
- Registry ID: `REP_KPCA`.

<a id="pseudotime"></a>
## PSEUDOTIME
- **The dynamics and regulators of cell fate decisions are revealed by pseudotemporal ordering of single cells** — Trapnell C; Cacchiarelli D; Grimsby J; Pokharel P; Li S; Morse M; Lennon NJ; Livak KJ; Mikkelsen TS; Rinn JL (2014), Nature Biotechnology 32:381–386.
- DOI: `10.1038/nbt.2859`; [publication/source](https://cole-trapnell-lab.github.io/pdfs/papers/trapnell-cacchiarelli-monocle.pdf); code: https://github.com/cole-trapnell-lab/monocle-release.
- Access: Original author-hosted paper and PubMed identity; pseudotemporal ordering concept
- Registry ID: `REP_PSEUDOTIME`.

<a id="networkx"></a>
## NETWORKX
- **NetworkX graph types** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://networkx.org/documentation/stable/reference/classes/index.html); code: https://github.com/networkx/networkx.
- Access: Official classes documentation; directed, undirected, multigraph and attributes
- Registry ID: `REP_NETWORKX`.

<a id="hypernetx"></a>
## HYPERNETX
- **HyperNetX documentation** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://hypernetx.readthedocs.io/en/latest/); code: https://github.com/pnnl/HyperNetX.
- Access: Official documentation; hypergraphs as set systems and source link
- Registry ID: `REP_HYPERNETX`.

<a id="tensor_doc"></a>
## TENSOR_DOC
- **Tensor Toolbox for MATLAB** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://www.tensortoolbox.org/); code: https://gitlab.com/tensors/tensor_toolbox.
- Access: Official software page; author-linked implementation and CP/Tucker methods
- Registry ID: `REP_TENSOR_DOC`.

<a id="uniprot"></a>
## UNIPROT
- **UniProtKB and annotation evidence** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://www.uniprot.org/help/uniprotkb/); code: not_applicable.
- Access: Official indexed help text: curated versus computational records; direct help rendering returned JavaScript fallback
- Registry ID: `REP_UNIPROT`.

<a id="sk_neighbors"></a>
## SK_NEIGHBORS
- **Nearest Neighbors** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://scikit-learn.org/stable/modules/neighbors.html); code: https://github.com/scikit-learn/scikit-learn.
- Access: Official user guide; neighbors, search algorithms and graph encoding
- Registry ID: `REP_SK_NEIGHBORS`.

<a id="destiny"></a>
## DESTINY
- **destiny: diffusion maps** — Official project maintainers (2026), Official documentation; accessed 2026-09-11.
- DOI: `not_applicable`; [publication/source](https://bioconductor.org/packages/release/bioc/html/destiny.html); code: https://bioconductor.org/packages/release/bioc/html/destiny.html.
- Access: Official Bioconductor package description and source links; diffusion-map implementation, not original Coifman code
- Registry ID: `REP_DESTINY`.
