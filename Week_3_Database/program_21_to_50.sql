-- =========================================================
-- 21. Get a list of wearable device information
-- =========================================================
SELECT *
FROM wearabledevicedata;


-- =========================================================
-- 22. Get a list of all the blood tests done
-- =========================================================
SELECT *
FROM bloodtest;


-- =========================================================
-- 23. Get a list of members who are aged greater than 50
-- =========================================================
SELECT *
FROM memberinfo
WHERE age > 50;


-- =========================================================
-- 24. Get a list of addresses for the city 'Flora'
-- =========================================================
SELECT *
FROM addressinfo
WHERE city = 'Flora';


-- =========================================================
-- 25. Get a list of all unique states
-- =========================================================
SELECT DISTINCT state
FROM addressinfo;


-- =========================================================
-- 26. Get the total number of members in the database
-- =========================================================
SELECT COUNT(*) AS total_members
FROM memberinfo;


-- =========================================================
-- 27. Get the total number of blood tests done
-- =========================================================
SELECT COUNT(*) AS total_blood_tests
FROM bloodtest;


-- =========================================================
-- 28. Get the average cholesterol level for members
-- =========================================================
SELECT AVG(serumcholesterol) AS avg_cholesterol
FROM bloodtest;


-- =========================================================
-- 29. Get the maximum peak value in symptoms
-- =========================================================
SELECT MAX(oldpeak) AS max_peak_value
FROM symptom;


-- =========================================================
-- 30. Get the list of tests done between
--     January 1, 2015 and January 31, 2019
-- =========================================================
SELECT *
FROM bloodtest
WHERE date BETWEEN '2015-01-01' AND '2019-01-31';


-- =========================================================
-- 31. Get the number of males and females
--     aged between 50 and 60
-- =========================================================
SELECT gender, COUNT(*) AS count
FROM memberinfo
WHERE age BETWEEN 50 AND 60
GROUP BY gender;


-- =========================================================
-- 32. Get the list of tests where blood pressure
--     is between 100 and 200
-- =========================================================
SELECT *
FROM bloodtest
WHERE bloodpressure BETWEEN 100 AND 200;


-- =========================================================
-- 33. Get the list of symptoms diagnosed for patients
-- =========================================================
SELECT *
FROM symptom;


-- =========================================================
-- 34. Get the average age of patients in the database
-- =========================================================
SELECT AVG(age) AS avg_age
FROM memberinfo;


-- =========================================================
-- 35. Get the total number of cities for each state
-- =========================================================
SELECT state, COUNT(DISTINCT city) AS total_cities
FROM addressinfo
GROUP BY state;


SELECT 
    a.state,
    COUNT(CASE WHEN m.gender = 'Male' THEN 1 END) AS male_count,
    COUNT(CASE WHEN m.gender = 'Female' THEN 1 END) AS female_count
FROM addressinfo a
JOIN memberinfo m
    ON a.member_id = m.member_id
GROUP BY a.state;

-- =========================================================
-- 36. Get the number of patients in age groups
-- =========================================================
SELECT
  CASE
    WHEN age BETWEEN 10 AND 20 THEN '10-20'
    WHEN age BETWEEN 21 AND 30 THEN '20-30'
    WHEN age BETWEEN 31 AND 40 THEN '30-40'
    WHEN age BETWEEN 41 AND 50 THEN '40-50'
    WHEN age BETWEEN 51 AND 60 THEN '50-60'
    WHEN age BETWEEN 61 AND 70 THEN '60-70'
  END AS age_group,
  COUNT(*) AS total_patients
FROM memberinfo
GROUP BY age_group
ORDER BY age_group;


-- =========================================================
-- 37. Get the list of members and their addresses
-- =========================================================
SELECT m.*, a.*
FROM memberinfo m
JOIN addressinfo a
  ON m.member_id = a.memberinfo_member_id;


-- =========================================================
-- 38. Get the list of members and their cardio history
-- =========================================================
SELECT m.firstname, m.lastname, c.*
FROM memberinfo m
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id;


-- =========================================================
-- 39. Get the list of members and their diseases
-- =========================================================
SELECT m.firstname, m.lastname, d.*
FROM memberinfo m
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
JOIN diseasedetail d
  ON c.cardio_id = d.cardiodiagnosis_cardio_id;


-- =========================================================
-- 40. Get the list of females diagnosed with a heart attack
-- =========================================================
SELECT m.*
FROM memberinfo m
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
WHERE m.gender = '0'
  AND c.cardioarrestdetected = 1;


-- =========================================================
-- 41. Get the list of female members and their cardio info
--     for those aged above 50
-- =========================================================
SELECT m.*, c.*
FROM memberinfo m
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
WHERE m.gender = '0'
  AND m.age > 50;


