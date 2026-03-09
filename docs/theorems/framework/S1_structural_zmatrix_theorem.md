# S1 — Structural Z-Matrix Theorem

## Purpose

This theorem exports the **off-diagonal sign structure** of the canonical coupling operator associated with a relational potential.

It exists to support the framework-closure structural layer between:

- B-layer operator construction (`C = −H`), and
- D-layer inverse-positivity arguments (D1), which require Z-matrix structure as part of standard sufficient conditions for M-matrix behaviour.

No claim is made here about diagonal dominance (S2) or nonsingular M-matrix properties (S3).

The Z-matrix sign structure established here is used downstream in S2 (together with magnitude bounds) and then in S3 (together with strict diagonal dominance) to obtain nonsingular M-matrix structure.

------------------------------------------------------------------------

# 1. Setup and canonical objects

All canonical objects and notation are as defined in:

- `docs/foundations/core_objects.md`

Let `Φ(w, θ)` be a relational potential satisfying the regularity assumptions of:

- A1 — Admissible Relational Potential Well-Posedness.

Let `Ω_Φ ⊆ W × Θ` denote the admissible potential domain on which `Φ` is defined.

Assume `Φ ∈ C²_w(Ω_Φ)` so that the Hessian exists on `Ω_Φ`.

------------------------------------------------------------------------

# 2. Hessian and coupling operator

Define the Hessian (B1):

`H(w, θ) := ∇²_{ww} Φ(w, θ)`.

Define the coupling operator (B1):

`C(w, θ) := −H(w, θ)`.

------------------------------------------------------------------------

# 3. Smooth-domain scope

All claims in this theorem are understood on `Ω_Φ` under the regularity hypothesis `Φ ∈ C²_w(Ω_Φ)` (A1).

If the admissible domain includes boundary points at which second derivatives fail to exist, then the theorem is understood as applying on the subset of `Ω_Φ` where the second partial derivatives `∂²Φ/(∂w_i ∂w_j)` exist.

No new canonical set notation is introduced for this restriction.

------------------------------------------------------------------------

# 4. Decomposition hypothesis (motif-local form)

Assume the potential admits a finite decomposition into local terms of the form:

`Φ(w, θ) = Σ_{e ∈ E} φ_e(w_e, θ) + Σ_{m ∈ M} ψ_m(w_{S_m}, θ)`,

where each `S_m ⊆ {1, …, n}` is a finite coordinate subset and `w_{S_m}` denotes the subvector of `w` indexed by `S_m`.

This decomposition is a structural hypothesis. The framework must separately define what constitutes an admissible local term and what motif classes are permitted.

These framework-level definitions are specified in:

- `docs/foundations/admissible_motif_taxonomy.md`.

The corresponding construction rule specifying which potentials are framework-admissible is given in:

- `docs/foundations/admissible_potential_grammar.md`.

------------------------------------------------------------------------

# 5. Theorem statement (Z-matrix sign pattern)

Assume that for every motif term `ψ_m` and every pair of distinct indices `i ≠ j`:

`∂²ψ_m/(∂w_i ∂w_j) ≥ 0`

holds on `Ω_Φ` (interpreting the derivative as `0` whenever `{i, j} ⊄ S_m`).

Then for every `(w, θ) ∈ Ω_Φ` and every pair of distinct indices `i ≠ j`:

1. `H_{ij}(w, θ) = ∂²Φ/(∂w_i ∂w_j) ≥ 0`.
2. `C_{ij}(w, θ) ≤ 0`.

Therefore `C(w, θ)` is a **Z-matrix** on `Ω_Φ`.

------------------------------------------------------------------------

# 6. Pilot motif workflow note (development discipline)

This theorem is intended to be certified using a motif-based workflow:

1. Write `Φ` as a sum of motif-local terms.
2. Compute off-diagonal state cross-partials for each term.
3. Group terms into a small number of motif classes (proof-organisation constraint).
4. Prove one sign lemma per class.
5. Conclude with a summation/globalisation step.

