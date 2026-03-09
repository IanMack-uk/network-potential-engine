# S2 — Structural Diagonal Dominance Theorem

## Purpose

This theorem exports a **row-wise diagonal dominance condition** for the canonical coupling operator.

It is the magnitude-layer complement to S1:

- S1 certifies that `C(w, θ)` is a Z-matrix (off-diagonal entries are nonpositive).
- S2 certifies sufficient conditions under which `C(w, θ)` is **strictly diagonally dominant by rows** on a certified region.

No claim is made here about nonsingular M-matrix structure (S3).

------------------------------------------------------------------------

# 1. Setup and canonical objects

All canonical objects and notation are as defined in:

- `docs/foundations/core_objects.md`

Let `Φ(w, θ)` be a relational potential satisfying the regularity assumptions of:

- A1 — Admissible Relational Potential Well-Posedness.

Let `Ω_Φ ⊆ W × Θ` denote the admissible potential domain on which `Φ` is defined.

Assume `Φ ∈ C²_w(Ω_Φ)` so that the Hessian exists on `Ω_Φ`.

------------------------------------------------------------------------

# 2. Hessian and coupling operator

Define the Hessian (B1):

`H(w, θ) := ∇²_{ww} Φ(w, θ)`.

Define the coupling operator (B1):

`C(w, θ) := −H(w, θ)`.

------------------------------------------------------------------------

# 3. Locality / incidence structure

Let `N(i) ⊆ {1, …, n}` denote an index-neighborhood set for each `i` as in B2.

Under the B2 locality hypothesis, the coupling operator inherits sparsity:

- if `j ∉ N(i)`, then `C_{ij}(w, θ) = 0`.

This theorem uses locality only for bounding the **row off-diagonal absolute sum** via an incidence/row-sparsity control.

------------------------------------------------------------------------

# 4. Row dominance quantities

For each row index `i`, define:

- `d_i(w, θ) := C_{ii}(w, θ)`
- `r_i(w, θ) := Σ_{j≠i} |C_{ij}(w, θ)|`
- `m_i(w, θ) := d_i(w, θ) − r_i(w, θ)`

Strict row diagonal dominance is equivalent to:

`m_i(w, θ) > 0` for all `i`.

------------------------------------------------------------------------

# 5. Theorem statement (margin construction)

Assume the following hypotheses on a certified region `Ω_{S2} ⊆ Ω_Φ`:

In framework instantiations, the diagonal lower bounds are expected to be derived from admissible Class A curvature contributions, while the row-sum bounds are expected to be derived from magnitude bounds on admissible Class B/C terms together with locality-based incidence bookkeeping.

In the current repository closure, a sufficient-form set of magnitude admissibility conditions (including a B2-style incidence bookkeeping route) is specified in:

- `docs/foundations/admissible_motif_taxonomy.md`.

## 5.1 Z-matrix sign structure (from S1)

Assume S1 holds for `Φ` so that `C(w, θ)` is a Z-matrix on `Ω_{S2}`:

- for all `i ≠ j`, `C_{ij}(w, θ) ≤ 0`.

This hypothesis is not used to *define* `r_i`, but it may be used to simplify bounding arguments.

## 5.2 Diagonal lower bounds

Assume the potential admits a Class A/B/C decomposition per the admissible potential grammar.

Assume that for each coordinate `i`, the total Class A diagonal curvature contribution admits a certified lower bound on `Ω_{S2}`.

Concretely, let `E(i)` denote the set of edge-local terms whose state coordinate is `w_i`.

For each `e ∈ E(i)`, define `λ_e(w, θ) := −∂²φ_e/(∂w_i²)`.

Assume there exist certified lower bounds `\underline{λ}_e(w, θ)` such that on `Ω_{S2}`:

`λ_e(w, θ) ≥ \underline{λ}_e(w, θ) ≥ 0`.

Define the Class A diagonal lower bound:

`\underline{d}_i(w, θ) := Σ_{e ∈ E(i)} \underline{λ}_e(w, θ)`.

## 5.3 Off-diagonal row-sum upper bounds

