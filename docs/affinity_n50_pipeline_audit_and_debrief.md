# Affinity n=50 pipeline — Complete audit + debrief

## 1) Executive audit summary

### What’s complete right now

- Jobs 0–14 are implemented at n=50 scale with concrete artifacts under:
  - `affinity/artifacts/n50/`
- There is a one-command verification transcript (Job 13) that re-checks the key invariants for Jobs 6–12 and writes an auditable transcript:
  - `affinity/artifacts/n50/smoke_run_transcript_v1.txt`
- There is a “product validity harness” (Job 14) that runs two scenarios and writes:
  - scenario definitions
  - scenario outputs
  - evaluation note

### What is “research-grade” vs “product-grade”

- Research-grade traceability is good: artifacts are versioned, deterministic, and include definitions + references.
- Product-grade validity is not claimed (and shouldn’t be yet): the current n=50 run is built on placeholder-uniform signal choices, so behavior is mostly testing coherence and monotonicity rather than “helps students”.

---

## 2) Artifact inventory (authoritative evidence in repo)

Everything below exists in `affinity/artifacts/n50/`.

### Jobs 1–4: cohort + schema + source

- Registry
  - `student_registry_v1.json`
  - `student_registry_v1_validation.txt`
- Observation schema + sample
  - `observations_schema_v1.json`
  - `observations_schema_v1_validation.txt`
  - `observations_sample_v1.json`
- Node attributes
  - `node_attribute_field_v1.json`
  - `node_attribute_field_v1_validation.txt`
- Source mapping + source vector
  - `source_mapping_psi_v1.txt`
  - `source_vector_s_v1.json`
  - `source_vector_s_v1_validation.txt`

### Jobs 5–9: regime + Φ/θ + equilibrium + operators

- Feasibility regime
  - `feasibility_regime_v1.txt`
  - `feasibility_diagnostics_v1.txt`
- Baseline potential specification / parameters
  - `potential_phi_and_theta_spec_v1.md`
  - `potential_phi_and_theta_params_v1.json`
- Equilibrium
  - `equilibrium_w_star_v1.json`
  - `equilibrium_w_star_v1_diagnostics.txt`
- Coupling operator
  - `coupling_operator_C_v1.json`
  - `coupling_operator_C_v1_diagnostics.txt`
- Green operator “apply policy” + diagnostics
  - `green_operator_G_v1_policy.txt`
  - `green_operator_G_v1_diagnostics.txt`

### Jobs 10–12: propagation + energies + export

- Propagation
  - `propagated_value_v_v1.json`
  - `propagated_value_v_v1_residual.txt`
- Energies
  - `node_energy_E_v1.json`
  - `node_energy_E_eff_v1.json`
  - `node_energy_rankings_topk_v1.txt`
  - `node_energy_canonical_score_v1.txt`
- App-facing export
  - `app_facing_outputs_v1.json`
  - `app_facing_outputs_v1_report_example.md`

### Job 13: single-command smoke transcript (verification harness)

- `smoke_run_transcript_v1.txt`

### Job 14: product validity checks

- `product_validity_scenarios_v1.json`
- `product_validity_outputs_v1.json`
- `product_validity_evaluation_note_v1.txt`

---

## 3) Runner scripts (single-command reproducibility)

### Job 13 runner (verifies Jobs 6–12 artifacts, recomputes key residuals)

- Script:
  - `src/network_potential_engine/scripts/run_affinity_n50_smoke_transcript_v1.py`
- Command:

```bash
PYTHONPATH=src python3 -m network_potential_engine.scripts.run_affinity_n50_smoke_transcript_v1
```

- Writes:
  - `affinity/artifacts/n50/smoke_run_transcript_v1.txt`

### Job 14 runner (scenario harness; writes 3 evidence artifacts)

- Script:
  - `src/network_potential_engine/scripts/run_affinity_n50_product_validity_checks_v1.py`
- Command:

```bash
PYTHONPATH=src python3 -m network_potential_engine.scripts.run_affinity_n50_product_validity_checks_v1
```

- Writes:
  - `affinity/artifacts/n50/product_validity_scenarios_v1.json`
  - `affinity/artifacts/n50/product_validity_outputs_v1.json`
  - `affinity/artifacts/n50/product_validity_evaluation_note_v1.txt`

---

## 4) Git audit (recent evidence commits)

Recent “job-level” evidence commits show the pipeline being completed in order:

- Job 7 (equilibrium): `c6e6c11`
- Job 8 (coupling operator): `5aa5536`
- Job 9 (Green operator diagnostics/policy): `9d9c27a`
- Job 10 (propagation + residual): `4864697`
- Job 11 (energies + ranking summary): `63ad827`
- Job 12 (app-facing export): `16e0145`
- Job 13 (smoke transcript runner + transcript): `99a9c3d`
- Job 14 (validity runner + artifacts): `61a8d70`

