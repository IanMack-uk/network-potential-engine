# Neo4j tie strength runbook (copy/paste order)

This folder contains an end-to-end set of Cypher scripts to compute:

- `Participation.attendance_probability_score`
- `Person.providerScore`
- Deterministic `Participation.u_attend` and `Participation.attended`
- `(:Person)-[:IS_SIMILAR_TO]-(:Person)` with:
  - `co_attend_count`
  - `demographic_similarity`
  - `similarity_strength`
  - `tie_strength_total`
  - `tie_type` (Granovetter: `WEAK` / `STRONG`)
- `(:Person)-[:HELPS]->(:Person)` with:
  - `help_strength`
  - `help_type`
- Optional: `s.is_reciprocal_support`

## Scope

All queries are scoped to:

- Students: `(:Tag {slug:"lcm-student"})`
- BA programme: `course.title CONTAINS "ORIGINAL - BA"`

Note: module/session participation is linked via:

- `(part:Participation)-[:IN_ACTIVITY]->(event:Event)`

## Run order

### Attendance + provider scoring

1. `05_seed_wellbeing_fields.cypher`
   - Seeds HEPI-aligned compositional/contextual wellbeing proxies onto `Person` and derives:
     - `Person.lifeStabilityLsb`
     - `Person.lifeSatisfactionLsf`
     - `Person.holisticWellbeingHwi`
     - `Person.hwiBand`

2. `10_set_attendance_probability_per_participation.cypher`
   - Sets `Participation.attendance_probability_score`.

3. `20_set_provider_score_per_person.cypher`
   - Sets `Person.providerScore`.

4. `30_sample_attended_deterministic.cypher`
   - Sets deterministic `Participation.u_attend` and `Participation.attended`.

### Similarity network build

5. `40_delete_is_similar_to_edges.cypher` (destructive)
   - Deletes all existing `:IS_SIMILAR_TO` relationships.

6. `41_create_is_similar_to_from_coattendance_cutoff_4.cypher`
   - Creates `:IS_SIMILAR_TO` edges when co-attendance count meets cutoff.

7. `42_set_demographic_similarity.cypher`
   - Sets `s.demographic_similarity` on `:IS_SIMILAR_TO`.

8. `43_set_similarity_strength.cypher`
   - Sets `s.similarity_strength`.

### Help network build

9. `50_delete_helps_edges.cypher` (destructive)
   - Deletes all existing `:HELPS` relationships.

10. `51_create_helps_edges.cypher`
   - Creates/updates `:HELPS` edges and sets `h.help_strength`.

11. `52_set_help_type.cypher`
   - Sets `h.help_type` categories from `help_strength`.

### Combine into tie strength + classify

12. `60_set_tie_strength_total_and_help_components.cypher`
   - Sets `s.tie_strength_total`, `s.helps_ab`, `s.helps_ba`.

13. `61_set_help_mutual_and_is_reciprocal_support.cypher` (optional)
   - Sets `s.help_mutual` and `s.is_reciprocal_support`.

14. `70_compute_strong_cutoff_p80.cypher`
   - Computes the 80th percentile cutoff for STRONG ties.

15. `71_set_tie_type_from_cutoff.cypher`
   - Sets `s.tie_type` (`WEAK` / `STRONG`) from the chosen cutoff.

16. `73_sanity_check_tie_type_counts.cypher` (optional)
   - Sanity check: counts ties by type.

17. `62_sanity_check_reciprocal_support_counts.cypher` (optional)
   - Sanity check: counts reciprocal support ties.

Optional audits:

- `audits/11_wellbeing_distribution.cypher`

## Exports / views

- **Pipeline input (directed `w_ij`)**
  - `90_export_directed_wij_code_ready.cypher`

- **Primary audit view (includes ABSENT pairs)**
  - `72_readable_ties_including_absent_pairs.cypher`

- **Optional readable view (existing ties only)**
  - `91_readable_existing_ties.cypher`

- **Optional app-facing readable list (existing ties only)**
  - `80_readable_existing_ties_app_facing.cypher`

## Artifact generation (v2 Option B)

The v2 artifact generator can pull its inputs live from Neo4j Aura and write a versioned snapshot per run.

- Configure `.env`:
  - `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`, optional `NEO4J_DATABASE`
- Run (live + snapshot):
  - `python -m network_potential_engine.scripts.run_affinity_n50_generate_artifacts_v2_optionB --neo4j-live --snapshot --audit`

Outputs:

- Artifacts written to:
  - `affinity/artifacts/n50/`
- Run snapshot written to:
  - `affinity/artifacts/n50/snapshots/<run_id>/`
  - Includes versioned exports for the run (e.g. personal properties, module interest scores, raw tie rows) and the generated artifacts.
