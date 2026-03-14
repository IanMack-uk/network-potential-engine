MATCH (person:Person)-[:HAS_TAG]->(:Tag {slug: "lcm-student"})
WITH person, person.id AS pid
WITH person, pid,
     pid + '|polar' AS k_polar,
     pid + '|res' AS k_res,
     pid + '|commute' AS k_commute,
     pid + '|work' AS k_work,
     pid + '|employment' AS k_employment,
     pid + '|open_to_work' AS k_open_to_work,
     pid + '|means' AS k_means,
     pid + '|teach_support' AS k_teach_support,
     pid + '|feedback' AS k_feedback,
     pid + '|teach_interest' AS k_teach_interest,
     pid + '|house' AS k_house,
     pid + '|finance' AS k_finance,
    pid + '|routine' AS k_routine,
    pid + '|purpose' AS k_purpose,
    pid + '|fulfil' AS k_fulfil,
    pid + '|happy' AS k_happy
WITH person,
     apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_polar})) AS h_polar,
     apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_res})) AS h_res,
     apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_commute})) AS h_commute,
     apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_work})) AS h_work,
     apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_employment})) AS h_employment,
     apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_open_to_work})) AS h_open_to_work,
     apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_means})) AS h_means,
     apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_teach_support})) AS h_teach_support,
     apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_feedback})) AS h_feedback,
     apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_teach_interest})) AS h_teach_interest,
     apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_house})) AS h_house,
    apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_finance})) AS h_finance,
    apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_routine})) AS h_routine,
    apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_purpose})) AS h_purpose,
    apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_fulfil})) AS h_fulfil,
    apoc.hashing.fingerprint(apoc.create.vNode(['K'], {k:k_happy})) AS h_happy
WITH person,
     reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_polar, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_polar,
     reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_res, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_res,
     reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_commute, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_commute,
     reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_work, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_work,
     reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_employment, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_employment,
     reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_open_to_work, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_open_to_work,
     reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_means, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_means,
     reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_teach_support, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_teach_support,
     reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_feedback, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_feedback,
     reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_teach_interest, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_teach_interest,
    reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_house, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_house,
    reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_finance, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_finance,
    reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_routine, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_routine,
    reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_purpose, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_purpose,
    reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_fulfil, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_fulfil,
    reduce(u = 0.0, i IN range(0, 7) | u + (CASE toLower(substring(h_happy, i, 1)) WHEN '0' THEN 0 WHEN '1' THEN 1 WHEN '2' THEN 2 WHEN '3' THEN 3 WHEN '4' THEN 4 WHEN '5' THEN 5 WHEN '6' THEN 6 WHEN '7' THEN 7 WHEN '8' THEN 8 WHEN '9' THEN 9 WHEN 'a' THEN 10 WHEN 'b' THEN 11 WHEN 'c' THEN 12 WHEN 'd' THEN 13 WHEN 'e' THEN 14 WHEN 'f' THEN 15 ELSE 0 END) / (16.0 ^ (i + 1))) AS u_happy
WITH person,
     duration.between(person.dateOfBirth, date()).years AS age_years,
     (1 + toInteger(floor(5.0 * u_polar))) AS polar_quintile,
     coalesce(person.nationality, 'United Kingdom') AS nationality,
     u_res AS u_res,
     u_commute AS u_commute,
     u_work AS u_work,
     u_employment AS u_employment,
     u_open_to_work AS u_open_to_work,
     u_means AS financial_means_0_1,
     CASE coalesce(person.outputProductivity, 'medium')
       WHEN 'very_low' THEN 0.15
       WHEN 'low' THEN 0.30
       WHEN 'medium' THEN 0.50
       WHEN 'high' THEN 0.70
       WHEN 'very_high' THEN 0.85
       ELSE 0.50
     END AS output_productivity_score_0_1,
     (10.0 * u_teach_support) AS teaching_support_0_10,
     (10.0 * u_feedback) AS feedback_usefulness_0_10,
     (10.0 * u_teach_interest) AS teaching_interest_0_10,
     u_house AS u_house,
     u_finance AS u_finance,
     u_routine AS u_routine,
     u_purpose AS u_purpose,
     u_fulfil AS u_fulfil,
     u_happy AS u_happy
WITH person,
     age_years,
     polar_quintile,
     nationality,
     u_res,
     u_commute,
     u_work,
     u_employment,
     u_open_to_work,
     financial_means_0_1,
     output_productivity_score_0_1,
     teaching_support_0_10,
     feedback_usefulness_0_10,
     teaching_interest_0_10,
     u_house,
     u_finance,
     u_routine,
     u_purpose,
     u_fulfil,
     u_happy,
     CASE
       WHEN age_years <= 19 THEN 0.05
       WHEN age_years >= 23 THEN -0.05
       ELSE 0.0
     END AS age_home_off,
     CASE
       WHEN nationality <> 'United Kingdom' THEN -0.05
       ELSE 0.0
     END AS nat_home_off
