# P14 — Comparative Statics Layer

## Purpose

This step-level anchor records the comparative-statics implication chain used in the framework.

It introduces no new proofs. It only points to the repo-certified theorem documents and the certified chain transcript.

------------------------------------------------------------------------

## Layer claim (comparative statics via factorisation and sign control)

Fix a parameter value `θ` on a regime where an interior equilibrium branch `w*(θ)` is licensed and the response identity applies.

Under the response identity of **C1**,

`D_θ w*(θ) = C(θ)^{-1} H_{wθ}(w*(θ), θ)`,

and the two sign hypotheses exported by **D1** and **D2**,

- `C(θ)^{-1} ≥ 0` entrywise, and
- `H_{wθ}(w*(θ), θ) ≥ 0` entrywise,

the response-positivity conclusion of **D3** follows:

- `D_θ w*(θ) ≥ 0` entrywise.

In words: **comparative statics positivity** is obtained by combining the factorised response identity with inverse-positivity and mixed-block-positivity.

------------------------------------------------------------------------

## Canonical anchors

- Response identity:
  - `docs/theorems/framework/C1_equilibrium_response_theorem.md`
- Inverse positivity component:
  - `docs/theorems/framework/D1_inverse_positivity_theorem.md`
- Mixed-block positivity component:
  - `docs/theorems/framework/D2_mixed_block_positivity_theorem.md`
- Response positivity conclusion:
  - `docs/theorems/framework/D3_response_positivity_theorem.md`

------------------------------------------------------------------------

## Certified chain transcript (computational evidence)

The chain is exercised end-to-end by:

- `src/network_potential_engine/scripts/check_comparative_statics_chain.py`
