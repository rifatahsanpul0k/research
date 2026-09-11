# 7. ADT and CITE-seq

CITE-seq uses antibodies covalently linked to oligonucleotides. Antibody binding measures epitopes, while the oligo barcode is amplified and sequenced alongside transcriptome tags [S06]. The usual observation is a cell or partition; (X_{ADT}\in\mathbb N_0^{n\times q}) stores assigned ADT counts for (q) antibody features.

RNA abundance ≠ protein abundance ≠ protein activity. Translation, trafficking, degradation, epitope accessibility, and post-translational regulation separate these quantities. ADT background includes nonspecific binding, free antibody tags, ambient antibody, and saturation; isotype/empty-droplet controls can reveal background [S06][S07].

When RNA and ADT rows share documented barcodes, they are fully paired measurements of the same observation. A shared row index alone is insufficient if files were independently reordered or assembled. Protein panels are targeted and do not measure the whole proteome.

**Evidence:** [S06], [S07].
