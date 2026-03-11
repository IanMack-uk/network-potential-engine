# P10 — Propagation Mapping

## Purpose

This step introduces the **propagation mapping** as the first application of the inverse response operator to a node-level source vector.

It is an operator-application step:

- it defines the propagated value field `v` via `v = G s`;
- it does **not** introduce node-energy aggregation parameters (`β₀`, `β₁`) (Step `11(12)`);
- it does **not** introduce receptivity modulation `\tilde{v} = ρ \odot v` (Step `12(13)`);
- it is distinct from the response operator `R = C^{-1} H_{wθ}` (exported by C1).

------------------------------------------------------------------------

## Setup

Let `Φ(w, θ)` be a relational potential and define canonical objects as in `docs/foundations/core_objects.md`:

- coupling operator: `C(w, θ) := −∇²_{ww} Φ(w, θ)`
- inverse response operator (when defined): `G(w, θ) := C(w, θ)^{-1}`

Let `s = (s_i) ∈ ℝ^n` denote a node-level source value vector (as defined in Step `3(10)`), and let `v ∈ ℝ^n` denote the propagated value field defined below.

The operator `G(w, θ)` acts on node-indexed vectors, so on any fixed node set it is an `n×n` linear operator.

When an equilibrium branch `w*(θ)` is licensed by the A-layer and one works with equilibrium-evaluated objects, one may write

- `G(θ) := G(w*(θ), θ)`

provided the evaluation convention is explicit and the relevant coupling operator is invertible.

In some model classes (including the TDC instantiation in `core_objects.md`) the coupling operator does not depend on `w`, in which case the shorthand `C(θ)` and `G(θ)` may be used without an equilibrium-evaluation convention.

------------------------------------------------------------------------

## Definition (propagation mapping)

### Two-variable operator application

On any regime in which `G(w, θ)` is defined, and for any admissible source vector `s`, define the propagated value field

`v := G(w, θ) s`.

### Equilibrium-evaluated shorthand

When the shorthand `G(θ)` is licensed (equilibrium-evaluated or model-simplified), define

- `v(θ) := G(θ) s`.

------------------------------------------------------------------------

## Domain of validity

The propagation mapping is defined **only** on regimes where the inverse response operator exists.

- If one writes `v = G(w, θ) s`, this requires `C(w, θ)` nonsingular.
- If one writes `v(θ) = G(θ) s`, this requires:
  1. an explicit evaluation convention for `G(θ)` (equilibrium-evaluated or model-simplified), and
  2. `C(θ)` nonsingular on the parameter regime of interest.

Invertibility is not established by P10; it is imported from the regimes that license `G` (Step `9(7)` and its dependencies).

------------------------------------------------------------------------

## Separation from adjacent operators / steps

- **Inverse response operator (Step 9(7))**
  - `G(w, θ) := C(w, θ)^{-1}` (when defined).

- **Propagation mapping (this step)**
  - `v := G s`.

- **Response operator (C1 / core objects)**
  - `R(θ) = D_θ w*(θ)` and, under the response regime,
    - `R(θ) = C(θ)^{-1} H_{wθ}(w*(θ), θ)`.
  - This uses `C(θ)^{-1}` but is a distinct object from `v`.

- **Node energy (Step 11(12))**
  - Combines `s` and `Gs` with weights `β₀`, `β₁`.

- **Diffusion / receptivity (Step 12(13))**
  - Acts on `v` via `\tilde{v} = ρ \odot v`.

------------------------------------------------------------------------

## Computational note (supporting)

When `G` is represented implicitly through `C`, the definition `v = G s` is equivalently characterised as the unique solution to

- `C(w, θ) v = s`.

Under the equilibrium-evaluated shorthand, this is correspondingly

- `C(θ) v(θ) = s`.

In numeric computations, it is typically preferable to compute `v` by solving the linear system `C v = s` rather than explicitly forming `G = C^{-1}`.

------------------------------------------------------------------------

## Notational scope

- The canonical coupling operator is the two-variable object `C(w, θ)`.
- The canonical inverse operator is correspondingly `G(w, θ) = C(w, θ)^{-1}` when defined.
- The propagation mapping exports `v` as the image of `s` under `G`.
- The shorthand forms `G(θ)` and `v(θ)` are permitted only when the evaluation convention is explicit (equilibrium-evaluated or model-simplified).
