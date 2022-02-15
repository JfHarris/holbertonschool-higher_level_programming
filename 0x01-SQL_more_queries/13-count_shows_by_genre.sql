-- Import the database dump from hbtn_0d_tvshows
-- to your MySQL server: download
SELECT ge.`name` AS `genre`,
COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS ge
INNER JOIN `tv_show_genres` AS ts
ON ge.`id` = t.`genre_id`
GROUP BY ge.`name`
ORDER BY `number_of_shows` DESC;
