# Admissible Potential Grammar (Framework Specification)

## Purpose

This document specifies the **construction grammar** for framework-admissible relational potentials.

It is a specification layer: it defines the design space of potentials allowed by the framework, rather than asserting a theorem about arbitrary potentials.

The grammar is intended to support certification of:

- S1 — Structural Z-Matrix Theorem (`docs/theorems/framework/S1_structural_zmatrix_theorem.md`)

by ensuring that every framework-admissible potential is built from motif-local term families whose off-diagonal Hessian signs are certified by the S1 motif sign lemmas.

This document is consistent with the canonical objects in:

- `docs/foundations/core_objects.md`.

------------------------------------------------------------------------

# 1. Canonical objects and scope

State and parameter variables:

- `w ∈ ℝⁿ`
- `θ ∈ ℝⁿ`

Relational potential:

- `Φ(w, θ)`

Admissible potential domain:

- `Ω_Φ ⊆ W × Θ`

Regularity scope:

- potentials are required to satisfy `Φ ∈ C²_w(Ω_Φ)` as licensed by A1.

Hessian and coupling operator (B1):

- `H(w, θ) := ∇²_{ww} Φ(w, θ)`
- `C(w, θ) := −H(w, θ)`

------------------------------------------------------------------------

# 2. Motif taxonomy dependency

The admissible motif classes used by this grammar are defined in:

- `docs/foundations/admissible_motif_taxonomy.md`.

The certified sign lemmas for these classes are indexed in:

- `docs/theorems/framework/S1_motif_sign_lemmas.md`.

------------------------------------------------------------------------

# 3. Grammar: admissible construction rules

A relational potential `Φ(w, θ)` is **framework-admissible** if and only if it can be written as a finite sum of local terms of the form:

`Φ(w, θ) = Σ_{e ∈ E} φ_e(w_e, θ) + Σ_{m ∈ M_B} ψ_m^(B)(w_{S_m}, θ) + Σ_{m ∈ M_C} ψ_m^(C)(w_{S_m}, θ)`,

where:

- `E`, `M_B`, and `M_C` are finite index sets,
- each edge-local term `φ_e(w_e, θ)` is Class A admissible (edge-local),
- each interaction motif term `ψ_m^(B)(w_{S_m}, θ)` is Class B admissible (interaction),
- each closure motif term `ψ_m^(C)(w_{S_m}, θ)` is Class C admissible (closure).

No other term forms are admitted by the framework unless the grammar is explicitly extended.

------------------------------------------------------------------------

# 4. Relationship to S1

Under this grammar:

- all edge-local terms satisfy the off-diagonal vanishing property (S1L1),
- all interaction motif terms satisfy the off-diagonal nonnegativity property (S1L2),
- all closure motif terms satisfy the off-diagonal nonnegativity property (S1L3).

Therefore, for any framework-admissible `Φ(w, θ)`, the off-diagonal Hessian entries satisfy:

- for `i ≠ j`, `H_{ij}(w, θ) ≥ 0`, hence `C_{ij}(w, θ) ≤ 0`.

This discharges the decomposition and sign hypotheses needed to apply S1, leaving only regularity and domain assumptions (A1) and the operator definition (B1).

------------------------------------------------------------------------

# 4.1 Relationship to S2/S3

S2 and S3 are magnitude/invertibility layers and require additional admissibility conditions beyond the sign closure guaranteed by this grammar.

In particular, S2 requires explicit magnitude bounds and locality/incidence bookkeeping on a certified region `Ω_{S2} ⊆ Ω_Φ` to construct diagonal-dominance margins. These additional requirements are specified as an S2 magnitude admissibility addendum in:

- `docs/foundations/admissible_motif_taxonomy.md`.

------------------------------------------------------------------------

# 5. Deferred composition layer

Outer scalar compositions (for example `±log(1 + ·)`) are not admitted by this grammar by default.

If a future framework extension intends to admit such compositions, it must do so by:

- explicitly extending the grammar, and
- supplying closure conditions that preserve the S1 off-diagonal sign requirements.
