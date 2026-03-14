from __future__ import annotations

import argparse
import json
import os
import platform
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np


def _find_repo_root(start: Path) -> Path:
    p = start
    while True:
        if (p / ".git").exists():
            return p
        if p.parent == p:
            raise RuntimeError("Could not find repo root")
        p = p.parent


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def _format_float(x: float) -> str:
    return f"{x:.16g}"


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


def _tier_1_to_5(x: str) -> int:
    m = {"very_low": 1, "low": 2, "medium": 3, "high": 4, "very_high": 5}
    if x not in m:
        raise ValueError(f"Unexpected tier enum: {x!r}")
    return int(m[x])


def _rho(cat: str) -> float:
    m = {
        "innovator": 1.10,
        "early_adopter": 1.05,
        "early_majority": 1.00,
        "late_majority": 0.95,
        "laggard": 0.90,
    }
    if cat not in m:
        raise ValueError(f"Unexpected adopterCategory enum: {cat!r}")
    return float(m[cat])


def _coupling_operator_from_ties(
    *,
    student_ids: list[str],
    w_directed: dict[tuple[str, str], float],
    alpha: float,
    jitter: float,
) -> tuple[np.ndarray, float]:
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
    return C, scale


def _coupling_intermediates_from_ties(
    *,
    student_ids: list[str],
    w_directed: dict[tuple[str, str], float],
    alpha: float,
    jitter: float,
) -> dict[str, Any]:
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
    return {
        "W": W,
        "W_sym": W_sym,
        "scale": float(scale),
        "W_sym_scaled": W_sym_scaled,
        "d": d,
        "L": L,
        "C": C,
    }


def _check_no_nan_inf(x: np.ndarray, *, name: str) -> None:
    if not np.isfinite(x).all():
        bad = np.where(~np.isfinite(x))[0]
        raise ValueError(f"{name} contains non-finite values at indices: {bad[:10].tolist()}")


def _ranking_indices_by_policy(score: np.ndarray, *, top_k: int) -> list[int]:
    return sorted(range(int(score.shape[0])), key=lambda i: (-float(score[i]), int(i)))[:top_k]


@dataclass(frozen=True)
class _Context:
    repo_root: Path
    artifacts_dir: Path
    static_dir: Path
    neo4j_dir: Path


