# Preprocessing principles

**Status: verified notes; descriptive, pre-modeling scope.**

### A–C. Meaning, mechanism, relationships

An observed matrix is a measurement of captured molecules, fragments, tags, or coordinates, not the complete biological state of a cell or spot. Sequencing, capture efficiency, molecule loss, amplification and feature assignment make the observed value (X_{ij}^{obs}) a noisy sample of an underlying process. A preprocessing operation is a declared function (X^{proc}=f(X^{obs};	heta)): it can change scale, variance, sparsity, feature relations, distances and therefore neighborhoods. The operation must be interpreted with the assay and observation unit. QC describes observations; filtering removes records; normalization changes comparability; transformation changes the numerical scale [S01,S06,S08,S16].

### D–F. Measurement, numerical form, project relevance

The source files are AnnData H5AD objects. An (n\times p) CSR matrix stores `data`, `indices`, and `indptr`; `obs` stores observation metadata, `var` feature metadata, and `obsm/spatial` coordinate arrays [S20,S22]. For example, a 3-cell RNA matrix is

|   | Gene A | Gene B | Gene C |
|---|---:|---:|---:|
| C1 | 8 | 0 | 3 |
| C2 | 1 | 6 | 2 |
| C3 | 7 | 0 | 4 |

Rows are assay observations, columns are feature identifiers, and values are stored assay quantities whose exact semantics must be checked. The same discipline is required for spatial omics (coordinates and footprint) and multi-omics (pairing and modality-specific units). Later similarity or representation learning can preserve technical variation or erase biology depending on (f); this phase therefore records alternatives without selecting one.

### G. Misconceptions and H. Evidence

“Raw” does not mean biologically complete, a zero is not always absence, and a processed value is not a molecule count. A QC threshold is a decision with a loss function, not a biological law. Sources: Brennecke et al. [S36], Hafemeister & Satija [S37], OSCA normalization/data infrastructure [S38,S39], AnnData and 10x format documentation [S20,S22].
