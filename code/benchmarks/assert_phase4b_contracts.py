"""Automated preflight contract assertion suite for Phase 4B (v2.1.0).

Verifies all frozen methodological contracts:
1. Exact barcode alignment across modalities, annotations, coordinates
2. K_reference and evaluation population definitions (including D1 Exclude contract)
3. Raw count layer contracts for scvi models
4. ADT dimensionality and frozen feature lists
5. KMeans n_init == 20
6. Model hyperparameters (SpatialGlue k and epochs, totalVI/MultiVI max_epochs)
7. Global seed constants (silhouette seed == 1729, permutation seed == 1729)
8. Permutation semantics helper (preserves obs_names identically and permutes measurements)
9. MultiVI and totalVI modality pairing alignment assertions
"""

from pathlib import Path
import sys
import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp
from sklearn.cluster import KMeans

ROOT = Path(__file__).resolve().parent.parent.parent
RAW = ROOT / "04_datasets"
FEAT = ROOT / "08_experiments/phase4b_diagnostics/artifacts/features"
PREFLIGHT = ROOT / "08_experiments/phase4b_diagnostics/PHASE_4B_PREFLIGHT_CONTRACT.csv"

datasets = [
    ("LN_A1", RAW / "10x_human_lymph_node_A1/raw", "adata_ADT.h5ad", "annotation.csv", "Barcode", "manual-anno", None),
    ("LN_D1", RAW / "10x_human_lymph_node_D1/raw", "adata_ADT.h5ad", "annotation.csv", "barcode", "manual-anno", "Exclude"),
    ("MB_E11", RAW / "Mouse_Brain_E11_S1/raw", "adata_ATAC.h5ad", "anno.csv", "barcode", "cluster", None),
    ("MB_E13", RAW / "Mouse_Brain_E13_S1/raw", "adata_ATAC.h5ad", "anno.csv", "barcode", "cluster", None),
    ("MB_E15", RAW / "Mouse_Brain_E15_S1/raw", "adata_ATAC.h5ad", "anno.csv", "barcode", "cluster", None),
]

print("=== Running Automated Phase 4B Preflight Assertions (v2.1.0) ===")

# --- 1. Verify Preflight Contract Table Integrity ---
pref_df = pd.read_csv(PREFLIGHT)
assert "kmeans_n_init" in pref_df.columns, "kmeans_n_init missing from preflight contract table"
assert (pref_df["kmeans_n_init"] == 20).all(), "kmeans_n_init must be 20 for all entries in preflight table"
assert (pref_df["silhouette_sampling_seed"] == 1729).all(), "silhouette_sampling_seed must be 1729"
assert (pref_df["permutation_seed"] == 1729).all(), "permutation_seed must be 1729"

# Check SpatialGlue hyperparameter contracts in preflight table
sg_human = pref_df[(pref_df["method"] == "SpatialGlue") & (pref_df["dataset"].isin(["LN_A1", "LN_D1"]))]
assert (sg_human["spatial_k"] == "3").all() or (sg_human["spatial_k"] == 3).all(), "SpatialGlue human spatial_k != 3"
assert (sg_human["epochs"] == "600").all() or (sg_human["epochs"] == 600).all(), "SpatialGlue human epochs != 600"

sg_mouse = pref_df[(pref_df["method"] == "SpatialGlue") & (pref_df["dataset"].isin(["MB_E11", "MB_E13", "MB_E15"]))]
assert (sg_mouse["spatial_k"] == "6").all() or (sg_mouse["spatial_k"] == 6).all(), "SpatialGlue mouse spatial_k != 6"
assert (sg_mouse["epochs"] == "1600").all() or (sg_mouse["epochs"] == 1600).all(), "SpatialGlue mouse epochs != 1600"

# Check deep non-spatial model contracts
tot_rows = pref_df[pref_df["method"] == "totalVI"]
assert (tot_rows["epochs"] == "200").all() or (tot_rows["epochs"] == 200).all(), "totalVI max_epochs != 200"

mvi_rows = pref_df[pref_df["method"] == "MultiVI"]
assert (mvi_rows["epochs"] == "200").all() or (mvi_rows["epochs"] == 200).all(), "MultiVI max_epochs != 200"

print(">> Preflight contract table parameters verified.")

