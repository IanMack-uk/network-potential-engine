# Paper 1 Strengthening Plan (Repo-Certified Upgrades Through E3)

## Target

- Paper: `NetworkPotential_Paper1_OperatorTheory_v0.6.md`
- Folder: `docs/research_papers/Paper1_OperatorTheory/`
- Scope of strengthening in this plan:

  - **Upgrade statements that are now supported by repo-certified framework results** (through **E3**).
  - **Do not** attempt to certify (or rewrite into certified form) operator-theoretic results that are not yet part of the certified theorem spine (e.g. propagation/echo bounds), except by explicitly labelling them as *research results / to-be-certified* and listing what certification artifacts would be required.

------------------------------------------------------------------------

# Suggested Improvement Order (Recommended)

Use this order of tasks unless there is a strong reason to deviate.

1.  **Paper framing pass (no edits yet)**

    - confirm what parts of Paper 1 are intended to be:
        - certified (repo-backed)
        - classical (externally citable)
        - research (uncertified / conjectural)

2.  **Definitions + notation pass (early edits)**

    - ensure all operator objects are defined before first use (`H`, `H^*`, `L`, `S`, `U(t)`)
    - unify notation (especially `H^*` and `H^{\text{\textbackslash*}}` usage)

3.  **Assumptions + scope pass**

    - make interior/hyperbolic/nondegenerate assumptions explicit where needed
    - explicitly qualify TDC-specific certification vs general framework narrative

4.  **Certification linking pass (repo grounding)**

    - add explicit repo references for certified subclaims (theorem doc + tests/scripts)
    - re-label non-certified theorems (propagation/echo bounds) as research / certification pending

5.  **Section-by-section strengthening (body of paper)**

    - apply the concrete edits listed in Section 5 of this plan
    - update dependent later sections immediately when a definition/assumption changes

6.  **Cross-section consistency review (full-paper audit)**

    - reread Paper 1 in order and fix:
        - silent reliance on uncertified claims
        - missing hypotheses on theorem-like statements
        - misaligned “certified vs research” status

7.  **Introduction / abstract / conclusion refresh (last substantive edit)**

    - ensure the abstract and introduction’s “paper establishes” list matches what is actually certified
    - update the conclusion to separate certified results from research claims

8.  **Final proofread pass**

    - grammar, punctuation, spelling
    - readability and formatting consistency

# 1 Relevant repo sources (certified spine)

## 1.1 Canonical theorem documents

- `docs/theorems/framework/A1_admissible_relational_potential_well_posedness.md`
- `docs/theorems/framework/A2_equilibrium_existence.md`
- `docs/theorems/framework/A3b_interior_nondegeneracy.md`
- `docs/theorems/framework/B1_hessian_coupling_theorem.md`
- `docs/theorems/framework/B2_locality_incident_structure_inheritance.md`
- `docs/theorems/framework/C1_equilibrium_response_theorem.md`
- `docs/theorems/framework/D1_inverse_positivity_theorem.md`
- `docs/theorems/framework/D2_mixed_block_positivity_theorem.md`
- `docs/theorems/framework/D3_response_positivity_theorem.md`
- `docs/theorems/framework/E1_explicit_admissible_region_theorem.md`
- `docs/theorems/framework/E2_segment_path_certification_lemma.md`
- `docs/theorems/framework/E3_local_weak_ordering_theorem.md`

## 1.2 Primary tests (paper-facing evidence anchors)

- `tests/test_B1_tdc_hessian_coupling_identity.py`
- `tests/test_B2_tdc_locality_inheritance.py`
- `tests/test_C1_tdc_equilibrium_response_identity.py`
- `tests/test_D1_tdc_inverse_positivity.py`
- `tests/test_D2_tdc_mixed_block_positivity.py`
- `tests/test_D3_tdc_response_positivity.py`
- `tests/test_E1_tdc_region.py`
- `tests/test_E2_tdc_segment_certificate.py`
- `tests/test_E3_tdc_local_weak_ordering.py`

## 1.3 Human-readable certification scripts

