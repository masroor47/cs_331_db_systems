/* Assignment 5 In-class view of all tables and columns in UDB database */
CREATE OR REPLACE view v_udb_table_columns as
select 
	TABLE_NAME, ORDINAL_POSITION, COLUMN_NAME, DATA_TYPE, coalesce(CHARACTER_MAXIMUM_LENGTH, NUMERIC_PRECISION), IS_NULLABLE
from 
	information_schema.columns
where 
	table_schema = 'udb'
ORDER BY TABLE_NAME, ORDINAL_POSITION;

/* Select everything from the new view v_udb_table_columns */
SELECT * FROM v_udb_table_columns;

/* Aggregation: retrieve number of columns per table */
select table_name, count(column_name) as columns
from v_udb_table_columns
group by table_name;