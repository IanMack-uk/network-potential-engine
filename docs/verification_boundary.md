# Verification Boundary & Claims Register

## Purpose

This document defines the **verification boundary** of the repository
and records the verification status of the major claims made across the
theoretical and computational components.

The goal is to clearly distinguish between:

-   **formal mathematical results**
-   **symbolic or computational verification**
-   **deterministic pipeline replay**
-   **instance-level demonstrations**
-   **conceptual interpretations**

This document complements the certification ledgers by providing a
**global classification of repository claims**.

It should be read alongside:

-   `docs/certification_framework.md`
-   `docs/theorems/tdc/tdc_certification_ledger.md`
-   `docs/audits/affinity_pipeline_certification_ledger.md`
-   `docs/theorem_pipeline_bridge.md`

Together these documents define the repository's **verification
architecture**.

------------------------------------------------------------------------

# Categories of Verification

The repository distinguishes several levels of verification strength.

  -----------------------------------------------------------------------
  Category                            Meaning
  ----------------------------------- -----------------------------------
  **Formal theorem**                  Proven mathematically in theorem
                                      documentation.

  **Symbolic verification**           Algebraic identities verified by
                                      symbolic or residual checks in
                                      code.

  **Certified sufficient condition**  Structural analytic condition
                                      verified which implies a result.

  **Deterministic pipeline replay**   Computational results reproducible
                                      exactly by rerunning the pipeline.

  **Instance witness**                Demonstration using a specific
                                      dataset or parameter instance.

  **Conceptual interpretation**       Explanatory or theoretical
                                      interpretation not directly
                                      verified in code.
  -----------------------------------------------------------------------

These categories are used to avoid overstating what the computational
checks prove.

------------------------------------------------------------------------

# Claims Register

The following table records the verification status of the primary
claims implemented or referenced by the repository.

  -----------------------------------------------------------------------------------------
  Claim                   Verification category   Evidence
  ----------------------- ----------------------- -----------------------------------------
  TDC equilibrium         Formal theorem +        `tdc_local_ordering_theorem_formal.md`,
  response identity       symbolic verification   response identity check scripts

  Coupling operator       Symbolic verification   symbolic operator construction checks
  identity (C = -H)                               

  Structural M-matrix     Certified sufficient    S-layer scripts verifying Z-matrix and
  conditions              condition               diagonal dominance

  Segment-certified       Formal theorem +        theorem document and E3 instance-witness
  monotonicity theorem    instance witnesses      scripts
  (TDC model)

  Propagation solve (Cv = Deterministic pipeline  Affinity pipeline audit script
  s) in pipeline          replay                  

  Source score            Symbolic / arithmetic   pipeline reconstruction checks
  computation             verification            

  Energy and              Symbolic / arithmetic   energy reconstruction steps
  effective-energy        verification            
  calculations                                    

  Artifact consistency    Deterministic pipeline  audit transcript and artifact checks
  across pipeline stages  replay                  

  Ranking export          Instance witness        ranking artifact inspection
  correctness                                     

  Equilibrium             Conceptual              theorem-side documentation
  interpretation of       interpretation          
  ranking                                         
  -----------------------------------------------------------------------------------------

------------------------------------------------------------------------

# Verification Coverage

The repository currently provides strong guarantees for:

-   symbolic identities and algebraic relationships
-   structural sufficient-condition checks in the theorem layer
-   deterministic replay of the Affinity pipeline
-   artifact consistency across computational stages

These guarantees ensure that:

1.  the **theoretical identities used by the implementation are
    correct**, and
2.  the **computational pipeline reproduces exported artifacts
    deterministically**.

At present the repository should be understood as having **two strong verified islands**:

- a theorem-side island (formal theorem statements plus symbolic/analytic verification of identities and sufficient conditions), and
- a pipeline-side island (deterministic replay and arithmetic audit of exported artifacts).

The semantic bridge between theorem objects and pipeline objects is documented in
`docs/theorem_pipeline_bridge.md` and is not yet complete.

------------------------------------------------------------------------

# Verification Boundary

Certain broader interpretations remain **outside the current
computational verification boundary**.

For the Affinity pipeline in particular, the current audited run should be interpreted conservatively:

- source-score and receptivity heterogeneity may be limited in the current audited setup, so ranking differences can be substantially driven by deterministic tie-breaks;
- deterministic replay and arithmetic audit demonstrate reproducibility and internal coherence, not theorem proof;
- monotonicity theorems do not apply to pipeline rankings without an explicit, premise-complete theorem–pipeline bridge.

The current mapping status and non-transfer points are recorded in:
`docs/theorem_pipeline_bridge.md`.

Examples include:

-   equilibrium semantics of pipeline ranking outputs
-   comparative statics beyond the TDC model
-   dynamic evolution results
-   universality-layer claims

These remain part of the theoretical framework and are documented in
theorem materials rather than verified directly in pipeline code.

------------------------------------------------------------------------

# Relationship to Certification Ledgers

This document sits above the certification ledgers in the documentation
hierarchy.

  ---------------------------------------------------------------------------------------------
  Document                                                  Role
  --------------------------------------------------------- -----------------------------------
  `docs/theorems/tdc/tdc_certification_ledger.md`           Maps theorem statements to
                                                            verification scripts

  `docs/audits/affinity_pipeline_certification_ledger.md`   Maps pipeline stages to audit
                                                            checks

  `docs/verification_boundary.md`                           Classifies verification status of
                                                            major repository claims
  ---------------------------------------------------------------------------------------------

Together they form a **transparent verification framework**.

------------------------------------------------------------------------

# Repository Verification Structure

The full documentation structure is:

    formal mathematics
            ↓
    theorem certification ledger
            ↓
    verification scripts

    pipeline execution
            ↓
    pipeline certification ledger
            ↓
    artifacts / audit transcripts

The verification boundary document provides a **top-level summary of
what these layers collectively establish**.

------------------------------------------------------------------------

# Summary

The repository uses a **multi-layer certification approach**:

  -----------------------------------------------------------------------
  Layer                               Purpose
  ----------------------------------- -----------------------------------
  Formal theorem documents            Mathematical definitions and
                                      results

  Certification ledgers               Map claims to verification methods

  Verification scripts                Execute computational checks

  Artifacts and transcripts           Provide reproducible evidence

  Verification boundary               Defines scope of what is proven vs
                                      demonstrated
  -----------------------------------------------------------------------

This architecture makes the repository **unusually transparent and
auditable** for external reviewers.
