# 15. Feature identifiers and annotation

RNA features may be gene symbols, Ensembl gene IDs, transcript IDs, or probe IDs. ATAC features are genomic intervals/peaks tied to a reference assembly. ADT features are antibody or protein names. Ensembl stable IDs identify genes, transcripts, exons, and proteins; version suffixes can change across annotation releases [S25].

Mappings are not generally one-to-one: one gene has transcripts, transcripts can encode protein products, symbols can change, and peaks can overlap multiple genes. Duplicate names require explicit disambiguation. A feature matrix must retain the identifier source, genome build, annotation release, and feature order.

Joining by display name can silently duplicate, drop, or misalign features. Cross-species symbols and version-stripped IDs are especially risky. Multimodal correspondence must be recorded as a mapping with evidence and uncertainty, not assumed from string similarity.

**Evidence:** [S25], [S02], [S09].
