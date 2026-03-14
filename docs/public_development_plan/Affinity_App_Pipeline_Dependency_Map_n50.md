# Affinity App (n=50 cohort) — Research-Grade Pipeline Dependency Map

## Purpose of this document

This document is a **partner dependency map** to:

- `docs/development_plan/Network_Potential_Framework_Dependency_Map.md`

It translates the framework’s object layers (P-series) into concrete **jobs** required to build an end-to-end, **research-grade** pipeline that:

- ingests data about a cohort of `n = 50` students,
- instantiates the framework objects and assumptions in a disciplined way,
- produces mathematically grounded outputs that help those students via the Affinity app.

This document is **not itself a theorem specification**. It is a planning artifact that enumerates what must be built, in what order, and what “done” means.

Note: for the current v2 implementation, the pipeline supports pulling inputs live from Neo4j Aura and writing per-run provenance bundles under `affinity/artifacts/n50/snapshots/<run_id>/`. See `docs/how_to_run_affinity_v2_live_neo4j.md`.

---

## Status indicators

- ★ Verified (tested + documented; n=50 runner/artifact exists + evidence/paperwork completed)
- ✓ Cohort-ready (n=50 runner/artifact exists)
- ◐ Framework-ready (core code exists; n=50 runner/artifact not done)
- ○ Not started (no n=50 runner/artifact yet)

---

# Jobs in order (research-grade, n=50)

This plan is written using **backward design**:

- We start from the **required research-grade outputs** (rankings + explanations) and the **framework objects** they depend on.
- From that, we derive what must be specified upstream (energy choice, propagation, operators, equilibrium, potential).
- Only then do we derive the **minimal data schema we need** (and how it populates `x`, `s`, and `θ`).

To keep implementation practical, the job list below is presented in **execution order** (what you build/run first), even though the requirements logic is derived backward from the pipeline.

Each job lists:

- **What you produce** (the object/output)
- **What it depends on**
- **Completion gate** (how we know it’s done)

---

## Backward-design trace (conceptual, not execution order)

```text
App outputs (rankings + explanations)
  -> choose canonical score (E vs E_eff) and explanation decomposition
  -> need energies (E, E_eff)
  -> need propagation (v = G s)
  -> need Green operator (G) / linear solve policy
  -> need coupling (C = -∇²_{ww}Φ(w*,θ))
  -> need equilibrium network (w*) and feasibility regime
  -> need explicit potential Φ(w,θ) and a θ policy
  -> need source mapping ψ and node attributes x
  -> need minimal observations schema to populate x and θ (and any support constraints)
  -> need registry / node indexing discipline (V)
```

## Job 0 — Agree and freeze this pipeline (research-grade jobs-in-order)

- **Status**
  - ★ Verified
- **What you produce**
  - an approved, frozen version of this document as the authoritative “run order” for research-grade n=50 work
- **Depends on**
  - nothing
- **Evidence / paperwork**
  - a committed version of this file that is explicitly marked as approved (e.g. via git history / PR / sign-off note)
- **Completion gate**
  - this job list is explicitly approved as the starting point, and changes thereafter are treated as controlled revisions

## Job 1 — Fix cohort indexing (V) and student registry

- **Status**
  - ★ Verified
- **What you produce**
  - a single source of truth for the cohort node set `V` (size n=50) and a stable ordering / registry of students
  - a canonical student identifier policy that all downstream artifacts use
- **Depends on**
  - Job 0
- **Evidence / paperwork**
  - a committed `n=50` cohort registry artifact and a validation transcript that counts to 50 and checks uniqueness:
    - `affinity/artifacts/n50/static/registry/student_registry_v1.json`
    - `affinity/artifacts/n50/static/registry/student_registry_v1_validation.txt`
- **Completion gate**
  - you can point to a single registry file and every downstream job references it, with no “index drift” ambiguity

---

## Job 2 — Define a minimal data schema we need to ingest (observations)

- **Status**
  - ★ Verified
- **What you produce**
  - a JSON/CSV schema for the minimal observations required by the research-grade run (events/interactions/exposures), even if initially mock-generated
  - an explicit mapping from observations to upstream formal inputs (what populates `x` and what populates `θ`)
- **Depends on**
  - Job 1
- **Evidence / paperwork**
  - a schema document/example file + a validation transcript for one sample dataset:
    - `affinity/artifacts/n50/static/schemas/observations_schema_v1.json`
    - `affinity/artifacts/n50/legacy/v1/observations_sample_v1.json`
    - `affinity/artifacts/n50/static/schemas/observations_schema_v1_validation.txt`
- **Completion gate**
  - raw data can be loaded and validated (types, missingness policy)

---

## Job 3 — Build node attributes x (including capacities r)

- **Status**
  - ★ Verified
- **What you produce**
  - `x_i := (r_i, extras_i)` for each student
  - `x := (x_i)_{i∈V}`
