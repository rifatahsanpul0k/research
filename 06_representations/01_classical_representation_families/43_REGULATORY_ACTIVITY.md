# Inferred regulatory activity

Phase 2B · conceptual study; no project-data fitting or performance ranking.

## Three distinct inference paths

An RNA table X:n×p can be mapped to regulator scores A:n×r using a specified target relationship and scoring rule. A peak-accessibility table U:n×q can instead be mapped to motif/annotation scores through peak membership. These outputs infer different quantities; a common “activity” name does not make them comparable measurements.

| Representative approach | Mechanism studied | What the score supports |
|---|---|---|
| SCENIC | Infer coexpression relationships, use motif information to refine candidate regulons, then assess their activity using AUCell rankings | Expression support for an inferred regulator-target program |
| chromVAR | Aggregate accessibility over peaks sharing a motif/annotation and compare deviations using bias-matched background information | TF-associated accessibility variation, not direct TF binding |
| Pathway scoring | Summarize member-gene values or ranks | A method-dependent expression/annotation summary |

The original SCENIC source and official workflow support the first pipeline; chromVAR's paper and official code distinguish motif-associated accessibility from expression.[^1][^2] These are literature mechanisms only: no gene regulatory network is constructed.

## Why expression is not activity

A TF's own RNA amount, its protein abundance, DNA binding and downstream target response are different biological quantities. A motif may be recognized by related TFs, so accessibility around that motif need not uniquely identify the active factor. Correlation between target expression and a regulator does not establish causation; motif support refines an inference but does not replace experimental validation.

For the mouse stages, different ATAC peak sets require compatible annotation and background definitions before motif scores could be compared. Missing E18 ATAC cannot yield a measured chromVAR result. For spots, inferred activities may aggregate multiple cells. No regulator-specific interpretation is made from toy coordinates.

Costs include feature-to-regulon/peak mapping and score calculation; SCENIC also includes a separate network inference stage, while chromVAR uses background sampling. Output n×r storage can be compact but hides input residuals and prior uncertainty. Code repositories are verified as official; no model, motif database or prior payload is installed or run.

## Evidence

[^1]: Aibar S; González-Blas CB; Moerman T; Huynh-Thu VA; Imrichova H; Hulselmans G; Rambow F; Marine JC; Geurts P; Aerts J; van den Oord J; Atak ZK; Wouters J; Aerts S (2017). [SCENIC: single-cell regulatory network inference and clustering](https://www.nature.com/articles/nmeth.4463). See [access record](SOURCES.md#scenic).
[^2]: Schep AN; Wu B; Buenrostro JD; Greenleaf WJ (2017). [chromVAR: inferring transcription-factor-associated accessibility from single-cell epigenomic data](https://pubmed.ncbi.nlm.nih.gov/28825706/). See [access record](SOURCES.md#chromvar).