Pilot implementations may use model-defined semantic groupings as a proxy for motifs to generate auditable cross-partial sign tables.

------------------------------------------------------------------------

# 7. Proof skeleton

1. **Termwise differentiation**

   By the decomposition hypothesis, `Φ` is a finite sum of local terms. Under `Φ ∈ C²_w(Ω_Φ)` (A1), the second partial derivatives with respect to `w` exist and the Hessian entries satisfy termwise additivity:

   `H_{ij}(w, θ) = Σ_{e ∈ E} ∂²φ_e/(∂w_i ∂w_j) + Σ_{m ∈ M} ∂²ψ_m/(∂w_i ∂w_j)`.

2. **Off-diagonal sign control**

   For `i ≠ j`, edge-local terms do not contribute to cross-partials between distinct coordinates (S1L1).

   For admissible interaction and closure motifs, the required cross-partial sign inequalities are certified by the motif sign lemmas indexed in:

   - `docs/theorems/framework/S1_motif_sign_lemmas.md`.

   Therefore `H_{ij}(w, θ) ≥ 0` for all `i ≠ j`.

3. **Coupling operator sign conclusion**

   By definition (B1), `C(w, θ) = −H(w, θ)`. Hence for `i ≠ j`,

   `C_{ij}(w, θ) = −H_{ij}(w, θ) ≤ 0`.

4. **Z-matrix conclusion**

   By definition, `C(w, θ)` is a Z-matrix.

------------------------------------------------------------------------

# 8. Explicit dependency audit

This theorem depends only on:

- A1 — Admissible Relational Potential Well-Posedness (licenses `Φ ∈ C²_w(Ω_Φ)` and existence of Hessian entries)
- B1 — Hessian–Coupling Theorem (defines `H(w, θ)` and `C(w, θ) = −H(w, θ)` and fixes the notational scope)
- S1L1 — Edge-Local Terms Have Zero Off-Diagonal Cross-Partials (`docs/theorems/framework/S1L1_edge_local_offdiagonal_zero.md`)
- S1L2 — Pairwise Interaction Motifs Have Nonnegative Off-Diagonal Cross-Partials (`docs/theorems/framework/S1L2_interaction_cross_partials_nonnegative.md`)
- S1L3 — Triadic Closure Product Motifs Have Nonnegative Off-Diagonal Cross-Partials (`docs/theorems/framework/S1L3_closure_cross_partials_nonnegative.md`)

This theorem does not depend on equilibrium existence, response theory, or ordering theorems.

------------------------------------------------------------------------

# 9. Computational evidence (supporting)

The codebase contains a pilot semantic grouping and sign-table pipeline for the TDC instantiation that certifies the intended Z-matrix sign pattern at the symbolic level.

- Pilot motif analysis module:
  - `src/network_potential_engine/symbolic/motif_analysis.py`
    - `decompose_tdc_into_pilot_groups`
    - `build_cross_partial_report_for_groups`
    - `write_report_json`

- Check script (writes an auditable JSON artifact):
  - `src/network_potential_engine/scripts/check_S1_motif_cross_partials.py`
  - artifact output:
    - `docs/artifacts/S1/tdc_motif_cross_partials.json`

- Pytest regression coverage:
  - `tests/test_S1_motif_cross_partials_tdc.py`

These artifacts are supporting evidence for the development workflow and are not, by themselves, a certified replacement for a framework-level motif taxonomy and sign lemmas.

------------------------------------------------------------------------

# 10. Remaining gap to full proof

To certify this theorem at the framework level (beyond model-specific evidence), the following items must be completed:

1. **Authoritative framework admissibility specification**
   - Maintain the admissible motif taxonomy and admissible potential grammar at the framework level.

2. **Model instantiation compliance**
   - Ensure that each model instantiation’s `Φ` is constructed from, or decomposes into, the admitted term families.

3. **(Optional) Locality bookkeeping**
   - Use B2-style locality structure to describe which off-diagonal entries can be nonzero, to support S2-style row-sum bounds.
