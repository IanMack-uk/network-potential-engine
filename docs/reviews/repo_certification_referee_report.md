# Referee Report: Certification Architecture Review

**Role assumed:** Senior Professor of Applied Mathematics specialising
in optimisation theory, operator theory, equilibrium analysis, and
theorem certification.

**Scope of review:**

-   TDC theorem document
-   TDC certification ledger
-   Certification framework
-   Verification boundary document
-   Affinity pipeline certification ledger
-   Affinity n=50 pipeline audit and debrief

This report evaluates the repository **as a mathematical programme and
certification architecture**, not merely as documentation.

------------------------------------------------------------------------

# Executive Summary

The repository exhibits an unusually strong **verification
architecture** compared with typical research codebases. The
documentation explicitly separates:

1.  Formal mathematical results\
2.  Certification ledgers mapping claims to evidence\
3.  Executable verification scripts\
4.  Pipeline execution artifacts

This layered structure significantly improves auditability and
reproducibility.

However, the repository currently contains **two certified islands**:

-   a **formal theorem island** (TDC monotonicity / equilibrium
    structure),
-   a **deterministic replay island** (Affinity pipeline execution and
    artifact verification).

The **bridge between these two layers is not yet mathematically
certified**.\
This is the principal architectural gap.

The repository should therefore currently be described as:

> A rigorous verification-oriented mathematical software repository with
> a strong theorem layer and a strong deterministic replay layer, but an
> incomplete theorem--pipeline semantic bridge.

------------------------------------------------------------------------

# Major Issues (Required Revisions)

## 1. Missing theorem--pipeline semantic bridge

The repository lacks a formally specified mapping between the theorem
objects and the pipeline implementation.

Required clarification:

-   What pipeline object corresponds to the equilibrium variable
    (w\^\*)?
-   What matrix corresponds to (C)?
-   What pipeline elements correspond to:
    -   \(s\)
    -   \(v\)
    -   \(E\)
    -   (E\_{eff})

Each mapping must be classified as:

  Mapping type                Meaning
  --------------------------- -----------------------------------------
  Identity                    mathematically identical object
  Implementation equivalent   algorithmically equivalent construction
  Modelling interpretation    conceptual interpretation
  Not yet implemented         conceptual only

Without this bridge, monotonicity theorems cannot be claimed to apply to
pipeline rankings.

------------------------------------------------------------------------

## 2. Regularity assumption missing in the theorem document

The response identity uses derivatives of (w\^\*(θ)).

However, the differentiability of (w\^\*(θ)) is not explicitly
justified.

Add a proposition:

> **Smoothness of the equilibrium map.**\
> If (C(θ)) is smooth in (θ) and nonsingular on region (R), then
>
> \[ w\^\*(θ) = C(θ)\^{-1} θ \]
>
> is smooth on (R).

This follows directly from the implicit function theorem.

------------------------------------------------------------------------

## 3. Local ordering theorem is actually segment-conditional

The theorem currently titled:

> Local ordering theorem on the admissible region

actually requires the entire segment between two points to remain inside
the admissible region.

Recommended rename:

-   **Segment-certified monotonicity theorem**
-   **Pathwise local ordering theorem**

This prevents misunderstanding about global monotonicity.

------------------------------------------------------------------------

## 4. Certification terminology should be tightened

The repository currently mixes several types of evidence:

  -----------------------------------------------------------------------
  Evidence type                       Meaning
  ----------------------------------- -----------------------------------
  Formal theorem                      mathematically proven statement

  Certified sufficient condition      verifiable premises implying a
                                      theorem

  Instance witness                    demonstration for a single
                                      parameter instance

  Deterministic replay                reproducible execution of a
                                      pipeline
  -----------------------------------------------------------------------

The term **"certification" should be reserved for**:

-   formal proofs
-   region-complete sufficient condition checks

Instance witnesses should not be described as certification.

------------------------------------------------------------------------

## 5. Pipeline currently validates infrastructure, not modelling claims

The Affinity n=50 audit shows:

-   uniform source scores
-   uniform receptivity
-   ranking dominated by tie-breaking
-   simplified propagation checks

Thus the pipeline run is best interpreted as:

> an infrastructure coherence test rather than substantive model
> validation.

This caveat should appear earlier in the documentation.

------------------------------------------------------------------------

# Medium Priority Improvements

## 1. Add a "logical role" column to certification ledgers

Each claim should include:

  Role                     Meaning
  ------------------------ --------------------------------
  Identity                 algebraic equality
  Premise check            verifies theorem conditions
  Bridge lemma             connects theorem components
  Terminal theorem         main mathematical result
  Instance corroboration   dataset-specific demonstration

This clarifies the proof dependency graph.

------------------------------------------------------------------------

## 2. Distinguish theorem proofs from implementation verification

For each claim, explicitly separate:

-   **Mathematical status**
-   **Repository verification status**

Example:

    Mathematical status: Formal theorem
    Repository verification: symbolic audit of implementation identity

------------------------------------------------------------------------

## 3. Promote audit caveats into higher-level documentation

Important caveats currently appear only in the pipeline debrief:

-   uniform source score
-   uniform receptivity
-   ranking dominated by tie-breaks

These should also appear in:

-   the certification framework
-   the verification boundary document

------------------------------------------------------------------------

# Technical Hardening Recommendations

## 1. Counterfactual recomputation must re-solve the system

The debrief proposes rerunning propagation with modified parameters.

This is essential.

A proper counterfactual test requires recomputing:

    C v' = s'

rather than adjusting exported scores downstream.

------------------------------------------------------------------------

## 2. Strengthen admissible region certification

The current admissible region is sufficient but conservative.

Future work may include:

-   tighter norm bounds
-   Gershgorin-style refinements
-   structured inverse positivity results

------------------------------------------------------------------------

# Positive Assessment

Despite the issues above, the repository demonstrates several best
practices rarely seen together:

### Strong architectural separation

The project clearly distinguishes:

-   mathematical proofs
-   computational verification
-   pipeline execution

### Transparent certification ledgers

Each claim includes:

-   claim type
-   verification mode
-   code anchor
-   artifact reference
-   remaining gap

### Honest pipeline audit

The pipeline debrief openly states limitations and experimental status.

### Reproducibility orientation

Deterministic replay and artifact verification are integrated into the
pipeline.

------------------------------------------------------------------------

# Final Verdict

The repository represents a **well-designed mathematical verification
programme** with:

-   strong theorem-side structure,
-   strong reproducibility practices,
-   unusually transparent certification documentation.

However, it is **not yet a fully unified certified mathematical
system**.

The missing component is the **formal semantic bridge between theorem
objects and pipeline implementation**.

Once that bridge is explicitly defined and verified, the project could
legitimately claim a fully integrated theorem-to-pipeline certification
framework.

------------------------------------------------------------------------

# Recommended Next Milestone

The next architectural milestone should be a document titled:

**`theorem_pipeline_bridge.md`**

This document should formally define:

1.  the mapping between theorem variables and pipeline objects
2.  which mappings are identities vs interpretations
3.  which monotonicity results transfer to the pipeline
4.  which assumptions are required for that transfer

Completing this bridge would convert the repository from **two certified
islands** into a **single certified mathematical system**.
