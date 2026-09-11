"""Build only the baseline families authorized for Phase 3C."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from code.benchmarks.common.h5ad import H5ADView
from code.benchmarks.common.preprocessing import (
    adt_representation,
    atac_representation,
    concatenate_equal_blocks,
    coordinate_representation,
    pca_representation,
    rna_representation,
)


@dataclass(frozen=True)
class Representation:
    baseline: str
    modalities: str
    values: np.ndarray
    preprocessing: dict[str, object]


def build_representations(rna: H5ADView, second: H5ADView | None, second_modality: str | None) -> dict[str, Representation]:
    rna_values, rna_meta = rna_representation(rna.matrix, rna.feature_ids)
    pca_values, pca_meta = pca_representation(rna_values)
    space_values, space_meta = coordinate_representation(rna.coordinates)
    result = {
        "RNA": Representation("RNA", "RNA", rna_values, {"RNA": rna_meta}),
        "PCA": Representation("PCA", "RNA", pca_values, {"RNA": rna_meta, "PCA": pca_meta}),
        "SPACE": Representation("SPACE", "spatial_coordinates", space_values, {"coordinates": space_meta}),
    }
    if second is None or second_modality is None:
        return result
    if rna.observation_ids != second.observation_ids:
        raise ValueError("paired modality observation order differs")
    if not np.array_equal(rna.coordinates, second.coordinates):
        raise ValueError("paired modality coordinates differ")
    if second_modality == "ADT":
        second_values, second_meta = adt_representation(second.matrix, second.feature_ids)
        code = "ADT"
    elif second_modality == "ATAC":
        second_values, second_meta = atac_representation(second.matrix, second.feature_ids)
        code = "ATAC"
    else:
        raise ValueError(f"unsupported second modality: {second_modality}")
    concat_values, concat_meta = concatenate_equal_blocks(rna_values, second_values)
    result[code] = Representation(code, code, second_values, {code: second_meta})
    result["CONCAT"] = Representation("CONCAT", f"RNA+{code}", concat_values, {"RNA": rna_meta, code: second_meta, "concatenation": concat_meta})
    return result
