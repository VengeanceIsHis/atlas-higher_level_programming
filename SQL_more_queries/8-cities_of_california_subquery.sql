-- CREATE A NEW TABLE REFERENCING CALI
SELECT citites.city_name
FROM cities
WHERE states.state_name = 'California'
ORDER BY cities.id ASC;