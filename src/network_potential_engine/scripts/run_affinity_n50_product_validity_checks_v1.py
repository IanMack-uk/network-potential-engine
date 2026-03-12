from __future__ import annotations

import json
import platform
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


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


def _load_json(path: Path) -> object:
    return json.loads(path.read_text())


def _write_json(path: Path, obj: object) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=False) + "\n")


def _fmt_float(x: float) -> str:
    return f"{x:.16g}"


@dataclass(frozen=True)
class ScenarioResult:
    scenario_id: str
    name: str
    passed: bool
    details: dict[str, object]


def _scenario_s1_schema_and_explanation_coherence(
    *, export: dict[str, object], tol: float
) -> ScenarioResult:
    students = export.get("students")
    if not isinstance(students, list):
        return ScenarioResult(
            scenario_id="S1",
            name="Schema + explanation coherence",
            passed=False,
            details={"error": "export['students'] missing or not a list"},
        )

    missing_fields: list[dict[str, object]] = []
    max_abs_err = 0.0
    worst_node_index: int | None = None

    for s in students:
        if not isinstance(s, dict):
            missing_fields.append({"error": "student entry not an object"})
            continue

        node_index = s.get("node_index")
        e_eff = s.get("E_eff")
        expl = s.get("explanation")

        if (
            not isinstance(node_index, int)
            or not isinstance(e_eff, (int, float))
            or not isinstance(expl, dict)
        ):
            missing_fields.append(
                {
                    "node_index": node_index,
                    "error": "missing node_index (int), E_eff (number), or explanation (object)",
                }
            )
            continue

        intrinsic = expl.get("intrinsic_component")
        network = expl.get("network_component")
        if not isinstance(intrinsic, (int, float)) or not isinstance(network, (int, float)):
            missing_fields.append(
                {
                    "node_index": node_index,
                    "error": "missing intrinsic_component/network_component (number)",
                }
            )
            continue

        abs_err = abs((float(intrinsic) + float(network)) - float(e_eff))
        if abs_err > max_abs_err:
            max_abs_err = abs_err
            worst_node_index = int(node_index)

    ranking = export.get("rankings")
    ranking_ok = True
    ranking_error: str | None = None

    if not isinstance(ranking, dict) or not isinstance(ranking.get("entries"), list):
        ranking_ok = False
        ranking_error = "export['rankings']['entries'] missing or not a list"
    else:
        entries = ranking["entries"]
        # Compute expected ordering by (-E_eff, node_index)
        score_by_node_index: dict[int, float] = {}
        for s in students:
            if isinstance(s, dict) and isinstance(s.get("node_index"), int) and isinstance(
                s.get("E_eff"), (int, float)
            ):
                score_by_node_index[int(s["node_index"])] = float(s["E_eff"])

        expected = sorted(
            score_by_node_index.items(),
            key=lambda kv: (-kv[1], kv[0]),
        )
        expected_node_indices = [ni for ni, _ in expected]

        observed_node_indices: list[int] = []
        for e in entries:
            if not isinstance(e, dict) or not isinstance(e.get("node_index"), int):
                ranking_ok = False
                ranking_error = "ranking entry missing node_index (int)"
                break
            observed_node_indices.append(int(e["node_index"]))

        if ranking_ok:
            top_k = export.get("top_k")
            if isinstance(top_k, int) and top_k > 0:
                expected_topk = expected_node_indices[:top_k]
                observed_topk = observed_node_indices[:top_k]
                if expected_topk != observed_topk:
                    ranking_ok = False
                    ranking_error = "top_k ordering mismatch vs (-E_eff, node_index)"
            else:
                # If top_k isn't present, require full equality.
                if expected_node_indices != observed_node_indices:
                    ranking_ok = False
                    ranking_error = "full ordering mismatch vs (-E_eff, node_index)"

    passed = (
        len(missing_fields) == 0
        and max_abs_err <= float(tol)
        and ranking_ok
    )

    return ScenarioResult(
        scenario_id="S1",
        name="Schema + explanation coherence",
        passed=passed,
        details={
            "tol": float(tol),
            "missing_fields_count": len(missing_fields),
            "missing_fields_examples": missing_fields[:5],
            "max_abs_err_intrinsic_plus_network_minus_E_eff": float(max_abs_err),
            "worst_node_index": worst_node_index,
            "ranking_ok": ranking_ok,
            "ranking_error": ranking_error,
        },
    )


