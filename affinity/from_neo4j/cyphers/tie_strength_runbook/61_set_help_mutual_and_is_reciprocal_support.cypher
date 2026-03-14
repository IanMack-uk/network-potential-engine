MATCH (a:Person)-[s:IS_SIMILAR_TO]-(b:Person)
OPTIONAL MATCH (a)-[h1:HELPS]->(b)
OPTIONAL MATCH (b)-[h2:HELPS]->(a)
WITH s,
     coalesce(h1.help_strength,0.0) AS hab,
     coalesce(h2.help_strength,0.0) AS hba
WITH s,
     CASE WHEN hab < hba THEN hab ELSE hba END AS help_mutual
SET s.help_mutual = help_mutual,
    s.is_reciprocal_support = (help_mutual >= 0.10);