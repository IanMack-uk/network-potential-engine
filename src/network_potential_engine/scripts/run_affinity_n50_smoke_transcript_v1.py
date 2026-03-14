from __future__ import annotations

import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

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


def _load_json(path: Path) -> object:
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


def main() -> int:
    repo_root = Path(__file__).resolve().parents[3]
    artifacts_root = repo_root / "affinity" / "artifacts" / "n50"
    static_dir = artifacts_root / "static"
    legacy_dir = artifacts_root / "legacy" / "v1"
    latest_dir = artifacts_root / "generated" / "latest"

    transcript_path = latest_dir / "smoke_run_transcript_v1.txt"

    artifact_paths = {
        "registry": static_dir / "registry" / "student_registry_v1.json",
        "source_s": legacy_dir / "source_vector_s_v1.json",
        "coupling_C": legacy_dir / "coupling_operator_C_v1.json",
        "propagated_v": legacy_dir / "propagated_value_v_v1.json",
        "energy_E": legacy_dir / "node_energy_E_v1.json",
        "energy_E_eff": legacy_dir / "node_energy_E_eff_v1.json",
        "export": legacy_dir / "app_facing_outputs_v1.json",
    }

    missing = [str(p) for p in artifact_paths.values() if not p.exists()]
    if missing:
        print("Missing required artifacts:")
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

    nodes = sorted(registry["nodes"], key=lambda x: x["node_index"])
    student_ids = [n["student_id"] for n in nodes]
    n = len(student_ids)

    s_map = {e["student_id"]: float(e["s"]) for e in s_obj["s"]}
    s = np.array([s_map[sid] for sid in student_ids], dtype=float)
    v = np.asarray(v_obj["v"], dtype=float).reshape(-1)
    E = np.asarray(E_obj["E"], dtype=float).reshape(-1)
    E_eff = np.asarray(Eeff_obj["E_eff"], dtype=float).reshape(-1)
    rho = np.asarray(Eeff_obj["rho"], dtype=float).reshape(-1)

    beta0 = float(E_obj["parameters"]["beta0"])
    beta1 = float(E_obj["parameters"]["beta1"])

    fmt = C_obj["format"]
    if fmt.get("type") != "symmetric_tridiagonal":
        raise ValueError("coupling_operator_C_v1.json must be symmetric_tridiagonal")
    main = np.asarray(fmt["main_diagonal"], dtype=float)
    off = np.asarray(fmt["off_diagonal"], dtype=float)
    C = _reconstruct_tridiagonal_matrix(main=main, off=off)

    lines: list[str] = []

    def section(title: str) -> None:
        lines.append("=" * 78)
        lines.append(title)
        lines.append("=" * 78)

    def record(msg: str = "") -> None:
        lines.append(msg)

    utc_now = datetime.now(timezone.utc).isoformat()
    head_sha = _try_git_head_sha(repo_root)

    section("Job 13 — Affinity n=50 smoke run transcript (v1)")
    record(f"timestamp_utc: {utc_now}")
    record(f"python: {sys.version.split()[0]}")
    record(f"platform: {platform.platform()}")
    record(f"git_head_sha: {head_sha if head_sha is not None else 'UNKNOWN'}")
    record("")

    section("Artifacts loaded")
    for k, p in artifact_paths.items():
        record(f"- {k}: {p.relative_to(repo_root)}")
    record("")

    overall_pass = True

    section("Registry / shape checks")
    try:
        if n != 50:
            raise ValueError(f"registry n must be 50, got {n}")
        if v.shape != (n,):
            raise ValueError(f"v must have shape ({n},), got {v.shape}")
        if E.shape != (n,) or E_eff.shape != (n,) or rho.shape != (n,):
            raise ValueError("E, E_eff, rho must all match registry length")
        record("PASS")
    except Exception as exc:
        overall_pass = False
        record(f"FAIL: {type(exc).__name__}: {exc}")
    record("")

    section("Propagation residual check (recomputed)")
    try:
        res = C.dot(v) - s
        res_l2 = float(np.linalg.norm(res))
        res_linf = float(np.max(np.abs(res)))
        tol = 1e-10
        record(f"||C v - s||_2: {_format_float(res_l2)}")
        record(f"||C v - s||_inf: {_format_float(res_linf)}")
        record(f"tolerance: {tol}")
        if res_l2 > tol or res_linf > tol:
            raise ValueError("propagation residual exceeds tolerance")
        record("PASS")
    except Exception as exc:
        overall_pass = False
        record(f"FAIL: {type(exc).__name__}: {exc}")
    record("")

    section("Energy identity checks")
    try:
        E_expected = beta0 * s + beta1 * v
        if not np.allclose(E, E_expected):
            raise ValueError("E does not satisfy E = beta0*s + beta1*v")
        Eeff_expected = beta0 * s + beta1 * (rho * v)
        if not np.allclose(E_eff, Eeff_expected):
            raise ValueError("E_eff does not satisfy E_eff = beta0*s + beta1*(rho ⊙ v)")
        record(f"beta0: {_format_float(beta0)}")
        record(f"beta1: {_format_float(beta1)}")
        record(f"E_min: {_format_float(float(E.min()))}")
        record(f"E_max: {_format_float(float(E.max()))}")
        record(f"E_eff_min: {_format_float(float(E_eff.min()))}")
        record(f"E_eff_max: {_format_float(float(E_eff.max()))}")
        record("PASS")
    except Exception as exc:
        overall_pass = False
        record(f"FAIL: {type(exc).__name__}: {exc}")
    record("")

    section("Export JSON consistency checks")
    try:
        if export_obj.get("canonical_score") != "E_eff":
            raise ValueError("export canonical_score must be E_eff")
        top_k = int(export_obj.get("top_k"))
        if top_k <= 0:
            raise ValueError("export top_k must be positive")

        students = export_obj.get("students")
        if not isinstance(students, list) or len(students) != n:
            raise ValueError("export students must be a list of length n")

        for i, st in enumerate(students):
            if int(st["node_index"]) != i:
                raise ValueError("export students must be node_index_ascending")
            if st["student_id"] != student_ids[i]:
                raise ValueError("export student_id mismatch vs registry")
            if float(st["E_eff"]) != float(E_eff[i]):
                raise ValueError("export E_eff mismatch vs Job 11 artifact")

        expected_rank_idx = _ranking_indices_by_policy(E_eff, top_k=top_k)

        entries = export_obj.get("rankings", {}).get("entries")
        if not isinstance(entries, list) or len(entries) != top_k:
            raise ValueError("export rankings.entries must have length top_k")

        for r, i_expected in enumerate(expected_rank_idx, start=1):
            ent = entries[r - 1]
            if int(ent["rank"]) != r:
                raise ValueError("export rank field mismatch")
            if int(ent["node_index"]) != int(i_expected):
                raise ValueError("export ranking order mismatch")
            if ent["student_id"] != student_ids[i_expected]:
                raise ValueError("export ranking student_id mismatch")

        record(f"canonical_score: E_eff")
        record(f"top_k: {top_k}")
        record("top_k_node_indices: " + ", ".join(str(i) for i in expected_rank_idx))
        record("PASS")
    except Exception as exc:
        overall_pass = False
        record(f"FAIL: {type(exc).__name__}: {exc}")
    record("")

    section("Overall result")
    record("PASS" if overall_pass else "FAIL")

    transcript_path.write_text("\n".join(lines) + "\n")

    print("\n".join(lines))
    print(f"\nWROTE: {transcript_path}")

    return 0 if overall_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
