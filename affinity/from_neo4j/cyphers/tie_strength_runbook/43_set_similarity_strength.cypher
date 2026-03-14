MATCH ()-[s:IS_SIMILAR_TO]-()
WITH s,
     coalesce(s.co_attend_count,0) AS t,
     coalesce(s.demographic_similarity,0.0) AS d
SET s.similarity_strength = (1.0 * t) * (1.0 + 0.6*d);