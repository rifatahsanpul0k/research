# Foundation-model concept

Phase 2C · method study · studied_not_fitted · not_reproduced.

A biological foundation model is a large pretrained model intended to transfer to multiple datasets or tasks. Pretraining learns parameters from a corpus; adaptation changes their use or values for a target setting. The term describes an intended reuse pattern, not a guarantee of biological understanding.[^1][^2]

**Zero-shot** use applies a model to a task without fitting task-specific examples in the stated setting. **Few-shot** use adapts with a small specified number of examples. **Fine-tuning** changes some or all pretrained parameters; a frozen encoder with a newly trained classifier is a different adaptation. These labels must state what was fitted and what labels were available.

A pretrained representation \(z=f_{\theta_0}(x)\) and a fine-tuned \(z'=f_{\theta_*}(x)\) may have different geometries. If an embedding changes after adaptation, its interpretation cannot be inherited unchanged from the initial model card.

**Project interpretation:** pretraining observations, donors or near-duplicate studies overlapping a later test set would weaken a transfer claim. Knowledge of a gene vocabulary is not knowledge of a donor's unseen phenotype. Large corpora can overrepresent common tissues and omit a developmental stage or assay. A model may confidently interpolate familiar patterns into an unfamiliar biological setting.

Readiness for later evaluation requires checkpoint-specific provenance, tokenizer and feature coverage, train/test separation, and an explicit task definition. This note does not build an experiment plan or select a foundation model. Larger parameter count is not an inherent superiority claim; attention patterns and token predictions remain computational evidence with biological interpretation still to be established.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Reusable pretrained encoder or generative network |
| Training objective | Pretraining followed by a separately stated adaptation objective |
| Biological prior | Corpus, vocabulary and task assumptions |
| Downstream model | Zero-shot rule, frozen-head model or fine-tuned model |
| Evaluation | Transfer under stated data separation and domain assumptions |

## Evidence

[^1]: [SCGPT: original source and access notes](SOURCES.md#scgpt).
[^2]: [GENEFORMER: original source and access notes](SOURCES.md#geneformer).

