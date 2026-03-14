# Job 6 — Potential Φ(w,θ) + θ specification (v1)

## Purpose

Freeze the exact baseline potential `Φ(w,θ)` and the construction/meaning of `θ` for the Affinity n=50 v1 run.

This spec is the authoritative reference for Jobs 7–10.

## Selected Φ(w,θ)

- **Name**: `theta_dependent_curvature_potential`
- **Repo anchor**: `src/network_potential_engine/symbolic/potential.py`
- **Signature (as implemented)**:
  - `theta_dependent_curvature_potential(w, theta, base_quadratic_weight=1, theta_curvature_weight=1/5, coupling_weight=1/2)`

## Mathematical form (as implemented)

Given `w ∈ R^n` (column vector) and `θ ∈ R^n` (column vector), with `n=50`:

`Φ(w,θ) = Σ_i θ_i w_i - (1/2) Σ_i (q + α θ_i) w_i^2 - (c/2) Σ_{i=0}^{n-2} (w_i - w_{i+1})^2`

where:

- `q = base_quadratic_weight`
- `α = theta_curvature_weight`
- `c = coupling_weight`

## Parameterization (v1)

- `base_quadratic_weight (q) = 1.0`
- `theta_curvature_weight (α) = 0.2` (i.e. `1/5`)
- `coupling_weight (c) = 0.5` (i.e. `1/2`)

## Definition of θ (v1)

- **Meaning**:
  - `θ_i` is the per-node parameter used by `Φ`.
- **Construction policy (frozen)**:
  - For v1, set `θ := s` where `s` is the Job 4 source vector.

### Data sources

- Source vector:
  - `affinity/artifacts/n50/legacy/v1/source_vector_s_v1.json`
- Cohort ordering:
  - `affinity/artifacts/n50/static/registry/student_registry_v1.json`

### Ordering rule

- `θ` is constructed as a length-50 column vector ordered by `node_index` (0..49) from the registry.
- For each index `i`, the value is the `s` associated with that registry student.

### v1 consequence

- Since Job 4 produced `s_i = 1.0` for all students, v1 uses:
  - `θ_i = 1.0` for all `i`.

## Exclusions / constraints

- No PII-derived features are permitted in `θ`.
- No randomness permitted in `θ` construction.

## Evidence linkage

- Parameter dump used by the run:
  - `affinity/artifacts/n50/legacy/v1/potential_phi_and_theta_params_v1.json`
