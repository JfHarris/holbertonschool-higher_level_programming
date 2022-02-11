-- Import database dump from hbtn_0d_tvshows to your MySQL server: download
-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT sh.`title`, ge.`genre_id`
  FROM `tv_shows` AS sh
       LEFT JOIN `tv_show_genres` AS ge
       ON sh.`id` = ge.`show_id`
 ORDER BY sh.`title`, ge.`genre_id`;
