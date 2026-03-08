# ChatGPT Theorem Development Brief — D1 Inverse Positivity Theorem

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

D1 should export only the inverse-positivity property of the coupling operator.

It must not leak:

- mixed-block positivity (D2)
- response positivity (D3)
- ordering consequences (E-layer)

------------------------------------------------------------------------

# Governing constraint

**TDC is the certification target; do not weaken or reinterpret it.**

D1 must be stated so that, when instantiated with the TDC coupling operator C(θ), it reproduces the inverse-positivity mechanism already proved in:

- `docs/theorems/tdc/tdc_local_ordering_theorem_formal.md` (Lemma 8)

No framework reformulation is allowed that would require changing TDC semantics or “massaging” the TDC hypotheses.

------------------------------------------------------------------------

# Purpose

This brief initiates a ChatGPT conversation to produce a **certification-quality statement and proof** for:

**Theorem D1 — Inverse Positivity Theorem**

in the Network Potential Framework.

D1 is the first theorem in the sign-controlled response layer:

A1 → A2 → A3 → B1 → B2 → C1 → **D1** → D2 → D3 → E1 → E2 → E3.

D1 must export a checkable sufficient condition implying the entrywise nonnegativity of the inverse coupling operator:

```text
C(θ)^{-1} ≥ 0
```

------------------------------------------------------------------------

# Repository Sources (authoritative)

ChatGPT should inspect and ground all mathematics in the following repository sources:

## Workflow / architecture

- `docs/development_plan/Certified Theorem Workflow for the Network Potential Framework.md`
  - Describes D1 as the inverse-positivity layer.

- `docs/development_plan/theorem_dependency_and_tdc_alignment.md`
  - Fixes the role of D1 in the spine and the separation of sign-control layers.

## Foundational definitions

- `docs/foundations/core_objects.md`
  - Canonical coupling operator object C and response factorisation.

## Certified framework theorems upstream

- `docs/theorems/framework/B1_hessian_coupling_theorem.md`
- `docs/theorems/framework/C1_equilibrium_response_theorem.md`

## TDC theorem (certification target)

- `docs/theorems/tdc/tdc_local_ordering_theorem_formal.md`
  - Lemma 8: inverse positivity via M-matrix mechanism.

## Existing code evidence (TDC-specific sufficient conditions)

- `src/network_potential_engine/theorem/tdc_bounds.py`
- `tests/test_tdc_bounds.py`
- `src/network_potential_engine/scripts/check_tdc_bounds.py`

(These currently support the TDC sign-control regime via curvature-margin bounds and should be treated as model evidence, not as the definition of D1.)

------------------------------------------------------------------------

# What the repo already establishes (high-level)

1. The TDC theorem already proves an inverse-positivity mechanism: strict diagonal dominance of a Z-matrix implies nonsingular M-matrix, hence C(θ)^{-1} ≥ 0.
2. The codebase implements and tests analytic TDC margin/bounds used to certify sign-control regimes along paths.
3. The framework pipeline requires D1 to export inverse positivity separately from mixed-block positivity (D2).

------------------------------------------------------------------------

# What is missing / what D1 must clarify

D1 must make explicit:

- the **general matrix-analytic hypotheses** under which inverse positivity holds,
- a clean separation between:
  - the abstract theorem statement, and
  - the model-specific (TDC) instantiation,
- the exact object to which the theorem applies (the coupling operator C(θ), equilibrium-evaluated when appropriate).

D1 must not be framed as “TDC bounds” or “TDC region” as the theorem itself; those remain model evidence and should appear only as an instantiation/corollary.

------------------------------------------------------------------------

# Recommended framing (best practice)

## Primary theorem statement: nonsingular M-matrix

State D1 at the framework level as:

- If C(θ) is a **nonsingular M-matrix**, then its inverse is entrywise nonnegative:

```text
C(θ)^{-1} ≥ 0.
```

This is the cleanest reusable operator-theory statement and aligns exactly with the TDC theorem’s Lemma 8 language.