Assume that for each off-diagonal entry `C_{ij}(w, θ)` that can be nonzero on `Ω_{S2}`, there exists a certified upper bound on its magnitude.

Concretely, assume there exist certified functions `\overline{β}_{ij}(w, θ) ≥ 0` such that on `Ω_{S2}`:

`|C_{ij}(w, θ)| ≤ \overline{β}_{ij}(w, θ)`.

Assume also that locality neighborhoods `N(i)` are provided as in B2 such that `C_{ij}(w, θ) = 0` on `Ω_{S2}` whenever `j ∉ N(i)`.

Define the row-sum upper bound:

`\overline{r}_i(w, θ) := Σ_{j ∈ N(i) \ {i}} \overline{β}_{ij}(w, θ)`.

## 5.4 Strict margin

Assume there exists a certified function `m(w, θ) > 0` on `Ω_{S2}` such that for all indices `i` and all `(w, θ) ∈ Ω_{S2}`:

`\underline{d}_i(w, θ) − \overline{r}_i(w, θ) ≥ m(w, θ)`.

Then for all indices `i` and all `(w, θ) ∈ Ω_{S2}`:

`m_i(w, θ) = d_i(w, θ) − r_i(w, θ) ≥ \underline{d}_i(w, θ) − \overline{r}_i(w, θ) ≥ m(w, θ) > 0`.

Therefore `C(w, θ)` is **strictly diagonally dominant by rows** on `Ω_{S2}`.

------------------------------------------------------------------------

# 6. Proof skeleton

1. **Lower bound the diagonal**

   By hypothesis, `d_i(w, θ) ≥ \underline{d}_i(w, θ)` on `Ω_{S2}`.

2. **Upper bound the off-diagonal absolute row sum**

   By hypothesis, `r_i(w, θ) ≤ \overline{r}_i(w, θ)` on `Ω_{S2}`.

3. **Construct the margin**

   Combining the above yields:

   `m_i(w, θ) = d_i(w, θ) − r_i(w, θ) ≥ \underline{d}_i(w, θ) − \overline{r}_i(w, θ) ≥ m(w, θ) > 0`.

4. **Strict diagonal dominance**

   Since `m_i(w, θ) > 0` for all rows `i` on `Ω_{S2}`, the coupling operator is strictly diagonally dominant by rows.

------------------------------------------------------------------------

# 7. Explicit dependency audit

This theorem depends only on:

- A1 — Admissible Relational Potential Well-Posedness (licenses `Φ ∈ C²_w(Ω_Φ)` and existence of Hessian entries)
- B1 — Hessian–Coupling Theorem (defines `H(w, θ)` and `C(w, θ) = −H(w, θ)`)
- B2 — Locality / Incident Structure Inheritance (used as an admissible route to row-sum / incidence control)
- S1 — Structural Z-Matrix Theorem (optional for bounding simplifications, but the Z-matrix sign structure is part of the intended S1–S2–S3 chain)

This theorem does not depend on equilibrium response theory, inverse positivity theorems, or ordering theorems.

------------------------------------------------------------------------

# 8. Computational evidence (supporting)

The repository contains a TDC Phase-1 evidence pipeline that computes row-wise diagonal dominance margins and writes an auditable JSON report:

- Check script:
  - `src/network_potential_engine/scripts/check_S2_row_dominance_tdc.py`
  - artifact output:
    - `docs/artifacts/S2/tdc_row_dominance_report.json`

- Pytest regression coverage:
  - `tests/test_S2_row_dominance_tdc.py`

These artifacts provide supporting evidence for the intended S2 magnitude layer and serve as a concrete instantiation target for the framework theorem.

------------------------------------------------------------------------

# 9. Remaining gap to full framework certification

The framework now specifies a sufficient-form magnitude admissibility layer for S2 (in the admissible motif taxonomy) that provides an explicit, auditable route to constructing `\underline{d}_i` and `\overline{r}_i` on a certified region `Ω_{S2}` for the initial admitted closed-form families.

Remaining work for broader framework closure is to extend this sufficient-form magnitude admissibility layer beyond the initial closed-form families and to standardise the incidence bookkeeping for general motif inventories.
