# B2 — Locality / Incident Structure Inheritance

## Purpose

This theorem exports the fact that a locality hypothesis on the marginal structure of the potential induces a corresponding locality (sparsity) structure in the Hessian and therefore in the coupling operator.

No claim is made here about invertibility, positivity, M-matrix structure, or ordering consequences.

------------------------------------------------------------------------

# 1. Setup

Let Φ(w, θ) be a relational potential satisfying the regularity assumptions of

A1 — Admissible Relational Potential Well-Posedness.

Let Ω_Φ ⊆ W × Θ denote the admissible potential domain on which Φ is defined.

Assume Φ ∈ C²_w(Ω_Φ) so that the Hessian

H(w, θ) = ∇²_ww Φ(w, θ)

exists on Ω_Φ.

------------------------------------------------------------------------

# 2. Locality hypothesis

Fix a collection of index sets N(i) ⊆ {1, …, n}.

Assume that for each i, the i-th marginal incentive

∂Φ/∂w_i

depends on the state vector w only through the coordinates indexed by N(i). Equivalently, for each i and each j ∉ N(i), the partial derivative

∂/∂w_j ( ∂Φ/∂w_i )

vanishes on Ω_Φ.

------------------------------------------------------------------------

# 3. Theorem statement

Assume the locality hypothesis above.

Then for every (w, θ) ∈ Ω_Φ and every pair of indices i, j:

1. If j ∉ N(i), then H_{ij}(w, θ) = 0.
2. The coupling operator C(w, θ) := −H(w, θ) inherits the same sparsity pattern: if j ∉ N(i), then C_{ij}(w, θ) = 0.

------------------------------------------------------------------------

# 4. Proof

Fix i, j.

If j ∉ N(i), then by the locality hypothesis the function ∂Φ/∂w_i does not depend on the variable w_j on Ω_Φ.

Because Φ ∈ C²_w(Ω_Φ), the mixed second derivative exists and equals

H_{ij}(w, θ) = ∂²Φ/(∂w_i ∂w_j) = ∂/∂w_j ( ∂Φ/∂w_i ).

Therefore H_{ij}(w, θ) = 0 for all (w, θ) ∈ Ω_Φ whenever j ∉ N(i).

Finally, by B1, C(w, θ) := −H(w, θ), so C_{ij}(w, θ) = −H_{ij}(w, θ) and the same sparsity pattern holds for C.

------------------------------------------------------------------------

# 5. Notational scope

- This theorem is stated in coordinate form with abstract index-neighborhoods N(i).
- In special models, locality may be described as a banded / incident / graph-neighborhood sparsity pattern.

------------------------------------------------------------------------

# 6. Computational evidence (supporting)

For the TDC model, the coupling operator is tridiagonal (nearest-neighbour locality). This sparsity pattern is verified in:

- `tests/test_B2_tdc_tridiagonal_coupling_structure.py`
