from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
from datetime import datetime, timedelta, timezone
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from typing import Iterable

import numpy as np
from neo4j import GraphDatabase


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


def _snapshot_run(
    *,
    artifacts_dir: Path,
    snapshot_root: Path,
    run_id: str,
    extra_files: list[Path],
    created_files: list[Path],
) -> Path:
    snapshot_dir = snapshot_root / run_id
    snapshot_dir.mkdir(parents=True, exist_ok=True)

    for p in extra_files + created_files:
        if not p.exists():
            continue
        dst = snapshot_dir / p.name
        try:
            if p.resolve() == dst.resolve():
                continue
        except FileNotFoundError:
            pass
        shutil.copy2(p, dst)

    (snapshot_dir / "snapshot_manifest.json").write_text(
        json.dumps(
            {
                "run_id": run_id,
                "created_files": [p.name for p in created_files],
                "extra_files": [p.name for p in extra_files if p.exists()],
                "timestamp_utc": run_id,
            },
            indent=2,
            sort_keys=False,
        )
        + "\n"
    )

    return snapshot_dir


def _load_dotenv(dotenv_path: Path) -> dict[str, str]:
    if not dotenv_path.exists():
        return {}

    out: dict[str, str] = {}
    for raw_line in dotenv_path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].lstrip()
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        v = v.strip().strip("\"'")
        if k:
            out[k] = v
    return out


@dataclass(frozen=True)
class _Neo4jConfig:
    uri: str
    username: str
    password: str
    database: str | None


def _load_neo4j_config(*, repo_root: Path) -> _Neo4jConfig:
    env_from_file = _load_dotenv(repo_root / ".env")

    def get(name: str) -> str:
        v = os.environ.get(name)
        if v is None:
            v = env_from_file.get(name)
        if v is None or not v.strip():
            raise RuntimeError(f"Missing required environment variable: {name}")
        return v.strip()

    uri = get("NEO4J_URI")
    username = get("NEO4J_USERNAME")
    password = get("NEO4J_PASSWORD")

    database = os.environ.get("NEO4J_DATABASE") or env_from_file.get("NEO4J_DATABASE")
    if database is not None:
        database = database.strip()
        if not database:
            database = None

    return _Neo4jConfig(uri=uri, username=username, password=password, database=database)


