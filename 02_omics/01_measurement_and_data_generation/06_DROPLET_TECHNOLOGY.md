# 6. Droplet technology

Microfluidic droplets pair beads and sampled cells or nuclei. Bead oligos carry observation barcodes and UMIs; captured molecules are copied into tagged cDNA, pooled, amplified, and sequenced [S01].

Observed barcodes include empty droplets containing ambient molecules, droplets with two or more cells (doublets/multiplets), and damaged cells. Consequently one barcode is an index for a partition, not a mathematical guarantee of one intact biological cell. Ambient RNA can create counts for genes absent from the captured cell; multiplets create mixtures [S18].

Cell calling and doublet flags are derived metadata. Empty-droplet handling changes which rows enter a matrix, so filtered and unfiltered matrices answer different questions. Droplet chemistry, loading, and sequencing depth are technical covariates relevant to downstream biological similarity.

**Evidence:** [S01], [S18].
