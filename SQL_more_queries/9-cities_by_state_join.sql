-- Lists all cities in my database hbtn_0d_usa
SELECT cities.id, states.id, name
FROM cities, states
ORDER BY id ASC;