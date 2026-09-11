"""Frozen transparent Phase 3C preprocessing and representations."""

from __future__ import annotations

import hashlib
import math

import numpy as np
from scipy import sparse
from sklearn.decomposition import PCA, TruncatedSVD


def _validate_nonnegative_finite(matrix: sparse.spmatrix) -> None:
    data = matrix.data
    if not np.isfinite(data).all():
        raise ValueError("source matrix contains non-finite stored values")
    if np.any(data < 0):
        raise ValueError("source matrix contains negative values")


def zscore_columns(matrix: np.ndarray) -> np.ndarray:
    values = np.asarray(matrix, dtype=np.float64)
    mean = values.mean(axis=0)
    scale = values.std(axis=0, ddof=0)
    safe = np.where(scale > 0, scale, 1.0)
    result = (values - mean) / safe
    result[:, scale == 0] = 0.0
    return result


def rna_representation(matrix: sparse.csr_matrix, feature_ids: list[str], n_features: int = 2000) -> tuple[np.ndarray, dict[str, object]]:
    _validate_nonnegative_finite(matrix)
    logged = matrix.copy().astype(np.float64)
    logged.data = np.log1p(logged.data)
    mean = np.asarray(logged.mean(axis=0)).ravel()
    second = np.asarray(logged.power(2).mean(axis=0)).ravel()
    variance = np.maximum(second - mean * mean, 0.0)
    count = min(n_features, matrix.shape[1])
    positions = np.lexsort((np.arange(matrix.shape[1]), -variance))[:count]
    dense = logged[:, positions].toarray()
    representation = zscore_columns(dense)
    selected = [feature_ids[int(i)] for i in positions]
    metadata = {
        "source_semantics": "SOURCE_PROVIDED_PROCESSED_X_COUNT_SEMANTICS_UNKNOWN",
        "library_size_normalization": False,
        "transform": "log1p_on_stored_nonzero_values",
        "feature_selection": "top_population_variance_after_log1p_stable_position_ties",
        "requested_features": n_features,
        "selected_features": count,
        "selected_positions": [int(i) for i in positions],
        "selected_feature_ids": selected,
        "selected_feature_ids_sha256": hashlib.sha256(("\n".join(selected) + "\n").encode()).hexdigest(),
        "scaling": "feature_population_zscore_constant_to_zero",
    }
    return representation, metadata


def adt_representation(matrix: sparse.csr_matrix, feature_ids: list[str]) -> tuple[np.ndarray, dict[str, object]]:
    _validate_nonnegative_finite(matrix)
    dense = matrix.toarray().astype(np.float64, copy=False)
    geometric = np.exp(np.log1p(dense).mean(axis=1, keepdims=True))
    clr = np.log1p(dense / geometric)
    representation = zscore_columns(clr)
    return representation, {
        "source_semantics": "SOURCE_PROVIDED_PROCESSED_X_COUNT_SEMANTICS_UNKNOWN",
        "transform": "per_observation_CLR_log1p_ratio",
        "clr_geometric_mean": "exp(mean(log1p(x)))_across_features",
        "features": len(feature_ids),
        "feature_ids_sha256": hashlib.sha256(("\n".join(feature_ids) + "\n").encode()).hexdigest(),
        "scaling": "feature_population_zscore_constant_to_zero",
    }


