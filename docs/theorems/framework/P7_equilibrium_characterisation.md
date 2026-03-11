# P7 — Equilibrium Characterisation

## Purpose

Provide the canonical **first-order characterisation** of equilibrium network configurations in terms of stationarity conditions on the network potential.

This step is the bridge between:

- Step `6(4)` (equilibrium as an optimisation solution concept), and
- the operator layer, which uses derivatives of the potential evaluated at equilibrium.

The key output is an assumption-scoped statement of when an equilibrium `w*` satisfies `∇_w Φ(w*, \tilde{θ}) = 0` (equivalently `F(w*, \tilde{θ})=0`).

## Setup

Canonical objects:

- state: `w ∈ ℝⁿ`
- parameters: `θ ∈ ℝⁿ`
- potential: `Φ(w, θ)` (see `docs/foundations/core_objects.md`)
- equilibrium operator: `F(w, θ) := ∇_w Φ(w, θ)`

Feasibility and equilibrium solution concept:

- feasible set: `W_feas(r)` (see `docs/theorems/framework/P4_feasible_relational_investment.md`)
- equilibrium solution concept: `w* ∈ argmax_{w ∈ W_feas(r)} Φ(w, \tilde{θ})` (see `docs/theorems/framework/P6_equilibrium_network.md`)

Notation note:

- Following Step `5(3)`, any appearance of `Φ(w ; s , θ)` is treated as `Φ(w, \tilde{θ})` with `\tilde{θ}` bundling all exogenous inputs.

## Theorem statement (interior first-order condition)

### T1. Interior local maximiser implies stationarity

Assume:

1. `Φ(·, \tilde{θ})` is differentiable in `w` on a neighborhood of `w*`.
2. `w*` is a local maximiser of `w ↦ Φ(w, \tilde{θ})` over the feasible set `W_feas(r)`.
3. `w*` lies in the interior of `W_feas(r)`.

Then

`∇_w Φ(w*, \tilde{θ}) = 0`.

Equivalently,

`F(w*, \tilde{θ}) = 0`.

### Proof

Because `w*` is an interior local maximiser of a differentiable function, the classical first-order necessary condition for an unconstrained interior optimum applies, yielding `∇_w Φ(w*, \tilde{θ}) = 0`.

## Scope guard (boundary / constrained regimes)

This document does not certify a complete first-order characterisation for constrained/boundary equilibria.

If `w*` lies on the boundary of `W_feas(r)`, the appropriate first-order conditions are KKT-type conditions (requiring additional constraint-qualification hypotheses) and are not asserted here.

## Relationship to A-layer equilibrium definition

The A-layer equilibrium definition (`docs/theorems/framework/A2_equilibrium_existence.md`) defines equilibria as solutions of

`F(w, θ) = 0`.

The statement T1 gives an explicit interface: under the interior regime assumptions above, an optimisation-defined equilibrium from Step `6(4)` satisfies the A-layer stationarity equilibrium condition.

## Repository anchors

- Canonical object system:
  - `docs/foundations/core_objects.md`
- Stationarity equilibrium definition:
  - `docs/theorems/framework/A2_equilibrium_existence.md`
- Equilibrium solution concept and interior interface lemma:
  - `docs/theorems/framework/P6_equilibrium_network.md`
- Feasible set definition:
  - `docs/theorems/framework/P4_feasible_relational_investment.md`

## Domain of validity

This characterisation applies only in the interior regime where `w*` is an interior local maximiser and the potential is differentiable in `w`.

No boundary/KKT or global existence/uniqueness claim is made.

## Computational evidence anchors

This step is a classical first-order necessary-condition statement.

Existing symbolic tooling that computes `F(w, θ) = ∇_w Φ(w, θ)` (used throughout the A-layer checks) is implemented in:

- `src/network_potential_engine/symbolic/gradient.py`
