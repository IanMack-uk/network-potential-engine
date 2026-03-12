# C1 — Equilibrium Response Theorem

## Purpose

This theorem exports the **equilibrium response identity**: under the interior nondegeneracy regime, the equilibrium branch depends differentiably on the parameters and its derivative factorises into an inverse-curvature term and a mixed-derivative term.

It is the interface between the operator-generation layer (B1/B2) and the sign-controlled response layer (D1–D3).

No claim is made here about sign structure (inverse positivity) or ordering consequences.

------------------------------------------------------------------------

# 1. Setup

Let Φ(w, θ) be a relational potential satisfying the regularity assumptions of

A1 — Admissible Relational Potential Well-Posedness.

Let the equilibrium operator be

F(w, θ) = ∇\_w Φ(w, θ)

as defined in `docs/foundations/core_objects.md`.

Let the Hessian and coupling operator be

H(w, θ) = ∇²\_{ww} Φ(w, θ),

C(w, θ) = −H(w, θ).

Let the mixed derivative block be

H\_{wθ}(w, θ) = D\_θ(∇\_w Φ(w, θ)).

Fix a parameter value θ and let w\*(θ) be an interior equilibrium satisfying

F(w\*(θ), θ) = 0.

------------------------------------------------------------------------

# 2. Hypotheses (response regime)

Assume:

1. The equilibrium operator F(w, θ) = ∇_w Φ(w, θ) is continuously differentiable in (w, θ) on the admissible domain (as explicitly licensed in A1), so that the mixed derivative block H\_{wθ}(w, θ) = D_θ(∇_w Φ(w, θ)) exists and is continuous.
2. The equilibrium branch θ ↦ w\*(θ) is locally well-defined and differentiable on the regime of interest (as licensed by A3a under the interior nondegeneracy hypothesis).
3. The equilibrium w\*(θ) is an interior equilibrium and satisfies the interior nondegeneracy hypothesis of A3b, i.e. H(w\*(θ), θ) is nonsingular.

Equivalently, the equilibrium-evaluated coupling matrix

C(θ) := C(w\*(θ), θ)

is nonsingular.

------------------------------------------------------------------------

# 3. Theorem statement (factorised response identity)

Under the hypotheses above, the equilibrium mapping θ ↦ w\*(θ) is differentiable (locally, on the interior nondegeneracy region), and its Jacobian satisfies

D\_θ w\*(θ) = C(θ)^{-1} H\_{wθ}(w\*(θ), θ).

------------------------------------------------------------------------

# 4. Proof

Consider the equilibrium condition

F(w\*(θ), θ) = 0.

Differentiate both sides with respect to θ (entrywise) and apply the chain rule:

D\_w F(w\*(θ), θ) · D\_θ w\*(θ) + D\_θ F(w\*(θ), θ) = 0.

Because F(w, θ) = ∇\_w Φ(w, θ), we have

D\_w F(w, θ) = ∇²\_{ww} Φ(w, θ) = H(w, θ)

and

D\_θ F(w, θ) = D\_θ(∇\_w Φ(w, θ)) = H\_{wθ}(w, θ).

Evaluating at (w\*(θ), θ) gives

H(w\*(θ), θ) · D\_θ w\*(θ) + H\_{wθ}(w\*(θ), θ) = 0.

By definition, C(θ) := −H(w\*(θ), θ), so the previous display becomes

−C(θ) · D\_θ w\*(θ) + H\_{wθ}(w\*(θ), θ) = 0.

Since C(θ) is nonsingular by hypothesis, rearranging yields

D\_θ w\*(θ) = C(θ)^{-1} H\_{wθ}(w\*(θ), θ).

------------------------------------------------------------------------

# 5. Notational scope

- The canonical coupling operator is the two-variable object C(w, θ) = −H(w, θ).
- In this theorem, C(θ) denotes the equilibrium-evaluated object C(w\*(θ), θ).

------------------------------------------------------------------------

# 6. Computational evidence (supporting)

For the TDC model, a symbolic verification of the response identity is implemented in:

- `src/network_potential_engine/scripts/check_A3a_tdc_equilibrium_regularity.py`
