MATCH (p:Person)-[:HAS_PARTICIPATION]->(part:Participation)
WITH p, part
MATCH (m:Event {type:"MODULE", typeCategory:"EDUCATION"})
WHERE m.id = part.scope.id
WITH p, part, m,
     toString(apoc.hashing.fingerprint('attend::' + p.id + '::' + m.id + '::' + part.id)) AS fp
WITH p, part, m, fp,
     CASE
       WHEN substring(fp,0,2) = '0x' THEN substring(fp,2,12)
       ELSE substring(fp,0,10)
     END AS hex10
WITH p, part, m, fp, hex10,
     toInteger('0x' + hex10) AS x
WITH p, part, m, fp, hex10, x,
     toFloat(x) / 1099511627776.0 AS u
RETURN
  p.id AS person_id,
  p.displayName AS displayName,
  m.id AS module_id,
  m.title AS module_title,
  part.id AS participation_id,
  part.attendance_probability_score AS attendance_probability_score,
  fp AS fingerprint,
  hex10 AS hex10,
  u AS u_attend_recomputed,
  part.u_attend AS u_attend_stored,
  part.attended AS attended_stored,
  (u < coalesce(part.attendance_probability_score,0.0)) AS attended_recomputed
LIMIT 25;
