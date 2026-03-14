MATCH (part:Participation)
WHERE part.attendance_probability_score IS NOT NULL
RETURN
  count(*) AS n,
  avg(part.attendance_probability_score) AS mean,
  min(part.attendance_probability_score) AS min,
  max(part.attendance_probability_score) AS max;
