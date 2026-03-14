from __future__ import annotations

import json
import platform
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


def _find_repo_root(start: Path) -> Path:
    p = start.resolve()
    for candidate in [p, *p.parents]:
        if (candidate / ".git").exists() or (candidate / "pyproject.toml").exists():
            return candidate
    return start.resolve()


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


def _write_json(path: Path, obj: Any) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=False) + "\n")


def _fmt_float(x: float) -> str:
    return f"{x:.16g}"


@dataclass(frozen=True)
class ScenarioResult:
    scenario_id: str
    name: str
    passed: bool
    details: dict[str, object]


def _ranking_indices_by_policy(score: np.ndarray, *, top_k: int) -> list[int]:
    return sorted(range(int(score.shape[0])), key=lambda i: (-float(score[i]), int(i)))[:top_k]


def _load_v2_vectors(*, artifacts_dir: Path) -> tuple[list[str], np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    artifacts_root = artifacts_dir.parent.parent
    registry_obj = _load_json(artifacts_root / "static" / "registry" / "student_registry_v1.json")
    s_obj = _load_json(artifacts_dir / "source_vector_s_v2.json")
    C_obj = _load_json(artifacts_dir / "coupling_operator_C_v2.json")
    v_obj = _load_json(artifacts_dir / "propagated_value_v_v2.json")
    Eeff_obj = _load_json(artifacts_dir / "node_energy_E_eff_v2.json")

    nodes = sorted(registry_obj["nodes"], key=lambda x: int(x["node_index"]))
    student_ids = [n["student_id"] for n in nodes]
    n = len(student_ids)

    s_map = {e["student_id"]: float(e["s"]) for e in s_obj["s"]}
    s = np.array([s_map[sid] for sid in student_ids], dtype=float)

    fmt = C_obj["format"]
    if fmt.get("type") != "symmetric_dense":
        raise ValueError("coupling_operator_C_v2.json must be symmetric_dense")
    C = np.asarray(fmt["matrix"], dtype=float)

    v = np.asarray(v_obj["v"], dtype=float).reshape(-1)

    rho = np.asarray(Eeff_obj["rho"], dtype=float).reshape(-1)
    E_eff = np.asarray(Eeff_obj["E_eff"], dtype=float).reshape(-1)

    beta0 = float(Eeff_obj.get("parameters", {}).get("beta0", 1.0))
    beta1 = float(Eeff_obj.get("parameters", {}).get("beta1", 1.0))

    if s.shape != (n,) or v.shape != (n,) or rho.shape != (n,) or E_eff.shape != (n,):
        raise ValueError("vector length mismatch vs registry")
    if C.shape != (n, n):
        raise ValueError("C shape mismatch vs registry")

    return student_ids, s, C, v, rho, np.array([beta0, beta1], dtype=float)


def _solve_v(*, C: np.ndarray, s: np.ndarray) -> np.ndarray:
    return np.linalg.solve(C, s)


def _compute_E_eff(*, s: np.ndarray, v: np.ndarray, rho: np.ndarray, beta0: float, beta1: float) -> np.ndarray:
    return beta0 * s + beta1 * (rho * v)


def _w_directed_from_ties(ties_obj: dict[str, Any]) -> dict[tuple[str, str], float]:
    ties = ties_obj.get("ties")
    if not isinstance(ties, list):
        raise ValueError("tie_strengths_w_v2.json must contain list field 'ties'")
    out: dict[tuple[str, str], float] = {}
    for t in ties:
        if not isinstance(t, dict):
            continue
        a = t.get("actor_student_id")
        b = t.get("target_student_id")
        w = t.get("w")
        if isinstance(a, str) and isinstance(b, str) and isinstance(w, (int, float)):
            out[(a, b)] = float(out.get((a, b), 0.0) + float(w))
    return out


def _coupling_operator_from_ties(
    *,
    student_ids: list[str],
    w_directed: dict[tuple[str, str], float],
    alpha: float,
    jitter: float,
) -> np.ndarray:
    n = len(student_ids)
    idx = {sid: i for i, sid in enumerate(student_ids)}
    W = np.zeros((n, n), dtype=float)

    for (a, b), wt in w_directed.items():
        if a == b:
            continue
        ia = idx.get(a)
        ib = idx.get(b)
        if ia is None or ib is None:
            continue
        W[ia, ib] += float(wt)

    W_sym = 0.5 * (W + W.T)
    nonzero = W_sym[W_sym > 0]
    scale = float(np.mean(nonzero)) if nonzero.size > 0 else 1.0
    if scale <= 0:
        scale = 1.0
    W_sym_scaled = W_sym / scale

    d = np.sum(W_sym_scaled, axis=1)
    L = np.diag(d) - W_sym_scaled

    C = np.eye(n, dtype=float) + float(alpha) * L + float(jitter) * np.eye(n, dtype=float)
    return C


def _scenario_v2_s1_export_coherence(*, artifacts_dir: Path, tol: float) -> ScenarioResult:
    export_obj = _load_json(artifacts_dir / "app_facing_outputs_v2.json")
    if not isinstance(export_obj, dict):
        return ScenarioResult("S1", "Export schema + explanation coherence", False, {"error": "export not object"})

    students = export_obj.get("students")
    if not isinstance(students, list):
        return ScenarioResult("S1", "Export schema + explanation coherence", False, {"error": "students missing"})

    missing_fields_count = 0
    max_abs_err = 0.0

    score_by_node_index: dict[int, float] = {}

    for s in students:
        if not isinstance(s, dict):
            missing_fields_count += 1
            continue

        node_index = s.get("node_index")
        e_eff = s.get("E_eff")
        expl = s.get("explanation")

        if not isinstance(node_index, int) or not isinstance(e_eff, (int, float)) or not isinstance(expl, dict):
            missing_fields_count += 1
            continue

        intrinsic = expl.get("intrinsic_component")
        network = expl.get("network_component")
        if not isinstance(intrinsic, (int, float)) or not isinstance(network, (int, float)):
            missing_fields_count += 1
            continue

        abs_err = abs((float(intrinsic) + float(network)) - float(e_eff))
        max_abs_err = max(max_abs_err, abs_err)
        score_by_node_index[int(node_index)] = float(e_eff)

    ranking = export_obj.get("rankings")
    ranking_ok = True
    ranking_error: str | None = None

    if not isinstance(ranking, dict) or not isinstance(ranking.get("entries"), list):
        ranking_ok = False
        ranking_error = "rankings.entries missing"
    else:
        entries = ranking["entries"]
        expected = sorted(score_by_node_index.items(), key=lambda kv: (-kv[1], kv[0]))
        expected_node_indices = [ni for ni, _ in expected]
        observed_node_indices: list[int] = []
        for e in entries:
            if not isinstance(e, dict) or not isinstance(e.get("node_index"), int):
                ranking_ok = False
                ranking_error = "ranking entry missing node_index"
                break
            observed_node_indices.append(int(e["node_index"]))

        if ranking_ok:
            top_k = export_obj.get("top_k")
            top_k_int = int(top_k) if isinstance(top_k, int) and top_k > 0 else None
            if top_k_int is not None:
                if expected_node_indices[:top_k_int] != observed_node_indices[:top_k_int]:
                    ranking_ok = False
                    ranking_error = "top_k ordering mismatch"
            else:
                if expected_node_indices != observed_node_indices:
                    ranking_ok = False
                    ranking_error = "full ordering mismatch"

    passed = bool(missing_fields_count == 0 and max_abs_err <= float(tol) and ranking_ok)

    return ScenarioResult(
        "S1",
        "Export schema + explanation coherence",
        passed,
        {
            "tol": float(tol),
            "missing_fields_count": int(missing_fields_count),
            "max_abs_err_intrinsic_plus_network_minus_E_eff": float(max_abs_err),
            "ranking_ok": bool(ranking_ok),
            "ranking_error": ranking_error,
        },
    )


def _scenario_v2_s2_intrinsic_source_value_uplift(
    *,
    student_ids: list[str],
    s: np.ndarray,
    C: np.ndarray,
    rho: np.ndarray,
    beta0: float,
    beta1: float,
    node_index: int,
    delta: float,
    top_k: int,
) -> ScenarioResult:
    n = int(s.shape[0])
    if node_index < 0 or node_index >= n:
        return ScenarioResult(
            "S2",
            "Intrinsic source value uplift (re-solve)",
            False,
            {"error": f"node_index out of range: {node_index}"},
        )

    v0 = _solve_v(C=C, s=s)
    E0 = _compute_E_eff(s=s, v=v0, rho=rho, beta0=beta0, beta1=beta1)

    s_cf = np.array(s, dtype=float)
    s_cf[node_index] = float(s_cf[node_index] + float(delta))
    v_cf = _solve_v(C=C, s=s_cf)
    E_cf = _compute_E_eff(s=s_cf, v=v_cf, rho=rho, beta0=beta0, beta1=beta1)

    base_rank = {i: r for r, i in enumerate(_ranking_indices_by_policy(E0, top_k=n), start=1)}
    cf_rank = {i: r for r, i in enumerate(_ranking_indices_by_policy(E_cf, top_k=n), start=1)}

    score_increased = bool(E_cf[node_index] > E0[node_index])
    rank_not_worse = bool(cf_rank[node_index] <= base_rank[node_index])

    baseline_top = _ranking_indices_by_policy(E0, top_k=top_k)
    cf_top = _ranking_indices_by_policy(E_cf, top_k=top_k)

    passed = bool(score_increased and rank_not_worse)

    return ScenarioResult(
        "S2",
        "Intrinsic source value uplift (re-solve)",
        passed,
        {
            "node_index": int(node_index),
            "student_id": student_ids[node_index],
            "delta": float(delta),
            "baseline": {"E_eff": float(E0[node_index]), "rank": int(base_rank[node_index])},
            "counterfactual": {"E_eff": float(E_cf[node_index]), "rank": int(cf_rank[node_index])},
            "checks": {"score_increased": score_increased, "rank_not_worse": rank_not_worse},
            "baseline_top_k_node_indices": baseline_top,
            "counterfactual_top_k_node_indices": cf_top,
        },
    )


def _scenario_v2_s3_network_intervention_strengthen_pair(
    *,
    student_ids: list[str],
    w_directed: dict[tuple[str, str], float],
    s: np.ndarray,
    rho: np.ndarray,
    beta0: float,
    beta1: float,
    i: int,
    j: int,
    delta_w: float,
    alpha: float,
    jitter: float,
) -> ScenarioResult:
    n = int(s.shape[0])
    if i < 0 or i >= n or j < 0 or j >= n or i == j:
        return ScenarioResult(
            "S3",
            "Network intervention (tie strengthen -> regenerate C -> re-solve)",
            False,
            {"error": "invalid i/j"},
        )

    sid_i = student_ids[i]
    sid_j = student_ids[j]

    C0 = _coupling_operator_from_ties(
        student_ids=student_ids, w_directed=w_directed, alpha=alpha, jitter=jitter
    )
    v0 = _solve_v(C=C0, s=s)

    w_cf = dict(w_directed)
    w_cf[(sid_i, sid_j)] = float(w_cf.get((sid_i, sid_j), 0.0) + float(delta_w))
    w_cf[(sid_j, sid_i)] = float(w_cf.get((sid_j, sid_i), 0.0) + float(delta_w))

    C1 = _coupling_operator_from_ties(
        student_ids=student_ids, w_directed=w_cf, alpha=alpha, jitter=jitter
    )
    v1 = _solve_v(C=C1, s=s)

    E0 = _compute_E_eff(s=s, v=v0, rho=rho, beta0=beta0, beta1=beta1)
    E1 = _compute_E_eff(s=s, v=v1, rho=rho, beta0=beta0, beta1=beta1)

    gap0 = float(abs(float(v0[i]) - float(v0[j])))
    gap1 = float(abs(float(v1[i]) - float(v1[j])))

    smoothing = bool(gap1 <= gap0 + 1e-12)
    solvable = bool(np.isfinite(v1).all())

    passed = bool(smoothing and solvable)

    return ScenarioResult(
        "S3",
        "Network intervention (tie strengthen -> regenerate C -> re-solve)",
        passed,
        {
            "pair": {"i": int(i), "j": int(j), "student_id_i": sid_i, "student_id_j": sid_j},
            "delta_w": float(delta_w),
            "alpha": float(alpha),
            "jitter": float(jitter),
            "gap_abs_v_i_minus_v_j": {"baseline": gap0, "counterfactual": gap1},
            "checks": {"smoothing_gap_not_increase": smoothing, "solvable": solvable},
            "E_eff_pair": {
                "baseline": {"i": float(E0[i]), "j": float(E0[j])},
                "counterfactual": {"i": float(E1[i]), "j": float(E1[j])},
            },
        },
    )


def _scenario_v2_s4_network_intervention_weaken_pair(
    *,
    student_ids: list[str],
    w_directed: dict[tuple[str, str], float],
    s: np.ndarray,
    rho: np.ndarray,
    beta0: float,
    beta1: float,
    i: int,
    j: int,
    delta_w: float,
    alpha: float,
    jitter: float,
) -> ScenarioResult:
    n = int(s.shape[0])
    if i < 0 or i >= n or j < 0 or j >= n or i == j:
        return ScenarioResult(
            "S4",
            "Network intervention (tie weaken -> regenerate C -> re-solve)",
            False,
            {"error": "invalid i/j"},
        )

    sid_i = student_ids[i]
    sid_j = student_ids[j]

    C0 = _coupling_operator_from_ties(
        student_ids=student_ids, w_directed=w_directed, alpha=alpha, jitter=jitter
    )
    v0 = _solve_v(C=C0, s=s)

    w_cf = dict(w_directed)
    w_cf[(sid_i, sid_j)] = float(max(0.0, float(w_cf.get((sid_i, sid_j), 0.0)) - float(delta_w)))
    w_cf[(sid_j, sid_i)] = float(max(0.0, float(w_cf.get((sid_j, sid_i), 0.0)) - float(delta_w)))

    C1 = _coupling_operator_from_ties(
        student_ids=student_ids, w_directed=w_cf, alpha=alpha, jitter=jitter
    )
    v1 = _solve_v(C=C1, s=s)

    E0 = _compute_E_eff(s=s, v=v0, rho=rho, beta0=beta0, beta1=beta1)
    E1 = _compute_E_eff(s=s, v=v1, rho=rho, beta0=beta0, beta1=beta1)

    gap0 = float(abs(float(v0[i]) - float(v0[j])))
    gap1 = float(abs(float(v1[i]) - float(v1[j])))

    decoupling = bool(gap1 >= gap0 - 1e-12)
    solvable = bool(np.isfinite(v1).all())
    passed = bool(decoupling and solvable)

    return ScenarioResult(
        "S4",
        "Network intervention (tie weaken -> regenerate C -> re-solve)",
        passed,
        {
            "pair": {"i": int(i), "j": int(j), "student_id_i": sid_i, "student_id_j": sid_j},
            "delta_w": float(delta_w),
            "alpha": float(alpha),
            "jitter": float(jitter),
            "gap_abs_v_i_minus_v_j": {"baseline": gap0, "counterfactual": gap1},
            "checks": {"decoupling_gap_not_decrease": decoupling, "solvable": solvable},
            "E_eff_pair": {
                "baseline": {"i": float(E0[i]), "j": float(E0[j])},
                "counterfactual": {"i": float(E1[i]), "j": float(E1[j])},
            },
        },
    )


def _scenario_v2_s5_intrinsic_source_value_uplift_spillover(
    *,
    student_ids: list[str],
    s: np.ndarray,
    C: np.ndarray,
    rho: np.ndarray,
    beta0: float,
    beta1: float,
    node_index: int,
    delta: float,
    w_directed: dict[tuple[str, str], float],
) -> ScenarioResult:
    n = int(s.shape[0])
    if node_index < 0 or node_index >= n:
        return ScenarioResult(
            "S5",
            "Intrinsic source value uplift spillover (re-solve)",
            False,
            {"error": f"node_index out of range: {node_index}"},
        )

    v0 = _solve_v(C=C, s=s)
    E0 = _compute_E_eff(s=s, v=v0, rho=rho, beta0=beta0, beta1=beta1)

    s_cf = np.array(s, dtype=float)
    s_cf[node_index] = float(s_cf[node_index] + float(delta))
    v1 = _solve_v(C=C, s=s_cf)
    E1 = _compute_E_eff(s=s_cf, v=v1, rho=rho, beta0=beta0, beta1=beta1)

    dv = v1 - v0
    dE = E1 - E0

    # Spillover: at least one other node experiences a measurable dv.
    tol = 1e-10
    spillover_nodes = [int(i) for i in range(n) if i != node_index and abs(float(dv[i])) > tol]
    spillover_exists = bool(len(spillover_nodes) > 0)

    # Connectivity-weighted sanity check: nodes more strongly tied to the uplifted node
    # should, on average, see larger absolute dv than very weakly connected nodes.
    sid0 = student_ids[node_index]
    strength_to_uplift = np.zeros(n, dtype=float)
    for j, sid in enumerate(student_ids):
        if j == node_index:
            continue
        w01 = float(w_directed.get((sid0, sid), 0.0))
        w10 = float(w_directed.get((sid, sid0), 0.0))
        strength_to_uplift[j] = 0.5 * (w01 + w10)

    hi = [i for i in range(n) if i != node_index and strength_to_uplift[i] > 0]
    lo = [i for i in range(n) if i != node_index and strength_to_uplift[i] == 0]

    connectivity_check = True
    hi_mean = None
    lo_mean = None
    if len(hi) >= 3 and len(lo) >= 3:
        hi_mean = float(np.mean(np.abs(dv[hi])))
        lo_mean = float(np.mean(np.abs(dv[lo])))
        connectivity_check = bool(hi_mean >= lo_mean - 1e-12)

    passed = bool(spillover_exists and connectivity_check)

    return ScenarioResult(
        "S5",
        "Intrinsic source value uplift spillover (re-solve)",
        passed,
        {
            "node_index": int(node_index),
            "student_id": sid0,
            "delta": float(delta),
            "checks": {
                "spillover_exists": spillover_exists,
                "connectivity_weighted_dv_check": connectivity_check,
            },
            "spillover_node_count": int(len(spillover_nodes)),
            "spillover_node_indices_sample": spillover_nodes[:10],
            "dv_max_abs": float(np.max(np.abs(dv))),
            "dE_max_abs": float(np.max(np.abs(dE))),
            "connectivity_summary": {
                "hi_group_size": int(len(hi)),
                "lo_group_size": int(len(lo)),
                "hi_mean_abs_dv": None if hi_mean is None else float(hi_mean),
                "lo_mean_abs_dv": None if lo_mean is None else float(lo_mean),
            },
        },
    )


def _scenario_v2_s6_receptivity_only_change(
    *,
    student_ids: list[str],
    s: np.ndarray,
    v: np.ndarray,
    rho: np.ndarray,
    beta0: float,
    beta1: float,
    node_index: int,
    delta_rho: float,
    top_k: int,
) -> ScenarioResult:
    n = int(s.shape[0])
    if node_index < 0 or node_index >= n:
        return ScenarioResult(
            "S6",
            "Receptivity-only change (rho)",
            False,
            {"error": f"node_index out of range: {node_index}"},
        )

    E0 = _compute_E_eff(s=s, v=v, rho=rho, beta0=beta0, beta1=beta1)

    rho_cf = np.array(rho, dtype=float)
    rho_cf[node_index] = float(rho_cf[node_index] + float(delta_rho))
    E1 = _compute_E_eff(s=s, v=v, rho=rho_cf, beta0=beta0, beta1=beta1)

    expected_delta = float(beta1 * float(delta_rho) * float(v[node_index]))
    observed_delta = float(E1[node_index] - E0[node_index])
    delta_ok = bool(abs(observed_delta - expected_delta) <= 1e-12)

    # No other nodes should change.
    others_max_abs = float(np.max(np.abs(np.delete(E1 - E0, node_index)))) if n > 1 else 0.0
    others_unchanged = bool(others_max_abs <= 1e-12)

    base_rank = {i: r for r, i in enumerate(_ranking_indices_by_policy(E0, top_k=n), start=1)}
    cf_rank = {i: r for r, i in enumerate(_ranking_indices_by_policy(E1, top_k=n), start=1)}

    baseline_top = _ranking_indices_by_policy(E0, top_k=top_k)
    cf_top = _ranking_indices_by_policy(E1, top_k=top_k)

    passed = bool(delta_ok and others_unchanged)

    return ScenarioResult(
        "S6",
        "Receptivity-only change (rho)",
        passed,
        {
            "node_index": int(node_index),
            "student_id": student_ids[node_index],
            "delta_rho": float(delta_rho),
            "expected_delta_E_eff": expected_delta,
            "observed_delta_E_eff": observed_delta,
            "others_unchanged_max_abs": others_max_abs,
            "checks": {"delta_exact": delta_ok, "others_unchanged": others_unchanged},
            "baseline": {"E_eff": float(E0[node_index]), "rank": int(base_rank[node_index])},
            "counterfactual": {"E_eff": float(E1[node_index]), "rank": int(cf_rank[node_index])},
            "baseline_top_k_node_indices": baseline_top,
            "counterfactual_top_k_node_indices": cf_top,
        },
    )


def main() -> int:
    repo_root = _find_repo_root(Path(__file__))
    artifacts_root = repo_root / "affinity" / "artifacts" / "n50"
    static_dir = artifacts_root / "static"
    artifacts_dir = artifacts_root / "generated" / "latest"

    export_path = artifacts_dir / "app_facing_outputs_v2.json"
    ties_path = artifacts_dir / "tie_strengths_w_v2.json"

    scenarios_path = artifacts_dir / "product_validity_scenarios_v2.json"
    outputs_path = artifacts_dir / "product_validity_outputs_v2.json"
    note_path = artifacts_dir / "product_validity_evaluation_note_v2.txt"

    if not export_path.exists():
        raise FileNotFoundError(str(export_path))
    if not ties_path.exists():
        raise FileNotFoundError(str(ties_path))

    student_ids, s, C, v, rho, beta = _load_v2_vectors(artifacts_dir=artifacts_dir)
    beta0 = float(beta[0])
    beta1 = float(beta[1])

    export_obj = _load_json(export_path)
    if not isinstance(export_obj, dict):
        raise TypeError("app_facing_outputs_v2.json must be a JSON object")

    w_directed = _w_directed_from_ties(_load_json(ties_path))

    tol = 1e-12
    top_k = int(export_obj.get("top_k", 10))

    s2_node_index = 0
    s2_delta = 0.25

    s3_i = 0
    s3_j = 1
    s3_delta_w = 10.0

    s4_i = 0
    s4_j = 1
    s4_delta_w = 10.0

    s5_node_index = 0
    s5_delta = 0.25

    s6_node_index = 0
    s6_delta_rho = 0.05

    C_policy = _load_json(artifacts_dir / "coupling_operator_C_v2.json").get("policy", {})
    alpha = float(C_policy.get("alpha", 1.0)) if isinstance(C_policy, dict) else 1.0
    jitter = float(C_policy.get("jitter", 1e-6)) if isinstance(C_policy, dict) else 1e-6

    timestamp_utc = datetime.now(timezone.utc).isoformat()

    scenario_defs = {
        "schema_version": "1.0",
        "name": "affinity_product_validity_scenarios_v2",
        "timestamp_utc": timestamp_utc,
        "git_head_sha": _try_git_head_sha(repo_root),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "inputs": {
            "export_ref": "affinity/artifacts/n50/generated/latest/app_facing_outputs_v2.json",
            "ties_ref": "affinity/artifacts/n50/generated/latest/tie_strengths_w_v2.json",
            "source_vector_ref": "affinity/artifacts/n50/generated/latest/source_vector_s_v2.json",
            "coupling_operator_ref": "affinity/artifacts/n50/generated/latest/coupling_operator_C_v2.json",
        },
        "frozen_parameters": {
            "tol": tol,
            "S2": {"node_index": s2_node_index, "delta_s": s2_delta},
            "S3": {"i": s3_i, "j": s3_j, "delta_w": s3_delta_w, "alpha": alpha, "jitter": jitter},
            "S4": {"i": s4_i, "j": s4_j, "delta_w": s4_delta_w, "alpha": alpha, "jitter": jitter},
            "S5": {"node_index": s5_node_index, "delta_s": s5_delta},
            "S6": {"node_index": s6_node_index, "delta_rho": s6_delta_rho},
        },
        "scenarios": [
            {
                "scenario_id": "S1",
                "name": "Export schema + explanation coherence",
                "expectation": {
                    "description": "Each student has explanation fields and intrinsic+network == E_eff within tol; rankings match (-E_eff, node_index)."
                },
            },
            {
                "scenario_id": "S2",
                "name": "Intrinsic source value uplift (re-solve)",
                "expectation": {
                    "description": "Uplifting one node's intrinsic source value s_i by +delta and re-solving C v = s increases its E_eff and does not worsen its rank."
                },
            },
            {
                "scenario_id": "S3",
                "name": "Network intervention (strengthen tie pair -> regenerate C -> re-solve)",
                "expectation": {
                    "description": "Strengthening a tie between two nodes should not increase the absolute gap |v_i - v_j| (smoothing effect) after regenerating C and re-solving."
                },
            },
            {
                "scenario_id": "S4",
                "name": "Network intervention (weaken tie pair -> regenerate C -> re-solve)",
                "expectation": {
                    "description": "Weakening a tie between two nodes should not decrease the absolute gap |v_i - v_j| (decoupling effect) after regenerating C and re-solving."
                },
            },
            {
                "scenario_id": "S5",
                "name": "Intrinsic source value uplift spillover (re-solve)",
                "expectation": {
                    "description": "Uplifting one node's intrinsic source value s_i and re-solving should produce non-trivial network spillovers (other nodes' v change); more connected nodes should (weakly) show larger changes on average."
                },
            },
            {
                "scenario_id": "S6",
                "name": "Receptivity-only change (rho)",
                "expectation": {
                    "description": "Changing one node's rho should change only that node's E_eff by exactly beta1*(delta_rho)*v_i, with all other nodes unchanged."
                },
            },
        ],
    }

    r1 = _scenario_v2_s1_export_coherence(artifacts_dir=artifacts_dir, tol=tol)
    r2 = _scenario_v2_s2_intrinsic_source_value_uplift(
        student_ids=student_ids,
        s=s,
        C=C,
        rho=rho,
        beta0=beta0,
        beta1=beta1,
        node_index=s2_node_index,
        delta=s2_delta,
        top_k=top_k,
    )
    r3 = _scenario_v2_s3_network_intervention_strengthen_pair(
        student_ids=student_ids,
        w_directed=w_directed,
        s=s,
        rho=rho,
        beta0=beta0,
        beta1=beta1,
        i=s3_i,
        j=s3_j,
        delta_w=s3_delta_w,
        alpha=alpha,
        jitter=jitter,
    )

    r4 = _scenario_v2_s4_network_intervention_weaken_pair(
        student_ids=student_ids,
        w_directed=w_directed,
        s=s,
        rho=rho,
        beta0=beta0,
        beta1=beta1,
        i=s4_i,
        j=s4_j,
        delta_w=s4_delta_w,
        alpha=alpha,
        jitter=jitter,
    )

    r5 = _scenario_v2_s5_intrinsic_source_value_uplift_spillover(
        student_ids=student_ids,
        s=s,
        C=C,
        rho=rho,
        beta0=beta0,
        beta1=beta1,
        node_index=s5_node_index,
        delta=s5_delta,
        w_directed=w_directed,
    )

    r6 = _scenario_v2_s6_receptivity_only_change(
        student_ids=student_ids,
        s=s,
        v=v,
        rho=rho,
        beta0=beta0,
        beta1=beta1,
        node_index=s6_node_index,
        delta_rho=s6_delta_rho,
        top_k=top_k,
    )

    all_passed = bool(r1.passed and r2.passed and r3.passed and r4.passed and r5.passed and r6.passed)

    outputs = {
        "schema_version": "1.0",
        "name": "affinity_product_validity_outputs_v2",
        "timestamp_utc": timestamp_utc,
        "git_head_sha": _try_git_head_sha(repo_root),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "results": [
            {"scenario_id": r1.scenario_id, "name": r1.name, "passed": r1.passed, "details": r1.details},
            {"scenario_id": r2.scenario_id, "name": r2.name, "passed": r2.passed, "details": r2.details},
            {"scenario_id": r3.scenario_id, "name": r3.name, "passed": r3.passed, "details": r3.details},
            {"scenario_id": r4.scenario_id, "name": r4.name, "passed": r4.passed, "details": r4.details},
            {"scenario_id": r5.scenario_id, "name": r5.name, "passed": r5.passed, "details": r5.details},
            {"scenario_id": r6.scenario_id, "name": r6.name, "passed": r6.passed, "details": r6.details},
        ],
        "overall": {"passed": all_passed},
    }

    note_lines: list[str] = []
    note_lines.append("Job 14 — Product validity checks — evaluation note (v2)")
    note_lines.append("")
    note_lines.append(f"timestamp_utc: {timestamp_utc}")
    note_lines.append(f"git_head_sha: {_try_git_head_sha(repo_root)}")
    note_lines.append(f"python: {sys.version.split()[0]}")
    note_lines.append(f"platform: {platform.platform()}")
    note_lines.append("")

    def _fmt_result(r: ScenarioResult) -> None:
        note_lines.append(f"{r.scenario_id} — {r.name}")
        note_lines.append(f"- passed: {r.passed}")
        note_lines.append("")

    _fmt_result(r1)
    _fmt_result(r2)
    _fmt_result(r3)
    _fmt_result(r4)
    _fmt_result(r5)
    _fmt_result(r6)

    note_lines.append("Conclusion")
    note_lines.append(f"- overall_passed: {all_passed}")
    note_lines.append("")

    _write_json(scenarios_path, scenario_defs)
    _write_json(outputs_path, outputs)
    note_path.write_text("\n".join(note_lines) + "\n")

    print("==============================================================================")
    print("Job 14 — Affinity n=50 product validity checks (v2)")
    print("==============================================================================")
    print(f"timestamp_utc: {timestamp_utc}")
    print(f"python: {sys.version.split()[0]}")
    print(f"platform: {platform.platform()}")
    print(f"git_head_sha: {_try_git_head_sha(repo_root)}")
    print("")

    for r in (r1, r2, r3, r4, r5, r6):
        print("------------------------------------------------------------------------------")
        print(f"{r.scenario_id}: {r.name}")
        print("PASS" if r.passed else "FAIL")

    print("------------------------------------------------------------------------------")
    print("Overall")
    print("PASS" if all_passed else "FAIL")
    print("")

    print(f"WROTE: {scenarios_path}")
    print(f"WROTE: {outputs_path}")
    print(f"WROTE: {note_path}")

    return 0 if all_passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
