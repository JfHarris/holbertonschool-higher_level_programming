-- lists all records of table second_table of the database
-- hbtn_0c_0 in your MySQL server.
SELECT `score`, `nam` FROM second_table WHERE `name` IS NOT NULL ORDER BY `score` DESC;