# --- 2. Verify Datasets, Annotations, and Counts ---
for d_name, raw_dir, m2_file, anno_file, bc_col, label_col, excl in datasets:
    adata_rna = ad.read_h5ad(raw_dir / "adata_RNA.h5ad")
    adata_m2 = ad.read_h5ad(raw_dir / m2_file)
    anno_df = pd.read_csv(raw_dir / anno_file)
    coords = adata_rna.obsm["spatial"] if "spatial" in adata_rna.obsm else adata_rna.obs[["x", "y"]].values
    coords = np.asarray(coords, dtype=np.float64)
    labels = anno_df[label_col].values

    # Observation counts
    assert len(adata_rna) == len(adata_m2), f"{d_name}: RNA vs M2 length mismatch"
    assert len(adata_rna) == len(anno_df), f"{d_name}: RNA vs annotation length mismatch"
    assert len(adata_rna) == len(coords), f"{d_name}: RNA vs coords length mismatch"
    assert np.all(np.isfinite(coords)), f"{d_name}: coords contain non-finite values"

    # Barcode match
    assert adata_rna.obs_names.tolist() == adata_m2.obs_names.tolist(), f"{d_name}: RNA vs M2 barcode mismatch"
    assert adata_rna.obs_names.tolist() == anno_df[bc_col].tolist(), f"{d_name}: RNA vs anno barcode mismatch"

    # K_reference and evaluation population
    if excl:
        eval_mask = labels != excl
        eval_labels = labels[eval_mask]
        assert np.sum(~eval_mask) == 10, f"{d_name}: Expected 10 Exclude spots, got {np.sum(~eval_mask)}"
        k_ref = len(np.unique(eval_labels))
        assert k_ref == 10, f"{d_name}: Expected Primary K_ref=10, got {k_ref}"
        k_sens = len(np.unique(labels))
        assert k_sens == 11, f"{d_name}: Expected Sensitivity K_ref=11, got {k_sens}"
    else:
        eval_labels = labels
        k_ref = len(np.unique(eval_labels))

    if d_name == "LN_A1":
        assert k_ref == 10, f"{d_name}: Expected K_ref=10, got {k_ref}"
    elif d_name == "MB_E11":
        assert k_ref == 8, f"{d_name}: Expected K_ref=8, got {k_ref}"
    elif d_name in ["MB_E13", "MB_E15"]:
        assert k_ref == 12, f"{d_name}: Expected K_ref=12, got {k_ref}"

    # Raw count contracts for scvi models
    rna_data = adata_rna.X.data if sp.issparse(adata_rna.X) else adata_rna.X
    assert np.all(rna_data == np.floor(rna_data)), f"{d_name}: RNA counts not integer"
    assert rna_data.min() >= 0, f"{d_name}: RNA contains negative values"

    if d_name in ["LN_A1", "LN_D1"]:
        adt_data = adata_m2.X.data if sp.issparse(adata_m2.X) else adata_m2.X
        assert np.all(adt_data == np.floor(adt_data)), f"{d_name}: ADT counts not integer"
        assert adata_m2.shape[1] == 31, f"{d_name}: ADT shape expected 31 features, got {adata_m2.shape[1]}"

        # Frozen feature lists
        rna_f = (FEAT / f"{d_name}_rna_features.txt").read_text().strip().split("\n")
        adt_f = (FEAT / f"{d_name}_adt_features.txt").read_text().strip().split("\n")
        assert len(rna_f) == 2000, f"{d_name}: Frozen RNA features != 2000"
        assert len(rna_f) == len(set(rna_f)), f"{d_name}: Frozen RNA features contain duplicates"
        assert len(adt_f) == 31, f"{d_name}: Frozen ADT features != 31"
        assert len(adt_f) == len(set(adt_f)), f"{d_name}: Frozen ADT features contain duplicates"
    else:
        atac_data = adata_m2.X.data if sp.issparse(adata_m2.X) else adata_m2.X
        assert np.all(atac_data == np.floor(atac_data)), f"{d_name}: ATAC counts not integer"

        # Frozen feature lists
        rna_f = (FEAT / f"{d_name}_rna_features.txt").read_text().strip().split("\n")
        mvi_f = (FEAT / f"{d_name}_multivi_atac_features.txt").read_text().strip().split("\n")
        mofa_f = (FEAT / f"{d_name}_mofa_atac_features.txt").read_text().strip().split("\n")
        assert len(rna_f) == 2000, f"{d_name}: Frozen RNA features != 2000"
        assert len(mvi_f) <= 20000, f"{d_name}: MultiVI ATAC features > 20000"
        assert len(mofa_f) == 2000, f"{d_name}: MOFA+ ATAC features != 2000"

    print(f"[{d_name}] Dataset alignments, counts, and frozen features verified.")

# --- 3. Verify Permutation Semantics Helper ---
sys.path.insert(0, str(ROOT / "code/benchmarks"))
from run_phase4b_benchmark import permute_measurements_keep_obs, KMEANS_N_INIT

assert KMEANS_N_INIT == 20, f"KMEANS_N_INIT in runner must be 20, got {KMEANS_N_INIT}"

# Test permutation helper on a synthetic test AnnData
n_spots, n_vars = 50, 10
orig_x = np.arange(n_spots * n_vars, dtype=np.float32).reshape(n_spots, n_vars)
test_obs = [f"spot_{i}" for i in range(n_spots)]
test_ad = ad.AnnData(X=orig_x.copy(), obs=pd.DataFrame(index=test_obs))
perm = np.random.RandomState(42).permutation(n_spots)

perm_ad = permute_measurements_keep_obs(test_ad, perm)
assert perm_ad.obs_names.equals(test_ad.obs_names), "permute_measurements_keep_obs modified obs_names!"
assert np.allclose(perm_ad.X, orig_x[perm]), "permute_measurements_keep_obs failed to permute .X correctly!"
assert not np.allclose(perm_ad.X, orig_x), "Permuted matrix is identical to unpermuted matrix!"
print(">> Permutation semantics helper verified successfully.")

print("\n>>> ALL PREFLIGHT ASSERTIONS PASSED (100% VALIDATED) <<<")
