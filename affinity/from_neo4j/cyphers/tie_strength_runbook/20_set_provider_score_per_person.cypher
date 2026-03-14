MATCH (person:Person)-[:HAS_TAG]->(:Tag {slug: "lcm-student"})
WITH person,
     (CASE WHEN person.providesTeaching THEN 0.50 ELSE 0.0 END) +
     (CASE WHEN person.providesSupport THEN 0.20 ELSE 0.0 END) +
     (CASE WHEN person.providesMentorship THEN 0.20 ELSE 0.0 END) +
     (CASE WHEN person.providesIntroductions THEN 0.20 ELSE 0.0 END) +
     (CASE WHEN person.offersOpportunities THEN 0.10 ELSE 0.0 END) AS prov_raw
SET person.providerScore = CASE WHEN prov_raw > 1.0 THEN 1.0 ELSE prov_raw END;