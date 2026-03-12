# P3 — Node Source Value

## Purpose

Fix a canonical definition of **node source value** as a node-indexed scalar field derived from node attributes.

This step introduces source values `s_i` and the source field `s = (s_i)`. The source field is intended to serve as the canonical upstream input to:

- the dependency-map notation `Φ(w; s, θ)` (reconciled with canonical `Φ(w, θ)` in Step `5(3)`), and
- the propagation mapping `v := G(w, θ) s` (Step `10(11)`).

------------------------------------------------------------------------

## Setup

Let `V` be a finite node set (as in Step `1(1)`).

Let node attributes be represented as in Step `2(9)` (canonical anchor: `docs/theorems/framework/P2_node_attributes.md`).

------------------------------------------------------------------------

## Definitions

### D1. Production mapping

A **production mapping** is any map

`ψ : x_i \mapsto s_i`

from node attribute records to real scalars.

This step is **interface-first**: it fixes the existence and role of `ψ` without asserting any unique canonical functional form.

### D2. Node source value

For each node `i ∈ V`, define the node source value as

` s_i := ψ(x_i) `.

### D3. Source value field

Define the source field as the node-indexed family

` s := (s_i)_{i \in V} `.

When `V` is ordered/indexed, the field `s` may be represented as a vector in `ℝ^{|V|}`.

------------------------------------------------------------------------

## Interface invariants

### I1. Node indexing discipline

The source field is indexed by nodes:

- `s_i` exists only for `i ∈ V`, and
- `s` has node dimension `|V|`.

### I2. Separation from edge-indexed state variables

In full generality, the source vector `s` is node-indexed and may therefore be distinct from edge-indexed representations of relational weights (Step `1(1)`).

In the certified core pipeline, the canonical object convention is single-space: `w`, `s`, and downstream node-level fields are all treated as vectors in the same ambient `\mathbb{R}^n` (see `docs/foundations/core_objects.md`). A fully general node/edge bridge-operator formulation is treated as a universality-layer schema (Step `17(17)`).

### I3. Compatibility with canonical potential signature

Some framework descriptions write the potential as `Φ(w; s, θ)` to emphasize dependence on node source values.

The canonical object system in `docs/foundations/core_objects.md` freezes the potential signature as `Φ(w, θ)`.

Compatibility is obtained by treating `s` as part of the parameter bundle, as specified in Step `5(3)`:

- there exists an embedding `ι` that maps a pair `(s, θ)` into a single parameter vector `\tilde{θ} := ι(s, θ)`, and
- `Φ(w; s, θ)` is interpreted as `Φ(w, \tilde{θ})`.

This step does not define `ι`; it only certifies that `s` is the upstream object intended by the `s` notation.

------------------------------------------------------------------------

## Domain of validity

This step requires only:

- a finite node set `V`,
- well-defined node attributes `x_i`, and
- a real-valued mapping `ψ` on those attributes.

No equilibrium, feasibility, invertibility, or monotonicity assumptions are used.

------------------------------------------------------------------------

## Computational evidence anchors

Evidence is provided by unit tests that verify:

- reference evaluation of a simple production mapping `ψ_ref` on node attributes,
- construction of a node-indexed source vector `s` from an attribute field,
- deterministic ordering and shape of the resulting `s` vector.

Repo anchors:

- `src/network_potential_engine/source/node_source_value.py`
- `tests/test_node_source_value.py`
- optional: `src/network_potential_engine/scripts/check_P3_node_source_value.py`
