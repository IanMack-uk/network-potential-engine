from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import numpy as np


def _find_repo_root(start: Path) -> Path:
    p = start
    while True:
        if (p / ".git").exists() or (p / "pyproject.toml").exists():
            return p
        if p.parent == p:
            raise RuntimeError("Could not locate repo root (.git or pyproject.toml)")
        p = p.parent


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def _write_json(path: Path, obj: Any) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=False) + "\n")


def _stable_u01(seed: str) -> float:
    h = hashlib.sha256(seed.encode("utf-8")).digest()
    x = int.from_bytes(h[:8], "big", signed=False)
    return (x % (10**12)) / float(10**12)


def _with_seed_prefix(*, scenario_seed: str | None, key: str) -> str:
    if scenario_seed is None:
        return key
    return f"scenario_seed::{scenario_seed}::{key}"


def _tier_1_to_5(x: str) -> int:
    m = {"very_low": 1, "low": 2, "medium": 3, "high": 4, "very_high": 5}
    if x not in m:
        raise ValueError(f"Unexpected tier enum: {x!r}")
    return int(m[x])


def _rho(cat: str) -> float:
    m = {
        "innovator": 0.90,
        "early_adopter": 0.95,
        "early_majority": 1.00,
        "late_majority": 1.05,
        "laggard": 1.10,
    }
    if cat not in m:
        raise ValueError(f"Unexpected adopterCategory enum: {cat!r}")
    return float(m[cat])


def _attendance_propensity(*, student_id: str, scenario_seed: str | None) -> float:
    u = 2.0 * _stable_u01(_with_seed_prefix(scenario_seed=scenario_seed, key=f"a::{student_id}")) - 1.0
    a = 0.55 + 0.15 * u
    return float(min(0.95, max(0.20, a)))


def _load_registry_student_ids(registry_path: Path) -> list[str]:
    obj = _load_json(registry_path)
    nodes = obj.get("nodes")
    if not isinstance(nodes, list):
        raise ValueError("registry.nodes must be a list")
    nodes_sorted = sorted(nodes, key=lambda x: int(x["node_index"]))
    return [n["student_id"] for n in nodes_sorted]


def _load_personal_props(personal_props_path: Path) -> dict[str, dict[str, Any]]:
    raw = _load_json(personal_props_path)
    if not isinstance(raw, list):
        raise ValueError("Expected list at top-level of n50_student_personal_properties.json")
    out: dict[str, dict[str, Any]] = {}
    for rec in raw:
        student = rec.get("student")
        if not isinstance(student, dict):
            continue
        sid = student.get("id")
        if isinstance(sid, str) and sid:
            out[sid] = student
    return out


def _load_shared_tags(shared_tags_path: Path) -> dict[tuple[str, str], int]:
    raw = _load_json(shared_tags_path)
    if not isinstance(raw, list):
        raise ValueError("Expected list at top-level of n5_students_module_share_tags.json")
    out: dict[tuple[str, str], int] = {}
    for rec in raw:
        dn = rec.get("displayName")
        title = rec.get("title")
        t = rec.get("sharedTagCount")
        if isinstance(dn, str) and isinstance(title, str) and isinstance(t, int):
            out[(dn, title)] = int(t)
    return out


def _reconstruct_tridiagonal_matrix(*, main: np.ndarray, off: np.ndarray) -> np.ndarray:
    n = int(main.shape[0])
    C = np.diag(main)
    C += np.diag(off, 1)
    C += np.diag(off, -1)
    return C