def atac_representation(matrix: sparse.csr_matrix, feature_ids: list[str]) -> tuple[np.ndarray, dict[str, object]]:
    _validate_nonnegative_finite(matrix)
    values = matrix.copy().astype(np.float64)
    row_sum = np.asarray(values.sum(axis=1)).ravel()
    inverse = np.zeros_like(row_sum)
    inverse[row_sum > 0] = 1.0 / row_sum[row_sum > 0]
    tf = sparse.diags(inverse) @ values
    document_frequency = np.asarray((values > 0).sum(axis=0)).ravel()
    idf = np.log1p(values.shape[0] / (1.0 + document_frequency))
    tfidf = tf.multiply(idf).tocsr()
    svd = TruncatedSVD(n_components=31, algorithm="randomized", n_iter=7, random_state=0, tol=0.0)
    all_components = svd.fit_transform(tfidf)
    representation = zscore_columns(all_components[:, 1:31])
    return representation, {
        "source_semantics": "SOURCE_PROVIDED_PROCESSED_X_FRAGMENT_SEMANTICS_UNKNOWN",
        "transform": "TF=X/row_sum; IDF=log1p(n/(1+document_frequency)); T=TF*IDF",
        "zero_sum_rows": int(np.count_nonzero(row_sum == 0)),
        "lsi": {"implementation": "sklearn.decomposition.TruncatedSVD", "components_fit": 31, "component_dropped": 1, "components_kept": 30, "algorithm": "randomized", "n_iter": 7, "random_state": 0, "tol": 0.0},
        "features": len(feature_ids),
        "feature_ids_sha256": hashlib.sha256(("\n".join(feature_ids) + "\n").encode()).hexdigest(),
        "scaling": "LSI_component_population_zscore_constant_to_zero",
    }


def pca_representation(rna: np.ndarray) -> tuple[np.ndarray, dict[str, object]]:
    model = PCA(n_components=30, svd_solver="randomized", whiten=False, random_state=0,
                n_oversamples=10, iterated_power=4, power_iteration_normalizer="QR")
    representation = model.fit_transform(rna)
    return representation, {
        "input": "frozen_BASE_RNA_representation",
        "implementation": "sklearn.decomposition.PCA",
        "n_components": 30,
        "svd_solver": "randomized",
        "centered": True,
        "whiten": False,
        "random_state": 0,
        "n_oversamples": 10,
        "iterated_power": 4,
        "power_iteration_normalizer": "QR",
        "explained_variance_ratio_sum": float(model.explained_variance_ratio_.sum()),
    }


def coordinate_representation(coordinates: np.ndarray) -> tuple[np.ndarray, dict[str, object]]:
    if coordinates.ndim != 2 or coordinates.shape[1] != 2 or not np.isfinite(coordinates).all():
        raise ValueError("coordinates must be finite n x 2")
    return zscore_columns(coordinates), {
        "coordinate_units": "UNKNOWN",
        "transform": "column_population_zscore_constant_to_zero",
        "physical_unit_conversion": False,
    }


def concatenate_equal_blocks(first: np.ndarray, second: np.ndarray) -> tuple[np.ndarray, dict[str, object]]:
    if first.shape[0] != second.shape[0]:
        raise ValueError("concatenation blocks have different observation counts")
    norms = [float(np.linalg.norm(first)), float(np.linalg.norm(second))]
    if any(value == 0 for value in norms):
        raise ValueError("cannot scale a zero Frobenius-norm block")
    factors = [math.sqrt(first.shape[0]) / (math.sqrt(2.0) * value) for value in norms]
    representation = np.concatenate((first * factors[0], second * factors[1]), axis=1)
    return representation, {
        "fusion": "column_concatenation",
        "learned_weighting": False,
        "block_dimensions": [int(first.shape[1]), int(second.shape[1])],
        "block_frobenius_norms_before": norms,
        "block_scale_factors": factors,
        "target_mean_squared_row_norm_per_block": 0.5,
    }


def row_diagnostics(matrix: np.ndarray) -> dict[str, object]:
    values = np.asarray(matrix, dtype=np.float64)
    row_hashes = {hashlib.sha256(np.ascontiguousarray(row).tobytes()).digest() for row in values}
    variance = values.var(axis=0, ddof=0)
    return {
        "shape": [int(x) for x in values.shape],
        "finite": bool(np.isfinite(values).all()),
        "duplicate_rows": int(values.shape[0] - len(row_hashes)),
        "zero_variance_dimensions": int(np.count_nonzero(variance == 0)),
        "total_variance": float(variance.sum()),
        "collapsed": bool(np.all(variance == 0)),
    }
