# Representation taxonomy

Status: unranked planning scaffold. No relevant papers have been collected or verified. Mathematical forms below are notation conventions for organizing later study, not assertions that every method in a family uses the same formulation. Biological interpretations are questions to validate; advantages, disadvantages, suitable inputs/models, assumptions, and failure modes are **candidate assessment prompts**, not established comparative findings. None is a recommendation for the six uninspected datasets.

Notation: n = observations; p = features; d = latent dimensions; m indexes a view where applicable. Shapes, units, constraints, and observation identities must be restated in each actual method record. Families overlap and may appear at different pipeline stages.

Phase 2A mathematical clarification: stored rows are x_i^T with x_i a p-dimensional column vector. A map W of shape d×p acts as z_i=Wx_i, while the full observation matrix maps as Z=XW^T. If a family below writes Z=XW instead, its W has shape p×d. For X≈UV^T, factors have shapes n×d and p×d; factors are not generally identifiable without constraints. Full SVD factors have shapes n×n, n×p and p×p; thin SVD uses h=min(n,p). A positive-semidefinite kernel must satisfy its Gram-matrix condition; an arbitrary similarity need not qualify. These clarifications do not select, rank or begin a family review. See [mathematical foundations](05_methods/01_mathematical_foundations/CONCEPT_MAP.md).

Permanent evaluation principle: numerical compactness, reconstruction, label agreement and biological validity are separate questions. All future family assessments must report computational, statistical and biological evidence, with label provenance and sampling units. [Evaluation distinction](05_methods/01_mathematical_foundations/36_BIOLOGICAL_VS_COMPUTATIONAL_EVALUATION.md).

## RF01. Raw feature spaces

- **What is represented:** Measured observation-feature entries.
- **Mathematical form:** `X ∈ R^(n×p), with original units and provenance`.
- **Biological interpretation to verify:** Direct link to named measured features.
- **Potential advantages to assess:** Feature traceability.
- **Potential disadvantages to assess:** Dimension, scale, and measurement noise.
- **Suitable modalities to verify:** RNA, ADT/protein, ATAC, other verified tables.
- **Suitable models to verify:** Statistical estimators, classical ML, neural models.
- **Assumptions to check:** Rows and columns have verified meaning; raw versus processed state is known.
- **Common failure modes to investigate:** Confusing transformed values with counts; batch or depth dominating the analysis. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF02. PCA latent spaces

- **What is represented:** Linear coordinates and feature loadings.
- **Mathematical form:** `Z = X_centered W, W ∈ R^(p×d)`.
- **Biological interpretation to verify:** Interpretation through documented loadings.
- **Potential advantages to assess:** Compact linear coordinates.
- **Potential disadvantages to assess:** Potential loss of information outside retained components.
- **Suitable modalities to verify:** Numeric feature matrices after justified preprocessing.
- **Suitable models to verify:** Clustering, regression, other embedding consumers.
- **Assumptions to check:** Centering, scaling, rank, and fitting scope are specified.
- **Common failure modes to investigate:** Interpreting variance as biological importance; fitting on held-out data. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF03. CCA/PLS latent spaces

- **What is represented:** Coordinates relating two feature views.
- **Mathematical form:** `Z₁ = X₁W₁; Z₂ = X₂W₂; objective differs by method`.
- **Biological interpretation to verify:** Cross-view relationships to investigate.
- **Potential advantages to assess:** Explicit view-specific projections.
- **Potential disadvantages to assess:** Dependence on correspondence and chosen cross-view objective.
- **Suitable modalities to verify:** Paired or explicitly aligned modality tables.
- **Suitable models to verify:** Multiview estimators and downstream predictors.
- **Assumptions to check:** Observation correspondences and method-specific constraints are justified.
- **Common failure modes to investigate:** Incorrect row pairing; conflating correlation and covariance objectives. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF04. General matrix factorization

