-- CREATE A NEW TABLE REFERENCING CALI
SELECT city_name
FROM cities
WHERE state_name = 'California'
ORDER BY cities.id ASC;