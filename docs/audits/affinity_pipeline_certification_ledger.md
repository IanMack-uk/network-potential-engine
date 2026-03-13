# Affinity Pipeline Certification Ledger

**Purpose**

This document maps each stage of the **Affinity data‑driven pipeline
audit** to its verification mechanism in the repository implementation.

It mirrors the structure used in the TDC theorem certification ledger:

    docs/theorems/tdc/tdc_certification_ledger.md

but applies it to the **pipeline audit side** of the repository rather
than the formal theorem side.

The goal is to clarify exactly **how each stage of the Affinity pipeline
is verified**, and what kind of verification is being performed.

This ledger therefore distinguishes between:

-   **Audited identities** --- arithmetic or algebraic identities
    verified directly.
-   **Certified sufficient conditions** --- analytic conditions whose
    verification implies the claim.
-   **Instance witnesses** --- checks performed on a concrete dataset or
    pipeline run.
-   **Proof‑only items** --- conceptual or theorem‑side claims
    referenced but not verified in the pipeline code.

The Affinity pipeline should be interpreted primarily as a **data‑driven
audit and deterministic replay system**, not a formal theorem prover.

------------------------------------------------------------------------

# Verification Mode Legend

  -----------------------------------------------------------------------
  Verification mode                   Meaning
  ----------------------------------- -----------------------------------
  **Audited identity**                Exact arithmetic or algebraic
                                      identity verified via
                                      reconstruction or residual checks.

  **Certified sufficient condition**  Analytic structural condition whose
                                      verification implies the claim.

  **Instance witness**                A concrete dataset instance where
                                      premises and conclusions are
                                      observed numerically.

  **Proof‑only**                      Conceptual or theorem‑level claim
                                      not implemented as executable
                                      verification.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Affinity Pipeline Certification Ledger

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Pipeline stage /     Claim type       Mathematical   Computational    Verification   Code anchor                                            Evidence       Remaining gap
  audit item                            status         status           mode                                                                  artifact       
  -------------------- ---------------- -------------- ---------------- -------------- ------------------------------------------------------ -------------- ------------------
  Node set ingestion   representation   exact          data‑check       audited        `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    add schema
                                                                       identity                                                              `artifacts/`   documentation
                                                                                                                                           `n50/student_registry_v1.json`,
                                                                                                                                           `n50/data_driven_full_audit_transcript_v2.txt`

  Directed tie         representation   exact          data‑check       audited        `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    add structural
  ingestion                                                             identity                                                              `artifacts/`   validation script
                                                                                                                                           `n50/tie_strengths_w_v2.json`,
                                                                                                                                           `n50/data_driven_full_audit_transcript_v2.txt`

  Node attribute       representation   exact          data‑check       audited        `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    document attribute
  ingestion                                                             identity                                                              `artifacts/`   schema
                                                                                                                                           `n50/observations_v2.json`,
                                                                                                                                           `affinity/from_neo4j/n50_student_personal_properties.json`,
                                                                                                                                           `n50/data_driven_full_audit_transcript_v2.txt`

  Ordinal‑to‑numeric   preprocessing    sufficient     numeric          instance       `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    formalize encoding
  encoding             rule                            reconstruction   witness                                                               `artifacts/`   policy
                                                                                                                                           `n50/observations_v2.json`,
                                                                                                                                           `n50/data_driven_full_audit_transcript_v2.txt`

  Source score         arithmetic       exact          numeric          audited        `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    none
  computation (s_i =   identity                        reconstruction   identity                                                              `artifacts/`   
  (Q_i P_i)/9)                                                                                                                                           `n50/source_vector_s_v2.json`,
                                                                                                                                                          `n50/data_driven_full_audit_transcript_v2.txt`

  Tie symmetrisation   preprocessing    sufficient     numeric          instance       `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    document symmetry
  rule                 rule                            reconstruction   witness                                                               `artifacts/`   policy
                                                                                                                                           `n50/tie_strengths_w_v2.json`,
                                                                                                                                           `n50/data_driven_full_audit_transcript_v2.txt`

  Weighted adjacency   arithmetic       exact          numeric          audited        `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    add analytic
  construction         identity                        reconstruction   identity                                                              `artifacts/`   description
                                                                                                                                           `n50/tie_strengths_w_v2.json`,
                                                                                                                                           `n50/data_driven_full_audit_transcript_v2.txt`

  Laplacian            algebraic        exact          numeric          audited        `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    none
  construction (L =    identity                        reconstruction   identity                                                              `artifacts/`   
  D - A)                                                                                                                                           `n50/tie_strengths_w_v2.json`,
                                                                                                                                                          `n50/data_driven_full_audit_transcript_v2.txt`

  Coupling operator (C algebraic        exact          numeric          audited        `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    link to
  = I + αL + εI)       identity                        reconstruction   identity                                                              `artifacts/`   theorem‑side
                                                                                                                                                            operator
                                                                                                                                                            interpretation
                                                                                                                                           `n50/coupling_operator_C_v2.json`,
                                                                                                                                           `n50/data_driven_full_audit_transcript_v2.txt`

  Linear propagation   linear system    exact          numeric check    audited        `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    add
  solve (C v = s)      identity                                         identity                                                                             condition‑number
                                                                                                                                                             logging
                                                                                                                                           `artifacts/`   
                                                                                                                                           `n50/propagated_value_v_v2.json`,
                                                                                                                                           `n50/data_driven_full_audit_transcript_v2.txt`

  Propagation residual solver           exact          numeric check    audited        `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    none
  verification         correctness                                      identity                                                              `artifacts/`   
                                                                                                                                           `n50/data_driven_full_audit_transcript_v2.txt`

  Node energy (E = s + arithmetic       exact          numeric          audited        `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    none
  v)                   identity                        reconstruction   identity                                                              `artifacts/`   
                                                                                                                                           `n50/node_energy_E_v2.json`,
                                                                                                                                           `n50/data_driven_full_audit_transcript_v2.txt`

  Receptivity mapping  arithmetic       exact          numeric          audited        `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    document parameter
  (ṽ = ρ ⊙ v)          identity                        reconstruction   identity                                                              `artifacts/`   source
                                                                                                                                           `n50/data_driven_full_audit_transcript_v2.txt`

  Effective energy     arithmetic       exact          numeric          audited        `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    none
  (E_eff = s + ρ ⊙ v)  identity                        reconstruction   identity                                                              `artifacts/`   
                                                                                                                                           `n50/node_energy_E_eff_v2.json`,
                                                                                                                                           `n50/data_driven_full_audit_transcript_v2.txt`

  Ranking / top‑k      deterministic    witness        numeric check    instance       `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    document tie‑break
  export               ordering                                         witness                                                               `artifacts/`   policy
                                                                                                                                           `n50/app_facing_outputs_v2.json`,
                                                                                                                                           `n50/data_driven_full_audit_transcript_v2.txt`

  Artifact existence   structural       sufficient     data‑check       certified      `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    expand validation
  and schema checks    validation                                       sufficient                                                            `artifacts/`   coverage
                                                                        condition                                                                 `n50/data_driven_full_audit_transcript_v2.txt`

  End‑to‑end pipeline  deterministic    witness        numeric‑check    instance       `check_affinity_n50_full_pipeline_v2_data_driven.py`   `affinity/`    add
  replay               replay                                           witness                                                               `artifacts/`   reproducibility
                                                                                                                                                            harness
                                                                                                                                           `n50/data_driven_full_audit_transcript_v2.txt`,
                                                                                                                                           `n50/full_pipeline_transcript_v2.txt`

  Equilibrium          conceptual       proof‑only     not implemented  proof‑only     theorem documentation                                  none           requires
  interpretation of    mapping                                                                                                                               theorem‑side
  ranking                                                                                                                                                    linkage
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

