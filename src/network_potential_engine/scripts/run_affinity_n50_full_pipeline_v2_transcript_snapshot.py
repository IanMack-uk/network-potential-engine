from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def _find_repo_root(start: Path) -> Path:
    p = start
    while True:
        if (p / ".git").exists():
            return p
        if p.parent == p:
            raise RuntimeError("Could not find repo root")
        p = p.parent


def _run_step(name: str, args: list[str], *, cwd: Path, env: dict[str, str]) -> None:
    print("=" * 78)
    print(f"AFFINITY N50 V2 FULL TRANSCRIPT (SNAPSHOT): {name}")
    print("=" * 78)
    proc = subprocess.run(args, cwd=str(cwd), env=env)
    if proc.returncode != 0:
        raise SystemExit(proc.returncode)
    print()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--include-certified",
        action="store_true",
        help="Also run the theorem-level certified checker (model checks, not data-driven).",
    )
    parser.add_argument(
        "--seed",
        default=None,
        help="Optional scenario seed forwarded to the artifact generator.",
    )
    parser.add_argument(
        "--neo4j-ties-json",
        default=None,
        help="Path to Neo4j-exported directed tie weights JSON forwarded to the artifact generator.",
    )
    parser.add_argument(
        "--neo4j-readable-json",
        default=None,
        help="Optional path to Neo4j-exported readable tie table JSON forwarded to the artifact generator.",
    )
    parser.add_argument(
        "--neo4j-live",
        action="store_true",
        help="If set, connect to Neo4j using .env and pull ties live (forwarded to artifact generator).",
    )
    parser.add_argument(
        "--snapshot-dir",
        default="",
        help=(
            "Optional snapshot directory (relative to repo root). If not set, defaults to affinity/artifacts/n50/generated/snapshots."
        ),
    )
    args = parser.parse_args()

    repo_root = _find_repo_root(Path(__file__).resolve())

    env = dict(os.environ)
    env["PYTHONPATH"] = "src" + (":" + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")

    artifact_args: list[str] = [
        sys.executable,
        "-m",
        "network_potential_engine.scripts.run_affinity_n50_generate_artifacts_v2_optionB",
        "--audit",
        "--snapshot",
    ]

    if args.seed is not None:
        artifact_args.extend(["--seed", str(args.seed)])

    if args.neo4j_ties_json is not None:
        artifact_args.extend(["--neo4j-ties-json", str(args.neo4j_ties_json)])

    if args.neo4j_readable_json is not None:
        artifact_args.extend(["--neo4j-readable-json", str(args.neo4j_readable_json)])

    if args.neo4j_live:
        artifact_args.append("--neo4j-live")

    if str(args.snapshot_dir).strip():
        artifact_args.extend(["--snapshot-dir", str(args.snapshot_dir)])

    _run_step(
        "Generate v2 artifacts (Option B) + audit output + SNAPSHOT",
        artifact_args,
        cwd=repo_root,
        env=env,
    )

    _run_step(
        "Smoke transcript v2 (validates artifacts + PASS/FAIL)",
        [sys.executable, "-m", "network_potential_engine.scripts.run_affinity_n50_smoke_transcript_v2"],
        cwd=repo_root,
        env=env,
    )

    if args.include_certified:
        _run_step(
            "Certified pipeline checker (P-series / TDC symbolic checks)",
            [sys.executable, "-m", "network_potential_engine.scripts.check_full_certified_pipeline"],
            cwd=repo_root,
            env=env,
        )

    print("=" * 78)
    print("AFFINITY N50 V2 FULL TRANSCRIPT (SNAPSHOT): PASS")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
