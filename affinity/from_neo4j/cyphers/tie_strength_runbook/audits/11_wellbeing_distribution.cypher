MATCH (person:Person)-[:HAS_TAG]->(:Tag {slug: "lcm-student"})
WITH collect(person) AS people
RETURN
  size(people) AS n_students,
  reduce(s = 0.0, p IN people | s + coalesce(p.lifeStabilityLsb, 0.0)) / toFloat(size(people)) AS mean_lsb,
  reduce(m = 1e9, p IN people | CASE WHEN coalesce(p.lifeStabilityLsb, 0.0) < m THEN coalesce(p.lifeStabilityLsb, 0.0) ELSE m END) AS min_lsb,
  reduce(m = -1e9, p IN people | CASE WHEN coalesce(p.lifeStabilityLsb, 0.0) > m THEN coalesce(p.lifeStabilityLsb, 0.0) ELSE m END) AS max_lsb,
  reduce(s = 0.0, p IN people | s + coalesce(p.lifeSatisfactionLsf, 0.0)) / toFloat(size(people)) AS mean_lsf,
  reduce(m = 1e9, p IN people | CASE WHEN coalesce(p.lifeSatisfactionLsf, 0.0) < m THEN coalesce(p.lifeSatisfactionLsf, 0.0) ELSE m END) AS min_lsf,
  reduce(m = -1e9, p IN people | CASE WHEN coalesce(p.lifeSatisfactionLsf, 0.0) > m THEN coalesce(p.lifeSatisfactionLsf, 0.0) ELSE m END) AS max_lsf,
  reduce(s = 0.0, p IN people | s + coalesce(p.holisticWellbeingHwi, 0.0)) / toFloat(size(people)) AS mean_hwi,
  reduce(m = 1e9, p IN people | CASE WHEN coalesce(p.holisticWellbeingHwi, 0.0) < m THEN coalesce(p.holisticWellbeingHwi, 0.0) ELSE m END) AS min_hwi,
  reduce(m = -1e9, p IN people | CASE WHEN coalesce(p.holisticWellbeingHwi, 0.0) > m THEN coalesce(p.holisticWellbeingHwi, 0.0) ELSE m END) AS max_hwi,
  reduce(c = 0, p IN people | c + CASE WHEN coalesce(p.openToWork, false) THEN 1 ELSE 0 END) AS n_open_to_work_true;

MATCH (person:Person)-[:HAS_TAG]->(:Tag {slug: "lcm-student"})
RETURN person.employmentStatus AS employmentStatus, count(*) AS n
ORDER BY n DESC;

MATCH (person:Person)-[:HAS_TAG]->(:Tag {slug: "lcm-student"})
RETURN person.paidWorkHoursBand AS paidWorkHoursBand, count(*) AS n
ORDER BY n DESC;