def _neo4j_query_rows(*, cfg: _Neo4jConfig, cypher: str, parameters: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    driver = GraphDatabase.driver(cfg.uri, auth=(cfg.username, cfg.password))
    try:
        with driver.session(database=cfg.database) as session:
            result = session.run(cypher, parameters or {})
            return [dict(r) for r in result]
    finally:
        driver.close()


def _neo4j_value_to_jsonable(x: Any) -> Any:
    # Neo4j Python driver returns temporal types that are not JSON-serializable.
    # We convert them into stable dict representations that match our existing JSON style.
    if x is None:
        return None
    if isinstance(x, (str, int, float, bool)):
        return x
    if isinstance(x, bytes):
        return x.decode("utf-8", errors="replace")
    if isinstance(x, dict):
        return {str(k): _neo4j_value_to_jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_neo4j_value_to_jsonable(v) for v in x]

    # Duck-typed temporal types
    if hasattr(x, "year") and hasattr(x, "month") and hasattr(x, "day") and not hasattr(x, "hour"):
        return {"year": int(x.year), "month": int(x.month), "day": int(x.day)}
    if hasattr(x, "year") and hasattr(x, "month") and hasattr(x, "day") and hasattr(x, "hour"):
        out = {
            "year": int(x.year),
            "month": int(x.month),
            "day": int(x.day),
            "hour": int(getattr(x, "hour", 0)),
            "minute": int(getattr(x, "minute", 0)),
            "second": int(getattr(x, "second", 0)),
            "nanosecond": int(getattr(x, "nanosecond", 0)),
        }
        # Some temporal types expose offset / timezone separately.
        if hasattr(x, "time_zone_offset"):
            try:
                out["timeZoneOffsetSeconds"] = int(getattr(x.time_zone_offset, "seconds", 0))
            except Exception:
                out["timeZoneOffsetSeconds"] = None
        else:
            out["timeZoneOffsetSeconds"] = None
        out["timeZoneId"] = str(getattr(x, "time_zone", None)) if getattr(x, "time_zone", None) else None
        return out

    # Fallback: make it stable-ish
    return str(x)


def _export_live_student_personal_properties(
    *,
    repo_root: Path,
    versioned_out_dir: Path,
    canonical_out_dir: Path,
    run_id: str,
) -> Path:
    cfg = _load_neo4j_config(repo_root=repo_root)
    cypher = """
MATCH (p:Person)-[:HAS_TAG]->(:Tag {slug:"lcm-student"})
RETURN
  p.id AS id,
  p.displayName AS displayName,
  p.givenName AS givenName,
  p.familyName AS familyName,
  p.preferredName AS preferredName,
  p.sex AS sex,
  p.sexuality AS sexuality,
  p.ethnicity AS ethnicity,
  p.nationality AS nationality,
  p.dateOfBirth AS dateOfBirth,
  p.email AS email,
  p.imageURL AS imageURL,
  p.notes AS notes,
  p.adopterCategory AS adopterCategory,
  p.outputQuality AS outputQuality,
  p.outputProductivity AS outputProductivity,
  p.reliabilityBand AS reliabilityBand,
  p.initiativeBand AS initiativeBand,
  p.relationshipCapacityBand AS relationshipCapacityBand,
  p.openToCollaborate AS openToCollaborate,
  p.openToWork AS openToWork,
  p.offersOpportunities AS offersOpportunities,
  p.providesIntroductions AS providesIntroductions,
  p.providesMentorship AS providesMentorship,
  p.providerScore AS providerScore,
  // wellbeing fields (if present)
  p.lifeStabilityLsb AS lifeStabilityLsb,
  p.lifeSatisfactionLsf AS lifeSatisfactionLsf,
  p.holisticWellbeingHwi AS holisticWellbeingHwi,
  p.hwiBand AS hwiBand,
  p.polarQuintile AS polarQuintile,
  p.residentialStatus AS residentialStatus,
  p.commuteBand AS commuteBand,
  p.employmentStatus AS employmentStatus,
  p.paidWorkHoursBand AS paidWorkHoursBand
ORDER BY p.displayName, p.id;
"""
    rows = _neo4j_query_rows(cfg=cfg, cypher=cypher)
    recs: list[dict[str, Any]] = []
    for r in rows:
        sid = r.get("id")
        dn = r.get("displayName")
        if not isinstance(sid, str) or not sid:
            continue
        if not isinstance(dn, str) or not dn:
            dn = sid
        student = {k: _neo4j_value_to_jsonable(v) for k, v in r.items() if k}
        recs.append({"student": student})

    versioned = versioned_out_dir / f"n50_student_personal_properties__{run_id}.json"
    canonical = canonical_out_dir / "n50_student_personal_properties.json"
    _write_json(versioned, recs)
    _write_json(canonical, recs)
    return versioned


def _export_live_student_module_interest_scores(
    *,
    repo_root: Path,
    versioned_out_dir: Path,
    canonical_out_dir: Path,
    run_id: str,
) -> Path:
    cfg = _load_neo4j_config(repo_root=repo_root)
    cypher = """
MATCH (p:Person)-[:HAS_TAG]->(:Tag {slug:"lcm-student"})
MATCH (p)-[i:INTERESTED_IN]->(event:Event)
MATCH (event)-[:IS_PART_OF]->(course:Event)
WHERE course.title CONTAINS "ORIGINAL - BA"
WITH p, event, coalesce(i.weight, 0.0) AS w
ORDER BY p.id, w DESC, event.title
WITH p, collect({score: w, id: event.id, title: event.title}) AS modules
RETURN
  p.id AS id,
  p.displayName AS displayName,
  modules AS modules
ORDER BY displayName, id;
"""
    rows = _neo4j_query_rows(cfg=cfg, cypher=cypher)
    recs: list[dict[str, Any]] = []
    for r in rows:
        sid = r.get("id")
        dn = r.get("displayName")
        mods = r.get("modules")
        if not isinstance(sid, str) or not sid:
            continue
        if not isinstance(dn, str) or not dn:
            dn = sid
        if not isinstance(mods, list):
            mods = []
        modules_json = []
        for m in mods:
            if not isinstance(m, dict):
                continue
            modules_json.append({k: _neo4j_value_to_jsonable(v) for k, v in m.items() if k})
        recs.append({"displayName": dn, "id": sid, "modules": modules_json})

    versioned = versioned_out_dir / f"student_module_interest_score__{run_id}.json"
    canonical = canonical_out_dir / "student_module_interest_score.json"
    _write_json(versioned, recs)
    _write_json(canonical, recs)
    return versioned


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
        "innovator": 1.10,
        "early_adopter": 1.05,
        "early_majority": 1.00,
        "late_majority": 0.95,
        "laggard": 0.90,
    }
    if cat not in m:
        raise ValueError(f"Unexpected adopterCategory enum: {cat!r}")
    return float(m[cat])


