# Cell identity, type and state

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

A cell is a membrane-bounded biological system whose organized molecules sustain cellular processes. The plasma membrane separates internal from external conditions and mediates exchange and signaling. A nucleus is a compartment of a eukaryotic cell, not an entire cell.[^MEM]

**Cell type** names a category of cellular organization; **subtype** refines that category. **State** describes a condition of a cell within a chosen classification. **Phenotype** is the set of observable characteristics, including morphology, molecules and function. Identity integrates these with developmental history; it is not identical to an RNA vector.[^IDENT]

## B. Mechanism

Regulatory programs shape expression and protein output; protein activity and environmental input help determine phenotype. This is an interacting causal system, not an arithmetic sum of independent factors.[^REG][^PROT]

For T cells, naive, activated, memory and exhausted describe useful distinctions within a broader identity. Activation may be transient, whereas memory and exhaustion can involve persistent differentiation programs. “State” therefore does not mean automatically short-lived or reversible, and the four labels are not equally simple or mutually exclusive switches.[^TSTATE]

## C. Relationship to prior concepts

Phase 1A supplies molecules and Phase 1B their regulation. Here those concepts support a cellular classification. The next topic asks why members of the same category still differ. Type/state boundaries depend on the biological question and evidence; a functional state is a condition of activity, not proof of a new ancestry.[^TYPE]

## D. Experimental observation/measurement

Microscopy characterizes shape and organization; molecular measurements characterize selected constituents; functional observations characterize what cells do. Combining these gives different evidence from assigning identity on molecular profiles alone.[^TYPE] Repeated observations are needed to support persistence rather than merely naming a snapshot “stable”.

## E. Computational representation

A proposed metadata design:

| observation | broad_type | subtype | state | functional_evidence | label_source |
|---|---|---|---|---|---|
| A | T cell | unknown | activated_candidate | not_measured | hypothetical reviewer |
| B | T cell | unknown | unknown | not_measured | hypothetical reviewer |

These are fictional labels. `unknown` differs from a negative finding. Categorical labels, phenotype vectors, continuous activity scores and distributions over candidate labels encode different claims.

## F. Relevance to our project

For single-cell interpretation, distinguish identity from condition. For spatial biology, record environment independently. For multi-omics, ask which component of phenotype each measurement supports. Future similarity, representation learning and downstream evaluation must specify whether the target is type, state or function; this phase selects no method.

## G. Common misconceptions

A cell is not defined by one marker, one cluster or its position. “Same genome” does not imply the same phenotype. “Same T-cell type” does not imply the same activation history. Comprehension check: identical RNA measurements plus different protein activation can support different states without establishing different types.[^REG][^PROT][^TYPE]

## H. Evidence

[^MEM]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [Membrane Structure](https://www.ncbi.nlm.nih.gov/books/NBK21055/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source MEM](SOURCES.md#mem).

[^IDENT]: Morris SA (2019). [The evolving concept of cell identity in the single cell era](https://pubmed.ncbi.nlm.nih.gov/31249002/). Development. DOI: 10.1242/dev.169748. Supporting location/access: [source IDENT](SOURCES.md#ident).

[^REG]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [An Overview of Gene Control](https://www.ncbi.nlm.nih.gov/books/NBK26885/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source REG](SOURCES.md#reg).

[^PROT]: Alberts B; Johnson A; Lewis J; Raff M; Roberts K; Walter P (2002). [Protein Function](https://www.ncbi.nlm.nih.gov/books/NBK26911/). Molecular Biology of the Cell, 4th edition. DOI: unknown. Supporting location/access: [source PROT](SOURCES.md#prot).

[^TSTATE]: Wherry EJ; Kurachi M (2015). [Molecular and cellular insights into T cell exhaustion](https://pmc.ncbi.nlm.nih.gov/articles/PMC4889009/). Nature Reviews Immunology. DOI: 10.1038/nri3862. Supporting location/access: [source TSTATE](SOURCES.md#tstate).

[^TYPE]: Zeng H (2022). [What is a cell type and how to define it?](https://pubmed.ncbi.nlm.nih.gov/35868277/). Cell. DOI: 10.1016/j.cell.2022.06.031. Supporting location/access: [source TYPE](SOURCES.md#type).