WITH person,
     polar_quintile,
     u_commute,
     u_work,
     u_employment,
     u_open_to_work,
     financial_means_0_1,
     output_productivity_score_0_1,
     teaching_support_0_10,
     feedback_usefulness_0_10,
     teaching_interest_0_10,
     u_house,
     u_finance,
     u_routine,
     u_purpose,
     u_fulfil,
     u_happy,
     CASE
       WHEN u_res < (CASE
         WHEN (0.33 + age_home_off + nat_home_off) < 0.05 THEN 0.05
         WHEN (0.33 + age_home_off + nat_home_off) > 0.95 THEN 0.95
         ELSE (0.33 + age_home_off + nat_home_off)
       END) THEN 'lives_at_home'
       ELSE 'relocated'
     END AS residential_status
WITH person,
     polar_quintile,
     residential_status,
     u_work,
     u_employment,
     u_open_to_work,
     financial_means_0_1,
     output_productivity_score_0_1,
     teaching_support_0_10,
     feedback_usefulness_0_10,
     teaching_interest_0_10,
     u_house,
     u_finance,
     u_routine,
     u_purpose,
     u_fulfil,
     u_happy,
     CASE
       WHEN u_commute < (CASE
         WHEN (0.30 + (CASE WHEN residential_status = 'lives_at_home' THEN 0.05 ELSE -0.05 END)) < 0.05 THEN 0.05
         WHEN (0.30 + (CASE WHEN residential_status = 'lives_at_home' THEN 0.05 ELSE -0.05 END)) > 0.95 THEN 0.95
         ELSE (0.30 + (CASE WHEN residential_status = 'lives_at_home' THEN 0.05 ELSE -0.05 END))
       END) THEN 'long'
       ELSE 'short'
     END AS commute_band
WITH person,
     polar_quintile,
     residential_status,
     commute_band,
     u_work,
     u_open_to_work,
     financial_means_0_1,
     output_productivity_score_0_1,
     teaching_support_0_10,
     feedback_usefulness_0_10,
     teaching_interest_0_10,
     u_house,
     u_finance,
     u_routine,
     u_purpose,
     u_fulfil,
     u_happy,
     CASE
       WHEN (u_employment + 0.35*(0.5 - financial_means_0_1) + 0.35*(0.5 - output_productivity_score_0_1)) >= 0.85 THEN 'full_time'
       WHEN (u_employment + 0.35*(0.5 - financial_means_0_1) + 0.35*(0.5 - output_productivity_score_0_1)) >= 0.65 THEN 'contract'
       WHEN (u_employment + 0.35*(0.5 - financial_means_0_1) + 0.35*(0.5 - output_productivity_score_0_1)) >= 0.35 THEN 'part_time'
       ELSE 'no_job'
     END AS employment_status
WITH person,
     polar_quintile,
     residential_status,
     commute_band,
     employment_status,
     financial_means_0_1,
     output_productivity_score_0_1,
     teaching_support_0_10,
     feedback_usefulness_0_10,
     teaching_interest_0_10,
     u_house,
     u_finance,
     u_routine,
     u_purpose,
     u_fulfil,
     u_happy,
     CASE
       WHEN employment_status = 'full_time' THEN '12_plus'
       WHEN employment_status = 'contract' THEN CASE WHEN u_work < (0.60 - 0.20*output_productivity_score_0_1) THEN '12_plus' ELSE '0_11' END
       WHEN employment_status = 'part_time' THEN CASE WHEN u_work < (0.40 - 0.25*output_productivity_score_0_1) THEN '12_plus' ELSE '0_11' END
       ELSE '0_11'
     END AS paid_work_hours_band,
     CASE
       WHEN employment_status = 'full_time' THEN (u_open_to_work < 0.40)
       WHEN employment_status IN ['contract', 'part_time'] THEN (u_open_to_work < 0.70)
       WHEN (financial_means_0_1 > 0.70 AND output_productivity_score_0_1 > 0.70) THEN (u_open_to_work < 0.30)
       ELSE (u_open_to_work < 0.75)
     END AS openToWork
