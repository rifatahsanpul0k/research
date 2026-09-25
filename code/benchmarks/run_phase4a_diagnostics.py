"""Phase 4A Diagnostic Screening Experiment.

Evaluates four core diagnostic hypotheses:
H1: Cluster degeneracy fools geometric metrics (high silhouette / low entropy).
H2: Spatial baseline dominance (SPACE vs multimodal).
H3: Modality contribution (unimodal ablation and cross-modal permutation).
H4: Seed stability (representation vs clustering variance across seeds).
"""

from __future__ import annotations

import csv
import json
import os
import sys
from pathlib import Path

# Set thread parallelism before importing numpy/torch
for var in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[var] = "1"

import numpy as np
import pandas as pd
import scipy.sparse as sp
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_mutual_info_score, adjusted_rand_score, normalized_mutual_info_score, silhouette_score
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "external/SpatialGlue"))

import anndata as ad
import torch

from SpatialGlue.preprocess import construct_neighbor_graph
from SpatialGlue.SpatialGlue_pyG import Train_SpatialGlue

EXPERIMENT_ROOT = ROOT / "08_experiments"
PHASE4A_DIR = EXPERIMENT_ROOT / "phase4a_diagnostics"
FIGURES_DIR = PHASE4A_DIR / "figures"
ARTIFACTS_DIR = PHASE4A_DIR / "artifacts"
SEEDS = (1729, 2718, 31415)


def compute_cluster_diagnostics(labels: np.ndarray, representation: np.ndarray, ref_labels: np.ndarray) -> dict:
    """Compute all H1 cluster pathology and evaluation metrics."""
    n_obs = len(labels)
    unique_clusters, counts = np.unique(labels, return_counts=True)
    k = len(unique_clusters)
    p_k = counts / n_obs
    
    f_max = float(np.max(p_k))
    min_size = int(np.min(counts))
    singletons = int(np.sum(counts == 1))
    singleton_fraction = float(singletons / k) if k > 0 else 0.0
    
    # Entropy
    entropy = -float(np.sum(p_k * np.log(p_k + 1e-12)))
    max_entropy = np.log(k) if k > 1 else 1.0
    h_norm = float(entropy / max_entropy)
    k_eff = float(np.exp(entropy))
    
    ari = float(adjusted_rand_score(ref_labels, labels))
    nmi = float(normalized_mutual_info_score(ref_labels, labels, average_method="arithmetic"))
    
    # Silhouette (sampled at 500 for consistency with Phase 3C baseline convention)
    try:
        if k > 1 and k < n_obs:
            sample_size = min(500, n_obs)
            sil = float(silhouette_score(representation, labels, metric="euclidean", sample_size=sample_size, random_state=0))
        else:
            sil = float("nan")
    except Exception:
        sil = float("nan")
        
    return {
        "n_obs": n_obs,
        "k": k,
        "k_eff": k_eff,
        "f_max": f_max,
        "h_norm": h_norm,
        "entropy": entropy,
        "min_size": min_size,
        "singletons": singletons,
        "singleton_fraction": singleton_fraction,
        "counts": {str(c): int(cnt) for c, cnt in zip(unique_clusters, counts)},
        "ari": ari,
        "nmi": nmi,
        "silhouette": sil,
    }


def compute_neighborhood_jaccard(emb1: np.ndarray, emb2: np.ndarray, k: int = 15) -> float:
    """Compute mean pairwise neighborhood Jaccard index between two representations."""
    nn1 = NearestNeighbors(n_neighbors=k + 1).fit(emb1)
    nn2 = NearestNeighbors(n_neighbors=k + 1).fit(emb2)
    
    # Exclude self
    indices1 = nn1.kneighbors(return_distance=False)[:, 1:]
    indices2 = nn2.kneighbors(return_distance=False)[:, 1:]
    
    jaccards = []
    for i in range(len(emb1)):
        set1 = set(indices1[i])
        set2 = set(indices2[i])
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        jaccards.append(intersection / union if union > 0 else 0.0)
        
    return float(np.mean(jaccards))


