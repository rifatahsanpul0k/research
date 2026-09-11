# Paper extraction schema

One immutable `paper_id` (future format `PAP-000001`) per work, with linked publication versions. Store a detailed record under `03_papers/<paper_id>/` and index it in `papers.csv`. No paper has been registered or extracted yet.

For every substantive field, record value, evidence classification, source version and locator, verification status, and unresolved uncertainty. Use `unknown`, not inferred values. Use a table/list when a paper contains multiple datasets, tasks, configurations, or results.

| Field | Required contents |
|---|---|
| paper_id | Immutable identifier; aliases and related versions |
| title | Verified full title |
| authors | Verified authorship |
| year | Publication year; distinguish preprint and journal dates |
| journal | Venue and publication/peer-review status |
| DOI | Verified DOI or unknown |
| paper_url | Canonical article/preprint URL and access date |
| code_url | Official code URL, verification evidence, and codebase ID |
| research_problem | Authors' stated problem; distinguish our framing |
| biological_motivation | Biological rationale with supporting passage |
| modalities | Measured modalities, pairing, observation units, and inputs actually used |
| datasets | Accessions, versions, tissues, organisms, sample structure, and split roles |
| preprocessing | Ordered filters, transformations, normalization, feature selection, and fit scope |
| input_representation | Objects supplied to the method, dimensions, units, and construction |
| representation_learning_method | Mechanism that constructs or learns a representation, if applicable |
| architecture_model | Model components and the role of each |
| mathematical_formulation | Variables, dimensions, equations, constraints, assumptions, and source locators |
| objective_loss | Exact objectives, terms, weights, and optimization direction |
| training_procedure | Optimizer, schedule, stopping, initialization, splits, and selection process |
| hyperparameters | Reported values, search space, selection criteria, defaults, and unreported fields |
| downstream_tasks | Intended prediction, inference, clustering, or other task and target |
| baselines | Names, versions, preprocessing, input availability, and tuning comparability |
| metrics | Definitions, implementation/version, direction, aggregation, and uncertainty |
| results | Author-reported values with dataset/task/configuration/table links; never mix with our runs |
| ablation_studies | Changed factor, controls, measured outcome, and limitations |
| biological_evaluation | Biological references, label origin, independent support, and circularity risks |
| limitations | Separate author-stated limitations from our evidence-backed assessment |
| reproducibility_status | Source access, code verification, environment, execution, and linked reproduction IDs |
| relevance_to_project | Scope fit based on verified inputs/tasks; no novelty inference |
| unresolved_questions | Missing information and next verification actions |

Additional provenance: extractor/date, source type, document checksum if local, supplements inspected, license/access restrictions, corrections, and change history. Detailed results require separate per-comparison rows, including uncertainty and deviations; the root registry remains a discovery index.
