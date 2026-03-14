MATCH (a:Person)-[s:IS_SIMILAR_TO]-(b:Person)
WITH a,b,s,
     CASE WHEN a.nationality = b.nationality THEN 1.0 ELSE 0.0 END AS sim_nat,
     CASE WHEN a.sexuality = b.sexuality THEN 1.0 ELSE 0.0 END AS sim_sexuality,
     CASE WHEN a.ethnicity = b.ethnicity THEN 1.0 ELSE 0.0 END AS sim_ethnicity,
     CASE
       WHEN (1.0 - (abs(duration.inDays(a.dateOfBirth, b.dateOfBirth).days) / 365.25) / 4.0) < 0.0 THEN 0.0
       ELSE (1.0 - (abs(duration.inDays(a.dateOfBirth, b.dateOfBirth).days) / 365.25) / 4.0)
     END AS sim_age
SET s.demographic_similarity =
  0.30*sim_nat + 0.25*sim_ethnicity + 0.20*sim_sexuality + 0.25*sim_age;