def _attendance_propensity(*, student_id: str, scenario_seed: str | None) -> float:
    u = 2.0 * _stable_u01(_with_seed_prefix(scenario_seed=scenario_seed, key=f"a::{student_id}")) - 1.0
    a = 0.55 + 0.15 * u
    return float(min(0.95, max(0.20, a)))


def _load_neo4j_directed_ties_live(*, repo_root: Path) -> tuple[dict[tuple[str, str], float], list[dict[str, Any]]]:
    cfg = _load_neo4j_config(repo_root=repo_root)
    cypher_path = (
        repo_root
        / "affinity"
        / "from_neo4j"
        / "cyphers"
        / "tie_strength_runbook"
        / "90_export_directed_wij_code_ready.cypher"
    )
    cypher = cypher_path.read_text()
    rows = _neo4j_query_rows(cfg=cfg, cypher=cypher)

    out: dict[tuple[str, str], float] = {}
    for rec in rows:
        a = rec.get("actor_student_id")
        b = rec.get("target_student_id")
        wt = rec.get("w")
        if not (isinstance(a, str) and isinstance(b, str)):
            continue
        try:
            wtf = float(wt)
        except (TypeError, ValueError):
            continue
        if wtf <= 0.0:
            continue
        out[(a, b)] = float(out.get((a, b), 0.0) + wtf)

    return out, rows


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


def _load_student_module_interest_scores(
    interest_scores_path: Path,
) -> tuple[dict[tuple[str, str], float], list[str]]:
    raw = _load_json(interest_scores_path)
    if not isinstance(raw, list):
        raise ValueError("Expected list at top-level of student_module_interest_score.json")

    out: dict[tuple[str, str], float] = {}
    titles: set[str] = set()

    for rec in raw:
        if not isinstance(rec, dict):
            continue
        sid = rec.get("id")
        if not isinstance(sid, str) or not sid:
            continue
        modules = rec.get("modules")
        if not isinstance(modules, list):
            continue
        for m in modules:
            if not isinstance(m, dict):
                continue
            title = m.get("title")
            score = m.get("score")
            if not isinstance(title, str) or not title:
                continue
            try:
                sf = float(score)
            except (TypeError, ValueError):
                continue
            if sf < 0.0:
                sf = 0.0
            if sf > 1.0:
                sf = 1.0
            titles.add(title)
            out[(sid, title)] = float(sf)

    return out, sorted(titles)


