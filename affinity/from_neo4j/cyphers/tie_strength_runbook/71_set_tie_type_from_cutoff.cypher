MATCH ()-[s:IS_SIMILAR_TO]-()
SET s.tie_type =
  CASE
    WHEN s.tie_strength_total >= 7.8947638603696095 THEN 'STRONG'
    ELSE 'WEAK'
  END;