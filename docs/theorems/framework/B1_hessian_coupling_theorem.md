# B1 — Hessian–Coupling Theorem

## Purpose

This theorem exports the **coupling operator** as the canonical negative-Hessian object associated with a relational potential.

It exists to prevent notation drift and to make the operator chain auditable for the downstream response and ordering theorems.

No claim is made here about invertibility, positivity, M-matrix structure, or ordering consequences.

Role in framework: B1 defines the Hessian and coupling operator objects used throughout the structural curvature layer. In particular, S1 uses B1 to formulate the Z-matrix sign condition for `C(w, θ)`, S2 uses B1 to define the row-dominance quantities for `C(w, θ)`, and S3 uses B1 to formulate nonsingular M-matrix structure for `C(w, θ)`.

------------------------------------------------------------------------

# 1. Setup

Let Φ(w, θ) be a relational potential satisfying the regularity assumptions of

A1 — Admissible Relational Potential Well-Posedness.

In particular, assume Φ ∈ C²_w(Ω_Φ), so that second derivatives with respect to the state variable w exist on Ω_Φ.

Let Ω_Φ ⊆ W × Θ denote the admissible potential domain on which Φ is defined.

------------------------------------------------------------------------

# 2. Hessian and coupling operator

Define the state Hessian

H(w, θ) = ∇²_ww Φ(w, θ)

and define the coupling operator

C(w, θ) = −H(w, θ).

In later layers of the theorem stack, one often works with the coupling operator evaluated at an equilibrium branch w*(θ). This theorem does not assume such a branch exists.

------------------------------------------------------------------------

# 3. Theorem statement

Then:

1. The Hessian H(w, θ) exists for all (w, θ) ∈ Ω_Φ.
2. The coupling operator C(w, θ) is well-defined on Ω_Φ.
3. If H(w, θ) is symmetric, then C(w, θ) is symmetric.

No claim is made about invertibility or sign structure of C.

------------------------------------------------------------------------

# 4. Notational scope (C(w, θ) versus C(θ))

- In general, the canonical coupling operator is the two-variable object C(w, θ) defined above.
- If later documents write C(θ), this must be understood as either:
  1. a model-specific simplification in which H (hence C) is independent of w, or
  2. shorthand for evaluation at an equilibrium branch w*(θ), i.e. C(θ) := C(w*(θ), θ), when w*(θ) is licensed by later theorems.

------------------------------------------------------------------------

# 5. Proof

1. Since Φ ∈ C²_w(Ω_Φ), the matrix of second partial derivatives with respect to w exists at every (w, θ) ∈ Ω_Φ. Therefore H(w, θ) exists on Ω_Φ.
2. By definition C(w, θ) := −H(w, θ). Since H exists on Ω_Φ, the coupling operator C is well-defined on Ω_Φ.
3. If H(w, θ) is symmetric, then

   C(w, θ)^T
   = (−H(w, θ))^T
   = −H(w, θ)^T
   = −H(w, θ)
   = C(w, θ),

   so C(w, θ) is symmetric.

------------------------------------------------------------------------

# 6. Computational evidence (supporting)

The codebase already includes a symbolic operator definition and tests that certify the identity C = −H in example models:

- `src/network_potential_engine/symbolic/operators.py` (`coupling_operator_from_hessian`)
- `tests/test_operators.py` (`test_coupling_operator_is_negative_hessian`)
- `tests/test_B1_tdc_hessian_coupling_identity.py` (`test_tdc_coupling_operator_is_negative_hessian`)