def load_phase3c_run(dataset: str, baseline: str, seed: int) -> dict:
    """Load representation, clusters, and ground truth from frozen Phase 3C run."""
    slug_map = {
        "LN_A1": ("EXP-LN-A1", "04_datasets/10x_human_lymph_node_A1/raw/annotation.csv", "manual-anno"),
        "MB_E13": ("EXP-MB-E13", "04_datasets/Mouse_Brain_E13_S1/raw/anno.csv", "cluster"),
    }
    prefix, ref_path, label_col = slug_map[dataset]
    exp_id = f"{prefix}-{baseline}-KMEANS-S{seed}"
    exp_dir = EXPERIMENT_ROOT / exp_id
    
    if not exp_dir.exists():
        raise FileNotFoundError(f"Missing Phase 3C run: {exp_dir}")
        
    embedding = np.load(exp_dir / "embedding.npz")["embedding"]
    clusters_df = pd.read_csv(exp_dir / "clusters.csv")
    cluster_labels = clusters_df["cluster"].values
    
    ref_df = pd.read_csv(ROOT / ref_path)
    ref_labels = ref_df[label_col].values
    
    return {
        "exp_id": exp_id,
        "dataset": dataset,
        "baseline": baseline,
        "seed": seed,
        "embedding": embedding,
        "clusters": cluster_labels,
        "ref_labels": ref_labels,
    }


def run_spatialglue(adata1: ad.AnnData, adata2: ad.AnnData, seed: int, datatype: str = "SPOTS", n_neighbors: int = 3, epochs: int = 600) -> np.ndarray:
    """Train SpatialGlue on paired spatial omics AnnData objects."""
    torch.manual_seed(seed)
    np.random.seed(seed)
    
    data = construct_neighbor_graph(adata1, adata2, datatype=datatype, n_neighbors=n_neighbors)
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
    emb = output["SpatialGlue"]
    return emb


