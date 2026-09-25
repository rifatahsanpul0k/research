# Working ASTRA gated spatial DEC

Start with **[ASTRA_working_model.ipynb](ASTRA_working_model.ipynb)**. It runs locally in the project environment or can be uploaded by itself to Colab: the notebook embeds the implementation, configs and tests. Select a GPU for full training, set the dataset directory, and run the cells. Each run writes to a new directory, with separate outputs for every seed.

The user's preferred model is preserved as **[hello.py](hello.py)**. Despite its extension, that file contains notebook JSON, not executable Python. Its contents were unchanged. The implementation in [model.py](model.py) preserves its neural architecture and objective. **No improved biological ARI is claimed**: the original file contains no saved run outputs, and a full GPU benchmark has not been run in this session.

## What to run

From the repository root, using Python 3.11 or a compatible environment:

```bash
python -m pip install -r better_model/requirements.txt
python -m better_model.run --smoke
python -m better_model.run --config better_model/configs/reference.json --preflight
python -m better_model.run --config better_model/configs/reference.json --data-root 04_datasets
```

This workspace already has the dependencies in `07_models/01_reproduction_environment/.venv-baselines/bin/python`; substitute that executable for `python` to use it. The exact direct dependency versions in `requirements.txt` were observed in this local environment; installation and GPU execution on Colab remain to be verified. Every run captures the complete installed distribution list.

`--smoke` uses 48 synthetic observations and five epochs on CPU. It is an engineering check, not a biological experiment. Full configs declare `COLAB_GPU` and fail clearly if CUDA is unavailable; `--preflight` only checks inputs and configuration, so it works locally. `COLAB_CPU` is available for an intentionally selected remote CPU runtime.

Input layout can be either `DATA_ROOT/DATASET/FILE` or `DATA_ROOT/DATASET/raw/FILE`:

| Modality pair | Required inputs | Annotation column |
|---|---|---|
| RNA + ADT | `adata_RNA.h5ad`, `adata_ADT.h5ad`, optional `annotation.csv` | `manual-anno` |
| RNA + ATAC | `adata_RNA.h5ad`, `adata_ATAC.h5ad`, optional `anno.csv` | `cluster` |

All observations need unique barcodes. Both modalities must have exactly the same barcode set, and the RNA object needs finite `obsm['spatial']` coordinates. The loader reorders the auxiliary modality and annotation table by barcode. If both modalities contain coordinates, they must agree after alignment. No raw input is changed. To run without annotations, omit `annotation_file` and specify `n_clusters` explicitly.

## Reference and candidate

| Config | Purpose |
|---|---|
| [reference.json](configs/reference.json) | A1 and D1, reference graph weights and checkpoint selection, seeds 42/1234/2024 |
| [affinity_candidate.json](configs/affinity_candidate.json) | Same datasets, seeds, architecture and budget; nonnegative cosine weights, decreasing spatial affinities and partition guards |
| [five_datasets_reference.json](configs/five_datasets_reference.json) | A1, D1, E11, E13 and E15 with explicit ADT/ATAC preprocessing |

The default keeps the reference's 512 hidden units, 64-dimensional latent space, 15 neighbors, four reconstruction terms, beta=25, gamma=10, delta=1, DEC weight=1 and spatial-target strength=0.15. Training uses 250 pretraining epochs, restores the selected stage-1 weights, initializes prototypes in those exact latent coordinates, then runs 150 epochs at one tenth of the learning rate. Stage 2 compares DEC labels with KMeans by silhouette, as the reference does.

The candidate is a **hypothesis**, not a verified improvement. The source's raw distance weights and signed cosines remain the reference default so changing them cannot silently invalidate an ARI comparison. Sparse graphs, sparse target propagation, and blocked/checkpointed all-pairs spatial loss reduce memory without replacing the loss with sampled negatives. Pairwise loss time remains quadratic. `silhouette_sample_size` and `evaluate_every` can reduce evaluation cost, but change the selection protocol and must be recorded as separate experiments.

A1 K=10 and D1 K=11 reproduce the original annotation cardinality, including D1's `Exclude` category. The five-dataset config adds E11 K=8, E13 K=12 and E15 K=12. These are **reference-assisted K values**, not label-free cluster-number estimates. Missing labels are excluded from evaluation. To exclude D1's `Exclude` class, set `excluded_labels: ["Exclude"]` in **both** compared configs; changing K from 11 to 10 is a separate protocol change. E18 remains gated until a verified complete ATAC file and its expected SHA-256 are supplied.

## Saved artifacts and reuse

Each output root contains resolved configs, package versions, code snapshots/checksums, source-file checksums, run status, aggregate metrics, and per-dataset preprocessing parameters and graph edges. Each `DATASET/seed_N/` contains:

- `model.pt`: selected model parameters, model configuration, selected labels and checkpoint/bridge metadata.
- `result.h5ad`: selected embedding, both gate matrices, labels, observed log-normalized RNA in `X`, and scaled RNA inputs/reconstructions in separately named layers.
- `assignments.csv`, `baseline_assignments.csv`, `metrics.json`, `selection.json`, `history.jsonl`.

```python
from better_model.training import load_checkpoint
model, metadata = load_checkpoint("RUN/DATASET/seed_42/model.pt", device="cpu")
# Reuse the same paired data, preprocessing and saved graph for reconstruction.
# metadata['selected_labels'] is the actual selected partition (KMeans or DEC).
```

This is a transductive graph model: loading a checkpoint alone is not a validated predictor for a new donor. The `reconstructed_scaled_rna` layer is standardized model output, not raw counts or an appropriate input to the original automatic marker test. `X` retains observed log-normalized HVG expression for separate exploratory analysis. Gates are internal weights, not causal modality contributions.

## Comparing ARI

Run both configs with the same source files, annotation policy, K and seeds, then:

```bash
python -m better_model.compare REFERENCE_RUN CANDIDATE_RUN --output better_model/outputs/comparison
```

The comparison refuses incomplete runs, mismatched source/preprocessing policies, missing seeds and different training/selection budgets. It reports paired per-seed deltas and dataset-level mean/std. It does not automatically promote a model. The included RNA PCA, auxiliary PCA, equal-block concatenation and coordinate-only baselines are diagnostic controls under this pipeline, not claimed reproductions of the older Phase 3C benchmark.

Full model superiority requires the user's original ARI records plus matched full runs. Do not use test ARI to select epochs. For later tuning, designate a development sample before inspecting new outcomes, freeze the chosen recipe, and report the other sample separately; A1/D1 donor independence has not been established here. Seed variation is optimization variability, not uncertainty across biological replicates.

## Validation and analysis

```bash
python -m unittest discover -s better_model/tests -v
python better_model/build_notebook.py
```

Rebuild the portable notebook after editing any module or config. Tests cover original architecture/loss agreement, sparse-vs-dense loss values and gradients, preprocessing, barcode pairing, graph edge cases, both training stages, deterministic CPU repeats, checkpoint reload, candidate guards and per-seed persistence. See [validation/tests.log](validation/tests.log), [validation/local_checks.json](validation/local_checks.json), and [CODEBASE_AUDIT.md](CODEBASE_AUDIT.md) for actual evidence and remaining limits.
