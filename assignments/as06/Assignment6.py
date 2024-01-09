# Queens COllege
# Database SYstems (CSCI 331)
# Winter 2024
# Assignment 4 Query runner, tracker, visualizer
# Masroor Khonkhodzhaev

import os
import sys
sys.path.append("..")

from dotenv import load_dotenv

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
        table = [comment, headers, types, alignments, data]
        tables.append(table)
    output_file = assignment.replace(" ", "") + "-results.html"
    ou.write_html_file_new(output_file, "TBA", tables, True, None, True)



def main():
    comments, queries = read_queries("Assignment6.sql")
    process_queries(comments, queries, "udb", "Assignment 4", add_stats=True)

    # assignments = [f"Assignment {i}" for i in range(3, 5)]
    # retrieve_query_log(assignments, "meta")

    comments, queries = read_queries("Analytics.sql")
    process_queries(comments, queries, "meta", "Analytics", add_stats=True)

if __name__ == "__main__":
    assignment = "Assignment 6"
    main()
