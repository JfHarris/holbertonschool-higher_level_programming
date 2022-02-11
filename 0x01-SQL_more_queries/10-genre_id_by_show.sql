-- Import database dump from hbtn_0d_tvshows to your MySQL server: download
-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, tv-show_genres.genre_id FROM tv-shows RIGHT JOIN tv_show_genres ON tv-shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
