# Enhancers

## A. Biological meaning

Enhancers are DNA elements defined functionally by their ability to increase transcription from a promoter in an appropriate context. They can act at a distance and in either orientation in classical assays. This does not imply that genomic distance, orientation or neighboring DNA never affects their endogenous action.[^SELECT]

## B. Mechanism

An enhancer recruits combinations of TFs and cofactors that can influence promoter activation. Which enhancer functions in which cell depends on available regulators, chromatin and promoter compatibility. Enhancer action and enhancer-promoter proximity are related but distinct processes; their coupling is still an active mechanistic question.[^ENH][^SELECT]

Accessibility and enrichment of H3K27ac or H3K4me1 can help identify candidate enhancer regions. These signals are not equivalent to a functional test. H3K27ac helped distinguish active from inactive/poised enhancer candidates in landmark experiments, but a histone-mark rule is not a universal definition.[^AC]

## C. Relationship to previous concepts

A promoter specifies an initiation region; an enhancer influences its output. Enhancers may be upstream, downstream or within gene-associated sequence, so the nearest gene is not necessarily the target. One element may affect more than one gene, and several elements may influence one gene.[^ENH][^LINK]

The chain below contains separate hypotheses at each arrow:

    ATAC peak
      -> candidate regulatory region
      -> possible target gene
      -> proposed effect on gene expression

## D. Measurement

| Evidence | What it supports | What remains unresolved |
|---|---|---|
| Accessibility or histone enrichment | Candidate regulatory chromatin | Enhancer function and target |
| Reporter assay | Sequence can enhance the tested construct | Endogenous target and native-context necessity |
| Contact measurement | Spatial proximity-related evidence | Regulatory direction and effect |
| Endogenous perturbation plus RNA readout | Effect of intervening at the region in tested conditions | Specificity, mechanism and transfer to other contexts |

Functional validation and prediction are kept separate in enhancer studies.[^ENH][^LINK]

## E. Computational representation

Synthetic relationship records:

| region_id | candidate_gene | evidence_type | value | units | context | status |
|---|---|---|---:|---|---|---|
| E1 | G1 | distance | 5000 | bp | toy-cell-A | hypothesis |
| E1 | G3 | contact_enrichment | 2.1 | assay_ratio | toy-cell-A | observed_contact |
| E1 | G3 | perturbation_RNA_change | -0.7 | log2_fold_change | toy-cell-A | synthetic_effect_example |

All values are invented. A negative change after inhibiting a region is consistent with a positive regulatory contribution under adequate controls; the sign is the perturbation response, not automatically an edge sign. Do not compare 5000 bp, 2.1-fold enrichment and -0.7 log2 fold change as a common confidence scale.

## F. Relevance to our research

Future peak-to-gene links require evidence, context and uncertainty. Spatial proximity of cells is different from proximity of genomic loci within a nucleus. Biological similarity based on candidate enhancers may reflect regulatory potential rather than current RNA output. No preferred computational representation follows from these facts.

## G. Common misconceptions

An ATAC peak is not automatically an enhancer; an enhancer is not automatically linked to its nearest gene; a contact is not automatically causal; activity in a reporter does not verify an endogenous target. A label such as active enhancer must state the assay or functional criterion used.[^ENH][^ENC]

## H. Evidence

[^SELECT]: Yang JH; Hansen AS (2024). [Enhancer selectivity in space and time: from enhancer-promoter interactions to promoter activation](https://www.nature.com/articles/s41580-024-00710-6). Nature Reviews Molecular Cell Biology; review. Locator: Abstract and figure descriptions 1-4.

[^ENH]: Friedman MJ; Wagner T; Lee H; Rosenfeld MG; Oh S (2024). [Enhancer-promoter specificity in gene transcription: molecular mechanisms and disease associations](https://www.nature.com/articles/s12276-024-01233-y). Experimental & Molecular Medicine; review. Locator: Introduction; Identification of enhancer-promoter interactions; Functional validation of enhancers.

[^AC]: Creyghton MP; Cheng AW; Welstead GG; Kooistra T; Carey BW; Steine EJ; Hanna J; Lodato MA; Frampton GM; Sharp PA; Boyer LA; Young RA; Jaenisch R (2010). [Histone H3K27ac separates active from poised enhancers and predicts developmental state](https://pmc.ncbi.nlm.nih.gov/articles/PMC3003124/). Proceedings of the National Academy of Sciences USA; primary_research. Locator: Abstract and H3K27ac/H3K4me1 comparison.

[^LINK]: Fulco CP; Nasser J; Jones TR; Munson G; Bergman DT; Subramanian V; Grossman SR; Anyoha R; Doughty BR; Patwardhan TA; Nguyen TH; Kane M; Perez EM; Durand NC; Lareau CA; Stamenova EK; Aiden EL; Lander ES; Engreitz JM (2019). [Activity-by-contact model of enhancer-promoter regulation from thousands of CRISPR perturbations](https://pmc.ncbi.nlm.nih.gov/articles/PMC6886585/). Nature Genetics; primary_research. Locator: Abstract; CRISPR perturbation evidence and candidate-link motivation.

[^ENC]: ENCODE Project Consortium; Moore JE; Purcaro MJ; Pratt HE; Epstein CB; Shoresh N; Adrian J; Kawli T; Davis CA; et al. (2020). [Expanded encyclopaedias of DNA elements in the human and mouse genomes](https://www.nature.com/articles/s41586-020-2493-4). Nature; database_resource_paper. Locator: Abstract; Figure 2 and candidate CRE registry description.

