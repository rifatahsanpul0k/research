# Biological-prior representations

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Prior information defines an additional mapping

A prior-based representation combines a measured table X:n×p with an annotation relation P, such as gene×pathway membership. A simple linear score \(R=XP\) has shape n×r when P:p×r, but many annotation-based methods use nonlinear scoring. The output summarizes the selected prior vocabulary; it does not independently establish biological function.

| Resource | Information relevant here | Provenance to retain |
|---|---|---|
| Gene Ontology | Functional annotations with evidence codes | Term, relation, evidence, taxon and source |
| Reactome | Reactions/pathways and species mappings | Event IDs, release, curated versus inferred status |
| STRING | Functional associations and optional physical network | Evidence channels, network type, species and score meaning |
| UniProt | Protein sequences/annotations, curated and computational records | Accession/isoform, assertion source and evidence |
| Ensembl | Gene/transcript/protein identifiers and versions | Genome assembly, release, version and mapping multiplicity |

These resources distinguish evidence types and identifiers rather than providing a single universal truth label.[^1][^2][^3][^4][^5]

## Project implications

A biological prior can make coordinates traceable to named processes or relations, but can also exclude unannotated genes, overrepresent well-studied processes, or transfer assertions across incompatible contexts. A gene-to-protein mapping may be one-to-many; an antibody target is not automatically one transcript's direct measurement. Cross-species mapping introduces another assumption.

For this project, no database payload, pathway membership matrix or knowledge graph is downloaded or instantiated. Before any future use, retain the measured feature universe, mapping coverage, unmatched IDs, evidence filters and database version. Absence of annotation is not evidence of no function. A prior used to build a representation cannot also serve as fully independent biological validation without accounting for circularity.

Storage depends on memberships/edges plus n×r scores; sparse aggregation costs about O(n·nnz(P)) for dense X under a simple multiplication strategy. Complex scoring or network propagation has different costs. Priors do not intrinsically handle missing assays, spatial frames or unknown observation units. The representation family remains unranked.

## Evidence

[^1]: Official project maintainers (2026). [Guide to GO evidence codes](https://geneontology.org/docs/guide-go-evidence-codes/). See [access record](SOURCES.md#go).
[^2]: Official project maintainers (2026). [Reactome Userguide](https://reactome.org/userguide). See [access record](SOURCES.md#reactome).
[^3]: Official project maintainers (2026). [STRING functional protein association networks — Help](https://string-db.org/cgi/info). See [access record](SOURCES.md#string).
[^4]: Official project maintainers (2026). [UniProtKB and annotation evidence](https://www.uniprot.org/help/uniprotkb/). See [access record](SOURCES.md#uniprot).
[^5]: Ensembl (2026). [Ensembl Stable IDs (June 2026 archive)](https://jun2026.archive.ensembl.org/info/genome/stable_ids/index.html). See [access record](SOURCES.md#ensembl).
