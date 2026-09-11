# Biological hierarchy and annotation resolution

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

Biological classifications can be hierarchical: a broad class contains more specific categories. Type/subtype granularity determines which distinctions a label expresses. Ontologies make definitions and relationships explicit, helping align terminology across studies.[^TYPE][^ONTO]

## B. Mechanism

The following is a deliberately partial teaching hierarchy, not a complete ontogenetic tree:

```text
Immune cell
  Lymphocyte
    T cell
      CD4 T cell
      CD8 T cell
    B cell
  Myeloid cell
```

The immunological categories draw on lymphocyte biology; the sketch omits other populations and developmental exceptions. CD4/CD8 classification here refers to a broad mature T-cell context, not an assertion that developing T cells are always exclusively one or the other.[^IMMUNE][^TDEV]

An ontology's “is-a” relationship is not necessarily an observed parent–daughter relation. A biological category can also participate in several classification relationships rather than one strict tree.[^ONTO]

## C. Relationship to prior concepts

Lineage (4) describes actual descent; hierarchy here describes categories. Anatomical “part-of” relations, such as medulla within lymph node, differ from both. State labels may apply across several subtypes rather than defining one exclusive child category.

## D. Experimental observation/measurement

Evidence must support the label's resolution. Morphology, molecular features and function can support different levels; naming finer categories does not by itself increase biological certainty.[^TYPE] Keep reference provenance and explicit definitions when reconciling labels.[^ONTO]

## E. Computational representation

Synthetic annotation-resolution example:

| observation | reference_fine | proposed_fine | shared_parent |
|---|---|---|---|
| A | CD4 T cell | CD8 T cell | T cell |
| B | B cell | CD8 T cell | lymphocyte |

The first disagreement preserves the broad T-cell class; the second does not. This explains why a future evaluation must report its label resolution. It is not a model benchmark or justification for overlooking subtype errors.

Possible forms include parent–child tables, nested sets, ontology networks, categorical labels at several resolutions and distributions over labels. A probability distribution over mutually exclusive leaf categories may be aggregated to parents under that explicit convention; overlapping categories require care.

## F. Relevance to our project

LN evaluation could emphasize broad immune/stromal distinctions or finer lymphocyte categories. Brain developmental roles and mature neuronal subtypes are different resolutions, not interchangeable vocabularies. Biological objectives must establish which errors matter before future representations are compared.

## G. Common misconceptions

A hierarchy is not a lineage trace; a broad correct label does not validate a fine label; a “part-of” link is not “is-a”. No complete immune or brain taxonomy is claimed. Check: plasma cells belong to a B-lineage developmental context, but a plasma-cell state is not equivalent to every B-cell annotation.

## H. Evidence

[^TYPE]: Zeng H (2022). [What is a cell type and how to define it?](https://pubmed.ncbi.nlm.nih.gov/35868277/). Cell. DOI: 10.1016/j.cell.2022.06.031. Supporting location/access: [source TYPE](SOURCES.md#type).

[^ONTO]: Osumi-Sutherland D; Xu C; Keays M; Levine AP; Kharchenko PV; Regev A; Lein E; Teichmann SA (2021). [Cell type ontologies of the Human Cell Atlas](https://pubmed.ncbi.nlm.nih.gov/34750578/). Nature Cell Biology. DOI: 10.1038/s41556-021-00787-7. Supporting location/access: [source ONTO](SOURCES.md#onto).

[^IMMUNE]: Janeway CA Jr; Travers P; Walport M; Shlomchik MJ (2001). [The components of the immune system](https://www.ncbi.nlm.nih.gov/books/NBK27092/). Immunobiology: The Immune System in Health and Disease, 5th edition. DOI: unknown. Supporting location/access: [source IMMUNE](SOURCES.md#immune).

[^TDEV]: Janeway CA Jr; Travers P; Walport M; Shlomchik MJ (2001). [Generation of lymphocytes in bone marrow and thymus](https://www.ncbi.nlm.nih.gov/books/NBK27123/). Immunobiology: The Immune System in Health and Disease, 5th edition. DOI: unknown. Supporting location/access: [source TDEV](SOURCES.md#tdev).

