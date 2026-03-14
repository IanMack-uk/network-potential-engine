from __future__ import annotations

import json
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


def _try_git_head_sha(repo_root: Path) -> str | None:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=str(repo_root),
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return out or None
    except Exception:
        return None


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def _format_float(x: float) -> str:
    return f"{x:.16g}"


def _reconstruct_tridiagonal_matrix(*, main: np.ndarray, off: np.ndarray) -> np.ndarray:
    n = int(main.shape[0])
    C = np.diag(main)
    C += np.diag(off, 1)
    C += np.diag(off, -1)
    return C


def _ranking_indices_by_policy(score: np.ndarray, *, top_k: int) -> list[int]:
    return sorted(range(int(score.shape[0])), key=lambda i: (-float(score[i]), int(i)))[:top_k]


def _check_no_nan_inf(x: np.ndarray, *, name: str) -> None:
    if not np.isfinite(x).all():
        bad = np.where(~np.isfinite(x))[0]
        raise ValueError(f"{name} contains non-finite values at indices: {bad[:10].tolist()}")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[3]
    artifacts_root = repo_root / "affinity" / "artifacts" / "n50"
    static_dir = artifacts_root / "static"
    latest_dir = artifacts_root / "generated" / "latest"

    transcript_path = latest_dir / "smoke_run_transcript_v2.txt"

    artifact_paths = {
        "registry": static_dir / "registry" / "student_registry_v1.json",
        "source_s": latest_dir / "source_vector_s_v2.json",
        "coupling_C": latest_dir / "coupling_operator_C_v2.json",
        "propagated_v": latest_dir / "propagated_value_v_v2.json",
        "energy_E": latest_dir / "node_energy_E_v2.json",
        "energy_E_eff": latest_dir / "node_energy_E_eff_v2.json",
        "export": latest_dir / "app_facing_outputs_v2.json",
        "observations": latest_dir / "observations_v2.json",
        "ties": latest_dir / "tie_strengths_w_v2.json",
    }

    missing = [str(p) for p in artifact_paths.values() if not p.exists()]
    if missing:
        print("Missing required v2 artifacts:")
        for m in missing:
            print(f"- {m}")
        return 2

    registry = _load_json(artifact_paths["registry"])
    s_obj = _load_json(artifact_paths["source_s"])
    C_obj = _load_json(artifact_paths["coupling_C"])
    v_obj = _load_json(artifact_paths["propagated_v"])
    E_obj = _load_json(artifact_paths["energy_E"])
    Eeff_obj = _load_json(artifact_paths["energy_E_eff"])
    export_obj = _load_json(artifact_paths["export"])
    observations_obj = _load_json(artifact_paths["observations"])
    ties_obj = _load_json(artifact_paths["ties"])

    nodes = sorted(registry["nodes"], key=lambda x: x["node_index"])
    student_ids = [n["student_id"] for n in nodes]
    n = len(student_ids)

    s_map = {e["student_id"]: float(e["s"]) for e in s_obj["s"]}
    s = np.array([s_map[sid] for sid in student_ids], dtype=float)
    v = np.asarray(v_obj["v"], dtype=float).reshape(-1)
    E = np.asarray(E_obj["E"], dtype=float).reshape(-1)
    E_eff = np.asarray(Eeff_obj["E_eff"], dtype=float).reshape(-1)
    rho = np.asarray(Eeff_obj["rho"], dtype=float).reshape(-1)

    if s.shape != (n,):
        raise ValueError(f"s length mismatch: expected {n}, got {s.shape}")
    if v.shape != (n,):
        raise ValueError(f"v length mismatch: expected {n}, got {v.shape}")
    if E.shape != (n,):
        raise ValueError(f"E length mismatch: expected {n}, got {E.shape}")
    if E_eff.shape != (n,):
        raise ValueError(f"E_eff length mismatch: expected {n}, got {E_eff.shape}")
    if rho.shape != (n,):
        raise ValueError(f"rho length mismatch: expected {n}, got {rho.shape}")

    _check_no_nan_inf(s, name="s")
    _check_no_nan_inf(v, name="v")
    _check_no_nan_inf(E, name="E")
    _check_no_nan_inf(E_eff, name="E_eff")
    _check_no_nan_inf(rho, name="rho")

    beta0 = float(E_obj.get("parameters", {}).get("beta0", 1.0))
    beta1 = float(E_obj.get("parameters", {}).get("beta1", 1.0))

    E_recon = beta0 * s + beta1 * v
    Eeff_recon = beta0 * s + beta1 * (rho * v)

    if float(np.max(np.abs(E - E_recon))) > 1e-9:
        raise ValueError("E does not match definition E = beta0*s + beta1*v")
    if float(np.max(np.abs(E_eff - Eeff_recon))) > 1e-9:
        raise ValueError("E_eff does not match definition E_eff = beta0*s + beta1*(rho ⊙ v)")

    fmt = C_obj["format"]
    if fmt.get("type") != "symmetric_dense":
        raise ValueError("coupling_operator_C_v2.json must be symmetric_dense")
    C = np.asarray(fmt["matrix"], dtype=float)
    if C.shape != (n, n):
        raise ValueError(f"C shape mismatch: expected {(n, n)}, got {C.shape}")

    residual = C @ v - s
    residual_norm = float(np.linalg.norm(residual, ord=2))

    events = observations_obj.get("events")
    if not isinstance(events, list):
        raise ValueError("observations_v2.json must contain a list field 'events'")

    ties = ties_obj.get("ties")
    if not isinstance(ties, list):
        raise ValueError("tie_strengths_w_v2.json must contain a list field 'ties'")

    top_k = int(export_obj.get("top_k", 10))
    score = E_eff
    top_policy = _ranking_indices_by_policy(score, top_k=top_k)

    export_entries = export_obj["rankings"]["entries"]
    export_top = [int(e["node_index"]) for e in export_entries]
    if export_top != top_policy:
        raise ValueError("export rankings do not match declared deterministic sort policy")

    lines: list[str] = []

    def section(title: str) -> None:
        lines.append("=" * 78)
        lines.append(title)
        lines.append("=" * 78)

    section("Affinity n=50 smoke transcript (v2)")
    lines.append(f"timestamp_utc: {datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')}")
    lines.append(f"python: {platform.python_version()}")
    lines.append(f"platform: {platform.platform()}")
    sha = _try_git_head_sha(repo_root)
    lines.append(f"git_head_sha: {sha if sha is not None else 'unknown'}")
    lines.append("")

    section("Artifact presence")
    for k, p in artifact_paths.items():
        lines.append(f"{k}: OK ({p.name})")

    lines.append("")
    section("Summary stats")
    lines.append(f"n_nodes: {n}")
    lines.append(f"n_observation_events: {len(events)}")
    lines.append(f"n_directed_ties: {len(ties)}")
    lines.append(f"solve_residual_l2_norm: {_format_float(residual_norm)}")
    lines.append("")
    lines.append(f"s: min={_format_float(float(np.min(s)))} mean={_format_float(float(np.mean(s)))} max={_format_float(float(np.max(s)))}")
    lines.append(
        f"rho: min={_format_float(float(np.min(rho)))} mean={_format_float(float(np.mean(rho)))} max={_format_float(float(np.max(rho)))}"
    )
    lines.append(
        f"E_eff: min={_format_float(float(np.min(E_eff)))} mean={_format_float(float(np.mean(E_eff)))} max={_format_float(float(np.max(E_eff)))}"
    )

    lines.append("")
    section("Top-k ranking (deterministic policy)")
    for rank, i in enumerate(top_policy, start=1):
        lines.append(
            f"{rank:2d}. node_index={i:2d} score={_format_float(float(score[i]))} student_id={student_ids[i]}"
        )

    lines.append("")
    section("PASS")
    lines.append("All checks passed.")

    transcript_path.write_text("\n".join(lines) + "\n")
    print(f"Wrote transcript: {transcript_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
