# Component terminology

This is an operational naming convention for project records. It is not a literature review. A single algorithm can play different roles; identify the role in each pipeline.

| Stage | What is recorded | Example distinction |
|---|---|---|
| Raw data | Acquired observations and accompanying metadata | Count matrix as acquired; provenance determines whether it is actually raw |
| Preprocessing | Filtering, transformations, alignment, feature selection | Normalized values are derived data, not raw counts |
| Initial representation | Object supplied to a learner | Feature matrix, token collection, graph adjacency plus node features |
| Representation-learning mechanism | Procedure that constructs or learns another representation | PCA fitting, contrastive training, or factorization |
| Model | Parameterized computation used for inference or learning | GCN is a graph model; it is not the adjacency matrix |
| Learned embedding | Output coordinates or latent descriptors | PCA scores or encoder output; distinguish parameters from per-observation coordinates |
| Downstream task | Intended use of a representation/model | Clustering or prediction; KMeans is a clustering algorithm |
| Evaluation | Procedure and criteria for judging task outputs | A defined metric with reference, split, and uncertainty |

Example bookkeeping only: acquired matrix → documented transformation → feature matrix → PCA fitting → fitted projection → component scores → KMeans clustering → predeclared evaluation. This example does not select a baseline. A representation-learning mechanism and its fitted model may describe different aspects of the same stage; record both without inventing an extra transformation. Some pipelines have no learned embedding.

Additional distinctions: cell type versus cell state; observation versus biological sample; sample label versus verified developmental stage; missing value versus observed zero; author-reported finding versus our experimental result; biological interpretation versus causal evidence. Source-backed teaching definitions for biological terms belong in the future curriculum notes.
