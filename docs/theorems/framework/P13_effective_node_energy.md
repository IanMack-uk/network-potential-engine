# P13 — Effective Node Energy

## Purpose

Fix a canonical definition of **effective node energy** as a node-indexed scalar field that combines:

- intrinsic node source value `s`, and
- receptivity-modulated propagated value field `\tilde{v} = ρ ⊙ v`.

This step is the post-receptivity analogue of the Step `11(12)` node energy definition.

------------------------------------------------------------------------

## Setup

Let `V` be a finite node set.

Let:

- `s ∈ ℝ^{|V|}` be a node-indexed source value vector (Step `3(10)`, canonical anchor: `docs/theorems/framework/P3_node_source_value.md`),
- `v ∈ ℝ^{|V|}` be a node-indexed propagated value vector (Step `10(11)`, canonical anchor: `docs/theorems/framework/P10_propagation_mapping.md`), and
- `ρ ∈ ℝ^{|V|}` be a node-indexed receptivity vector (Step `12(13)`, canonical anchor: `docs/theorems/framework/P12_diffusion_receptivity_layer.md`).

Define the receptivity-modulated propagated value field:

- `\tilde{v} := ρ ⊙ v`.

Let `β₀, β₁ ∈ ℝ` be scalar aggregation weights (introduced in Step `11(12)`).

------------------------------------------------------------------------

## Definition (effective node energy)

Define the effective node energy field as the node-indexed vector

`E_eff := β₀ s + β₁ \tilde{v}`.

Equivalently, substituting `\tilde{v} := ρ ⊙ v` and `v := G s` (when propagation is written in operator form),

`E_eff := β₀ s + β₁ (ρ ⊙ (G s))`.

------------------------------------------------------------------------

## Interface invariants

### I1. Node indexing discipline

`E_eff` is node-indexed and has the same dimension as `s`, `v`, and `ρ`:

- `E_eff ∈ ℝ^{|V|}`.

### I2. Separation from Step 11 energy

Step `11(12)` defines (pre-receptivity) node energy

- `E := β₀ s + β₁ v`.

Step `13(14)` defines (post-receptivity) effective node energy

- `E_eff := β₀ s + β₁ (ρ ⊙ v)`.

These are distinct objects; Step `13(14)` does not redefine Step `11(12)`.

------------------------------------------------------------------------

## Domain of validity

This definition requires:

- well-defined node vectors `s`, `v`, `ρ` of matching dimension, and
- real scalars `β₀`, `β₁`.

No assumptions about invertibility of `C`, existence of `G`, or computation of `v` are proven here; they are imported from earlier steps.

------------------------------------------------------------------------

## Computational evidence anchors

Evidence is provided by unit tests that verify:

- shape/indexing (`E_eff` has the same length as `s`),
- correctness of composition (`E_eff = β₀ s + β₁ (ρ ⊙ v)`),
- correct special cases (e.g. `ρ = 1` yields `E_eff = β₀ s + β₁ v`, matching Step `11(12)`’s formula for `E`).

Repo anchors:

- `src/network_potential_engine/energy/effective_energy.py`
- `tests/test_effective_energy.py`
- optional: `src/network_potential_engine/scripts/check_P13_effective_node_energy.py`
