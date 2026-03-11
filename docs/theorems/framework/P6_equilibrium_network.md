# P6 — Equilibrium Network

## Purpose

Fix the canonical **equilibrium network configuration** used as the solution concept for the Network Potential Framework.

This step defines equilibrium in the optimisation form used by the dependency map, while making its relationship to the A-layer stationarity equilibrium (`F(w, θ) = 0`) explicit and assumption-scoped.

## Setup

Canonical objects:

- state: `w ∈ ℝⁿ`
- parameters: `θ ∈ ℝⁿ`
- potential: `Φ(w, θ)` (canonical signature; see `docs/foundations/core_objects.md` and `docs/theorems/framework/P5_network_potential_functional.md`)

Feasible domain:

- `W_feas(r)` (see `docs/theorems/framework/P4_feasible_relational_investment.md`)

Notation note:

- Some framework descriptions write `Φ(w ; s , θ)`.
- As fixed in Step `5(3)`, interpret this as a notational view of `Φ(w, \tilde{θ})` where `\tilde{θ}` bundles all exogenous inputs (including any `s`).

## Definitions

### D1. Maximiser set

For fixed parameters `\tilde{θ}` and capacities `r`, define the maximiser set

`\operatorname{ArgMax}(\tilde{θ}, r) := \arg\max_{w \in W_{feas}(r)} Φ(w, \tilde{θ})`.

This is a set-valued object in general.

### D2. Equilibrium network (correspondence form)

An **equilibrium network configuration** is any element

`w* ∈ \operatorname{ArgMax}(\tilde{θ}, r)`.

Equivalently,

`w* ∈ \arg\max_{w \in W_{feas}(r)} Φ(w, \tilde{θ})`.

This definition is a solution concept and does not by itself guarantee existence or uniqueness.

### D3. Single-valued equilibrium (optional upgrade)

If additional hypotheses ensure that `\operatorname{ArgMax}(\tilde{θ}, r)` is a singleton, write `w*(\tilde{θ}, r)` for its unique element.

## Interface lemma (assumption-scoped)

### L1. Interior maximisers satisfy stationarity (conditional)

Assume:

1. `Φ(·, \tilde{θ})` is differentiable in `w` on an open set containing `w*`,
2. `w*` is an interior point of `W_feas(r)` (in particular, no active inequality constraints at `w*`).

Then `w*` satisfies the stationarity condition

`∇_w Φ(w*, \tilde{θ}) = 0`.

In the canonical notation of `docs/foundations/core_objects.md`, this is

`F(w*, \tilde{θ}) = 0` where `F(w, θ) := ∇_w Φ(w, θ)`.

#### Proof

Since `w*` is an interior maximiser of a differentiable function, the first-order necessary condition implies `∇_w Φ(w*, \tilde{θ}) = 0`.

Remark: For boundary optima under active inequality constraints, the appropriate first-order conditions are KKT-type conditions and are not certified by this lemma.

## Repository anchors

- Feasible set definition:
  - `docs/theorems/framework/P4_feasible_relational_investment.md`
- Potential functional definition and signature reconciliation:
  - `docs/theorems/framework/P5_network_potential_functional.md`
- Stationarity equilibrium concept (A-layer):
  - `docs/theorems/framework/A2_equilibrium_existence.md`
  - `docs/theorems/framework/A3a_equilibrium_regularity.md`

## Domain of validity

This document is valid for:

- any declared feasible set `W_feas(r)`,
- any potential `Φ` defined on a domain that includes `W_feas(r)` for the parameter values in question.

No claim of existence or uniqueness of maximisers is made without additional assumptions.

## Computational evidence anchors

This step is definitional.

Existing equilibrium tooling in the repository addresses stationarity equilibria (`F(w, θ)=0`) rather than general constrained argmax:

- symbolic equilibrium routines:
  - `src/network_potential_engine/symbolic/equilibrium.py`
- numeric root-solving of stationarity equilibrium:
  - `src/network_potential_engine/numeric/equilibrium.py`
