# Queens College
# Database Systems (CSCI 331)
# Winter 2024
# Assignment 9 - Pivot Tables
# Masroor Khonkhodzhaev

import sys
sys.path.append("..")
sys.path.append("../..")

import as03.Assignment3 as as3
import as05.Assignment5 as as5
from assignments import OutputUtil as ou


# SELECT product_name,
# SUM(CASE WHEN store_location = 'North' THEN num_sales ELSE 0 END) AS north,
# SUM(CASE WHEN store_location = 'Central' THEN num_sales ELSE 0 END) AS central,
# SUM(CASE WHEN store_location = 'South' THEN num_sales ELSE 0 END) AS south,
# SUM(CASE WHEN store_location = 'West' THEN num_sales ELSE 0 END) AS west
# FROM product_sales
# GROUP BY product_name;
def pivot_table(table, col_x, col_y, col_val):
    query = f"SELECT DISTINCT {col_x} from {table}"
    desc = f"Get all distinct values of {col_x} from table for pivot table"
    headers, data = as3.run_query(query, desc, "udb", assn)

    query2 = f"SELECT {col_y}, " 
    query2 += ",\n".join(
        f"SUM(CASE WHEN {col_x} = '{row[0]}' THEN {col_val} ELSE 0 END) AS {row[0].replace('.', '_').replace(' ', '')}" 
        for row in data
    )
    query2 +=  f" FROM {table} GROUP BY {col_y}"
    
    desc2 = f"Build a pivot table {table} for {col_x}, {col_y}"
    headers2, data2 = as3.run_query(query2, desc2, "udb", assn)

    numeric = [all( [as5.is_number(data2[i][j]) for i in range(len(data2))] ) for j in range(len(data2[0]))]
    alignments = ["r" if numeric[j] else "l" for j in range(len(numeric))]
    types = ["N" if n else "S" for n in numeric]
    table = [desc2, headers2, types, alignments, data2]
    return table


assn = "Assignment 9"
db = "udb"
def main():
    # comments, queries = as5.read_queries("Assignment9.sql")
    # as5.process_queries(comments, queries, db, assn)

    examples = [
        ('product_sales', 'product_name', 'store_location', 'num_sales'),
        ('instructor', 'dept_name', 'name', 'salary'),
    ]

    html_tables = []
    for example in examples:
        html_tables.append(pivot_table(*example))

    output_file = assn.replace(" ", "") + '-pivot-tables.html'
    title = f"Pivot tables for select examples"
    ou.write_html_file_new(output_file, title, html_tables, True, None, True)

    comments, queries = as5.read_queries("Analytics.sql")
    as5.process_queries(comments, queries, "meta", "Analytics-"+assn)

if __name__ == "__main__":
    main()