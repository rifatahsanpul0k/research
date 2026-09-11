# Human lymph-node foundations

Phase 1C; biological foundations. Numerical examples are synthetic unless explicitly identified as user-provided metadata.

## A. Biological meaning

Lymph nodes are secondary lymphoid organs that receive tissue-draining lymph and organize immune surveillance. Lymphatic circulation returns interstitial fluid toward the blood and transports antigens and cells. The node supports encounters that initiate or shape responses; it is not the primary site of T-cell maturation.[^IMMUNE]

## B. Mechanism

| Cell category | Foundational function/context |
|---|---|
| B cells | Antigen-responsive lymphocytes; can generate antibody-secreting descendants |
| T cells | Antigen recognition with differentiated helper, regulatory or cytotoxic roles |
| Plasma cells | Specialized antibody secretion |
| Macrophages | Phagocytosis and handling of material in tissue |
| Conventional dendritic cells | Antigen presentation and initiation/shaping of T-cell responses |

These are broad categories, not a complete annotation panel.[^IMMUNE][^TDEV] Stromal cells organize supporting structures and local signals. Blood and lymphatic endothelial cells form different vascular interfaces; follicular dendritic cells are stromal cells and differ from conventional dendritic cells.[^STROMA]

| Anatomy | Position or organization |
|---|---|
| Capsule | Connective-tissue enclosure; trabeculae extend inward |
| Subcapsular sinus | Lymphatic space under the capsule receiving afferent lymph |
| Cortex | Outer region including lymphoid follicles |
| Follicles | B-cell-rich structures; primary follicles lack, secondary follicles contain germinal centers |
| Paracortex / T-cell zone | Deeper cortical territory rich in T cells, with dendritic cells |
| Medulla | Inner region organized into medullary cords and sinuses |
| Medullary cords | Cellular strands including plasma cells and other immune cells |
| Medullary sinuses | Lymph-flow spaces between cords |
| Vessels | Blood vessels and afferent/efferent lymphatics are distinct systems |
| Hilum | Exit region for efferent lymphatic drainage |
| Stromal compartments | Regionally organized reticular, follicular and endothelial components |

Anatomical descriptions: histology text and institutional guide.[^HIST][^ANATOMY] High endothelial venules (HEVs) are specialized blood venules supporting lymphocyte entry, not lymphatic sinuses.[^STROMA]

## C. Relationship to prior concepts

The distinction between cell identity and region is essential: a B-cell-rich follicle is not made exclusively of B cells, and antigen-presenting function is not one unique cell type. Local organization provides opportunities for interactions, not proof of a particular event.[^STROMA]

## D. Experimental observation/measurement

Histology reveals cords, sinuses and tissue organization; appropriately interpreted molecular staining helps identify constituents.[^HIST] A section may omit an anatomical feature because of orientation or sampling. Functional immune activity requires evidence beyond resemblance to a textbook diagram.

## E. Computational representation

A prospective annotation record, not a real assignment:

| dataset | observation | region_candidate | evidence | status |
|---|---|---|---|---|
| 10x_human_lymph_node_A1 | unknown | follicle | not_inspected | unverified |
| 10x_human_lymph_node_D1 | unknown | medulla | not_inspected | unverified |

Category tables, compartment masks, tissue hierarchies and protein/molecular feature matrices store different evidence. These candidates are examples of future questions, not populated dataset labels.

## F. Relevance to our project

A1 and D1 motivate this human anatomical foundation. Their actual condition, cell composition, sampled regions, observation units and annotations remain unknown in datasets.csv. Mouse stromal studies can explain mechanisms but do not validate annotations in these human specimens.

## G. Common misconceptions

Lymph node ≠ thymus; plasma cell ≠ a free antibody molecule; FDC ≠ conventional DC; sinus ≠ blood vessel; textbook compartment ≠ verified dataset label. Check: a T-rich region label is anatomical enrichment evidence, not proof that every observation is a T cell.

## H. Evidence

[^IMMUNE]: Janeway CA Jr; Travers P; Walport M; Shlomchik MJ (2001). [The components of the immune system](https://www.ncbi.nlm.nih.gov/books/NBK27092/). Immunobiology: The Immune System in Health and Disease, 5th edition. DOI: unknown. Supporting location/access: [source IMMUNE](SOURCES.md#immune).

[^TDEV]: Janeway CA Jr; Travers P; Walport M; Shlomchik MJ (2001). [Generation of lymphocytes in bone marrow and thymus](https://www.ncbi.nlm.nih.gov/books/NBK27123/). Immunobiology: The Immune System in Health and Disease, 5th edition. DOI: unknown. Supporting location/access: [source TDEV](SOURCES.md#tdev).

[^STROMA]: Mueller SN; Germain RN (2009). [Stromal cell contributions to the homeostasis and functionality of the immune system](https://www.nature.com/articles/nri2588). Nature Reviews Immunology. DOI: 10.1038/nri2588. Supporting location/access: [source STROMA](SOURCES.md#stroma).

[^HIST]: Mercadante AA; Tadi P (2023). [Histology, Lymph Nodes](https://www.ncbi.nlm.nih.gov/books/NBK559053/). StatPearls. DOI: unknown. Supporting location/access: [source HIST](SOURCES.md#hist).

[^ANATOMY]: University of Leeds (unknown). [Lymph nodes: The Histology Guide](https://histology.leeds.ac.uk/home/lymphoid/lymphnodes/). The Histology Guide. DOI: not_applicable. Supporting location/access: [source ANATOMY](SOURCES.md#anatomy).

