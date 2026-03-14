MATCH ()-[s:IS_SIMILAR_TO]-()
RETURN
  sum(CASE WHEN s.is_reciprocal_support THEN 1 ELSE 0 END) AS reciprocal,
  count(DISTINCT s) AS total;