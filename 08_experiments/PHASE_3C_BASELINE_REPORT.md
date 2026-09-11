# Phase 3C transparent baseline report

## Scope and evidence status

Phase 3C executed 84 `SCIENTIFIC_BASELINE_RUN` configurations on the six local datasets: 28 eligible dataset–baseline combinations, each with KMeans seeds 1729, 2718 and 31415. These runs validate the real-data pipeline from checksum-gated inputs through identity-aware loading, frozen preprocessing, representation generation, common clustering, metrics, provenance and experiment registration.

No complex integration, deep-learning, graph, GNN, tuning, model selection, novelty or disease-association work was performed. The tables report results under the exact frozen configurations; their order is not a ranking.

## Inputs and preprocessing

The complete pre-result specification is in [PHASE_3C_CONFIG_FREEZE.md](PHASE_3C_CONFIG_FREEZE.md). Source H5AD `X` is treated as a processed mirror whose count/fragment semantics remain `UNKNOWN`. No library-size renormalization or observation filtering was applied.

- RNA: `log1p(X)` → stable top-2,000 population-variance features → column population z-scores.
- ADT: frozen per-observation CLR formula → column population z-scores.
- ATAC: TF-IDF → randomized 31-component truncated SVD with seed 0 → remove component 1 → z-score 30 retained LSI components.
- Concatenation: frozen RNA and second-modality blocks, each given equal Frobenius contribution; no learned weighting.
- PCA: frozen RNA representation → 30 randomized components with seed 0 and explicit solver parameters.
- Coordinates: two source coordinate columns standardized within dataset; coordinate units remain `UNKNOWN`.

Annotations were joined by barcode and used only to set the explicitly privileged `K` and to compute agreement metrics. They did not select features or fit representations. Common clustering was scikit-learn 1.9.1 KMeans with `n_init=20`; ARI and NMI measure agreement with the supplied reference annotation. Silhouette measures Euclidean separation under the predicted clustering and does not measure biological correctness.

## Human lymph-node results

Values are mean ± sample SD across the three predeclared KMeans seeds.

| Dataset | Baseline | Modalities | ARI mean ± SD | NMI mean ± SD | Silhouette mean ± SD |
|---|---|---|---:|---:|---:|
| LN_A1 | ADT | ADT | 0.2341 ± 0.0179 | 0.3082 ± 0.0061 | 0.1090 ± 0.0084 |
| LN_A1 | CONCAT | RNA+ADT | 0.2209 ± 0.0272 | 0.3235 ± 0.0144 | 0.0304 ± 0.0086 |
| LN_A1 | PCA | RNA | 0.2319 ± 0.0024 | 0.3402 ± 0.0023 | 0.1510 ± 0.0005 |
| LN_A1 | RNA | RNA | 0.2137 ± 0.0025 | 0.3127 ± 0.0073 | -0.0334 ± 0.0006 |
| LN_A1 | SPACE | spatial coordinates | 0.0673 ± 0.0005 | 0.1518 ± 0.0018 | 0.3535 ± 0.0009 |
| LN_D1 | ADT | ADT | 0.2455 ± 0.0074 | 0.3075 ± 0.0110 | 0.1059 ± 0.0020 |
| LN_D1 | CONCAT | RNA+ADT | 0.2102 ± 0.0359 | 0.3108 ± 0.0154 | 0.0200 ± 0.0090 |
| LN_D1 | PCA | RNA | 0.1461 ± 0.0012 | 0.2508 ± 0.0020 | 0.0918 ± 0.0008 |
| LN_D1 | RNA | RNA | 0.1413 ± 0.0046 | 0.2256 ± 0.0020 | -0.0528 ± 0.0011 |
| LN_D1 | SPACE | spatial coordinates | 0.0515 ± 0.0019 | 0.1478 ± 0.0048 | 0.3401 ± 0.0062 |

These values are configuration-specific reference points. For example, coordinate clustering has positive silhouette but low annotation agreement, showing that geometric compactness and agreement with the supplied tissue-region annotation answer different questions.

## Embryonic mouse-brain results

