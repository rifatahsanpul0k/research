# Future experiment protocol

Status: protocol only. No experiments have been planned in the registry or run. No model, task, metric, split, seed value, or hyperparameter setting is selected by this document.

## Preconditions

Before a future run, establish relevant biology and assay understanding, verify the dataset and official baseline sources, complete the dataset manifest, define a task and evaluation plan, and document the question being tested. Advanced method development follows verified baseline reproduction and comparison.

## Immutable run record

Use a unique immutable ID such as `EXP-YYYYMMDD-0001`, allocated before execution. Never reuse an ID or overwrite outputs. A changed dataset, split, seed, configuration, or code version requires a new run ID; link retries and related runs using `parent_experiment_id` and a comparison-group ID. Record planned, running, completed, failed, cancelled, or blocked status without deleting unsuccessful runs.

| Required field | Contents |
|---|---|
| question_and_evidence | Question ID, rationale, evidence classification, prospective expectation when applicable |
| dataset_version | Dataset ID(s), immutable acquisition manifest, checksums, modality and sample subsets |
| preprocessing_version | Code commit/config hash, ordered transformations, QC, feature mapping/selection, fit scope, artifact checksums |
| split_definition | Unit of independence, train/validation/test IDs, grouping, stratification, leakage checks |
| random_seeds | Seeds for all relevant generators/components and any nondeterministic operations |
| initial_representation | Representation ID, construction, dimensions, units, included modalities/spatial information |
| representation_method | Method ID, objective, fit scope, and learned transformations, or not applicable |
| model | Model/implementation version, component roles, initialization, checkpoint provenance |
| hyperparameters | Exact values, defaults resolved, search space, search budget, selection rule, stopping criteria |
| learned_embedding | Artifact path, dimensions, observation mapping, or not applicable |
| downstream_task | Inputs, target, prediction unit, and evaluation purpose |
| evaluation_metrics | Prospective definitions, implementations/versions, direction, aggregation, uncertainty method |
| runtime | Start/end times and timezone, wall time, stage breakdown, peak memory and accelerator usage when measurable |
| hardware_software_environment | OS, CPU, RAM, accelerator, driver/runtime, language, locked dependencies, code commit and dirty diff |
| saved_artifacts | Full config, manifests, logs, environments, checkpoints, outputs, metrics, and checksums |
| biological_evaluation | Label/source provenance, biological relevance, independent references, circularity assessment |
| reproducibility_requirements | Exact command, environment restoration, data access, repeated-run plan, expected checks |
| outcome_and_deviations | Observed results, failures, protocol deviations, limitations, linked interpretation |

## Evaluation and comparison rules

- Define the task after verifying the data; choose metrics that match it, with biological and technical rationale. Do not select metrics after inspecting test outcomes.
- Fit preprocessing and learned representations only within their permitted data scope. Declare transductive versus inductive use, including any use of held-out coordinates or unlabeled observations.
- Select split units after donor/sample dependencies are known. Record why each held-out unit supports the intended generalization claim; do not treat observations from the same source as automatically independent.
- Use validation data for model selection; preserve test data for the declared final evaluation. Specify repeat counts and uncertainty methods prospectively, respecting the actual independent units.
- Compare eligible baselines under explicit preprocessing, input-access, tuning-budget, task, and resource conditions. Record justified method-specific requirements and deviations.
- Separate evaluations for human lymph node and mouse embryonic brain. Cross-system transfer, if later feasible, needs a separately specified protocol and feature/label mapping.
- Check whether biological references or labels were used to construct features, representations, or training targets; document circular evaluation risks.
- Report failures, uncertainty, runtime/memory, and biological evidence alongside scores. Numerical improvement alone does not establish a mechanism or novelty.

## Future artifact layout

`08_experiments/<experiment_id>/` will contain the run record, resolved config, command, environment lock, split manifest, logs, metrics, and artifact manifest. Large artifacts may use documented external storage with immutable identifiers and checksums. `09_results/` will contain analyses referencing those IDs rather than overwriting run outputs. No run directory is created during bootstrap.

Update `experiments.csv` and `RESEARCH_LOG.md` for each future run. A reproduction claim must name the source result, match or explain deviations from its protocol, and link executable instructions and observed outputs.
