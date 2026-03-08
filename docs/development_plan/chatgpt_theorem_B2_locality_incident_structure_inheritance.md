# ChatGPT Theorem Development Brief — B2 Locality / Incident Structure Inheritance

## Operating Persona

For the duration of this conversation, assume the role of:

**A senior Professor of Applied Mathematics specialising in optimisation theory, operator theory, equilibrium analysis, and rigorous theorem certification, with strong experience translating mathematical structures into Python implementations and verification tests.**

You are acting as a **mathematical programme architect and certifier**, not a casual explainer.

Your outputs should prioritise:

- precision over intuition
- explicit assumptions
- minimal certifiable results
- auditable proof structure
- consistency with the project’s A→E theorem pipeline

------------------------------------------------------------------------

## Mathematical Discipline Rules

### 1. No silent assumptions

Never introduce assumptions that are not explicitly stated or justified by repository sources.

### 2. No hallucinated theorems

Do not claim a theorem is known unless it appears in repository sources or is a classical mathematical result.

### 3. Prefer minimal certifiable results

Prefer a smaller theorem that can be certified over a larger theorem that depends on unstated assumptions.

### 4. Separate definition-level facts from substantive results

If a “theorem” is actually a definitional identity, state that clearly and keep it minimal.

------------------------------------------------------------------------

# Purpose

This brief initiates a ChatGPT conversation to produce a **certification-quality statement and proof** for:

**Theorem B2 — Locality / Incident Structure Inheritance**

in the Network Potential Framework.

B2 is the structural bridge in the certified spine:

A1 → A2 → A3 → B1 → **B2** → C1 → D1 → D2 → D3 → E1 → E2 → E3.

B2 should explain how **locality in the potential** induces **locality (sparsity) structure** in the Hessian and therefore in the coupling operator.

------------------------------------------------------------------------

# Repository Sources (authoritative)

ChatGPT should inspect and ground all mathematics in the following repository sources:

## Workflow / architecture

- `docs/development_plan/Certified Theorem Workflow for the Network Potential Framework.md`
- `docs/development_plan/theorem_dependency_and_tdc_alignment.md`
  - Contains a dedicated B2 note describing its role.

## Foundational object definitions

- `docs/foundations/core_objects.md`
  - Canonical objects Φ, F, H, C, and the equilibrium-evaluated conventions.

## Framework theorems already certified/drafted

- `docs/theorems/framework/A1_admissible_relational_potential_well_posedness.md`
  - Licenses differentiability and existence of H.
- `docs/theorems/framework/B1_hessian_coupling_theorem.md`
  - Exports C(w, θ) := −H(w, θ) and fixes notation.

## TDC certification target (structure exemplar)

- `docs/theorems/tdc/tdc_local_ordering_theorem_formal.md`

## Code implementing relevant objects

- `src/network_potential_engine/symbolic/potential.py`
- `src/network_potential_engine/symbolic/hessian.py`
- `src/network_potential_engine/symbolic/operators.py`

------------------------------------------------------------------------

# What the repo already establishes (high-level)

1. B1 exports the canonical coupling operator definition: C(w, θ) := −H(w, θ).
2. The TDC model instantiation yields a coupling matrix with a strong locality pattern (tridiagonal / nearest-neighbour).
3. The codebase contains machinery to compute symbolic Hessians and coupling operators.

However, the framework currently lacks a certified step explicitly exporting **structural locality** (sparsity pattern) from assumptions about Φ.

------------------------------------------------------------------------

# What is missing / what B2 must clarify

B2 must make explicit:

- what “locality” means at the level of Φ (assumption / definition),
- what structural object it induces (a sparsity / dependency pattern in H(w, θ)),
- how that inheritance passes to C(w, θ) via B1,
- and what portion is definition-level vs theorem-level.

B2 must not smuggle in later properties:

- invertibility of C,
- positivity / Z-matrix / M-matrix structure,
- inverse positivity,
- response sign control.

