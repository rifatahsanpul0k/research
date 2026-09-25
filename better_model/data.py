"""Barcode alignment and sparse preprocessing; never modifies source AnnData."""

from dataclasses import asdict, dataclass

import anndata as ad
import numpy as np
import pandas as pd
import scanpy as sc
from scipy import sparse
from sklearn.decomposition import PCA

from .config import PreprocessConfig


def align_modalities(rna, aux):
    for name, obj in (("RNA", rna), ("auxiliary", aux)):
        if not obj.obs_names.is_unique or obj.obs_names.hasnans:
            raise ValueError(f"{name} observation IDs must be unique and nonmissing")
    if set(rna.obs_names) != set(aux.obs_names):
        raise ValueError("Modalities must have exactly the same barcode set; no silent intersection")
    if rna.n_obs < 3:
        raise ValueError("At least three paired observations are required")
    rna, aux = rna.copy(), aux[rna.obs_names].copy()
    if "spatial" not in rna.obsm:
        raise ValueError("RNA requires obsm['spatial']")
    pos = np.asarray(rna.obsm["spatial"], dtype=np.float64)
    if pos.shape != (rna.n_obs, 2) or not np.isfinite(pos).all():
        raise ValueError("Spatial coordinates must be finite n x 2")
    if "spatial" in aux.obsm and not np.allclose(pos, aux.obsm["spatial"], rtol=0, atol=1e-6):
        raise ValueError("Paired modalities disagree on spatial coordinates after barcode alignment")
    return rna, aux


def align_annotations(frame, obs_names, column):
    if not frame.index.is_unique or frame.index.hasnans:
        raise ValueError("Annotation barcodes must be unique and nonmissing")
    if column not in frame:
        raise ValueError(f"Missing annotation column: {column}")
    if not pd.Index(obs_names).isin(frame.index).all():
        raise ValueError("Annotation table is missing observation barcodes")
    return frame.loc[obs_names, column].copy()


def checked_matrix(x, name):
    values = x.data if sparse.issparse(x) else np.asarray(x)
    if not np.isfinite(values).all() or np.any(values < 0):
        raise ValueError(f"{name} must contain finite, nonnegative input values")
    if min(x.shape) < 1 or not np.any(values > 0):
        raise ValueError(f"{name} has no usable measurements")
    return sparse.csr_matrix(x, dtype=np.float64)


def zscore(x):
    x = np.asarray(x, dtype=np.float64)
    mean = x.mean(axis=0)
    scale = x.std(axis=0, ddof=1)  # Scanpy's sample standard deviation.
    scale[scale < 1e-12] = 1.0
    return ((x - mean) / scale).astype(np.float32), mean, scale


@dataclass
class PreparedData:
    rna: np.ndarray
    aux: np.ndarray
    positions: np.ndarray
    # X is observed log-normalized RNA, never reconstructed/scaled expression.
    output: ad.AnnData
    transforms: dict
    metadata: dict


def preprocess(rna, aux, config: PreprocessConfig):
    config.validate()
    rna, aux = align_modalities(rna, aux)
    rna.X = checked_matrix(rna.X, "RNA")
    aux.X = checked_matrix(aux.X, config.aux_modality)
    zero_rows = {"rna": int(np.sum(np.asarray(rna.X.sum(axis=1)).ravel() == 0)),
                 "aux": int(np.sum(np.asarray(aux.X.sum(axis=1)).ravel() == 0))}
    # Keep duplicate display names traceable without changing features or row order.
    rna.var["source_feature_name"] = rna.var_names.astype(str)
    rna.var_names_make_unique()
    sc.pp.filter_genes(rna, min_cells=config.min_cells)
    if rna.n_vars < 2:
        raise ValueError("Fewer than two RNA genes survive min_cells")
    n_hvg = min(config.n_hvg, rna.n_vars)
    if config.hvg_flavor == "seurat_v3":
        sc.pp.highly_variable_genes(rna, flavor="seurat_v3", n_top_genes=n_hvg)
    if config.rna_input == "counts":
        sc.pp.normalize_total(rna, target_sum=1e4)
        sc.pp.log1p(rna)
    if config.hvg_flavor == "seurat":
        sc.pp.highly_variable_genes(rna, flavor="seurat", n_top_genes=n_hvg)
    # Densify ONLY the selected genes, unlike the reference's full RNA scaling.
    hvg = rna[:, rna.var["highly_variable"].to_numpy()].copy()
    if hvg.n_vars < 2:
        raise ValueError("HVG selection returned fewer than two genes")
    x_rna, rna_mean, rna_scale = zscore(hvg.X.toarray())
    transforms = {"rna_mean": rna_mean, "rna_scale": rna_scale,
                  "rna_features": hvg.var_names.to_numpy(dtype=str),
                  "aux_features": aux.var_names.to_numpy(dtype=str)}
    if config.aux_modality == "ADT":
        x = aux.X.toarray()
        geometric_mean = np.exp(np.log1p(x).mean(axis=1, keepdims=True))
        x_aux, mean, scale = zscore(np.log1p(x / (geometric_mean + 1e-12)))
        transforms.update(aux_mean=mean, aux_scale=scale)
        aux_recipe = "per-spot CLR, sample-standard-deviation scaling"
    else:
        # Same TF-IDF -> total-normalize -> log1p -> centered PCA as hello.py.
        # ARPACK centers implicitly, so a dense n_spots x n_peaks copy is unnecessary.
        x = aux.X
        idf = x.shape[0] / (np.asarray(x.sum(axis=0)).ravel() + 1e-12)
        row_sum = np.asarray(x.sum(axis=1)).ravel()
        x = x.multiply((1 / (row_sum + 1e-12))[:, None]).multiply(idf).tocsr()
        total = np.asarray(x.sum(axis=1)).ravel()
        x = x.multiply((1e4 / np.maximum(total, 1e-12))[:, None]).tocsr()
        x.data = np.log1p(x.data)
        n_comps = min(config.atac_components, min(x.shape) - 1)
        if n_comps < 1:
            raise ValueError("ATAC matrix is too small for PCA")
        pca = PCA(n_components=n_comps, svd_solver="arpack", random_state=config.preprocessing_seed)
        x_aux = pca.fit_transform(x).astype(np.float32)
        transforms.update(atac_idf=idf, atac_pca_mean=pca.mean_, atac_pca_components=pca.components_)
        aux_recipe = "reference TF-IDF, total=1e4, log1p, centered sparse ARPACK PCA"
    if not np.isfinite(x_rna).all() or not np.isfinite(x_aux).all():
        raise FloatingPointError("Preprocessing produced nonfinite features")
    hvg.layers["scaled_input"] = x_rna.copy()
    return PreparedData(x_rna, x_aux, np.asarray(rna.obsm["spatial"]), hvg, transforms,
                        {"config": asdict(config), "fit_scope": "all paired spots; transductive",
                         "zero_input_rows": zero_rows, "aux_recipe": aux_recipe,
                         "rna_shape": list(x_rna.shape), "aux_shape": list(x_aux.shape)})
