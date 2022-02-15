-- Import database dump of hbtn_0d_tvshows to your MySQL server: download
-- script that lists all shows contained in database hbtn_0d_tvshows
SELECT sh.`title`, ge.`genre_id`
FROM `tv_shows` AS sh
LEFT JOIN `tv_show_genres` AS ge
ON sh.`id` = ge.`show_id`
ORDER BY sh.`title`, ge.`genre_id`;
