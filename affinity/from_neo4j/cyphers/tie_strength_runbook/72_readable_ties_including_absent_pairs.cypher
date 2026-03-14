MATCH (a:Person)-[:HAS_TAG]->(:Tag {slug:"lcm-student"})
MATCH (b:Person)-[:HAS_TAG]->(:Tag {slug:"lcm-student"})
WHERE a.id < b.id
OPTIONAL MATCH (a)-[s:IS_SIMILAR_TO]-(b)
OPTIONAL MATCH (a)-[h1:HELPS]->(b)
OPTIONAL MATCH (b)-[h2:HELPS]->(a)
WITH a,b,s,
     coalesce(h1.help_strength,0.0) AS helps_ab,
     coalesce(h2.help_strength,0.0) AS helps_ba
RETURN
  a.displayName AS personA,
  b.displayName AS personB,
  CASE
    WHEN s IS NULL THEN 'ABSENT'
    ELSE s.tie_type
  END AS tie_type,
  CASE
    WHEN s IS NULL THEN 0.0
    ELSE coalesce(s.tie_strength_total,0.0)
  END AS tie_strength_total,
  CASE
    WHEN s IS NULL THEN false
    ELSE coalesce(s.is_reciprocal_support,false)
  END AS is_reciprocal_support,
  helps_ab,
  helps_ba
ORDER BY tie_strength_total DESC, helps_ab + helps_ba DESC;