- **Depends on**
  - Job 1
- **Repo anchors**
  - `src/network_potential_engine/attributes/node_attributes.py`
- **Evidence / paperwork**
  - a serialized `NodeAttributeField` artifact for n=50 + a validation transcript (required keys present):
    - `affinity/artifacts/n50/legacy/v1/node_attribute_field_v1.json`
    - `affinity/artifacts/n50/legacy/v1/node_attribute_field_v1_validation.txt`
- **Completion gate**
  - a validated `NodeAttributeField` exists for all 50 students

---

## Job 4 — Lock ψ and compute source values s

- **Status**
  - ★ Verified
- **What you produce**
  - a production mapping `ψ` and the source vector `s` where `s_i = ψ(x_i)`
- **Depends on**
  - Job 3
- **Repo anchors**
  - `src/network_potential_engine/source/node_source_value.py`
  - `src/network_potential_engine/source/value_model.py`
- **Evidence / paperwork**
  - a saved `s` vector (with node IDs) + a short note stating the frozen `ψ` used:
    - `affinity/artifacts/n50/static/specs/source_mapping_psi_v1.txt`
    - `affinity/artifacts/n50/legacy/v1/source_vector_s_v1.json`
    - `affinity/artifacts/n50/legacy/v1/source_vector_s_v1_validation.txt`
- **Completion gate**
  - `s` is computed deterministically and matches the declared `ψ`

---

## Job 5 — Declare the feasibility regime W_feas(r) we are using

- **Status**
  - ★ Verified
- **What you produce**
  - an explicit statement of the feasibility regime:
    - interior/unconstrained (constraints inactive), or
    - constrained (KKT/VI)
- **Depends on**
  - Job 3
- **Repo anchors**
  - `src/network_potential_engine/constraints/feasible_relational_investment.py`
- **Evidence / paperwork**
  - a short “feasibility regime declaration” note (interior vs constrained) + feasibility diagnostics output for one run:
    - `affinity/artifacts/n50/legacy/v1/feasibility_regime_v1.txt`
    - `affinity/artifacts/n50/legacy/v1/feasibility_diagnostics_v1.txt`
- **Completion gate**
  - the regime is written down and feasibility diagnostics are defined (even if not yet binding)

---

## Job 6 — Select a baseline potential Φ(w,θ) and define θ (Approach 1)

- **Status**
  - ★ Verified
- **What you produce**
  - a named potential `Φ(w, θ)` from existing repo instantiations
  - a policy for what `θ` means and how it is constructed from cohort signals
- **Depends on**
  - Jobs 1–5
- **Repo anchors**
  - `src/network_potential_engine/symbolic/potential.py`
- **Evidence / paperwork**
  - a written spec for `Φ` and `θ` (meaning, dimensionality, construction) + a reproducible parameter dump used by the run:
    - `affinity/artifacts/n50/static/specs/potential_phi_and_theta_spec_v1.md`
    - `affinity/artifacts/n50/legacy/v1/potential_phi_and_theta_params_v1.json`
- **Completion gate**
  - `Φ` is selected and parameterized, and `θ` construction is frozen for the n=50 run

---

## Job 7 — Compute or license an equilibrium w*

- **Status**
  - ★ Verified
- **What you produce**
  - an equilibrium candidate `w*` (with explicit diagnostics)
- **Depends on**
  - Job 6
- **Repo anchors**
  - `src/network_potential_engine/numeric/equilibrium.py`
- **Evidence / paperwork**
  - a saved `w*` artifact + solver diagnostics (residual norms, iterations, constraint status):
    - `affinity/artifacts/n50/legacy/v1/equilibrium_w_star_v1.json`
    - `affinity/artifacts/n50/legacy/v1/equilibrium_w_star_v1_diagnostics.txt`
- **Completion gate**
  - residual norms and (if relevant) constraint diagnostics are produced with a clear pass/fail threshold

---

## Job 8 — Compute coupling operator C = -∇²_{ww}Φ(w*,θ)

- **Status**
  - ★ Verified
- **What you produce**
  - Hessian `H(w*,θ)` and coupling matrix `C(w*,θ) = -H(w*,θ)`
- **Depends on**
  - Job 7
- **Repo anchors**
  - `src/network_potential_engine/symbolic/hessian.py`
  - `src/network_potential_engine/symbolic/operators.py`
- **Evidence / paperwork**
  - a saved `C` artifact + shape/symmetry/sign diagnostics report:
    - `affinity/artifacts/n50/legacy/v1/coupling_operator_C_v1.json`
    - `affinity/artifacts/n50/legacy/v1/coupling_operator_C_v1_diagnostics.txt`
- **Completion gate**
  - `C` is computed at n=50 with shape checks and stored diagnostics

---

## Job 9 — Construct Green operator G = C^{-1} (or solve with C)

