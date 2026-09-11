"""Traceable failed-run artifact creation."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from code.benchmarks.common.io import write_json_atomic


def write_failure_artifacts(output: str | Path, experiment_id: str, error: BaseException,
                            category: str, stage: str, traceback_text: str) -> dict[str, object]:
    destination = Path(output)
    destination.mkdir(parents=True, exist_ok=True)
    record = {
        "experiment_id": experiment_id,
        "status": "FAILED",
        "failure_category": category,
        "stage": stage,
        "error_type": type(error).__name__,
        "error": str(error),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }
    write_json_atomic(record, destination / "failure.json")
    (destination / "stderr.log").write_text(traceback_text)
    (destination / "stdout.log").touch()
    (destination / "STATUS").write_text("FAILED\n")
    return record