WITH person,
     polar_quintile,
     residential_status,
     commute_band,
     employment_status,
     paid_work_hours_band,
     openToWork,
     financial_means_0_1,
     output_productivity_score_0_1,
     teaching_support_0_10,
     feedback_usefulness_0_10,
     teaching_interest_0_10,
     u_house,
     u_finance,
     u_routine,
     u_purpose,
     u_fulfil,
     u_happy,
     CASE polar_quintile WHEN 1 THEN -1.0 WHEN 2 THEN -0.5 WHEN 3 THEN 0.0 WHEN 4 THEN 0.5 WHEN 5 THEN 1.0 ELSE 0.0 END AS polar_off,
     CASE residential_status WHEN 'relocated' THEN 0.3 ELSE -0.3 END AS res_off,
     CASE commute_band WHEN 'short' THEN 0.2 ELSE -0.2 END AS commute_off,
     CASE paid_work_hours_band WHEN '12_plus' THEN -0.5 ELSE 0.2 END AS work_off
WITH person,
     polar_quintile,
     residential_status,
     commute_band,
     employment_status,
     paid_work_hours_band,
     openToWork,
     financial_means_0_1,
     output_productivity_score_0_1,
     teaching_support_0_10,
     feedback_usefulness_0_10,
     teaching_interest_0_10,
     polar_off,
     res_off,
     commute_off,
     work_off,
     (5.0 + 0.6*polar_off + 1.0*res_off + 1.0*commute_off + (u_house - 0.5) * 1.0) AS housing_raw,
     (5.0 + 0.5*polar_off + 1.0*work_off + (u_finance - 0.5) * 1.2) AS finance_raw,
     (CASE person.reliabilityBand
       WHEN 'extremely_high' THEN 9.0
       WHEN 'very_high' THEN 8.0
       WHEN 'high' THEN 7.5
       WHEN 'medium_high' THEN 7.0
       WHEN 'medium' THEN 5.5
       WHEN 'medium_low' THEN 4.5
       WHEN 'low_medium' THEN 3.5
       WHEN 'low' THEN 3.0
       WHEN 'very_low' THEN 2.5
       ELSE 5.5
     END + (u_routine - 0.5) * 1.0) AS routine_raw,
     (CASE person.initiativeBand
       WHEN 'very_high' THEN 9.0
       WHEN 'high' THEN 8.0
       WHEN 'medium' THEN 6.0
       WHEN 'low_medium' THEN 4.5
       WHEN 'low' THEN 3.5
       WHEN 'very_low' THEN 2.5
       ELSE 6.0
     END + (u_purpose - 0.5) * 1.0) AS purpose_raw,
     u_fulfil,
     u_happy
WITH person,
     polar_quintile,
     residential_status,
     commute_band,
     employment_status,
     paid_work_hours_band,
     openToWork,
     financial_means_0_1,
     output_productivity_score_0_1,
     teaching_support_0_10,
     feedback_usefulness_0_10,
     teaching_interest_0_10,
     CASE WHEN housing_raw < 1.0 THEN 1.0 WHEN housing_raw > 10.0 THEN 10.0 ELSE housing_raw END AS housing_security_1_10,
     CASE WHEN finance_raw < 1.0 THEN 1.0 WHEN finance_raw > 10.0 THEN 10.0 ELSE finance_raw END AS financial_confidence_1_10,
     CASE WHEN routine_raw < 1.0 THEN 1.0 WHEN routine_raw > 10.0 THEN 10.0 ELSE routine_raw END AS routine_consistency_1_10,
     CASE WHEN purpose_raw < 1.0 THEN 1.0 WHEN purpose_raw > 10.0 THEN 10.0 ELSE purpose_raw END AS sense_of_purpose_1_10,
     u_fulfil,
     u_happy
WITH person,
     polar_quintile,
     residential_status,
     commute_band,
     employment_status,
     paid_work_hours_band,
     openToWork,
     financial_means_0_1,
     output_productivity_score_0_1,
     teaching_support_0_10,
     feedback_usefulness_0_10,
     teaching_interest_0_10,
     housing_security_1_10,
     financial_confidence_1_10,
     routine_consistency_1_10,
     sense_of_purpose_1_10,
     (5.0 + 0.30*(sense_of_purpose_1_10 - 5.0) + 0.50*(teaching_interest_0_10 - 5.0) + (u_fulfil - 0.5) * 1.0) AS fulfil_raw,
     u_happy
WITH person,
     polar_quintile,
     residential_status,
     commute_band,
     employment_status,
     paid_work_hours_band,
     openToWork,
     financial_means_0_1,
     output_productivity_score_0_1,
     teaching_support_0_10,
     feedback_usefulness_0_10,
     teaching_interest_0_10,
     housing_security_1_10,
     financial_confidence_1_10,
     routine_consistency_1_10,
     sense_of_purpose_1_10,
     CASE WHEN fulfil_raw < 1.0 THEN 1.0 WHEN fulfil_raw > 10.0 THEN 10.0 ELSE fulfil_raw END AS creative_fulfilment_1_10,
     u_happy
