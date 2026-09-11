# 11. Multimodal assays

Fully paired data measure modalities on the same observation, for example ((RNA_i,ADT_i)) or ((RNA_i,ATAC_i)). Partially paired data have missing modality blocks; unpaired data measure different observations; mosaic designs mix modality combinations across samples. A mask (M_{im}\in\{0,1\}) records whether modality (m) exists for observation (i).

Pairing is established by experimental indexing, shared barcodes, or explicit sample design—not by matching row numbers. Spatial modalities can be paired on one section, approximately aligned on serial sections, or independently sampled [S13][S14].

RNA, protein, and accessibility have different units, feature spaces, sensitivity, and noise. Integration later must preserve these distinctions; this phase does not select an algorithm. Biological similarity cannot be judged from one modality when another is missing without stating the observation design.

**Evidence:** [S06], [S09], [S13], [S14].
