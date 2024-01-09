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


def process_queries(file_name, db, assignment):
    with open(file_name, 'r') as file:
        text = file.read()
        queries = text.strip().split(";")
        tables = []
        for query in queries:
            if len(query) == 0:
                continue
            res = query.split("*/")
            comment, sql = res
            comment = comment.replace("/*", "").strip()
            sql = sql.strip()
            headers, data = as3.run_query(sql, comment, db, assignment)
            alignments = ['l'] * len(headers)
            types = ["S"] * len(headers)
            table = [comment, headers, types, alignments, data]
            tables.append(table)
        output_file = assignment.replace(" ", "") + "-results.html"
        ou.write_html_file_new(output_file, "TBA", tables, True, None, True)
            

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
    process_queries("Assignment4.sql", "udb", "Assignment 4")

    assignments = [f"Assignment {i}" for i in range(3, 5)]
    print(f"assignments to query: {assignments}")
    retrieve_query_log(assignments, "meta")



if __name__ == "__main__":
    assignment = "Assignment 4"
    main()