| Dataset | Baseline | Modalities | ARI mean ± SD | NMI mean ± SD | Silhouette mean ± SD |
|---|---|---|---:|---:|---:|
| MB_E11 | ATAC | ATAC | -0.0024 ± 0.0000 | 0.0077 ± 0.0000 | 0.9239 ± 0.0014 |
| MB_E11 | CONCAT | RNA+ATAC | 0.2249 ± 0.0139 | 0.2090 ± 0.0036 | 0.0354 ± 0.0225 |
| MB_E11 | PCA | RNA | 0.1599 ± 0.0004 | 0.2344 ± 0.0006 | 0.1913 ± 0.0002 |
| MB_E11 | RNA | RNA | 0.1708 ± 0.0061 | 0.2332 ± 0.0036 | 0.0241 ± 0.0055 |
| MB_E11 | SPACE | spatial coordinates | 0.1057 ± 0.0003 | 0.2013 ± 0.0003 | 0.3737 ± 0.0002 |
| MB_E13 | ATAC | ATAC | 0.0030 ± 0.0004 | 0.0188 ± 0.0011 | 0.9496 ± 0.0008 |
| MB_E13 | CONCAT | RNA+ATAC | 0.0562 ± 0.0145 | 0.0991 ± 0.0148 | 0.0741 ± 0.0338 |
| MB_E13 | PCA | RNA | 0.0580 ± 0.0004 | 0.1577 ± 0.0002 | 0.1595 ± 0.0008 |
| MB_E13 | RNA | RNA | 0.0486 ± 0.0061 | 0.1504 ± 0.0134 | 0.0137 ± 0.0030 |
| MB_E13 | SPACE | spatial coordinates | 0.1453 ± 0.0022 | 0.3366 ± 0.0025 | 0.3359 ± 0.0020 |
| MB_E15 | ATAC | ATAC | 0.0851 ± 0.1461 | 0.1205 ± 0.1900 | 0.7200 ± 0.3785 |
| MB_E15 | CONCAT | RNA+ATAC | 0.1098 ± 0.0007 | 0.1581 ± 0.0011 | 0.0559 ± 0.0012 |
| MB_E15 | PCA | RNA | 0.1060 ± 0.0135 | 0.2152 ± 0.0239 | 0.1597 ± 0.0033 |
| MB_E15 | RNA | RNA | 0.0952 ± 0.0178 | 0.2008 ± 0.0206 | 0.0082 ± 0.0043 |
| MB_E15 | SPACE | spatial coordinates | 0.1787 ± 0.0030 | 0.3912 ± 0.0026 | 0.3504 ± 0.0010 |
| MB_E18 | PCA | RNA | 0.1159 ± 0.0024 | 0.2712 ± 0.0085 | 0.1192 ± 0.0019 |
| MB_E18 | RNA | RNA | 0.0773 ± 0.0126 | 0.1974 ± 0.0142 | -0.0179 ± 0.0023 |
| MB_E18 | SPACE | spatial coordinates | 0.1702 ± 0.0004 | 0.3824 ± 0.0023 | 0.3428 ± 0.0031 |

E18 ATAC-only and RNA+ATAC concatenation are `NOT_APPLICABLE_E18_ATAC_UNVERIFIED`; no ATAC statistic or result was produced for E18. Mouse stages were processed independently.

## Quality diagnostics and interpretation limits

All 84 embeddings are finite, noncollapsed, contain every expected observation and have zero duplicate rows. All predicted solutions contain the requested number of nonempty clusters. Twenty-seven runs have at least one singleton cluster and are listed in [PHASE_3C_QC_FLAGS.csv](PHASE_3C_QC_FLAGS.csv).

The strongest warning concerns ATAC-only LSI. E11 and E13 KMeans runs assign more than 90% of observations to one cluster while isolating multiple singleton clusters. Their high silhouette values therefore describe this imbalanced geometric partition and must not be interpreted as biological correctness. E15 ATAC is also highly seed-sensitive: ARI and silhouette sample SDs are 0.1461 and 0.3785. The frozen runs are retained as evidence of a pipeline/data-representation issue; no post-result parameter adjustment was made.

The reference annotations have incomplete biological provenance and are not absolute truth. A spot or capture location may contain mixtures. Similar metric values do not establish biological equivalence, and metric differences do not establish causal or mechanistic explanations.

## Reproducibility and artifacts

- Individual canonical values: [PHASE_3C_BASELINE_RESULTS.csv](PHASE_3C_BASELINE_RESULTS.csv)
- Generated three-seed summaries: [PHASE_3C_BASELINE_AGGREGATES.csv](PHASE_3C_BASELINE_AGGREGATES.csv)
- Executed/applicability matrix: [PHASE_3C_DATASET_BASELINE_STATUS.csv](PHASE_3C_DATASET_BASELINE_STATUS.csv)
- Source checks before/after: [PHASE_3C_INPUT_PREFLIGHT.json](PHASE_3C_INPUT_PREFLIGHT.json), [PHASE_3C_SOURCE_POSTCHECK.json](PHASE_3C_SOURCE_POSTCHECK.json)
- Exact repeatability audit: [PHASE_3C_REPEATABILITY.json](PHASE_3C_REPEATABILITY.json)

Recomputation of all 28 seed-1729 dataset–baseline combinations produced bitwise-identical embeddings, identical clusters and zero metric difference. All 17 source files still matched the Phase 1D manifest afterward.

Each experiment directory contains the frozen config, environment, identity map, embedding, clusters, metrics with implementation/version/parameters, validation diagnostics, preprocessing record, provenance, logs, status and artifact manifest. Per-run `runtime_seconds` measures clustering, metric calculation and serialization after a representation shared across the seed series had been built. Shared dataset representation-build timing is recorded by the repeatability audit and is not allocated to individual seed runs; this limits runtime comparisons.

No scientific execution failure occurred. The retained QC flags and runtime-scope correction are documented separately. Phase 3C supports progression to review, but it does not select a Phase 3D method or establish that any representation is generally superior.