- **Status**
  - ★ Verified
- **What you produce**
  - a certified way to apply `G` to vectors (explicit inverse or linear solve)
- **Depends on**
  - Job 8
- **Repo anchors**
  - `src/network_potential_engine/numeric/green_operator.py`
  - `src/network_potential_engine/numeric/response.py`
- **Evidence / paperwork**
  - conditioning/invertibility diagnostics (e.g. rank/cond/solver status) + declared policy for failure/regularization:
    - `affinity/artifacts/n50/legacy/v1/green_operator_G_v1_diagnostics.txt`
    - `affinity/artifacts/n50/static/specs/green_operator_G_v1_policy.txt`
- **Completion gate**
  - invertibility/certification diagnostics are produced; failure mode is explicit if `C` is singular/ill-conditioned

---

## Job 10 — Propagate values: v = Gs (solve C v = s)

- **Status**
  - ★ Verified
- **What you produce**
  - propagated value vector `v`
- **Depends on**
  - Jobs 4 and 9
- **Evidence / paperwork**
  - a saved `v` artifact + residual report `||C v - s||`:
    - `affinity/artifacts/n50/legacy/v1/propagated_value_v_v1.json`
    - `affinity/artifacts/n50/legacy/v1/propagated_value_v_v1_residual.txt`
- **Completion gate**
  - propagation residual check passes: `||C v - s||` below tolerance

---

## Job 11 — Compute energies (E and E_eff)

- **Status**
  - ★ Verified
- **What you produce**
  - `E = beta0*s + beta1*v`
  - `E_eff = beta0*s + beta1*(rho ⊙ v)` (with declared `rho`)
- **Depends on**
  - Job 10
- **Repo anchors**
  - `src/network_potential_engine/energy/node_energy.py`
  - `src/network_potential_engine/energy/effective_energy.py`
- **Evidence / paperwork**
  - saved `E` / `E_eff` artifacts + ranking summary (top-k) and a note declaring which score is canonical:
    - `affinity/artifacts/n50/legacy/v1/node_energy_E_v1.json`
    - `affinity/artifacts/n50/legacy/v1/node_energy_E_eff_v1.json`
    - `affinity/artifacts/n50/legacy/v1/node_energy_rankings_topk_v1.txt`
    - `affinity/artifacts/n50/legacy/v1/node_energy_canonical_score_v1.txt`
- **Completion gate**
  - stable top-k rankings exist for `s`, `v`, `E`, `E_eff`

---

## Job 12 — Export app-facing outputs (rankings + explanations)

- **Status**
  - ★ Verified
- **What you produce**
  - an output schema (JSON) containing:
    - rankings (e.g. top-k by `E_eff`)
    - per-student decomposition/explanation (intrinsic vs network component)
- **Depends on**
  - Job 11
- **Evidence / paperwork**
  - exported JSON outputs + a rendered report example demonstrating explanation fields:
    - `affinity/artifacts/n50/legacy/v1/app_facing_outputs_v1.json`
    - `affinity/artifacts/n50/static/examples/app_facing_outputs_v1_report_example.md`
- **Completion gate**
  - outputs can be rendered in a report and are stable under reruns

---

## Job 13 — Research-grade correctness checks (smoke run transcript)

- **Status**
  - ★ Verified
- **What you produce**
  - a single-command cohort-scale run that prints:
    - equilibrium diagnostics
    - coupling/Green diagnostics
    - propagation residual diagnostics
    - energy summaries
- **Depends on**
  - Jobs 6–12
- **Evidence / paperwork**
  - a single saved “run transcript” (stdout/log file) with seed/config, diagnostics, and pass/fail summary:
    - `affinity/artifacts/n50/legacy/v1/smoke_run_transcript_v1.txt`
- **Completion gate**
  - one command produces an auditable transcript for the n=50 run

---

## Job 14 — Product validity checks (does it help students?)

- **Status**
  - ★ Verified
- **What you produce**
  - scenario tests / offline metrics that check qualitative behavior
- **Depends on**
  - Job 12
- **Evidence / paperwork**
  - scenario definitions + saved outputs + a short evaluation note (expected vs observed qualitative behavior)
    - `affinity/artifacts/n50/legacy/v1/product_validity_scenarios_v1.json`
    - `affinity/artifacts/n50/legacy/v1/product_validity_outputs_v1.json`
    - `affinity/artifacts/n50/legacy/v1/product_validity_evaluation_note_v1.txt`
- **Completion gate**
  - at least 2 scenarios match declared qualitative expectations

---

# Overall completion gates (v0)

The Affinity research-grade n=50 pipeline is “v0 complete” when:

- ○ Jobs 1–13 run end-to-end with explicit diagnostics.
- ○ Outputs are exported in an app-facing schema with per-student explanations.
- ○ The run is reproducible and auditable.