- **What is represented:** Factors approximating a feature matrix.
- **Mathematical form:** `X ≈ UVᵀ`.
- **Biological interpretation to verify:** Candidate feature programs and observation scores.
- **Potential advantages to assess:** Structured decomposition.
- **Potential disadvantages to assess:** Factor non-uniqueness and rank dependence.
- **Suitable modalities to verify:** Numeric biological matrices.
- **Suitable models to verify:** Factorization procedures, downstream models.
- **Assumptions to check:** Objective, constraints, rank, and factor scaling are explicit.
- **Common failure modes to investigate:** Assigning biological meaning to arbitrary rotations or factor permutations. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF05. NMF/iNMF/MOFA-style representations

- **What is represented:** Constrained or multiview factors; formulations must remain distinct.
- **Mathematical form:** `Illustrative factorization X^(m) ≈ Z^(m)W^(m)ᵀ + E^(m); sharing and distributions are method-specific`.
- **Biological interpretation to verify:** Candidate shared/private programs.
- **Potential advantages to assess:** Explicit study of feature factors and view structure.
- **Potential disadvantages to assess:** Dependence on constraints, likelihoods, and sharing choices.
- **Suitable modalities to verify:** Compatible single-view or multiview tables, verified per method.
- **Suitable models to verify:** Specific verified factor models and downstream consumers.
- **Assumptions to check:** Do not treat these names as one objective; verify positivity and likelihood requirements.
- **Common failure modes to investigate:** Applying incompatible input transformations; forcing shared structure; conflating methods. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF06. Probabilistic latent-variable representations

- **What is represented:** Latent distributions or posterior summaries.
- **Mathematical form:** `p(X,Z); p(Z|X) or an approximation q(Z|X)`.
- **Biological interpretation to verify:** Latent quantities and their model-dependent uncertainty.
- **Potential advantages to assess:** Distributional rather than only point representation.
- **Potential disadvantages to assess:** Sensitivity to likelihood, prior, and inference approximation.
- **Suitable modalities to verify:** Tables with a defensible measurement model.
- **Suitable models to verify:** Probabilistic inference and generative models.
- **Assumptions to check:** Likelihood, priors, identifiability, and approximation are specified.
- **Common failure modes to investigate:** Treating posterior uncertainty as calibrated without checking. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF07. Autoencoder embeddings

- **What is represented:** Encoded observation coordinates.
- **Mathematical form:** `Z = fθ(X); reconstructed X̂ = gφ(Z)`.
- **Biological interpretation to verify:** Learned features requiring separate biological interpretation.
- **Potential advantages to assess:** Flexible encoding to assess.
- **Potential disadvantages to assess:** Training and decoder choices influence what is retained.
- **Suitable modalities to verify:** Numeric modality tables with defined targets.
- **Suitable models to verify:** Encoder/decoder models and downstream predictors.
- **Assumptions to check:** Input transformation and reconstruction target are appropriate.
- **Common failure modes to investigate:** Reconstructing technical variation; assuming reconstruction implies biological validity. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF08. VAE representations

- **What is represented:** Posterior parameters or sampled latent coordinates.
- **Mathematical form:** `qφ(Z|X), pθ(X|Z), and a specified prior p(Z)`.
- **Biological interpretation to verify:** Model-dependent latent factors and uncertainty.
- **Potential advantages to assess:** Joint study of latent representation and generation.
- **Potential disadvantages to assess:** Approximate inference and objective choices.
- **Suitable modalities to verify:** Modalities matched to verified likelihoods.
- **Suitable models to verify:** Variational generative models.
- **Assumptions to check:** Distinguish posterior mean, variance, and latent samples.
- **Common failure modes to investigate:** Ignoring posterior collapse or likelihood mismatch; conflating latent summaries. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF09. Multimodal latent spaces

- **What is represented:** Joint/shared and optionally private modality coordinates.
- **Mathematical form:** `Z_shared and Z_private^(m), with modality-specific maps`.
- **Biological interpretation to verify:** Candidate common and modality-specific signals.
- **Potential advantages to assess:** Explicit integration of views.
- **Potential disadvantages to assess:** Alignment and missing-view complexity.
- **Suitable modalities to verify:** Paired, partially paired, or unpaired data only as supported.
- **Suitable models to verify:** Multiview, multimodal generative, or discriminative models.
- **Assumptions to check:** Pairing, missingness, and shared/private definitions are documented.
- **Common failure modes to investigate:** Erasing modality-specific biology; aligning unrelated observations. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF10. Contrastive embeddings