# Pipeline Dependency Structure

The Affinity pipeline follows the computational structure:

    attributes / ties
            ↓
    source score s
            ↓
    coupling operator C
            ↓
    solve C v = s
            ↓
    energy E = s + v
            ↓
    effective energy E_eff = s + ρ ⊙ v
            ↓
    ranking / export

This structure corresponds to the computational propagation architecture
used by the repository's network‑potential engine.

------------------------------------------------------------------------

# Interpretation

The Affinity pipeline certification operates at three levels:

### 1. Audited identities

Exact arithmetic relationships verified through deterministic
reconstruction:

Examples:

-   source score formula
-   Laplacian construction
-   coupling operator construction
-   propagation linear system
-   energy and effective‑energy formulas

These are the strongest guarantees in the pipeline audit.

------------------------------------------------------------------------

### 2. Certified sufficient conditions

Structural checks that imply correctness of certain pipeline stages.

Examples:

-   artifact schema validation
-   structural checks of adjacency and Laplacian properties

These provide analytic guarantees but do not prove full theoretical
results.

------------------------------------------------------------------------

### 3. Instance witnesses

Many pipeline checks are **instance‑level validations** on a specific
dataset (e.g., the `n50` dataset).

Examples:

-   ranking outputs
-   propagation results
-   full pipeline replay

These demonstrate the pipeline behavior but do not prove universal
properties of the framework.

------------------------------------------------------------------------

# Current Certification Boundary

The Affinity pipeline certification ledger documents the current
verification boundary of the data‑driven audit stack.

Its strongest guarantees are:

-   exact arithmetic reconstruction of exported values
-   deterministic replay of the propagation computation
-   artifact consistency across pipeline stages

Broader interpretations---such as equilibrium semantics, comparative
statics, dynamic evolution, or universality---remain **theorem‑side
matters** unless explicitly re‑verified within pipeline code.

------------------------------------------------------------------------

# Relationship to Theorem‑Side Certification

The theorem‑side certification ledger is documented in:

    docs/theorems/tdc/tdc_certification_ledger.md

Together, the two ledgers provide complementary coverage:

  Ledger                         Scope
  ------------------------------ -----------------------------
  **TDC certification ledger**   formal theorem verification
  **Affinity pipeline ledger**   data‑driven pipeline audit

This dual‑ledger structure ensures that the repository's **theoretical
claims and computational pipeline** can both be audited transparently.
