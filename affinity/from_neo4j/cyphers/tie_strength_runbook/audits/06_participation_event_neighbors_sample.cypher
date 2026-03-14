MATCH (:Person)-[:HAS_PARTICIPATION]->(part:Participation)
WITH part LIMIT 50
OPTIONAL MATCH (part)-[r]-(e:Event)
RETURN
  part.id AS participation_id,
  type(r) AS rel_type,
  startNode(r).id AS rel_start_id,
  endNode(r).id AS rel_end_id,
  e.id AS event_id,
  e.type AS event_type,
  e.typeCategory AS event_typeCategory,
  e.title AS event_title
ORDER BY participation_id, rel_type, event_id
LIMIT 200;