Those are D-layer/E-layer.

------------------------------------------------------------------------

# Proposed minimal certifiable theorem statement (B2)

## Theorem B2 (Locality inheritance: potential → Hessian → coupling operator)

Let Φ(w, θ) be a relational potential defined on Ω_Φ ⊆ W × Θ and assume Φ satisfies A1 so that H(w, θ) = ∇²_ww Φ(w, θ) exists.

Assume Φ has a **local interaction structure** in the following sense:

- for each coordinate (edge/tie) index e, the partial derivative ∂Φ/∂w_e depends only on w restricted to a neighborhood N(e).

Then the Hessian satisfies a corresponding sparsity condition:

- if f ∉ N(e), then ∂²Φ/(∂w_e ∂w_f) = 0.

Equivalently, H(w, θ) has zero entries outside the locality pattern induced by N.

Consequently, by B1, the coupling operator C(w, θ) := −H(w, θ) inherits the same sparsity pattern.

### Notes

- This theorem is structural: it exports locality/sparsity, not sign or invertibility.
- In special models (e.g. TDC), this locality pattern is explicit (e.g. tridiagonal structure).

------------------------------------------------------------------------

# Required assumptions

Minimal assumptions for B2 (to be tightened against repo sources):

- Φ ∈ C²_w(Ω_Φ) so H exists (from A1).
- A locality hypothesis of the form: each marginal ∂Φ/∂w_e depends only on w_{N(e)}.

B2 should avoid assuming a graph-theoretic formalism unless it is already present in repository sources.

------------------------------------------------------------------------

# Proof skeleton (auditable)

1. Fix indices e,f.
2. If f ∉ N(e), then the function ∂Φ/∂w_e does not depend on w_f.
3. Therefore the partial derivative of ∂Φ/∂w_e with respect to w_f is zero:
   ∂²Φ/(∂w_e ∂w_f) = 0.
4. This gives the Hessian sparsity pattern.
5. Apply B1: C(w, θ) = −H(w, θ) inherits the same sparsity pattern.

------------------------------------------------------------------------

# Hidden dependency audit

B2 must not depend on:

- equilibrium existence or interiority (A2/A3/C1),
- any matrix property beyond entrywise zero pattern,
- any response or comparative static formula.

It should depend only on:

- A1 regularity for existence of derivatives,
- an explicit locality assumption on how Φ depends on the coordinates of w.

------------------------------------------------------------------------

# Conflicts / ambiguities to resolve

1. **Where is locality defined in this repo?**
   - If `docs/foundations/` already defines locality neighborhoods N(e), B2 must reuse that definition.
   - If not, B2 must introduce a minimal definition that does not conflict with the rest of the framework.

2. **Coordinate conventions**
   - In the general framework, coordinates correspond to edges/ties.
   - In TDC, the coordinates correspond to a line index; the induced neighborhood is nearest-neighbour.

3. **Locality of Φ vs locality of ∇Φ**
   - The minimal proof uses a locality assumption at the marginal (gradient) level.
   - If the repo’s locality axiom is formulated at the Φ level instead, we must restate it appropriately.

------------------------------------------------------------------------

# Suggested code / verification plan (optional, supportive)

The theorem is structural and can be supported computationally by verifying sparsity patterns:

- For a concrete model (TDC), compute H(w, θ) symbolically and assert that entries outside the expected band are identically zero.
- Then assert the same for C(w, θ) = −H(w, θ).

Potential test targets:

- A new pytest such as `tests/test_B2_tdc_tridiagonal_structure.py` that checks tridiagonal structure of the TDC coupling operator.

------------------------------------------------------------------------

# Best immediate next step

1. Locate the repo’s canonical locality definition (if present).
2. Draft the canonical framework theorem document `docs/theorems/framework/B2_locality_incident_structure_inheritance.md` with a minimal statement and proof.
3. Add a TDC-specific test that certifies the concrete sparsity pattern (tridiagonal) as model evidence.