---

## 5) Important pipeline invariants that are currently verified

From the Job 13 transcript (successful run):

- Registry / shape checks: PASS
- Propagation residual: recomputed `||C v - s||` is ~`1e-15` (PASS vs tol `1e-10`)
- Energy identities: PASS under frozen parameters
- Export JSON consistency: canonical score is `E_eff`, ranking deterministic tie-break `(-score, node_index)` matches

From Job 14:

- S1: explanation coherence + ranking coherence PASS
- S2: uplift monotonicity PASS (under the counterfactual model used)

---

# Debrief: what is placeholder vs “real-data-ready”

## A) What is placeholder / harness-level (by design right now)

- `s` is uniform (all ones) in `source_vector_s_v1.json`
  - intrinsic signal is constant across students.
- `rho` is all ones (Job 11 policy)
  - no receptivity heterogeneity.
- Consequence:
  - `E_eff = s + v` is nearly constant here.
  - rankings become mostly about deterministic tie-break policy (node index), not substantive differences.
- Job 14 S2 counterfactual currently changes `s` while holding `v` fixed
  - a controlled harness check, not a full re-run of upstream physics.

This is appropriate for v1: it proves wiring, schema, determinism, and math identities.
It should be interpreted as an infrastructure/coherence validation, not a substantive modelling validation.
For the current theorem–pipeline semantic boundary, see `docs/theorem_pipeline_bridge.md`.

## B) What is already “real-data-ready” (architecture-wise)

- Artifact contract is in place (each stage saves an auditable output).
- Ordering contract is in place (registry-based stable `node_index`).
- Operator flow is in place:
  - equilibrium → Hessian/coupling operator → solve-based Green application → propagation → energies → export
- Verification harness (Job 13) will still work when values become non-uniform, as long as schema stays consistent.

## C) The main “missing link” to become substantive

You need nontrivial, data-driven inputs:

- A non-uniform source mapping `ψ` producing heterogeneous `s`
- Potentially nontrivial receptivity `ρ`
- A `Φ(w,θ)` and `θ` reflecting real relational structure and calibrated parameters

Once those are real, you should expect:

- nontrivial variation in `v`
- nontrivial variation in `E_eff`
- rankings that are not tie-break artifacts
- Job 14 scenarios can become much more meaningful (e.g., “increase s for a node should increase its score and also propagate appropriately through v” if you re-run upstream steps)

---

# Key risks / weak spots

## 1) Git-ignored tracking docs

Your pipeline map + dev briefs live under `docs/development_plan/`, which is git-ignored.

- Impact:
  - the repo has runnable artifacts and code,
  - but the “official job status ledger” is local-only.
- Risk:
  - cloning elsewhere loses the local status marks unless you copy those files.

## 2) Job 14 counterfactual is intentionally simplified

S2 currently checks a monotonicity property in a way that is guaranteed under `E_eff = s + v` with fixed `v`.

- Good for: proving export/score/ranking machinery monotonicity.
- Not a: full “recompute pipeline under counterfactual inputs” test.

A next evolution is: counterfactual `s'` → solve `C v' = s'` → recompute `E_eff'` → compare.

---

# Recommended next hardening steps

## 1) Add a true counterfactual re-run scenario (Job 14 v2)

- Construct `s'` with one node uplifted
- Recompute `v'` by solving `C v' = s'`
- Recompute energies and re-rank
- Check:
  - target score increases
  - neighbors respond in expected direction (depending on operator structure)

## 2) Introduce one non-uniform “toy realism” input set (n=50 v2)

Without touching Neo4j:

- make `s` mildly heterogeneous (deterministic function of `node_index`)
- make `rho` mildly heterogeneous

This would immediately make ranking substantive while remaining deterministic and non-PII.

## 3) Add a single “pipeline regen” runner

You have strong verification scripts (Jobs 13/14), but not necessarily a single runner that regenerates every artifact from scratch for n=50.

If you want “one command rebuilds everything”, add an orchestrator that re-runs Jobs 4–14.

---

# “How do we run these values through the pipeline again?”

## Verification rerun (no regeneration, just checks)

- Job 13:

```bash
PYTHONPATH=src python3 -m network_potential_engine.scripts.run_affinity_n50_smoke_transcript_v1
```

- Job 14:

```bash
PYTHONPATH=src python3 -m network_potential_engine.scripts.run_affinity_n50_product_validity_checks_v1
```

## Regeneration (change upstream inputs)

Today, if you change `source_vector_s_v1.json` manually, you would also need to regenerate:

- propagation `v` (Job 10)
- energies (Job 11)
- export (Job 12)

…and then rerun Jobs 13–14.

A “regen runner” could orchestrate that automatically, but it doesn’t exist yet as a single command.
