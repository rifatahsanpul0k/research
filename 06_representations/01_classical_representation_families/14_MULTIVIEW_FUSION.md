# Multiple views and classical alignment methods

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Where combination occurs

Let \(X^{(m)}:n_m\times p_m\), m=1,…,v. A correspondence table must specify whether rows describe the same physical observations. Early fusion concatenates compatible paired rows before fitting; intermediate fusion transforms views and combines their coordinates or relationships; late fusion combines separate decisions/summaries. These categories specify pipeline position, not one mathematical object or a quality order. Shared and view-specific information need not have the same biological relevance.[^1]

For paired data, \(R=[f_1(X^{(1)})|\cdots|f_v(X^{(v)})]\) has n rows and Σk_m columns if each transform returns n×k_m. An alternative retains the tuple of matrices without forcing one coordinate system. A late decision combination \(p_i=\sum_m\alpha_mp_i^{(m)}\) is a probability vector only if all component vectors share a category vocabulary, weights are nonnegative and sum to one. This equation defines a possible construction, not a fitted project method.

## Three representative batch-alignment mechanisms

| Method | Input and mechanism studied | Output object | Limits to carry forward |
|---|---|---|---|
| MNN | Datasets in a comparable expression feature space; identify mutual nearest neighbors across batches and use their differences to estimate correction vectors | Corrected feature values in the original approach; fastMNN is a distinct low-dimensional implementation | Needs shared populations and assumptions separating batch shifts from biological variation; arbitrary disjoint modalities do not satisfy the common-space input |
| Harmony | Initial low-dimensional coordinates plus batch covariates; iterative soft clustering encourages batch diversity and estimates cluster-dependent corrections | Corrected observation embedding, not a new measured count matrix | Integration depends on the initial representation and covariates; genuine stage effects confounded with batch may be removed |
| Scanorama | Expression matrices with gene identifiers; find cross-dataset matches and join compatible datasets into panoramas | API distinguishes integrated low-dimensional embeddings from corrected expression output | Matching shared states does not establish lineage or equivalent assays; unmatched populations and feature intersections matter |

The MNN publication and batchelor documentation support the first mechanism; the official Harmony project documents its embedding-level procedure; Scanorama's paper and author API distinguish integration and correction outputs.[^2][^3][^4] No published speed or accuracy rankings are transferred to this project.

## Project interpretation

These are alignment mechanisms that **produce** representations. They do not prove that every batch effect should be removed. Before future use we need the donor/section/batch/stage design and a defensible definition of variation to retain. E11 through E18 are chronological categories; aligning them cannot be treated as neutral nuisance correction. None of these base RNA alignment mechanisms automatically reconciles genes, antibodies and unequal peak sets.

For paired views, absent entries require a declared policy; for unpaired datasets, matching needs biological overlap and an identifiable comparison space. Masking, selecting a shared feature axis and inferred correspondence are different operations. Memory generally includes input/embedding and neighbor/correction structures; exact all-pair matching can cost O(n²d) in d coordinates, while approximate searches and method-specific implementations change the cost and introduce additional sensitivity. No software was installed, cloned or run. Official repositories are recorded for later reproducibility work.

## Evidence

[^1]: Argelaguet R; Cuomo ASE; Stegle O; Marioni JC (2021). [Computational principles and challenges in single-cell data integration](https://www.nature.com/articles/s41587-021-00895-7). See [access record](SOURCES.md#integration).
[^2]: Haghverdi L; Lun ATL; Morgan MD; Marioni JC (2018). [Batch effects in single-cell RNA-sequencing data are corrected by matching mutual nearest neighbors](https://www.nature.com/articles/nbt.4091). See [access record](SOURCES.md#mnn).
[^3]: Korsunsky I; Millard N; Fan J; Slowikowski K; Zhang F; Wei K; Baglaenko Y; Brenner M; Loh PR; Raychaudhuri S (2019). [Fast, sensitive and accurate integration of single-cell data with Harmony](https://www.nature.com/articles/s41592-019-0619-0). See [access record](SOURCES.md#harmony).
[^4]: Hie B; Bryson B; Berger B (2019). [Efficient integration of heterogeneous single-cell transcriptomes using Scanorama](https://www.nature.com/articles/s41587-019-0113-3). See [access record](SOURCES.md#scanorama).
