-- SCRIPTS THAT LISTS SHOW  IN A SET DATABASE
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;