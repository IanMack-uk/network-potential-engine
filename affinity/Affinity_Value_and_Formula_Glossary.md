# Affinity — Value and Formula Glossary (n=50 pipeline)

This file documents the **named values / symbols** used in the current Affinity n=50 research-grade pipeline, along with the **formulas we have frozen** and the points where items are still **policy TBD**.

---

## Index / quick navigation

- Registry and indexing: `V`, `student_id`, `node_index`
- Observations / ties: `O`, `w_ij` (tie strength), `A` (adjacency)
- Source / propagation: `s`, `C`, `G`, `v`
- Energies / scores: `E`, `rho`, `E_eff`
- Export: rankings, explanation fields

---

## Registry and indexing

### `V`

- **Meaning**: Cohort node set (students).
- **Concrete representation**:
  - `affinity/artifacts/n50/static/registry/student_registry_v1.json`
- **Notes**:
  - All vectors and operators are expressed in **`node_index` ascending** order.

### `student_id`

- **Meaning**: Stable unique student identifier.
- **Representation**:
  - string URN, e.g. `urn:qc:person:ulid:...`

### `node_index`

- **Meaning**: Stable integer index in `[0, n-1]` defining the ordering of cohort vectors.
- **Representation**:
  - In registry nodes: `{ "node_index": i, "student_id": ... }`

---

## Observations / ties (upstream model inputs)

### `O` (observations event log)

- **Meaning**: A log of observed interactions (or derived interactions) used to infer student–student relationships.
- **Schema reference**:
  - `affinity/artifacts/n50/static/schemas/observations_schema_v1.json`
- **Canonical fields**:
  - `event_id`
  - `timestamp`
  - `event_type` (currently `interaction`)
  - `actor_student_id`
  - `target_student_id`
  - `weight` (nonnegative)

### `w_ij` (tie strength)

- **Meaning**: Weight of a directed tie from student `i` to student `j`.
- **Where it comes from**:
  - Derived from observations `O` via an aggregation policy.
- **Current status**:
  - **Policy TBD** for v2+.

### `A` (adjacency / weight matrix)

- **Meaning**: A weighted adjacency representation of ties.
- **Where it is used**:
  - As an intermediate to define the network potential `Φ(w, θ)` and the equilibrium computation.
- **Current status**:
  - Not yet frozen in a “real data” sense; the current pipeline uses a simplified baseline potential/operator chain.

---

## Source / propagation

### `x` (node attributes)

- **Meaning**: Per-student attribute bundle (capacities/constraints/etc.).
- **Concrete representation**:
  - `affinity/artifacts/n50/legacy/v1/node_attribute_field_v1.json`
- **Key v1 attribute**:
  - `r` (capacity) (currently constant `1.0` for all nodes)

### `ψ` (source mapping)

- **Meaning**: Policy that maps upstream observations/attributes into the intrinsic source signal.
- **v1 artifact**:
  - `affinity/artifacts/n50/static/specs/source_mapping_psi_v1.txt`
- **Current status**:
  - v1 is a frozen placeholder mapping.

### `s` (source vector)

- **Meaning (app)**: Per-student intrinsic source value signal (value created at that source/person).
- **Representation**:
  - `affinity/artifacts/n50/legacy/v1/source_vector_s_v1.json`
  - Stored as a list of `{student_id, s}` pairs.
- **v1 policy**:
  - `s_i = 1.0` for all students.
- **v2 policy (Option B; intrinsic source value)**:
  - In v2, `s` is treated as a per-student intrinsic source value (value created at that source).
  - Upstream inputs (Neo4j export snapshot):
    - `affinity/from_neo4j/n50_student_personal_properties.json`
    - `outputQuality` in `{very_low, low, medium, high, very_high}`
    - `outputProductivity` in `{very_low, low, medium, high, very_high}`
  - Tier mapping (frozen):
    - `very_low → 1`
    - `low → 2`
    - `medium → 3`
    - `high → 4`
    - `very_high → 5`
  - Definition (frozen):
    - Let `Q_i = tier(outputQuality_i)` and `P_i = tier(outputProductivity_i)`.
    - `s_i = (Q_i * P_i) / 9.0` (so `medium × medium` maps to `s=1.0`).

### `C` (coupling operator)

- **Meaning (math)**: Coupling operator used for propagation; in the framework it corresponds to a Hessian-derived operator from the potential at equilibrium.
- **Representation**:
  - `affinity/artifacts/n50/legacy/v1/coupling_operator_C_v1.json`
- **v1 format**:
  - symmetric tridiagonal.

### `G` (Green operator)

- **Meaning**: The inverse operator `G = C^{-1}` (applied via solves rather than materializing the matrix).
- **Representation**:
  - Policy + diagnostics:
    - `affinity/artifacts/n50/static/specs/green_operator_G_v1_policy.txt`
    - `affinity/artifacts/n50/legacy/v1/green_operator_G_v1_diagnostics.txt`

### `v` (propagated value)

- **Meaning (app)**: Network-propagated component induced by `s` through the cohort network.
- **Definition (frozen)**:
  - `v = G s`
  - equivalently: solve `C v = s`
- **Representation**:
  - `affinity/artifacts/n50/legacy/v1/propagated_value_v_v1.json`
- **Diagnostics**:
  - `affinity/artifacts/n50/legacy/v1/propagated_value_v_v1_residual.txt`

---

## Energies / scores

### `β0`, `β1`

