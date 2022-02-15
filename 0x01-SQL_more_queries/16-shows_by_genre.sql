-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
-- script that lists all shows, and all genres linked to that show from hbtn_0d_tvshows
SELECT ts.`title`, ge.`name`
FROM `tv_shows` AS ts
INNER JOIN `tv_show_genres` AS sh
ON ts.`id` = sh.`show_id`
INNER JOIN `tv_genres` AS ge
ON sh.`genre_id` = g.`id`
ORDER BY ts.`title`, ge.`name`;