- **What is represented:** Coordinates shaped by selected pair relationships.
- **Mathematical form:** `Z = fθ(X), trained with a specified contrastive objective`.
- **Biological interpretation to verify:** Meaning depends on how positive and negative relations are justified.
- **Potential advantages to assess:** Direct study of chosen invariances.
- **Potential disadvantages to assess:** Pair selection and augmentation dependence.
- **Suitable modalities to verify:** Tables with defensible relation/augmentation rules.
- **Suitable models to verify:** Contrastive encoders and embedding consumers.
- **Assumptions to check:** Pair labels, negatives, and augmentations preserve the intended biology.
- **Common failure modes to investigate:** False negatives; removing a biological distinction through augmentation. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF11. Metric-learning embeddings

- **What is represented:** Coordinates or distances optimized for a relationship target.
- **Mathematical form:** `Z = fθ(X) or d_M(x,y), with stated constraints on M`.
- **Biological interpretation to verify:** Similarity according to the chosen supervision.
- **Potential advantages to assess:** Task-directed distance construction.
- **Potential disadvantages to assess:** Dependence on labels, constraints, or training relationships.
- **Suitable modalities to verify:** Numeric tables with verified relationship evidence.
- **Suitable models to verify:** Metric learners, retrieval, clustering, classifiers.
- **Assumptions to check:** Distance properties and relationship provenance are explicit.
- **Common failure modes to investigate:** Label leakage; distances that fail outside the training system. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF12. Manifold representations

- **What is represented:** Coordinates or geometry derived from a specified neighborhood model.
- **Mathematical form:** `Z ∈ R^(n×d), with a declared geometry-preservation criterion`.
- **Biological interpretation to verify:** Candidate local/global structure requiring validation.
- **Potential advantages to assess:** Study of nonlinear geometry.
- **Potential disadvantages to assess:** Neighborhood, scale, and out-of-sample choices.
- **Suitable modalities to verify:** Tables with justified feature scaling and distance.
- **Suitable models to verify:** Manifold learners and downstream embedding consumers.
- **Assumptions to check:** Geometry and neighborhood meaning are defensible.
- **Common failure modes to investigate:** Overinterpreting display separation; instability under neighborhood changes. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF13. Kernel representations

- **What is represented:** Pairwise kernel evaluations or implicit features.
- **Mathematical form:** `Kᵢⱼ = k(xᵢ,xⱼ); kernel conditions depend on method`.
- **Biological interpretation to verify:** Similarity under an explicit kernel.
- **Potential advantages to assess:** Nonlinear comparisons through a defined function.
- **Potential disadvantages to assess:** Kernel/scale choice and pairwise storage.
- **Suitable modalities to verify:** Numeric or structured tabular inputs with suitable kernel.
- **Suitable models to verify:** Kernel estimators and spectral methods.
- **Assumptions to check:** Required kernel properties and centering are checked.
- **Common failure modes to investigate:** Invalid kernel assumptions; memory growth; similarity driven by batch. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF14. Optimal-transport representations

- **What is represented:** Couplings or transported features between measures.
- **Mathematical form:** `Π ∈ R₊^(n×m), with specified cost and marginal constraints`.
- **Biological interpretation to verify:** Candidate correspondence between observations or distributions.
- **Potential advantages to assess:** Explicit correspondence and mass allocation.
- **Potential disadvantages to assess:** Cost, regularization, and matching assumptions.
- **Suitable modalities to verify:** Aligned feature spaces or other justified cost constructions.
- **Suitable models to verify:** Transport solvers and downstream models.
- **Assumptions to check:** Mass meaning, balance assumptions, and comparison space are justified.
- **Common failure modes to investigate:** Forcing false matches; treating coupling as confirmed biological correspondence. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF15. Graphs

