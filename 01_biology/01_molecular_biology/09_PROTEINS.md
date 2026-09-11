# 09. Proteins

Status: Phase 1A notes complete; source-backed teaching scaffold.

## A. Biological meaning

Proteins are polymers of amino acids that fold into structures able to catalyze reactions, provide structure, transport molecules, signal, bind DNA/RNA, and carry out many cellular functions. For protein-coding genes, protein sequence is specified by coding information read through mRNA [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK21050/).

## B. Biological mechanism

After translation, a polypeptide folds into a functional conformation, may join complexes, localize to specific compartments, and undergo chemical modifications. Protein abundance depends on translation, folding, trafficking, modification, and degradation, not only mRNA abundance [Alberts 2002, Ch. 6](https://www.ncbi.nlm.nih.gov/books/NBK26829/).

## C. Relationships

Proteins are the usual functional output of protein-coding gene expression. They can regulate earlier stages by binding DNA, modifying chromatin, controlling transcription, processing RNA, or participating in signaling.

## D. Experimental measurement

Proteins can be measured by mass spectrometry, antibody-based assays, flow cytometry, immunostaining, Western blotting, affinity reagents, and single-cell multimodal protein measurements. Each method has specificity, sensitivity, dynamic range, and background limitations.

## E. Numerical/computational representation

Protein measurements may become a cells x proteins matrix:

| cell_id | CD3_protein | CD19_protein | ProteinX |
|---|---:|---:|---:|
| C1 | 120 | 2 | 8 |
| C2 | 4 | 95 | 3 |

A feature metadata table should record antibody, protein identifier, gene link, and assay chemistry when available.

## F. Relevance to our project

Single-cell multi-omics may combine RNA and protein features from the same or matched cells. Spatial methods may detect proteins in tissue context. Biological similarity based on proteins can differ from similarity based on RNA because proteins integrate translation, degradation, localization, and cell surface state. Representation learning needs to respect modality-specific noise and biological meaning.

## G. Misconceptions

- Treating gene expression and protein abundance as interchangeable.
- Assuming antibody feature names uniquely identify proteins without reagent metadata.
- Ignoring post-translational modification and localization when interpreting protein function.

## H. Evidence

- Alberts et al., *Molecular Biology of the Cell*, Chapter 6.
- Baysoy et al., 2023, *Nature Reviews Molecular Cell Biology*, single-cell multi-omics and proteome modalities.

