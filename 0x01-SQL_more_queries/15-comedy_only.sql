-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
-- script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT ts.`title`
FROM `tv_shows` AS ts
INNER JOIN `tv_show_genres` AS sh
ON ts.`id` = s.`show_id`
INNER JOIN `tv_genres` AS ge
ON ge.`id` = sh.`genre_id`
WHERE ge.`name` = "Comedy"
ORDER BY ts.`title`;
