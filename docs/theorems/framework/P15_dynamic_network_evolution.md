# P15 — Dynamic Network Evolution

## Purpose

Fix a canonical **dynamic extension** of the Network Potential framework by specifying a time-indexed evolution rule for the network state.

This step introduces a time-dependent relational state `w(t)` (or discrete-time `w_t`) and a dynamics template driven by the potential `Φ(w, θ)` via its stationarity operator `F(w, θ) := ∇_w Φ(w, θ)`.

This step is scoped to an **interior/unconstrained** regime and does not impose feasibility constraints (e.g. projection onto `W_feas(r)`).

------------------------------------------------------------------------

## Setup

Let `Φ(w, θ)` be a relational potential as fixed canonically in Step `5(3)` (anchor: `docs/theorems/framework/P5_network_potential_functional.md`).

Let the stationarity operator be

- `F(w, θ) := ∇_w Φ(w, θ)`,

as used in Step `7(5)` (anchor: `docs/theorems/framework/P7_equilibrium_characterisation.md`).

Fix a parameter vector `θ` (held constant during evolution).

------------------------------------------------------------------------

## Definitions

### D1. Time-dependent network state

A **dynamic network state** is a time-indexed state variable

- `w(t) ∈ ℝ^n`, for `t ≥ 0`,

where `n` matches the canonical state dimension in `docs/foundations/core_objects.md`.

A discrete-time variant is a sequence

- `w_t ∈ ℝ^n`, for `t = 0, 1, 2, ...`.

### D2. Gradient-ascent dynamics (continuous time)

Define the (interior) gradient-ascent dynamics by the ordinary differential equation

- `\dot{w}(t) := F(w(t), θ) = ∇_w Φ(w(t), θ)`.

### D3. Euler discretisation (discrete time)

Define the corresponding explicit Euler iteration with step size `η > 0`:

- `w_{t+1} := w_t + η F(w_t, θ)`.

------------------------------------------------------------------------

## Interface invariants

### I1. Steady state equals stationarity (interior regime)

For the continuous-time dynamics, a steady state `w̄` satisfies

- `\dot{w}(t) = 0` at `w(t)=w̄` iff `F(w̄, θ) = 0`.

Thus, in the interior regime, steady states correspond to the stationarity condition used to characterise equilibrium.

### I2. Separation from feasibility / constrained dynamics

This step does not enforce constraints such as `w ∈ W_feas(r)`.

Any projected dynamics or KKT/variational-inequality constrained evolution belongs to a later scarcity/constrained package.

------------------------------------------------------------------------

## Domain of validity

This step requires:

- a regime where `F(w, θ) = ∇_w Φ(w, θ)` is well-defined,
- and an interior/unconstrained interpretation of the evolution rule.

No global convergence or stability claims are made here.

------------------------------------------------------------------------

## Computational evidence anchors

Evidence is provided by unit tests and a smoke-check script that demonstrate:

- a toy potential where the Euler iteration converges to a stationary point,
- and that fixed points of the iteration satisfy `F(w, θ)=0` in the toy case.

Repo anchors:

- `src/network_potential_engine/dynamics/gradient_flow.py`
- `tests/test_dynamic_network_evolution.py`
- optional: `src/network_potential_engine/scripts/check_P15_dynamic_network_evolution.py`
