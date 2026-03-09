# S1L1 — Edge-Local Terms Have Zero Off-Diagonal Cross-Partials

## Statement

Let `Φ(w, θ)` be a relational potential defined on `Ω_Φ ⊆ W × Θ`.

Let `φ_e(w_e, θ)` be an edge-local term depending on a single state coordinate `w_e`.

Then for every pair of distinct indices `i ≠ j` and every `(w, θ) ∈ Ω_Φ`:

`∂²φ_e/(∂w_i ∂w_j) = 0`.

Equivalently, the Hessian of `φ_e` with respect to `w` is diagonal.

------------------------------------------------------------------------

## Proof

Fix distinct indices `i ≠ j`.

Because `φ_e` depends only on the single coordinate `w_e`, at least one of the variables `w_i` or `w_j` does not appear in `φ_e`.

Therefore the corresponding first partial derivative is identically zero:

- either `∂φ_e/∂w_i = 0`, or `∂φ_e/∂w_j = 0`.

Differentiating once more with respect to the other variable yields:

`∂²φ_e/(∂w_i ∂w_j) = 0`.

------------------------------------------------------------------------

## Role in S1

This lemma certifies that edge-local terms contribute only to the diagonal of `H(w, θ) = ∇²_{ww}Φ(w, θ)`, and hence do not affect the off-diagonal sign constraints required to show that `C(w, θ) = −H(w, θ)` is a Z-matrix.
