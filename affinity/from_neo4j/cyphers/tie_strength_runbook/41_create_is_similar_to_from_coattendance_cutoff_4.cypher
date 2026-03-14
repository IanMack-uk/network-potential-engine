MATCH (a:Person)-[:HAS_TAG]->(:Tag {slug:"lcm-student"})
MATCH (b:Person)-[:HAS_TAG]->(:Tag {slug:"lcm-student"})
MATCH (a)-[:HAS_PARTICIPATION]->(pa:Participation {attended:true})-[:IN_ACTIVITY]->(e:Event)
MATCH (b)-[:HAS_PARTICIPATION]->(pb:Participation {attended:true})-[:IN_ACTIVITY]->(e)
MATCH (e)-[:IS_PART_OF]->(course:Event)
WHERE course.title CONTAINS "ORIGINAL - BA"
  AND a.id < b.id
WITH a, b, count(DISTINCT e) AS co_attend_count
WHERE co_attend_count >= 4
MERGE (a)-[s:IS_SIMILAR_TO]-(b)
SET s.co_attend_count = co_attend_count;