def _load_neo4j_directed_ties(*, ties_path: Path) -> dict[tuple[str, str], float]:
    raw = _load_json(ties_path)
    if not isinstance(raw, list):
        raise ValueError("Expected list at top-level of Neo4j tie strength export JSON")
    out: dict[tuple[str, str], float] = {}
    for rec in raw:
        if not isinstance(rec, dict):
            continue
        a = rec.get("actor_student_id")
        b = rec.get("target_student_id")
        wt = rec.get("w")
        if not (isinstance(a, str) and isinstance(b, str)):
            continue
        if wt is None:
            continue
        try:
            wtf = float(wt)
        except (TypeError, ValueError):
            continue
        if wtf <= 0.0:
            continue
        out[(a, b)] = float(out.get((a, b), 0.0) + wtf)
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
        "--neo4j-ties-json",
        default=None,
        help=(
            "Path to Neo4j-exported directed tie weights JSON (list of {actor_student_id,target_student_id,w}). "
            "If provided, attendance/co-attendance simulation is skipped and these ties are treated as authoritative."
        ),
    )
    parser.add_argument(
        "--neo4j-readable-json",
        default=None,
        help=(
            "Optional path to Neo4j-exported readable tie table JSON. Not used for computation; "
            "stored as a string reference in generated artifacts for auditability."
        ),
    )
    parser.add_argument(
        "--neo4j-live",
        action="store_true",
        help=(
            "If set, connect to Neo4j (Aura) using .env (NEO4J_URI/USERNAME/PASSWORD[/DATABASE]) and "
            "pull directed ties (w_ij) live via tie_strength_runbook/90_export_directed_wij_code_ready.cypher. "
            "This bypasses --neo4j-ties-json."
        ),
    )
    parser.add_argument(
        "--snapshot",
        action="store_true",
        help=(
            "If set, archive all generated artifacts and any pulled Neo4j inputs into a timestamped snapshot folder "
            "under affinity/artifacts/n50/snapshots/."
        ),
    )
    parser.add_argument(
        "--snapshot-dir",
        default="",
        help=(
            "Optional snapshot directory (relative to repo root). If not set, defaults to affinity/artifacts/n50/snapshots." 
        ),
    )
    parser.add_argument(
        "--audit",
        action="store_true",
        help="Print an end-to-end audit report to stdout and write it to an artifact text file.",
    )
    args = parser.parse_args()

    scenario_seed = str(args.seed) if args.seed is not None else None

    live_neo4j_mode = bool(args.neo4j_live)
    neo4j_mode = live_neo4j_mode or (args.neo4j_ties_json is not None)

    repo_root = _find_repo_root(Path(__file__).resolve())
    artifacts_root = repo_root / "affinity" / "artifacts" / "n50"
    static_dir = artifacts_root / "static"
    latest_dir = artifacts_root / "generated" / "latest"
    neo4j_dir = repo_root / "affinity" / "from_neo4j"

    run_id = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace(":", "-")

    snapshot_root = (
        (repo_root / str(args.snapshot_dir)).resolve()
        if str(args.snapshot_dir).strip()
        else (artifacts_root / "generated" / "snapshots")
    )
    snapshot_dir = snapshot_root / run_id
    versioned_exports_dir = snapshot_dir
    if not args.snapshot:
        versioned_exports_dir = neo4j_dir / "_runs" / run_id
    versioned_exports_dir.mkdir(parents=True, exist_ok=True)

    latest_dir.mkdir(parents=True, exist_ok=True)

    registry_path = static_dir / "registry" / "student_registry_v1.json"
    coupling_C_v1_path = artifacts_root / "legacy" / "v1" / "coupling_operator_C_v1.json"
    personal_props_path = neo4j_dir / "n50_student_personal_properties.json"
    interest_scores_path = neo4j_dir / "student_module_interest_score.json"
    participation_graph_path = neo4j_dir / "n50-student-participation-graph.json"

    created_files: list[Path] = []
    extra_snapshot_files: list[Path] = []

    if live_neo4j_mode:
        versioned_personal = _export_live_student_personal_properties(
            repo_root=repo_root,
            versioned_out_dir=versioned_exports_dir,
            canonical_out_dir=neo4j_dir,
            run_id=run_id,
        )
        personal_props_path = versioned_personal
        extra_snapshot_files.append(versioned_personal)

        versioned_interest = _export_live_student_module_interest_scores(
            repo_root=repo_root,
            versioned_out_dir=versioned_exports_dir,
            canonical_out_dir=neo4j_dir,
            run_id=run_id,
        )
        extra_snapshot_files.append(versioned_interest)

    neo4j_ties_json_path: Path | None = None
    if (not live_neo4j_mode) and (args.neo4j_ties_json is not None):
        neo4j_ties_json_path = (repo_root / str(args.neo4j_ties_json)).resolve()
        if not neo4j_ties_json_path.exists():
            raise FileNotFoundError(str(neo4j_ties_json_path))

    neo4j_readable_json_path: Path | None = None
    if args.neo4j_readable_json is not None:
        neo4j_readable_json_path = (repo_root / str(args.neo4j_readable_json)).resolve()
        if not neo4j_readable_json_path.exists():
            raise FileNotFoundError(str(neo4j_readable_json_path))

    required: list[Path] = [registry_path, coupling_C_v1_path, personal_props_path]
    if (not neo4j_mode) and neo4j_ties_json_path is None:
        required.extend([interest_scores_path, participation_graph_path])
    for p in required:
        if not p.exists():
            raise FileNotFoundError(str(p))

    student_ids = _load_registry_student_ids(registry_path)
    people = _load_personal_props(personal_props_path)

    for sid in student_ids:
        if sid not in people:
            raise ValueError(f"student_id from registry missing in personal properties: {sid}")

    interest_scores: dict[tuple[str, str], float] = {}
    module_titles: list[str] = []
    if not neo4j_mode:
        interest_scores, module_titles = _load_student_module_interest_scores(interest_scores_path)

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

    # Observations/ties
    events: list[dict[str, Any]] = []
    w: dict[tuple[str, str], float] = {}
    attendance_counts: dict[str, int] = {sid: 0 for sid in student_ids}
    n_sessions_per_module = 0

    if not neo4j_mode:
        # Simulate attendance and co-attendance observations
        t0 = datetime(2026, 3, 1, tzinfo=timezone.utc)
        evt_counter = 1
        n_sessions_per_module = 8

        for m_idx, title in enumerate(module_titles):
            for sess in range(n_sessions_per_module):
                ts = t0 + timedelta(days=7 * m_idx, hours=2 * sess)
                attendees: list[str] = []
                for sid in student_ids:
                    st = people[sid]
                    score = float(interest_scores.get((sid, title), 0.0))
                    t = int(round(3.0 * score))
                    if t < 0:
                        t = 0
                    if t > 3:
                        t = 3
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

        observations_path = latest_dir / "observations_v2.json"
        _write_json(
            observations_path,
            {
                "schema_version": "1.0",
                "schema_ref": "affinity/artifacts/n50/static/schemas/observations_schema_v1.json",
                "cohort_registry_ref": "affinity/artifacts/n50/static/registry/student_registry_v1.json",
                "generated": {"method": "optionB_v2_attendance_simulation", "scenario_seed": scenario_seed},
                "events": events,
            },
        )
        created_files.append(observations_path)
    else:
        live_pulled_path: Path | None = None
        if live_neo4j_mode:
            w, neo4j_rows = _load_neo4j_directed_ties_live(repo_root=repo_root)
            # Persist the pulled rows into the run's versioned exports dir and also refresh the canonical latest file.
            live_pulled_path = versioned_exports_dir / f"tie_strength_code_data_live__{run_id}.json"
            _write_json(live_pulled_path, neo4j_rows)
            _write_json(neo4j_dir / "tie_strength_code_data_live.json", neo4j_rows)
            extra_snapshot_files.append(live_pulled_path)
        else:
            # Authoritative ties from Neo4j export
            if neo4j_ties_json_path is None:
                raise RuntimeError("neo4j_mode requires --neo4j-ties-json or --neo4j-live")
            w = _load_neo4j_directed_ties(ties_path=neo4j_ties_json_path)

        # Validate that the tie file references known students.
        student_id_set = set(student_ids)
        unknown = sorted({sid for pair in w.keys() for sid in pair if sid not in student_id_set})
        if unknown:
            raise ValueError(
                "Neo4j tie export contains actor/target student_ids not present in registry: " + ", ".join(unknown[:10])
            )

        observations_path = latest_dir / "observations_v2.json"
        ties_source: str
        if live_neo4j_mode:
            ties_source = (
                "live:affinity/from_neo4j/cyphers/tie_strength_runbook/90_export_directed_wij_code_ready.cypher"
            )
            if live_pulled_path is not None:
                ties_source = ties_source + f" (pulled_rows_file={live_pulled_path})"
        else:
            ties_source = str(neo4j_ties_json_path)

        _write_json(
            observations_path,
            {
                "schema_version": "1.0",
                "schema_ref": "affinity/artifacts/n50/static/schemas/observations_schema_v1.json",
                "cohort_registry_ref": "affinity/artifacts/n50/static/registry/student_registry_v1.json",
                "generated": {
                    "method": "optionB_v2_neo4j_authoritative_ties",
                    "scenario_seed": scenario_seed,
                    "ties_source": ties_source,
                    "readable_source": (str(neo4j_readable_json_path) if neo4j_readable_json_path is not None else None),
                },
                "events": [],
            },
        )
        created_files.append(observations_path)

        if neo4j_readable_json_path is not None:
            archived_readable = latest_dir / neo4j_readable_json_path.name
            shutil.copy2(neo4j_readable_json_path, archived_readable)
            created_files.append(archived_readable)

    source_vector_path = latest_dir / "source_vector_s_v2.json"
    _write_json(
        source_vector_path,
        {
            "schema_version": "1.0",
            "name": "affinity_source_vector_s_v2",
            "cohort_registry_ref": "affinity/artifacts/n50/static/registry/student_registry_v1.json",
            "definition": "s_i = (Q_i * P_i) / 9.0",
            "s": s_entries,
        },
    )
    created_files.append(source_vector_path)

    # Tie weights (derived) as a simple artifact
    ties = []
    for (a, b), wt in sorted(w.items(), key=lambda x: (x[0][0], x[0][1])):
        ties.append({"actor_student_id": a, "target_student_id": b, "w": float(wt)})

    tie_strengths_path = latest_dir / "tie_strengths_w_v2.json"
    _write_json(
        tie_strengths_path,
        {
            "schema_version": "1.0",
            "name": "affinity_tie_strengths_w_v2",
            "cohort_registry_ref": "affinity/artifacts/n50/static/registry/student_registry_v1.json",
            "observations_ref": "affinity/artifacts/n50/generated/latest/observations_v2.json",
            "definition": "w_ij = sum(weight) over events with actor=i and target=j",
            "ties": ties,
        },
    )
    created_files.append(tie_strengths_path)

    # Build and write data-driven coupling operator C_v2 from v2 ties
    C_v2, C_v2_policy = _coupling_operator_from_ties(student_ids=student_ids, w_directed=w)
    coupling_v2_path = latest_dir / "coupling_operator_C_v2.json"
    _write_json(
        coupling_v2_path,
        {
            "schema_version": "1.0",
            "name": "affinity_coupling_operator_C_v2",
            "cohort_registry_ref": "affinity/artifacts/n50/static/registry/student_registry_v1.json",
            "ties_ref": "affinity/artifacts/n50/generated/latest/tie_strengths_w_v2.json",
            "format": {"type": "symmetric_dense", "matrix": [[float(x) for x in row] for row in C_v2.tolist()]},
            "policy": C_v2_policy,
        },
    )
    created_files.append(coupling_v2_path)

    # Propagation + energies using data-driven C_v2
    v = np.linalg.solve(C_v2, s_vec)

    propagated_path = latest_dir / "propagated_value_v_v2.json"
    _write_json(
        propagated_path,
        {
            "schema_version": "1.0",
            "name": "affinity_propagated_value_v_v2",
            "cohort_registry_ref": "affinity/artifacts/n50/static/registry/student_registry_v1.json",
            "source_vector_ref": "affinity/artifacts/n50/generated/latest/source_vector_s_v2.json",
            "coupling_operator_C_ref": "affinity/artifacts/n50/generated/latest/coupling_operator_C_v2.json",
            "definition": "v = G s, computed by solving C v = s",
            "ordering": "node_index_ascending",
            "method": {"type": "solve", "solver": "numpy.linalg.solve", "numpy_only": True},
            "v": [float(x) for x in v.reshape(-1)],
        },
    )
    created_files.append(propagated_path)

    beta0 = 1.0
    beta1 = 1.0
    E = beta0 * s_vec + beta1 * v
    E_eff = beta0 * s_vec + beta1 * (rho_vec * v)

    energy_E_path = latest_dir / "node_energy_E_v2.json"
    _write_json(
        energy_E_path,
        {
            "schema_version": "1.0",
            "name": "affinity_node_energy_E_v2",
            "cohort_registry_ref": "affinity/artifacts/n50/static/registry/student_registry_v1.json",
            "source_vector_ref": "affinity/artifacts/n50/generated/latest/source_vector_s_v2.json",
            "propagated_value_v_ref": "affinity/artifacts/n50/generated/latest/propagated_value_v_v2.json",
            "definition": "E = beta0*s + beta1*v",
            "ordering": "node_index_ascending",
            "parameters": {"beta0": beta0, "beta1": beta1},
            "E": [float(x) for x in E.reshape(-1)],
        },
    )
    created_files.append(energy_E_path)

    energy_E_eff_path = latest_dir / "node_energy_E_eff_v2.json"
    _write_json(
        energy_E_eff_path,
        {
            "schema_version": "1.0",
            "name": "affinity_node_energy_E_eff_v2",
            "cohort_registry_ref": "affinity/artifacts/n50/static/registry/student_registry_v1.json",
            "source_vector_ref": "affinity/artifacts/n50/generated/latest/source_vector_s_v2.json",
            "propagated_value_v_ref": "affinity/artifacts/n50/generated/latest/propagated_value_v_v2.json",
            "definition": "E_eff = beta0*s + beta1*(rho ⊙ v)",
            "ordering": "node_index_ascending",
            "parameters": {"beta0": beta0, "beta1": beta1},
            "rho": [float(x) for x in rho_vec.reshape(-1)],
            "E_eff": [float(x) for x in E_eff.reshape(-1)],
        },
    )
    created_files.append(energy_E_eff_path)

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

    app_outputs_path = latest_dir / "app_facing_outputs_v2.json"
    _write_json(
        app_outputs_path,
        {
            "schema_version": "1.0",
            "name": "affinity_app_facing_outputs_v2",
            "cohort_registry_ref": "affinity/artifacts/n50/static/registry/student_registry_v1.json",
            "inputs": {
                "source_vector_ref": "affinity/artifacts/n50/generated/latest/source_vector_s_v2.json",
                "propagated_value_v_ref": "affinity/artifacts/n50/generated/latest/propagated_value_v_v2.json",
                "energy_E_ref": "affinity/artifacts/n50/generated/latest/node_energy_E_v2.json",
                "energy_E_eff_ref": "affinity/artifacts/n50/generated/latest/node_energy_E_eff_v2.json",
            },
            "canonical_score": "E_eff",
            "top_k": top_k,
            "ranking_policy": {"sort_key": "(-score, node_index)", "score_field": "E_eff", "deterministic": True},
            "rankings": {"by_score": "E_eff", "entries": entries},
            "students": students,
        },
    )
    created_files.append(app_outputs_path)

    if args.snapshot:
        snapshot_dir = _snapshot_run(
            artifacts_dir=latest_dir,
            snapshot_root=snapshot_root,
            run_id=run_id,
            extra_files=extra_snapshot_files,
            created_files=created_files,
        )
        if args.audit:
            print(f"snapshot_dir: {snapshot_dir}")

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
        if neo4j_mode:
            lines.append("mode: neo4j_authoritative_ties")
            if neo4j_ties_json_path is not None:
                lines.append(f"neo4j_ties_source: {neo4j_ties_json_path}")
            if neo4j_readable_json_path is not None:
                lines.append(f"neo4j_readable_source: {neo4j_readable_json_path}")
        else:
            lines.append("mode: simulated_attendance_coattendance")
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
        if not neo4j_mode:
            lines.append("- P(attend) = min(1, a_i * (1 + 0.05*t)), where t=round(3*interest_score), interest_score in [0,1]")
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
        if not neo4j_mode:
            lines.append("")
            lines.append("Modules (derived from shared tags)")
            for t in module_titles:
                lines.append(f"- {t}")
            lines.append("")

        if neo4j_mode:
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
                "out_degree",
                "in_degree",
                "w_out_sum",
                "w_in_sum",
                "v",
                "E",
                "E_eff",
            ]
        else:
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
            if neo4j_mode:
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
                    str(int(out_deg.get(sid, 0))),
                    str(int(in_deg.get(sid, 0))),
                    f"{float(w_out_sum.get(sid, 0.0)):.6g}",
                    f"{float(w_in_sum.get(sid, 0.0)):.6g}",
                    f"{float(v[i]):.6g}",
                    f"{float(E[i]):.6g}",
                    f"{float(E_eff[i]):.6g}",
                ]
            else:
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

        report_path = latest_dir / "optionB_v2_audit_report.txt"
        report_path.write_text("\n".join(lines) + "\n")
        print(report_path.read_text())
        print(f"Wrote audit report: {report_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
