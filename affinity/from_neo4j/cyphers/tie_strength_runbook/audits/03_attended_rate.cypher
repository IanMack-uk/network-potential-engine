MATCH (part:Participation)
WHERE part.attended IS NOT NULL
RETURN
  count(*) AS n,
  sum(CASE WHEN part.attended THEN 1 ELSE 0 END) AS attended_true,
  (toFloat(sum(CASE WHEN part.attended THEN 1 ELSE 0 END)) / toFloat(count(*))) AS attended_rate;
