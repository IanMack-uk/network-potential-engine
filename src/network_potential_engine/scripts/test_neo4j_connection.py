from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path

from neo4j import GraphDatabase


def _find_repo_root(start: Path) -> Path:
    p = start
    while True:
        if (p / ".git").exists() or (p / "pyproject.toml").exists():
            return p
        if p.parent == p:
            raise RuntimeError("Could not locate repo root (.git or pyproject.toml)")
        p = p.parent


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


def _load_config(repo_root: Path) -> _Neo4jConfig:
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


def main() -> int:
    repo_root = _find_repo_root(Path(__file__).resolve())
    cfg = _load_config(repo_root)

    query = "MATCH (person:Person) RETURN count(person) AS n"

    driver = GraphDatabase.driver(cfg.uri, auth=(cfg.username, cfg.password))
    try:
        with driver.session(database=cfg.database) as session:
            rec = session.run(query).single()
            n = None if rec is None else rec.get("n")
            print(f"OK: connected to Neo4j at {cfg.uri}")
            if cfg.database:
                print(f"database: {cfg.database}")
            print(f"Person count: {n}")
    finally:
        driver.close()

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        raise
