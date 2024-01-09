

/* Summary of queries */
SELECT query_assn as assignment, COUNT(*), MIN(query_dur) AS Min_Dur, AVG(query_dur) AS Avg_Dur, MAX(query_dur) AS Max_Dur, SUM(query_dur) AS Total_Dur
FROM query
GROUP BY assignment
ORDER BY assignment;  

/* Retrieve queries for Assignment 3 */
SELECT * FROM query where query_assn = 'Assignment 3' ORDER BY query_ended LIMIT 100;

/* Retrieve queries for Assignment 4 */
SELECT * FROM query where query_assn = 'Assignment 4' ORDER BY query_ended LIMIT 100;

/* Retrieve queries for Assignment 5 */ 
SELECT * FROM query where query_assn = 'Assignment 5' ORDER BY query_ended LIMIT 100;