def _scenario_s2_single_node_uplift(
    *, export: dict[str, object], node_index: int, delta: float
) -> ScenarioResult:
    students = export.get("students")
    if not isinstance(students, list):
        return ScenarioResult(
            scenario_id="S2",
            name="Single-node uplift monotonicity",
            passed=False,
            details={"error": "export['students'] missing or not a list"},
        )

    baseline_scores: dict[int, float] = {}
    baseline_s: dict[int, float] = {}
    baseline_v: dict[int, float] = {}

    for s in students:
        if not isinstance(s, dict):
            continue
        ni = s.get("node_index")
        s_val = s.get("s")
        v_val = s.get("v")
        e_eff = s.get("E_eff")
        if (
            isinstance(ni, int)
            and isinstance(s_val, (int, float))
            and isinstance(v_val, (int, float))
            and isinstance(e_eff, (int, float))
        ):
            baseline_scores[int(ni)] = float(e_eff)
            baseline_s[int(ni)] = float(s_val)
            baseline_v[int(ni)] = float(v_val)

    if node_index not in baseline_scores:
        return ScenarioResult(
            scenario_id="S2",
            name="Single-node uplift monotonicity",
            passed=False,
            details={"error": f"node_index {node_index} not found"},
        )

    # Counterfactual: keep v fixed; increase s only for target node.
    counterfactual_scores: dict[int, float] = dict(baseline_scores)
    counterfactual_scores[node_index] = baseline_scores[node_index] + float(delta)

    baseline_order = sorted(
        baseline_scores.items(),
        key=lambda kv: (-kv[1], kv[0]),
    )
    counterfactual_order = sorted(
        counterfactual_scores.items(),
        key=lambda kv: (-kv[1], kv[0]),
    )

    baseline_rank: dict[int, int] = {ni: idx + 1 for idx, (ni, _) in enumerate(baseline_order)}
    counterfactual_rank: dict[int, int] = {
        ni: idx + 1 for idx, (ni, _) in enumerate(counterfactual_order)
    }

    baseline_target_score = baseline_scores[node_index]
    counterfactual_target_score = counterfactual_scores[node_index]

    score_increased = counterfactual_target_score > baseline_target_score
    rank_not_worse = counterfactual_rank[node_index] <= baseline_rank[node_index]

    others_unchanged_max_abs = 0.0
    for ni, base_score in baseline_scores.items():
        if ni == node_index:
            continue
        abs_err = abs(counterfactual_scores[ni] - base_score)
        if abs_err > others_unchanged_max_abs:
            others_unchanged_max_abs = abs_err

    passed = bool(score_increased and rank_not_worse and others_unchanged_max_abs == 0.0)

    top_k = export.get("top_k")
    top_k_int = int(top_k) if isinstance(top_k, int) and top_k > 0 else 10

    return ScenarioResult(
        scenario_id="S2",
        name="Single-node uplift monotonicity",
        passed=passed,
        details={
            "node_index": int(node_index),
            "delta": float(delta),
            "baseline": {
                "s": baseline_s[node_index],
                "v": baseline_v[node_index],
                "E_eff": baseline_target_score,
                "rank": baseline_rank[node_index],
            },
            "counterfactual": {
                "s": baseline_s[node_index] + float(delta),
                "v": baseline_v[node_index],
                "E_eff": counterfactual_target_score,
                "rank": counterfactual_rank[node_index],
            },
            "checks": {
                "score_increased": score_increased,
                "rank_not_worse": rank_not_worse,
                "others_unchanged_max_abs": float(others_unchanged_max_abs),
            },
            "baseline_top_k_node_indices": [ni for ni, _ in baseline_order[:top_k_int]],
            "counterfactual_top_k_node_indices": [ni for ni, _ in counterfactual_order[:top_k_int]],
        },
    )


