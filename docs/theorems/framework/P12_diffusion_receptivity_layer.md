# P12 — Diffusion / Receptivity Layer

## Purpose

Fix a canonical **receptivity modulation** of the propagated value field.

This step introduces a node-indexed receptivity vector `ρ` and defines the modulated propagated value field

- `\tilde{v} := ρ ⊙ v`,

where `⊙` denotes entrywise (Hadamard) multiplication.

This step does not define propagation (`v = G s`), node energy aggregation (`E = β₀ s + β₁ v`), or effective energy; those belong to adjacent steps.

------------------------------------------------------------------------

## Setup

Let `V` be a finite node set.

Let:

- `v ∈ ℝ^{|V|}` be a node-indexed propagated value vector (Step `10(11)`, canonical anchor: `docs/theorems/framework/P10_propagation_mapping.md`).

Let:

- `ρ ∈ ℝ^{|V|}` be a node-indexed receptivity vector.

------------------------------------------------------------------------

## Definition (receptivity modulation)

Define the receptivity-modulated propagated value field as

`\tilde{v} := ρ ⊙ v`.

Equivalently, in coordinates:

- for each node index `i`, `\tilde{v}_i := ρ_i v_i`.

------------------------------------------------------------------------

## Interface invariants

### I1. Node indexing discipline

`ρ`, `v`, and `\tilde{v}` are all node-indexed and share the same dimension:

- `ρ, v, \tilde{v} ∈ ℝ^{|V|}`.

### I2. Separation from propagation

Propagation is defined upstream (Step `10(11)`) via

- `v := G s`.

Step `12(13)` does not change how `v` is generated; it only post-processes `v` entrywise.

### I3. Separation from energy aggregation and effective energy

- Node energy aggregation `E := β₀ s + β₁ v` is defined in Step `11(12)`.
- Effective energy that combines receptivity and propagation is defined in Step `13(14)`.

Accordingly, Step `12(13)` exports `\tilde{v}` but introduces no `β` weights and does not define `E`.

------------------------------------------------------------------------

## Domain of validity

This definition requires:

- well-defined node vectors `ρ` and `v` of matching dimension.

No assumptions about sign, boundedness, or dynamics are required.

------------------------------------------------------------------------

## Computational evidence anchors

Evidence is provided by unit tests that verify:

- shape/indexing (`\tilde{v}` has the same length as `v`),
- correct elementwise scaling (`\tilde{v}_i = ρ_i v_i`),
- correct special cases (e.g. `ρ = 1` yields `\tilde{v} = v`, `ρ = 0` yields `\tilde{v} = 0`).

Repo anchors:

- `src/network_potential_engine/diffusion/receptivity.py`
- `tests/test_receptivity.py`
- optional: `src/network_potential_engine/scripts/check_P12_diffusion_receptivity.py`