- `src/network_potential_engine/scripts/check_B1_tdc_hessian_coupling_identity.py`
- `src/network_potential_engine/scripts/check_B2_tdc_locality_inheritance.py`
- `src/network_potential_engine/scripts/check_C1_tdc_equilibrium_response_identity.py`
- `src/network_potential_engine/scripts/check_D1_tdc_inverse_positivity.py`
- `src/network_potential_engine/scripts/check_D2_tdc_mixed_block_positivity.py`
- `src/network_potential_engine/scripts/check_D3_tdc_response_positivity.py`
- `src/network_potential_engine/scripts/check_E1_tdc_region.py`
- `src/network_potential_engine/scripts/check_E2_tdc_segment_certificate.py`
- `src/network_potential_engine/scripts/check_E3_tdc_local_weak_ordering.py`

Supplementary end-to-end evidence (path/chain summaries):

- `src/network_potential_engine/scripts/check_tdc_chain_witness.py`
- `src/network_potential_engine/scripts/check_tdc_path_summary.py`

------------------------------------------------------------------------

# 2 What the repo already establishes (relevant to Paper 1)

This is the **certified content** you can safely use to strengthen Paper 1.

- **A-layer (A1–A3)**
  - well-posedness / admissibility conditions for the potential class
  - existence of equilibrium in the relevant regime
  - interior nondegeneracy / hyperbolicity regime assumptions (as used downstream)

- **B-layer (B1–B2)**
  - coupling operator identified with the negative equilibrium Hessian (when instantiated in the certified model pipeline)
  - locality/incident inheritance structure (local sparsity / block structure inherited from admissible potentials)

- **C-layer (C1)**
  - equilibrium response identity (linear response / IFT-style derivative identity) in the certified regime

- **D-layer (D1–D3)**
  - inverse positivity, mixed-block positivity, and response-positivity conclusions in the certified regime
  - these provide the mathematically rigorous “sign-preserving comparative statics” backbone

- **E-layer (E1–E3)**
  - explicit admissible region characterization
  - segment/path certification lemma
  - local weak ordering theorem (model-certified)

------------------------------------------------------------------------

# 3 What is missing or ambiguous (relative to Paper 1’s current scope)

Paper 1 contains major themes which **go beyond** the current certified spine:

- propagation semigroup bounds (e.g. Theorem 0.4.1, Theorem 6.2.1)
- finite-speed propagation style conclusions
- echo operator theory and reconstruction results

These may be correct research statements, but they are **not currently certified** by the repo’s A1–E3 theorem workflow.

Therefore, the strengthening strategy is:

- For anything that rests on **(Hessian -> coupling operator) + locality + response identity + sign properties**, you can upgrade to *repo-certified* statements.
- For anything that asserts **quantitative propagation/echo bounds**, you should:

  - label as *research result / not yet certified in the theorem workflow*, and
  - add a short “Certification status” note listing what repo artifacts would be required (theorem doc + check script + tests).

------------------------------------------------------------------------

# 4 Claim inventory (Paper 1)

The plan below treats the paper’s main objects/claims in the order they appear.

## 4.1 Core objects (high impact)

- relational potential `\Phi_G`
- equilibrium `w^*` and equilibrium Hessian `H^*`
- coupling operator `L = -H^*`
- locality of Hessian / sparsity structure and induced edge-interaction graph
- susceptibility operator `S = (H^*)^{-1}`
- linear response equation `H^* \delta w = f`

## 4.2 Higher-level operator theory (lower impact for A1–E3)

- spectral decomposition results (largely classical finite-dimensional spectral theory)
- propagation semigroup `U(t) = e^{-tL}`
- echo operators and reconstruction claims

------------------------------------------------------------------------

# 5 Concrete strengthening edits (section-by-section)

This section lists **exact strengthening targets**, with **what to change**, and **what to cite**.

## 5.1 Front matter: “Mathematical Scope” (lines ~19–52)

### Strengthening targets

- “Relational potentials generate self-adjoint Hessian operators …”
- “equilibrium evaluations determine admissible coupling operators …”
- “susceptibility operators describing equilibrium response …”

### Proposed upgrade