def _run_step(name: str, fn) -> None:
    print("=" * 78)
    print(f"AFFINITY N50 V2 DATA-DRIVEN CHECK: {name}")
    print("=" * 78)
    fn()
    print()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--full",
        action="store_true",
        help="Print full per-student tables for each stage (large output).",
    )
    parser.add_argument(
        "--regen",
        action="store_true",
        help="Regenerate v2 Affinity n=50 artifacts (Option B) before running checks.",
    )
    parser.add_argument(
        "--neo4j-ties-json",
        type=str,
        default="",
        help=(
            "Optional path (relative to repo root) to Neo4j-exported directed tie weights JSON. "
            "If provided, it will be passed through to the v2 artifact generator during --regen."
        ),
    )
    parser.add_argument(
        "--neo4j-readable-json",
        type=str,
        default="",
        help=(
            "Optional path (relative to repo root) to Neo4j-exported readable tie table JSON. "
            "If provided, it will be passed through to the v2 artifact generator during --regen."
        ),
    )
    parser.add_argument(
        "--seed",
        type=str,
        default="",
        help="Optional scenario seed to pass through to the v2 artifact generator when using --regen.",
    )
    parser.add_argument(
        "--out",
        type=str,
        default="",
        help="If set, also write the full transcript to this path.",
    )
    args = parser.parse_args()

    transcript_lines: list[str] = []

    def emit(line: str = "") -> None:
        print(line)
        transcript_lines.append(line)

    def section(title: str) -> None:
        emit("=" * 78)
        emit(title)
        emit("=" * 78)

    def run_step(*, step_id: str, title: str, fn) -> None:
        section(f"STEP {step_id} BEGIN: {title}")
        fn()
        emit("")
        section(f"STEP {step_id} END: {title}")
        emit("")

    repo_root = _find_repo_root(Path(__file__).resolve())
    ctx = _Context(
        repo_root=repo_root,
        artifacts_dir=repo_root / "affinity" / "artifacts" / "n50" / "generated" / "latest",
        static_dir=repo_root / "affinity" / "artifacts" / "n50" / "static",
        neo4j_dir=repo_root / "affinity" / "from_neo4j",
    )

    if args.regen:
        gen_script = repo_root / "src" / "network_potential_engine" / "scripts" / "run_affinity_n50_generate_artifacts_v2_optionB.py"
        if not gen_script.exists():
            raise RuntimeError(f"Could not find v2 artifact generator script: {gen_script}")

        cmd = [sys.executable, str(gen_script)]
        if args.seed:
            cmd.extend(["--seed", str(args.seed)])
        if args.neo4j_ties_json:
            cmd.extend(["--neo4j-ties-json", str(args.neo4j_ties_json)])
        if args.neo4j_readable_json:
            cmd.extend(["--neo4j-readable-json", str(args.neo4j_readable_json)])

        section("Regen: running v2 artifact generator (Option B)")
        emit("command: " + " ".join(cmd))
        subprocess.check_call(cmd, cwd=str(repo_root))
        emit("")

    section("Affinity n=50 full pipeline check (v2, data-driven)")
    emit(f"timestamp_utc: {datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')}")
    emit(f"python: {platform.python_version()}")
    emit(f"platform: {platform.platform()}")
    sha = _try_git_head_sha(repo_root)
    emit(f"git_head_sha: {sha if sha is not None else 'unknown'}")
    emit(f"pid: {os.getpid()}")
    emit("")

    artifact_paths = {
        "registry": ctx.static_dir / "registry" / "student_registry_v1.json",
        "source_s": ctx.artifacts_dir / "source_vector_s_v2.json",
        "ties": ctx.artifacts_dir / "tie_strengths_w_v2.json",
        "coupling_C": ctx.artifacts_dir / "coupling_operator_C_v2.json",
        "propagated_v": ctx.artifacts_dir / "propagated_value_v_v2.json",
        "energy_E": ctx.artifacts_dir / "node_energy_E_v2.json",
        "energy_E_eff": ctx.artifacts_dir / "node_energy_E_eff_v2.json",
        "export": ctx.artifacts_dir / "app_facing_outputs_v2.json",
        "observations": ctx.artifacts_dir / "observations_v2.json",
        "personal_props": ctx.neo4j_dir / "n50_student_personal_properties.json",
    }

    missing = [str(p) for p in artifact_paths.values() if not p.exists()]
    if missing:
        print("Missing required inputs/artifacts:")
        for m in missing:
            print(f"- {m}")
        return 2

    state: dict[str, Any] = {}

    def step_na(step_label: str) -> None:
        emit("status: N/A")
        emit(
            "reason: this is a symbolic/theorem-only certified spine step; this checker is data-driven and does not reconstruct it from v2 artifacts."
        )
        emit(f"step_label: {step_label}")

    def step_presence() -> None:
        for k, p in artifact_paths.items():
            emit(f"{k}: OK ({p})")

    def step_load() -> None:
        state["registry"] = _load_json(artifact_paths["registry"])
        state["s_obj"] = _load_json(artifact_paths["source_s"])
        state["ties_obj"] = _load_json(artifact_paths["ties"])
        state["C_obj"] = _load_json(artifact_paths["coupling_C"])
        state["v_obj"] = _load_json(artifact_paths["propagated_v"])
        state["E_obj"] = _load_json(artifact_paths["energy_E"])
        state["Eeff_obj"] = _load_json(artifact_paths["energy_E_eff"])
        state["export_obj"] = _load_json(artifact_paths["export"])
        state["observations_obj"] = _load_json(artifact_paths["observations"])
        state["people_raw"] = _load_json(artifact_paths["personal_props"])

        nodes = sorted(state["registry"]["nodes"], key=lambda x: x["node_index"])
        student_ids = [n["student_id"] for n in nodes]
        state["student_ids"] = student_ids
        state["n"] = len(student_ids)

        people: dict[str, dict[str, Any]] = {}
        if not isinstance(state["people_raw"], list):
            raise ValueError("Expected list at top-level of n50_student_personal_properties.json")
        for rec in state["people_raw"]:
            student = rec.get("student") if isinstance(rec, dict) else None
            if not isinstance(student, dict):
                continue
            sid = student.get("id")
            if isinstance(sid, str) and sid:
                people[sid] = student
        state["people"] = people

        for sid in student_ids:
            if sid not in people:
                raise ValueError(f"student_id from registry missing in personal properties: {sid}")

        emit(f"n_nodes: {state['n']}")

        dn = []
        for sid in student_ids:
            dn.append(str(people[sid].get("displayName", "")))
        state["display_names"] = dn

    def step_p1_network_representation() -> None:
        registry = state["registry"]
        nodes = registry.get("nodes")
        if not isinstance(nodes, list):
            raise ValueError("student_registry_v1.json must contain list field 'nodes'")

        node_indices: list[int] = []
        student_ids: list[str] = []
        for rec in nodes:
            if not isinstance(rec, dict):
                continue
            node_indices.append(int(rec.get("node_index")))
            student_ids.append(str(rec.get("student_id")))

        if len(set(node_indices)) != len(node_indices):
            raise ValueError("registry node_index values must be unique")
        if sorted(node_indices) != list(range(len(node_indices))):
            raise ValueError("registry node_index values must be contiguous 0..n-1")
        if len(set(student_ids)) != len(student_ids):
            raise ValueError("registry student_id values must be unique")

        emit(f"n_nodes: {len(nodes)}")

    def step_p2_node_attributes() -> None:
        student_ids = state["student_ids"]
        people = state["people"]

        oq = []
        op = []
        ac = []
        for sid in student_ids:
            st = people[sid]
            oq.append(str(st.get("outputQuality", "")))
            op.append(str(st.get("outputProductivity", "")))
            ac.append(str(st.get("adopterCategory", "")))

        emit("attributes_present: outputQuality, outputProductivity, adopterCategory")
        emit(
            "summary: "
            + f"unique_outputQuality={len(set(oq))} "
            + f"unique_outputProductivity={len(set(op))} "
            + f"unique_adopterCategory={len(set(ac))}"
        )

        if args.full:
            emit(
                "\t".join(
                    [
                        "node_index",
                        "displayName",
                        "student_id",
                        "outputQuality",
                        "outputProductivity",
                        "adopterCategory",
                    ]
                )
            )
            for i, sid in enumerate(student_ids):
                st = people[sid]
                emit(
                    "\t".join(
                        [
                            str(i),
                            str(st.get("displayName", "")),
                            sid,
                            str(st.get("outputQuality", "")),
                            str(st.get("outputProductivity", "")),
                            str(st.get("adopterCategory", "")),
                        ]
                    )
                )

    def step_p4_feasible_relational_investment() -> None:
        step_na("P4")

    def step_p5_network_potential_functional() -> None:
        step_na("P5")

    def step_p6_equilibrium_network() -> None:
        step_na("P6")

    def step_p7_equilibrium_characterisation() -> None:
        step_na("P7")

    def step_p9_green_operator() -> None:
        step_na("P9")

    def step_p14_comparative_statics_layer() -> None:
        step_na("P14")

    def step_ordering_layer_e1_e2_e3() -> None:
        step_na("ORDERING")

    def step_p15_dynamic_network_evolution() -> None:
        step_na("P15")

    def step_p16_endogenous_topology() -> None:
        step_na("P16")

    def step_p17_universality_layer() -> None:
        step_na("P17")

    def step_p3_source_s() -> None:
        student_ids = state["student_ids"]
        s_obj = state["s_obj"]
        people = state["people"]
        n = int(state["n"])

        emit("Frozen policy:")
        emit("- Q,P tier mapping: very_low->1 low->2 medium->3 high->4 very_high->5")
        emit("- s_i = (Q_i * P_i) / 9.0")
        emit("")

        s_map = {e["student_id"]: float(e["s"]) for e in s_obj["s"]}
        s_from_artifact = np.array([s_map[sid] for sid in student_ids], dtype=float)

        s_recon = np.zeros(n, dtype=float)
        for i, sid in enumerate(student_ids):
            st = people[sid]
            q = _tier_1_to_5(str(st["outputQuality"]))
            p = _tier_1_to_5(str(st["outputProductivity"]))
            s_recon[i] = (float(q) * float(p)) / 9.0

        err = float(np.max(np.abs(s_from_artifact - s_recon)))
        emit(f"max|s_artifact - s_reconstructed| = {_format_float(err)}")
        if err > 1e-12:
            raise ValueError("s_v2 does not match frozen policy s_i=(Q_i*P_i)/9")

        _check_no_nan_inf(s_from_artifact, name="s")
        state["s"] = s_from_artifact

        emit(
            "summary: "
            + f"s[min/mean/max]={_format_float(float(np.min(s_from_artifact)))}/{_format_float(float(np.mean(s_from_artifact)))}/{_format_float(float(np.max(s_from_artifact)))}"
        )

        if args.full:
            header = ["node_index", "displayName", "student_id", "outputQuality", "outputProductivity", "Q", "P", "s"]
            emit("\t".join(header))
            for i, sid in enumerate(student_ids):
                st = people[sid]
                oq = str(st.get("outputQuality", ""))
                op = str(st.get("outputProductivity", ""))
                Q = _tier_1_to_5(oq)
                P = _tier_1_to_5(op)
                emit(
                    "\t".join(
                        [
                            str(i),
                            str(st.get("displayName", "")),
                            sid,
                            oq,
                            op,
                            str(Q),
                            str(P),
                            _format_float(float(s_from_artifact[i])),
                        ]
                    )
                )

    def step_p12_rho() -> None:
        student_ids = state["student_ids"]
        people = state["people"]
        Eeff_obj = state["Eeff_obj"]
        n = int(state["n"])

        emit("Frozen policy:")
        emit("- adopterCategory -> rho mapping:")
        emit("  - innovator: 1.10")
        emit("  - early_adopter: 1.05")
        emit("  - early_majority: 1.00")
        emit("  - late_majority: 0.95")
        emit("  - laggard: 0.90")
        emit("")

        rho_art = np.asarray(Eeff_obj["rho"], dtype=float).reshape(-1)
        if rho_art.shape != (n,):
            raise ValueError(f"rho length mismatch: expected {n}, got {rho_art.shape}")

        rho_recon = np.zeros(n, dtype=float)
        for i, sid in enumerate(student_ids):
            rho_recon[i] = _rho(str(people[sid]["adopterCategory"]))

        err = float(np.max(np.abs(rho_art - rho_recon)))
        emit(f"max|rho_artifact - rho_reconstructed| = {_format_float(err)}")
        if err > 1e-12:
            raise ValueError("rho does not match frozen adopterCategory policy")

        _check_no_nan_inf(rho_art, name="rho")
        state["rho"] = rho_art

        emit(
            "summary: "
            + f"rho[min/mean/max]={_format_float(float(np.min(rho_art)))}/{_format_float(float(np.mean(rho_art)))}/{_format_float(float(np.max(rho_art)))}"
        )

        if args.full:
            emit("\t".join(["node_index", "displayName", "student_id", "adopterCategory", "rho"]))
            for i, sid in enumerate(student_ids):
                st = people[sid]
                emit(
                    "\t".join(
                        [
                            str(i),
                            str(st.get("displayName", "")),
                            sid,
                            str(st.get("adopterCategory", "")),
                            _format_float(float(rho_art[i])),
                        ]
                    )
                )

    def _load_ties_as_directed() -> dict[tuple[str, str], float]:
        ties_obj = state["ties_obj"]
        ties = ties_obj.get("ties")
        if not isinstance(ties, list):
            raise ValueError("tie_strengths_w_v2.json must contain list field 'ties'")

        w_directed: dict[tuple[str, str], float] = {}
        for rec in ties:
            if not isinstance(rec, dict):
                continue
            a = rec.get("actor_student_id")
            b = rec.get("target_student_id")
            wt = rec.get("w")
            if isinstance(a, str) and isinstance(b, str) and isinstance(wt, (int, float)):
                w_directed[(a, b)] = float(wt)
        return w_directed

    def step_p8a_symmetrization_scaling() -> None:
        student_ids = state["student_ids"]
        C_obj = state["C_obj"]

        policy = C_obj.get("policy")
        if not isinstance(policy, dict):
            raise ValueError("coupling_operator_C_v2.json must include policy dict")
        alpha = float(policy.get("alpha", 1.0))
        jitter = float(policy.get("jitter", 1e-6))

        emit("Frozen policy:")
        emit("- w_sym(i,j) = 0.5*(w_ij + w_ji)")
        emit("- scale = mean_nonzero(W_sym)")
        emit("- W_sym_scaled = W_sym / scale")
        emit("")

        w_directed = _load_ties_as_directed()
        inter = _coupling_intermediates_from_ties(
            student_ids=student_ids,
            w_directed=w_directed,
            alpha=alpha,
            jitter=jitter,
        )
        state["C_inter"] = inter

        scale_recon = float(inter["scale"])
        scale_art = float(policy.get("scaling", {}).get("mean_nonzero_w_sym", scale_recon))
        emit(f"alpha: {alpha}")
        emit(f"jitter: {jitter}")
        emit(f"mean_nonzero_w_sym (artifact): {_format_float(scale_art)}")
        emit(f"mean_nonzero_w_sym (recomputed): {_format_float(scale_recon)}")

        W_sym = np.asarray(inter["W_sym"], dtype=float)
        nonzero = W_sym[W_sym > 0]
        emit(f"n_nonzero_w_sym: {int(nonzero.size)}")
        if nonzero.size > 0:
            emit(
                "w_sym_nonzero summary: "
                + f"min={_format_float(float(np.min(nonzero)))} "
                + f"mean={_format_float(float(np.mean(nonzero)))} "
                + f"max={_format_float(float(np.max(nonzero)))}"
            )

    def step_p8b_laplacian_diagnostics() -> None:
        inter = state.get("C_inter")
        if not isinstance(inter, dict):
            raise ValueError("Expected coupling intermediates in state (run P8a first)")

        emit("Frozen policy:")
        emit("- d_i = sum_j W_sym_scaled(i,j)")
        emit("- L = D - W_sym_scaled")
        emit("")

        L = np.asarray(inter["L"], dtype=float)
        diag = np.diag(L)
        off = L - np.diag(diag)
        emit(
            "L diagnostics: "
            + f"diag[min/mean/max]={_format_float(float(np.min(diag)))}/{_format_float(float(np.mean(diag)))}/{_format_float(float(np.max(diag)))}; "
            + f"offdiag[min/mean/max]={_format_float(float(np.min(off)))}/{_format_float(float(np.mean(off)))}/{_format_float(float(np.max(off)))}"
        )
        row_sums = np.sum(L, axis=1)
        emit(f"max|row_sum(L)| = {_format_float(float(np.max(np.abs(row_sums))))}")

    def step_p8c_final_coupling_operator() -> None:
        student_ids = state["student_ids"]
        C_obj = state["C_obj"]
        n = int(state["n"])

        fmt = C_obj.get("format")
        if not isinstance(fmt, dict) or fmt.get("type") != "symmetric_dense":
            raise ValueError("coupling_operator_C_v2.json must be format.type=symmetric_dense")
        C_art = np.asarray(fmt.get("matrix"), dtype=float)
        if C_art.shape != (n, n):
            raise ValueError(f"C_v2 shape mismatch: expected {(n, n)}, got {C_art.shape}")

        policy = C_obj.get("policy")
        if not isinstance(policy, dict):
            raise ValueError("coupling_operator_C_v2.json must include policy dict")
        alpha = float(policy.get("alpha", 1.0))
        jitter = float(policy.get("jitter", 1e-6))

        emit("Frozen policy:")
        emit("- C = I + alpha*L + jitter*I")
        emit("")

        inter = state.get("C_inter")
        if not isinstance(inter, dict):
            w_directed = _load_ties_as_directed()
            inter = _coupling_intermediates_from_ties(
                student_ids=student_ids,
                w_directed=w_directed,
                alpha=alpha,
                jitter=jitter,
            )
            state["C_inter"] = inter
        C_recon = np.asarray(inter["C"], dtype=float)

        diag = np.diag(C_art)
        off = C_art - np.diag(diag)
        emit(
            "C_v2 diagnostics: "
            + f"diag[min/mean/max]={_format_float(float(np.min(diag)))}/{_format_float(float(np.mean(diag)))}/{_format_float(float(np.max(diag)))}; "
            + f"offdiag[min/mean/max]={_format_float(float(np.min(off)))}/{_format_float(float(np.mean(off)))}/{_format_float(float(np.max(off)))}"
        )

        err = float(np.max(np.abs(C_art - C_recon)))
        emit(f"max|C_artifact - C_reconstructed| = {_format_float(err)}")
        if err > 1e-8:
            raise ValueError("C_v2 does not match reconstruction from ties under frozen policy")

        _check_no_nan_inf(C_art.reshape(-1), name="C")
        state["C"] = C_art

    def step_p8_coupling_C_v2() -> None:
        emit("note: P8 coupling operator is reported as granular sub-steps P8a/P8b/P8c")

    def step_p10_propagation() -> None:
        C = state["C"]
        s = state["s"]
        v_obj = state["v_obj"]
        n = int(state["n"])

        v = np.asarray(v_obj["v"], dtype=float).reshape(-1)
        if v.shape != (n,):
            raise ValueError(f"v length mismatch: expected {n}, got {v.shape}")

        residual = C @ v - s
        residual_norm = float(np.linalg.norm(residual, ord=2))
        residual_max = float(np.max(np.abs(residual)))
        emit("Definition:")
        emit("- v solves: C v = s")
        emit("")
        emit(f"solve_residual_l2_norm: {_format_float(residual_norm)}")
        emit(f"solve_residual_linf_norm: {_format_float(residual_max)}")
        if residual_norm > 1e-6:
            raise ValueError("Propagation solve residual too large (C v != s)")

        _check_no_nan_inf(v, name="v")
        state["v"] = v

        emit(
            "summary: "
            + f"v[min/mean/max]={_format_float(float(np.min(v)))}/{_format_float(float(np.mean(v)))}/{_format_float(float(np.max(v)))}"
        )

        if args.full:
            student_ids = state["student_ids"]
            people = state["people"]
            emit("\t".join(["node_index", "displayName", "student_id", "v"]))
            for i, sid in enumerate(student_ids):
                emit(
                    "\t".join(
                        [
                            str(i),
                            str(people[sid].get("displayName", "")),
                            sid,
                            _format_float(float(v[i])),
                        ]
                    )
                )

    def step_p11_node_energy_definition() -> None:
        s = state["s"]
        v = state["v"]
        E_obj = state["E_obj"]

        beta0 = float(E_obj.get("parameters", {}).get("beta0", 1.0))
        beta1 = float(E_obj.get("parameters", {}).get("beta1", 1.0))

        E = np.asarray(E_obj["E"], dtype=float).reshape(-1)
        E_recon = beta0 * s + beta1 * v
        e_err = float(np.max(np.abs(E - E_recon)))

        emit("Definition:")
        emit("- E = beta0*s + beta1*v")
        emit("")
        emit(f"beta0: {_format_float(beta0)}")
        emit(f"beta1: {_format_float(beta1)}")
        emit(f"max|E - (beta0*s+beta1*v)| = {_format_float(e_err)}")
        if e_err > 1e-9:
            raise ValueError("E does not match definition")

        _check_no_nan_inf(E, name="E")
        state["E"] = E

        emit(
            "summary: "
            + f"E[min/mean/max]={_format_float(float(np.min(E)))}/{_format_float(float(np.mean(E)))}/{_format_float(float(np.max(E)))}"
        )

        if args.full:
            student_ids = state["student_ids"]
            people = state["people"]
            emit("\t".join(["node_index", "displayName", "student_id", "s", "v", "E"]))
            for i, sid in enumerate(student_ids):
                emit(
                    "\t".join(
                        [
                            str(i),
                            str(people[sid].get("displayName", "")),
                            sid,
                            _format_float(float(s[i])),
                            _format_float(float(v[i])),
                            _format_float(float(E[i])),
                        ]
                    )
                )

    def step_p13_effective_node_energy() -> None:
        s = state["s"]
        v = state["v"]
        rho = state["rho"]

        E_obj = state["E_obj"]
        Eeff_obj = state["Eeff_obj"]

        beta0 = float(E_obj.get("parameters", {}).get("beta0", 1.0))
        beta1 = float(E_obj.get("parameters", {}).get("beta1", 1.0))

        E_eff = np.asarray(Eeff_obj["E_eff"], dtype=float).reshape(-1)
        Eeff_recon = beta0 * s + beta1 * (rho * v)
        ee_err = float(np.max(np.abs(E_eff - Eeff_recon)))

        emit("Definition:")
        emit("- E_eff = beta0*s + beta1*(rho ⊙ v)")
        emit("")
        emit(f"beta0: {_format_float(beta0)}")
        emit(f"beta1: {_format_float(beta1)}")
        emit(f"max|E_eff - (beta0*s+beta1*(rho*v))| = {_format_float(ee_err)}")

        if ee_err > 1e-9:
            raise ValueError("E_eff does not match definition")

        _check_no_nan_inf(E_eff, name="E_eff")
        state["E_eff"] = E_eff

        emit(
            "summary: "
            + f"E_eff[min/mean/max]={_format_float(float(np.min(E_eff)))}/{_format_float(float(np.mean(E_eff)))}/{_format_float(float(np.max(E_eff)))}"
        )

        if args.full:
            student_ids = state["student_ids"]
            people = state["people"]
            emit("\t".join(["node_index", "displayName", "student_id", "s", "rho", "v", "E_eff"]))
            for i, sid in enumerate(student_ids):
                emit(
                    "\t".join(
                        [
                            str(i),
                            str(people[sid].get("displayName", "")),
                            sid,
                            _format_float(float(s[i])),
                            _format_float(float(rho[i])),
                            _format_float(float(v[i])),
                            _format_float(float(E_eff[i])),
                        ]
                    )
                )

    def step_export_ranking_policy() -> None:
        export_obj = state["export_obj"]
        E_eff = state["E_eff"]
        student_ids = state["student_ids"]
        people = state["people"]

        top_k = int(export_obj.get("top_k", 10))
        top_policy = _ranking_indices_by_policy(E_eff, top_k=top_k)

        export_entries = export_obj["rankings"]["entries"]
        export_top = [int(e["node_index"]) for e in export_entries]

        emit("Ranking policy:")
        emit(f"top_k: {top_k}")
        emit(f"ranking_policy: {export_obj.get('ranking_policy')}")
        if export_top != top_policy:
            raise ValueError("export rankings do not match declared deterministic sort policy")

        emit("Top-k by E_eff (policy order):")
        for rank, i in enumerate(top_policy, start=1):
            emit(
                f"{rank:2d}. node_index={i:2d} score={_format_float(float(E_eff[i]))} "
                + f"displayName={people[student_ids[i]].get('displayName','')} student_id={student_ids[i]}"
            )
        emit("")
        emit("Top-k PASS (export matches policy)")

    def step_obs_observations_summary() -> None:
        observations_obj = state["observations_obj"]

        events = observations_obj.get("events")
        if not isinstance(events, list):
            raise ValueError("observations_v2.json must contain a list field 'events'")

        emit(f"n_observation_events: {len(events)}")

    def step_ties_tie_distribution() -> None:
        ties_obj = state["ties_obj"]

        ties = ties_obj.get("ties")
        if not isinstance(ties, list):
            raise ValueError("tie_strengths_w_v2.json must contain a list field 'ties'")
        emit(f"n_directed_ties: {len(ties)}")

        # Tie distribution summary
        wts = []
        for rec in ties:
            if isinstance(rec, dict) and isinstance(rec.get("w"), (int, float)):
                wts.append(float(rec["w"]))
        if wts:
            w_arr = np.asarray(wts, dtype=float)
            emit(
                "tie_strength w summary: "
                + f"min={_format_float(float(np.min(w_arr)))} "
                + f"mean={_format_float(float(np.mean(w_arr)))} "
                + f"max={_format_float(float(np.max(w_arr)))}"
            )

        if args.full:
            emit("")
            emit("Sample ties (first 25):")
            emit("\t".join(["actor_student_id", "target_student_id", "w"]))
            for rec in ties[:25]:
                if not isinstance(rec, dict):
                    continue
                emit(
                    "\t".join(
                        [
                            str(rec.get("actor_student_id", "")),
                            str(rec.get("target_student_id", "")),
                            _format_float(float(rec.get("w", 0.0))),
                        ]
                    )
                )

    run_step(step_id="0", title="Artifact presence", fn=step_presence)
    run_step(step_id="1", title="Load inputs", fn=step_load)

    run_step(step_id="P1", title="P1 / Step 1(1) — Network Representation", fn=step_p1_network_representation)
    run_step(step_id="P2", title="P2 / Step 2(9) — Node Attributes", fn=step_p2_node_attributes)
    run_step(step_id="P3", title="P3 / Step 3(10) — Node Source Value (s_v2)", fn=step_p3_source_s)
    run_step(
        step_id="P4",
        title="P4 / Step 4(2) — Feasible Relational Investment",
        fn=step_p4_feasible_relational_investment,
    )
    run_step(step_id="P5", title="P5 / Step 5(3) — Network Potential Functional", fn=step_p5_network_potential_functional)
    run_step(step_id="P6", title="P6 / Step 6(4) — Equilibrium Network", fn=step_p6_equilibrium_network)
    run_step(step_id="P7", title="P7 / Step 7(5) — Equilibrium Characterisation", fn=step_p7_equilibrium_characterisation)

    run_step(step_id="OBS", title="OBS — Observations summary", fn=step_obs_observations_summary)
    run_step(step_id="TIES", title="TIES — Tie aggregation + distribution", fn=step_ties_tie_distribution)

    run_step(step_id="P8", title="P8 / Step 8(6) — Coupling Operator", fn=step_p8_coupling_C_v2)
    run_step(step_id="P8a", title="P8a — Symmetrization + scaling diagnostics", fn=step_p8a_symmetrization_scaling)
    run_step(step_id="P8b", title="P8b — Laplacian L diagnostics", fn=step_p8b_laplacian_diagnostics)
    run_step(step_id="P8c", title="P8c — Final C_v2 artifact check", fn=step_p8c_final_coupling_operator)

    run_step(step_id="P9", title="P9 / Step 9(7) — Green Operator", fn=step_p9_green_operator)
    run_step(step_id="P10", title="P10 / Step 10(11) — Propagation Mapping", fn=step_p10_propagation)
    run_step(step_id="P11", title="P11 / Step 11(12) — Node Energy Definition", fn=step_p11_node_energy_definition)
    run_step(step_id="P12", title="P12 / Step 12(13) — Diffusion / Receptivity", fn=step_p12_rho)
    run_step(step_id="P13", title="P13 / Step 13(14) — Effective Node Energy", fn=step_p13_effective_node_energy)
    run_step(step_id="P14", title="P14 / Step 14(8) — Comparative Statics Layer", fn=step_p14_comparative_statics_layer)
    run_step(step_id="ORDERING", title="Ordering layer — E1 -> E2 -> E3", fn=step_ordering_layer_e1_e2_e3)
    run_step(step_id="P15", title="P15 / Step 15(15) — Dynamic Network Evolution", fn=step_p15_dynamic_network_evolution)
    run_step(step_id="P16", title="P16 / Step 16(16) — Endogenous Topology", fn=step_p16_endogenous_topology)
    run_step(step_id="P17", title="P17 / Step 17(17) — Universality Layer", fn=step_p17_universality_layer)

    run_step(step_id="EXPORT", title="Export ranking policy", fn=step_export_ranking_policy)

    section("AFFINITY N50 V2 DATA-DRIVEN CHECK: PASS")

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("\n".join(transcript_lines) + "\n")
        emit(f"wrote transcript: {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
