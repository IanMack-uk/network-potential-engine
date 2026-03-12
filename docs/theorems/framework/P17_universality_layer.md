# P17 — Universality Layer

## Purpose

Fix a canonical **universality layer** interface for the Network Potential framework.

This step introduces a disciplined way to state that a property of the framework holds **uniformly across a class of admissible potentials**.

It is interface-first:

- it freezes the object `ℱ` (a class of potentials defined by explicit predicates),
- it freezes the schema of a “universality claim” (scope + assumptions + statement),
- it does **not** certify any new deep operator theorems beyond this schema.

------------------------------------------------------------------------

## Setup

Canonical objects and notation discipline are fixed upstream (see `docs/foundations/core_objects.md`).

- state: `w ∈ ℝⁿ`
- parameters: `θ ∈ ℝᵖ`
- relational potential: `Φ(w, θ)`

Operator spine (upstream anchors):

- coupling operator (Step `8(6)`): `C(w, θ) := −∇²_{ww} Φ(w, θ)`
  - canonical anchor: `docs/theorems/framework/P8_coupling_operator.md`

- Green operator (Step `9(7)`): `G(w, θ) := C(w, θ)^{-1}` (when defined)
  - canonical anchor: `docs/theorems/framework/P9_green_operator.md`

- propagation mapping (Step `10(11)`): `v := G(w, θ) s`
  - canonical anchor: `docs/theorems/framework/P10_propagation_mapping.md`

Framework admissibility conventions for potentials are specified in:

- `docs/foundations/admissible_potential_grammar.md`

------------------------------------------------------------------------

## Definitions

### D0. Bridge-operator schema (node/edge typing generalization)

Some admissible model classes distinguish:

- an edge-indexed state space `\mathbb{R}^{|E|}` for relational weights, and
- a node-indexed space `\mathbb{R}^{|V|}` for source/value fields.

In such cases, the Green operator `G(w, θ) := C(w, θ)^{-1}` remains an operator on the state space induced by differentiation with respect to `w`.

A node-level propagation operator is then obtained by introducing explicit bridge/readout maps:

- `B : \mathbb{R}^{|V|} \to \mathbb{R}^{|E|}` (inject node sources into state space)
- `R : \mathbb{R}^{|E|} \to \mathbb{R}^{|V|}` (read out state-space responses back to nodes)

and defining the induced node-level transfer operator

- `K(w, θ) := R \, G(w, θ) \, B = R \, C(w, θ)^{-1} \, B`.

In this schema, the node-level propagation mapping may be stated as `v := K(w, θ) s`.

This repository’s certified core pipeline uses a single ambient `\mathbb{R}^n` convention for `w`, `s`, and `v`. The bridge-operator schema above records the path to full generality when one wishes to keep node- and edge-indexed spaces distinct.

### D1. Universality class of potentials

A **universality class** `ℱ` is a specified family of potentials

- `ℱ ⊆ { Φ : Ω_Φ → ℝ }`

together with an explicit **membership predicate** that is auditable.

In this repository, the baseline universality class is the **framework-admissible class**:

- `ℱ_framework := { Φ : Φ is framework-admissible by the admissible potential grammar }`.

Additional universality classes may be defined as subclasses of `ℱ_framework` by adding explicit predicates.

Examples (schema only; not certified as the only useful choices):

- regularity subclass: `ℱ_C2 := { Φ ∈ ℱ_framework : Φ ∈ C²_w(Ω_Φ) }`
- invertibility-regime subclass: `ℱ_inv := { Φ ∈ ℱ_framework : C(w, θ) is nonsingular on a declared regime }`

The defining requirement is: membership in `ℱ` must be stated by **explicit conditions**, not by informal descriptions.

### D2. Universality claim

A **universality claim** over a class `ℱ` is a statement of the form:

- `∀ Φ ∈ ℱ : P(Φ)`

where `P(Φ)` is a well-typed property that may reference:

- the canonical objects induced by `Φ` (e.g. `C(w, θ)`), and
- declared regimes in which those objects are defined (e.g. invertibility regimes for `G`).

### D3. Universality claim record (audit schema)

Every universality claim recorded in this repository must specify:

1. **Scope**
   - the class `ℱ` (or subclass) over which the claim quantifies.
2. **Assumptions / regimes**
   - any additional hypotheses required beyond class membership (e.g. invertibility of `C`).
3. **Statement**
   - the precise property `P(Φ)` asserted.
4. **Dependencies**
   - upstream operator objects/results required to interpret or prove the claim (e.g. Step `8(6)` and Step `9(7)`).

------------------------------------------------------------------------

## Domain of validity

This step is definitional.

It is valid on any regimes where the referenced upstream objects are well-defined:

- to reference `C(w, θ)`, one requires the regularity needed to define `∇²_{ww} Φ`;
- to reference `G(w, θ)`, one additionally requires invertibility of `C(w, θ)` on the declared regime.

No claim of existence, uniqueness, or convergence is introduced by this step.

------------------------------------------------------------------------

## Computational evidence anchors

This step is interface-only.

No new code, tests, or scripts are required for certification.

Evidence for the upstream operator spine is already present in the repository (see anchors in P8/P9/P10 and their tests/scripts).
