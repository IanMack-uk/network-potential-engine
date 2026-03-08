# Theorem Workflow Progress Checklist

This document is a living checklist for tracking progress through the Network Potential Framework theorem workflow.

It is aligned to the dependency graph in:

- `docs/development_plan/theorem_dependency_and_tdc_alignment.md`

---

## Dependency graph summary (at a glance)

```text
FOUNDATIONS
A1  Well-Posedness of the Admissible Relational Potential  [complete]
  |
A2  Equilibrium Existence  [complete]
  |
A3  Interior Nondegeneracy / Strict Local Maximum  [complete]
  |
  +----------------------+
  |                      |
  v                      |
OPERATOR                |
B1  Hessian-Coupling Theorem  [complete]
  |
B2  Locality / Incident Structure Inheritance  [complete]
  |
  v
RESPONSE
C1  Equilibrium Response Theorem  [complete]
  |
  v
SIGN CONTROL
D1  Inverse Positivity Theorem  [complete]
  |
D2  Mixed-Block Positivity Theorem  [complete]
  |
D3  Response Positivity Theorem  [complete]
  |
  v
ORDERING
E1  Explicit Admissible-Region Theorem  [complete]
  |
E2  Segment / Path Certification Lemma  [complete]
  |
E3  Local Weak Ordering Theorem  [complete]
  |
E4  Strict Ordering Theorem  [not_started]
```

---

## Status vocabulary (use these values)

- `not_started`
- `draft`
- `in_progress`
- `implemented` (code exists, but not yet tied to theorem statement)
- `verified` (scripts/tests run and pass locally)
- `complete` (theorem doc + proof integration + code verification is in place)

---

## Evidence fields (what “status” should correspond to)

For each theorem layer below, track evidence using these fields:

- **Theorem doc**: path to the canonical theorem markdown
- **Proof integrated**: yes/no (or section number)
- **Verification script(s)**: path(s) under `src/network_potential_engine/scripts/`
- **Tests**: path(s) under `tests/`
- **Notes / gaps**: what is missing to move to the next status

### How to run the evidence (commands)

This repository expects modules to be importable from `src/`. When running scripts directly, use `PYTHONPATH=src`:

Policy note:

- Core numeric pipeline code may use SciPy when it materially improves performance or solver robustness.
- Certification scripts/tests should prefer NumPy-only checks when a direct construction exists (e.g. linear TDC equilibrium via `C(\theta) w = \theta`).

As a result, some numeric utilities may require SciPy at runtime, but the certification evidence is designed to remain runnable without SciPy when possible.

```bash
PYTHONPATH=src python3 -m network_potential_engine.scripts.check_A1_tdc_well_posedness
PYTHONPATH=src python3 -m network_potential_engine.scripts.check_A2_tdc_equilibrium_existence
PYTHONPATH=src python3 -m network_potential_engine.scripts.check_A3_tdc_interior_nondegeneracy
PYTHONPATH=src python3 -m network_potential_engine.scripts.check_A3_tdc_equilibrium_regularity
PYTHONPATH=src python3 -m network_potential_engine.scripts.check_C1_tdc_equilibrium_response_identity
```

To run a targeted pytest subset:

```bash
pytest -q tests/test_A1_tdc_derivative_objects_exist.py \
  tests/test_A1_tdc_domain_and_well_definedness.py \
  tests/test_A1_tdc_polynomial_regularity.py \
  tests/test_A2_tdc_equilibrium_existence.py \
  tests/test_A3_tdc_equilibrium_regularity.py \
  tests/test_A3_tdc_interior_nondegeneracy.py \
  tests/test_B1_tdc_hessian_coupling_identity.py \
  tests/test_B2_tdc_tridiagonal_coupling_structure.py \
  tests/test_C1_tdc_equilibrium_response_identity.py
```

---

# A. Foundations

## A1 — Well-Posedness of the Admissible Relational Potential

- **Status**: `complete`
- **Theorem doc**: `docs/theorems/framework/A1_admissible_relational_potential_well_posedness.md`
- **Proof integrated**: yes (`# 8. Proof`)
- **Verification script(s)**: `src/network_potential_engine/scripts/check_A1_tdc_well_posedness.py`
- **Tests**: `tests/test_A1_tdc_*.py`
- **Notes / gaps**:

## A2 — Equilibrium Existence

