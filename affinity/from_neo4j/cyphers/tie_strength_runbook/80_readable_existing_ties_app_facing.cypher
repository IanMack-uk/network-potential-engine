MATCH (a:Person)-[:HAS_TAG]->(:Tag {slug:"lcm-student"})
MATCH (b:Person)-[:HAS_TAG]->(:Tag {slug:"lcm-student"})
WHERE a.id < b.id
OPTIONAL MATCH (a)-[s:IS_SIMILAR_TO]-(b)
OPTIONAL MATCH (a)-[h1:HELPS]->(b)
OPTIONAL MATCH (b)-[h2:HELPS]->(a)
WITH a,b,s,
     coalesce(h1.help_strength,0.0) AS helps_ab,
     coalesce(h2.help_strength,0.0) AS helps_ba
WHERE s IS NOT NULL
RETURN
  a.displayName AS personA,
  b.displayName AS personB,
  s.tie_type AS tie_type,
  s.tie_strength_total AS tie_strength_total,
  coalesce(s.is_reciprocal_support,false) AS is_reciprocal_support,
  helps_ab,
  helps_ba
ORDER BY tie_strength_total DESC;