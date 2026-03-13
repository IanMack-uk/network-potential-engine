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
    print(f"AFFINITY N50 V2 FULL TRANSCRIPT: {name}")
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
    args = parser.parse_args()

    repo_root = _find_repo_root(Path(__file__).resolve())

    env = dict(os.environ)
    env["PYTHONPATH"] = "src" + (":" + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")

    _run_step(
        "Generate v2 artifacts (Option B) + audit output",
        [
            sys.executable,
            "-m",
            "network_potential_engine.scripts.run_affinity_n50_generate_artifacts_v2_optionB",
            "--audit",
        ],
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
    print("AFFINITY N50 V2 FULL TRANSCRIPT: PASS")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
