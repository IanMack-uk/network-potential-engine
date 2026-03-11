# Theorem Input Dossier (Filled)

## A. Paper Objective

- Working paper title: Certified monotone comparative statics for relational potentials: an auditable theorem-to-code pipeline
- Target theorem section title: The certified A1–E3 spine (with structural curvature layer S1–S3)
- Intended mathematical contribution in one sentence:
  - Provide an auditable, theorem-first pipeline that starts from a relational potential \(\Phi(w,\theta)\) and ends with a certified local weak ordering statement for equilibria \(w^*(\theta)\), with every intermediate exported object anchored to repository code/tests/scripts.
- Intended certification level:
  - [ ] repo-certified only
  - [x] repo-certified + classical background
  - [ ] mixed certified and labelled research programme

## B. Mathematical Setting

- Ambient space:
  - Repo-certified (framework): \(\Omega = \mathbb R^n \times \mathbb R^n\) with admissible sets \(W \subseteq \mathbb R^n\), \(\Theta \subseteq \mathbb R^n\), and admissible potential domain \(\Omega_\Phi \subseteq W\times\Theta\).
  - Anchor: `docs/theorems/framework/A1_admissible_relational_potential_well_posedness.md`.
- State variable(s):
  - \(w \in W\subseteq\mathbb R^n\).
- Parameter variable(s):
  - \(\theta \in \Theta\subseteq\mathbb R^n\).
- Additional index sets / graph objects:
  - Framework-level locality described abstractly via index neighborhoods \(N(i)\subseteq\{1,\dots,n\}\).
  - Anchor: `docs/theorems/framework/B2_locality_incident_structure_inheritance.md`.
- Core map/operator/potential:
  - Potential: \(\Phi(w,\theta)\).
  - Equilibrium operator: \(F(w,\theta)=\nabla_w\Phi(w,\theta)\).
  - Anchors: `docs/foundations/core_objects.md`, `docs/theorems/framework/A1_admissible_relational_potential_well_posedness.md`.
- Equilibrium concept:
  - Equilibrium is stationarity: \(F(w,\theta)=0\).
  - Anchor: `docs/theorems/framework/A2_equilibrium_existence.md`.

## C. Main Theorem Candidate

- Theorem name:
  - Main theorem candidate (paper-facing): Local weak ordering from sign-controlled response along certified segments.
  - Repo theorem name: `E3 — Local Weak Ordering Theorem`.
- Informal statement in one sentence:
  - If \(\theta'\succeq \theta\) and the segment between them stays in a certified admissible region where the equilibrium response Jacobian is entrywise nonnegative, then \(w^*(\theta')\succeq w^*(\theta)\).