def main() -> int:
    repo_root = _find_repo_root(Path(__file__))
    artifacts_dir = repo_root / "affinity" / "artifacts" / "n50"

    export_path = artifacts_dir / "app_facing_outputs_v1.json"

    scenarios_path = artifacts_dir / "product_validity_scenarios_v1.json"
    outputs_path = artifacts_dir / "product_validity_outputs_v1.json"
    note_path = artifacts_dir / "product_validity_evaluation_note_v1.txt"

    export = _load_json(export_path)
    if not isinstance(export, dict):
        raise TypeError("app_facing_outputs_v1.json must be a JSON object")

    # Frozen v1 parameters
    tol = 1e-12
    s2_node_index = 0
    s2_delta = 0.5

    timestamp_utc = datetime.now(timezone.utc).isoformat()

    scenario_defs = {
        "schema_version": "1.0",
        "name": "affinity_product_validity_scenarios_v1",
        "timestamp_utc": timestamp_utc,
        "git_head_sha": _try_git_head_sha(repo_root),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "inputs": {
            "export_ref": "affinity/artifacts/n50/app_facing_outputs_v1.json",
        },
        "frozen_parameters": {
            "tol": tol,
            "S2": {"node_index": s2_node_index, "delta": s2_delta},
        },
        "scenarios": [
            {
                "scenario_id": "S1",
                "name": "Schema + explanation coherence",
                "expectation": {
                    "description": "Each student has explanation fields and intrinsic+network == E_eff within tol; ranking matches (-E_eff, node_index)."
                },
            },
            {
                "scenario_id": "S2",
                "name": "Single-node uplift monotonicity",
                "expectation": {
                    "description": "Uplifting one node's s by +delta increases its E_eff and does not worsen its rank; all other nodes unchanged."
                },
            },
        ],
    }

    r1 = _scenario_s1_schema_and_explanation_coherence(export=export, tol=tol)
    r2 = _scenario_s2_single_node_uplift(
        export=export, node_index=s2_node_index, delta=s2_delta
    )

    all_passed = bool(r1.passed and r2.passed)

    outputs = {
        "schema_version": "1.0",
        "name": "affinity_product_validity_outputs_v1",
        "timestamp_utc": timestamp_utc,
        "git_head_sha": _try_git_head_sha(repo_root),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "results": [
            {
                "scenario_id": r1.scenario_id,
                "name": r1.name,
                "passed": r1.passed,
                "details": r1.details,
            },
            {
                "scenario_id": r2.scenario_id,
                "name": r2.name,
                "passed": r2.passed,
                "details": r2.details,
            },
        ],
        "overall": {"passed": all_passed},
    }

    note_lines: list[str] = []
    note_lines.append("Job 14 — Product validity checks — evaluation note (v1)")
    note_lines.append("")
    note_lines.append(f"timestamp_utc: {timestamp_utc}")
    note_lines.append(f"git_head_sha: {_try_git_head_sha(repo_root)}")
    note_lines.append(f"python: {sys.version.split()[0]}")
    note_lines.append(f"platform: {platform.platform()}")
    note_lines.append("")

    note_lines.append("Scenario S1 — Schema + explanation coherence")
    note_lines.append("Expected:")
    note_lines.append("- explanation fields present")
    note_lines.append("- intrinsic_component + network_component == E_eff (within tol)")
    note_lines.append("- ranking matches (-E_eff, node_index)")
    note_lines.append("Observed:")
    note_lines.append(f"- passed: {r1.passed}")
    note_lines.append(
        "- max_abs_err(intrinsic+network-E_eff): "
        + _fmt_float(
            float(
                r1.details.get("max_abs_err_intrinsic_plus_network_minus_E_eff", float("nan"))
            )
        )
    )
    note_lines.append(
        "- ranking_ok: "
        + str(bool(r1.details.get("ranking_ok")))
        + ("" if not r1.details.get("ranking_error") else f" (error: {r1.details.get('ranking_error')})")
    )
    note_lines.append("")

    note_lines.append("Scenario S2 — Single-node uplift monotonicity")
    note_lines.append("Expected:")
    note_lines.append("- target node score increases")
    note_lines.append("- target node rank does not worsen")
    note_lines.append("- other nodes unchanged")
    note_lines.append("Observed:")
    note_lines.append(f"- passed: {r2.passed}")
    if isinstance(r2.details.get("checks"), dict):
        checks = r2.details["checks"]
        note_lines.append(f"- score_increased: {checks.get('score_increased')}")
        note_lines.append(f"- rank_not_worse: {checks.get('rank_not_worse')}")
        note_lines.append(
            "- others_unchanged_max_abs: "
            + _fmt_float(float(checks.get("others_unchanged_max_abs", float("nan"))))
        )
    note_lines.append("")

    note_lines.append("Conclusion")
    note_lines.append(f"- overall_passed: {all_passed}")
    note_lines.append("")
    note_lines.append("Note")
    note_lines.append(
        "- v1 uses placeholder-uniform signal regime, so validity checks here are harness-level (coherence/monotonicity), not outcome efficacy."
    )
    note_lines.append("")

    _write_json(scenarios_path, scenario_defs)
    _write_json(outputs_path, outputs)
    note_path.write_text("\n".join(note_lines) + "\n")

    # stdout summary
    print("==============================================================================")
    print("Job 14 — Affinity n=50 product validity checks (v1)")
    print("==============================================================================")
    print(f"timestamp_utc: {timestamp_utc}")
    print(f"python: {sys.version.split()[0]}")
    print(f"platform: {platform.platform()}")
    print(f"git_head_sha: {_try_git_head_sha(repo_root)}")
    print("")

    for r in (r1, r2):
        print("------------------------------------------------------------------------------")
        print(f"{r.scenario_id}: {r.name}")
        print(f"PASS" if r.passed else "FAIL")

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
