MATCH ()-[s:IS_SIMILAR_TO]-()
RETURN s.tie_type AS type, count(DISTINCT s) AS n
ORDER BY n DESC;