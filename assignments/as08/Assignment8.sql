DROP TABLE IF EXISTS backup;

/* Assignment 8, [1] Create a new table "backup" with the following columns and datatypes 
backup_id (int, autoincrement)
relation (varchar)
rows (int)
cols (int)
csv_lenth (int)
xml_length (int)
json_length (int)
csv_data (clob or large varchar))
xml_data (clob or large varchar)
json_data (JSON)
dtm (timestamp)
*/

CREATE TABLE backup(
    backup_id           INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    relation            VARCHAR(25), 
    num_rows            INT,
    num_cols            INT,
    csv_length           INT,
    xml_length          INT,
    json_length         INT,
    csv_data            LONGTEXT,
    xml_data            LONGTEXT,
    json_data           JSON,
    dtm                 DATETIME DEFAULT CURRENT_TIMESTAMP
);

/* Assignment 8, [7] Create a view v_table_backups that has a list of backups without the actual csv_data, xml_data, and json_data */

CREATE OR REPLACE VIEW v_table_backups AS
    (SELECT 
        backup_id, 
        relation AS table_name, 
        num_rows,
        num_cols AS columns,
        csv_length,
        xml_length,
        json_length,
        dtm AS date_or_something
    FROM backup
    ORDER BY relation, dtm);

/* Selecting from v_table_backups view */
SELECT * FROM v_table_backups;