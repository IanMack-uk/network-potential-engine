# A3a — Equilibrium regularity

## Purpose

This theorem establishes **equilibrium regularity**: under a nonsingularity regime at an interior equilibrium, the equilibrium condition

F(w, θ) = 0

licenses a locally well-defined and differentiable equilibrium branch

w*(θ).

This theorem does not export the factorised response identity; that identity belongs to

- C1 — Equilibrium Response Theorem.

------------------------------------------------------------------------

# 1. Setup

Let Φ(w, θ) be a relational potential satisfying the regularity assumptions of

A1 — Admissible Relational Potential Well-Posedness.

Let the equilibrium operator be

F(w, θ) = ∇_w Φ(w, θ)

as defined in `docs/foundations/core_objects.md`.

Fix a parameter value θ₀ and an equilibrium w₀ satisfying

F(w₀, θ₀) = 0.

Assume w₀ is an interior equilibrium (w₀ lies in the interior of W).

------------------------------------------------------------------------

# 2. Hypotheses (regularity regime)

Assume:

1. Φ is twice continuously differentiable in w and once continuously differentiable in θ on the admissible domain (as in A1), so that:

   - D_w F(w, θ) exists and is continuous,
   - D_θ F(w, θ) exists and is continuous.

2. The equilibrium is nondegenerate at (w₀, θ₀):

   D_w F(w₀, θ₀) is invertible.

Since F(w, θ) = ∇_w Φ(w, θ), we have

D_w F(w, θ) = ∇²_{ww} Φ(w, θ) = H(w, θ),

so the nondegeneracy hypothesis is equivalent to invertibility of the equilibrium Hessian H(w₀, θ₀).

------------------------------------------------------------------------

# 3. Theorem statement (local branch and differentiability)

Under the hypotheses above, there exist neighborhoods U of w₀ and V of θ₀ such that:

1. For every θ ∈ V there exists a unique w*(θ) ∈ U satisfying

   F(w*(θ), θ) = 0.

2. The mapping θ ↦ w*(θ) is differentiable on V.

------------------------------------------------------------------------

# 4. Proof (classical external input)

This theorem is an application of the classical implicit function theorem.

1. By A1, F is continuously differentiable in (w, θ) in a neighborhood of (w₀, θ₀).
2. By hypothesis, D_w F(w₀, θ₀) is invertible.
3. Therefore, by the implicit function theorem, there exist neighborhoods U of w₀ and V of θ₀ and a unique differentiable map w*(·): V → U such that F(w*(θ), θ) = 0 for all θ ∈ V.

------------------------------------------------------------------------

# 5. Notational scope

- The canonical equilibrium operator is the two-variable object F(w, θ).
- This theorem licenses a local equilibrium branch w*(θ) near θ₀.
- Any formula for D_θ w*(θ) is exported by C1, not by this theorem.

------------------------------------------------------------------------

# 6. TDC model instantiation (certification target)

In the Theta-Dependent Curvature (TDC) instantiation, the equilibrium branch is defined by the explicit linear system

C(θ) w*(θ) = θ

whenever the coupling operator C(θ) is nonsingular.

In this model regime, differentiability of the explicitly constructed branch is supported by symbolic calculations.

------------------------------------------------------------------------

# 7. Computational evidence (supporting)

TDC-specific supporting checks are implemented in:

- `src/network_potential_engine/scripts/check_A3a_tdc_equilibrium_regularity.py`
- `tests/test_A3a_tdc_equilibrium_regularity.py`
