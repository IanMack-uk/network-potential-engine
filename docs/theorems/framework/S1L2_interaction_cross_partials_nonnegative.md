# S1L2 — Pairwise Interaction Motifs Have Nonnegative Off-Diagonal Cross-Partials

## Statement

Let `Φ(w, θ)` be a relational potential defined on `Ω_Φ ⊆ W × Θ`.

Let `ψ(w_S, θ)` be a motif-local interaction term supported on a finite index set `S ⊆ {1, …, n}`.

Assume that `ψ` admits a finite pairwise decomposition of the form:

`ψ(w_S, θ) = Σ_{(i,j) ∈ P} g_{ij}(w_i, w_j, θ)`,

where:

- `P` is a finite set of unordered index pairs with `{i, j} ⊆ S`,
- each `g_{ij}` is `C²` with respect to `(w_i, w_j)` on `Ω_Φ`, and satisfies:

`∂²g_{ij}/(∂w_i ∂w_j) ≥ 0`

on `Ω_Φ`.

Then for any pair of distinct indices `a ≠ b`:

- if `{a, b} ⊆ S`, then `∂²ψ/(∂w_a ∂w_b) ≥ 0` on `Ω_Φ`,
- otherwise `∂²ψ/(∂w_a ∂w_b) = 0`.

------------------------------------------------------------------------

## Proof

Fix distinct indices `a ≠ b`.

By the assumed pairwise decomposition,

`∂²ψ/(∂w_a ∂w_b) = Σ_{(i,j) ∈ P} ∂²g_{ij}/(∂w_a ∂w_b)`.

For any pair `(i,j) ∈ P`, the function `g_{ij}` depends only on `(w_i, w_j)` (and `θ`). Therefore:

- if `{a, b} ≠ {i, j}`, then at least one of `w_a` or `w_b` is not among the variables of `g_{ij}`, hence `∂²g_{ij}/(∂w_a ∂w_b) = 0`,
- if `{a, b} = {i, j}`, then `∂²g_{ij}/(∂w_a ∂w_b) = ∂²g_{ab}/(∂w_a ∂w_b) ≥ 0` by hypothesis.

Thus every summand in the expression for `∂²ψ/(∂w_a ∂w_b)` is nonnegative. Hence:

`∂²ψ/(∂w_a ∂w_b) ≥ 0`.

If `{a, b} ⊄ S`, then `ψ` does not depend on at least one of `w_a` or `w_b`, so `∂²ψ/(∂w_a ∂w_b) = 0`.

------------------------------------------------------------------------

## Role in S1

This lemma provides a sufficient-form certification route for Class B (interaction) motifs: interaction terms built as finite sums of pairwise components with nonnegative mixed partial derivatives contribute nonnegative off-diagonal entries to the Hessian `H(w, θ)` and hence nonpositive off-diagonal entries to the coupling operator `C(w, θ) = −H(w, θ)`.
