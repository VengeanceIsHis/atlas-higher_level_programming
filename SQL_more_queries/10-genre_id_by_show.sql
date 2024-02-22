-- SCRIPTS THAT LISTS SHOW  IN A SET DATABASE
SELECT tv_shows.title, tb_show_genres.genre_id
FROM tv_shows
ORDER BY tv_shows.title, tv_shows_genres.genre_id ASC;