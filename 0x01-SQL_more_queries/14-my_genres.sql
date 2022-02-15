-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
-- script that uses hbtn_0d_tvshows database to lists all genres of show Dexter
SELECT ge.`name`
FROM `tv_genres` AS ge
INNER JOIN `tv_show_genres` AS sh
ON ge.`id` = sh.`genre_id`
INNER JOIN `tv_shows` AS ts
ON ts.`id` = sh.`show_id`
WHERE ts.`title` = "Dexter"
ORDER BY ge.`name`;
