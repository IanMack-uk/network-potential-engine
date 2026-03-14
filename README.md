# Network Potential Engine

This repository implements and audits a network-based potential framework
linking formal theory, computational verification, and pipeline artifacts.

## Verification & Certification Framework

The repository includes an explicit certification structure connecting
formal mathematical results to verification scripts and computational outputs.

Key documents:

- `docs/README.md` – documentation index
- `docs/certification_framework.md` – overview of the repository's certification architecture
- `docs/verification_boundary.md` – claims register defining what is proven, verified, or demonstrated
- `docs/theorem_pipeline_bridge.md` – theorem-to-pipeline mapping and current semantic transfer boundary
- `docs/theorems/tdc/tdc_certification_ledger.md` – theorem-to-code verification mapping
- `docs/audits/affinity_pipeline_certification_ledger.md` – pipeline-to-artifact audit mapping

These documents allow readers to trace claims from **theory → verification scripts → artifacts**.

## Affinity v2 (live Neo4j Aura)

To run the current Affinity n=50 v2 pipeline against Neo4j Aura (authoritative inputs) while writing a per-run provenance snapshot:

- `docs/how_to_run_affinity_v2_live_neo4j.md`

Neo4j tie-strength model + runbook:

- `affinity/from_neo4j/TIE_STRENGTH_MODEL.md`
- `affinity/from_neo4j/cyphers/tie_strength_runbook/RUNBOOK.md`

## Repository Structure

```
docs/
  certification_framework.md
  verification_boundary.md
  theorem_pipeline_bridge.md

  theorems/
    tdc/
      tdc_local_ordering_theorem_formal.md
      tdc_certification_ledger.md

  audits/
    affinity_pipeline_certification_ledger.md
```

## Key Components

- **Theorem layer** – formal results describing the network potential framework.
- **Certification ledgers** – map claims to verification mechanisms.
- **Verification scripts** – executable checks validating theory and pipeline outputs.
- **Artifacts** – exported computational results used for audit and reproduction.

See `docs/certification_framework.md` for a full explanation of the verification architecture.
