"""Frozen common KMeans and metric implementation for Phase 3C."""

from __future__ import annotations

from collections import Counter

import numpy as np
import sklearn
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score, silhouette_score


def cluster_and_evaluate(representation: np.ndarray, labels: np.ndarray, seed: int) -> tuple[np.ndarray, dict[str, object], dict[str, int]]:
    cluster_count = int(np.unique(labels).size)
    model = KMeans(n_clusters=cluster_count, init="k-means++", n_init=20, max_iter=300,
                   tol=1e-4, random_state=seed, algorithm="lloyd")
    clusters = model.fit_predict(representation)
    observed_clusters = int(np.unique(clusters).size)
    if observed_clusters < 2:
        raise ValueError("common clustering produced fewer than two clusters")
    sample_size = min(500, representation.shape[0])
    metrics = {
        "interpretation": "agreement_with_reference_annotation_and_metric_dependent_separation",
        "cluster_count": cluster_count,
        "cluster_count_source": "reference_annotation_count",
        "privileged_label_information": True,
        "ARI": {
            "implementation": "sklearn.metrics.adjusted_rand_score",
            "library_version": sklearn.__version__,
            "parameters": {},
            "inputs": ["reference_annotations", "predicted_clusters"],
            "result": float(adjusted_rand_score(labels, clusters)),
        },
        "NMI": {
            "implementation": "sklearn.metrics.normalized_mutual_info_score",
            "library_version": sklearn.__version__,
            "parameters": {"average_method": "arithmetic"},
            "inputs": ["reference_annotations", "predicted_clusters"],
            "result": float(normalized_mutual_info_score(labels, clusters, average_method="arithmetic")),
        },
        "silhouette": {
            "implementation": "sklearn.metrics.silhouette_score",
            "library_version": sklearn.__version__,
            "parameters": {"metric": "euclidean", "sample_size": sample_size, "random_state": 0},
            "inputs": ["representation", "predicted_clusters"],
            "result": float(silhouette_score(representation, clusters, metric="euclidean", sample_size=sample_size, random_state=0)),
        },
        "kmeans": {
            "implementation": "sklearn.cluster.KMeans",
            "library_version": sklearn.__version__,
            "parameters": {"n_clusters": cluster_count, "init": "k-means++", "n_init": 20, "max_iter": 300, "tol": 1e-4, "random_state": seed, "algorithm": "lloyd"},
            "iterations": int(model.n_iter_),
            "inertia": float(model.inertia_),
        },
    }
    sizes = {str(key): int(value) for key, value in sorted(Counter(int(x) for x in clusters).items())}
    return clusters, metrics, sizes