- **Meaning**: Scalar coefficients weighting intrinsic vs network components.
- **v1 frozen values**:
  - `β0 = 1.0`
  - `β1 = 1.0`

### `E` (node energy)

- **Meaning**: A score derived from `s` and `v`.
- **v1 representation**:
  - `affinity/artifacts/n50/legacy/v1/node_energy_E_v1.json`
- **Notes**:
  - In v1, this is computed consistently with the declared parameterization.

### `ρ` / `rho` (receptivity)

- **Meaning (app)**: Per-student multiplier for the network component (how much network propagation affects the final score).
- **v1 policy**:
  - `rho_i = 1.0` for all students.
- **v2 policy (Option B; adopter categories)**:
  - Each student has an `adopterCategory` provided upstream in:
    - `affinity/from_neo4j/n50_student_personal_properties.json`
  - Category values (frozen):
    - `innovator`
    - `early_adopter`
    - `early_majority`
    - `late_majority`
    - `laggard`
  - Cohort distribution (n=50; intended/frozen):
    - `innovator`: 1 student
    - `early_adopter`: 7 students
    - `early_majority`: 17 students
    - `late_majority`: 17 students
    - `laggard`: 8 students
  - Receptivity computation:
    - `rho_i = r(adopterCategory_i)` where `r(·)` is a category-to-scalar mapping.
    - Numeric mapping (frozen):
      - `innovator → 0.90`
      - `early_adopter → 0.95`
      - `early_majority → 1.00`
      - `late_majority → 1.05`
      - `laggard → 1.10`
- **Representation**:
  - Stored in `affinity/artifacts/n50/legacy/v1/node_energy_E_eff_v1.json`.

### `E_eff` (effective energy / canonical score)

- **Meaning (app)**: Final canonical ranking score.
- **Definition (frozen in v1)**:
  - `E_eff = β0 * s + β1 * (rho ⊙ v)`
  - where `⊙` denotes elementwise multiplication.
- **Representation**:
  - `affinity/artifacts/n50/legacy/v1/node_energy_E_eff_v1.json`
- **Canonical score declaration**:
  - `affinity/artifacts/n50/legacy/v1/node_energy_canonical_score_v1.txt`

---

## Export

### Rankings

- **Meaning**: Sorted list of students by canonical score.
- **v1 export**:
  - `affinity/artifacts/n50/legacy/v1/app_facing_outputs_v1.json`
- **v1 sorting policy (frozen)**:
  - sort key: `(-score, node_index)`
  - score: `E_eff`

### Explanations

- **Meaning**: Per-student decomposition used for app display.
- **v1 explanation fields**:
  - `intrinsic_component`
  - `network_component`
  - plus a formula string

---

## Counterfactuals (what-if analysis)

### Counterfactual input

- **Meaning**: A hypothetical change to an upstream input (e.g., `s` or `rho`) to simulate “what if we intervene?”.
- **Minimal counterfactual (definition)**:
  - choose a modified source vector `s'` (e.g., boost one student’s `s_i`)

### Counterfactual recomputation levels

- **Level 0 (export-only)**:
  - change `E_eff` without recomputing upstream values.
  - Useful for UI harnessing only.
- **Level 1 (propagation-consistent)**:
  - recompute `v'` by solving `C v' = s'`.
  - recompute `E_eff'`.
  - This is the “realistic counterfactual” path.

---

## Option B (v2) toy realism signals (policy-in-progress)

These items are not part of v1, but are being defined as a deterministic mock realism layer.

### Attendance propensity `a_i`

- **Meaning**: Per-participation attendance probability (stored on `Participation` as `attendance_probability_score`).
- **Status**: Implemented in Neo4j (authoritative) as a band/attribute-driven baseline plus interest and wellbeing offsets.
- **Notes**:
  - The baseline includes offsets from `Person.reliabilityBand`, `Person.initiativeBand`, `Person.openToCollaborate`, `Person.openToWork`.
  - Wellbeing offsets include:
    - `Person.lifeStabilityLsb` (LSB): larger attendance offset.
    - `Person.lifeSatisfactionLsf` (LSF): smaller “mood / engagement” offset.
  - Per-module interest weight is applied multiplicatively to the baseline probability.
  - Coefficients (frozen):
    - `k_lsb = 0.06`
    - `k_lsf = 0.02`
    - `k_interest = 0.15`
  - Definitions (frozen):
    - `life_off = k_lsb * ((coalesce(lifeStabilityLsb, 5.5) - 5.5) / 4.5)`
    - `mood_off = k_lsf * ((coalesce(lifeSatisfactionLsf, 5.5) - 5.5) / 4.5)`
    - `a_raw = 0.55 + rel_off + init_off + collab_off + work_off + life_off + mood_off`
    - `a_i = clamp(a_raw, 0.20, 0.95)`
    - `p_raw = a_i * (1.0 + k_interest * interest)`
    - `attendance_probability_score = clamp(p_raw, 0.0, 1.0)`

### Interest factor `t_{i,m}`

- **Meaning**: Per-student per-module interest strength.
- **Source**:
  - `affinity/from_neo4j/student_module_interest_score.json`
- **Rule (current)**:
  - The Neo4j runbook reads `INTERESTED_IN.weight` for the `(Person)-[:INTERESTED_IN]->(Event)` edge and applies an interest multiplier to the attendance baseline.

---

## References

- Pipeline map:
  - `docs/public_development_plan/Affinity_App_Pipeline_Dependency_Map_n50.md`
- Audit/debrief:
  - `docs/affinity_n50_pipeline_audit_and_debrief.md`