- **What is represented:** Nodes, edges, and optional attributes.
- **Mathematical form:** `G=(V,E), A ∈ R^(n×n), node features X`.
- **Biological interpretation to verify:** Declared cell, feature, or other biological relations.
- **Potential advantages to assess:** Explicit relational structure.
- **Potential disadvantages to assess:** Construction and sparsification choices.
- **Suitable modalities to verify:** Tables, coordinates, or curated interactions with documented edge meaning.
- **Suitable models to verify:** Graph algorithms and graph neural models.
- **Assumptions to check:** Node identity, edge meaning, direction, weighting, and construction scope are defined.
- **Common failure modes to investigate:** Spurious edges; leakage during graph construction; unjustified neighborhood smoothing. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF16. Heterogeneous graphs

- **What is represented:** Multiple node and relation types.
- **Mathematical form:** `G=(V,E,τ_V,τ_E)`.
- **Biological interpretation to verify:** Typed relations such as observation-feature links, if justified.
- **Potential advantages to assess:** Explicit distinction among relation types.
- **Potential disadvantages to assess:** Schema and relation-specific modeling complexity.
- **Suitable modalities to verify:** Tables and knowledge sources with verified typed identifiers.
- **Suitable models to verify:** Heterogeneous graph/network models.
- **Assumptions to check:** Types, identifier mappings, and relation semantics are verified.
- **Common failure modes to investigate:** Incorrect cross-database mappings; mixing evidence strengths as equivalent edges. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF17. Multiplex/multiview graphs

- **What is represented:** Multiple edge layers over linked entities.
- **Mathematical form:** `{A^(m)} with explicit interlayer mappings`.
- **Biological interpretation to verify:** View-specific relations and their possible integration.
- **Potential advantages to assess:** Retains separate relation layers.
- **Potential disadvantages to assess:** Layer alignment and weighting choices.
- **Suitable modalities to verify:** Multiple modalities or relation sources with known correspondences.
- **Suitable models to verify:** Multilayer network or multiview graph models.
- **Assumptions to check:** Cross-layer node correspondence and edge comparability are specified.
- **Common failure modes to investigate:** Dominant layers; duplicated evidence; inconsistent node alignment. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF18. Hypergraphs

- **What is represented:** Relations joining groups of entities.
- **Mathematical form:** `H ∈ {0,1}^(n×e), or a defined weighted incidence matrix`.
- **Biological interpretation to verify:** Group-level relationships requiring explicit semantics.
- **Potential advantages to assess:** Direct group-incidence representation.
- **Potential disadvantages to assess:** Hyperedge construction and weighting complexity.
- **Suitable modalities to verify:** Tables or biological group annotations with justified membership.
- **Suitable models to verify:** Hypergraph methods and incidence-based models.
- **Assumptions to check:** Hyperedge meaning, size, membership, and construction scope are defined.
- **Common failure modes to investigate:** Arbitrary group formation; redundant memberships; label-derived leakage. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF19. Tensors

- **What is represented:** Values arranged along three or more declared axes.
- **Mathematical form:** `T ∈ R^(n₁×n₂×…×n_k)`.
- **Biological interpretation to verify:** Axis-specific biological structure when compatible.
- **Potential advantages to assess:** Preserves an explicit multi-axis organization.
- **Potential disadvantages to assess:** Incomplete or incompatible axes and storage cost.
- **Suitable modalities to verify:** Tables with verified observation/feature/context correspondences.
- **Suitable models to verify:** Tensor decompositions and tensor-aware models.
- **Assumptions to check:** Axis alignment, units, and missing-entry masks are explicit.
- **Common failure modes to investigate:** Fabricated correspondences; treating unmeasured entries as zeros. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF20. Set representations

