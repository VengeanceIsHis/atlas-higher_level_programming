-- Lists all cities in my database hbtn_0d_usa
SELECT cities.id, states.name, cities.name
FROM cities, states
ORDER BY cities.id ASC;