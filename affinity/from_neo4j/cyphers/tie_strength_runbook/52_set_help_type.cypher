MATCH ()-[h:HELPS]->()
SET h.help_type =
  CASE
    WHEN h.help_strength < 0.10 THEN 'LIGHT'
    WHEN h.help_strength < 0.40 THEN 'MEDIUM'
    ELSE 'STRONG'
  END;