# Single-cell transformers

Phase 2C · method study · studied_not_fitted · not_reproduced.

The three examples below describe their original publications. Later checkpoints require separate provenance; corpus size is a reported design fact, not a performance ranking.

| Model | Input and pretraining | Representation | Reported task types |
| --- | --- | --- | --- |
| scGPT (Cui et al., 2024) | Gene identities with expression-value encoding; generative/masked expression learning; over 33 million cells | Contextual gene and observation embeddings | Annotation, integration, perturbation prediction |
| Geneformer V1 (Theodoris et al., 2023) | Corpus-scaled gene-rank sequence; masked gene-identity prediction; about 30 million human transcriptomes | Contextual gene vectors and pooled observation vectors | Gene/cell classification and in silico perturbation |
| scFoundation (Hao et al., 2024) | Expression-aware asymmetric transformer-like model; read-depth-related expression recovery; over 50 million human profiles, about 20,000 genes | Gene-context and observation embeddings | Expression enhancement, annotation and predictive tasks |

The publication/design evidence and its access depth are indexed in [SOURCES](SOURCES.md).[^1][^2][^3]

## Five components for each named method

| Method | Architecture | Objective | Biological prior | Downstream model | Evaluation |
| --- | --- | --- | --- | --- | --- |
| scGPT | Transformer with gene/value encodings | Generative/masked expression pretraining and task adaptation | Vocabulary, corpus, measurement encodings | Task-specific head or integration procedure | Task-specific primary-paper studies; no local test |
| Geneformer V1 | Transformer encoder | Masked identity prediction | Corpus scaling, ranked vocabulary | Fine-tuned classifier or perturbation analysis | Held-out task evidence, not general biological understanding |
| scFoundation | Asymmetric encoder/decoder | Read-depth-aware expression recovery | Gene coverage and corpus construction | Task-specific regression/classification | Reported tasks; no project result |

**Project interpretation:** a human RNA corpus does not establish mouse RNA–ATAC compatibility. ADT and spatial context are not guaranteed to be represented by RNA pretraining. Uneven tissue coverage, study overlap and phenotype leakage can affect transfer. A task-specific success cannot establish regulatory causality.

Official repositories: [scGPT](https://github.com/bowang-lab/scGPT), [Geneformer](https://huggingface.co/ctheodoris/Geneformer), [scFoundation](https://github.com/biomap-research/scFoundation). The Geneformer model card currently points to a V2 default trained on about 104 million transcriptomes; that is not the original V1 model. Its original V1 description reports 10M parameters and input length 2,048. scFoundation's paper reports 100M parameters. These numbers are provenance facts, not recommendations.[^3][^4]

No checkpoint was downloaded or executed. Model-card claims of biological understanding remain claims requiring task-specific scientific evidence.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | See model-specific table; architecture varies across the three systems |
| Training objective | See table; generative expression and masked identity differ |
| Biological prior | Corpus and tokenizer assumptions, not verified mechanisms |
| Downstream model | Task-specific heads and analyses |
| Evaluation | Published task evidence; no local benchmark |

## Evidence

[^1]: [SCGPT: original source and access notes](SOURCES.md#scgpt).
[^2]: [GENEFORMER: original source and access notes](SOURCES.md#geneformer).
[^3]: [SCFOUNDATION: original source and access notes](SOURCES.md#scfoundation).
[^4]: [GENEFORMER_CODE: original source and access notes](SOURCES.md#geneformer_code).

