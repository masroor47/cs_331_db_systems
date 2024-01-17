# Queens COllege
# Database SYstems (CSCI 331)
# Winter 2024
# Assignment 5 Tables, Views, and Meta-Data
# Masroor Khonkhodzhaev

import sys
sys.path.append("..")
sys.path.append("../..")

import as03.Assignment3 as as3
from assignments import OutputUtil as ou


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_number(x):
	return isinstance(x, int) or isinstance(x, float) or (isinstance(x, str) and is_float(x))

# [1] Define a function get_ruler(length) that will create a "ruler" 
# (i.e. numeric column headings) used to measure the positions and total space
def get_ruler_for_html(length, for_html=False):
    ruler1 = "".join([str(10*i).rjust(10, ' ') for i in range(1, 2+int(length/10))])
    ruler1 = ruler1.replace(' ', '&nbsp;')
    ruler2 = "0123456789" * (1+ int(length/10))
    return ruler1 + "<br>" + ruler2


def read_queries(file_name):
    with open(file_name, 'r') as file:
        comments = []
        sqls = []
        text = file.read()
        queries = text.strip().split(";")
        for query in queries:
            if len(query) == 0:
                continue
            if "*/" in query:
                comment, sql = query.split("*/")
                comment = comment.replace("/*", "").strip()
            else:
                comment = f"Query from: '{file_name}'"
                sql = query
            sql = sql.strip()
            if "CREATE FUNCTION" in sql.upper() or "CREATE PROCEDURE" in sql.upper():
                sql = sql.replace("##", ";")
                print(f"REPLACED ## {sql}")
            comments.append(comment)
            sqls.append(sql)
    return comments, sqls


def process_queries(
            comments, 
            queries, 
            db, 
            assignment, 
            add_stats=False, 
            debug=False,
            format=""):
    tables = []
    for query, comment in zip(queries, comments):
        if format in ['F', 'V']:
            headers, data, cursor_desc = as3.run_query(query, comment, db, assignment, debug=debug, get_cursor_desc=True)
            print(cursor_desc)

            headers.append(("Fixed" if format == 'F' else "Variable") + '-Length Format')
            col_widths = [desc[3] for desc in cursor_desc]
            for row in data:
                if format == 'F':
                    record = "".join([str(row[i]).ljust(col_wid, ' ') for i, col_wid in enumerate(col_widths)])
                    record = record.replace(' ', '&nbsp;')
                else:
                    record = "|".join([str(row[i]) for i in range(len(col_widths))])
                ruler = "<tt>"  + get_ruler_for_html(sum(col_widths)) + '<br>' + record + "</tt>"
                row.append(ruler)
        else:
            headers, data = as3.run_query(query, comment, db, assignment, debug=debug)
        if len(headers) == 0: continue
        numeric = [all( [is_number(data[i][j]) for i in range(len(data))] ) for j in range(len(data[0]))]
        alignments = ["r" if numeric[j] else "l" for j in range(len(numeric))]
        types = ["N" if n else "S" for n in numeric]
        table = [comment, headers, types, alignments, data]
        tables.append(table)
    output_file = assignment.replace(" ", "") + "-results.html"
    ou.write_html_file_new(output_file, assignment, tables, True, None, True)
            

def retrieve_query_log(assignments, db):
    tables = []
    for _assignment in assignments:
        sql = f"SELECT * FROM query WHERE query_assn = '{_assignment}'"
        desc = f"retrieve all queries executed for {_assignment}"
        headers, data = as3.run_query(sql, desc, db, assignments[-1])
        alignments = ['l'] * len(headers)
        types = ['S'] * len(headers)
        table = [desc, headers, types, alignments, data]
        tables.append(table)
    output_file = assignment.replace(" ", "") + "-log.html"
    title = "All queries for assignments to dat"
    ou.write_html_file_new(output_file, title, tables, True, None, True)


def main():
    comments, queries = read_queries("Assignment4.sql")
    process_queries(comments, queries, "udb", "Assignment 4", add_stats=True)

    comments, queries = read_queries("Assignment5.sql")
    process_queries(comments, queries, "udb", "Assignment 5", add_stats=True)

    # assignments = [f"Assignment {i}" for i in range(3, 5)]
    # retrieve_query_log(assignments, "meta")

    comments, queries = read_queries("Analytics.sql")
    process_queries(comments, queries, "meta", "Analytics", add_stats=True)

if __name__ == "__main__":
    assignment = "Assignment 5"
    main()