- **Status**: `complete`
- **Theorem doc**: `docs/theorems/framework/A2_equilibrium_existence.md`
- **Proof integrated**: yes (`# 10. Proof`)
- **Verification script(s)**: `src/network_potential_engine/scripts/check_A2_tdc_equilibrium_existence.py`
- **Tests**: `tests/test_A2_tdc_equilibrium_existence.py`
- **Notes / gaps**: 

## A3 — Interior Nondegeneracy / Strict Local Maximum

- **Status**: `complete`
- **Theorem doc**: `docs/theorems/framework/A3_interior_nondegeneracy.md`
- **Proof integrated**: yes (`# 9. Proof`)
- **Verification script(s)**:
  - `src/network_potential_engine/scripts/check_A3_tdc_interior_nondegeneracy.py`
  - `src/network_potential_engine/scripts/check_A3_tdc_equilibrium_regularity.py`
- **Tests**: `tests/test_A3_tdc_*.py`
- **Notes / gaps**: 

---

# B. Operator generation

## B1 — Hessian–Coupling Theorem

- **Status**: `complete`
- **Theorem doc**: `docs/theorems/framework/B1_hessian_coupling_theorem.md`
- **Proof integrated**: yes (`# 5. Proof`)
- **Verification script(s)**: `src/network_potential_engine/scripts/check_B1_tdc_hessian_coupling_identity.py`
- **Tests**:
  - `tests/test_operators.py` (bootstrap case: `C + H = 0`)
  - `tests/test_B1_tdc_hessian_coupling_identity.py` (TDC case: `C + H = 0`)
- **Notes / gaps**:
  - Code evidence already exists for the core identity:
    - `src/network_potential_engine/symbolic/operators.py` (`coupling_operator_from_hessian`)
    - `tests/test_operators.py` (`test_coupling_operator_is_negative_hessian`)
  - Optional: add a TDC-specific B1 test if you want redundancy beyond the bootstrap operator test.

## B2 — Locality / Incident Structure Inheritance

- **Status**: `complete`
- **Theorem dev brief**: `docs/development_plan/chatgpt_theorem_B2_locality_incident_structure_inheritance.md`
- **Theorem doc**: `docs/theorems/framework/B2_locality_incident_structure_inheritance.md`
- **Proof integrated**: yes (`# 4. Proof`)
- **Verification script(s)**: `src/network_potential_engine/scripts/check_B2_tdc_tridiagonal_coupling_structure.py`
- **Tests**:
  - `tests/test_B2_tdc_tridiagonal_coupling_structure.py` (TDC case: tridiagonal locality)
- **Notes / gaps**:

---

# C. Response identity

## C1 — Equilibrium Response Theorem

- **Status**: `complete`
- **Theorem doc**: `docs/theorems/framework/C1_equilibrium_response_theorem.md`
- **Proof integrated**: yes (`# 4. Proof`)
- **Verification script(s)**:
  - `src/network_potential_engine/scripts/check_C1_tdc_equilibrium_response_identity.py`
  - `src/network_potential_engine/scripts/check_A3_tdc_equilibrium_regularity.py` (historical / overlapping evidence)
- **Tests**:
  - `tests/test_C1_tdc_equilibrium_response_identity.py`
- **Notes / gaps**:

---

# D. Sign-controlled response

## D1 — Inverse Positivity Theorem

- **Status**: `complete`
- **Theorem doc**: `docs/theorems/framework/D1_inverse_positivity_theorem.md`
- **Proof integrated**: yes (`# 5. Proof`)
- **Verification script(s)**:
  - `src/network_potential_engine/scripts/check_D1_tdc_inverse_positivity.py`
  - `src/network_potential_engine/scripts/check_tdc_bounds.py`
- **Tests**:
  - `tests/test_D1_tdc_inverse_positivity.py`
  - `tests/test_tdc_bounds.py`
- **Notes / gaps**:
  - TDC-specific inverse-positivity *sufficient condition* is implemented via curvature margins and analytic bounds (M-matrix style mechanism).

## D2 — Mixed-Block Positivity Theorem

- **Status**: `complete`
- **Theorem doc**: `docs/theorems/framework/D2_mixed_block_positivity_theorem.md`
- **Proof integrated**: yes (`# 3. Proof`)
- **Verification script(s)**:
  - `src/network_potential_engine/scripts/check_D2_tdc_mixed_block_positivity.py`
  - `src/network_potential_engine/scripts/check_tdc_conditions.py`
  - `src/network_potential_engine/scripts/check_tdc_conditions_scan.py`
- **Tests**:
  - `tests/test_D2_tdc_mixed_block_positivity.py`
  - `tests/test_tdc_conditions.py`
  - `tests/test_tdc_conditions_scan.py`
