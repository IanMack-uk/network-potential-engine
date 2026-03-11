# P11 — Node Energy Definition

## Purpose

Fix a canonical definition of **node energy** as a node-indexed scalar field combining:

- intrinsic node source value `s`, and
- propagated value field `v = G s` (Step `10(11)`).

This step introduces no receptivity/diffusion modulation; that belongs to Step `12(13)`.

------------------------------------------------------------------------

## Setup

Let `V` be a finite node set.

Let:

- `s ∈ ℝ^{|V|}` be a node-indexed source value vector (Step `3(10)`, canonical anchor: `docs/theorems/framework/P3_node_source_value.md`), and
- `v ∈ ℝ^{|V|}` be the propagated value field defined by the propagation mapping (Step `10(11)`, canonical anchor: `docs/theorems/framework/P10_propagation_mapping.md`):
  - `v := G s` on any regime where `G` exists.

Let `β₀, β₁ ∈ ℝ` be scalar aggregation weights.

------------------------------------------------------------------------

## Definition (node energy)

Define the node energy field as the node-indexed vector

`E := β₀ s + β₁ v`.

Equivalently, using `v := G s`,

`E := (β₀ I + β₁ G) s`.

------------------------------------------------------------------------

## Interface invariants

### I1. Node indexing discipline

`E` is node-indexed and has the same dimension as `s` and `v`:

- `E ∈ ℝ^{|V|}`.

### I2. Separation from receptivity modulation

Receptivity/diffusion modulation acts on `v` via

- `\tilde{v} = ρ ⊙ v`,

and is introduced only in Step `12(13)`.

Accordingly, Step `11(12)` energy is defined strictly as `E = β₀ s + β₁ v` with no `ρ` factor.

------------------------------------------------------------------------

## Domain of validity

This definition requires:

- well-defined node vectors `s` and `v` of matching dimension, and
- real scalars `β₀`, `β₁`.

No assumptions about invertibility of `C`, existence of `G`, or computation of `v` are proven here; they are imported from earlier steps.

------------------------------------------------------------------------

## Computational evidence anchors

Evidence is provided by unit tests that verify:

- shape/indexing (`E` has the same length as `s`),
- linearity in `s` and `v`,
- correct special cases (e.g. `β₀=1,β₁=0` yields `E=s`; `β₀=0,β₁=1` yields `E=v`).

Repo anchors:

- `src/network_potential_engine/energy/node_energy.py`
- `tests/test_node_energy.py`
- optional: `src/network_potential_engine/scripts/check_P11_node_energy_definition.py`
