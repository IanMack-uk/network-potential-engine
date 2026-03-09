# S1 — Motif Sign Lemmas (Index)

## Purpose

This document records the **motif-class sign lemmas** required to certify:

- S1 — Structural Z-Matrix Theorem (`docs/theorems/framework/S1_structural_zmatrix_theorem.md`).

This document serves as the canonical index for the certified motif sign lemmas used by S1.

The admissible motif classes and the associated sign-lemma targets are specified in:

- `docs/foundations/admissible_motif_taxonomy.md`.

------------------------------------------------------------------------

# 1. Canonical setup

Let `Φ(w, θ)` be a relational potential defined on `Ω_Φ ⊆ W × Θ`.

Assume `Φ ∈ C²_w(Ω_Φ)` (A1), so that the Hessian exists:

- `H(w, θ) := ∇²_{ww} Φ(w, θ)`.

Define the coupling operator (B1):

- `C(w, θ) := −H(w, θ)`.

Let a motif-local term have the form `ψ(w_S, θ)` for some finite index subset `S ⊆ {1, …, n}`.

------------------------------------------------------------------------

# 2. Lemma L1 — Edge-local terms have zero off-diagonal cross-partials

This lemma is certified as:

- `docs/theorems/framework/S1L1_edge_local_offdiagonal_zero.md`.

------------------------------------------------------------------------

# 3. Lemma L2 — Interaction motifs have nonnegative off-diagonal cross-partials

This lemma is certified as:

- `docs/theorems/framework/S1L2_interaction_cross_partials_nonnegative.md`.

------------------------------------------------------------------------

# 4. Lemma L3 — Closure motifs have nonnegative off-diagonal cross-partials

This lemma is certified as:

- `docs/theorems/framework/S1L3_closure_cross_partials_nonnegative.md`.

------------------------------------------------------------------------

# 5. Integration into S1

Given:

- a decomposition `Φ(w, θ) = Σ_{e ∈ E} φ_e(w_e, θ) + Σ_{m ∈ M} ψ_m(w_{S_m}, θ)`, and
- Lemma L1 for the edge-local class, and
- Lemma L2 for the interaction class, and
- Lemma L3 for the closure class,

the S1 off-diagonal sign conclusion follows by termwise differentiation and summation:

- for `i ≠ j`, `H_{ij}(w, θ) ≥ 0`, hence `C_{ij}(w, θ) ≤ 0`.

------------------------------------------------------------------------

# 6. Remaining gap

The remaining gap for S1 certification is not at the lemma level; it is at the framework specification level:

1. Maintain an authoritative admissible taxonomy and admissible potential grammar.
2. Ensure that model instantiations decompose into the admitted term families.