- **Notes / gaps**:
  - TDC-specific mixed-block positivity is implemented as the sufficient condition `1 - \alpha w_i^*(\theta) >= 0` (checked directly from the computed equilibrium).
  - Framework-level D2 is still missing a canonical theorem doc + proof phrased in terms of the general mixed derivative block object `H_{w\theta}`.

## D3 — Response Positivity Theorem

- **Status**: `complete`
- **Theorem doc**: `docs/theorems/framework/D3_response_positivity_theorem.md`
- **Proof integrated**: yes (`# 4. Proof`)
- **Verification script(s)**:
  - `src/network_potential_engine/scripts/check_D3_tdc_response_positivity.py`
  - `src/network_potential_engine/scripts/check_tdc_chain_witness.py`
  - `src/network_potential_engine/scripts/check_tdc_path_summary.py`
- **Tests**:
  - `tests/test_D3_tdc_response_positivity.py`
  - `tests/test_tdc_local_theorem.py`
  - `tests/test_tdc_conditions_scan.py`
  - `tests/test_tdc_region.py`
  - `tests/test_tdc_segment.py`
- **Notes / gaps**:
  - TDC-specific response positivity is certified through combined sufficient-condition checks along scans/chains (conditions + region + segment certificates).

---

# E. Ordering package

## E1 — Explicit Admissible-Region Theorem

- **Status**: `complete`
- **Theorem doc**: `docs/theorems/framework/E1_explicit_admissible_region_theorem.md`
- **Proof integrated**: yes (`# 4. Proof`)
- **Verification script(s)**:
  - `src/network_potential_engine/scripts/check_E1_tdc_region.py`
  - `src/network_potential_engine/scripts/check_tdc_region.py`
  - `src/network_potential_engine/scripts/check_tdc_region_scan.py`
- **Tests**:
  - `tests/test_E1_tdc_region.py`
  - `tests/test_tdc_region.py`
  - `tests/test_tdc_region_scan.py`
- **Notes / gaps**:
  - E1 is implemented and tested for the TDC model via `network_potential_engine.theorem.tdc_region` (the theorem-ready region membership check).

## E2 — Segment / Path Certification Lemma

- **Status**: `complete`
- **Theorem doc**: `docs/theorems/framework/E2_segment_path_certification_lemma.md`
- **Proof integrated**: yes (`# 3. Proof`)
- **Verification script(s)**:
  - `src/network_potential_engine/scripts/check_E2_tdc_segment_certificate.py`
  - `src/network_potential_engine/scripts/check_tdc_segment.py`
  - `src/network_potential_engine/scripts/check_tdc_local_theorem.py`
- **Tests**:
  - `tests/test_E2_tdc_segment_certificate.py`
  - `tests/test_tdc_segment.py`
  - `tests/test_tdc_local_theorem.py`
- **Notes / gaps**:
  - E2 is implemented and tested for TDC via `network_potential_engine.theorem.tdc_segment` (rigorous segment certificate).

## E3 — Local Weak Ordering Theorem

- **Status**: `complete`
- **Theorem doc**: `docs/theorems/framework/E3_local_weak_ordering_theorem.md`
- **Proof integrated**: yes (`# 4. Proof`)
- **Verification script(s)**:
  - `src/network_potential_engine/scripts/check_E3_tdc_local_weak_ordering.py`
  - `src/network_potential_engine/scripts/check_tdc_local_theorem.py`
  - `src/network_potential_engine/scripts/check_tdc_chain_witness.py`
  - `src/network_potential_engine/scripts/check_tdc_path_summary.py`
- **Tests**:
  - `tests/test_E3_tdc_local_weak_ordering.py`
  - `tests/test_tdc_local_theorem.py`
  - `tests/test_tdc_region.py`
  - `tests/test_tdc_segment.py`
- **Notes / gaps**:
  - This is certified at the TDC model level; E3 has also been extracted as a standalone framework theorem.

## E4 — Strict Ordering Theorem

- **Status**: `not_started`
- **Theorem doc**: 
- **Proof integrated**: 
- **Verification script(s)**: 
- **Tests**: 
- **Notes / gaps**: 

---

# F–I. Later packages (placeholders)

Set these to `not_started` until the A–E spine is fully certified.

- **F (structural differentiation)**: `not_started`
- **G (genericity)**: `not_started`
- **H (scarcity / constrained geometry)**: `not_started`
- **I (propagation / opportunity / dynamics / topology)**: `not_started`
