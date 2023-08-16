-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres
    JOIN tv_show_genres
    ON id = genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;

show tables;
SELECT * FROM tv_genres;
SELECT * FROM tv_show_genres;
SELECT * FROM tv_shows;
