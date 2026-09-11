"""Minimal read-only H5AD loader for the Phase 3C source mirrors."""

from __future__ import annotations

import csv
import hashlib
from dataclasses import dataclass
from pathlib import Path

import h5py
import numpy as np
from scipy import sparse


def _decode(value: object) -> str:
    if isinstance(value, bytes):
        return value.decode("utf-8")
    if isinstance(value, np.generic):
        return str(value.item())
    return str(value)


def _index(group: h5py.Group) -> list[str]:
    key = group.attrs.get("_index", "_index")
    key = key.decode("utf-8") if isinstance(key, bytes) else str(key)
    obj = group[key]
    if not isinstance(obj, h5py.Dataset):
        raise ValueError(f"categorical index is unsupported at {obj.name}")
    return [_decode(value) for value in obj[()]]


def _matrix(obj: h5py.Group | h5py.Dataset) -> sparse.csr_matrix:
    if isinstance(obj, h5py.Dataset):
        return sparse.csr_matrix(np.asarray(obj[()], dtype=np.float64))
    encoding = obj.attrs.get("encoding-type", "")
    encoding = encoding.decode("utf-8") if isinstance(encoding, bytes) else str(encoding)
    shape = tuple(int(x) for x in obj.attrs["shape"])
    data = np.asarray(obj["data"], dtype=np.float64)
    indices = np.asarray(obj["indices"], dtype=np.int64)
    indptr = np.asarray(obj["indptr"], dtype=np.int64)
    if encoding == "csr_matrix":
        return sparse.csr_matrix((data, indices, indptr), shape=shape)
    if encoding == "csc_matrix":
        return sparse.csc_matrix((data, indices, indptr), shape=shape).tocsr()
    raise ValueError(f"unsupported H5AD matrix encoding: {encoding}")


def sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def identifiers_sha256(values: list[str]) -> str:
    return hashlib.sha256(("\n".join(values) + "\n").encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class H5ADView:
    path: Path
    matrix: sparse.csr_matrix
    observation_ids: list[str]
    feature_ids: list[str]
    original_feature_ids: list[str]
    coordinates: np.ndarray
    file_sha256: str


def load_h5ad(path: str | Path, expected_sha256: str) -> H5ADView:
    source = Path(path)
    before = sha256(source)
    if before != expected_sha256:
        raise ValueError(f"source checksum mismatch: {source}")
    with h5py.File(source, "r") as handle:
        matrix = _matrix(handle["X"])
        observation_ids = _index(handle["obs"])
        original_feature_ids = _index(handle["var"])
        gene_ids = None
        if "gene_ids" in handle["var"] and isinstance(handle["var/gene_ids"], h5py.Dataset):
            gene_ids = [_decode(value) for value in handle["var/gene_ids"][()]]
        if gene_ids and len(gene_ids) == matrix.shape[1] and len(set(gene_ids)) == len(gene_ids) and all(gene_ids):
            feature_ids = gene_ids
        else:
            feature_ids = [f"{value}#{position}" for position, value in enumerate(original_feature_ids)]
        coordinates = np.asarray(handle["obsm/spatial"], dtype=np.float64)
    after = sha256(source)
    if before != after:
        raise RuntimeError(f"source changed during read: {source}")
    if matrix.shape != (len(observation_ids), len(feature_ids)):
        raise ValueError(f"axis lengths do not match matrix: {source}")
    if coordinates.shape != (matrix.shape[0], 2):
        raise ValueError(f"expected n x 2 spatial coordinates: {source}")
    return H5ADView(source, matrix, observation_ids, feature_ids, original_feature_ids, coordinates, after)


def load_labels(path: str | Path, observation_ids: list[str], label_column: str) -> tuple[np.ndarray, dict[str, object]]:
    source = Path(path)
    with source.open(newline="", encoding="utf-8-sig") as stream:
        rows = list(csv.DictReader(stream))
    if not rows:
        raise ValueError(f"empty annotation file: {source}")
    id_candidates = [name for name in rows[0] if name.lower() == "barcode"]
    if len(id_candidates) != 1 or label_column not in rows[0]:
        raise ValueError(f"annotation columns unresolved: {source}")
    id_column = id_candidates[0]
    mapping: dict[str, str] = {}
    for row in rows:
        identity, label = row[id_column], row[label_column]
        if not identity or not label or identity in mapping:
            raise ValueError(f"missing or duplicate annotation identity: {source}")
        mapping[identity] = label
    requested, available = set(observation_ids), set(mapping)
    if requested != available:
        raise ValueError(f"annotation identity set mismatch: {source}")
    labels = np.asarray([mapping[identity] for identity in observation_ids], dtype=str)
    diagnostics = {
        "path": str(source),
        "id_column": id_column,
        "label_column": label_column,
        "rows": len(rows),
        "matched": len(observation_ids),
        "missing": 0,
        "extra": 0,
        "categories": int(np.unique(labels).size),
        "joined_by_identifier": True,
    }
    return labels, diagnostics
