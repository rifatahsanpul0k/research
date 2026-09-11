# 4. scRNA-seq

scRNA-seq measures sampled RNA molecules from isolated cells. Dissociation, capture in a droplet or well, reverse transcription, cDNA amplification, observation/UMI barcoding, library preparation, sequencing, mapping, and gene assignment produce a cell-by-gene matrix [S01][S02].

The observation unit is intended to be a cell, but damaged cells, empty droplets, and multiplets violate that intention. (X_{RNA}\in\mathbb N_0^{n\times p}), where (X_{ij}) is the observed assigned count for gene (j) in observation (i). It is an observation of captured and sequenced molecules, not the exact cellular RNA inventory.

Capture efficiency, transcript length, sequencing depth, ambient RNA, barcode errors, and annotation affect counts. A zero can mean no sampled molecule, insufficient sampling, assay sensitivity, or processing. scRNA-seq supports cell-state and cell-type study, but similarity in (X) is conditional on these measurement limits and metadata [S16][S18].

**Evidence:** [S01], [S02], [S03], [S16], [S18].
