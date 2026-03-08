# ChatGPT Theorem Development Brief — E1 Explicit Admissible-Region Theorem

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

E1 should export only an **explicit admissible region** of parameter values under which the D-layer hypotheses hold pointwise.

It must not leak:

- path/segment certification (E2)
- integration-to-ordering arguments (E3)
- any stronger ordering conclusions

------------------------------------------------------------------------

# Governing constraint

**TDC is the certification target; do not weaken or reinterpret it.**

E1 must be stated so that, when instantiated with the TDC model, it reproduces the admissible-region construction and guarantees already proved in:

- `docs/theorems/tdc/tdc_local_ordering_theorem_formal.md` (Definition 14 and Proposition 15)

No framework reformulation is allowed that would require changing TDC semantics or “massaging” the TDC hypotheses.

------------------------------------------------------------------------

# Purpose

This brief initiates a ChatGPT conversation to produce a **certification-quality statement and proof** for:

**Theorem E1 — Explicit Admissible-Region Theorem**

in the Network Potential Framework.

E1 is the first theorem in the ordering package layer:

A1 → A2 → A3 → B1 → B2 → C1 → D1 → D2 → D3 → **E1** → E2 → E3.

E1 must export a **checkable region** of parameter values such that for all θ in that region, the pointwise sign-control hypotheses needed for D3 hold.

------------------------------------------------------------------------

# Repository Sources (authoritative)

ChatGPT should inspect and ground all mathematics in the following repository sources:

## Workflow / architecture

- `docs/development_plan/Certified Theorem Workflow for the Network Potential Framework.md`
- `docs/development_plan/theorem_dependency_and_tdc_alignment.md`

## Foundational definitions

- `docs/foundations/core_objects.md`
  - Objects: w*(θ), C(θ), H_{wθ}(w*(θ), θ), D_θ w*(θ).

## Framework theorems upstream

- `docs/theorems/framework/D1_inverse_positivity_theorem.md`
- `docs/theorems/framework/D2_mixed_block_positivity_theorem.md`
- `docs/theorems/framework/D3_response_positivity_theorem.md`

## TDC theorem (certification target)

- `docs/theorems/tdc/tdc_local_ordering_theorem_formal.md`
  - Definition 14 (admissible region)
  - Proposition 15 (pointwise positivity on admissible region)

## Existing code evidence (TDC specific)

- `src/network_potential_engine/theorem/tdc_region.py`
- `src/network_potential_engine/theorem/tdc_segment.py`
- `src/network_potential_engine/theorem/tdc_path_summary.py`
- `tests/test_tdc_region.py`
- `tests/test_tdc_segment.py`
- `src/network_potential_engine/scripts/check_tdc_region.py`

------------------------------------------------------------------------

# What the repo already establishes (high-level)

1. The TDC theorem defines an explicit region of θ values (Definition 14) in terms of checkable sufficient-condition inequalities.
2. On that region, the pointwise sign-control hypotheses hold (Proposition 15), i.e. the D-layer conditions are satisfied.
3. The codebase implements region checks/certificates, including region membership and sampling/scan utilities.

------------------------------------------------------------------------

# What is missing / what E1 must clarify

E1 must make explicit:

- what the admissible region is (as a set defined by inequalities)
- what it guarantees (pointwise validity of D1/D2, hence D3)
- what it does NOT guarantee (no path/segment or ordering claims)

E1 must not:

- assume a path/segment structure
- perform any integration argument

------------------------------------------------------------------------

# Proposed minimal certifiable theorem statement (E1)

## Theorem E1 (Explicit admissible region)

Fix a model (e.g. TDC) and define an explicit set R ⊆ Θ of parameter values θ by checkable inequalities such that for every θ ∈ R:

- C(θ) is invertible and C(θ)^{-1} ≥ 0 (D1 hypothesis holds), and
- H_{wθ}(w*(θ), θ) ≥ 0 (D2 hypothesis holds).

Then, for all θ ∈ R, the response positivity conclusion of D3 holds:

D_θ w*(θ) ≥ 0.

------------------------------------------------------------------------

# Proof skeleton (auditable)

1. Unpack the definition of the admissible region R.
2. Show R implies the pointwise hypotheses of D1 and D2.
3. Invoke D3 (which composes C1 + D1 + D2) to conclude D_θ w*(θ) ≥ 0 pointwise on R.

------------------------------------------------------------------------

# Hidden dependency audit

E1 depends on:

- the pointwise D-layer hypotheses (D1/D2) and their combination (D3)
- model-specific inequalities defining the region

E1 must not depend on:

- E2 path/segment certification
- E3 ordering arguments

------------------------------------------------------------------------

# Suggested code / verification plan (supporting)

Recommended evidence artifacts:

- Existing TDC region checks/tests should remain the main evidence:
  - `src/network_potential_engine/theorem/tdc_region.py`
  - `tests/test_tdc_region.py`
  - `src/network_potential_engine/scripts/check_tdc_region.py`

Optional additions for symmetry with the framework naming:

- `src/network_potential_engine/scripts/check_E1_tdc_region.py`
- `tests/test_E1_tdc_region.py`

These should verify:

- membership checks for representative θ values
- that the region conditions imply the D-layer conditions (either directly or by calling existing condition-check utilities)

------------------------------------------------------------------------

# Best immediate next step

1. Audit `tdc_region.py` and the exact inequalities used, and map them to Definition 14 / Proposition 15.
2. Draft the canonical framework theorem doc `docs/theorems/framework/E1_explicit_admissible_region_theorem.md`.
3. Decide whether to add dedicated E1-named check/test artifacts or to rely on the existing TDC region evidence.
