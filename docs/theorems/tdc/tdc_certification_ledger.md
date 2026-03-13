
# TDC Certification Ledger

Purpose: map each formal item in
`docs/theorems/tdc/tdc_local_ordering_theorem_formal.md`
to its verification mode in the implementation.

This document distinguishes between:

- Formal theorem items
- Symbolic audits (identities)
- Certified sufficient conditions
- Instance witnesses
- Proof-only items

---

## Verification Mode Legend

| Verification mode | Meaning |
|---|---|
| Audited identity | Symbolic equality verified via residual checks |
| Certified sufficient condition | Analytic condition verified implying the theorem |
| Instance witness | Numeric example confirming premises and conclusion |
| Proof-only | Present in theorem docs but not implemented in code |

---

## Certification Ledger

| Formal item | Logical role | Claim type | Mathematical status | Repository verification status | Verification mode | Code anchor | Evidence artifact | Remaining gap |
|---|---|---|---|---|---|---|---|---|
| Prop 1 — TDC potential | Identity | object definition | exact | symbolic audit | symbolic audit (identity) | `symbolic/potential.py` | symbolic construction | none |
| Prop 2 — equilibrium operator | Identity | algebraic identity | exact | symbolic audit | symbolic audit (identity) | `check_A2_tdc_equilibrium_existence.py` | script output | none |
| Prop 3 — Hessian | Identity | derivative identity | exact | symbolic audit | symbolic audit (identity) | `symbolic/hessian.py` | residual checks | none |
| Prop 4 — mixed derivative block | Identity | derivative identity | exact | symbolic audit | symbolic audit (identity) | `symbolic/mixed_derivatives.py` | symbolic construction | none |
| Prop 5 — affine equilibrium w*=C^{-1}θ | Identity | algebraic identity | exact | symbolic audit | symbolic audit (identity) | `check_A2_tdc_equilibrium_existence.py` | script output | none |
| Prop 6 — response identity | Identity | algebraic identity | exact | symbolic audit | symbolic audit (identity) | `check_C1_tdc_equilibrium_response_identity.py` | residual check | none |
| Lemma 7 — Z-matrix structure | Premise check | sign structure | sufficient | analytic-check | certified sufficient condition | `check_S1_motif_cross_partials.py` | script output | none |
| Lemma 8 — diagonal dominance | Premise check | inequality condition | sufficient | analytic-check | certified sufficient condition | `check_S2_row_dominance_tdc.py` | margin logs | none |
| Corollary — M-matrix property | Premise check | structural theorem | sufficient | analytic-check | certified sufficient condition | `check_S3_mmatrix_tdc.py` | artifact JSON | none |
| Lemma — inverse positivity | Instance corroboration | matrix property | sufficient | numeric-check | instance witness | `check_D1_tdc_inverse_positivity.py` | script output | analytic generalisation |
| Lemma — mixed-block positivity | Premise check | inequality condition | sufficient | analytic+numeric | certified sufficient condition | `check_D2_tdc_mixed_block_positivity.py` | script output | region-wide analytic verification |
| Corollary — response positivity | Instance corroboration | monotonicity | sufficient | numeric-check | instance witness | `check_D3_tdc_response_positivity.py` | script output | analytic upgrade |
| Definition — admissible region | Premise check | set definition | exact | analytic-check | certified sufficient condition | `theorem/tdc_region.py` | region evaluation | none |
| Proposition — positivity on region | Premise check | inequality theorem | sufficient | analytic+numeric | certified sufficient condition | `check_E1_tdc_region.py` | script output | expand analytic bounds |
| Lemma — segment containment | Premise check | path condition | exact | analytic-check | certified sufficient condition | `theorem/tdc_segment.py` | script output | none |
| Theorem 17 — segment-certified monotonicity | Terminal theorem | monotonicity | formal theorem | numeric-check | instance witness | `check_E3_tdc_local_weak_ordering.py` | script output | region-wide certification |
| End-to-end workflow | Deterministic replay check | theorem composition | sufficient | analytic+numeric | instance witness | `check_tdc_full_workflow.py` | workflow transcript | stronger region coverage |

---

## Dependency Structure

A1
↓
A2 → A3b
↓
C1
↓
D1 ← S3 ← S2 ← S1
↓
D2
↓
D3
↓
E1 → E2 → E3

---

## Summary

The TDC theorem implementation uses three verification modes:

1. Audited identities (symbolic equality checks)
2. Certified sufficient conditions (analytic structural checks)
3. Instance witnesses (representative numeric demonstrations)

This ledger clarifies the correspondence between the formal theorem and the repository implementation.
