# Theorem–Pipeline Bridge Note

## Purpose

This document defines the current mapping between:

- theorem-side objects in `docs/theorems/tdc/tdc_local_ordering_theorem_formal.md`, and
- pipeline-side objects and artifacts audited by the Affinity pipeline (e.g. `affinity/artifacts/n50/`).

It is an architectural boundary note. It does not add new mathematics, and it does not claim that theorem results automatically apply to pipeline rankings.

## Mapping status taxonomy

Each mapping below is classified as one of:

| Mapping status | Meaning |
|---|---|
| Identity | The same mathematical object (after aligning notation). |
| Implementation equivalent | Algorithmically equivalent construction of the same mathematical object, possibly with modelling parameters frozen and/or discretized choices fixed. |
| Modelling interpretation | A conceptual interpretation linking a pipeline object to a theorem object, without a certified identity/equivalence. |
| Not yet implemented | The theorem object has no pipeline counterpart at present. |

## Core object mapping

| Theorem-side object | Pipeline-side object | Mapping status | Notes / boundary |
|---|---|---|---|
| \(C(\theta)\) (coupling operator) | `affinity/artifacts/n50/generated/latest/coupling_operator_C_v2.json` | Implementation equivalent | Pipeline constructs \(C\) as \(I + \alpha L + \varepsilon I\) from ties via a Laplacian. This is not the same parametric family as the tridiagonal TDC \(C(\theta)\); it is a network-Laplacian operator used by the Affinity pipeline. The shared symbol \(C\) is an operator-role analogy, not a proven identity between models. |
| \(s\) (source vector) | `affinity/artifacts/n50/generated/latest/source_vector_s_v2.json` | Implementation equivalent | Pipeline source \(s\) is a constructed input vector. It is not currently a theorem-side \(\theta\) parameter; it plays the role of an exogenous forcing term in the linear solve. |
| \(v\) (propagated value / potential response) | `affinity/artifacts/n50/generated/latest/propagated_value_v_v2.json` | Implementation equivalent | Pipeline solves \(Cv = s\). This is a Green-operator style propagation step. It is not currently certified as the derivative response \(D_\theta w^*(\theta)\) from the TDC theorem chain. |
| \(E\) (energy) | `affinity/artifacts/n50/generated/latest/node_energy_E_v2.json` | Implementation equivalent | Pipeline defines \(E = s + v\) as an audited identity. This is a pipeline-level definition; it is not a theorem-level energy functional in the TDC documents. |
| \(\rho\) (receptivity weights) | derived from observations in `affinity/artifacts/n50/generated/latest/observations_v2.json` and audited in transcript | Modelling interpretation | \(\rho\) is a pipeline receptivity field. There is no direct counterpart in the current TDC theorem chain. Note: in Neo4j-authoritative ties mode, `observations_v2.json` may be a provenance stub (with no event list) and should be treated as metadata rather than a primary signal source. |
| \(E_{\mathrm{eff}}\) (effective energy) | `affinity/artifacts/n50/generated/latest/node_energy_E_eff_v2.json` | Implementation equivalent | Pipeline defines \(E_{\mathrm{eff}} = s + \rho \odot v\). This is an audited identity given \(s\), \(\rho\), and \(v\). |
| \(w^*(\theta)\) (equilibrium) | none in v2 Affinity artifacts | Not yet implemented | The Affinity v2 pipeline does not currently compute an equilibrium \(w^*(\theta)\) for a \(\theta\)-parametric potential. Any link between Affinity ranking outputs and the TDC equilibrium map is therefore interpretive only at present. |

## Transfer status of theorem claims to pipeline

- **Transfers now (as audited identities / deterministic replay)**
  - Pipeline identities and reconstruction checks (e.g. \(Cv=s\), \(E=s+v\), \(E_{\mathrm{eff}}=s+\rho\odot v\)) transfer as *pipeline definitions plus audited arithmetic*.

- **Transfers only conditionally (modelling interpretation, not yet certified)**
  - Any claim that interprets pipeline rankings as monotone comparative statics of a theorem-side equilibrium requires an explicit, certified mapping from pipeline objects to the theorem model (in particular, a defined \(\theta\) and a computed \(w^*(\theta)\)).

- **Does not transfer yet**
  - The TDC monotonicity/ordering theorem does not currently certify anything directly about Affinity rankings, because the theorem-side equilibrium object \(w^*(\theta)\) is not instantiated in the Affinity pipeline and the operator families differ.

## Evidence pointers

- Theorem-side specification: `docs/theorems/tdc/tdc_local_ordering_theorem_formal.md`
- Theorem certification ledger: `docs/theorems/tdc/tdc_certification_ledger.md`
- Pipeline certification ledger: `docs/audits/affinity_pipeline_certification_ledger.md`
- Affinity pipeline audit transcript (v2): `affinity/artifacts/n50/generated/latest/data_driven_full_audit_transcript_v2.txt`
