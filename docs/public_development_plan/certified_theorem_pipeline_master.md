# Certified Theorem Pipeline for the Network Potential Framework --- Version 3

## Purpose of this update

This document extends the certified theorem pipeline to **internally
close the framework mathematically**. All theorems A1--E3 are now
implemented and verified in the repository pipeline, but a
**framework-level structural theorem** is still needed to justify the
M-matrix property used in D1 generically.

The TDC model proves this property explicitly. The framework must now
extract that reasoning into a **native structural theorem**.

The new structural closure layer sits between **B2 and D1**.

------------------------------------------------------------------------

# Updated Dependency Graph (at a glance)

FOUNDATIONS A1 Well-posedness \| A2 Equilibrium existence \| A3a Equilibrium regularity \| A3b Interior nondegeneracy

OPERATOR GENERATION B1 Hessian–Coupling Theorem \| B2 Locality / Incident Structure Inheritance

STRUCTURAL CURVATURE (NEW) S1 Structural Z-Matrix Theorem \| S2 Structural Diagonal Dominance Theorem \| S3 Structural M-Matrix Theorem

RESPONSE C1 Equilibrium Response Theorem

SIGN CONTROL D1 Inverse positivity \| D2 Mixed-block positivity \| D3 Response positivity

ORDERING E1 Explicit admissible region \| E2 Segment certification \| E3 Local weak ordering \| E4 Strict ordering

------------------------------------------------------------------------

# Role of the Structural Curvature Layer (S1–S3)

The S-layer answers the question:

Why does the relational potential produce an operator with the
properties required for inverse positivity?

The answer is:

1.  motif structure induces cross-partial sign patterns
2.  cohesion curvature dominates interaction curvature
3.  locality bounds off-diagonal row sums

Together these produce an M-matrix coupling operator.

The intended structural dependency chain is:

`S1 → S2 → S3 → D1`.

------------------------------------------------------------------------

# Structural Closure Layer (NEW)

## Theorem S1 — Structural Z-Matrix Theorem

### Goal

Prove that the equilibrium coupling operator

C(θ) = -H(θ)

is a **Z-matrix**, meaning

C_ij ≤ 0 for i ≠ j.

### Motivation

Inverse positivity (D1) relies on the coupling operator being a
**nonsingular M-matrix**. A sufficient condition for this is:

1.  C is a Z-matrix
2.  C is strictly diagonally dominant

TDC proves the Z-matrix property directly because the off-diagonal
entries are −c.

The framework must now prove this property **for admissible relational
potentials**.

### Required work

Status: complete

Certified artifacts:

- Foundations specifications:
  - `docs/foundations/admissible_motif_taxonomy.md`
  - `docs/foundations/admissible_potential_grammar.md`
- Certified theorem and lemmas:
  - `docs/theorems/framework/S1_structural_zmatrix_theorem.md`
  - `docs/theorems/framework/S1_motif_sign_lemmas.md`
  - `docs/theorems/framework/S1L1_edge_local_offdiagonal_zero.md`
  - `docs/theorems/framework/S1L2_interaction_cross_partials_nonnegative.md`
  - `docs/theorems/framework/S1L3_closure_cross_partials_nonnegative.md`
- Supporting evidence pipeline:
  - script: `src/network_potential_engine/scripts/check_S1_motif_cross_partials.py`
  - artifact: `docs/artifacts/S1/tdc_motif_cross_partials.json`
  - tests: `tests/test_S1_motif_cross_partials_tdc.py`

------------------------------------------------------------------------

## Theorem S2 — Structural Diagonal Dominance Theorem

### Goal

Prove a **framework-level lower bound on diagonal curvature** such that

C_ii \> Σ\_{j ≠ i} \|C_ij\|

holds on an admissible region.

### Motivation

This condition, together with the Z-matrix property, guarantees that

C(θ) is a nonsingular M-matrix.

### Required work

1.  Express diagonal curvature in terms of cohesion components.
2.  Bound off-diagonal interactions using the locality theorem B2.
3.  Derive row-sum bounds using motif interaction structure.
4.  Define a curvature margin function analogous to the TDC margin m(θ).

Current status:

- Certified theorem doc:
  - `docs/theorems/framework/S2_structural_diagonal_dominance_theorem.md`
- TDC Phase-1 evidence pipeline:
  - script: `src/network_potential_engine/scripts/check_S2_row_dominance_tdc.py`
  - artifact: `docs/artifacts/S2/tdc_row_dominance_report.json`
  - tests: `tests/test_S2_row_dominance_tdc.py`

------------------------------------------------------------------------

## Theorem S3 — Structural M-Matrix Theorem

### Goal

Combine S1 and S2 to prove:

If the Network Potential satisfies the structural curvature conditions,
then the equilibrium coupling operator C(θ) is a **nonsingular
M-matrix**.

### Consequence

This theorem **justifies D1 at the framework level**.

It closes the logical gap between:

B-layer operator structure and D-layer inverse positivity.

Current status:

- Certified theorem doc:
  - `docs/theorems/framework/S3_structural_mmatrix_theorem.md`
- TDC Phase-1 evidence pipeline:
  - script: `src/network_potential_engine/scripts/check_S3_mmatrix_tdc.py`
  - artifact: `docs/artifacts/S3/tdc_mmatrix_report.json`
  - tests: `tests/test_S3_mmatrix_tdc.py`

------------------------------------------------------------------------

# Updated Certified Pipeline

A1 Well-posedness\
A2 Equilibrium existence\
A3a Equilibrium regularity\
A3b Interior nondegeneracy

B1 Hessian–Coupling Theorem\
B2 Locality / Incident Structure Inheritance

S1 Structural Z-Matrix Theorem (NEW)\
S2 Structural Diagonal Dominance Theorem (NEW)\
S3 Structural M-Matrix Theorem (NEW)

C1 Equilibrium response identity

D1 Inverse positivity\
D2 Mixed-block positivity\
D3 Response positivity

E1 Admissible region\
E2 Segment certification\
E3 Local weak ordering

E4 Strict ordering

------------------------------------------------------------------------

# Immediate Development Tasks

1.  Record explicit citation targets for the classical matrix results used in S3.
2.  Optionally formalize the initial closure convention `Ω_{S3} := Ω_{S2}` across the workflow/checklists.
3.  Decide whether to stop after S-layer closure and move into D1 cleanup/alignment, or continue S3 documentation polish.
