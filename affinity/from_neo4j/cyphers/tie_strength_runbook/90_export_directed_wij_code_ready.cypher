MATCH (a:Person)-[:HAS_TAG]->(:Tag {slug:"lcm-student"})
MATCH (b:Person)-[:HAS_TAG]->(:Tag {slug:"lcm-student"})
WHERE a.id < b.id
MATCH (a)-[s:IS_SIMILAR_TO]-(b)
OPTIONAL MATCH (a)-[h1:HELPS]->(b)
OPTIONAL MATCH (b)-[h2:HELPS]->(a)
WITH a,b,s,
     coalesce(h1.help_strength,0.0) AS help_ab,
     coalesce(h2.help_strength,0.0) AS help_ba,
     coalesce(s.tie_strength_total,0.0) AS t
WITH a,b,help_ab,help_ba,t,
     CASE
       WHEN (t - 0.5*(help_ab + help_ba)) < 0.0 THEN 0.0
       ELSE (t - 0.5*(help_ab + help_ba))
     END AS base
UNWIND [
  {actor_student_id: a.id, target_student_id: b.id, w: (base + help_ab)},
  {actor_student_id: b.id, target_student_id: a.id, w: (base + help_ba)}
] AS row
RETURN
  row.actor_student_id AS actor_student_id,
  row.target_student_id AS target_student_id,
  row.w AS w
ORDER BY actor_student_id, target_student_id;