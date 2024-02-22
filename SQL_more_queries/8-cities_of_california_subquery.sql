-- CREATE A NEW TABLE REFERENCING CALI
SELECT citites.city_name
FROM cities
JOIN states ON cities.state_id = states.id
WHERE states.state_name = 'California'
ORDER BY cities.id ASC;