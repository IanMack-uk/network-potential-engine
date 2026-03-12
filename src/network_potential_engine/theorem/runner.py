from __future__ import annotations

import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import numpy as np


@dataclass(frozen=True)
class CheckReport:
    name: str
    passed: bool
    error_type: str | None = None
    error_message: str | None = None
    payload: Any | None = None
    error: Exception | None = None
    tolerances: dict[str, float] | None = None
    regime_tag: str | None = None
    matrix_fingerprint: str | None = None
    consumed_assumption_ids: list[str] | None = None

    def to_json_dict(self) -> dict[str, Any]:
        scipy_version: str | None
        try:
            import scipy  # type: ignore

            scipy_version = str(scipy.__version__)
        except ModuleNotFoundError:
            scipy_version = None

        return {
            "name": self.name,
            "passed": self.passed,
            "error_type": self.error_type,
            "error_message": self.error_message,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "git_commit": _git_commit(),
            "python_version": sys.version,
            "platform": platform.platform(),
            "numpy_version": str(np.__version__),
            "scipy_version": scipy_version,
            "tolerances": self.tolerances,
            "regime_tag": self.regime_tag,
            "matrix_fingerprint": self.matrix_fingerprint,
            "consumed_assumption_ids": self.consumed_assumption_ids,
        }


def _git_commit() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL,
        )
    except Exception:
        return "unknown"

    return out.decode("utf-8").strip() or "unknown"


def run_check(
    name: str,
    fn: Callable[[], Any],
    *,
    artifact_mode: bool = False,
    artifact_path: str | Path | None = None,
    tolerances: dict[str, float] | None = None,
    regime_tag: str | None = None,
    matrix_fingerprint: str | None = None,
    consumed_assumption_ids: list[str] | None = None,
) -> CheckReport:
    try:
        payload = fn()
    except Exception as exc:
        report = CheckReport(
            name=name,
            passed=False,
            error_type=type(exc).__name__,
            error_message=str(exc),
            payload=None,
            error=exc,
            tolerances=tolerances,
            regime_tag=regime_tag,
            matrix_fingerprint=matrix_fingerprint,
            consumed_assumption_ids=consumed_assumption_ids,
        )

        if artifact_mode and artifact_path is not None:
            path = Path(artifact_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(report.to_json_dict(), indent=2, sort_keys=True))

        return report

    report = CheckReport(
        name=name,
        passed=True,
        payload=payload,
        error=None,
        tolerances=tolerances,
        regime_tag=regime_tag,
        matrix_fingerprint=matrix_fingerprint,
        consumed_assumption_ids=consumed_assumption_ids,
    )

    if artifact_mode and artifact_path is not None:
        path = Path(artifact_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report.to_json_dict(), indent=2, sort_keys=True))

    return report