- **What is represented:** Collections with a declared order-invariance requirement.
- **Mathematical form:** `Sᵢ = {xᵢ₁,…,xᵢₖ}, with metadata/masks as required`.
- **Biological interpretation to verify:** Groups of measured entities without arbitrary ordering.
- **Potential advantages to assess:** Variable-cardinality collections to assess.
- **Potential disadvantages to assess:** Element identity and aggregation design.
- **Suitable modalities to verify:** Grouped cells/features or other verified collections.
- **Suitable models to verify:** Set-based encoders, pooling models, suitable attention models.
- **Assumptions to check:** Set membership and desired permutation behavior are defined.
- **Common failure modes to investigate:** Accidental ordering dependence; discarding meaningful element identity. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF21. Transformer/token representations

- **What is represented:** Tokens encoding entities, values, modality, or context.
- **Mathematical form:** `Tᵢ ∈ R^(Lᵢ×d), with vocabulary and masks`.
- **Biological interpretation to verify:** Interpretation depends on token identity and value encoding.
- **Potential advantages to assess:** Explicit compositional encoding to assess.
- **Potential disadvantages to assess:** Tokenization, ordering, context-length, and training choices.
- **Suitable modalities to verify:** Tables with a defensible token schema.
- **Suitable models to verify:** Transformers or other token-processing models.
- **Assumptions to check:** Token meanings, order, masking, and pretrained-source provenance are documented.
- **Common failure modes to investigate:** Arbitrary order artifacts; truncation; attention mistaken for causal explanation. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF22. Prototype representations

- **What is represented:** Reference points and observation-to-prototype relations.
- **Mathematical form:** `C ∈ R^(k×d); Rᵢⱼ = similarity(zᵢ,cⱼ) or assignments`.
- **Biological interpretation to verify:** Candidate representative patterns, not automatically cell types.
- **Potential advantages to assess:** Compact reference-based description.
- **Potential disadvantages to assess:** Prototype count and assignment choices.
- **Suitable modalities to verify:** Feature matrices or verified embeddings.
- **Suitable models to verify:** Prototype learners, clustering, metric or classification models.
- **Assumptions to check:** Prototype meaning and fitting scope are specified.
- **Common failure modes to investigate:** Missing rare structure; unstable prototypes; interpreting centroids as actual cells. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF23. Learned similarity structures

- **What is represented:** An estimated affinity or relation object.
- **Mathematical form:** `Sᵢⱼ = sθ(xᵢ,xⱼ), with declared constraints`.
- **Biological interpretation to verify:** Learned relationships requiring independent evaluation.
- **Potential advantages to assess:** Adaptable relation definition.
- **Potential disadvantages to assess:** Supervision and constraint dependence.
- **Suitable modalities to verify:** Tabular views or embeddings with justified learning signals.
- **Suitable models to verify:** Similarity learners, kernel-compatible or graph consumers when valid.
- **Assumptions to check:** Symmetry, positivity, sparsity, and training information are declared.
- **Common failure modes to investigate:** Self-confirming evaluation; treating arbitrary affinity as a valid kernel or distance. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## RF24. Hybrid representations

- **What is represented:** Composition of explicitly named representation objects.
- **Mathematical form:** `R = compose(R₁,…,R_k), with each map specified`.
- **Biological interpretation to verify:** Interpretation of each component and their combination.
- **Potential advantages to assess:** Combines separately justified information sources.
- **Potential disadvantages to assess:** Complexity and attribution across stages.
- **Suitable modalities to verify:** Only modalities supported by the component designs.
- **Suitable models to verify:** Explicit compositions of eligible models.
- **Assumptions to check:** Every component, interface, fit scope, and input source is documented.
- **Common failure modes to investigate:** Uncontrolled comparisons; hidden leakage; unclear source of an observed effect. Frequency and applicability are unverified.
- **Relevant papers:** unknown; populate with verified paper IDs during the later literature phase.

## Future record requirements

Use `representations.csv` for specific documented representation instances, not automatic entries for every family. Assign an immutable ID; record its family IDs, pipeline role, exact construction, modality availability, mathematical definition, assumptions, sources, and evaluation context. Update assessment prompts with evidence and precise citations before treating them as established claims. Do not rank families without a defined task and controlled evidence.