def main() -> None:
    print("=== STARTING PHASE 4A DIAGNOSTIC SCREENING EXPERIMENT ===")
    
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    (ARTIFACTS_DIR / "cluster_sizes").mkdir(parents=True, exist_ok=True)
    (ARTIFACTS_DIR / "neighborhood_stability").mkdir(parents=True, exist_ok=True)
    (ARTIFACTS_DIR / "permutations").mkdir(parents=True, exist_ok=True)
    
    datasets = ["LN_A1", "MB_E13"]
    transparent_baselines = {
        "LN_A1": ["SPACE", "PCA", "ADT", "CONCAT"],
        "MB_E13": ["SPACE", "PCA", "ATAC", "CONCAT"],
    }
    
    all_runs = []
    
    # 1. Evaluate frozen Phase 3C runs
    print("\n--- Step 1: Processing Frozen Phase 3C Runs ---")
    for dataset in datasets:
        for baseline in transparent_baselines[dataset]:
            for seed in SEEDS:
                run_data = load_phase3c_run(dataset, baseline, seed)
                diag = compute_cluster_diagnostics(run_data["clusters"], run_data["embedding"], run_data["ref_labels"])
                
                record = {
                    "experiment_id": run_data["exp_id"],
                    "dataset": dataset,
                    "method": baseline,
                    "seed": seed,
                    "is_spatial": baseline in ["SPACE", "SpatialGlue"],
                    **diag,
                }
                all_runs.append(record)
                
                # Save cluster size artifact
                with open(ARTIFACTS_DIR / "cluster_sizes" / f"{run_data['exp_id']}_cluster_sizes.json", "w") as f:
                    json.dump(diag["counts"], f, indent=2)
                    
                print(f"[{dataset}][{baseline}][S{seed}] ARI: {diag['ari']:.4f}, NMI: {diag['nmi']:.4f}, Sil: {diag['silhouette']:.4f}, H_norm: {diag['h_norm']:.4f}, f_max: {diag['f_max']:.4f}, Singletons: {diag['singletons']}")

    # 2. Run SpatialGlue on LN_A1 and MB_E13
    print("\n--- Step 2: Executing SpatialGlue Across Project Seeds ---")
    sg_embeddings = {}
    
    for dataset in datasets:
        sg_embeddings[dataset] = {}
        # Prepare inputs
        pca_ref = load_phase3c_run(dataset, "PCA", 1729)["embedding"]
        m2_code = "ADT" if dataset == "LN_A1" else "ATAC"
        m2_ref = load_phase3c_run(dataset, m2_code, 1729)["embedding"]
        space_ref = load_phase3c_run(dataset, "SPACE", 1729)["embedding"]
        ref_labels = load_phase3c_run(dataset, "PCA", 1729)["ref_labels"]
        k_clusters = len(np.unique(ref_labels))
        
        datatype = "SPOTS" if dataset == "LN_A1" else "Spatial-epigenome-transcriptome"
        n_neighbors = 3 if dataset == "LN_A1" else 6
        
        for seed in SEEDS:
            exp_id = f"EXP-{dataset.replace('_', '-')}-SPATIALGLUE-KMEANS-S{seed}"
            print(f"Training SpatialGlue: {exp_id}...")
            
            adata1 = ad.AnnData(X=pca_ref.copy())
            adata1.obsm["feat"] = pca_ref.copy()
            adata1.obsm["spatial"] = space_ref.copy()
            
            adata2 = ad.AnnData(X=m2_ref.copy())
            adata2.obsm["feat"] = m2_ref.copy()
            adata2.obsm["spatial"] = space_ref.copy()
            
            emb = run_spatialglue(adata1, adata2, seed=seed, datatype=datatype, n_neighbors=n_neighbors, epochs=600)
            sg_embeddings[dataset][seed] = emb
            
            # Downstream KMeans clustering using seed
            km = KMeans(n_clusters=k_clusters, n_init=20, random_state=seed)
            clusters = km.fit_predict(emb)
            
            diag = compute_cluster_diagnostics(clusters, emb, ref_labels)
            record = {
                "experiment_id": exp_id,
                "dataset": dataset,
                "method": "SpatialGlue",
                "seed": seed,
                "is_spatial": True,
                **diag,
            }
            all_runs.append(record)
            
            # Save cluster sizes and embedding
            np.savez_compressed(ARTIFACTS_DIR / f"{exp_id}_embedding.npz", embedding=emb)
            with open(ARTIFACTS_DIR / "cluster_sizes" / f"{exp_id}_cluster_sizes.json", "w") as f:
                json.dump(diag["counts"], f, indent=2)
                
            print(f"[{dataset}][SpatialGlue][S{seed}] ARI: {diag['ari']:.4f}, NMI: {diag['nmi']:.4f}, Sil: {diag['silhouette']:.4f}, H_norm: {diag['h_norm']:.4f}, f_max: {diag['f_max']:.4f}, Singletons: {diag['singletons']}")

    # 3. Permutation Controls for H2 and H3 on MB_E13
    print("\n--- Step 3: Executing Permutation Controls for H2 and H3 on MB_E13 ---")
    e13_pca = load_phase3c_run("MB_E13", "PCA", 1729)["embedding"]
    e13_atac = load_phase3c_run("MB_E13", "ATAC", 1729)["embedding"]
    e13_space = load_phase3c_run("MB_E13", "SPACE", 1729)["embedding"]
    e13_ref = load_phase3c_run("MB_E13", "PCA", 1729)["ref_labels"]
    n_spots = len(e13_ref)
    k_e13 = len(np.unique(e13_ref))
    
    perm_records = []
    
    # Control A: True Molecular + True Space (SpatialGlue already run)
    # Control B: Randomized Molecular + True Space
    np.random.seed(42)
    rand_pca = e13_pca[np.random.permutation(n_spots)]
    rand_atac = e13_atac[np.random.permutation(n_spots)]
    
    adata1_rand = ad.AnnData(X=rand_pca.copy())
    adata1_rand.obsm["feat"] = rand_pca.copy()
    adata1_rand.obsm["spatial"] = e13_space.copy()
    
    adata2_rand = ad.AnnData(X=rand_atac.copy())
    adata2_rand.obsm["feat"] = rand_atac.copy()
    adata2_rand.obsm["spatial"] = e13_space.copy()
    
    print("Running Control B: Randomized Molecular + True Coordinates...")
    emb_ctrl_b = run_spatialglue(adata1_rand, adata2_rand, seed=1729, datatype="Spatial-epigenome-transcriptome", n_neighbors=6, epochs=600)
    km_b = KMeans(n_clusters=k_e13, n_init=20, random_state=1729).fit_predict(emb_ctrl_b)
    diag_b = compute_cluster_diagnostics(km_b, emb_ctrl_b, e13_ref)
    perm_records.append({"control": "Control_B_RandomMol_TrueSpace", **diag_b})
    print(f"[Control B] ARI: {diag_b['ari']:.4f}, NMI: {diag_b['nmi']:.4f}")
    
    # Control C: True Molecular + Permuted Coordinates
    perm_space = e13_space[np.random.permutation(n_spots)]
    adata1_perm_sp = ad.AnnData(X=e13_pca.copy())
    adata1_perm_sp.obsm["feat"] = e13_pca.copy()
    adata1_perm_sp.obsm["spatial"] = perm_space.copy()
    
    adata2_perm_sp = ad.AnnData(X=e13_atac.copy())
    adata2_perm_sp.obsm["feat"] = e13_atac.copy()
    adata2_perm_sp.obsm["spatial"] = perm_space.copy()
    
    print("Running Control C: True Molecular + Permuted Coordinates...")
    emb_ctrl_c = run_spatialglue(adata1_perm_sp, adata2_perm_sp, seed=1729, datatype="Spatial-epigenome-transcriptome", n_neighbors=6, epochs=600)
    km_c = KMeans(n_clusters=k_e13, n_init=20, random_state=1729).fit_predict(emb_ctrl_c)
    diag_c = compute_cluster_diagnostics(km_c, emb_ctrl_c, e13_ref)
    perm_records.append({"control": "Control_C_TrueMol_PermSpace", **diag_c})
    print(f"[Control C] ARI: {diag_c['ari']:.4f}, NMI: {diag_c['nmi']:.4f}")
    
    # H3 Modality Permutation Controls on CONCAT:
    # True CONCAT
    true_concat = np.hstack([e13_pca, e13_atac])
    km_cat = KMeans(n_clusters=k_e13, n_init=20, random_state=1729).fit_predict(true_concat)
    diag_cat = compute_cluster_diagnostics(km_cat, true_concat, e13_ref)
    perm_records.append({"control": "True_CONCAT", **diag_cat})
    
    # RNA intact, ATAC permuted
    perm_atac_concat = np.hstack([e13_pca, e13_atac[np.random.permutation(n_spots)]])
    km_perm_atac = KMeans(n_clusters=k_e13, n_init=20, random_state=1729).fit_predict(perm_atac_concat)
    diag_perm_atac = compute_cluster_diagnostics(km_perm_atac, perm_atac_concat, e13_ref)
    perm_records.append({"control": "RNA_Intact_ATAC_Permuted_CONCAT", **diag_perm_atac})
    print(f"[RNA Intact + ATAC Permuted CONCAT] ARI: {diag_perm_atac['ari']:.4f}, NMI: {diag_perm_atac['nmi']:.4f}")
    
    # RNA permuted, ATAC intact
    perm_rna_concat = np.hstack([e13_pca[np.random.permutation(n_spots)], e13_atac])
    km_perm_rna = KMeans(n_clusters=k_e13, n_init=20, random_state=1729).fit_predict(perm_rna_concat)
    diag_perm_rna = compute_cluster_diagnostics(km_perm_rna, perm_rna_concat, e13_ref)
    perm_records.append({"control": "RNA_Permuted_ATAC_Intact_CONCAT", **diag_perm_rna})
    print(f"[RNA Permuted + ATAC Intact CONCAT] ARI: {diag_perm_rna['ari']:.4f}, NMI: {diag_perm_rna['nmi']:.4f}")
    
    pd.DataFrame(perm_records).to_csv(ARTIFACTS_DIR / "permutations" / "permutation_controls_E13.csv", index=False)

    # 4. Save Runs and Diagnostics
    runs_df = pd.DataFrame(all_runs)
    runs_df.to_csv(PHASE4A_DIR / "PHASE_4A_RUNS.csv", index=False)
    
    # Compute Aggregates & Stability Diagnostics
    print("\n--- Step 4: Computing Summary Diagnostics & Stability ---")
    summary_rows = []
    
    for (dataset, method), group in runs_df.groupby(["dataset", "method"]):
        ari_mean, ari_sd = float(group["ari"].mean()), float(group["ari"].std())
        nmi_mean, nmi_sd = float(group["nmi"].mean()), float(group["nmi"].std())
        sil_mean, sil_sd = float(group["silhouette"].mean()), float(group["silhouette"].std())
        f_max_mean = float(group["f_max"].mean())
        h_norm_mean = float(group["h_norm"].mean())
        singletons_mean = float(group["singletons"].mean())
        
        # Stability across the 3 seeds
        # Pairwise AMI
        clusters_by_seed = [group[group["seed"] == s]["counts"].values for s in SEEDS]
        # Re-fetch cluster assignments
        clusters_list = []
        embeddings_list = []
        for s in SEEDS:
            if method == "SpatialGlue":
                emb = sg_embeddings[dataset][s]
                k_cl = len(np.unique(load_phase3c_run(dataset, "PCA", 1729)["ref_labels"]))
                cl = KMeans(n_clusters=k_cl, n_init=20, random_state=s).fit_predict(emb)
            else:
                p3c = load_phase3c_run(dataset, method, s)
                emb = p3c["embedding"]
                cl = p3c["clusters"]
            clusters_list.append(cl)
            embeddings_list.append(emb)
            
        ami_01 = adjusted_mutual_info_score(clusters_list[0], clusters_list[1])
        ami_02 = adjusted_mutual_info_score(clusters_list[0], clusters_list[2])
        ami_12 = adjusted_mutual_info_score(clusters_list[1], clusters_list[2])
        mean_ami = float(np.mean([ami_01, ami_02, ami_12]))
        
        # Neighborhood Jaccard
        jacc_01 = compute_neighborhood_jaccard(embeddings_list[0], embeddings_list[1], k=15)
        jacc_02 = compute_neighborhood_jaccard(embeddings_list[0], embeddings_list[2], k=15)
        jacc_12 = compute_neighborhood_jaccard(embeddings_list[1], embeddings_list[2], k=15)
        mean_jacc = float(np.mean([jacc_01, jacc_02, jacc_12]))
        
        summary_rows.append({
            "dataset": dataset,
            "method": method,
            "ari_mean": ari_mean,
            "ari_sd": ari_sd,
            "nmi_mean": nmi_mean,
            "nmi_sd": nmi_sd,
            "silhouette_mean": sil_mean,
            "silhouette_sd": sil_sd,
            "f_max_mean": f_max_mean,
            "h_norm_mean": h_norm_mean,
            "singletons_mean": singletons_mean,
            "pairwise_cluster_ami_mean": mean_ami,
            "neighborhood_jaccard_mean": mean_jacc,
        })
        
    diag_df = pd.DataFrame(summary_rows)
    
    # Compute Delta Molecular and Delta Modality
    diag_df["delta_molecular_ari"] = float("nan")
    diag_df["delta_molecular_nmi"] = float("nan")
    diag_df["delta_m2_ari"] = float("nan")
    diag_df["delta_rna_ari"] = float("nan")
    
    for dataset in datasets:
        space_ari = diag_df[(diag_df["dataset"] == dataset) & (diag_df["method"] == "SPACE")]["ari_mean"].values[0]
        space_nmi = diag_df[(diag_df["dataset"] == dataset) & (diag_df["method"] == "SPACE")]["nmi_mean"].values[0]
        rna_ari = diag_df[(diag_df["dataset"] == dataset) & (diag_df["method"] == "PCA")]["ari_mean"].values[0]
        m2_name = "ADT" if dataset == "LN_A1" else "ATAC"
        m2_ari = diag_df[(diag_df["dataset"] == dataset) & (diag_df["method"] == m2_name)]["ari_mean"].values[0]
        
        mask = diag_df["dataset"] == dataset
        diag_df.loc[mask, "delta_molecular_ari"] = diag_df.loc[mask, "ari_mean"] - space_ari
        diag_df.loc[mask, "delta_molecular_nmi"] = diag_df.loc[mask, "nmi_mean"] - space_nmi
        
        for m in ["CONCAT", "SpatialGlue"]:
            m_mask = (diag_df["dataset"] == dataset) & (diag_df["method"] == m)
            diag_df.loc[m_mask, "delta_m2_ari"] = diag_df.loc[m_mask, "ari_mean"] - rna_ari
            diag_df.loc[m_mask, "delta_rna_ari"] = diag_df.loc[m_mask, "ari_mean"] - m2_ari

    diag_df.to_csv(PHASE4A_DIR / "PHASE_4A_DIAGNOSTICS.csv", index=False)
    print("\nSummary Diagnostics:\n", diag_df[["dataset", "method", "ari_mean", "silhouette_mean", "f_max_mean", "h_norm_mean", "delta_molecular_ari", "pairwise_cluster_ami_mean"]])

    # 5. Generate Visualizations
    print("\n--- Step 5: Generating Stage A Visualizations ---")
    sns.set_theme(style="whitegrid", font_scale=1.1)
    
    # Plot 1: Silhouette vs Normalized Cluster Entropy
    fig, ax = plt.subplots(figsize=(8, 6))
    for dataset, marker in zip(["LN_A1", "MB_E13"], ["o", "s"]):
        sub = runs_df[runs_df["dataset"] == dataset]
        sns.scatterplot(
            data=sub,
            x="h_norm",
            y="silhouette",
            hue="method",
            style="dataset",
            s=120,
            ax=ax,
            legend="brief",
        )
    ax.axvline(0.6, color="red", linestyle="--", alpha=0.5, label="Entropy Warning (0.6)")
    ax.set_title("Plot 1: Silhouette vs Normalized Cluster Entropy (H1 Degeneracy Test)")
    ax.set_xlabel("Normalized Cluster Entropy (H_norm: 0=Degenerate, 1=Balanced)")
    ax.set_ylabel("Average Silhouette Width")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "silhouette_vs_entropy.png", dpi=300)
    plt.close()
    
    # Plot 2: ARI vs Maximum Cluster Fraction
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
        data=runs_df,
        x="f_max",
        y="ari",
        hue="method",
        style="dataset",
        s=120,
        ax=ax,
    )
    ax.set_title("Plot 2: ARI vs Maximum Cluster Fraction (f_max)")
    ax.set_xlabel("Maximum Cluster Fraction (f_max)")
    ax.set_ylabel("Adjusted Rand Index (ARI)")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "ari_vs_max_cluster_fraction.png", dpi=300)
    plt.close()
    
    # Plot 3: Space Baseline Comparison (Delta Molecular ARI)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(
        data=diag_df[diag_df["method"] != "SPACE"],
        x="method",
        y="delta_molecular_ari",
        hue="dataset",
        ax=ax,
    )
    ax.axhline(0, color="black", linestyle="--")
    ax.set_title("Plot 3: Delta Molecular ARI relative to SPACE Baseline (H2 Test)")
    ax.set_ylabel("Delta ARI (Method - SPACE)")
    ax.set_xlabel("Method")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "space_baseline_comparison.png", dpi=300)
    plt.close()
    
    # Plot 4: Joint vs Unimodal Modality Contribution
    fig, ax = plt.subplots(figsize=(8, 5))
    mod_contrib = diag_df[diag_df["method"].isin(["CONCAT", "SpatialGlue"])][["dataset", "method", "delta_m2_ari", "delta_rna_ari"]]
    mod_melted = pd.melt(mod_contrib, id_vars=["dataset", "method"], value_vars=["delta_m2_ari", "delta_rna_ari"], var_name="contrast", value_name="delta_ari")
    mod_melted["contrast"] = mod_melted["contrast"].replace({"delta_m2_ari": "Gain over RNA (Delta M2)", "delta_rna_ari": "Gain over M2 (Delta RNA)"})
    
    sns.barplot(data=mod_melted, x="method", y="delta_ari", hue="contrast", ax=ax)
    ax.axhline(0, color="black", linestyle="--")
    ax.set_title("Plot 4: Multimodal Incremental Contribution (H3 Test)")
    ax.set_ylabel("Incremental ARI Gain")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "modality_contribution.png", dpi=300)
    plt.close()
    
    # Plot 5: Seed Stability (Pairwise AMI)
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=diag_df, x="method", y="pairwise_cluster_ami_mean", hue="dataset", ax=ax)
    ax.set_ylim(0, 1.05)
    ax.set_title("Plot 5: Cluster Assignment Stability Across Seeds (Pairwise AMI) (H4 Test)")
    ax.set_ylabel("Mean Pairwise AMI Across Seeds")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "seed_stability.png", dpi=300)
    plt.close()
    
    # Plot 6: Spatial Maps for E13
    fig, axes = plt.subplots(1, 5, figsize=(25, 5))
    e13_coords = load_phase3c_run("MB_E13", "SPACE", 1729)["embedding"]
    
    maps_data = [
        ("Reference Annotation", load_phase3c_run("MB_E13", "PCA", 1729)["ref_labels"]),
        ("SPACE Baseline", load_phase3c_run("MB_E13", "SPACE", 1729)["clusters"]),
        ("ATAC-only (Pathological)", load_phase3c_run("MB_E13", "ATAC", 1729)["clusters"]),
        ("CONCAT", load_phase3c_run("MB_E13", "CONCAT", 1729)["clusters"]),
        ("SpatialGlue", KMeans(n_clusters=k_e13, n_init=20, random_state=1729).fit_predict(sg_embeddings["MB_E13"][1729])),
    ]
    
    for ax_idx, (title, cl_labels) in enumerate(maps_data):
        ax_map = axes[ax_idx]
        scatter = ax_map.scatter(e13_coords[:, 0], e13_coords[:, 1], c=pd.Categorical(cl_labels).codes, cmap="tab20", s=18, alpha=0.9)
        ax_map.set_title(title, fontsize=13, fontweight="bold")
        ax_map.set_xticks([])
        ax_map.set_yticks([])
        ax_map.set_aspect("equal")
        
    plt.suptitle("Plot 6: E13 Spatial Cluster Maps (Ground Truth vs Baselines vs SpatialGlue)", fontsize=16)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "spatial_maps.png", dpi=300)
    plt.close()
    
    print("\n=== STAGE A EXPERIMENTAL EXECUTION COMPLETE ===")


if __name__ == "__main__":
    main()
