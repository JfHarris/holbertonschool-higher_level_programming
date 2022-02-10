-- lists number of records with same score in the table second_table
-- of database hbtn_0c_0 in your MySQL server.
SELECT `score`, COUNT(`score`) 'number' FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
