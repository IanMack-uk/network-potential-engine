MATCH ()-[s:IS_SIMILAR_TO]-()
RETURN percentileCont(s.tie_strength_total, 0.80) AS strong_cut;