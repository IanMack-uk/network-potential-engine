MATCH (a:Person)-[s:IS_SIMILAR_TO]-(b:Person)
OPTIONAL MATCH (a)-[h1:HELPS]->(b)
OPTIONAL MATCH (b)-[h2:HELPS]->(a)
WITH s,
     coalesce(s.similarity_strength,0.0) AS sim,
     coalesce(h1.help_strength,0.0) AS helps_ab,
     coalesce(h2.help_strength,0.0) AS helps_ba
SET s.tie_strength_total = sim + helps_ab + helps_ba,
    s.helps_ab = helps_ab,
    s.helps_ba = helps_ba;
