# P2 — Node Attributes

## Purpose

Fix a canonical representation of **node attributes** for the Network Potential framework.

This step introduces node-indexed attribute objects `x_i` and the aggregated attribute field `x = (x_i)`. These objects are intended to:

- serve as the upstream input layer for Step `3(10)` (node source value `s_i = ψ(x_i)`), and
- support node-indexed capacity parameters such as `r_i` used by the feasibility layer (Step `4(2)`).

------------------------------------------------------------------------

## Setup

Let `V` be a finite node set (as in Step `1(1)` / `docs/theorems/framework/P1_network_representation_graph_layer.md`).

All objects in this step are indexed by nodes `i ∈ V`.

------------------------------------------------------------------------

## Definitions

### D1. Node attribute record (hybrid representation)

For each node `i ∈ V`, define a node attribute record

`x_i := (r_i, extras_i)`

where:

- `r_i ∈ ℝ` is a distinguished **capacity attribute** (relational capacity), and
- `extras_i` is a finite mapping from attribute names to real values:
  - `extras_i : \mathcal K \to ℝ`, with finite support.

The hybrid representation is chosen to provide:

- a stable canonical home for the capacity parameter `r_i` used by Step `4(2)`, while
- allowing additional exploratory attributes (e.g. creativity, influence) without requiring schema refactors.

### D2. Attribute field

Define the network-wide attribute field as the node-indexed family

`x := (x_i)_{i ∈ V}`.

------------------------------------------------------------------------

## Interface invariants

### I1. Node indexing discipline

Attributes are indexed by nodes:

- `x_i` exists only for `i ∈ V`.

### I2. Type discipline

All attribute values in this step are real scalars.

- `r_i ∈ ℝ`
- `extras_i[k] ∈ ℝ` for each attribute key `k` present in `extras_i`.

### I3. Separation from canonical parameter vector

Node attributes are distinct from the framework’s canonical parameter vector `θ ∈ ℝ^n` in `docs/foundations/core_objects.md`.

If a model chooses to embed some or all attributes into the parameter bundle used by `Φ(w, θ)`, that embedding must be stated explicitly downstream (typically in Step `3(10)` and/or in the `Φ(w; s, θ)` reconciliation of Step `5(3)`).

------------------------------------------------------------------------

## Domain of validity

This step requires only:

- a finite node set `V`, and
- well-defined real values for `r_i` and any declared `extras_i` values.

No equilibrium, feasibility, differentiability, or sign assumptions are used.

------------------------------------------------------------------------

## Computational evidence anchors

Evidence is provided by unit tests that verify:

- node indexing and construction of attribute fields,
- type validation and missingness policy,
- retrieval of `r` as a node-indexed vector for use in Step `4(2)`.

Repo anchors:

- `src/network_potential_engine/attributes/node_attributes.py`
- `tests/test_node_attributes.py`
- optional: `src/network_potential_engine/scripts/check_P2_node_attributes.py`