WITH person,
     polar_quintile,
     residential_status,
     commute_band,
     employment_status,
     paid_work_hours_band,
     openToWork,
     financial_means_0_1,
     output_productivity_score_0_1,
     teaching_support_0_10,
     feedback_usefulness_0_10,
     teaching_interest_0_10,
     housing_security_1_10,
     financial_confidence_1_10,
     routine_consistency_1_10,
     sense_of_purpose_1_10,
     creative_fulfilment_1_10,
     (5.0 + 0.40*(teaching_support_0_10 - 5.0) + 0.30*(feedback_usefulness_0_10 - 5.0) + 0.20*(creative_fulfilment_1_10 - 5.0) + (u_happy - 0.5) * 0.8) AS happy_raw
WITH person,
     polar_quintile,
     residential_status,
     commute_band,
     employment_status,
     paid_work_hours_band,
     openToWork,
     financial_means_0_1,
     output_productivity_score_0_1,
     teaching_support_0_10,
     feedback_usefulness_0_10,
     teaching_interest_0_10,
     housing_security_1_10,
     financial_confidence_1_10,
     routine_consistency_1_10,
     sense_of_purpose_1_10,
     creative_fulfilment_1_10,
     CASE WHEN happy_raw < 1.0 THEN 1.0 WHEN happy_raw > 10.0 THEN 10.0 ELSE happy_raw END AS global_happiness_1_10
WITH person,
     polar_quintile,
     residential_status,
     commute_band,
     employment_status,
     paid_work_hours_band,
     openToWork,
     financial_means_0_1,
     output_productivity_score_0_1,
     teaching_support_0_10,
     feedback_usefulness_0_10,
     teaching_interest_0_10,
     housing_security_1_10,
     financial_confidence_1_10,
     routine_consistency_1_10,
     global_happiness_1_10,
     sense_of_purpose_1_10,
     creative_fulfilment_1_10,
     (housing_security_1_10 + financial_confidence_1_10 + routine_consistency_1_10) / 3.0 AS life_stability_lsb,
     (global_happiness_1_10 + sense_of_purpose_1_10 + creative_fulfilment_1_10) / 3.0 AS life_satisfaction_lsf
WITH person,
     polar_quintile,
     residential_status,
     commute_band,
     employment_status,
     paid_work_hours_band,
     openToWork,
     financial_means_0_1,
     output_productivity_score_0_1,
     teaching_support_0_10,
     feedback_usefulness_0_10,
     teaching_interest_0_10,
     housing_security_1_10,
     financial_confidence_1_10,
     routine_consistency_1_10,
     global_happiness_1_10,
     sense_of_purpose_1_10,
     creative_fulfilment_1_10,
     life_stability_lsb,
     life_satisfaction_lsf,
     (life_stability_lsb + life_satisfaction_lsf) / 2.0 AS holistic_wellbeing_hwi
SET person.polarQuintile = polar_quintile,
    person.residentialStatus = residential_status,
    person.commuteBand = commute_band,
    person.employmentStatus = employment_status,
    person.paidWorkHoursBand = paid_work_hours_band,
    person.openToWork = openToWork,
    person.financialMeans0_1 = financial_means_0_1,
    person.outputProductivityScore0_1 = output_productivity_score_0_1,
    person.teachingSupport0_10 = teaching_support_0_10,
    person.feedbackUsefulness0_10 = feedback_usefulness_0_10,
    person.teachingInterest0_10 = teaching_interest_0_10,
    person.housingSecurity1_10 = housing_security_1_10,
    person.financialConfidence1_10 = financial_confidence_1_10,
    person.routineConsistency1_10 = routine_consistency_1_10,
    person.globalHappiness1_10 = global_happiness_1_10,
    person.senseOfPurpose1_10 = sense_of_purpose_1_10,
    person.creativeFulfilment1_10 = creative_fulfilment_1_10,
    person.lifeStabilityLsb = life_stability_lsb,
    person.lifeSatisfactionLsf = life_satisfaction_lsf,
    person.holisticWellbeingHwi = holistic_wellbeing_hwi,
    person.hwiBand =
      CASE
        WHEN holistic_wellbeing_hwi >= 8.5 THEN 'flourishing'
        WHEN holistic_wellbeing_hwi >= 6.0 THEN 'resilient'
        WHEN holistic_wellbeing_hwi >= 4.0 THEN 'vulnerable'
        ELSE 'critical'
      END;
