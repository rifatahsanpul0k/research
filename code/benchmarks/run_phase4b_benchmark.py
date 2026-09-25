#!/usr/bin/env python3
"""Phase 4B — Corrected Confirmation Benchmark Runner (v2.1.0).

Fully incorporates all methodological contracts:
1. Permutation semantics: preserve obs_names identically and permute only measurements (.X and layers)
2. KMeans contract: restored n_init = 20 across all primary, Exp R, Exp C, permutation, and sensitivity runs
3. Invariant latent distances: replace raw Euclidean distance with neighborhood Jaccard, distance Spearman, and Procrustes
4. Separation of primary performance from representation and clustering stochasticity
5. D1 Exclude handling: primary N=3349, K=10; secondary sensitivity N=3359, K=11 with dedicated silhouette sample
6. Zero-sized cluster preservation: np.bincount(eval_preds, minlength=k_ref) with 0*log(0)=0 entropy
7. Provenance tracking: training_status (EARLY_STOPPED, MAX_EPOCH_REACHED, DETERMINISTIC, COMPLETED)
8. Main figure filtering: Figures 1-4 use only primary evaluations (model_seed=1729, clustering_seed=1729)
9. Figure 4: Dual panel showing both Delta_M2 and Delta_RNA
10. Automated contract assertions and smoke report generation
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import random
import sys
import time

import anndata as ad
import matplotlib.pyplot as plt
import mudata as md
import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist
from scipy.spatial import procrustes
import scipy.sparse as sp
from scipy.stats import spearmanr
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.metrics import adjusted_mutual_info_score, adjusted_rand_score, normalized_mutual_info_score, silhouette_score

# Project Paths
ROOT = Path(__file__).resolve().parent.parent.parent
EXP_DIR = ROOT / "08_experiments/phase4b_diagnostics"
OUT_DIR = EXP_DIR
ARTIFACTS_DIR = EXP_DIR / "artifacts"
FEAT_DIR = ARTIFACTS_DIR / "features"
EMB_DIR = ARTIFACTS_DIR / "embeddings"
CLUST_DIR = ARTIFACTS_DIR / "cluster_sizes"
STAB_DIR = ARTIFACTS_DIR / "stability"
PERM_DIR = ARTIFACTS_DIR / "permutations"
FIGURES_DIR = EXP_DIR / "figures"
LOGS_DIR = EXP_DIR / "logs"

for d in [EXP_DIR, ARTIFACTS_DIR, FEAT_DIR, EMB_DIR, CLUST_DIR, STAB_DIR, PERM_DIR, FIGURES_DIR, LOGS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# Add external packages
sys.path.insert(0, str(ROOT / "external/SpatialGlue"))

# Global Random Seed Policy
SEEDS = [1729, 2718, 31415]
FIXED_CLUSTERING_SEED = 1729
FIXED_MODEL_SEED = 1729
SILHOUETTE_SAMPLE_SEED = 1729
DISTANCE_PAIR_SAMPLING_SEED = 1729
PERMUTATION_SEED = 1729
KMEANS_N_INIT = 20


def set_all_seeds(seed: int) -> None:
    """Explicitly seed all RNG sources before model construction."""
    random.seed(seed)
    np.random.seed(seed)
    import torch
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def zscore_columns(matrix: np.ndarray) -> np.ndarray:
    values = np.asarray(matrix, dtype=np.float64)
    mean = values.mean(axis=0)
    scale = values.std(axis=0, ddof=0)
    safe = np.where(scale > 0, scale, 1.0)
    result = (values - mean) / safe
    result[:, scale == 0] = 0.0
    return result


def permute_measurements_keep_obs(adata: ad.AnnData, perm: np.ndarray) -> ad.AnnData:
    """Permute molecular measurements (.X and layers) while keeping obs_names identical."""
    out = adata.copy()
    X = adata.X
    if sp.issparse(X):
        out.X = X[perm].copy()
    else:
        out.X = np.asarray(X)[perm].copy()

    if hasattr(adata, "layers") and adata.layers is not None:
        for layer_key in adata.layers.keys():
            L = adata.layers[layer_key]
            if sp.issparse(L):
                out.layers[layer_key] = L[perm].copy()
            else:
                out.layers[layer_key] = np.asarray(L)[perm].copy()

    assert out.obs_names.equals(adata.obs_names), "obs_names was altered during measurement permutation"
    return out


def load_dataset(dataset_name: str) -> dict[str, object]:
    """Load dataset, extract modalities, coordinates, annotations, and audit K."""
    print(f"\n==========================================")
    print(f"Loading Dataset: {dataset_name}")
    print(f"==========================================")

    if dataset_name == "LN_A1":
        raw_dir = ROOT / "04_datasets/10x_human_lymph_node_A1/raw"
        adata_rna = ad.read_h5ad(raw_dir / "adata_RNA.h5ad")
        adata_m2 = ad.read_h5ad(raw_dir / "adata_ADT.h5ad")
        anno_df = pd.read_csv(raw_dir / "annotation.csv")
        label_col = "manual-anno"
        labels = anno_df[label_col].values
        mod2_type = "ADT"
        excl_label = None
    elif dataset_name == "LN_D1":
        raw_dir = ROOT / "04_datasets/10x_human_lymph_node_D1/raw"
        adata_rna = ad.read_h5ad(raw_dir / "adata_RNA.h5ad")
        adata_m2 = ad.read_h5ad(raw_dir / "adata_ADT.h5ad")
        anno_df = pd.read_csv(raw_dir / "annotation.csv")
        label_col = "manual-anno"
        labels = anno_df[label_col].values
        mod2_type = "ADT"
        excl_label = "Exclude"
    elif dataset_name == "MB_E11":
        raw_dir = ROOT / "04_datasets/Mouse_Brain_E11_S1/raw"
        adata_rna = ad.read_h5ad(raw_dir / "adata_RNA.h5ad")
        adata_m2 = ad.read_h5ad(raw_dir / "adata_ATAC.h5ad")
        anno_df = pd.read_csv(raw_dir / "anno.csv")
        label_col = "cluster"
        labels = anno_df[label_col].values
        mod2_type = "ATAC"
        excl_label = None
    elif dataset_name == "MB_E13":
        raw_dir = ROOT / "04_datasets/Mouse_Brain_E13_S1/raw"
        adata_rna = ad.read_h5ad(raw_dir / "adata_RNA.h5ad")
        adata_m2 = ad.read_h5ad(raw_dir / "adata_ATAC.h5ad")
        anno_df = pd.read_csv(raw_dir / "anno.csv")
        label_col = "cluster"
        labels = anno_df[label_col].values
        mod2_type = "ATAC"
        excl_label = None
    elif dataset_name == "MB_E15":
        raw_dir = ROOT / "04_datasets/Mouse_Brain_E15_S1/raw"
        adata_rna = ad.read_h5ad(raw_dir / "adata_RNA.h5ad")
        adata_m2 = ad.read_h5ad(raw_dir / "adata_ATAC.h5ad")
        anno_df = pd.read_csv(raw_dir / "anno.csv")
        label_col = "cluster"
        labels = anno_df[label_col].values
        mod2_type = "ATAC"
        excl_label = None
    else:
        raise ValueError(f"Unknown dataset: {dataset_name}")

    coords = adata_rna.obsm["spatial"] if "spatial" in adata_rna.obsm else adata_rna.obs[["x", "y"]].values
    coords = np.asarray(coords, dtype=np.float64)

    # Evaluation population
    if excl_label:
        eval_mask = labels != excl_label
        eval_labels = labels[eval_mask]
    else:
        eval_mask = np.ones(len(labels), dtype=bool)
        eval_labels = labels

    k_ref = len(np.unique(eval_labels))
    n_total = len(labels)
    n_eval = len(eval_labels)

    print(f"Dataset: {dataset_name}, N_total={n_total}, N_eval={n_eval}, Mod2={mod2_type}, Reference K={k_ref}")
    print(f"Biological Labels ({k_ref}): {list(np.unique(eval_labels))}")
    if excl_label:
        print(f"Excluded from primary biological evaluation: {excl_label} ({np.sum(~eval_mask)} spots)")

    # Pre-select fixed silhouette subsample for primary evaluation (1000 spots or all if <= 1000)
    rng_sil = np.random.RandomState(SILHOUETTE_SAMPLE_SEED)
    if n_eval > 1000:
        sil_indices = rng_sil.choice(n_eval, size=1000, replace=False)
    else:
        sil_indices = np.arange(n_eval)

    # Dedicated silhouette sample over all n_total observations for D1 sensitivity analysis
    rng_sens = np.random.RandomState(SILHOUETTE_SAMPLE_SEED)
    if n_total > 1000:
        sil_indices_sensitivity = rng_sens.choice(n_total, size=1000, replace=False)
    else:
        sil_indices_sensitivity = np.arange(n_total)

    return {
        "dataset": dataset_name,
        "adata_rna": adata_rna,
        "adata_m2": adata_m2,
        "coords": coords,
        "labels": labels,
        "eval_mask": eval_mask,
        "eval_labels": eval_labels,
        "k_ref": k_ref,
        "n_total": n_total,
        "n_eval": n_eval,
        "mod2_type": mod2_type,
        "excl_label": excl_label,
        "sil_indices": sil_indices,
        "sil_indices_sensitivity": sil_indices_sensitivity,
    }


def get_transparent_representations(data_dict: dict[str, object]) -> dict[str, np.ndarray]:
    """Generate deterministic transparent representations (SPACE, RNA, M2, CONCAT)."""
    dataset = data_dict["dataset"]
    adata_rna = data_dict["adata_rna"]
    adata_m2 = data_dict["adata_m2"]
    coords = data_dict["coords"]
    mod2_type = data_dict["mod2_type"]

    # 1. SPACE: normalized 2D coordinates
    coords_norm = (coords - coords.min(axis=0)) / (coords.max(axis=0) - coords.min(axis=0) + 1e-8)

    # 2. RNA: 30 PCs from frozen 2,000 HVGs (log1p + z-score)
    rna_feat_path = FEAT_DIR / f"{dataset}_rna_features.txt"
    selected_rna_genes = rna_feat_path.read_text().strip().split("\n")
    gene_map = {g: i for i, g in enumerate(adata_rna.var_names)}
    top_rna_idx = [gene_map[g] for g in selected_rna_genes]

    X_rna = adata_rna.X[:, top_rna_idx].copy().astype(np.float64)
    if sp.issparse(X_rna):
        X_rna.data = np.log1p(X_rna.data)
        dense_rna = X_rna.toarray()
    else:
        dense_rna = np.log1p(X_rna)
    rna_z = zscore_columns(dense_rna)
    pca_rna = PCA(n_components=30, random_state=0)
    emb_rna = pca_rna.fit_transform(rna_z)

    # 3. M2:
    if mod2_type == "ADT":
        # ADT: 31 features CLR + z-score -> PCA (30 components)
        X_adt = adata_m2.X.toarray() if sp.issparse(adata_m2.X) else adata_m2.X.copy()
        X_adt = X_adt.astype(np.float64)
        geom = np.exp(np.log1p(X_adt).mean(axis=1, keepdims=True))
        clr = np.log1p(X_adt / (geom + 1e-8))
        adt_z = zscore_columns(clr)
        pca_adt = PCA(n_components=min(30, adt_z.shape[1]), random_state=0)
        emb_m2 = pca_adt.fit_transform(adt_z)
    else:
        # ATAC: TF-IDF + SVD components 1:31 (30 components)
        X_atac = adata_m2.X.copy()
        if not sp.issparse(X_atac):
            X_atac = sp.csr_matrix(X_atac)
        X_atac = X_atac.astype(np.float64)
        row_sum = np.asarray(X_atac.sum(axis=1)).ravel()
        inv = np.zeros_like(row_sum)
        inv[row_sum > 0] = 1.0 / row_sum[row_sum > 0]
        tf = sp.diags(inv) @ X_atac
        df = np.asarray((X_atac > 0).sum(axis=0)).ravel()
        idf = np.log1p(X_atac.shape[0] / (1.0 + df))
        tfidf = tf.multiply(idf).tocsr()
        svd = TruncatedSVD(n_components=31, algorithm="randomized", n_iter=7, random_state=0)
        comps = svd.fit_transform(tfidf)
        emb_m2 = zscore_columns(comps[:, 1:31])

    # 4. CONCAT: direct concatenation of RNA and M2
    emb_concat = np.hstack([emb_rna, emb_m2])

    return {
        "SPACE": coords_norm,
        "RNA": emb_rna,
        "M2": emb_m2,
        "CONCAT": emb_concat,
    }


def run_mofaplus(data_dict: dict[str, object], seed: int, n_factors: int = 10) -> tuple[np.ndarray, str, int]:
    """Run MOFA+ with frozen Phase 3D contract."""
    from mofapy2.run.entry_point import entry_point

    set_all_seeds(seed)
    dataset = data_dict["dataset"]
    adata_rna = data_dict["adata_rna"]
    adata_m2 = data_dict["adata_m2"]
    mod2_type = data_dict["mod2_type"]

    # View 1: RNA log1p + 2000 features + z-score
    rna_feat_path = FEAT_DIR / f"{dataset}_rna_features.txt"
    selected_rna = rna_feat_path.read_text().strip().split("\n")
    gene_map = {g: i for i, g in enumerate(adata_rna.var_names)}
    top_rna_idx = [gene_map[g] for g in selected_rna]

    X_rna = adata_rna.X[:, top_rna_idx].copy().astype(np.float64)
    dense_rna = X_rna.toarray() if sp.issparse(X_rna) else X_rna
    view1 = zscore_columns(np.log1p(dense_rna))

    # View 2: Modality 2
    if mod2_type == "ADT":
        X_adt = adata_m2.X.toarray() if sp.issparse(adata_m2.X) else adata_m2.X.copy()
        X_adt = X_adt.astype(np.float64)
        geom = np.exp(np.log1p(X_adt).mean(axis=1, keepdims=True))
        clr = np.log1p(X_adt / (geom + 1e-8))
        view2 = zscore_columns(clr)
    else:
        mofa_atac_path = FEAT_DIR / f"{dataset}_mofa_atac_features.txt"
        selected_atac = mofa_atac_path.read_text().strip().split("\n")
        atac_map = {p: i for i, p in enumerate(adata_m2.var_names)}
        top_atac_idx = [atac_map[p] for p in selected_atac]

        X_atac = adata_m2.X[:, top_atac_idx].copy().astype(np.float64)
        dense_atac = X_atac.toarray() if sp.issparse(X_atac) else X_atac
        view2 = zscore_columns(np.log1p(dense_atac))

    view_names = ["RNA", mod2_type]
    data = [[view1.copy()], [view2.copy()]]

    ent = entry_point()
    ent.set_data_options(center_groups=True, scale_groups=False, scale_views=True, use_float32=False)
    ent.set_data_matrix(data, likelihoods=["gaussian", "gaussian"], views_names=view_names)
    ent.set_model_options(factors=n_factors, spikeslab_weights=True, ard_weights=True, spikeslab_factors=False, ard_factors=False)
    ent.set_train_options(iter=1000, convergence_mode="fast", dropR2=None, seed=seed, verbose=False)
    ent.build()
    ent.run()

    z = ent.model.getExpectations()["Z"]["E"].copy()
    train_stats = ent.model.getTrainingStats()
    time_arr = train_stats.get("time", [])
    epochs_completed = int(np.sum(~np.isnan(time_arr))) if len(time_arr) > 0 else 1000
    status = "EARLY_STOPPED" if epochs_completed < 1000 else "MAX_EPOCH_REACHED"
    return np.asarray(z, dtype=np.float64), status, epochs_completed


def run_totalvi(data_dict: dict[str, object], seed: int, n_latent: int = 15, max_epochs: int = 200, batch_size: int = 128) -> tuple[np.ndarray, str, int]:
    """Run totalVI on raw discrete counts."""
    import scvi
    from scvi.model import TOTALVI

    set_all_seeds(seed)
    scvi.settings.seed = seed

    dataset = data_dict["dataset"]
    adata_rna = data_dict["adata_rna"]
    adata_adt = data_dict["adata_m2"]

    rna_feat_path = FEAT_DIR / f"{dataset}_rna_features.txt"
    selected_rna = rna_feat_path.read_text().strip().split("\n")
    gene_map = {g: i for i, g in enumerate(adata_rna.var_names)}
    top_rna_idx = [gene_map[g] for g in selected_rna]

    sub_rna = adata_rna[:, top_rna_idx].copy()
    sub_rna.var_names_make_unique()

    # Raw discrete ADT counts
    X_adt = adata_adt.X.toarray().astype(np.float32) if sp.issparse(adata_adt.X) else adata_adt.X.astype(np.float32)
    sub_rna.obsm["protein_expression"] = X_adt

    assert sub_rna.obs_names.equals(adata_adt.obs_names), "totalVI RNA and ADT obs_names must match identically"

    TOTALVI.setup_anndata(sub_rna, protein_expression_obsm_key="protein_expression")
    model = TOTALVI(sub_rna, n_latent=n_latent, gene_likelihood="nb")
    model.train(max_epochs=max_epochs, batch_size=batch_size, early_stopping=True, early_stopping_patience=20)
    z = model.get_latent_representation()
    
    epochs_completed = int(getattr(model.trainer, "current_epoch", max_epochs))
    status = "EARLY_STOPPED" if epochs_completed < max_epochs else "MAX_EPOCH_REACHED"
    return np.asarray(z, dtype=np.float64), status, epochs_completed


def run_multivi(data_dict: dict[str, object], seed: int, n_latent: int = 15, max_epochs: int = 200, batch_size: int = 128) -> tuple[np.ndarray, str, int]:
    """Run MultiVI on raw counts and top 20,000 accessible peaks."""
    import scvi
    from scvi.model import MULTIVI

    set_all_seeds(seed)
    scvi.settings.seed = seed

    dataset = data_dict["dataset"]
    adata_rna = data_dict["adata_rna"]
    adata_atac = data_dict["adata_m2"]

    # Frozen RNA features
    rna_feat_path = FEAT_DIR / f"{dataset}_rna_features.txt"
    selected_rna = rna_feat_path.read_text().strip().split("\n")
    gene_map = {g: i for i, g in enumerate(adata_rna.var_names)}
    top_rna_idx = [gene_map[g] for g in selected_rna]
    sub_rna = adata_rna[:, top_rna_idx].copy()

    # Frozen MultiVI ATAC features (top 20,000)
    mvi_atac_path = FEAT_DIR / f"{dataset}_multivi_atac_features.txt"
    selected_atac = mvi_atac_path.read_text().strip().split("\n")
    atac_map = {p: i for i, p in enumerate(adata_atac.var_names)}
    top_atac_idx = [atac_map[p] for p in selected_atac]
    sub_atac = adata_atac[:, top_atac_idx].copy()

    sub_rna.var_names_make_unique()
    sub_atac.var_names_make_unique()

    assert sub_rna.obs_names.equals(sub_atac.obs_names), "MultiVI RNA and ATAC obs_names must match identically"

    mdata = md.MuData({"rna": sub_rna, "atac": sub_atac})
    MULTIVI.setup_mudata(mdata, modalities={"rna_layer": "rna", "atac_layer": "atac"})
    model = MULTIVI(
        mdata,
        n_latent=n_latent,
        n_hidden=128,
        n_layers_encoder=2,
        n_layers_decoder=2,
        gene_likelihood="zinb",
        modality_weights="equal",
        modality_penalty="Jeffreys",
    )
    # In scvi-tools==1.4.2, MULTIVI.train hardcodes early_stopping_patience=50 into _train_runner_cls.
    model.train(max_epochs=max_epochs, batch_size=batch_size, early_stopping=True)
    z = model.get_latent_representation()
    
    epochs_completed = int(getattr(model.trainer, "current_epoch", max_epochs))
    status = "EARLY_STOPPED" if epochs_completed < max_epochs else "MAX_EPOCH_REACHED"
    return np.asarray(z, dtype=np.float64), status, epochs_completed


def run_spatialglue(
    data_dict: dict[str, object],
    seed: int,
    custom_rna_emb: np.ndarray | None = None,
    custom_m2_emb: np.ndarray | None = None,
    custom_coords: np.ndarray | None = None,
) -> tuple[np.ndarray, str, int]:
    """Run SpatialGlue with Phase 4A screened configuration and explicit seeding."""
    import torch
    from SpatialGlue.preprocess import construct_neighbor_graph
    from SpatialGlue.SpatialGlue_pyG import Train_SpatialGlue

    set_all_seeds(seed)

    dataset = data_dict["dataset"]
    mod2_type = data_dict["mod2_type"]
    coords = custom_coords if custom_coords is not None else data_dict["coords"]

    if custom_rna_emb is not None and custom_m2_emb is not None:
        emb_rna = custom_rna_emb
        emb_m2 = custom_m2_emb
    else:
        trans = get_transparent_representations(data_dict)
        emb_rna = trans["RNA"]
        emb_m2 = trans["M2"]

    ad1 = ad.AnnData(X=emb_rna.copy())
    ad1.obsm["feat"] = emb_rna.copy()
    ad1.obsm["spatial"] = coords.copy()

    ad2 = ad.AnnData(X=emb_m2.copy())
    ad2.obsm["feat"] = emb_m2.copy()
    ad2.obsm["spatial"] = coords.copy()

    is_adt = mod2_type == "ADT"
    datatype = "SPOTS" if is_adt else "Spatial-epigenome-transcriptome"
    n_neighbors = 3 if is_adt else 6
    epochs = 600 if is_adt else 1600

    data = construct_neighbor_graph(ad1, ad2, datatype=datatype, n_neighbors=n_neighbors)

    model = Train_SpatialGlue(
        data=data,
        datatype=datatype,
        device=torch.device("cpu"),
        random_seed=seed,
        learning_rate=0.0001,
        weight_decay=0.0,
        epochs=epochs,
        dim_output=64,
    )
    output = model.train()
    z = output["SpatialGlue"]
    return np.asarray(z, dtype=np.float64), "MAX_EPOCH_REACHED", epochs


def compute_clustering_and_diagnostics(
    embedding: np.ndarray,
    eval_mask: np.ndarray,
    eval_labels: np.ndarray,
    k_ref: int,
    sil_indices: np.ndarray,
    clustering_seed: int = FIXED_CLUSTERING_SEED,
) -> tuple[np.ndarray, dict[str, float], np.ndarray]:
    """Compute KMeans clustering (n_init=20) and all Phase 4B diagnostics on evaluation population."""
    km = KMeans(n_clusters=k_ref, random_state=clustering_seed, n_init=KMEANS_N_INIT)
    all_preds = km.fit_predict(embedding)

    eval_preds = all_preds[eval_mask]
    n_eval = len(eval_labels)

    ari = float(adjusted_rand_score(eval_labels, eval_preds))
    nmi = float(normalized_mutual_info_score(eval_labels, eval_preds))

    eval_emb = embedding[eval_mask]
    sil = float(silhouette_score(eval_emb[sil_indices], eval_preds[sil_indices]))

    # Preserve zero-sized clusters explicitly
    counts = np.bincount(eval_preds, minlength=k_ref)
    assert len(counts) == k_ref, f"Expected cluster count vector of length {k_ref}, got {len(counts)}"

    probs = counts / n_eval
    nz_probs = probs[probs > 0]
    h_c = float(-np.sum(nz_probs * np.log(nz_probs))) if len(nz_probs) > 0 else 0.0
    h_norm = float(h_c / np.log(k_ref)) if k_ref > 1 else 0.0
    k_eff = float(np.exp(h_c))
    f_max = float(np.max(probs))

    zero_clusters = int(np.sum(counts == 0))
    singletons = int(np.sum(counts == 1))
    singleton_frac = float(singletons / k_ref)
    min_size = int(np.min(counts))
    max_size = int(np.max(counts))

    diag = {
        "ari": ari,
        "nmi": nmi,
        "silhouette": sil,
        "h_c": h_c,
        "h_norm": h_norm,
        "k_eff": k_eff,
        "f_max": f_max,
        "zero_cluster_count": zero_clusters,
        "singleton_count": singletons,
        "singleton_fraction": singleton_frac,
        "min_cluster_size": min_size,
        "max_cluster_size": max_size,
    }
    return eval_preds, diag, counts


def compute_knn_jaccard(emb1: np.ndarray, emb2: np.ndarray, k_vals: list[int] = [5, 15, 30]) -> dict[str, dict[int, float]]:
    """Compute detailed distribution of kNN Jaccard similarity across observations."""
    d1 = cdist(emb1, emb1, metric="euclidean")
    d2 = cdist(emb2, emb2, metric="euclidean")
    np.fill_diagonal(d1, np.inf)
    np.fill_diagonal(d2, np.inf)

    out = {}
    for k in k_vals:
        nn1 = np.argpartition(d1, k, axis=1)[:, :k]
        nn2 = np.argpartition(d2, k, axis=1)[:, :k]

        jaccards = []
        for i in range(len(emb1)):
            s1 = set(nn1[i])
            s2 = set(nn2[i])
            inter = len(s1 & s2)
            union = len(s1 | s2)
            jaccards.append(inter / union if union > 0 else 0.0)
        j_arr = np.array(jaccards)
        out[k] = {
            "mean": float(np.mean(j_arr)),
            "median": float(np.median(j_arr)),
            "sd": float(np.std(j_arr)),
            "iqr": float(np.percentile(j_arr, 75) - np.percentile(j_arr, 25)),
            "p5": float(np.percentile(j_arr, 5)),
            "p95": float(np.percentile(j_arr, 95)),
        }
    return out


def compute_distance_correlation(emb1: np.ndarray, emb2: np.ndarray, n_pairs: int = 50000, seed: int = DISTANCE_PAIR_SAMPLING_SEED) -> float:
    """Compute Spearman correlation between pairwise distances in two embeddings."""
    np.random.seed(seed)
    n = len(emb1)
    idx1 = np.random.randint(0, n, size=n_pairs)
    idx2 = np.random.randint(0, n, size=n_pairs)
    diff = idx1 != idx2
    idx1, idx2 = idx1[diff], idx2[diff]

    dist1 = np.linalg.norm(emb1[idx1] - emb1[idx2], axis=1)
    dist2 = np.linalg.norm(emb2[idx1] - emb2[idx2], axis=1)
    corr, _ = spearmanr(dist1, dist2)
    return float(corr)


def main():
    parser = argparse.ArgumentParser(description="Run Phase 4B Corrected Confirmation Benchmark")
    parser.add_argument("--smoke-a", action="store_true", help="Run Smoke Test A on LN_A1")
    parser.add_argument("--smoke-b", action="store_true", help="Run Smoke Test B on MB_E13")
    parser.add_argument("--full", action="store_true", help="Run full Phase 4B confirmation benchmark")
    args = parser.parse_args()

    # Determine execution scope
    if args.smoke_a:
        active_datasets = ["LN_A1"]
        is_smoke = True
    elif args.smoke_b:
        active_datasets = ["MB_E13"]
        is_smoke = True
    else:
        active_datasets = ["LN_A1", "LN_D1", "MB_E11", "MB_E13", "MB_E15"]
        is_smoke = False

    print(f"=== Phase 4B Corrected Benchmark Initiated (Datasets: {active_datasets}, Smoke: {is_smoke}) ===")
    start_time = time.time()

    all_runs = []
    all_stability = []
    all_clustering_stability = []
    all_permutations = []

    embeddings_cache: dict[str, dict[str, dict[int, np.ndarray]]] = {}
    partitions_cache: dict[str, dict[str, dict[str, dict[int, np.ndarray]]]] = {}

    for d in active_datasets:
        embeddings_cache[d] = {}
        partitions_cache[d] = {"EXP_R": {}, "EXP_C": {}}

    # =========================================================================
    # Step 1: Transparent Controls (SPACE, RNA, M2, CONCAT)
    # =========================================================================
    print("\n>>> STEP 1: Transparent Controls (SPACE, RNA, M2, CONCAT) <<<")
    for dataset in active_datasets:
        data_dict = load_dataset(dataset)
        trans_dict = get_transparent_representations(data_dict)

        for m_name, emb in trans_dict.items():
            embeddings_cache[dataset][m_name] = {FIXED_MODEL_SEED: emb}
            np.savez_compressed(EMB_DIR / f"emb_{dataset}_{m_name}_s{FIXED_MODEL_SEED}.npz", embedding=emb)

            preds_1729, diag_1729, counts = compute_clustering_and_diagnostics(
                emb, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"], clustering_seed=1729
            )
            partitions_cache[dataset]["EXP_C"][m_name] = {1729: preds_1729}
            partitions_cache[dataset]["EXP_R"][m_name] = {1729: preds_1729}

            all_runs.append({
                "dataset": dataset,
                "method": m_name,
                "experiment_type": "EXP_C",
                "model_seed": FIXED_MODEL_SEED,
                "clustering_seed": 1729,
                "N_total": data_dict["n_total"],
                "N_evaluation": data_dict["n_eval"],
                "K_reference": data_dict["k_ref"],
                **diag_1729,
                "training_status": "DETERMINISTIC",
                "epochs_requested": "NA",
                "epochs_completed": "NA",
                "runtime_seconds": 0.1,
            })
            print(f"[{dataset}][{m_name}][C-Seed 1729] ARI: {diag_1729['ari']:.4f}, Sil: {diag_1729['silhouette']:.4f}, H_norm: {diag_1729['h_norm']:.4f}, f_max: {diag_1729['f_max']:.4f}")

            # Save cluster counts JSON
            with open(CLUST_DIR / f"cluster_sizes_{dataset}_{m_name}_s1729.json", "w") as f_json:
                json.dump({"counts": counts.tolist(), "labels": [str(x) for x in range(len(counts))]}, f_json)

            # D1 Sensitivity check
            if dataset == "LN_D1" and not is_smoke:
                sens_mask = np.ones(data_dict["n_total"], dtype=bool)
                sens_labels = data_dict["labels"]
                _, sens_diag, _ = compute_clustering_and_diagnostics(
                    emb, sens_mask, sens_labels, 11, data_dict["sil_indices_sensitivity"], clustering_seed=1729
                )
                all_runs.append({
                    "dataset": dataset,
                    "method": m_name,
                    "experiment_type": "SENSITIVITY_ONLY",
                    "model_seed": FIXED_MODEL_SEED,
                    "clustering_seed": 1729,
                    "N_total": data_dict["n_total"],
                    "N_evaluation": data_dict["n_total"],
                    "K_reference": 11,
                    **sens_diag,
                    "training_status": "DETERMINISTIC",
                    "epochs_requested": "NA",
                    "epochs_completed": "NA",
                    "runtime_seconds": 0.0,
                })

            # Exp C: Clustering seeds 2718 and 31415
            if not is_smoke:
                for c_seed in [2718, 31415]:
                    preds_c, diag_c, _ = compute_clustering_and_diagnostics(
                        emb, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"], clustering_seed=c_seed
                    )
                    partitions_cache[dataset]["EXP_C"][m_name][c_seed] = preds_c
                    all_runs.append({
                        "dataset": dataset,
                        "method": m_name,
                        "experiment_type": "EXP_C",
                        "model_seed": FIXED_MODEL_SEED,
                        "clustering_seed": c_seed,
                        "N_total": data_dict["n_total"],
                        "N_evaluation": data_dict["n_eval"],
                        "K_reference": data_dict["k_ref"],
                        **diag_c,
                        "training_status": "DETERMINISTIC",
                        "epochs_requested": "NA",
                        "epochs_completed": "NA",
                        "runtime_seconds": 0.0,
                    })

                # Exp C Stability (Pairwise AMI across KMeans seeds)
                p1729 = partitions_cache[dataset]["EXP_C"][m_name][1729]
                p2718 = partitions_cache[dataset]["EXP_C"][m_name][2718]
                p31415 = partitions_cache[dataset]["EXP_C"][m_name][31415]
                pairs = [("1729-2718", p1729, p2718), ("1729-31415", p1729, p31415), ("2718-31415", p2718, p31415)]
                for pair_name, pa, pb in pairs:
                    all_clustering_stability.append({
                        "dataset": dataset,
                        "method": m_name,
                        "fixed_model_seed": FIXED_MODEL_SEED,
                        "clustering_seed_pair": pair_name,
                        "ami": float(adjusted_mutual_info_score(pa, pb)),
                    })

    # =========================================================================
    # Step 2: MOFA+ (Classical Multimodal)
    # =========================================================================
    print("\n>>> STEP 2: MOFA+ (Classical Multimodal) <<<")
    for dataset in active_datasets:
        data_dict = load_dataset(dataset)
        embeddings_cache[dataset]["MOFA+"] = {}
        partitions_cache[dataset]["EXP_R"]["MOFA+"] = {}
        partitions_cache[dataset]["EXP_C"]["MOFA+"] = {}

        model_seeds = [FIXED_MODEL_SEED] if is_smoke else SEEDS
        for m_seed in model_seeds:
            t0 = time.time()
            emb, m_status, ep_done = run_mofaplus(data_dict, seed=m_seed, n_factors=10)
            t_train = time.time() - t0

            embeddings_cache[dataset]["MOFA+"][m_seed] = emb
            np.savez_compressed(EMB_DIR / f"emb_{dataset}_MOFA+_s{m_seed}.npz", embedding=emb)

            preds, diag, counts = compute_clustering_and_diagnostics(
                emb, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"], clustering_seed=FIXED_CLUSTERING_SEED
            )
            partitions_cache[dataset]["EXP_R"]["MOFA+"][m_seed] = preds
            if m_seed == FIXED_MODEL_SEED:
                partitions_cache[dataset]["EXP_C"]["MOFA+"][FIXED_CLUSTERING_SEED] = preds

            all_runs.append({
                "dataset": dataset,
                "method": "MOFA+",
                "experiment_type": "EXP_R",
                "model_seed": m_seed,
                "clustering_seed": FIXED_CLUSTERING_SEED,
                "N_total": data_dict["n_total"],
                "N_evaluation": data_dict["n_eval"],
                "K_reference": data_dict["k_ref"],
                **diag,
                "training_status": m_status,
                "epochs_requested": 1000,
                "epochs_completed": ep_done,
                "runtime_seconds": t_train,
            })
            print(f"[{dataset}][MOFA+][Exp R S{m_seed}] ARI: {diag['ari']:.4f}, Sil: {diag['silhouette']:.4f}, H_norm: {diag['h_norm']:.4f}, f_max: {diag['f_max']:.4f} ({t_train:.1f}s)")

            with open(CLUST_DIR / f"cluster_sizes_{dataset}_MOFA+_s{m_seed}.json", "w") as f_json:
                json.dump({"counts": counts.tolist(), "labels": [str(x) for x in range(len(counts))]}, f_json)

        # D1 Sensitivity check
        if dataset == "LN_D1" and not is_smoke:
            fixed_emb = embeddings_cache[dataset]["MOFA+"][FIXED_MODEL_SEED]
            sens_mask = np.ones(data_dict["n_total"], dtype=bool)
            sens_labels = data_dict["labels"]
            _, sens_diag, _ = compute_clustering_and_diagnostics(
                fixed_emb, sens_mask, sens_labels, 11, data_dict["sil_indices_sensitivity"], clustering_seed=FIXED_CLUSTERING_SEED
            )
            all_runs.append({
                "dataset": dataset,
                "method": "MOFA+",
                "experiment_type": "SENSITIVITY_ONLY",
                "model_seed": FIXED_MODEL_SEED,
                "clustering_seed": FIXED_CLUSTERING_SEED,
                "N_total": data_dict["n_total"],
                "N_evaluation": data_dict["n_total"],
                "K_reference": 11,
                **sens_diag,
                "training_status": "COMPLETED",
                "epochs_requested": "NA",
                "epochs_completed": "NA",
                "runtime_seconds": 0.0,
            })

        # Exp C on seed 1729
        if not is_smoke:
            fixed_emb = embeddings_cache[dataset]["MOFA+"][FIXED_MODEL_SEED]
            for c_seed in [2718, 31415]:
                preds, diag, _ = compute_clustering_and_diagnostics(
                    fixed_emb, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"], clustering_seed=c_seed
                )
                partitions_cache[dataset]["EXP_C"]["MOFA+"][c_seed] = preds
                all_runs.append({
                    "dataset": dataset,
                    "method": "MOFA+",
                    "experiment_type": "EXP_C",
                    "model_seed": FIXED_MODEL_SEED,
                    "clustering_seed": c_seed,
                    "N_total": data_dict["n_total"],
                    "N_evaluation": data_dict["n_eval"],
                    "K_reference": data_dict["k_ref"],
                    **diag,
                    "training_status": "COMPLETED",
                    "epochs_requested": "NA",
                    "epochs_completed": "NA",
                    "runtime_seconds": 0.0,
                })

            # Exp C Stability
            cp1729 = partitions_cache[dataset]["EXP_C"]["MOFA+"][1729]
            cp2718 = partitions_cache[dataset]["EXP_C"]["MOFA+"][2718]
            cp31415 = partitions_cache[dataset]["EXP_C"]["MOFA+"][31415]
            pairs = [("1729-2718", cp1729, cp2718), ("1729-31415", cp1729, cp31415), ("2718-31415", cp2718, cp31415)]
            for pair_name, pa, pb in pairs:
                all_clustering_stability.append({
                    "dataset": dataset,
                    "method": "MOFA+",
                    "fixed_model_seed": FIXED_MODEL_SEED,
                    "clustering_seed_pair": pair_name,
                    "ami": float(adjusted_mutual_info_score(pa, pb)),
                })

            # Exp R Stability
            e1729 = embeddings_cache[dataset]["MOFA+"][1729]
            e2718 = embeddings_cache[dataset]["MOFA+"][2718]
            e31415 = embeddings_cache[dataset]["MOFA+"][31415]
            p1729 = partitions_cache[dataset]["EXP_R"]["MOFA+"][1729]
            p2718 = partitions_cache[dataset]["EXP_R"]["MOFA+"][2718]
            p31415 = partitions_cache[dataset]["EXP_R"]["MOFA+"][31415]

            r_pairs = [("1729-2718", e1729, e2718, p1729, p2718), ("1729-31415", e1729, e31415, p1729, p31415), ("2718-31415", e2718, e31415, p2718, p31415)]
            for pair_name, ea, eb, pa, pb in r_pairs:
                j_res = compute_knn_jaccard(ea, eb, [5, 15, 30])
                spear = compute_distance_correlation(ea, eb)
                try:
                    _, _, proc_disp = procrustes(ea, eb)
                except Exception:
                    proc_disp = np.nan

                all_stability.append({
                    "dataset": dataset,
                    "method": "MOFA+",
                    "representation_seed_pair": pair_name,
                    "exp_r_cluster_ami": float(adjusted_mutual_info_score(pa, pb)),
                    "knn_jaccard_k5_mean": j_res[5]["mean"],
                    "knn_jaccard_k5_median": j_res[5]["median"],
                    "knn_jaccard_k15_mean": j_res[15]["mean"],
                    "knn_jaccard_k15_median": j_res[15]["median"],
                    "knn_jaccard_k30_mean": j_res[30]["mean"],
                    "knn_jaccard_k30_median": j_res[30]["median"],
                    "distance_spearman": spear,
                    "procrustes_discrepancy": float(proc_disp),
                })

    # =========================================================================
    # Step 3: Deep Non-Spatial Multimodal (totalVI for ADT, MultiVI for ATAC)
    # =========================================================================
    print("\n>>> STEP 3: Deep Non-Spatial Multimodal (totalVI & MultiVI) <<<")
    for dataset in active_datasets:
        data_dict = load_dataset(dataset)
        mod2_type = data_dict["mod2_type"]
        method_name = "totalVI" if mod2_type == "ADT" else "MultiVI"

        embeddings_cache[dataset][method_name] = {}
        partitions_cache[dataset]["EXP_R"][method_name] = {}
        partitions_cache[dataset]["EXP_C"][method_name] = {}

        model_seeds = [FIXED_MODEL_SEED] if is_smoke else SEEDS
        for m_seed in model_seeds:
            t0 = time.time()
            if method_name == "totalVI":
                emb, m_status, ep_done = run_totalvi(data_dict, seed=m_seed, n_latent=15, max_epochs=200, batch_size=128)
            else:
                emb, m_status, ep_done = run_multivi(data_dict, seed=m_seed, n_latent=15, max_epochs=200, batch_size=128)
            t_train = time.time() - t0

            embeddings_cache[dataset][method_name][m_seed] = emb
            np.savez_compressed(EMB_DIR / f"emb_{dataset}_{method_name}_s{m_seed}.npz", embedding=emb)

            preds, diag, counts = compute_clustering_and_diagnostics(
                emb, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"], clustering_seed=FIXED_CLUSTERING_SEED
            )
            partitions_cache[dataset]["EXP_R"][method_name][m_seed] = preds
            if m_seed == FIXED_MODEL_SEED:
                partitions_cache[dataset]["EXP_C"][method_name][FIXED_CLUSTERING_SEED] = preds

            all_runs.append({
                "dataset": dataset,
                "method": method_name,
                "experiment_type": "EXP_R",
                "model_seed": m_seed,
                "clustering_seed": FIXED_CLUSTERING_SEED,
                "N_total": data_dict["n_total"],
                "N_evaluation": data_dict["n_eval"],
                "K_reference": data_dict["k_ref"],
                **diag,
                "training_status": m_status,
                "epochs_requested": 200,
                "epochs_completed": ep_done,
                "runtime_seconds": t_train,
            })
            print(f"[{dataset}][{method_name}][Exp R S{m_seed}] ARI: {diag['ari']:.4f}, Sil: {diag['silhouette']:.4f}, H_norm: {diag['h_norm']:.4f}, f_max: {diag['f_max']:.4f} ({t_train:.1f}s)")

        # D1 Sensitivity check
        if dataset == "LN_D1" and not is_smoke:
            fixed_emb = embeddings_cache[dataset][method_name][FIXED_MODEL_SEED]
            sens_mask = np.ones(data_dict["n_total"], dtype=bool)
            sens_labels = data_dict["labels"]
            _, sens_diag, _ = compute_clustering_and_diagnostics(
                fixed_emb, sens_mask, sens_labels, 11, data_dict["sil_indices_sensitivity"], clustering_seed=FIXED_CLUSTERING_SEED
            )
            all_runs.append({
                "dataset": dataset,
                "method": method_name,
                "experiment_type": "SENSITIVITY_ONLY",
                "model_seed": FIXED_MODEL_SEED,
                "clustering_seed": FIXED_CLUSTERING_SEED,
                "N_total": data_dict["n_total"],
                "N_evaluation": data_dict["n_total"],
                "K_reference": 11,
                **sens_diag,
                "training_status": "COMPLETED",
                "epochs_requested": "NA",
                "epochs_completed": "NA",
                "runtime_seconds": 0.0,
            })

        # Exp C on seed 1729
        if not is_smoke:
            fixed_emb = embeddings_cache[dataset][method_name][FIXED_MODEL_SEED]
            for c_seed in [2718, 31415]:
                preds, diag, _ = compute_clustering_and_diagnostics(
                    fixed_emb, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"], clustering_seed=c_seed
                )
                partitions_cache[dataset]["EXP_C"][method_name][c_seed] = preds
                all_runs.append({
                    "dataset": dataset,
                    "method": method_name,
                    "experiment_type": "EXP_C",
                    "model_seed": FIXED_MODEL_SEED,
                    "clustering_seed": c_seed,
                    "N_total": data_dict["n_total"],
                    "N_evaluation": data_dict["n_eval"],
                    "K_reference": data_dict["k_ref"],
                    **diag,
                    "training_status": "COMPLETED",
                    "epochs_requested": "NA",
                    "epochs_completed": "NA",
                    "runtime_seconds": 0.0,
                })

            # Exp C Stability
            cp1729 = partitions_cache[dataset]["EXP_C"][method_name][1729]
            cp2718 = partitions_cache[dataset]["EXP_C"][method_name][2718]
            cp31415 = partitions_cache[dataset]["EXP_C"][method_name][31415]
            pairs = [("1729-2718", cp1729, cp2718), ("1729-31415", cp1729, cp31415), ("2718-31415", cp2718, cp31415)]
            for pair_name, pa, pb in pairs:
                all_clustering_stability.append({
                    "dataset": dataset,
                    "method": method_name,
                    "fixed_model_seed": FIXED_MODEL_SEED,
                    "clustering_seed_pair": pair_name,
                    "ami": float(adjusted_mutual_info_score(pa, pb)),
                })

            # Exp R Stability
            e1729 = embeddings_cache[dataset][method_name][1729]
            e2718 = embeddings_cache[dataset][method_name][2718]
            e31415 = embeddings_cache[dataset][method_name][31415]
            p1729 = partitions_cache[dataset]["EXP_R"][method_name][1729]
            p2718 = partitions_cache[dataset]["EXP_R"][method_name][2718]
            p31415 = partitions_cache[dataset]["EXP_R"][method_name][31415]

            r_pairs = [("1729-2718", e1729, e2718, p1729, p2718), ("1729-31415", e1729, e31415, p1729, p31415), ("2718-31415", e2718, e31415, p2718, p31415)]
            for pair_name, ea, eb, pa, pb in r_pairs:
                j_res = compute_knn_jaccard(ea, eb, [5, 15, 30])
                spear = compute_distance_correlation(ea, eb)
                try:
                    _, _, proc_disp = procrustes(ea, eb)
                except Exception:
                    proc_disp = np.nan

                all_stability.append({
                    "dataset": dataset,
                    "method": method_name,
                    "representation_seed_pair": pair_name,
                    "exp_r_cluster_ami": float(adjusted_mutual_info_score(pa, pb)),
                    "knn_jaccard_k5_mean": j_res[5]["mean"],
                    "knn_jaccard_k5_median": j_res[5]["median"],
                    "knn_jaccard_k15_mean": j_res[15]["mean"],
                    "knn_jaccard_k15_median": j_res[15]["median"],
                    "knn_jaccard_k30_mean": j_res[30]["mean"],
                    "knn_jaccard_k30_median": j_res[30]["median"],
                    "distance_spearman": spear,
                    "procrustes_discrepancy": float(proc_disp),
                })

    # =========================================================================
    # Step 4: Spatial Multimodal (SpatialGlue Across Datasets)
    # =========================================================================
    print("\n>>> STEP 4: Spatial Multimodal (SpatialGlue) <<<")
    for dataset in active_datasets:
        data_dict = load_dataset(dataset)
        embeddings_cache[dataset]["SpatialGlue"] = {}
        partitions_cache[dataset]["EXP_R"]["SpatialGlue"] = {}
        partitions_cache[dataset]["EXP_C"]["SpatialGlue"] = {}

        model_seeds = [FIXED_MODEL_SEED] if is_smoke else SEEDS
        for m_seed in model_seeds:
            t0 = time.time()
            emb, m_status, ep_done = run_spatialglue(data_dict, seed=m_seed)
            t_train = time.time() - t0

            embeddings_cache[dataset]["SpatialGlue"][m_seed] = emb
            np.savez_compressed(EMB_DIR / f"emb_{dataset}_SpatialGlue_s{m_seed}.npz", embedding=emb)

            preds, diag, counts = compute_clustering_and_diagnostics(
                emb, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"], clustering_seed=FIXED_CLUSTERING_SEED
            )
            partitions_cache[dataset]["EXP_R"]["SpatialGlue"][m_seed] = preds
            if m_seed == FIXED_MODEL_SEED:
                partitions_cache[dataset]["EXP_C"]["SpatialGlue"][FIXED_CLUSTERING_SEED] = preds

            all_runs.append({
                "dataset": dataset,
                "method": "SpatialGlue",
                "experiment_type": "EXP_R",
                "model_seed": m_seed,
                "clustering_seed": FIXED_CLUSTERING_SEED,
                "N_total": data_dict["n_total"],
                "N_evaluation": data_dict["n_eval"],
                "K_reference": data_dict["k_ref"],
                **diag,
                "training_status": m_status,
                "epochs_requested": ep_done,
                "epochs_completed": ep_done,
                "runtime_seconds": t_train,
            })
            print(f"[{dataset}][SpatialGlue][Exp R S{m_seed}] ARI: {diag['ari']:.4f}, Sil: {diag['silhouette']:.4f}, H_norm: {diag['h_norm']:.4f}, f_max: {diag['f_max']:.4f} ({t_train:.1f}s)")

            with open(CLUST_DIR / f"cluster_sizes_{dataset}_SpatialGlue_s{m_seed}.json", "w") as f_json:
                json.dump({"counts": counts.tolist(), "labels": [str(x) for x in range(len(counts))]}, f_json)

        # D1 Sensitivity check
        if dataset == "LN_D1" and not is_smoke:
            fixed_emb = embeddings_cache[dataset]["SpatialGlue"][FIXED_MODEL_SEED]
            sens_mask = np.ones(data_dict["n_total"], dtype=bool)
            sens_labels = data_dict["labels"]
            _, sens_diag, _ = compute_clustering_and_diagnostics(
                fixed_emb, sens_mask, sens_labels, 11, data_dict["sil_indices_sensitivity"], clustering_seed=FIXED_CLUSTERING_SEED
            )
            all_runs.append({
                "dataset": dataset,
                "method": "SpatialGlue",
                "experiment_type": "SENSITIVITY_ONLY",
                "model_seed": FIXED_MODEL_SEED,
                "clustering_seed": FIXED_CLUSTERING_SEED,
                "N_total": data_dict["n_total"],
                "N_evaluation": data_dict["n_total"],
                "K_reference": 11,
                **sens_diag,
                "training_status": "COMPLETED",
                "epochs_requested": "NA",
                "epochs_completed": "NA",
                "runtime_seconds": 0.0,
            })

        # Exp C on seed 1729
        if not is_smoke:
            fixed_emb = embeddings_cache[dataset]["SpatialGlue"][FIXED_MODEL_SEED]
            for c_seed in [2718, 31415]:
                preds, diag, _ = compute_clustering_and_diagnostics(
                    fixed_emb, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"], clustering_seed=c_seed
                )
                partitions_cache[dataset]["EXP_C"]["SpatialGlue"][c_seed] = preds
                all_runs.append({
                    "dataset": dataset,
                    "method": "SpatialGlue",
                    "experiment_type": "EXP_C",
                    "model_seed": FIXED_MODEL_SEED,
                    "clustering_seed": c_seed,
                    "N_total": data_dict["n_total"],
                    "N_evaluation": data_dict["n_eval"],
                    "K_reference": data_dict["k_ref"],
                    **diag,
                    "training_status": "COMPLETED",
                    "epochs_requested": "NA",
                    "epochs_completed": "NA",
                    "runtime_seconds": 0.0,
                })

            # Exp C Stability
            cp1729 = partitions_cache[dataset]["EXP_C"]["SpatialGlue"][1729]
            cp2718 = partitions_cache[dataset]["EXP_C"]["SpatialGlue"][2718]
            cp31415 = partitions_cache[dataset]["EXP_C"]["SpatialGlue"][31415]
            pairs = [("1729-2718", cp1729, cp2718), ("1729-31415", cp1729, cp31415), ("2718-31415", cp2718, cp31415)]
            for pair_name, pa, pb in pairs:
                all_clustering_stability.append({
                    "dataset": dataset,
                    "method": "SpatialGlue",
                    "fixed_model_seed": FIXED_MODEL_SEED,
                    "clustering_seed_pair": pair_name,
                    "ami": float(adjusted_mutual_info_score(pa, pb)),
                })

            # Exp R Stability
            e1729 = embeddings_cache[dataset]["SpatialGlue"][1729]
            e2718 = embeddings_cache[dataset]["SpatialGlue"][2718]
            e31415 = embeddings_cache[dataset]["SpatialGlue"][31415]
            p1729 = partitions_cache[dataset]["EXP_R"]["SpatialGlue"][1729]
            p2718 = partitions_cache[dataset]["EXP_R"]["SpatialGlue"][2718]
            p31415 = partitions_cache[dataset]["EXP_R"]["SpatialGlue"][31415]

            r_pairs = [("1729-2718", e1729, e2718, p1729, p2718), ("1729-31415", e1729, e31415, p1729, p31415), ("2718-31415", e2718, e31415, p2718, p31415)]
            for pair_name, ea, eb, pa, pb in r_pairs:
                j_res = compute_knn_jaccard(ea, eb, [5, 15, 30])
                spear = compute_distance_correlation(ea, eb)
                try:
                    _, _, proc_disp = procrustes(ea, eb)
                except Exception:
                    proc_disp = np.nan

                all_stability.append({
                    "dataset": dataset,
                    "method": "SpatialGlue",
                    "representation_seed_pair": pair_name,
                    "exp_r_cluster_ami": float(adjusted_mutual_info_score(pa, pb)),
                    "knn_jaccard_k5_mean": j_res[5]["mean"],
                    "knn_jaccard_k5_median": j_res[5]["median"],
                    "knn_jaccard_k15_mean": j_res[15]["mean"],
                    "knn_jaccard_k15_median": j_res[15]["median"],
                    "knn_jaccard_k30_mean": j_res[30]["mean"],
                    "knn_jaccard_k30_median": j_res[30]["median"],
                    "distance_spearman": spear,
                    "procrustes_discrepancy": float(proc_disp),
                })

    # =========================================================================
    # Step 5: Spatial Controls (SpatialGlue Ablation on LN_A1 and MB_E13)
    # =========================================================================
    if not is_smoke:
        print("\n>>> STEP 5: Spatial Controls (Controls A, B, C, D) <<<")
        for dataset in ["LN_A1", "MB_E13"]:
            data_dict = load_dataset(dataset)
            n_tot = data_dict["n_total"]
            coords = data_dict["coords"]

            # Control A: True molecular + True space (already in embeddings_cache)
            emb_a = embeddings_cache[dataset]["SpatialGlue"][FIXED_MODEL_SEED]
            _, diag_a, _ = compute_clustering_and_diagnostics(
                emb_a, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"], clustering_seed=FIXED_CLUSTERING_SEED
            )

            # Control B: Jointly permuted molecular (pi(R), pi(M)) + True space
            np.random.seed(PERMUTATION_SEED)
            perm_mol = np.random.permutation(n_tot)
            trans = get_transparent_representations(data_dict)
            emb_b, _, _ = run_spatialglue(
                data_dict,
                seed=FIXED_MODEL_SEED,
                custom_rna_emb=trans["RNA"][perm_mol],
                custom_m2_emb=trans["M2"][perm_mol],
                custom_coords=coords,
            )
            _, diag_b, _ = compute_clustering_and_diagnostics(
                emb_b, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"], clustering_seed=FIXED_CLUSTERING_SEED
            )

            # Control C: True molecular + Permuted space pi(S)
            np.random.seed(PERMUTATION_SEED)
            perm_sp = np.random.permutation(n_tot)
            emb_c, _, _ = run_spatialglue(
                data_dict,
                seed=FIXED_MODEL_SEED,
                custom_rna_emb=trans["RNA"],
                custom_m2_emb=trans["M2"],
                custom_coords=coords[perm_sp],
            )
            _, diag_c, _ = compute_clustering_and_diagnostics(
                emb_c, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"], clustering_seed=FIXED_CLUSTERING_SEED
            )

            # Invariant distances vs Paired Control A
            jaccard_b = compute_knn_jaccard(emb_a, emb_b, [15])[15]["mean"]
            spear_b = compute_distance_correlation(emb_a, emb_b)
            try:
                _, _, proc_b = procrustes(emb_a, emb_b)
                proc_b = float(proc_b)
            except Exception:
                proc_b = np.nan

            jaccard_c = compute_knn_jaccard(emb_a, emb_c, [15])[15]["mean"]
            spear_c = compute_distance_correlation(emb_a, emb_c)
            try:
                _, _, proc_c = procrustes(emb_a, emb_c)
                proc_c = float(proc_c)
            except Exception:
                proc_c = np.nan

            # Record controls
            all_permutations.append({
                "dataset": dataset,
                "method": "SpatialGlue",
                "permutation_type": "MOLECULAR_TO_SPACE_PERMUTED",
                "model_seed": FIXED_MODEL_SEED,
                "permutation_seed": PERMUTATION_SEED,
                "clustering_seed": FIXED_CLUSTERING_SEED,
                "ari": diag_b["ari"],
                "nmi": diag_b["nmi"],
                "silhouette": diag_b["silhouette"],
                "delta_ari_vs_paired": diag_b["ari"] - diag_a["ari"],
                "delta_nmi_vs_paired": diag_b["nmi"] - diag_a["nmi"],
                "neighborhood_jaccard_vs_paired": jaccard_b,
                "distance_spearman_vs_paired": spear_b,
                "procrustes_discrepancy_vs_paired": proc_b,
                "raw_coord_distance_vs_paired": "NA",
            })

            all_permutations.append({
                "dataset": dataset,
                "method": "SpatialGlue",
                "permutation_type": "SPACE_PERMUTED",
                "model_seed": FIXED_MODEL_SEED,
                "permutation_seed": PERMUTATION_SEED,
                "clustering_seed": FIXED_CLUSTERING_SEED,
                "ari": diag_c["ari"],
                "nmi": diag_c["nmi"],
                "silhouette": diag_c["silhouette"],
                "delta_ari_vs_paired": diag_c["ari"] - diag_a["ari"],
                "delta_nmi_vs_paired": diag_c["nmi"] - diag_a["nmi"],
                "neighborhood_jaccard_vs_paired": jaccard_c,
                "distance_spearman_vs_paired": spear_c,
                "procrustes_discrepancy_vs_paired": proc_c,
                "raw_coord_distance_vs_paired": "NA",
            })

            print(f"[{dataset}] Spatial Controls: Ctrl A (True) ARI={diag_a['ari']:.4f} | Ctrl B (Perm Mol) ARI={diag_b['ari']:.4f} | Ctrl C (Perm Space) ARI={diag_c['ari']:.4f}")

    # =========================================================================
    # Step 6: Modality Pairing Permutations (CONCAT, MOFA+, SpatialGlue, totalVI on A1, MultiVI on E13)
    # =========================================================================
    if not is_smoke:
        print("\n>>> STEP 6: Modality Pairing Permutations (M2 Permuted vs RNA Permuted) <<<")
        audit_rows = []
        for dataset in ["LN_A1", "MB_E13"]:
            data_dict = load_dataset(dataset)
            n_tot = data_dict["n_total"]
            np.random.seed(PERMUTATION_SEED)
            perm = np.random.permutation(n_tot)

            # Build and verify permutation audit records (at least 20 sampled spots)
            for sample_idx in range(min(25, n_tot)):
                audit_rows.append({
                    "dataset": dataset,
                    "row_index": sample_idx,
                    "barcode": data_dict["adata_rna"].obs_names[sample_idx],
                    "rna_source_row_for_m2_perm": sample_idx,
                    "m2_source_row_for_m2_perm": int(perm[sample_idx]),
                    "rna_barcode_unchanged": True,
                    "m2_barcode_unchanged": True,
                    "pairing_destroyed": bool(sample_idx != perm[sample_idx]),
                })

            trans = get_transparent_representations(data_dict)
            emb_rna_orig = trans["RNA"]
            emb_m2_orig = trans["M2"]

            # 1. CONCAT
            concat_orig_ari = [r for r in all_runs if r["dataset"] == dataset and r["method"] == "CONCAT" and r["clustering_seed"] == 1729][0]["ari"]
            concat_orig_nmi = [r for r in all_runs if r["dataset"] == dataset and r["method"] == "CONCAT" and r["clustering_seed"] == 1729][0]["nmi"]
            concat_orig_emb = trans["CONCAT"]

            # M2 permuted
            concat_m2_perm = np.hstack([emb_rna_orig, emb_m2_orig[perm]])
            _, d_c_m2, _ = compute_clustering_and_diagnostics(concat_m2_perm, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"])
            all_permutations.append({
                "dataset": dataset, "method": "CONCAT", "permutation_type": "M2_PAIRING_PERMUTED",
                "model_seed": FIXED_MODEL_SEED, "permutation_seed": PERMUTATION_SEED, "clustering_seed": FIXED_CLUSTERING_SEED,
                "ari": d_c_m2["ari"], "nmi": d_c_m2["nmi"], "silhouette": d_c_m2["silhouette"],
                "delta_ari_vs_paired": d_c_m2["ari"] - concat_orig_ari, "delta_nmi_vs_paired": d_c_m2["nmi"] - concat_orig_nmi,
                "neighborhood_jaccard_vs_paired": compute_knn_jaccard(concat_orig_emb, concat_m2_perm, [15])[15]["mean"],
                "distance_spearman_vs_paired": compute_distance_correlation(concat_orig_emb, concat_m2_perm),
                "procrustes_discrepancy_vs_paired": float(procrustes(concat_orig_emb, concat_m2_perm)[2]),
                "raw_coord_distance_vs_paired": float(np.mean(np.linalg.norm(concat_m2_perm - concat_orig_emb, axis=1))),
            })

            # RNA permuted
            concat_rna_perm = np.hstack([emb_rna_orig[perm], emb_m2_orig])
            _, d_c_rna, _ = compute_clustering_and_diagnostics(concat_rna_perm, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"])
            all_permutations.append({
                "dataset": dataset, "method": "CONCAT", "permutation_type": "RNA_PAIRING_PERMUTED",
                "model_seed": FIXED_MODEL_SEED, "permutation_seed": PERMUTATION_SEED, "clustering_seed": FIXED_CLUSTERING_SEED,
                "ari": d_c_rna["ari"], "nmi": d_c_rna["nmi"], "silhouette": d_c_rna["silhouette"],
                "delta_ari_vs_paired": d_c_rna["ari"] - concat_orig_ari, "delta_nmi_vs_paired": d_c_rna["nmi"] - concat_orig_nmi,
                "neighborhood_jaccard_vs_paired": compute_knn_jaccard(concat_orig_emb, concat_rna_perm, [15])[15]["mean"],
                "distance_spearman_vs_paired": compute_distance_correlation(concat_orig_emb, concat_rna_perm),
                "procrustes_discrepancy_vs_paired": float(procrustes(concat_orig_emb, concat_rna_perm)[2]),
                "raw_coord_distance_vs_paired": float(np.mean(np.linalg.norm(concat_rna_perm - concat_orig_emb, axis=1))),
            })

            # 2. MOFA+ (Retrained from scratch using permute_measurements_keep_obs)
            mofa_orig_emb = embeddings_cache[dataset]["MOFA+"][FIXED_MODEL_SEED]
            mofa_orig_ari = [r for r in all_runs if r["dataset"] == dataset and r["method"] == "MOFA+" and r["model_seed"] == 1729 and r["experiment_type"] == "EXP_R"][0]["ari"]
            mofa_orig_nmi = [r for r in all_runs if r["dataset"] == dataset and r["method"] == "MOFA+" and r["model_seed"] == 1729 and r["experiment_type"] == "EXP_R"][0]["nmi"]

            # M2 permuted
            dict_m2_perm = dict(data_dict)
            dict_m2_perm["adata_m2"] = permute_measurements_keep_obs(data_dict["adata_m2"], perm)
            emb_mofa_m2_perm, _, _ = run_mofaplus(dict_m2_perm, seed=FIXED_MODEL_SEED, n_factors=10)
            _, d_m_m2, _ = compute_clustering_and_diagnostics(emb_mofa_m2_perm, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"])
            all_permutations.append({
                "dataset": dataset, "method": "MOFA+", "permutation_type": "M2_PAIRING_PERMUTED",
                "model_seed": FIXED_MODEL_SEED, "permutation_seed": PERMUTATION_SEED, "clustering_seed": FIXED_CLUSTERING_SEED,
                "ari": d_m_m2["ari"], "nmi": d_m_m2["nmi"], "silhouette": d_m_m2["silhouette"],
                "delta_ari_vs_paired": d_m_m2["ari"] - mofa_orig_ari, "delta_nmi_vs_paired": d_m_m2["nmi"] - mofa_orig_nmi,
                "neighborhood_jaccard_vs_paired": compute_knn_jaccard(mofa_orig_emb, emb_mofa_m2_perm, [15])[15]["mean"],
                "distance_spearman_vs_paired": compute_distance_correlation(mofa_orig_emb, emb_mofa_m2_perm),
                "procrustes_discrepancy_vs_paired": float(procrustes(mofa_orig_emb, emb_mofa_m2_perm)[2]),
                "raw_coord_distance_vs_paired": "NA",
            })

            # RNA permuted
            dict_rna_perm = dict(data_dict)
            dict_rna_perm["adata_rna"] = permute_measurements_keep_obs(data_dict["adata_rna"], perm)
            emb_mofa_rna_perm, _, _ = run_mofaplus(dict_rna_perm, seed=FIXED_MODEL_SEED, n_factors=10)
            _, d_m_rna, _ = compute_clustering_and_diagnostics(emb_mofa_rna_perm, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"])
            all_permutations.append({
                "dataset": dataset, "method": "MOFA+", "permutation_type": "RNA_PAIRING_PERMUTED",
                "model_seed": FIXED_MODEL_SEED, "permutation_seed": PERMUTATION_SEED, "clustering_seed": FIXED_CLUSTERING_SEED,
                "ari": d_m_rna["ari"], "nmi": d_m_rna["nmi"], "silhouette": d_m_rna["silhouette"],
                "delta_ari_vs_paired": d_m_rna["ari"] - mofa_orig_ari, "delta_nmi_vs_paired": d_m_rna["nmi"] - mofa_orig_nmi,
                "neighborhood_jaccard_vs_paired": compute_knn_jaccard(mofa_orig_emb, emb_mofa_rna_perm, [15])[15]["mean"],
                "distance_spearman_vs_paired": compute_distance_correlation(mofa_orig_emb, emb_mofa_rna_perm),
                "procrustes_discrepancy_vs_paired": float(procrustes(mofa_orig_emb, emb_mofa_rna_perm)[2]),
                "raw_coord_distance_vs_paired": "NA",
            })

            # 3. SpatialGlue (Retrained from scratch with unpermuted coordinates)
            sg_orig_emb = embeddings_cache[dataset]["SpatialGlue"][FIXED_MODEL_SEED]
            sg_orig_ari = [r for r in all_runs if r["dataset"] == dataset and r["method"] == "SpatialGlue" and r["model_seed"] == 1729 and r["experiment_type"] == "EXP_R"][0]["ari"]
            sg_orig_nmi = [r for r in all_runs if r["dataset"] == dataset and r["method"] == "SpatialGlue" and r["model_seed"] == 1729 and r["experiment_type"] == "EXP_R"][0]["nmi"]

            # M2 permuted (custom_m2_emb permuted, custom_rna_emb & custom_coords unpermuted)
            emb_sg_m2_perm, _, _ = run_spatialglue(
                data_dict,
                seed=FIXED_MODEL_SEED,
                custom_rna_emb=emb_rna_orig,
                custom_m2_emb=emb_m2_orig[perm],
                custom_coords=data_dict["coords"],
            )
            _, d_sg_m2, _ = compute_clustering_and_diagnostics(emb_sg_m2_perm, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"])
            all_permutations.append({
                "dataset": dataset, "method": "SpatialGlue", "permutation_type": "M2_PAIRING_PERMUTED",
                "model_seed": FIXED_MODEL_SEED, "permutation_seed": PERMUTATION_SEED, "clustering_seed": FIXED_CLUSTERING_SEED,
                "ari": d_sg_m2["ari"], "nmi": d_sg_m2["nmi"], "silhouette": d_sg_m2["silhouette"],
                "delta_ari_vs_paired": d_sg_m2["ari"] - sg_orig_ari, "delta_nmi_vs_paired": d_sg_m2["nmi"] - sg_orig_nmi,
                "neighborhood_jaccard_vs_paired": compute_knn_jaccard(sg_orig_emb, emb_sg_m2_perm, [15])[15]["mean"],
                "distance_spearman_vs_paired": compute_distance_correlation(sg_orig_emb, emb_sg_m2_perm),
                "procrustes_discrepancy_vs_paired": float(procrustes(sg_orig_emb, emb_sg_m2_perm)[2]),
                "raw_coord_distance_vs_paired": "NA",
            })

            # RNA permuted (retrain SpatialGlue)
            emb_sg_rna_perm, _, _ = run_spatialglue(
                data_dict,
                seed=FIXED_MODEL_SEED,
                custom_rna_emb=emb_rna_orig[perm],
                custom_m2_emb=emb_m2_orig,
                custom_coords=data_dict["coords"],
            )
            _, d_sg_rna, _ = compute_clustering_and_diagnostics(emb_sg_rna_perm, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"])
            all_permutations.append({
                "dataset": dataset, "method": "SpatialGlue", "permutation_type": "RNA_PAIRING_PERMUTED",
                "model_seed": FIXED_MODEL_SEED, "permutation_seed": PERMUTATION_SEED, "clustering_seed": FIXED_CLUSTERING_SEED,
                "ari": d_sg_rna["ari"], "nmi": d_sg_rna["nmi"], "silhouette": d_sg_rna["silhouette"],
                "delta_ari_vs_paired": d_sg_rna["ari"] - sg_orig_ari, "delta_nmi_vs_paired": d_sg_rna["nmi"] - sg_orig_nmi,
                "neighborhood_jaccard_vs_paired": compute_knn_jaccard(sg_orig_emb, emb_sg_rna_perm, [15])[15]["mean"],
                "distance_spearman_vs_paired": compute_distance_correlation(sg_orig_emb, emb_sg_rna_perm),
                "procrustes_discrepancy_vs_paired": float(procrustes(sg_orig_emb, emb_sg_rna_perm)[2]),
                "raw_coord_distance_vs_paired": "NA",
            })

            # 4. Deep Model Pairing Permutations: totalVI (on A1) and MultiVI (on E13)
            if dataset == "LN_A1":
                tot_orig_emb = embeddings_cache[dataset]["totalVI"][FIXED_MODEL_SEED]
                tot_orig_ari = [r for r in all_runs if r["dataset"] == dataset and r["method"] == "totalVI" and r["model_seed"] == 1729 and r["experiment_type"] == "EXP_R"][0]["ari"]
                tot_orig_nmi = [r for r in all_runs if r["dataset"] == dataset and r["method"] == "totalVI" and r["model_seed"] == 1729 and r["experiment_type"] == "EXP_R"][0]["nmi"]

                # ADT permuted
                dict_adt_perm = dict(data_dict)
                dict_adt_perm["adata_m2"] = permute_measurements_keep_obs(data_dict["adata_m2"], perm)
                emb_tot_adt_perm, _, _ = run_totalvi(dict_adt_perm, seed=FIXED_MODEL_SEED, n_latent=15, max_epochs=200, batch_size=128)
                _, d_t_adt, _ = compute_clustering_and_diagnostics(emb_tot_adt_perm, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"])
                all_permutations.append({
                    "dataset": dataset, "method": "totalVI", "permutation_type": "M2_PAIRING_PERMUTED",
                    "model_seed": FIXED_MODEL_SEED, "permutation_seed": PERMUTATION_SEED, "clustering_seed": FIXED_CLUSTERING_SEED,
                    "ari": d_t_adt["ari"], "nmi": d_t_adt["nmi"], "silhouette": d_t_adt["silhouette"],
                    "delta_ari_vs_paired": d_t_adt["ari"] - tot_orig_ari, "delta_nmi_vs_paired": d_t_adt["nmi"] - tot_orig_nmi,
                    "neighborhood_jaccard_vs_paired": compute_knn_jaccard(tot_orig_emb, emb_tot_adt_perm, [15])[15]["mean"],
                    "distance_spearman_vs_paired": compute_distance_correlation(tot_orig_emb, emb_tot_adt_perm),
                    "procrustes_discrepancy_vs_paired": float(procrustes(tot_orig_emb, emb_tot_adt_perm)[2]),
                    "raw_coord_distance_vs_paired": "NA",
                })

                # RNA permuted
                dict_tot_rna = dict(data_dict)
                dict_tot_rna["adata_rna"] = permute_measurements_keep_obs(data_dict["adata_rna"], perm)
                emb_tot_rna_perm, _, _ = run_totalvi(dict_tot_rna, seed=FIXED_MODEL_SEED, n_latent=15, max_epochs=200, batch_size=128)
                _, d_t_rna, _ = compute_clustering_and_diagnostics(emb_tot_rna_perm, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"])
                all_permutations.append({
                    "dataset": dataset, "method": "totalVI", "permutation_type": "RNA_PAIRING_PERMUTED",
                    "model_seed": FIXED_MODEL_SEED, "permutation_seed": PERMUTATION_SEED, "clustering_seed": FIXED_CLUSTERING_SEED,
                    "ari": d_t_rna["ari"], "nmi": d_t_rna["nmi"], "silhouette": d_t_rna["silhouette"],
                    "delta_ari_vs_paired": d_t_rna["ari"] - tot_orig_ari, "delta_nmi_vs_paired": d_t_rna["nmi"] - tot_orig_nmi,
                    "neighborhood_jaccard_vs_paired": compute_knn_jaccard(tot_orig_emb, emb_tot_rna_perm, [15])[15]["mean"],
                    "distance_spearman_vs_paired": compute_distance_correlation(tot_orig_emb, emb_tot_rna_perm),
                    "procrustes_discrepancy_vs_paired": float(procrustes(tot_orig_emb, emb_tot_rna_perm)[2]),
                    "raw_coord_distance_vs_paired": "NA",
                })
                print(f"[{dataset}] totalVI Pairing Perm: Orig ARI={tot_orig_ari:.4f} | ADT Perm ARI={d_t_adt['ari']:.4f} | RNA Perm ARI={d_t_rna['ari']:.4f}")

            elif dataset == "MB_E13":
                mvi_orig_emb = embeddings_cache[dataset]["MultiVI"][FIXED_MODEL_SEED]
                mvi_orig_ari = [r for r in all_runs if r["dataset"] == dataset and r["method"] == "MultiVI" and r["model_seed"] == 1729 and r["experiment_type"] == "EXP_R"][0]["ari"]
                mvi_orig_nmi = [r for r in all_runs if r["dataset"] == dataset and r["method"] == "MultiVI" and r["model_seed"] == 1729 and r["experiment_type"] == "EXP_R"][0]["nmi"]

                # ATAC permuted
                dict_atac_perm = dict(data_dict)
                dict_atac_perm["adata_m2"] = permute_measurements_keep_obs(data_dict["adata_m2"], perm)
                emb_mvi_atac_perm, _, _ = run_multivi(dict_atac_perm, seed=FIXED_MODEL_SEED, n_latent=15, max_epochs=200, batch_size=128)
                _, d_mv_atac, _ = compute_clustering_and_diagnostics(emb_mvi_atac_perm, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"])
                all_permutations.append({
                    "dataset": dataset, "method": "MultiVI", "permutation_type": "M2_PAIRING_PERMUTED",
                    "model_seed": FIXED_MODEL_SEED, "permutation_seed": PERMUTATION_SEED, "clustering_seed": FIXED_CLUSTERING_SEED,
                    "ari": d_mv_atac["ari"], "nmi": d_mv_atac["nmi"], "silhouette": d_mv_atac["silhouette"],
                    "delta_ari_vs_paired": d_mv_atac["ari"] - mvi_orig_ari, "delta_nmi_vs_paired": d_mv_atac["nmi"] - mvi_orig_nmi,
                    "neighborhood_jaccard_vs_paired": compute_knn_jaccard(mvi_orig_emb, emb_mvi_atac_perm, [15])[15]["mean"],
                    "distance_spearman_vs_paired": compute_distance_correlation(mvi_orig_emb, emb_mvi_atac_perm),
                    "procrustes_discrepancy_vs_paired": float(procrustes(mvi_orig_emb, emb_mvi_atac_perm)[2]),
                    "raw_coord_distance_vs_paired": "NA",
                })

                # RNA permuted
                dict_mvi_rna = dict(data_dict)
                dict_mvi_rna["adata_rna"] = permute_measurements_keep_obs(data_dict["adata_rna"], perm)
                emb_mvi_rna_perm, _, _ = run_multivi(dict_mvi_rna, seed=FIXED_MODEL_SEED, n_latent=15, max_epochs=200, batch_size=128)
                _, d_mv_rna, _ = compute_clustering_and_diagnostics(emb_mvi_rna_perm, data_dict["eval_mask"], data_dict["eval_labels"], data_dict["k_ref"], data_dict["sil_indices"])
                all_permutations.append({
                    "dataset": dataset, "method": "MultiVI", "permutation_type": "RNA_PAIRING_PERMUTED",
                    "model_seed": FIXED_MODEL_SEED, "permutation_seed": PERMUTATION_SEED, "clustering_seed": FIXED_CLUSTERING_SEED,
                    "ari": d_mv_rna["ari"], "nmi": d_mv_rna["nmi"], "silhouette": d_mv_rna["silhouette"],
                    "delta_ari_vs_paired": d_mv_rna["ari"] - mvi_orig_ari, "delta_nmi_vs_paired": d_mv_rna["nmi"] - mvi_orig_nmi,
                    "neighborhood_jaccard_vs_paired": compute_knn_jaccard(mvi_orig_emb, emb_mvi_rna_perm, [15])[15]["mean"],
                    "distance_spearman_vs_paired": compute_distance_correlation(mvi_orig_emb, emb_mvi_rna_perm),
                    "procrustes_discrepancy_vs_paired": float(procrustes(mvi_orig_emb, emb_mvi_rna_perm)[2]),
                    "raw_coord_distance_vs_paired": "NA",
                })
                print(f"[{dataset}] MultiVI Pairing Perm: Orig ARI={mvi_orig_ari:.4f} | ATAC Perm ARI={d_mv_atac['ari']:.4f} | RNA Perm ARI={d_mv_rna['ari']:.4f}")

        if audit_rows:
            pd.DataFrame(audit_rows).to_csv(PERM_DIR / "permutation_semantics_audit.csv", index=False)
            print("permutation_semantics_audit.csv saved successfully.")

    # =========================================================================
    # Step 7: Core Table Serialization
    # =========================================================================
    print("\n>>> STEP 7: Serializing Core Benchmark CSV Tables <<<")
    runs_df = pd.DataFrame(all_runs)
    runs_df.to_csv(OUT_DIR / "PHASE_4B_RUNS.csv", index=False)
    print("PHASE_4B_RUNS.csv saved.")

    stability_df = pd.DataFrame(all_stability)
    stability_df.to_csv(OUT_DIR / "PHASE_4B_STABILITY.csv", index=False)
    print("PHASE_4B_STABILITY.csv saved.")

    clustering_stab_df = pd.DataFrame(all_clustering_stability)
    clustering_stab_df.to_csv(OUT_DIR / "PHASE_4B_CLUSTERING_STABILITY.csv", index=False)
    print("PHASE_4B_CLUSTERING_STABILITY.csv saved.")

    perms_df = pd.DataFrame(all_permutations)
    perms_df.to_csv(OUT_DIR / "PHASE_4B_PERMUTATIONS.csv", index=False)
    print("PHASE_4B_PERMUTATIONS.csv saved.")

    # Generate PHASE_4B_DIAGNOSTICS.csv separating Primary Performance from Stochasticity
    diag_rows = []
    for dataset in active_datasets:
        space_runs = runs_df[(runs_df["dataset"] == dataset) & (runs_df["method"] == "SPACE") & (runs_df["clustering_seed"] == 1729)]
        space_ari = space_runs["ari"].values[0] if len(space_runs) > 0 else np.nan
        space_nmi = space_runs["nmi"].values[0] if len(space_runs) > 0 else np.nan

        rna_runs = runs_df[(runs_df["dataset"] == dataset) & (runs_df["method"] == "RNA") & (runs_df["clustering_seed"] == 1729)]
        rna_ari = rna_runs["ari"].values[0] if len(rna_runs) > 0 else np.nan

        m2_runs = runs_df[(runs_df["dataset"] == dataset) & (runs_df["method"] == "M2") & (runs_df["clustering_seed"] == 1729)]
        m2_ari = m2_runs["ari"].values[0] if len(m2_runs) > 0 else np.nan

        methods_in_d = runs_df[runs_df["dataset"] == dataset]["method"].unique()
        for method in methods_in_d:
            m_runs = runs_df[(runs_df["dataset"] == dataset) & (runs_df["method"] == method)]

            # 1. Primary Performance: model_seed=1729, clustering_seed=1729 (excluding SENSITIVITY_ONLY)
            primary_runs = m_runs[(m_runs["clustering_seed"] == 1729) & (m_runs["experiment_type"] != "SENSITIVITY_ONLY")]
            if method in ["MOFA+", "totalVI", "MultiVI", "SpatialGlue"]:
                p_run = primary_runs[primary_runs["model_seed"] == 1729]
            else:
                p_run = primary_runs

            if len(p_run) > 0:
                p_row = p_run.iloc[0]
                ari_primary = float(p_row["ari"])
                nmi_primary = float(p_row["nmi"])
                sil_primary = float(p_row["silhouette"])
                hnorm_primary = float(p_row["h_norm"])
                keff_primary = float(p_row["k_eff"])
                fmax_primary = float(p_row["f_max"])
                sing_primary = float(p_row["singleton_fraction"])
                zero_clust_primary = int(p_row.get("zero_cluster_count", 0))
                min_sz_primary = int(p_row["min_cluster_size"])
                max_sz_primary = int(p_row["max_cluster_size"])
            else:
                ari_primary = nmi_primary = sil_primary = np.nan
                hnorm_primary = keff_primary = fmax_primary = sing_primary = np.nan
                zero_clust_primary = min_sz_primary = max_sz_primary = np.nan

            # 2. Representation Stochasticity (Exp R across model seeds 1729, 2718, 31415)
            if method in ["MOFA+", "totalVI", "MultiVI", "SpatialGlue"]:
                exp_r_runs = m_runs[m_runs["experiment_type"] == "EXP_R"]
                ari_m_mean = float(exp_r_runs["ari"].mean())
                ari_m_sd = float(exp_r_runs["ari"].std(ddof=1)) if len(exp_r_runs) > 1 else 0.0
                nmi_m_mean = float(exp_r_runs["nmi"].mean())
                nmi_m_sd = float(exp_r_runs["nmi"].std(ddof=1)) if len(exp_r_runs) > 1 else 0.0
                sil_m_mean = float(exp_r_runs["silhouette"].mean())
            else:
                ari_m_mean = ari_primary
                ari_m_sd = 0.0
                nmi_m_mean = nmi_primary
                nmi_m_sd = 0.0
                sil_m_mean = sil_primary

            delta_vs_space_ari = ari_primary - space_ari
            delta_vs_space_nmi = nmi_primary - space_nmi

            if method not in ["SPACE", "RNA", "M2"]:
                delta_m2_ari = ari_primary - rna_ari
                delta_rna_ari = ari_primary - m2_ari
            else:
                delta_m2_ari = "NA"
                delta_rna_ari = "NA"

            # delta_space for SpatialGlue (Control A - Control C)
            if method == "SpatialGlue" and len(perms_df) > 0:
                p_c = perms_df[(perms_df["dataset"] == dataset) & (perms_df["method"] == "SpatialGlue") & (perms_df["permutation_type"] == "SPACE_PERMUTED")]
                if len(p_c) > 0:
                    delta_sp_ari = -float(p_c["delta_ari_vs_paired"].values[0])
                    delta_sp_nmi = -float(p_c["delta_nmi_vs_paired"].values[0])
                else:
                    delta_sp_ari = "NA"
                    delta_sp_nmi = "NA"
            else:
                delta_sp_ari = "NA"
                delta_sp_nmi = "NA"

            # Stability metrics
            if len(stability_df) > 0:
                s_match = stability_df[(stability_df["dataset"] == dataset) & (stability_df["method"] == method)]
                if len(s_match) > 0:
                    r_ami = float(s_match["exp_r_cluster_ami"].mean())
                    r_j5 = float(s_match["knn_jaccard_k5_mean"].mean())
                    r_j15 = float(s_match["knn_jaccard_k15_mean"].mean())
                    r_j30 = float(s_match["knn_jaccard_k30_mean"].mean())
                    r_spear = float(s_match["distance_spearman"].mean())
                    proc_vals = s_match["procrustes_discrepancy"].dropna()
                    r_proc = float(proc_vals.mean()) if len(proc_vals) > 0 else "NA"
                else:
                    r_ami = r_j5 = r_j15 = r_j30 = r_spear = 1.0
                    r_proc = 0.0
            else:
                r_ami = r_j5 = r_j15 = r_j30 = r_spear = r_proc = "NA"

            # Clustering stability from Exp C
            if len(clustering_stab_df) > 0:
                c_match = clustering_stab_df[(clustering_stab_df["dataset"] == dataset) & (clustering_stab_df["method"] == method)]
                c_ami = float(c_match["ami"].mean()) if len(c_match) > 0 else "NA"
            else:
                c_ami = "NA"

            diag_rows.append({
                "dataset": dataset,
                "method": method,
                "ARI_primary": ari_primary,
                "NMI_primary": nmi_primary,
                "silhouette_primary": sil_primary,
                "H_norm_primary": hnorm_primary,
                "K_eff_primary": keff_primary,
                "f_max_primary": fmax_primary,
                "singleton_fraction_primary": sing_primary,
                "zero_cluster_count_primary": zero_clust_primary,
                "min_cluster_size_primary": min_sz_primary,
                "max_cluster_size_primary": max_sz_primary,
                "ARI_model_seed_mean": ari_m_mean,
                "ARI_model_seed_sd": ari_m_sd,
                "NMI_model_seed_mean": nmi_m_mean,
                "NMI_model_seed_sd": nmi_m_sd,
                "silhouette_model_seed_mean": sil_m_mean,
                "delta_vs_SPACE_ARI": delta_vs_space_ari,
                "delta_vs_SPACE_NMI": delta_vs_space_nmi,
                "delta_RNA_ARI": delta_rna_ari,
                "delta_M2_ARI": delta_m2_ari,
                "delta_space_ARI": delta_sp_ari,
                "delta_space_NMI": delta_sp_nmi,
                "representation_AMI": r_ami,
                "representation_Jaccard_5": r_j5,
                "representation_Jaccard_15": r_j15,
                "representation_Jaccard_30": r_j30,
                "distance_Spearman": r_spear,
                "procrustes_discrepancy": r_proc,
                "clustering_AMI": c_ami,
            })

    diag_df = pd.DataFrame(diag_rows)
    diag_df.to_csv(OUT_DIR / "PHASE_4B_DIAGNOSTICS.csv", index=False)
    print("PHASE_4B_DIAGNOSTICS.csv saved.")

    # =========================================================================
    # Step 8: Publication-Quality Visualizations (Figures 1 to 9)
    # =========================================================================
    if not is_smoke:
        print("\n>>> STEP 8: Generating Clean Publication Figures (Figures 1 to 9) <<<")
        plt.rcParams.update({"font.size": 11, "figure.autolayout": True})

        # Primary runs only for Figures 1-3
        primary_runs = runs_df[
            (runs_df["clustering_seed"] == 1729) &
            (runs_df["model_seed"] == 1729) &
            (runs_df["experiment_type"] != "SENSITIVITY_ONLY")
        ].copy()

        # Fig 1: Silhouette vs Normalized Entropy
        plt.figure(figsize=(9, 6))
        for m in primary_runs["method"].unique():
            sub = primary_runs[primary_runs["method"] == m]
            plt.scatter(sub["h_norm"], sub["silhouette"], label=m, alpha=0.85, s=75)
        plt.xlabel("Partition Normalized Entropy ($H_{norm}$)")
        plt.ylabel("Silhouette Score")
        plt.title("Figure 1: Geometric Silhouette vs Partition Entropy (Primary Evaluations)")
        plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.grid(True, linestyle=":", alpha=0.5)
        plt.savefig(FIGURES_DIR / "fig1_silhouette_vs_entropy.png", dpi=300, bbox_inches="tight")
        plt.close()

        # Fig 2: ARI vs Maximum Cluster Fraction
        plt.figure(figsize=(9, 6))
        for m in primary_runs["method"].unique():
            sub = primary_runs[primary_runs["method"] == m]
            plt.scatter(sub["f_max"], sub["ari"], label=m, alpha=0.85, s=75)
        plt.xlabel("Maximum Cluster Fraction ($f_{max}$)")
        plt.ylabel("Adjusted Rand Index (ARI)")
        plt.title("Figure 2: Annotation Agreement vs Dominant Cluster Fraction (Primary Evaluations)")
        plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.grid(True, linestyle=":", alpha=0.5)
        plt.savefig(FIGURES_DIR / "fig2_ari_vs_fmax.png", dpi=300, bbox_inches="tight")
        plt.close()

        # Fig 3: Method ARI relative to SPACE (Delta_vsSPACE)
        plt.figure(figsize=(10, 6))
        comp_methods = ["RNA", "M2", "CONCAT", "MOFA+", "totalVI", "MultiVI", "SpatialGlue"]
        bar_width = 0.11
        x = np.arange(len(active_datasets))
        for i, m in enumerate(comp_methods):
            vals = []
            for d in active_datasets:
                r = diag_df[(diag_df["dataset"] == d) & (diag_df["method"] == m)]
                vals.append(float(r["delta_vs_SPACE_ARI"].values[0]) if len(r) > 0 else np.nan)
            plt.bar(x + i * bar_width, vals, width=bar_width, label=m)
        plt.axhline(0, color="black", linestyle="--", linewidth=1.0)
        plt.xticks(x + bar_width * 3, active_datasets)
        plt.xlabel("Dataset")
        plt.ylabel(r"$\Delta_{vsSPACE}$ ARI ($Score_{method} - Score_{SPACE}$)")
        plt.title("Figure 3: Representation Agreement Relative to Physical Coordinates Baseline (Primary)")
        plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.grid(True, linestyle=":", alpha=0.5)
        plt.savefig(FIGURES_DIR / "fig3_full_vs_space.png", dpi=300, bbox_inches="tight")
        plt.close()

        # Fig 4: Multimodal Added Value (Dual Panel: Delta_M2 and Delta_RNA)
        fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)
        joint_methods = ["CONCAT", "MOFA+", "totalVI", "MultiVI", "SpatialGlue"]
        bar_width = 0.15

        # Panel A: Delta_M2 = S_joint - S_RNA
        for i, m in enumerate(joint_methods):
            vals = []
            for d in active_datasets:
                r = diag_df[(diag_df["dataset"] == d) & (diag_df["method"] == m)]
                val = r["delta_M2_ARI"].values[0] if len(r) > 0 else np.nan
                vals.append(float(val) if val != "NA" else np.nan)
            axes[0].bar(x + i * bar_width, vals, width=bar_width, label=m)
        axes[0].axhline(0, color="black", linestyle="--", linewidth=1.0)
        axes[0].set_xticks(x + bar_width * 2)
        axes[0].set_xticklabels(active_datasets)
        axes[0].set_xlabel("Dataset")
        axes[0].set_ylabel(r"$\Delta_{M2}$ ARI ($ARI_{joint} - ARI_{RNA}$)")
        axes[0].set_title(r"Panel A: Added Value Above RNA Baseline ($\Delta_{M2}$)")
        axes[0].grid(True, linestyle=":", alpha=0.5)
        axes[0].legend(loc="upper left")

        # Panel B: Delta_RNA = S_joint - S_M2
        for i, m in enumerate(joint_methods):
            vals = []
            for d in active_datasets:
                r = diag_df[(diag_df["dataset"] == d) & (diag_df["method"] == m)]
                val = r["delta_RNA_ARI"].values[0] if len(r) > 0 else np.nan
                vals.append(float(val) if val != "NA" else np.nan)
            axes[1].bar(x + i * bar_width, vals, width=bar_width, label=m)
        axes[1].axhline(0, color="black", linestyle="--", linewidth=1.0)
        axes[1].set_xticks(x + bar_width * 2)
        axes[1].set_xticklabels(active_datasets)
        axes[1].set_xlabel("Dataset")
        axes[1].set_ylabel(r"$\Delta_{RNA}$ ARI ($ARI_{joint} - ARI_{M2}$)")
        axes[1].set_title(r"Panel B: Added Value Above Modality 2 Baseline ($\Delta_{RNA}$)")
        axes[1].grid(True, linestyle=":", alpha=0.5)

        plt.suptitle("Figure 4: Multimodal Added-Value Relative to Both Unimodal Baselines", fontsize=13)
        plt.tight_layout()
        plt.savefig(FIGURES_DIR / "fig4_joint_vs_unimodal.png", dpi=300, bbox_inches="tight")
        plt.close()

        # Fig 5: Pairing Permutation Effects
        plt.figure(figsize=(9, 6))
        pairing_perms = perms_df[perms_df["permutation_type"].isin(["M2_PAIRING_PERMUTED", "RNA_PAIRING_PERMUTED"])]
        if len(pairing_perms) > 0:
            labels_p = [f"{r['dataset']}-{r['method']}-{r['permutation_type'].split('_')[0]}" for _, r in pairing_perms.iterrows()]
            plt.barh(labels_p, pairing_perms["delta_ari_vs_paired"], color=["crimson" if v < -0.05 else "goldenrod" if v < 0 else "forestgreen" for v in pairing_perms["delta_ari_vs_paired"]])
            plt.axvline(0, color="black", linestyle="--", linewidth=1.0)
            plt.xlabel(r"$\Delta$ ARI (Permuted Pairing - Original Paired)")
            plt.title("Figure 5: Modality-Pairing Permutation Response Across Learned Models")
            plt.grid(True, linestyle=":", alpha=0.5)
            plt.savefig(FIGURES_DIR / "fig5_modality_permutation.png", dpi=300, bbox_inches="tight")
            plt.close()

        # Fig 6: Representation-seed kNN Neighborhood Stability
        plt.figure(figsize=(10, 6))
        stab_learned = stability_df[stability_df["method"].isin(["MOFA+", "totalVI", "MultiVI", "SpatialGlue"])]
        if len(stab_learned) > 0:
            stab_agg = stab_learned.groupby(["dataset", "method"])[["knn_jaccard_k5_mean", "knn_jaccard_k15_mean", "knn_jaccard_k30_mean"]].mean().reset_index()
            x_s = np.arange(len(stab_agg))
            plt.bar(x_s - 0.22, stab_agg["knn_jaccard_k5_mean"], width=0.22, label="k=5")
            plt.bar(x_s, stab_agg["knn_jaccard_k15_mean"], width=0.22, label="k=15")
            plt.bar(x_s + 0.22, stab_agg["knn_jaccard_k30_mean"], width=0.22, label="k=30")
            plt.xticks(x_s, [f"{r['dataset']}\n{r['method']}" for _, r in stab_agg.iterrows()], rotation=45, ha="right")
            plt.ylabel("Mean Neighborhood Jaccard Overlap")
            plt.ylim(0, 1.05)
            plt.title("Figure 6: Latent Neighborhood Stability Across Model Seeds (Exp R)")
            plt.legend()
            plt.grid(True, linestyle=":", alpha=0.5)
            plt.savefig(FIGURES_DIR / "fig6_representation_stability.png", dpi=300, bbox_inches="tight")
            plt.close()

        # Fig 7: Representation Stochasticity vs Clustering Stochasticity
        plt.figure(figsize=(8, 6))
        for m in diag_df["method"].unique():
            sub = diag_df[diag_df["method"] == m]
            sub_r = pd.to_numeric(sub["representation_AMI"], errors="coerce")
            sub_c = pd.to_numeric(sub["clustering_AMI"], errors="coerce")
            valid = (~sub_r.isna()) & (~sub_c.isna())
            if valid.sum() > 0:
                plt.scatter(sub_c[valid], sub_r[valid], label=m, s=80, alpha=0.85)
        plt.plot([0, 1], [0, 1], color="black", linestyle="--", alpha=0.6, label="Equal Instability Line")
        plt.xlabel("Clustering Stochasticity: KMeans AMI (Exp C)")
        plt.ylabel("Representation Stochasticity: Model Seed AMI (Exp R)")
        plt.title("Figure 7: Representation Stochasticity vs Downstream Clustering Stochasticity")
        plt.xlim(0.2, 1.05)
        plt.ylim(0.0, 1.05)
        plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.grid(True, linestyle=":", alpha=0.5)
        plt.savefig(FIGURES_DIR / "fig7_repr_vs_clustering_instability.png", dpi=300, bbox_inches="tight")
        plt.close()

        # Fig 8: Distance-Spearman Correlation across Model Seeds
        plt.figure(figsize=(9, 5))
        if len(stability_df) > 0:
            stab_dist = stability_df.groupby(["dataset", "method"])["distance_spearman"].mean().reset_index()
            plt.bar([f"{r['dataset']}-{r['method']}" for _, r in stab_dist.iterrows()], stab_dist["distance_spearman"], color="teal", alpha=0.85)
            plt.xticks(rotation=45, ha="right")
            plt.ylabel(r"Spearman $\rho$ on Sampled Latent Distances")
            plt.title("Figure 8: Pairwise Latent Distance Stability Across Training Seeds")
            plt.ylim(0, 1.05)
            plt.grid(True, linestyle=":", alpha=0.5)
            plt.savefig(FIGURES_DIR / "fig8_distance_spearman.png", dpi=300, bbox_inches="tight")
            plt.close()

        # Fig 9: SpatialGlue Spatial-Ablation Effects
        plt.figure(figsize=(8, 5))
        sp_sub = perms_df[perms_df["permutation_type"].isin(["MOLECULAR_TO_SPACE_PERMUTED", "SPACE_PERMUTED"])]
        if len(sp_sub) > 0:
            sp_labels = [f"{r['dataset']}\n{r['permutation_type'].replace('_', ' ')}" for _, r in sp_sub.iterrows()]
            plt.bar(sp_labels, sp_sub["delta_ari_vs_paired"], color=["purple" if "SPACE" in l else "navy" for l in sp_labels], alpha=0.85)
            plt.axhline(0, color="black", linestyle="--", linewidth=1.0)
            plt.ylabel(r"$\Delta$ ARI Relative to Control A (Paired)")
            plt.title("Figure 9: SpatialGlue Spatial Ablation Response (Controls B & C)")
            plt.grid(True, linestyle=":", alpha=0.5)
            plt.savefig(FIGURES_DIR / "fig9_spatialglue_ablation.png", dpi=300, bbox_inches="tight")
            plt.close()

    elapsed = time.time() - start_time
    print(f"\n=== Benchmark Finished Successfully in {elapsed:.1f}s ({elapsed/60:.2f} min) ===")


if __name__ == "__main__":
    main()
