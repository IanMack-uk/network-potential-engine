# A3 --- Interior Nondegeneracy

## Purpose

This theorem establishes **interior nondegeneracy** of equilibrium points
for relational potential systems.

It formalizes the condition under which an equilibrium point is a
**strict local maximizer** of the potential in the state variables, and
hence is locally isolated.

------------------------------------------------------------------------

# 1. Setup

Let Φ(w, θ) be a relational potential satisfying the regularity
assumptions of

A1 --- Admissible Relational Potential Well-Posedness.

Let the equilibrium operator be

F(w, θ) = ∇\_w Φ(w, θ)

as defined in `docs/foundations/core_objects.md`.

Fix parameters θ in the admissible domain and consider equilibria w ∈ W
satisfying

F(w, θ) = 0.

------------------------------------------------------------------------

# 2. Interior equilibrium

An equilibrium w is called an **interior equilibrium** if w lies in the
interior of the admissible state set W.

This theorem concerns the local structure of interior equilibria.

------------------------------------------------------------------------

# 3. Hessian and coupling operator

Define the Hessian

H(w, θ) = ∇²_ww Φ(w, θ)

and the coupling operator

C(θ) = −H(w, θ).

No global sign or invertibility property is assumed a priori; such
properties are imposed as hypotheses below.

------------------------------------------------------------------------

# 4. Interior nondegeneracy hypothesis

Let w\*(θ) be an interior equilibrium satisfying

F(w\*(θ), θ) = 0.

Assume the Hessian at the equilibrium is **negative definite**:

xᵀ H(w\*(θ), θ) x < 0  for all nonzero x ∈ ℝⁿ.

Equivalently, assume the coupling operator at the equilibrium is
**positive definite**:

xᵀ C(θ) x > 0  for all nonzero x ∈ ℝⁿ.

------------------------------------------------------------------------

# 5. Consequences

Under the hypothesis above:

1. w\*(θ) is a strict local maximizer of the map w ↦ Φ(w, θ).
2. w\*(θ) is locally isolated as a solution of F(w, θ) = 0.
3. The Hessian H(w\*(θ), θ) is invertible, and therefore C(θ) is
   invertible at the equilibrium.

------------------------------------------------------------------------

# 6. Domain of validity

This theorem holds on the subset of Ω_eq where the interior equilibrium
exists and the Hessian is negative definite.

In the admissibility taxonomy, this corresponds to an interior
nondegeneracy region contained in Ω_eq.

------------------------------------------------------------------------

# 7. TDC model instantiation

For the Theta-Dependent Curvature (TDC) model, the coupling operator is
tridiagonal and satisfies C(θ) = −H(θ).

On parameter regions where C(θ) is positive definite, the Hessian is
negative definite and the interior nondegeneracy hypothesis holds.

------------------------------------------------------------------------

# 8. Conclusion

Interior nondegeneracy (negative definiteness of the Hessian at
equilibrium) implies that equilibria are strict local maximizers and are
locally isolated.

This property is a foundation for differentiability of the equilibrium
branch and the response analysis developed in later theorems.

------------------------------------------------------------------------

# 9. Proof

## 9.1 Strict local maximum

Fix θ and let w\* = w\*(θ) be an interior equilibrium.

Since Φ ∈ C²_w(Ω_Φ), the function w ↦ Φ(w, θ) is twice continuously
differentiable in a neighborhood of w\*.

At equilibrium, ∇\_w Φ(w\*, θ) = F(w\*, θ) = 0.

Assume the Hessian H(w\*, θ) is negative definite.

By the multivariate second-derivative test, there exists a neighborhood
U of w\* such that for all w ∈ U \ {w\*},

Φ(w, θ) < Φ(w\*, θ).

Therefore w\* is a strict local maximizer of Φ(·, θ).

## 9.2 Local isolation of the equilibrium

If w\* is a strict local maximizer of Φ(·, θ), then in a sufficiently
small neighborhood U of w\* there is no other point w ≠ w\* with
∇\_w Φ(w, θ) = 0, because any other stationary point in U would also be a
local extremum candidate and would contradict strictness at w\*.

Hence w\* is locally isolated as a solution of F(w, θ) = 0.

## 9.3 Invertibility

Negative definiteness implies that the Hessian matrix H(w\*, θ) is
nonsingular. Therefore C(θ) = −H(w\*, θ) is also nonsingular at w\*.

## 9.4 Computational verification (TDC instance)

For the TDC model, the algebraic identities and representative numeric
support checks for interior nondegeneracy are verified computationally in

`src/network_potential_engine/scripts/check_A3_tdc_interior_nondegeneracy.py`

and in the pytest file

`tests/test_A3_tdc_interior_nondegeneracy.py`.
