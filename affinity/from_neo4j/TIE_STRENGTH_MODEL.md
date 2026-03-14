# Tie strength + tie type model (Neo4j authoritative)

This document describes exactly how tie strength (`tie_strength_total`) and tie classification (`tie_type`) are computed in Neo4j, and how the exports are converted into directed weights `w_ij` for the v2 Option B artifact generator.

## Graph entities (authoritative)

- `(:Person)`
  - `id` is the stable identifier (e.g. `urn:qc:person:ulid:...`) and is treated as the **student_id** in the artifact pipeline.
  - `displayName` is human-readable only.

- `(:Person)-[s:IS_SIMILAR_TO]-(:Person)` (undirected)
  - Encodes *time / similarity based* tie evidence.
  - Inputs (already computed upstream):
    - `s.similarity_strength` (scalar)

- `(:Person)-[h:HELPS]->(:Person)` (directed)
  - Encodes *reciprocal services* evidence.
  - Inputs (already computed upstream):
    - `h.help_strength` (scalar)

## Upstream prerequisites (attendance + wellbeing)

Tie evidence in this model is driven primarily by attendance/co-attendance.

In the current runbook, attendance probability is influenced by seeded wellbeing fields on `Person`:

- `person.lifeStabilityLsb` (LSB): primary “ability to show up reliably” offset.
- `person.lifeSatisfactionLsf` (LSF): smaller “mood / willingness to engage” offset.

These offsets are applied when computing `Participation.attendance_probability_score`:

- Implementation: `affinity/from_neo4j/cyphers/tie_strength_runbook/10_set_attendance_probability_per_participation.cypher`

Attendance is then deterministically sampled into `Participation.attended`, which drives co-attendance and therefore `s.similarity_strength`:

- Implementation: `affinity/from_neo4j/cyphers/tie_strength_runbook/30_sample_attended_deterministic.cypher`

## Step 1: Compute `tie_strength_total`

For each undirected similarity edge `s` between `a` and `b`:

- `helps_ab = coalesce( (a)-[:HELPS]->(b).help_strength , 0.0)`
- `helps_ba = coalesce( (b)-[:HELPS]->(a).help_strength , 0.0)`
- `sim = coalesce(s.similarity_strength, 0.0)`

**Definition**

- `s.tie_strength_total = sim + helps_ab + helps_ba`

Implementation: `affinity/from_neo4j/cyphers/tie_strength_runbook/60_set_tie_strength_total_and_help_components.cypher`

## Step 2: Compute `is_reciprocal_support`

We flag a similarity tie as having reciprocal support when *both* directions of help are sufficiently strong.

**Definition**

- `s.is_reciprocal_support = (helps_ab >= 0.25 AND helps_ba >= 0.25)`

Implementation:
- `affinity/from_neo4j/cyphers/tie_strength_runbook/61_set_help_mutual_and_is_reciprocal_support.cypher`

## Step 3: Compute `tie_type`

We classify only existing `:IS_SIMILAR_TO` edges as `WEAK` or `STRONG`.

- `ABSENT` ties are **implicit**: if there is no `:IS_SIMILAR_TO` edge for a pair, the tie is absent.

**Threshold**

- Strong cutoff constant:
  - `strong_cut = 7.8947638603696095`

**Definition**

- `s.tie_type = 'STRONG'` if `s.tie_strength_total >= strong_cut`, else `'WEAK'`

Implementation: `affinity/from_neo4j/cyphers/tie_strength_runbook/71_set_tie_type_from_cutoff.cypher`

## Export A (readable): tie strength + type table

This export is for audit/inspection. It includes *all student pairs* and labels:

- `STRONG` / `WEAK` when `:IS_SIMILAR_TO` exists
- `ABSENT` when `:IS_SIMILAR_TO` does not exist

Implementation: `affinity/from_neo4j/cyphers/tie_strength_runbook/72_readable_ties_including_absent_pairs.cypher`

Typical target filename:

- `affinity/from_neo4j/tie_type_and_strength_readable.json`

Note: the Cypher script returns rows in Neo4j; writing the JSON file is typically done by exporting/downloading the result from your Neo4j client and saving it to the target path. Saving to the same path will overwrite the existing file.

## Export B (code-ingest): directed weights `w_ij`

The artifact generator consumes a directed weight map `w_directed[(i,j)]`.

We export rows:

- `actor_student_id` (Person.id)
- `target_student_id` (Person.id)
- `w`

### Directed conversion rule

For each pair `(a,b)` where `:IS_SIMILAR_TO` exists:

- `t = coalesce(s.tie_strength_total, 0.0)`
- `help_ab = coalesce( (a)-[:HELPS]->(b).help_strength , 0.0)`
- `help_ba = coalesce( (b)-[:HELPS]->(a).help_strength , 0.0)`

We split the undirected total into:

- a non-negative symmetric base component
- plus the directional help component

**Definitions**

- `base = max(0, t - 0.5*(help_ab + help_ba))`
- `w_ab = base + help_ab`
- `w_ba = base + help_ba`

Implementation: `affinity/from_neo4j/cyphers/tie_strength_runbook/90_export_directed_wij_code_ready.cypher`

Typical target filename:

- `affinity/from_neo4j/tie_strength_code_data.json`

Note: the Cypher script returns rows in Neo4j; writing the JSON file is typically done by exporting/downloading the result from your Neo4j client and saving it to the target path. Saving to the same path will overwrite the existing file. The v2 generator also supports pulling these rows live from Neo4j Aura (and writing a run snapshot) via `--neo4j-live --snapshot`.

## Pipeline consumption (v2 Option B generator)

Script:

- `src/network_potential_engine/scripts/run_affinity_n50_generate_artifacts_v2_optionB.py`

Invocation:

Recommended (live Neo4j + snapshot):

- Provide Neo4j connection details via `.env`:
  - `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`, optional `NEO4J_DATABASE`
- Run the generator in live mode:
  - `python -m network_potential_engine.scripts.run_affinity_n50_generate_artifacts_v2_optionB --neo4j-live --snapshot --audit`

This will:

- Pull directed ties (`w_ij`) live by executing:
  - `affinity/from_neo4j/cyphers/tie_strength_runbook/90_export_directed_wij_code_ready.cypher`
- Pull additional cohort inputs live for auditability:
  - student personal properties
  - module interest weights (`:INTERESTED_IN`)
- Write artifacts into `affinity/artifacts/n50/`
- Write a timestamped snapshot folder:
  - `affinity/artifacts/n50/snapshots/<run_id>/`
  - containing the run's inputs and outputs for provenance

Behavior:

- Attendance/co-attendance simulation is skipped.
- `observations_v2.json` is written as a provenance stub referencing the Neo4j sources.

Optional (manual readable export):

- If you export the readable table JSON yourself (from `72_readable_ties_including_absent_pairs.cypher`), you can still pass it to the generator via:
  - `--neo4j-readable-json <path>`

## Rerun order (Neo4j)

Use the runbook:

- `affinity/from_neo4j/cyphers/tie_strength_runbook/RUNBOOK.md`

Key steps for finalization + export:

1. `60_set_tie_strength_total_and_help_components.cypher`
2. `61_set_help_mutual_and_is_reciprocal_support.cypher` (optional)
3. `71_set_tie_type_from_cutoff.cypher`
4. `72_readable_ties_including_absent_pairs.cypher`
5. `90_export_directed_wij_code_ready.cypher`
