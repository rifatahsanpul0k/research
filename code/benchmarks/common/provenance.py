"""Machine-readable run provenance helpers."""

from __future__ import annotations

import hashlib
import json
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REQUIRED_PROVENANCE = {
    "experiment_id", "timestamp_utc", "dataset", "method", "code_commit",
    "environment", "preprocessing", "seed", "parameters", "hardware",
    "input_checksums", "output_paths", "runtime_seconds", "exit_status",
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


def validate_provenance(record: dict[str, Any]) -> None:
    missing = sorted(REQUIRED_PROVENANCE - record.keys())
    if missing:
        raise ValueError(f"missing provenance fields: {', '.join(missing)}")


def write_json(record: dict[str, Any], path: str | Path) -> None:
    validate_provenance(record)
    Path(path).write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