Add a short “Certification Status (Repo)” paragraph immediately after the scope bullets that states:

- Coupling operator identification `L = -H^*` is certified in the repo **in the TDC instantiation**.
- Locality/incident inheritance is certified in the same regime.
- Linear response identity is certified in the same regime.

### Repo citations

- B1: `docs/theorems/framework/B1_hessian_coupling_theorem.md`
- B2: `docs/theorems/framework/B2_locality_incident_structure_inheritance.md`
- C1: `docs/theorems/framework/C1_equilibrium_response_theorem.md`

Evidence anchors:

- `tests/test_B1_tdc_hessian_coupling_identity.py`
- `tests/test_B2_tdc_locality_inheritance.py`
- `tests/test_C1_tdc_equilibrium_response_identity.py`

## 5.2 Section 0.2 “Equilibrium Operators” (lines ~389–438)

### Strengthening targets

- The identity `L = -H^*`.
- The claim “At interior strict local maxima the coupling operator satisfies `L \succ 0`.”

### Proposed upgrade

- Attach explicit hypothesis language:

  - interior equilibrium
  - hyperbolicity / nondegeneracy
  - (if needed) strict local maximum condition

- Add a parenthetical “(certified in repo in the TDC regime)” annotation to the `L = -H^*` identity.

### Repo citations

- B1 (core identity): `docs/theorems/framework/B1_hessian_coupling_theorem.md`
- A3b (nondegeneracy/hyperbolicity regime): `docs/theorems/framework/A3b_interior_nondegeneracy.md`

Evidence anchors:

- `tests/test_B1_tdc_hessian_coupling_identity.py`

## 5.3 Section 0.3 “Response vs Propagation” (lines ~439–470)

### Strengthening targets

- `S = (H^*)^{-1}` definition and linear response equation.

### Proposed upgrade

- Explicitly tie the response equation to the certified response identity theorem.
- Add a short note distinguishing:

  - response identity (certified)
  - subsequent propagation constructions (research; certification pending)

### Repo citations

- C1: `docs/theorems/framework/C1_equilibrium_response_theorem.md`

Evidence anchors:

- `tests/test_C1_tdc_equilibrium_response_identity.py`
- `src/network_potential_engine/scripts/check_C1_tdc_equilibrium_response_identity.py`

## 5.4 Section 0.4 “Main Theorem — Locality-Induced Propagation Geometry”

### Strengthening targets

- claims that “structural locality implies Hessian is sparse”
- claims that the induced sparsity defines an interaction graph

### Proposed upgrade

Split the strengthening into two layers:

1. **Certified statement** (add explicitly): locality/incident inheritance implies locality structure of the Hessian/coupling operator.
2. **Research statement** (keep as is, but label): the quantitative semigroup bounds / finite propagation conclusions.

### Repo citations

- Certified locality inheritance:
  - B2: `docs/theorems/framework/B2_locality_incident_structure_inheritance.md`

### Certification TODO (for later)

In the paper, add a short “Certification status” note near Theorem 0.4.1:

- Not currently part of the repo’s certified theorem spine.
- To certify, would require:

  - new theorem doc under `docs/theorems/`
  - `check_*.py` script producing numeric/operator evidence
  - `tests/test_*.py` capturing the bound(s) in a stable regression form

## 5.5 Section 2: “Differential Operators” (Hessian/locality/coupling)

### Strengthening targets

- Hessian operator definition + self-adjointness proposition
- locality of the Hessian proposition
- coupling operator definitions and “operators generated by relational potentials” proposition

### Proposed upgrade

- Where you assert locality and “generated by potentials” in the equilibrium/Hessian-to-coupling pipeline, cite B1/B2.
- Where you assert self-adjointness, either:

  - cite a classical result (finite-dimensional Hessian symmetry for `C^2` scalar potentials), or
  - if the repo theorem docs explicitly include self-adjointness as part of B1/B2, cite them.

### Repo citations

- B1: `docs/theorems/framework/B1_hessian_coupling_theorem.md`
- B2: `docs/theorems/framework/B2_locality_incident_structure_inheritance.md`

