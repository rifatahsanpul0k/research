# Biology to data

The measurement bridge is:

`biological sample → preparation/capture → labeled molecules → library → sequencing/measurement → assigned molecules → feature identifiers → matrix + metadata/coordinates`.

For the toy RNA matrix

\[
X_{RNA}=\begin{bmatrix}8&0&3\\1&6&2\\7&0&4\end{bmatrix}
\]

rows are observations C1–C3, columns are genes A–C, and 8 means eight assigned molecules/count units for gene A in C1 under the assay’s counting definition. It does not mean eight total biological transcripts existed in C1. ADT uses the same row linkage when paired:

\[
X_{ADT}=\begin{bmatrix}20&3\\2&18\\14&6\end{bmatrix}
\]

with columns protein markers P1–P2. ATAC can be represented as

\[
X_{ATAC}=\begin{bmatrix}1&0&0&2\\0&1&3&0\\2&0&1&0\end{bmatrix},
\]

where columns are genomic regions R1–R4 and values are fragments or another documented accessibility unit. Spatial coordinates are

\[
S=\begin{bmatrix}x_1&y_1\\x_2&y_2\\x_3&y_3\end{bmatrix}.
\]

Rows can be linked across matrices only when observation IDs and experimental design establish pairing. `obs` stores row metadata; `var` stores feature metadata; masks record missing modalities. A matrix can be sparse, filtered, normalized, or transformed, so its numerical values need a provenance record.

Two similar numerical vectors do not automatically imply biologically equivalent cells. They may be similarly sampled, share ambient RNA, be mixtures in spots, differ in protein activity despite similar RNA, or be measured under different depth/batch conditions. Biological equivalence requires compatible observation units, assays, identifiers, tissue context, metadata, and evidence beyond vector distance [S07][S13][S16][S17].

**Evidence:** [S01], [S06], [S09], [S11], [S13], [S16], [S20], [S22].
