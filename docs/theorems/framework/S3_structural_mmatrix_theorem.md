# S3 — Structural M-Matrix Theorem

## Purpose

This theorem exports a **nonsingular M-matrix** condition for the canonical coupling operator.

It is the completion of the structural curvature layer:

- S1 certifies Z-matrix sign structure of `C(w, θ)`.
- S2 certifies strict row diagonal dominance of `C(w, θ)` on a certified region.
- S3 combines these with classical matrix theory to conclude nonsingular M-matrix structure and hence inverse nonnegativity.

This theorem is the operator-theoretic bridge that justifies the framework use of inverse-positivity claims downstream (D1).

------------------------------------------------------------------------

# 1. Setup and canonical objects

All canonical objects and notation are as defined in:

- `docs/foundations/core_objects.md`

Let `Φ(w, θ)` be a relational potential satisfying the regularity assumptions of:

- A1 — Admissible Relational Potential Well-Posedness.

Let `Ω_Φ ⊆ W × Θ` denote the admissible potential domain.

Assume `Φ ∈ C²_w(Ω_Φ)` so that the Hessian exists on `Ω_Φ`.

------------------------------------------------------------------------

# 2. Hessian and coupling operator

Define the Hessian (B1):

`H(w, θ) := ∇²_{ww} Φ(w, θ)`.

Define the coupling operator (B1):

`C(w, θ) := −H(w, θ)`.

------------------------------------------------------------------------

# 3. Certified region and admissibility scope

Fix a certified region `Ω_{S3} ⊆ Ω_Φ`.

In the initial framework closure, take `Ω_{S3} := Ω_{S2}` where `Ω_{S2}` is the certified region on which S2’s strict diagonal dominance margin is certified.

------------------------------------------------------------------------

# 4. Theorem statement (nonsingular M-matrix conclusion)

Assume the following on `Ω_{S3}`:

## 4.1 Z-matrix sign structure (from S1)

Assume S1 holds for `Φ` so that `C(w, θ)` is a Z-matrix on `Ω_{S3}`:

- for all `i ≠ j`, `C_{ij}(w, θ) ≤ 0`.

## 4.2 Strict row diagonal dominance (from S2)

Assume S2 holds for `Φ` on `Ω_{S3}` so that `C(w, θ)` is strictly diagonally dominant by rows:

- for each `i`, `C_{ii}(w, θ) > Σ_{j≠i} |C_{ij}(w, θ)|`.

## 4.3 Conclusion

Then for every `(w, θ) ∈ Ω_{S3}`:

1. `C(w, θ)` is nonsingular.
2. `C(w, θ)` is a **nonsingular M-matrix**.
3. Consequently, `C(w, θ)^{-1}` exists and is entrywise nonnegative:

   `C(w, θ)^{-1} ≥ 0`.

------------------------------------------------------------------------

# 5. Proof skeleton

Fix `(w, θ) ∈ Ω_{S3}`.

1. **Z-matrix property**

   By S1, `C(w, θ)` is a Z-matrix.

2. **Strict diagonal dominance**

   By S2, `C(w, θ)` is strictly diagonally dominant by rows.

3. **Nonsingularity**

   By a classical result (Levy–Desplanques), strict diagonal dominance implies nonsingularity.

4. **M-matrix conclusion**

   By a classical sufficient condition: a strictly diagonally dominant Z-matrix is a nonsingular M-matrix.

5. **Inverse nonnegativity**

   Since `C(w, θ)` is a nonsingular M-matrix, standard M-matrix theory implies `C(w, θ)^{-1}` exists and is entrywise nonnegative.

------------------------------------------------------------------------

# 6. Explicit dependency audit

This theorem depends only on:

- A1 — Admissible Relational Potential Well-Posedness (licenses `Φ ∈ C²_w(Ω_Φ)` and existence of Hessian entries)
- B1 — Hessian–Coupling Theorem (defines `H(w, θ)` and `C(w, θ) = −H(w, θ)`)
- S1 — Structural Z-Matrix Theorem (`docs/theorems/framework/S1_structural_zmatrix_theorem.md`)
- S2 — Structural Diagonal Dominance Theorem (`docs/theorems/framework/S2_structural_diagonal_dominance_theorem.md`)

This theorem does not depend on equilibrium response theory, inverse-positivity theorems, or ordering theorems.

------------------------------------------------------------------------

# 7. Computational evidence (supporting)

- S1 evidence pipeline:
  - `src/network_potential_engine/scripts/check_S1_motif_cross_partials.py`
  - `docs/artifacts/S1/tdc_motif_cross_partials.json`
  - `tests/test_S1_motif_cross_partials_tdc.py`

- S2 evidence pipeline:
  - `src/network_potential_engine/scripts/check_S2_row_dominance_tdc.py`
  - `docs/artifacts/S2/tdc_row_dominance_report.json`
  - `tests/test_S2_row_dominance_tdc.py`

- S3 Phase-1 TDC evidence pipeline:
 
 - `src/network_potential_engine/scripts/check_S3_mmatrix_tdc.py`
 - `docs/artifacts/S3/tdc_mmatrix_report.json`
 - `tests/test_S3_mmatrix_tdc.py`

------------------------------------------------------------------------

# 8. Remaining gap to full framework certification

1. Record an explicit citation target (or short embedded lemma statement) for the classical matrix results used in Steps 3–5.
2. Provide a framework-wide definition of `Ω_{S3}` as `Ω_{S2}` for the initial closure.
