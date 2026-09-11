# Contrastive learning

Phase 2C · method study · studied_not_fitted · not_reproduced.

An encoder \(f_\phi\) maps an input to \(z\in\mathbb R^d\); a projection head can map \(z\) to a loss-specific space \(u\in\mathbb R^k\). The representation retained for downstream use need not be that head's output. Contrastive training increases relative agreement of designated positives compared with designated negatives. SimCLR provides a foundational example, emphasizing augmentations, projection heads and minibatch composition.[^1]

For two views \(t_1(x_i),t_2(x_i)\), the positive relation is constructed by the investigator. Another observation can serve as a negative without a verified “different cell type” label. False negatives arise when biologically related observations are repelled. Conversely, aggressive augmentations may remove the very signal that a later task needs.

Temperature \(\tau>0\) divides similarity scores before a softmax. Smaller values concentrate weight on score differences; it is not a biological temperature or a universal accuracy setting. Larger minibatches can supply more negatives but cost memory and can change the false-negative distribution. Results from visual pretraining do not establish an optimal omics batch size.[^1]

**Project interpretation:** masking an ADT marker and deleting a random image patch are not equivalent interventions. A positive pair should have an explicit preserved property, such as observation identity under a stated measurement perturbation. Paired spots may contain several cell populations, so positive identity does not imply cellular purity. Embeddings can retain an unwanted batch cue if it helps identify positive pairs.

[InfoNCE](15_INFONCE.md) defines one objective; [collapse](55_REPRESENTATION_COLLAPSE.md) explains degenerate agreement. Neither note prescribes augmentations for our datasets.

## Five separate components

| Component | Definition here |
| --- | --- |
| Architecture | Encoder and optional loss-specific projection head |
| Training objective | Positive-relative-to-negative agreement |
| Biological prior | Invariances defined by pair construction; no inherent biological truth |
| Downstream model | Separate classifier, retrieval or clustering on retained representation |
| Evaluation | Task utility and pair validity; not evaluated |

## Evidence

[^1]: [SIMCLR: original source and access notes](SOURCES.md#simclr).

