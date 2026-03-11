# P4 — Feasible Relational Investment

## Purpose

Fix a canonical **feasible state domain** for relational investment.

This document defines the capacity-constrained admissible set of relational configurations and makes the constraint compatible with both:

- the graph-indexed view `w = (w_{ij})` from Step 1(1), and
- the framework’s canonical state-vector convention `w \in \mathbb{R}^n` in `docs/foundations/core_objects.md`.

This step intentionally avoids reusing `Ω` for the feasible state set because `Ω` is reserved for ambient domains in `docs/foundations/admissibility_taxonomy.md`.

## Setup

Let `V` be a finite node set and let `E \subseteq V \times V` be an edge set.

Let `r = (r_i)` be a node-indexed capacity vector.

We use the Step 1(1) network-representation layer (canonical reference: `docs/theorems/framework/P1_network_representation_graph_layer.md`) and its convention that an edge-weight function `w : E \to \mathbb{R}` may be represented either:

- as a matrix `W = (W_{ij})` with support convention `W_{ij}=0` when `(i,j) \notin E`, or
- as an edge-indexed vector `\mathbf{w} \in \mathbb{R}^{|E|}` under a fixed edge ordering.

## Definitions

### D1. Capacity parameters

A **capacity vector** is a collection of real numbers `r = (r_i)` indexed by nodes `i \in V`.

### D2. Feasible relational investment set (graph-indexed form)

Define the feasible relational investment set as

`W_{feas}(r) := \{ w : E \to \mathbb{R} \ \mid\ \sum_{j : (i,j) \in E} w(i,j) \le r_i \ \text{for all } i \in V \}`.

If the model imposes additional admissibility constraints on weights (e.g. nonnegativity), they must be specified explicitly as additional constraints intersected with `W_{feas}(r)`.

### D3. Feasible relational investment set (matrix form)

Under the Step 1(1) matrix representation convention, define

`W_{feas}^{mat}(r) := \{ W \in \mathbb{R}^{|V|\times |V|} \ \mid\ W_{ij}=0\ \text{if } (i,j)\notin E, \ \sum_j W_{ij} \le r_i \ \text{for all } i \}`.

### D4. Feasible relational investment set (vector form)

Fix an edge ordering `\pi : \{1,\dots,|E|\} \to E` and represent weights by `\mathbf{w} \in \mathbb{R}^{|E|}` with `\mathbf{w}_k = w(\pi(k))`.

Define `W_{feas}^{vec}(r)` as the set of vectors `\mathbf{w}` whose induced edge-weight function belongs to `W_{feas}(r)`.

Equivalently, `\mathbf{w} \in W_{feas}^{vec}(r)` iff for every node `i`:

`\sum_{k : \pi(k) = (i,j) \text{ for some } j} \mathbf{w}_k \le r_i`.

## Export lemmas

### L1. Non-emptiness under nonnegative capacities

Assume `r_i \ge 0` for all `i`.

Then `W_{feas}(r)` is non-empty.

#### Proof

The zero assignment `w(i,j) := 0` for all `(i,j) \in E` satisfies `\sum_{j:(i,j)\in E} w(i,j) = 0 \le r_i` for every `i`.

### L2. Convexity (optional)

`W_{feas}(r)` is a convex set in the vector representation whenever it is described by linear inequality constraints.

#### Proof sketch

In the vector representation, each constraint is of the form `a_i^\top \mathbf{w} \le r_i` with `a_i` an indicator vector for edges leaving node `i`. Intersections of linear half-spaces are convex.

## Domain of validity

This document requires only:

- a finite node set `V` and edge set `E`,
- well-defined capacities `r_i`, and
- a fixed representation convention (Step 1(1)).

No optimisation or equilibrium assumptions are used.

## Computational evidence anchors

Evidence is provided by unit tests that verify:

- row-sum capacity checking in matrix form,
- consistency between vector and matrix interpretations under a chosen edge ordering.

Repo anchors:

- `tests/test_feasible_relational_investment.py`
- optional: `src/network_potential_engine/scripts/check_P4_feasible_relational_investment.py`