- Formal conclusion desired:
  - \(w^*(\theta')-w^*(\theta)\succeq 0\) coordinatewise.
- Is the conclusion global, local, pointwise, along a path, or model-specific?
  - Repo statement is **segment-level** (path integral along a segment) and is framed as a framework theorem; the computational evidence is explicitly **TDC instantiation**.
  - Anchor: `docs/theorems/framework/E3_local_weak_ordering_theorem.md`.

## D. Minimal Hypotheses

List only assumptions that are genuinely used.

1. **(Repo-certified)** Regularity / derivative object availability:
   - \(\Phi\) is finite/continuous, \(\Phi\in C_w^2(\Omega_\Phi)\), \(\Phi\in C_\theta^1(\Omega_\Phi)\) so that \(F,H,H_{w\theta}\) exist.
   - Anchor: `docs/theorems/framework/A1_admissible_relational_potential_well_posedness.md`.
2. **(Repo-certified)** Equilibrium concept:
   - Equilibrium points satisfy \(F(w,\theta)=0\).
   - Anchor: `docs/theorems/framework/A2_equilibrium_existence.md`.
3. **(Repo-certified)** Interior nondegeneracy (response regime):
   - At equilibrium, \(H(w^*(\theta),\theta)\) is nonsingular (equivalently \(C(\theta)\) nonsingular).
   - Anchor: `docs/theorems/framework/A3b_interior_nondegeneracy.md`.
4. **(Repo-certified)** Response identity in factorised form:
   - \(D_\theta w^*(\theta)=C(\theta)^{-1}H_{w\theta}(w^*(\theta),\theta)\).
   - Anchor: `docs/theorems/framework/C1_equilibrium_response_theorem.md`.
5. **(Repo-certified at interface level; classical input inside D1/S3)** Sign-controlled response and segment containment:
   - Pointwise: \(C(\theta)^{-1}\ge 0\) (D1) and \(H_{w\theta}(w^*(\theta),\theta)\ge 0\) (D2), hence \(D_\theta w^*(\theta)\ge 0\) (D3).
   - Segment-level: \(\gamma([0,1])\subseteq R\) (E2) and endpoint order \(\theta'\succeq\theta\) imply ordering (E3).
   - Anchors:
     - D1: `docs/theorems/framework/D1_inverse_positivity_theorem.md`
     - D2: `docs/theorems/framework/D2_mixed_block_positivity_theorem.md`
     - D3: `docs/theorems/framework/D3_response_positivity_theorem.md`
     - E2: `docs/theorems/framework/E2_segment_path_certification_lemma.md`
     - E3: `docs/theorems/framework/E3_local_weak_ordering_theorem.md`

For each assumption, record:
- whether it is repo-certified, classical, or provisional;
- where it appears in the repo.

Notes:
- The structural curvature layer S1–S3 (Z-matrix, diagonal dominance, M-matrix) provides a **framework-level sufficient route** to D1-style inverse positivity; these steps embed **classical external** matrix results (e.g. Levy–Desplanques / M-matrix facts) but are stated in repo theorem docs.
  - Anchors:
    - S1: `docs/theorems/framework/S1_structural_zmatrix_theorem.md`
    - S2: `docs/theorems/framework/S2_structural_diagonal_dominance_theorem.md`
    - S3: `docs/theorems/framework/S3_structural_mmatrix_theorem.md`

## E. Dependency Chain

Primary certified chain for the paper-facing local ordering theorem:

- A1 -> A2 -> A3b -> C1 -> D1 -> D2 -> D3 -> E1 -> E2 -> E3

Structural sufficient condition chain feeding D1 (optional, but part of the repo’s stated closure architecture):

- A1 -> B1 -> S1 -> (B2) -> S2 -> S3 -> D1

Expand each dependency with anchors.

- A1
  - theorem doc: `docs/theorems/framework/A1_admissible_relational_potential_well_posedness.md`
  - evidence script (TDC instantiation): `src/network_potential_engine/scripts/check_A1_tdc_well_posedness.py`
- A2
  - theorem doc: `docs/theorems/framework/A2_equilibrium_existence.md`
  - evidence script: `src/network_potential_engine/scripts/check_A2_tdc_equilibrium_existence.py`
  - test: `tests/test_A2_tdc_equilibrium_existence.py`
- A3b
  - theorem doc: `docs/theorems/framework/A3b_interior_nondegeneracy.md`
  - evidence script: `src/network_potential_engine/scripts/check_A3b_tdc_interior_nondegeneracy.py`
  - test: `tests/test_A3b_tdc_interior_nondegeneracy.py`
- C1
  - theorem doc: `docs/theorems/framework/C1_equilibrium_response_theorem.md`
  - evidence script: `src/network_potential_engine/scripts/check_C1_tdc_equilibrium_response_identity.py`
  - test: `tests/test_C1_tdc_equilibrium_response_identity.py`
- D1
  - theorem doc: `docs/theorems/framework/D1_inverse_positivity_theorem.md`
  - evidence script: `src/network_potential_engine/scripts/check_D1_tdc_inverse_positivity.py`
  - test: `tests/test_D1_tdc_inverse_positivity.py`
- D2
  - theorem doc: `docs/theorems/framework/D2_mixed_block_positivity_theorem.md`
  - evidence script: `src/network_potential_engine/scripts/check_D2_tdc_mixed_block_positivity.py`
  - test: `tests/test_D2_tdc_mixed_block_positivity.py`
- D3
  - theorem doc: `docs/theorems/framework/D3_response_positivity_theorem.md`
  - evidence script: `src/network_potential_engine/scripts/check_D3_tdc_response_positivity.py`
  - test: `tests/test_D3_tdc_response_positivity.py`
- E1
  - theorem doc: `docs/theorems/framework/E1_explicit_admissible_region_theorem.md`
  - implementation module (TDC): `src/network_potential_engine/theorem/tdc_region.py`
  - evidence script (TDC helpers): `src/network_potential_engine/scripts/check_tdc_region.py`
  - test: `tests/test_tdc_region.py`
- E2
  - theorem doc: `docs/theorems/framework/E2_segment_path_certification_lemma.md`
  - implementation module (TDC): `src/network_potential_engine/theorem/tdc_segment.py`
  - evidence script: `src/network_potential_engine/scripts/check_tdc_segment.py`
  - test: `tests/test_tdc_segment.py`
- E3
  - theorem doc: `docs/theorems/framework/E3_local_weak_ordering_theorem.md`
  - evidence script: `src/network_potential_engine/scripts/check_E3_tdc_local_weak_ordering.py`
  - test: `tests/test_E3_tdc_local_weak_ordering.py`

## F. Implementation Anchors

- symbolic modules:
  - `src/network_potential_engine/symbolic/potential.py` (TDC potential)
  - `src/network_potential_engine/symbolic/gradient.py`
  - `src/network_potential_engine/symbolic/hessian.py`
  - `src/network_potential_engine/symbolic/mixed_derivatives.py`
  - `src/network_potential_engine/symbolic/operators.py` (coupling/response operator construction)
  - `src/network_potential_engine/symbolic/symbols.py`
- numeric modules:
  - `src/network_potential_engine/numeric/lambdified.py`
- theorem helper modules (TDC instantiation):
  - `src/network_potential_engine/theorem/tdc_region.py`
  - `src/network_potential_engine/theorem/tdc_segment.py`
  - `src/network_potential_engine/theorem/tdc_bounds.py`
  - `src/network_potential_engine/theorem/tdc_conditions.py`
  - `src/network_potential_engine/theorem/tdc_local_theorem.py`
- scripts:
  - full trace runner: `src/network_potential_engine/scripts/check_tdc_full_workflow.py`
  - per-stage scripts: `src/network_potential_engine/scripts/check_A1_*.py`, `check_A2_*.py`, ..., `check_E3_*.py`, `check_S1_*.py`, `check_S2_*.py`, `check_S3_*.py`
- tests:
  - theorem-named TDC regressions: `tests/test_A2_tdc_equilibrium_existence.py`, `tests/test_C1_tdc_equilibrium_response_identity.py`, ..., `tests/test_E3_tdc_local_weak_ordering.py`, `tests/test_S*_*.py`

## G. Certification Status Audit

| Claim | Status | Internal Anchor(s) | Notes |
|---|---|---|---|
| A1 regularity licenses derivative objects | Repo-certified | `docs/theorems/framework/A1_admissible_relational_potential_well_posedness.md`; `src/network_potential_engine/scripts/check_A1_tdc_well_posedness.py` | Script is TDC instantiation evidence. |
| Equilibrium defined by stationarity \(F=0\) | Repo-certified | `docs/theorems/framework/A2_equilibrium_existence.md`; `src/network_potential_engine/scripts/check_A2_tdc_equilibrium_existence.py`; `tests/test_A2_tdc_equilibrium_existence.py` | A2 includes an affine coupling-form section as a sufficient model form. |
| A3a equilibrium regularity theorem statement | Certified (framework) + Classical | `docs/theorems/framework/A3a_equilibrium_regularity.md`; `src/network_potential_engine/scripts/check_A3a_tdc_equilibrium_regularity.py`; `tests/test_A3a_tdc_equilibrium_regularity.py` | Uses the classical implicit function theorem; evidence script/test are TDC instantiation support. |
| A3b interior nondegeneracy (nonsingularity at equilibrium) | Repo-certified | `docs/theorems/framework/A3b_interior_nondegeneracy.md`; `src/network_potential_engine/scripts/check_A3b_tdc_interior_nondegeneracy.py`; `tests/test_A3b_tdc_interior_nondegeneracy.py` | |
| Coupling operator definition \(C=-H\) | Repo-certified | `docs/theorems/framework/B1_hessian_coupling_theorem.md`; `src/network_potential_engine/symbolic/operators.py`; `tests/test_operators.py`; `tests/test_B1_tdc_hessian_coupling_identity.py` | |
| Locality / sparsity inheritance | Repo-certified (statement); evidence TDC | `docs/theorems/framework/B2_locality_incident_structure_inheritance.md`; `tests/test_B2_tdc_tridiagonal_coupling_structure.py` | Abstract locality hypothesis; evidence is model-specific. |
| Z-matrix sign structure (S1) | Repo-certified (framework statement); evidence TDC | `docs/theorems/framework/S1_structural_zmatrix_theorem.md`; motif lemmas; `src/network_potential_engine/scripts/check_S1_motif_cross_partials.py`; `tests/test_S1_motif_cross_partials_tdc.py` | S1 notes remaining gap: taxonomy/grammar compliance beyond model evidence. |
| Strict diagonal dominance (S2) | Repo-certified (framework statement); evidence TDC | `docs/theorems/framework/S2_structural_diagonal_dominance_theorem.md`; `src/network_potential_engine/scripts/check_S2_row_dominance_tdc.py`; `tests/test_S2_row_dominance_tdc.py` | |
| M-matrix conclusion (S3) | Mixed: repo theorem + classical external | `docs/theorems/framework/S3_structural_mmatrix_theorem.md`; `src/network_potential_engine/scripts/check_S3_mmatrix_tdc.py`; `tests/test_S3_mmatrix_tdc.py` | Uses classical external facts (Levy–Desplanques; M-matrix sufficient condition). |
| Response identity (C1) | Repo-certified | `docs/theorems/framework/C1_equilibrium_response_theorem.md`; `src/network_potential_engine/scripts/check_C1_tdc_equilibrium_response_identity.py`; `tests/test_C1_tdc_equilibrium_response_identity.py` | |
| Inverse positivity (D1) | Mixed: repo theorem + classical external | `docs/theorems/framework/D1_inverse_positivity_theorem.md`; `src/network_potential_engine/scripts/check_D1_tdc_inverse_positivity.py`; `tests/test_D1_tdc_inverse_positivity.py` | M-matrix theorem is classical external. |
| Mixed-block positivity (D2) | Repo-certified (interface); model-specific content in instantiation | `docs/theorems/framework/D2_mixed_block_positivity_theorem.md`; `src/network_potential_engine/scripts/check_D2_tdc_mixed_block_positivity.py`; `tests/test_D2_tdc_mixed_block_positivity.py` | D2 is formulated as an interface theorem. |
| Response positivity (D3) | Repo-certified | `docs/theorems/framework/D3_response_positivity_theorem.md`; `src/network_potential_engine/scripts/check_D3_tdc_response_positivity.py`; `tests/test_D3_tdc_response_positivity.py` | |
| Explicit admissible region (E1) | Repo-certified (framework definition); evidence TDC | `docs/theorems/framework/E1_explicit_admissible_region_theorem.md`; `src/network_potential_engine/theorem/tdc_region.py`; `tests/test_tdc_region.py` | E1 defines region abstractly; TDC provides explicit \(\mathcal R\). |
| Segment/path certificate (E2) | Repo-certified (framework lemma); evidence TDC | `docs/theorems/framework/E2_segment_path_certification_lemma.md`; `src/network_potential_engine/theorem/tdc_segment.py`; `tests/test_tdc_segment.py` | |
| Local weak ordering (E3) | Repo-certified (framework theorem); evidence TDC | `docs/theorems/framework/E3_local_weak_ordering_theorem.md`; `src/network_potential_engine/scripts/check_E3_tdc_local_weak_ordering.py`; `tests/test_E3_tdc_local_weak_ordering.py` | |

## H. Notation Audit

| Symbol | Meaning | First source location | Risks / ambiguities |
|---|---|---|---|
| \(F(w,\theta)\) | equilibrium operator \(\nabla_w\Phi\) | `docs/foundations/core_objects.md` | Must ensure every theorem uses the same definition. |
| \(H(w,\theta)\) | state Hessian \(\nabla^2_{ww}\Phi\) | `docs/foundations/core_objects.md`; B1 | Some docs abbreviate \(H(\theta)\) implicitly. |
| \(C(w,\theta)\) vs \(C(\theta)\) | coupling operator vs equilibrium/model shorthand | `docs/foundations/core_objects.md`; `docs/theorems/framework/B1_hessian_coupling_theorem.md` | Must preserve the discipline: \(C(\theta)\) is shorthand only in defined regimes. |
| “A3” | ambiguous: regularity vs nondegeneracy | various (E1/E3 setup lines) | Several framework docs still say “A2/A3/C1” rather than “A2/A3b/C1” and omit A3a explicitly. |

## I. Boundary of Safe Claims

- Claims safe to present as theorem/proposition:
  - The A1–E3 framework chain **as stated in the repo theorem documents**, with each interface theorem taken at its stated scope.
- Claims safe only as remarks:
  - The structural S-layer as a **sufficient-condition architecture** (S1–S3) feeding D1.
  - The TDC instantiation as a concrete certification target.
- Claims that must be labelled conjecture/open problem/research:
  - Any claim that requires an A3a theorem statement in docs (currently missing), or any claim that extends S1/S2 admissibility/taxonomy beyond what is currently specified.

## J. Inputs still missing

- missing theorem docs:
  - `A3a — Equilibrium regularity` theorem doc under `docs/theorems/framework/` (no file found).
- missing implementation evidence:
  - None for TDC instantiation of the existing chain; scripts/tests exist.
- missing tests:
  - None for the TDC instantiation of the existing chain.
- missing external citations:
  - Explicit citation targets for classical matrix results used in S3/D1 (Levy–Desplanques; M-matrix theory).
- unresolved notation issues:
  - Remove residual “A3” ambiguity in E-layer setup lines (should explicitly reference A3b and/or A3a where intended).
