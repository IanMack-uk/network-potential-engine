# S1L3 — Triadic Closure Product Motifs Have Nonnegative Off-Diagonal Cross-Partials

## Statement

Let `Φ(w, θ)` be a relational potential defined on `Ω_Φ ⊆ W × Θ`.

Let `ψ(w_S, θ)` be a motif-local closure term supported on a finite index set `S ⊆ {1, …, n}`.

Assume that `ψ` admits a finite decomposition into gated triadic product monomials of the form:

`ψ(w_S, θ) = Σ_{α ∈ A} a_α(θ) w_{ij(α)}^{p_α} w_{ik(α)}^{q_α} κ_α`,

where:

- `A` is a finite index set,
- for each `α`, the indices `ij(α)` and `ik(α)` denote two (not necessarily ordered) state coordinates corresponding to edges incident to a common node,
- `a_α(θ) ≥ 0` on `Ω_Φ`,
- `κ_α ≥ 0` is a topology-only gate (for example an adjacency indicator),
- `p_α, q_α > 0`, and each monomial is `C²_w` on `Ω_Φ`.

Then for any pair of distinct indices `a ≠ b`:

- if `{a, b} ⊆ S`, then `∂²ψ/(∂w_a ∂w_b) ≥ 0` on `Ω_Φ`,
- otherwise `∂²ψ/(∂w_a ∂w_b) = 0`.

------------------------------------------------------------------------

## Proof

Fix distinct indices `a ≠ b`.

By the assumed finite decomposition,

`∂²ψ/(∂w_a ∂w_b) = Σ_{α ∈ A} ∂²/(∂w_a ∂w_b) [a_α(θ) w_{ij(α)}^{p_α} w_{ik(α)}^{q_α} κ_α]`.

For a fixed `α`, the term `a_α(θ) w_{ij(α)}^{p_α} w_{ik(α)}^{q_α} κ_α` depends on at most two state coordinates, namely `w_{ij(α)}` and `w_{ik(α)}`.

Therefore:

- if `{a, b}` is not equal to `{ij(α), ik(α)}`, then at least one of `w_a` or `w_b` does not appear in this monomial, hence its mixed second derivative with respect to `(w_a, w_b)` is `0`.

- if `{a, b} = {ij(α), ik(α)}`, then (using `a_α(θ) κ_α ≥ 0` and `p_α, q_α > 0`):

`∂²/(∂w_a ∂w_b) [a_α(θ) w_a^{p_α} w_b^{q_α} κ_α] = a_α(θ) κ_α p_α q_α w_a^{p_α - 1} w_b^{q_α - 1} ≥ 0`

on `Ω_Φ`.

Thus every summand in the expression for `∂²ψ/(∂w_a ∂w_b)` is nonnegative. Hence:

`∂²ψ/(∂w_a ∂w_b) ≥ 0`.

If `{a, b} ⊄ S`, then `ψ` does not depend on at least one of `w_a` or `w_b`, so `∂²ψ/(∂w_a ∂w_b) = 0`.

------------------------------------------------------------------------

## Role in S1

This lemma provides a sufficient-form certification route for Class C (closure) motifs: closure terms built as finite sums of gated monomial products in two incident edge weights, with nonnegative coefficients, contribute nonnegative off-diagonal entries to the Hessian `H(w, θ)` and hence nonpositive off-diagonal entries to the coupling operator `C(w, θ) = −H(w, θ)`.
