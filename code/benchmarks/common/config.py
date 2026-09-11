"""Typed benchmark configuration objects; no biological data are loaded here."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

VALID_DATASETS = {"LN_A1", "LN_D1", "MB_E11", "MB_E13", "MB_E15", "MB_E18"}
VALID_STATUSES = {"PLANNED", "PREPARING", "RUNNING", "SUCCEEDED", "FAILED", "INVALID", "BLOCKED"}
VALID_COMPUTE_CLASSIFICATIONS = {
    "LOCAL_LIGHT",
    "COLAB_CPU",
    "COLAB_GPU",
    "COLAB_HIGH_MEMORY",
    "UNRESOLVED",
}


@dataclass(frozen=True)
class DatasetInput:
    dataset_id: str
    modality: str
    matrix_path: str
    observation_ids: str
    feature_ids: str
    counts_or_processed: str
    coordinates: str | None = None
    labels: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if self.dataset_id not in VALID_DATASETS:
            raise ValueError(f"unknown canonical dataset: {self.dataset_id}")
        if not self.modality or not self.matrix_path:
            raise ValueError("modality and matrix_path are required")
        if not self.observation_ids or not self.feature_ids:
            raise ValueError("explicit observation_ids and feature_ids are required")


@dataclass(frozen=True)
class RunConfig:
    experiment_id: str
    dataset: str
    method: str
    seed: int
    inputs: tuple[DatasetInput, ...]
    preprocessing: dict[str, Any]
    method_parameters: dict[str, Any]
    clustering: dict[str, Any]
    output_directory: str
    compute_classification: str = "UNRESOLVED"
    status: str = "PLANNED"
    example_only: bool = False

    def validate(self) -> None:
        if not self.experiment_id.startswith("EXP-"):
            raise ValueError("experiment_id must start with EXP-")
        if self.dataset not in VALID_DATASETS:
            raise ValueError(f"unknown canonical dataset: {self.dataset}")
        if not self.inputs:
            raise ValueError("at least one input is required")
        if self.status not in VALID_STATUSES:
            raise ValueError(f"unknown run status: {self.status}")
        if self.compute_classification not in VALID_COMPUTE_CLASSIFICATIONS:
            raise ValueError(f"unknown compute classification: {self.compute_classification}")
        if self.compute_classification == "UNRESOLVED" and self.status in {"RUNNING", "SUCCEEDED"}:
            raise ValueError("compute classification must be resolved before scientific execution")
        for item in self.inputs:
            item.validate()
            if item.dataset_id != self.dataset:
                raise ValueError("all inputs must match the run dataset")
        if Path(self.output_directory).name != self.experiment_id:
            raise ValueError("output directory must end with experiment_id")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)
