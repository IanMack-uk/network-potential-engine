MATCH (p:Person)
RETURN
  collect(DISTINCT coalesce(p.reliabilityBand,'<NULL>')) AS reliabilityBands,
  collect(DISTINCT coalesce(p.initiativeBand,'<NULL>')) AS initiativeBands,
  collect(DISTINCT toString(coalesce(p.openToCollaborate,'<NULL>'))) AS openToCollaborateValues,
  collect(DISTINCT toString(coalesce(p.openToWork,'<NULL>'))) AS openToWorkValues;
