/* Project 2*/ 
/* Part 1 */
SELECT *
FROM schooldistrict
WHERE schooldistrictID = 3;

/* Part 2 */
SELECT schoolname, schooldistrictID
FROM school
WHERE schooldistrictID = 3;

/* Part 3 */
SELECT schoolname
FROM school
WHERE schoolcode LIKE '%ES%';

/* Part 4 */
SELECT *
FROM bus
WHERE schooldistrictID = 3;

/* Part 5 */
SELECT *
FROM bus
WHERE capacity > 70;

/* Part 6 */
SELECT capacity, count(*) AS Number_Of_Buses
FROM bus
GROUP BY capacity;

/* Part 7 */
/* This is sad */
SELECT *
FROM passenger
WHERE firstname = 'Kurumi';

/* Part 8 */
SELECT firstname, middlename, lastname, count(*) AS number_of_names
FROM passenger
GROUP BY firstname
ORDER BY number_of_names DESC;

/* Part 9 */ 
SELECT count(*) AS number_of_people_in_my_district
FROM passenger
WHERE schoolID = 3;

/* Part 9 part 2 */
SELECT count(*) AS females_in_my_district
FROM passenger
WHERE schoolID = 3
AND gender = 'F';