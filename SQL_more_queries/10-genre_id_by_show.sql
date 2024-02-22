-- SCRIPTS THAT LISTS SHOW  IN A SET DATABASE
SELECT tv_shows.title, tb_show_genres.genre_id
FROM hbtn_0d_tvshows
ORDER BY tv_shows.title, tv_shows_genres.genre_id ASC;