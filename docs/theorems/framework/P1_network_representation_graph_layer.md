# P1 — Network Representation (Graph Layer)

## Purpose

Fix a canonical graph-layer representation for relational systems within the Network Potential framework.

This document exists to make graph-indexed notation (e.g. `w_{ij}`, `E \subseteq V \times V`) compatible with the framework’s canonical state-vector convention `w \in \mathbb{R}^n` used in `docs/foundations/core_objects.md`, without requiring downstream steps to redefine network primitives.

## Setup

Let:

- `V` be a finite node (vertex) set.
- `E \subseteq V \times V` be an edge set.

We interpret `E` as directed unless explicitly stated otherwise. Undirected networks are treated as the special case where `(i,j) \in E` iff `(j,i) \in E`, together with a symmetry convention on weights.

## Definitions

### D1. Weighted relational network

A **weighted relational network** is a triple

`G = (V, E, w)`

where `w` is a weight assignment on edges.

### D2. Edge-weight function

An **edge-weight function** is a map

`w : E \to \mathbb{R}`

(or more generally `w : E \to \mathcal{W}` for an admissible weight set `\mathcal{W} \subseteq \mathbb{R}` specified by the model instance).

### D3. Matrix representation induced by an edge-weight function

Assume `V` is equipped with a fixed ordering so that we can identify `V \cong \{1,\dots,|V|\}`.

Define the induced matrix representation `W = (W_{ij}) \in \mathbb{R}^{|V| \times |V|}` by

`W_{ij} := \begin{cases}
 w(i,j) & (i,j) \in E,\\
 0 & (i,j) \notin E.
\end{cases}`

This definition fixes a support convention: entries not supported by `E` are identically zero.

### D4. Edge-indexed vector representation (compatibility with `w \in \mathbb{R}^n`)

Let `\pi : \{1,\dots,|E|\} \to E` be a fixed bijection (an ordering of edges).

Define the edge-indexed vector representation `\mathbf{w} \in \mathbb{R}^{|E|}` by

`\mathbf{w}_k := w(\pi(k))`.

When the broader framework uses the canonical state-vector notation `w \in \mathbb{R}^n` (as in `docs/foundations/core_objects.md`), Step 1(1) uses D4 only as a **representational view**:

- if one chooses to represent relational weights as an edge-indexed vector, then `\mathbf{w} \in \mathbb{R}^{|E|}` is the edge-vector induced by an edge ordering `\pi`.
- in the certified core pipeline, downstream steps treat the canonical `w \in \mathbb{R}^n` as the primary state-space object; any identification between `n` and `|E|` must be declared explicitly as part of the chosen model instantiation.

Graph-indexed notation such as `w_{ij}` is then a derived view defined via D3 from `\mathbf{w}` and `E`.

## Export lemma

### L1. Support induces sparsity

Under Definitions D1–D3, if `(i,j) \notin E` then the corresponding matrix entry is identically zero:

`(i,j) \notin E \implies W_{ij} = 0`.

#### Proof

Immediate from the definition of `W_{ij}` in D3.

## Domain of validity

These definitions require only:

- finiteness of `V`,
- a fixed edge set `E`, and
- a well-defined weight assignment on `E`.

No equilibrium, optimality, differentiability, or convexity assumptions are used.

## Computational evidence anchors

This step is primarily definitional. Evidence is provided by unit tests that verify:

- the support convention in D3,
- consistency between D3 and D4 under a chosen edge ordering.

Anchors (to be added when implemented):

- `tests/test_graph_primitives.py`
- optional: `src/network_potential_engine/scripts/check_P1_graph_layer_primitives.py`
