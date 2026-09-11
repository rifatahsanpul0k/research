# Representative methods

|Method|Paper/year|Inputs|Spatial?|Architecture/objective|Prior|Output/task|Code/status|
|---|---|---|---|---|---|---|---|
|DCA|Eraslan 2019|RNA|no|count denoising AE|count model|cell z/denoise|theislab/dca; verified_official|
|scVI|Lopez 2018|RNA+batch|no|VAE/ELBO|library/batch|z, DE|scvi-tools; verified_official|
|totalVI|Gayoso 2021|RNA+ADT|no|multimodal VAE|protein background|shared z|scvi-tools; verified_official|
|MultiVI|Ashuach 2023|RNA+ATAC|no|multimodal VAE|modality/depth|shared z|scvi-tools; verified_official|
|Cobolt|Gong 2021|RNA/ATAC|no|hierarchical VAE|count likelihood|shared z|boyinggong/cobolt; author repo|
|MIDAS|primary record|mosaic RNA/ADT/ATAC|no|multimodal generative|shared/private|integrated z|UNKNOWN|
|BABEL|Wu 2021|RNA↔ATAC|no|coupled enc/dec|paired observations|translation|wukevin/babel; author repo|
|scGLUE|Cao & Gao 2022|RNA/ATAC|no|guidance graph encoders|regulatory graph|cell/feature z|gao-lab/GLUE; verified|
|SpatialGlue|Long 2024|spatial multi-omics|yes|spatial GNN/fusion|spatial graph|spot z|code provenance pending|
|SpaMI|Gao 2025|spatial multi-omics|yes|GAE+contrast+attention|spatial graph|spot z|Gaocongqiang/SpaMI; author repo|
|Garfield|2026|single-cell/spatial|yes|VGAE+contrast|molecular/spatial graph|atlas z|UNKNOWN|
|SCIGMA|2026 preprint|spatial multi-omics|yes|uncertainty GNN|views|z+uncertainty|UNKNOWN|
|ARISE|2026|spatial RNA/ADT/ATAC|yes|RNA-anchored GCN/fusion|shared-edge graph|spot z|UNKNOWN|
|scGPT|Cui 2024|gene tokens|no|transformer generative|corpus vocabulary|cell/gene z|bowang-lab/scGPT; author repo|
|Geneformer|Theodoris 2023|ranked gene tokens|no|transformer masked model|corpus/rank|cell z|ctheodoris/Geneformer; author repo|
|Hypergraph NN|Feng 2019|nodes+incidence|optional|hypergraph convolution|hyperedges|node z|implementations vary|
|R-GCN|Schlichtkrull 2018|typed relations|optional|relation-specific GNN|edge types|node z|DGL/PyG libraries|