## Concrete sufficient condition (corollary): strictly diagonally dominant Z-matrix

Include an explicit corollary usable in applications:

- If C(θ) is a **Z-matrix** (off-diagonals ≤ 0) and is **strictly diagonally dominant** (by rows, with positive diagonal), then C(θ) is a nonsingular M-matrix.

This is a tight, checkable sufficient condition that is also exactly how the TDC proof is structured.

------------------------------------------------------------------------

# Proposed minimal certifiable theorem statement (D1)

## Theorem D1 (Inverse positivity via M-matrix mechanism)

Let C(θ) be the coupling matrix/operator exported by B1 (equilibrium-evaluated when appropriate).

Assume C(θ) is a nonsingular M-matrix.

Then

```text
C(θ)^{-1} ≥ 0
```

entrywise.

### Corollary (strict diagonal dominance sufficient condition)

If, additionally, C(θ) is a Z-matrix and is strictly diagonally dominant by rows, then C(θ) is a nonsingular M-matrix, hence C(θ)^{-1} ≥ 0.

------------------------------------------------------------------------

# Required assumptions

Minimal assumptions for D1:

- C(θ) is a real square matrix.
- D1 imposes a structural sign hypothesis (Z-matrix / M-matrix style) at the level needed to guarantee inverse positivity.

No assumptions about H_{wθ} or response are allowed in D1.

------------------------------------------------------------------------

# Proof skeleton (auditable)

1. Recall the definition/characterisation of a nonsingular M-matrix (classical result).
2. Invoke the classical theorem: a nonsingular M-matrix has a nonnegative inverse.
3. For the corollary: show that strict diagonal dominance of a Z-matrix implies nonsingular M-matrix (classical sufficient condition).

All classical theorems invoked must be clearly stated as standard matrix analysis results.

------------------------------------------------------------------------

# Hidden dependency audit

D1 must not depend on:

- C1 response identity (except as a downstream consumer; D1 stands alone as a statement about C)
- any mixed-block object H_{wθ}
- any ordering/path arguments

D1 should depend only on:

- the coupling operator object C exported by B1
- classical matrix theory about M-matrices / Z-matrices / diagonal dominance

------------------------------------------------------------------------

# TDC instantiation requirement (must match existing theorem)

The D1 document must include a short “TDC instantiation” note stating:

- In the TDC model, C(θ) is tridiagonal with off-diagonals −c ≤ 0 (a Z-matrix).
- The TDC condition `q + α θ_i > 0` provides the diagonal-dominance margin as recorded in the TDC formal theorem.
- Therefore, by the corollary, C(θ) is a nonsingular M-matrix and C(θ)^{-1} ≥ 0.

This must match Lemma 7–8 of:

- `docs/theorems/tdc/tdc_local_ordering_theorem_formal.md`

------------------------------------------------------------------------

# Suggested code / verification plan (supporting)

Framework-level D1 is a mathematical theorem; code evidence should be conservative and must not replace the theorem.

Recommended evidence strategy:

- Keep existing TDC evidence as model checks:
  - `src/network_potential_engine/scripts/check_tdc_bounds.py`
  - `tests/test_tdc_bounds.py`

Optional additions only if needed for clarity:

- A small check script (framework-facing) that constructs a representative C(θ) from the TDC model and verifies:
  - off-diagonals are nonpositive,
  - diagonal dominance holds under the TDC margin condition,
  - and numerically that C(θ)^{-1} is entrywise nonnegative for a sample θ.

Any such numeric check must be labelled as supporting evidence only.

------------------------------------------------------------------------

# Best immediate next step

1. Draft the canonical framework theorem file under `docs/theorems/framework/` as `D1_inverse_positivity_theorem.md`.
2. Ensure the theorem’s primary statement is “nonsingular M-matrix ⇒ inverse nonnegative”, with diagonal dominance as a corollary.
3. Add an explicit “TDC instantiation” paragraph that matches the existing TDC theorem Lemma 8.
4. Update the workflow checklist to reference the new D1 theorem doc and existing evidence.
