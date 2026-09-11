"""Machine-readable run provenance helpers."""

from __future__ import annotations

import hashlib
import json
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REQUIRED_PROVENANCE_V1 = {
    "experiment_id", "timestamp_utc", "dataset", "method", "code_commit",
    "environment", "preprocessing", "seed", "parameters", "hardware",
    "input_checksums", "output_paths", "runtime_seconds", "exit_status",
}
REQUIRED_PROVENANCE = REQUIRED_PROVENANCE_V1 | {"compute_classification"}
VALID_COMPUTE_CLASSIFICATIONS = {
    "LOCAL_LIGHT", "COLAB_CPU", "COLAB_GPU", "COLAB_HIGH_MEMORY", "UNRESOLVED",
}


def sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def local_environment() -> dict[str, str]:
    return {"python": platform.python_version(), "platform": platform.platform(), "machine": platform.machine()}


def git_head(repo: str | Path = ".") -> str:
    return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()


def validate_provenance(record: dict[str, Any], schema_version: int = 2) -> None:
    if schema_version not in {1, 2}:
        raise ValueError(f"unsupported provenance schema version: {schema_version}")
    required = REQUIRED_PROVENANCE if schema_version == 2 else REQUIRED_PROVENANCE_V1
    missing = sorted(required - record.keys())
    if missing:
        raise ValueError(f"missing provenance fields: {', '.join(missing)}")
    if schema_version == 2:
        classification = record["compute_classification"]
        if classification not in VALID_COMPUTE_CLASSIFICATIONS:
            raise ValueError(f"unknown compute classification: {classification}")
        if classification == "UNRESOLVED" and record["exit_status"] in {"RUNNING", "SUCCEEDED"}:
            raise ValueError("compute classification must be resolved before scientific execution")


def write_json(record: dict[str, Any], path: str | Path, schema_version: int = 2) -> None:
    validate_provenance(record, schema_version=schema_version)
    Path(path).write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
