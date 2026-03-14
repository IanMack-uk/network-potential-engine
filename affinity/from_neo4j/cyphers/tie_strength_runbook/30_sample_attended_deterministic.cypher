MATCH (person:Person)-[:HAS_TAG]->(:Tag {slug: "lcm-student"})
MATCH (person)-[:HAS_PARTICIPATION]->(part:Participation)-[:IN_ACTIVITY]->(event:Event)
MATCH (event)-[:IS_PART_OF]->(course:Event)
WHERE course.title CONTAINS "ORIGINAL - BA"
WITH person, part, event,
     coalesce(part.attendance_probability_score, 0.0) AS p,
     person.id + '|' + event.id AS k
WITH part, p, apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k})) AS h
WITH part, p, h, 8 AS N
WITH part, p,
     reduce(u = 0.0, i IN range(0, N-1) |
       u +
       (
         CASE toLower(substring(h, i, 1))
           WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3
           WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7
           WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11
           WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15
           ELSE 0
         END
       ) / (16.0 ^ (i + 1))
     ) AS u_attend
SET part.u_attend = u_attend,
    part.attended = (u_attend < p);