# How to run Affinity v2 (live Neo4j Aura)

This document describes the recommended way to run the **Affinity n=50 v2 (Option B)** pipeline using **Neo4j Aura as the authoritative data source**, while preserving reproducibility via per-run **snapshot folders**.

## Prerequisites

- A working Python environment with repo dependencies installed.
- Neo4j Aura credentials stored in a local `.env` file at the repo root.

Required `.env` variables:

- `NEO4J_URI`
- `NEO4J_USERNAME`
- `NEO4J_PASSWORD`
- `NEO4J_DATABASE` (optional)

## Run command (recommended)

From the repo root:

```bash
python -m network_potential_engine.scripts.run_affinity_n50_generate_artifacts_v2_optionB \
  --neo4j-live \
  --snapshot \
  --audit
```

## What is pulled live from Neo4j

The generator pulls the following live inputs:

- Directed ties `w_ij` (from the Cypher logic in `affinity/from_neo4j/cyphers/tie_strength_runbook/90_export_directed_wij_code_ready.cypher`)
- Student personal properties (used to compute source vector `s` and receptivity proxies such as `rho`)
- Student module interest weights (exported from `(:Person)-[:INTERESTED_IN]->(:Event)` for audit completeness)

## Outputs

### Latest outputs

The generator writes the latest outputs to:

- `affinity/artifacts/n50/`

### Snapshot outputs (recommended for provenance)

When `--snapshot` is provided, the generator also writes a timestamped snapshot folder:

- `affinity/artifacts/n50/snapshots/<run_id>/`

The snapshot contains:

- Versioned live input exports for the run (e.g. personal properties and interest scores)
- Raw rows pulled for live tie export
- Generated pipeline artifacts
- `snapshot_manifest.json`

## What not to commit

Do not commit any of the following:

- `.env`
- `affinity/artifacts/n50/snapshots/`
- generated `*_v2.json` outputs

(These are ignored via `.gitignore` for code-only commits.)
