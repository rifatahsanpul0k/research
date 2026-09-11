# 8. scATAC-seq

ATAC-seq uses Tn5 transposase to insert adapters preferentially into accessible chromatin. Sequencing the resulting fragments samples accessible DNA, not RNA expression or all genomic DNA [S08][S09].

After barcode assignment and alignment, fragments may be counted over called genomic peaks. A cell-by-region matrix (X_{ATAC}\in\mathbb N_0^{n\times r}) has (r) regions; entries can be fragment counts, cut-site counts, binary accessibility, or other processed values. Peak calling and reference annotation define the feature set.

Accessibility may reflect regulatory potential, but an accessible region does not imply that a nearby gene is expressed. Peak-to-gene links are hypotheses dependent on distance, contacts, and cell context [S09][S10]. Fragment depth, TSS enrichment, nucleosome patterns, and FRiP are QC descriptors, not universal biological labels.

**Evidence:** [S08], [S09], [S10].
