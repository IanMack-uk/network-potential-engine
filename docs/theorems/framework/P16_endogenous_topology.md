# P16 — Endogenous Topology

## Purpose

Fix a canonical **endogenous topology** interface for the Network Potential framework.

In earlier steps the edge set `E` is treated as fixed and the network state variables evolve on that fixed support.

This step introduces a mechanism by which the **edge set itself may change** (edge creation/removal), producing an updated topology `E'`.

------------------------------------------------------------------------

## Setup

Let `V` be a finite node set.

Let `E ⊆ V × V` be a directed edge set and let `w` denote tie strengths on `E`, represented using the Step `1(1)` representation discipline (canonical anchor: `docs/theorems/framework/P1_network_representation_graph_layer.md`).

Let `Φ(w, θ)` be a relational potential (Step `5(3)`, canonical anchor: `docs/theorems/framework/P5_network_potential_functional.md`).

Let `w*(θ; E)` denote an equilibrium network configuration conditional on the topology `E` (Step `6(4)`, canonical anchor: `docs/theorems/framework/P6_equilibrium_network.md`).

------------------------------------------------------------------------

## Definitions

### D1. Topology update operator

A **topology update operator** is any rule

`\mathcal{T} : (E, \text{equilibrium-informed data}, θ) \mapsto E'`

that produces an updated edge set `E' ⊆ V × V` from the current edge set `E`, parameters `θ`, and any chosen equilibrium-informed data.

This step is interface-first: it fixes the existence and role of `\mathcal{T}` without asserting a unique canonical functional form.

### D2. Endogenous topology evolution (discrete time)

An **endogenous topology evolution** is a discrete-time sequence of edge sets defined by

- `E_{t+1} := \mathcal{T}(E_t, \cdots)`.

Optionally one may view the relational weights as evolving on each `E_t` via an inner equilibrium solve or inner dynamics, but this step does not certify existence/uniqueness of a joint fixed point in `(E,w)`.

------------------------------------------------------------------------

## Interface invariants

### I1. Representation discipline when `E` changes

When `E` changes to `E'`, any vector/matrix representation of edge weights must be re-established using the Step `1(1)` conventions (e.g. by choosing a new edge ordering for `E'`).

### I2. Separation from weight dynamics

Endogenous topology updates `E`.

Weight dynamics (fixed-topology updates of `w`) are treated separately (e.g. Step `15(15)`).

------------------------------------------------------------------------

## Domain of validity

This step requires only:

- a finite node set `V`, and
- well-defined edge sets `E` and `E'` as subsets of `V × V`.

No combinatorial optimality, equilibrium existence, or convergence properties are proven here.

------------------------------------------------------------------------

## Computational evidence anchors

Evidence is provided by unit tests and an optional smoke-check script that verify:

- topology update helpers are deterministic,
- updates respect node bounds (`E' ⊆ V×V`), and
- representation conversions can be re-established after an update.

Repo anchors:

- `src/network_potential_engine/topology/endogenous_topology.py`
- `tests/test_endogenous_topology.py`
- optional: `src/network_potential_engine/scripts/check_P16_endogenous_topology.py`
