MATCH (a:Person)-[:HAS_TAG]->(:Tag {slug:"lcm-student"})
MATCH (b:Person)-[:HAS_TAG]->(:Tag {slug:"lcm-student"})
MATCH (a)-[:HAS_PARTICIPATION]->(pa:Participation {attended:true})-[:IN_ACTIVITY]->(e:Event)
MATCH (b)-[:HAS_PARTICIPATION]->(pb:Participation {attended:true})-[:IN_ACTIVITY]->(e)
MATCH (e)-[:IS_PART_OF]->(course:Event)
WHERE course.title CONTAINS "ORIGINAL - BA"
  AND a.id <> b.id
MATCH (a)-[ia:INTERESTED_IN]->(e)
MATCH (b)-[ib:INTERESTED_IN]->(e)
WITH a,b,
     sum(
       coalesce(a.providerScore,0.0) * coalesce(ia.weight,0.0) * (1.0 - coalesce(ib.weight,0.0))
     ) AS help_strength
WHERE help_strength > 0
MERGE (a)-[h:HELPS]->(b)
SET h.help_strength = help_strength;