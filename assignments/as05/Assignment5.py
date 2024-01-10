# Queens COllege
# Database SYstems (CSCI 331)
# Winter 2024
# Assignment 5 Tables, Views, and Meta-Data
# Masroor Khonkhodzhaev


import os
import sys

from dotenv import load_dotenv

sys.path.append("..")
import as03.Assignment3 as as3
import OutputUtil as ou


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_number(x):
	return isinstance(x, int) or isinstance(x, float) or (isinstance(x, str) and is_float(x))


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


def process_queries(comments, queries, db, assignment, add_stats=False):
    tables = []
    for i in range(len(queries)):
        query = queries[i]
        comment = comments[i]
        print(query)
        print()
        headers, data = as3.run_query(query, comment, db, assignment)
        if len(headers) == 0: continue
        numeric = [all( [is_number(data[i][j]) for i in range(len(data))] ) for j in range(len(data[0]))]
        alignments = ["r" if numeric[j] else "l" for j in range(len(numeric))]
        types = ["N" if n else "S" for n in numeric]
        # print(numeric)
        # for j in range(len(numeric)):
        #     for r in range(len(data)):
        #         if numeric[j] == False: continue
        #         print(j, r)
        #         data[r][j] = float(data[r][j])

        # if add_stats:
        #     stat_cols = [j for j in range(len(numeric)) if numeric[j]]
        #     print(f"{query}\n{stat_cols}\n{data}\n")
        #     ou.add_stats(data, stat_cols, 0, 3, True)

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