## 5.6 Section 5: “Response Operators”

### Strengthening targets

- hyperbolicity implies invertibility
- susceptibility operator definition
- linear response equation

### Proposed upgrade

- Tie invertibility/hyperbolicity assumptions to A3b.
- Tie the response identity to C1.
- If the paper later discusses sign structure of `S` (or response coefficients), attach D1–D3 as the certified sign-control backbone.

### Repo citations

- A3b: `docs/theorems/framework/A3b_interior_nondegeneracy.md`
- C1: `docs/theorems/framework/C1_equilibrium_response_theorem.md`
- D1–D3: `docs/theorems/framework/D1_inverse_positivity_theorem.md`, `D2_mixed_block_positivity_theorem.md`, `D3_response_positivity_theorem.md`

Evidence anchors:

- `tests/test_C1_tdc_equilibrium_response_identity.py`
- `tests/test_D1_tdc_inverse_positivity.py`
- `tests/test_D2_tdc_mixed_block_positivity.py`
- `tests/test_D3_tdc_response_positivity.py`

## 5.7 Any ordering / monotonicity / sign-preserving comparative statics discussion

### Strengthening targets

Anywhere you assert “sign-preserving response”, “monotone comparative statics”, “ordering” as an operator consequence.

### Proposed upgrade

- If the paper treats these as general, add a qualifier:

  - “certified in repo for the TDC admissible region / certified path regime”

- Add pointers to the admissible region and segment/path results.

### Repo citations

- E1–E3: region/segment/local ordering
  - `docs/theorems/framework/E1_explicit_admissible_region_theorem.md`
  - `docs/theorems/framework/E2_segment_path_certification_lemma.md`
  - `docs/theorems/framework/E3_local_weak_ordering_theorem.md`

Evidence anchors:

- `tests/test_E1_tdc_region.py`
- `tests/test_E2_tdc_segment_certificate.py`
- `tests/test_E3_tdc_local_weak_ordering.py`
- `src/network_potential_engine/scripts/check_tdc_chain_witness.py`
- `src/network_potential_engine/scripts/check_tdc_path_summary.py`

------------------------------------------------------------------------

# 6 Assumptions audit (what Paper 1 should make explicit)

To align with the certified spine, Paper 1 should explicitly distinguish:

- `w^*` is an **interior equilibrium** (when required)
- **hyperbolicity / nondegeneracy** assumptions (invertibility of `H^*`)
- **locality/admissibility** assumptions on `\Phi_G` needed for sparsity/local interaction structure
- whether a claim is:

  - general for the admissible class, or
  - certified only for a specific instantiation (TDC)

------------------------------------------------------------------------

# 7 Hidden dependency audit (common implicit steps)

When reviewing Paper 1, check for silent use of:

- existence of equilibria (A2)
- interiority of equilibria (often needed for the clean Hessian operator discussion)
- invertibility / hyperbolicity (A3)
- locality inheritance and incident structure (B2)
- response identity / IFT derivative mapping (C1)
- sign control / inverse positivity (D1–D3)

------------------------------------------------------------------------

# 8 Risks / ambiguity list

- Paper 1 contains extensive propagation/echo results. These should not be labelled “certified” unless you create a dedicated certification track for them.
- Where Paper 1 currently reads as general-framework, you may need to insert “(certified for the TDC instantiation)” qualifiers so that the paper does not overclaim beyond the repo spine.

------------------------------------------------------------------------

# 9 Minimal edit log template (for after changes)

After implementing strengthening edits, record:

1. Sections changed
2. Claims upgraded to “certified” (with theorem doc + test/script anchors)
3. Claims qualified (general -> model-specific)
4. Claims marked “research / not yet certified”

------------------------------------------------------------------------

# 10 Best immediate next step

Choose one:

1. Apply the strengthening plan as **non-invasive citations/qualifiers only** (no re-proving anything).
2. If you want the propagation/echo results certified, start a new theorem certification track for:

   - locality-induced semigroup bounds
   - echo locality and reconstruction

   using the same theorem workflow structure (doc + script + tests).
