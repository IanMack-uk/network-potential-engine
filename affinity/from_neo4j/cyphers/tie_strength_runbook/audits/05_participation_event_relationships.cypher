MATCH (:Person)-[:HAS_PARTICIPATION]->(part:Participation)
OPTIONAL MATCH (part)-[r]->(e:Event)
RETURN
  coalesce(type(r),'<NO_REL>') AS rel_type,
  coalesce(e.type,'<NO_EVENT>') AS event_type,
  coalesce(e.typeCategory,'<NO_EVENT>') AS event_typeCategory,
  count(*) AS n
ORDER BY n DESC;
