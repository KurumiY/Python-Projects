/* Project 2 Part 2 */

/* Task 1 */
select	busnumber, capacity, lift, districtname, addressline1, city, state, zipcode
from	bus, schooldistrict, address;
 
 /* Task 2 */
 select		schoolname, zipcode
 from		address, school
 order by	zipcode;
 
 /* Task 3 */
 select	*
 from	passenger
 where	homeaddress in
		(select	addressID
		 from	address
         where	addressline1 = '2482');
         
/* Task 4 */
 select districtname, count(*)
 from schooldistrict, passenger
 where schooldistrict.schooldistrictID = passenger.schoolID
 group by schooldistrictID;
 
 /* Task 5 */
select		districtname, grade, count(*)
from		passenger, schooldistrict
where 		schoolID = 3 and passenger.schoolID = schooldistrict.schooldistrictID
group by	grade;

/* Task 6 */
select	routeID, routename, starttime, endtime, meridian, route.schooldistrictID, busID, schoolname
from	route, school
where	route.schooldistrictID = school.schooldistrictID and routeID in
		(select	routeID
         from	routeschool
         where	schoolID in
				(select	schoolID
                 from	school
                 where	schooldistrictID = 3));

/* Task 7 */
select		routename, districtname, count(*) as number_of_stop
from 		route, routestop, schooldistrict
where		route.schooldistrictID = schooldistrict.schooldistrictID 
			and route.routeID = routestop.routeID
			and route.schooldistrictID = 3
group by	route.routeID
order by 	number_of_stop;