# Method taxonomy

Status: organizational scaffold only; no literature reviewed, implementations verified, or methods ranked. Categories overlap. Examples are vocabulary anchors, not baseline selections or claims of suitability for the linked datasets.

Distinguish a method family from its input object, learned output, model role, and task. Populate study records under `05_methods/` and add `methods.csv` entries only when a specific method is identified and documented.

| Family | Role to document | Illustrative vocabulary / object to distinguish |
|---|---|---|
| Statistical methods | Estimation, transformation, testing, or prediction | Regression and statistical estimators; specify which stage uses them |
| Dimensionality reduction | Construct a lower-dimensional representation | PCA/CCA/PLS; record fitting, projections, and output scores separately |
| Matrix factorization | Decompose matrices into factors | NMF/iNMF/MOFA-style vocabulary; verify the specific formulation later |
| Clustering | Assign groups or estimate group structure | KMeans; cluster assignments are a task output, not an adjacency matrix |
| Probabilistic models | Specify distributions and infer parameters/latent variables | Latent-variable and mixture formulations |
| Classical ML | Prediction or other task-specific fitting | Linear models, trees, ensembles, support vector models |
| Kernel methods | Operate through a kernel/similarity construction | Kernel function and Gram matrix versus downstream estimator |
| Manifold learning | Construct or learn geometry/coordinates | Neighborhood construction versus coordinate embedding |
| Optimal transport | Optimize a coupling under a specified cost and constraints | Transport solver versus coupling versus transported features |
| Autoencoders | Encode inputs and reconstruct specified targets | Encoder/decoder model versus latent coordinates |
| VAEs | Learn a probabilistic latent-variable formulation | Posterior parameters, sampled latents, and generative model |
| Multimodal generative models | Jointly model specified modalities | Shared/private latent variables and modality likelihoods |
| Contrastive learning | Learn using relationships among examples | Pair construction, objective, encoder, and output embedding |
| Metric learning | Learn a distance, similarity, or embedding | Distance definition versus learned representation |
| Transformers | Process token/set/sequence inputs through a specified model | Tokenization, ordering, attention, and pooled output |
| Graph learning | Learn from or construct graph-structured inputs | Graph construction versus GCN or other graph model |
| Hypergraph learning | Learn from relationships spanning node groups | Incidence object versus learning operator |
| Heterogeneous networks | Model multiple node/edge types | Typed schema versus model; overlaps graph learning |
| Tensor methods | Operate on multi-axis arrays | Tensor construction, decomposition, and factor use |
| Set-based models | Model collections with explicit order behavior | Set construction, element encoder, aggregation |
| Hybrid approaches | Compose two or more mechanisms | Name every stage and justify its role separately |

For each future method record: immutable method ID, family memberships, intended stage/role, mathematical specification, inputs/outputs, biological motivation, assumptions, preprocessing, objective, training/inference procedure, hyperparameters, supported tasks, computational requirements, papers, official codebase/version, limitations, and verification status. Do not inherit a suitability or performance claim from family membership.
