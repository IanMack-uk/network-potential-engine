MATCH (person:Person)-[:HAS_TAG]->(:Tag {slug: "lcm-student"})
MATCH (person)-[:HAS_PARTICIPATION]->(part:Participation)-[:IN_ACTIVITY]->(event:Event)
MATCH (event)-[:IS_PART_OF]->(course:Event)
WHERE course.title CONTAINS "ORIGINAL - BA"
MATCH (person)-[i:INTERESTED_IN]->(event)
WITH person, part, event, coalesce(i.weight, 0.0) AS interest,

     CASE person.reliabilityBand
       WHEN 'extremely_high' THEN 0.10
       WHEN 'very_high' THEN 0.08
       WHEN 'high' THEN 0.08
       WHEN 'medium_high' THEN 0.04
       WHEN 'medium' THEN 0.00
       WHEN 'medium_low' THEN -0.04
       WHEN 'low_medium' THEN -0.06
       WHEN 'low' THEN -0.08
       WHEN 'very_low' THEN -0.10
       ELSE 0.00
     END AS rel_off,

     CASE person.initiativeBand
       WHEN 'very_high' THEN 0.06
       WHEN 'high' THEN 0.05
       WHEN 'medium' THEN 0.00
       WHEN 'low_medium' THEN -0.03
       WHEN 'low' THEN -0.05
       WHEN 'very_low' THEN -0.06
       ELSE 0.00
     END AS init_off,

     CASE WHEN person.openToCollaborate THEN 0.02 ELSE 0.00 END AS collab_off,
     CASE WHEN person.openToWork THEN 0.01 ELSE 0.00 END AS work_off
WITH person, part, interest, rel_off, init_off, collab_off, work_off,
     (0.06 * ((coalesce(person.lifeStabilityLsb, 5.5) - 5.5) / 4.5)) AS life_off
     ,(0.02 * ((coalesce(person.lifeSatisfactionLsf, 5.5) - 5.5) / 4.5)) AS mood_off
WITH part, interest,
     (0.55 + rel_off + init_off + collab_off + work_off + life_off + mood_off) AS a_raw
WITH part, interest,
     CASE WHEN a_raw < 0.20 THEN 0.20 WHEN a_raw > 0.95 THEN 0.95 ELSE a_raw END AS a_i
WITH part, interest, a_i, 0.15 AS k_interest
WITH part, a_i * (1.0 + k_interest * interest) AS p_raw
SET part.attendance_probability_score =
  CASE WHEN p_raw < 0.0 THEN 0.0 WHEN p_raw > 1.0 THEN 1.0 ELSE p_raw END;