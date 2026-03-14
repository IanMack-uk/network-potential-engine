# Repository Certification Framework

## Purpose

This document provides a high‑level overview of the **certification
architecture** used in this repository. It explains how formal
mathematical results and computational pipelines are linked through
explicit certification ledgers.

The repository separates **mathematical theory**, **computational
implementation**, and **verification artifacts** into clearly defined
layers so that each can be audited independently.

Two complementary certification ledgers provide this structure:

-   **Theorem certification ledger**
-   **Pipeline certification ledger**

Together they allow readers to trace claims from theory to executable
verification.

The repository currently has strong evidence in two layers:

- a theorem-side layer (formal statements plus symbolic/analytic checks of identities and sufficient conditions), and
- a pipeline-side layer (deterministic replay and arithmetic audits of exported artifacts).

Pipeline-side evidence may be stored either as the latest outputs under:

- `affinity/artifacts/n50/`

or as a per-run provenance bundle under:

- `affinity/artifacts/n50/snapshots/<run_id>/`

The formal semantic bridge between these layers is documented separately and is not yet complete:
`docs/theorem_pipeline_bridge.md`.

------------------------------------------------------------------------

# High-Level Certification Architecture

The repository organizes verification into three layers:

    formal mathematics
            ↓
    certification ledgers
            ↓
    verification scripts and artifacts

Each layer has a distinct purpose.

  -----------------------------------------------------------------------
  Layer                               Role
  ----------------------------------- -----------------------------------
  **Formal theorem documents**        State mathematical objects,
                                      definitions, and theorems.

  **Certification ledgers**           Map each claim to its verification
                                      mode and code anchor.

  **Verification scripts /            Execute checks and produce evidence
  artifacts**                         supporting the claims.
  -----------------------------------------------------------------------

This separation allows the repository to function both as a **research
artifact** and as an **auditable computational system**.

------------------------------------------------------------------------

# Theorem-Side Certification

Formal theorem material is documented under:

    docs/theorems/tdc/

The primary document is:

    docs/theorems/tdc/tdc_local_ordering_theorem_formal.md

This file contains the mathematical statements for the TDC theorem
chain.

A companion ledger records how each theorem component is verified in
code:

    docs/theorems/tdc/tdc_certification_ledger.md

### What the theorem ledger records

For each formal proposition or lemma it documents:

-   the mathematical claim
-   its verification mode
-   the script or module implementing the check
-   the artifact or transcript containing evidence

Verification modes used in the theorem ledger include:

  -----------------------------------------------------------------------
  Mode                                Meaning
  ----------------------------------- -----------------------------------
  **Audited identity**                Symbolic equality verified via
                                      residual checks.

  **Certified sufficient condition**  Analytic condition implying the
                                      theorem result.

  **Instance witness**                A concrete parameter instance
                                      demonstrating the claim.

  **Proof-only**                      Claim documented but not
                                      implemented as executable
                                      verification.
  -----------------------------------------------------------------------

This ledger therefore provides an explicit bridge between:

    formal theorem
          ↓
    certification ledger
          ↓
    verification script

------------------------------------------------------------------------

# Pipeline-Side Certification

The repository also includes a **data-driven computational pipeline
audit**.

This pipeline is documented through the Affinity certification ledger:

    docs/audits/affinity_pipeline_certification_ledger.md

The pipeline ledger maps **pipeline stages** rather than theorem
statements.

Typical pipeline stages include:

-   attribute ingestion
-   source score construction
-   coupling operator construction
-   propagation solve
-   energy computation
-   ranking export

Each stage is mapped to:

-   the script implementing the step
-   the verification method
-   the artifacts produced by the pipeline

The Affinity pipeline should be interpreted primarily as a
**deterministic replay and arithmetic audit** of exported artifacts
rather than a theorem prover.

In particular, the current audited run should be interpreted conservatively:

- rankings can be substantially driven by deterministic tie-breaks when upstream signals are close to uniform;
- uniform or near-uniform source scores and receptivity reduce substantive interpretability;
- theorem-side monotonicity results do not transfer to pipeline rankings without an explicit, premise-complete bridge.

------------------------------------------------------------------------

# Relationship Between the Two Ledgers

The two certification ledgers cover different aspects of the repository.

  Ledger                         Scope
  ------------------------------ ------------------------------
  **TDC certification ledger**   Formal theorem verification.
  **Affinity pipeline ledger**   Data-driven pipeline audit.

Conceptually they correspond to different verification directions:

    Theory → Code

The theorem ledger verifies that theoretical claims are reflected
correctly in code.

    Code → Artifacts

The pipeline ledger verifies that computational outputs are consistent
with the implemented algorithms.

Together they provide **bidirectional auditability** across the
repository.

However, bidirectional auditability does not by itself constitute theorem-to-pipeline semantic equivalence.
The current theorem–pipeline mapping status is recorded in `docs/theorem_pipeline_bridge.md`.

------------------------------------------------------------------------

# Dependency Overview

The combined certification flow can be visualized as:

    formal theorem
            ↓
    theorem certification ledger
            ↓
    verification scripts

    pipeline execution
            ↓
    pipeline certification ledger
            ↓
    artifacts / audit transcripts

This structure allows readers to independently verify:

-   the correctness of the theoretical framework
-   the correctness of the computational implementation
-   the reproducibility of the exported pipeline results

------------------------------------------------------------------------

# Certification Philosophy

The repository deliberately distinguishes between several levels of
verification strength.

  -----------------------------------------------------------------------
  Verification level                  Description
  ----------------------------------- -----------------------------------
  **Audited identity**                Exact arithmetic or symbolic
                                      equality verified directly.

  **Certified sufficient condition**  Analytic condition guaranteeing
                                      correctness.

  **Instance witness**                Demonstration using a specific
                                      dataset or parameter choice.

  **Proof-only**                      Claim documented but not currently
                                      executable as verification code.
  -----------------------------------------------------------------------

This explicit classification avoids overstating what the computational
checks prove, while still providing strong transparency about the
verification status of each claim.

------------------------------------------------------------------------

# Current Certification Boundary

The repository currently provides strong guarantees for:

-   symbolic identities in the theorem layer
-   structural sufficient-condition checks
-   deterministic replay of the Affinity pipeline
-   artifact consistency across computational stages

Some broader framework interpretations remain theorem-side matters,
including:

-   equilibrium semantics of pipeline outputs
-   comparative statics interpretations
-   dynamic and universality results

These interpretations can be incorporated into computational
certification in future extensions.

------------------------------------------------------------------------

# Summary

The repository uses a **dual-ledger certification framework**:

  -----------------------------------------------------------------------
  Component                           Role
  ----------------------------------- -----------------------------------
  Formal theorem documents            Mathematical definitions and
                                      results

  Theorem certification ledger        Maps theorem statements to
                                      verification scripts

  Pipeline certification ledger       Maps computational pipeline stages
                                      to audit checks

  Scripts and artifacts               Provide executable verification
                                      evidence
  -----------------------------------------------------------------------

This structure allows both the **mathematical theory** and the
**computational implementation** to be audited transparently by external
readers.
