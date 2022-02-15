-- Import the database dump from hbtn_0d_tvshows
-- to your MySQL server: download
SELECT sh.`title`, ge.`genre_id`
FROM `tv_shows` AS sh
LEFT JOIN `tv_show_genres` AS ge
ON sh.`id` = ge.`show_id`
WHERE ge.`genre_id` IS NULL
ORDER BY sh.`title`, ge.`genre_id`;