-- =========================================================
-- 42. Get the list of males who have blood pressure > 140
--     and have not had a heart attack
-- =========================================================
SELECT DISTINCT m.*
FROM memberinfo m
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b
  ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE m.gender = '1'
  AND b.bloodpressure > 140
  AND c.cardioarrestdetected = 0;


-- =========================================================
-- 43. Get the list of members who had a heart attack
--     from the state "Mountain Province"
-- =========================================================
SELECT DISTINCT m.*
FROM memberinfo m
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
JOIN addressinfo a
  ON m.member_id = a.memberinfo_member_id
WHERE c.cardioarrestdetected = 1
  AND a.state = 'Mountain Province';


-- =========================================================
-- 44. Get the list of male members and their diseases
--     with symptoms for those aged less than 40
-- =========================================================
SELECT DISTINCT m.firstname, m.lastname, d.*, s.*
FROM memberinfo m
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
JOIN diseasedetail d
  ON c.cardio_id = d.cardiodiagnosis_cardio_id
JOIN symptom s
  ON c.cardio_id = s.cardiodiagnosis_cardio_id
WHERE m.gender = '1'
  AND m.age < 40;


-- =========================================================
-- 45. Get the count of members from "Mountain Province"
--     aged between 50 and 60
-- =========================================================
SELECT COUNT(*) AS total_members
FROM memberinfo m
JOIN addressinfo a
  ON m.member_id = a.memberinfo_member_id
WHERE a.state = 'Mountain Province'
  AND m.age BETWEEN 50 AND 60;


-- =========================================================
-- 46. Get the count of male and female members who have
--     blood pressure > 140 and had a heart attack
-- =========================================================
SELECT m.gender, COUNT(DISTINCT m.member_id) AS total
FROM memberinfo m
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b
  ON c.cardio_id = b.cardiodiagnosis_cardio_id
WHERE b.bloodpressure > 140
  AND c.cardioarrestdetected = 1
GROUP BY m.gender;


-- =========================================================
-- 47. Get the average blood pressure of people aged
--     between 40-50 and 50-60
-- =========================================================
SELECT
  CASE
    WHEN m.age BETWEEN 40 AND 50 THEN '40-50'
    WHEN m.age BETWEEN 51 AND 60 THEN '50-60'
  END AS age_group,
  AVG(b.bloodpressure) AS avg_bp
FROM memberinfo m
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b
  ON c.cardio_id = b.cardiodiagnosis_cardio_id
GROUP BY age_group;


-- =========================================================
-- 48. Get the list of diseases for people with high
--     blood pressure (120-180), sorted by gender
-- =========================================================
SELECT m.gender, d.*
FROM memberinfo m
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
JOIN bloodtest b
  ON c.cardio_id = b.cardiodiagnosis_cardio_id
JOIN diseasedetail d
  ON c.cardio_id = d.cardiodiagnosis_cardio_id
WHERE b.bloodpressure BETWEEN 120 AND 180
ORDER BY m.gender;


-- =========================================================
-- 49. Get the count of people who have had their X-rays
--     every month from the state "Special Province"
-- =========================================================
SELECT COUNT(DISTINCT m.member_id) AS total_people
FROM memberinfo m
JOIN addressinfo a
  ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
JOIN xray x
  ON c.cardio_id = x.cardiodiagnosis_cardio_id
WHERE a.state = 'Special Province';


-- =========================================================
-- 50. Get the average age of people diagnosed with a
--     heart attack for each state, broken down by gender
-- =========================================================
SELECT a.state, m.gender, AVG(m.age) AS avg_age
FROM memberinfo m
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
JOIN addressinfo a
  ON m.member_id = a.memberinfo_member_id
WHERE c.cardioarrestdetected = 1
GROUP BY a.state, m.gender;


-- =========================================================
-- 51. Get the count of people for each state diagnosed
--     with a heart attack, slope = 2, with at least
--     one X-ray and one symptom
-- =========================================================
SELECT a.state, COUNT(DISTINCT m.member_id) AS total_people
FROM memberinfo m
JOIN addressinfo a
  ON m.member_id = a.memberinfo_member_id
JOIN cardiodiagnosis c
  ON m.member_id = c.memberinfo_member_id
JOIN wearabledevicedata w
  ON c.cardio_id = w.cardiodiagnosis_cardio_id
JOIN xray x
  ON c.cardio_id = x.cardiodiagnosis_cardio_id
JOIN symptom s
  ON c.cardio_id = s.cardiodiagnosis_cardio_id
WHERE c.cardioarrestdetected = 1
  AND w.slope = 2
GROUP BY a.state;