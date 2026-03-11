# P5 — Network Potential Functional

## Purpose

Fix the canonical **network potential functional** used as the scalar objective for evaluating relational network configurations.

This step is definitional. It specifies:

- the function signature of the potential `Φ`,
- the admissible domain on which `Φ` is defined, and
- the interface between feasibility constraints (Step `4(2)`) and admissibility taxonomy domains.

This document must remain consistent with the canonical objects frozen in:

- `docs/foundations/core_objects.md`

and the admissible construction specification:

- `docs/foundations/admissible_potential_grammar.md`.

## Setup

Canonical ambient variables:

- state: `w ∈ ℝⁿ`
- parameters: `θ ∈ ℝⁿ`

The representation discipline for `w` as an edge-indexed vector / supported matrix is fixed in Step `1(1)` (canonical reference: `docs/theorems/framework/P1_network_representation_graph_layer.md`).

The feasible relational investment set is fixed in Step `4(2)` (canonical reference: `docs/theorems/framework/P4_feasible_relational_investment.md`).

## Definition

### D1. Canonical potential functional (core object)

The **network potential functional** is a scalar map

`Φ(w, θ)`

consistent with the canonical object declaration in `docs/foundations/core_objects.md`.

### D2. Admissible potential domain

Let `W ⊆ ℝⁿ` be an admissible state domain and `Θ ⊆ ℝⁿ` be an admissible parameter domain.

Define the domain of definition of the potential as

`Ω_Φ ⊆ W × Θ`

as in `docs/foundations/admissibility_taxonomy.md`.

On `Ω_Φ`, the potential evaluates to real scalars.

### D3. Feasibility interface

The feasibility constraints from Step `4(2)` define a feasible state set `W_feas(r)`.

The intended optimisation/analysis domain for the network optimisation pipeline must satisfy

- `w ∈ W_feas(r)`,

and therefore `W` is chosen so that

- `W ⊆ W_feas(r)`

(or in the minimal feasibility-only choice, `W = W_feas(r)`).

This ensures feasibility is treated as an admissibility constraint on the state variable `w`.

### D4. Source-value notation (`s`)

Some framework descriptions (including the dependency map) write the potential as

`Φ(w ; s , θ)`

to emphasise dependence on node source values `s`.

In the canonical object system of `docs/foundations/core_objects.md`, the potential is written as `Φ(w, θ)`.

To reconcile these notations without redefining canonical objects, treat source values as part of the parameter bundle:

- there exists an embedding `ι` that maps a pair `(s, θ)` into a single parameter vector `\tilde{θ} := ι(s, θ)`,
- and `Φ(w ; s , θ)` is interpreted as the notational shorthand `Φ(w, \tilde{θ})`.

This preserves the canonical object signature while allowing later steps to reference `s` explicitly when convenient.

## Repository anchors

### A. Admissible potential specification layer

The admissible construction rules for framework potentials are specified in:

- `docs/foundations/admissible_potential_grammar.md`

### B. Example symbolic instantiations

Example symbolic potentials (model instantiations) are implemented in:

- `src/network_potential_engine/symbolic/potential.py`

These are examples of `Φ(w, θ)` in the canonical signature.

## Domain of validity

This document assumes only that:

- `w` and `θ` follow the canonical conventions from `docs/foundations/core_objects.md`, and
- `Φ` is declared with a domain `Ω_Φ` and is scalar-valued on that domain.

No regularity, equilibrium, or operator properties are asserted here.

## Computational evidence anchors

This step is primarily definitional.

Anchors:

- `docs/foundations/core_objects.md`
- `docs/foundations/admissible_potential_grammar.md`
- `src/network_potential_engine/symbolic/potential.py`