def _coupling_operator_from_ties(
    *,
    student_ids: list[str],
    w_directed: dict[tuple[str, str], float],
    alpha: float = 1.0,
    jitter: float = 1e-6,
) -> tuple[np.ndarray, dict[str, Any]]:
    """Build an SPD coupling operator from tie strengths.

    Policy (frozen for Option B v2):
      - Symmetricize directed ties: w_sym(i,j) = 0.5*(w_ij + w_ji)
      - Scale weights by mean nonzero w_sym to keep magnitudes stable.
      - Graph Laplacian: L = D - W_sym
      - Coupling operator: C = I + alpha*L + jitter*I  (SPD)

    Returns:
      C: np.ndarray (n,n)
      policy: JSON-serializable policy object to embed in artifact.
    """

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
        # We store directed weights in a dense matrix first.
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

    policy = {
        "type": "laplacian_from_ties",
        "symmetrization": "w_sym(i,j)=0.5*(w_ij+w_ji)",
        "scaling": {
            "type": "divide_by_mean_nonzero_w_sym",
            "mean_nonzero_w_sym": scale,
        },
        "laplacian": "L = D - W_sym_scaled",
        "definition": "C = I + alpha*L + jitter*I",
        "alpha": float(alpha),
        "jitter": float(jitter),
    }
    return C, policy


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--seed",
        default=None,
        help="Optional scenario seed. If provided, the simulated observations/ties will change deterministically while remaining reproducible.",
    )
    parser.add_argument(
        "--audit",
        action="store_true",
        help="Print an end-to-end audit report to stdout and write it to an artifact text file.",
    )
    args = parser.parse_args()

    scenario_seed = str(args.seed) if args.seed is not None else None

    repo_root = _find_repo_root(Path(__file__).resolve())
    artifacts_dir = repo_root / "affinity" / "artifacts" / "n50"
    neo4j_dir = repo_root / "affinity" / "from_neo4j"

    registry_path = artifacts_dir / "student_registry_v1.json"
    coupling_C_v1_path = artifacts_dir / "coupling_operator_C_v1.json"
    personal_props_path = neo4j_dir / "n50_student_personal_properties.json"
    shared_tags_path = neo4j_dir / "n5_students_module_share_tags.json"
    participation_graph_path = neo4j_dir / "n50-student-participation-graph.json"

    for p in [registry_path, coupling_C_v1_path, personal_props_path, shared_tags_path, participation_graph_path]:
        if not p.exists():
            raise FileNotFoundError(str(p))

    student_ids = _load_registry_student_ids(registry_path)
    people = _load_personal_props(personal_props_path)

    for sid in student_ids:
        if sid not in people:
            raise ValueError(f"student_id from registry missing in personal properties: {sid}")

    shared_tags = _load_shared_tags(shared_tags_path)
    module_titles = sorted({title for (_, title) in shared_tags.keys()})

    s_entries: list[dict[str, Any]] = []
    s_vec = np.zeros(len(student_ids), dtype=float)
    rho_vec = np.zeros(len(student_ids), dtype=float)
    a_vec = np.zeros(len(student_ids), dtype=float)

    for i, sid in enumerate(student_ids):
        st = people[sid]
        q = _tier_1_to_5(str(st["outputQuality"]))
        p = _tier_1_to_5(str(st["outputProductivity"]))
        s_i = (float(q) * float(p)) / 9.0
        s_entries.append({"student_id": sid, "s": s_i})
        s_vec[i] = s_i
        rho_vec[i] = _rho(str(st["adopterCategory"]))
        a_vec[i] = _attendance_propensity(student_id=sid, scenario_seed=scenario_seed)

    # Simulate attendance and co-attendance observations
    events: list[dict[str, Any]] = []
    w: dict[tuple[str, str], float] = {}
    attendance_counts: dict[str, int] = {sid: 0 for sid in student_ids}

    t0 = datetime(2026, 3, 1, tzinfo=timezone.utc)
    evt_counter = 1
    n_sessions_per_module = 8

    for m_idx, title in enumerate(module_titles):
        for sess in range(n_sessions_per_module):
            ts = t0 + timedelta(days=7 * m_idx, hours=2 * sess)
            attendees: list[str] = []
            for sid in student_ids:
                st = people[sid]
                dn = str(st.get("displayName", ""))
                t = int(shared_tags.get((dn, title), 0))
                a_i = _attendance_propensity(student_id=sid, scenario_seed=scenario_seed)
                mult = 1.0 + 0.05 * float(t)
                p_attend = min(1.0, a_i * mult)
                if (
                    _stable_u01(
                        _with_seed_prefix(
                            scenario_seed=scenario_seed, key=f"attend::{sid}::{title}::{sess}"
                        )
                    )
                    < p_attend
                ):
                    attendees.append(sid)

            attendees.sort()
            for sid in attendees:
                attendance_counts[sid] = int(attendance_counts.get(sid, 0) + 1)
            for ii in range(len(attendees)):
                for jj in range(ii + 1, len(attendees)):
                    a = attendees[ii]
                    b = attendees[jj]
                    for actor, target in ((a, b), (b, a)):
                        events.append(
                            {
                                "event_id": f"evt_{evt_counter:06d}",
                                "timestamp": ts.isoformat().replace("+00:00", "Z"),
                                "event_type": "interaction",
                                "actor_student_id": actor,
                                "target_student_id": target,
                                "weight": 1.0,
                                "channel": "co_attendance",
                                "metadata": {"pii": False, "module_title": title},
                            }
                        )
                        evt_counter += 1
                        w[(actor, target)] = float(w.get((actor, target), 0.0) + 1.0)

    _write_json(
        artifacts_dir / "observations_v2.json",
        {
            "schema_version": "1.0",
            "schema_ref": "affinity/artifacts/n50/observations_schema_v1.json",
            "cohort_registry_ref": "affinity/artifacts/n50/student_registry_v1.json",
            "generated": {"method": "optionB_v2_attendance_simulation", "scenario_seed": scenario_seed},
            "events": events,
        },
    )

    _write_json(
        artifacts_dir / "source_vector_s_v2.json",
        {
            "schema_version": "1.0",
            "name": "affinity_source_vector_s_v2",
            "cohort_registry_ref": "affinity/artifacts/n50/student_registry_v1.json",
            "definition": "s_i = (Q_i * P_i) / 9.0",
            "s": s_entries,
        },
    )

    # Tie weights (derived) as a simple artifact
    ties = []
    for (a, b), wt in sorted(w.items(), key=lambda x: (x[0][0], x[0][1])):
        ties.append({"actor_student_id": a, "target_student_id": b, "w": float(wt)})

    _write_json(
        artifacts_dir / "tie_strengths_w_v2.json",
        {
            "schema_version": "1.0",
            "name": "affinity_tie_strengths_w_v2",
            "cohort_registry_ref": "affinity/artifacts/n50/student_registry_v1.json",
            "observations_ref": "affinity/artifacts/n50/observations_v2.json",
            "definition": "w_ij = sum(weight) over events with actor=i and target=j",
            "ties": ties,
        },
    )

    # Build and write data-driven coupling operator C_v2 from v2 ties
    C_v2, C_v2_policy = _coupling_operator_from_ties(student_ids=student_ids, w_directed=w)
    _write_json(
        artifacts_dir / "coupling_operator_C_v2.json",
        {
            "schema_version": "1.0",
            "name": "affinity_coupling_operator_C_v2",
            "cohort_registry_ref": "affinity/artifacts/n50/student_registry_v1.json",
            "ties_ref": "affinity/artifacts/n50/tie_strengths_w_v2.json",
            "format": {"type": "symmetric_dense", "matrix": [[float(x) for x in row] for row in C_v2.tolist()]},
            "policy": C_v2_policy,
        },
    )

    # Propagation + energies using data-driven C_v2
    v = np.linalg.solve(C_v2, s_vec)

    _write_json(
        artifacts_dir / "propagated_value_v_v2.json",
        {
            "schema_version": "1.0",
            "name": "affinity_propagated_value_v_v2",
            "cohort_registry_ref": "affinity/artifacts/n50/student_registry_v1.json",
            "source_vector_ref": "affinity/artifacts/n50/source_vector_s_v2.json",
            "coupling_operator_C_ref": "affinity/artifacts/n50/coupling_operator_C_v2.json",
            "definition": "v = G s, computed by solving C v = s",
            "ordering": "node_index_ascending",
            "method": {"type": "solve", "solver": "numpy.linalg.solve", "numpy_only": True},
            "v": [float(x) for x in v.reshape(-1)],
        },
    )

    beta0 = 1.0
    beta1 = 1.0
    E = beta0 * s_vec + beta1 * v
    E_eff = beta0 * s_vec + beta1 * (rho_vec * v)

    _write_json(
        artifacts_dir / "node_energy_E_v2.json",
        {
            "schema_version": "1.0",
            "name": "affinity_node_energy_E_v2",
            "cohort_registry_ref": "affinity/artifacts/n50/student_registry_v1.json",
            "source_vector_ref": "affinity/artifacts/n50/source_vector_s_v2.json",
            "propagated_value_v_ref": "affinity/artifacts/n50/propagated_value_v_v2.json",
            "definition": "E = beta0*s + beta1*v",
            "ordering": "node_index_ascending",
            "parameters": {"beta0": beta0, "beta1": beta1},
            "E": [float(x) for x in E.reshape(-1)],
        },
    )

    _write_json(
        artifacts_dir / "node_energy_E_eff_v2.json",
        {
            "schema_version": "1.0",
            "name": "affinity_node_energy_E_eff_v2",
            "cohort_registry_ref": "affinity/artifacts/n50/student_registry_v1.json",
            "source_vector_ref": "affinity/artifacts/n50/source_vector_s_v2.json",
            "propagated_value_v_ref": "affinity/artifacts/n50/propagated_value_v_v2.json",
            "definition": "E_eff = beta0*s + beta1*(rho ⊙ v)",
            "ordering": "node_index_ascending",
            "parameters": {"beta0": beta0, "beta1": beta1},
            "rho": [float(x) for x in rho_vec.reshape(-1)],
            "E_eff": [float(x) for x in E_eff.reshape(-1)],
        },
    )

    ranking = sorted(range(len(student_ids)), key=lambda i: (-float(E_eff[i]), int(i)))
    top_k = 10
    entries = []
    for rank, i in enumerate(ranking[:top_k], start=1):
        entries.append(
            {"rank": rank, "node_index": int(i), "student_id": student_ids[i], "score": float(E_eff[i])}
        )

    students = []
    for i, sid in enumerate(student_ids):
        students.append(
            {
                "node_index": int(i),
                "student_id": sid,
                "s": float(s_vec[i]),
                "v": float(v[i]),
                "E": float(E[i]),
                "E_eff": float(E_eff[i]),
                "explanation": {
                    "intrinsic_component": float(beta0 * s_vec[i]),
                    "network_component": float(beta1 * (rho_vec[i] * v[i])),
                    "formula": "E_eff = beta0*s + beta1*(rho ⊙ v)",
                },
            }
        )

    _write_json(
        artifacts_dir / "app_facing_outputs_v2.json",
        {
            "schema_version": "1.0",
            "name": "affinity_app_facing_outputs_v2",
            "cohort_registry_ref": "affinity/artifacts/n50/student_registry_v1.json",
            "inputs": {
                "source_vector_ref": "affinity/artifacts/n50/source_vector_s_v2.json",
                "propagated_value_v_ref": "affinity/artifacts/n50/propagated_value_v_v2.json",
                "energy_E_ref": "affinity/artifacts/n50/node_energy_E_v2.json",
                "energy_E_eff_ref": "affinity/artifacts/n50/node_energy_E_eff_v2.json",
            },
            "canonical_score": "E_eff",
            "top_k": top_k,
            "ranking_policy": {"sort_key": "(-score, node_index)", "score_field": "E_eff", "deterministic": True},
            "rankings": {"by_score": "E_eff", "entries": entries},
            "students": students,
        },
    )

    if args.audit:
        n_nodes = len(student_ids)
        total_sessions = len(module_titles) * n_sessions_per_module

        w_out_sum: dict[str, float] = {sid: 0.0 for sid in student_ids}
        w_in_sum: dict[str, float] = {sid: 0.0 for sid in student_ids}
        out_deg: dict[str, int] = {sid: 0 for sid in student_ids}
        in_deg: dict[str, int] = {sid: 0 for sid in student_ids}

        for (actor, target), wt in w.items():
            w_out_sum[actor] = float(w_out_sum.get(actor, 0.0) + float(wt))
            w_in_sum[target] = float(w_in_sum.get(target, 0.0) + float(wt))
            out_deg[actor] = int(out_deg.get(actor, 0) + 1)
            in_deg[target] = int(in_deg.get(target, 0) + 1)

        ranking = sorted(range(n_nodes), key=lambda i: (-float(E_eff[i]), int(i)))
        rank_of: dict[int, int] = {idx: r for r, idx in enumerate(ranking, start=1)}

        lines: list[str] = []
        lines.append("=" * 78)
        lines.append("Affinity n=50 Option B v2 audit report")
        lines.append("=" * 78)
        lines.append(f"timestamp_utc: {datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')}")
        lines.append(f"n_nodes: {n_nodes}")
        lines.append(f"n_modules: {len(module_titles)}")
        lines.append(f"n_sessions_per_module: {n_sessions_per_module}")
        lines.append(f"total_sessions_per_student: {total_sessions}")
        lines.append(f"n_observation_events: {len(events)}")
        lines.append(f"n_directed_ties: {len(ties)}")
        lines.append("")
        lines.append("Frozen policies")
        lines.append("- s_i = (Q_i * P_i) / 9.0")
        lines.append("- Q,P tier mapping: very_low->1 low->2 medium->3 high->4 very_high->5")
        lines.append("- rho mapping: innovator 0.90, early_adopter 0.95, early_majority 1.00, late_majority 1.05, laggard 1.10")
        lines.append("- P(attend) = min(1, a_i * (1 + 0.05*sharedTagCount)), sharedTagCount<=3")
        lines.append(f"- scenario_seed: {scenario_seed}")
        lines.append("")
        lines.append("Summary stats")
        lines.append(
            f"s: min={float(np.min(s_vec)):.6g} mean={float(np.mean(s_vec)):.6g} max={float(np.max(s_vec)):.6g}"
        )
        lines.append(
            f"rho: min={float(np.min(rho_vec)):.6g} mean={float(np.mean(rho_vec)):.6g} max={float(np.max(rho_vec)):.6g}"
        )
        lines.append(
            f"E_eff: min={float(np.min(E_eff)):.6g} mean={float(np.mean(E_eff)):.6g} max={float(np.max(E_eff)):.6g}"
        )
        lines.append("")
        lines.append("Modules (derived from shared tags)")
        for t in module_titles:
            lines.append(f"- {t}")
        lines.append("")

        header = [
            "node_index",
            "rank",
            "displayName",
            "student_id",
            "adopterCategory",
            "outputQuality",
            "outputProductivity",
            "Q",
            "P",
            "s",
            "rho",
            "a_i",
            "sessions_attended",
            "attendance_rate",
            "out_degree",
            "in_degree",
            "w_out_sum",
            "w_in_sum",
            "v",
            "E",
            "E_eff",
        ]
        lines.append("Per-student audit (node_index order)")
        lines.append("\t".join(header))
        for i, sid in enumerate(student_ids):
            st = people[sid]
            dn = str(st.get("displayName", ""))
            adopter = str(st.get("adopterCategory", ""))
            oq = str(st.get("outputQuality", ""))
            op = str(st.get("outputProductivity", ""))
            Q = _tier_1_to_5(oq)
            P = _tier_1_to_5(op)
            attended = int(attendance_counts.get(sid, 0))
            att_rate = attended / float(total_sessions) if total_sessions > 0 else 0.0
            row = [
                str(i),
                str(rank_of[i]),
                dn,
                sid,
                adopter,
                oq,
                op,
                str(Q),
                str(P),
                f"{float(s_vec[i]):.6g}",
                f"{float(rho_vec[i]):.6g}",
                f"{float(a_vec[i]):.6g}",
                str(attended),
                f"{att_rate:.6g}",
                str(int(out_deg.get(sid, 0))),
                str(int(in_deg.get(sid, 0))),
                f"{float(w_out_sum.get(sid, 0.0)):.6g}",
                f"{float(w_in_sum.get(sid, 0.0)):.6g}",
                f"{float(v[i]):.6g}",
                f"{float(E[i]):.6g}",
                f"{float(E_eff[i]):.6g}",
            ]
            lines.append("\t".join(row))

        report_path = artifacts_dir / "optionB_v2_audit_report.txt"
        report_path.write_text("\n".join(lines) + "\n")
        print(report_path.read_text())
        print(f"Wrote audit report: {report_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
