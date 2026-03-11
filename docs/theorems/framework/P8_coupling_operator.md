# P8 — Coupling Operator

## Purpose

Fix the canonical **coupling operator** object for the Network Potential Framework as the negative Hessian of the potential with respect to state variables.

This step is a **step-level anchor** for the operator layer and is intentionally thin.

The canonical theorem authority for the coupling-operator definition and notation discipline is:

- `docs/theorems/framework/B1_hessian_coupling_theorem.md`

This document exists to:

- bind Step `8(6)` in the dependency map to the repo-certified theorem authority (B1),
- record evaluation conventions used downstream (e.g. equilibrium-evaluated shorthand), and
- provide direct repo anchors to code/tests/scripts that certify the identity `C = −H` in example instantiations.

## Setup

Canonical objects (frozen in `docs/foundations/core_objects.md`):

- state: `w ∈ ℝⁿ`
- parameters: `θ ∈ ℝⁿ`
- potential: `Φ(w, θ)`
- Hessian: `H(w, θ) := ∇²_{ww} Φ(w, θ)`
- coupling operator: `C(w, θ) := −H(w, θ)`

Notation note:

- Following Step `5(3)`, any appearance of `Φ(w ; s , θ)` is treated as `Φ(w, \tilde{θ})` with `\tilde{θ}` bundling all exogenous inputs.

## Definitions

### D1. State Hessian

On the admissible potential domain `Ω_Φ ⊆ W × Θ` (see `docs/foundations/admissibility_taxonomy.md`), define

`H(w, θ) := ∇²_{ww} Φ(w, θ)`.

### D2. Coupling operator

Define the coupling operator

`C(w, θ) := −H(w, θ)`.

## Notational scope (C(w,θ) versus C(θ))

The canonical coupling operator is the **two-variable** object `C(w, θ)`.

If later documents write `C(θ)`, this must be understood as either:

1. a model-specific simplification in which `H` (hence `C`) is independent of `w`, or
2. shorthand for evaluation at an equilibrium branch when licensed, i.e.
   - `C(θ) := C(w*(θ), θ)`.

This notation discipline is defined and enforced by B1.

## Repository anchors

### A. Canonical theorem authority

- `docs/theorems/framework/B1_hessian_coupling_theorem.md`

### B. Locality / sparsity inheritance (downstream structural dependency)

- `docs/theorems/framework/B2_locality_incident_structure_inheritance.md`

### C. Code anchors

- Hessian computation:
  - `src/network_potential_engine/symbolic/hessian.py` (`hessian_of_potential`)
- Coupling operator construction:
  - `src/network_potential_engine/symbolic/operators.py` (`coupling_operator_from_hessian`)

### D. Evidence anchors (tests and scripts)

- `tests/test_operators.py`
- `tests/test_B1_tdc_hessian_coupling_identity.py`
- `src/network_potential_engine/scripts/check_B1_tdc_hessian_coupling_identity.py`

## Domain of validity

This object definition is valid on the admissible potential domain `Ω_Φ` wherever `Φ ∈ C²_w(Ω_Φ)`.

No claim is made here about invertibility, sign structure, or ordering consequences.

## Computational evidence anchors

The repository contains symbolic checks and tests that certify the identity `C(w,θ) = −H(w,θ)` for example instantiations (see Evidence anchors above).
