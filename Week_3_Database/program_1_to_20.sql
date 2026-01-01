

-- -----------------------------------------------------
-- 1. Get all the predictions
-- -----------------------------------------------------
SELECT *
FROM cardiodiagnosis;


-- -----------------------------------------------------
-- 2. Get all the predictions for the CURRENT DAY
-- -----------------------------------------------------
SELECT *
FROM cardiodiagnosis
WHERE DATE(date) = CURRENT_DATE;

SELECT *
FROM cardiodiagnosis
WHERE DATE(date) = '2019-02-20';




-- -----------------------------------------------------
-- 3. Get all the predictions for the CURRENT DAY
--    sorted by highest probability at the top
-- -----------------------------------------------------
SELECT *
FROM cardiodiagnosis
WHERE DATE(date) = CURRENT_DATE
ORDER BY cardioarrestdetected DESC;

SELECT *
FROM cardiodiagnosis
WHERE DATE(date) = '2019-03-15'
ORDER BY cardioarrestdetected DESC;





-- -----------------------------------------------------
-- 4. Get all the UNIQUE cities
-- -----------------------------------------------------
SELECT DISTINCT city
FROM addressinfo;


-- -----------------------------------------------------
-- 5. Get all the members who are from city 'Burgos'
-- -----------------------------------------------------
SELECT m.*
FROM memberinfo m
JOIN addressinfo a
ON m.member_id = a.memberinfo_member_id
WHERE a.city = 'Burgos';


-- -----------------------------------------------------
-- 6. Get all the members who are from city 'Flora'
-- -----------------------------------------------------
SELECT m.*
FROM memberinfo m
JOIN addressinfo a
ON m.member_id = a.memberinfo_member_id
WHERE a.city = 'Flora';


-- -----------------------------------------------------
-- 7. Get the total number of blood tests done for Aisha
-- -----------------------------------------------------
SELECT COUNT(*) AS total_blood_tests
FROM bloodtest b
JOIN cardiodiagnosis c
ON b.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m
ON c.memberinfo_member_id = m.member_id
WHERE m.firstname = 'Aisha';


-- -----------------------------------------------------
-- 8. Get X-ray details of Ajay whose cardio test
--    was done on 26th January 2019
-- -----------------------------------------------------
SELECT x.*
FROM xray x
JOIN cardiodiagnosis c
ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m
ON c.memberinfo_member_id = m.member_id
WHERE m.firstname = 'Ajay'
  AND DATE(c.date) = '2019-01-26';


-- -----------------------------------------------------
-- 9. Get all the members from cities 'Burgos' and 'Flora'
-- -----------------------------------------------------
SELECT DISTINCT m.*
FROM memberinfo m
JOIN addressinfo a
ON m.member_id = a.memberinfo_member_id
WHERE a.city IN ('Burgos', 'Flora');


-- -----------------------------------------------------
-- 10. Get the total number of blood tests done for Aberson
-- -----------------------------------------------------
SELECT COUNT(*) AS total_blood_tests
FROM bloodtest b
JOIN cardiodiagnosis c
ON b.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m
ON c.memberinfo_member_id = m.member_id
WHERE m.firstname = 'Aberson';












-- =========================================================
-- 11. Get all address details for member ID M303
-- =========================================================
SELECT *
FROM addressinfo
WHERE memberinfo_member_id = 'M303';



-- =========================================================
-- 12. Get all X-ray details for cardio ID cid122
-- =========================================================
SELECT *
FROM xray
WHERE cardiodiagnosis_cardio_id = 'cid122';



-- =========================================================
-- 13. Get all symptom details whose cardio ID is
--     cid250 and cid300
-- =========================================================
SELECT *
FROM symptom
WHERE cardiodiagnosis_cardio_id IN ('cid250', 'cid300');



-- =========================================================
-- 14. Get all symptom details for the month of
--     July and year 2019
-- =========================================================
SELECT *
FROM symptom
WHERE EXTRACT(YEAR FROM date) = 2019
  AND EXTRACT(MONTH FROM date) = 7;



-- =========================================================
-- 15. Get X-ray details for the member
--     with the last name "Dailley"
-- =========================================================
SELECT x.*
FROM xray x
JOIN cardiodiagnosis c
  ON x.cardiodiagnosis_cardio_id = c.cardio_id
JOIN memberinfo m
  ON c.memberinfo_member_id = m.member_id
WHERE m.lastname = 'Dailley';



-- =========================================================
-- 16. Get wearable device data details for
--     cardio IDs between cid100 and cid200
-- =========================================================
SELECT *
FROM wearabledevicedata
WHERE cardiodiagnosis_cardio_id BETWEEN 'cid100' AND 'cid200';



-- =========================================================
-- 17. Display all cardio diagnosis details where
--     the first name starts with the letter "A"
-- =========================================================
SELECT c.*
FROM cardiodiagnosis c
JOIN memberinfo m
  ON c.memberinfo_member_id = m.member_id
WHERE m.firstname LIKE 'A%';



-- =========================================================
-- 18. Display all cardio diagnosis details where
--     the first name starts with "A" and ends with "A"
-- =========================================================
SELECT c.*
FROM cardiodiagnosis c
JOIN memberinfo m
  ON c.memberinfo_member_id = m.member_id
WHERE m.firstname LIKE 'A%A';



-- =========================================================
-- 19. Get all the members from the MemberInfo table
-- =========================================================
SELECT *
FROM memberinfo;



-- =========================================================
-- 20. Get all the addresses of members
-- =========================================================
SELECT *
FROM addressinfo;


