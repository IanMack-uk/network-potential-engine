# P9 — Green Operator (Inverse Coupling Operator)

## Purpose

This step introduces the **Green operator** as the inverse of the coupling operator.

It is an operator-construction step:

- it defines the Green operator `G = C^{-1}` on regimes where the coupling operator is invertible;
- it does **not** apply `G` to any specific signal (that occurs in Step `10(11)`);
- it is distinct from the response operator `R = C^{-1} H_{wθ}` (exported by C1).

------------------------------------------------------------------------

## Setup

Let `Φ(w, θ)` be a relational potential and define canonical objects as in `docs/foundations/core_objects.md`:

- equilibrium operator: `F(w, θ) := ∇_w Φ(w, θ)`
- Hessian: `H(w, θ) := ∇²_{ww} Φ(w, θ)`
- coupling operator: `C(w, θ) := −H(w, θ)`

In downstream response analysis one often works with the equilibrium-evaluated coupling operator

- `C(θ) := C(w*(θ), θ)`

when an equilibrium branch `w*(θ)` is licensed by the A-layer and the response regime (e.g. C1).

------------------------------------------------------------------------

## Definition (Green operator)

### Two-variable operator

On any regime in which `C(w, θ)` is **nonsingular**, define the Green operator

`G(w, θ) := C(w, θ)^{-1}`.

Equivalently, `G(w, θ)` is the unique linear operator satisfying

- `C(w, θ) G(w, θ) = I` and `G(w, θ) C(w, θ) = I`.

### Equilibrium-evaluated shorthand

When an equilibrium branch `w*(θ)` is available and the equilibrium-evaluated coupling operator

- `C(θ) := C(w*(θ), θ)`

is nonsingular, define

- `G(θ) := C(θ)^{-1} = C(w*(θ), θ)^{-1}`.

------------------------------------------------------------------------

## Domain of validity

The Green operator is defined **only** on parameter/state regimes where the relevant coupling operator is invertible.

- If one writes `G(w, θ)`, this requires `C(w, θ)` nonsingular.
- If one writes `G(θ)`, this requires:
  1. an equilibrium-evaluation convention (`C(θ) := C(w*(θ), θ)` or a model-specific simplification where `C` is independent of `w`), and
  2. `C(θ)` nonsingular.

Invertibility is not established by P9; it is imported from the appropriate regimes (e.g. interior nondegeneracy in C1, or structural sufficient conditions in the S-layer supporting D1).

------------------------------------------------------------------------

## Separation from adjacent operators / steps

- **Coupling operator (Step 8(6))**
  - `C(w, θ) := −H(w, θ)`.

- **Green operator (this step)**
  - `G(w, θ) := C(w, θ)^{-1}` (when defined).

- **Response operator (C1 / core objects)**
  - `R(θ) = D_θ w*(θ)` and, under the response regime,
    - `R(θ) = C(θ)^{-1} H_{wθ}(w*(θ), θ)`.
  - This uses `G(θ)` but is strictly downstream of P9.

- **Propagation mapping (Step 10(11))**
  - The application `v = G s` is introduced in Step `10(11)`.
  - P9 does not introduce `s` or `v`.

------------------------------------------------------------------------

## Computational evidence (supporting)

The repository already contains symbolic and numeric uses of `C^{-1}`:

- Symbolic (small examples):
  - `src/network_potential_engine/symbolic/operators.py` (uses `coupling_operator.inv()` in `response_operator`)
  - `src/network_potential_engine/scripts/check_C1_tdc_equilibrium_response_identity.py`

- Numeric:
  - `src/network_potential_engine/numeric/response.py` (computes `C^{-1} H_{wθ}` via `np.linalg.solve` rather than forming the explicit inverse)

- D-layer supporting evidence that explicitly computes `C(θ)^{-1}` in a representative TDC regime:
  - `docs/theorems/framework/D1_inverse_positivity_theorem.md`
  - `src/network_potential_engine/scripts/check_D1_tdc_inverse_positivity.py`
  - `tests/test_D1_tdc_inverse_positivity.py`

------------------------------------------------------------------------

## Notational scope

- The canonical coupling operator is the two-variable object `C(w, θ)`.
- The canonical inverse operator is correspondingly `G(w, θ) = C(w, θ)^{-1}` when defined.
- The shorthand `G(θ)` is permitted only when the evaluation convention is explicit (equilibrium-evaluated or model-simplified).
