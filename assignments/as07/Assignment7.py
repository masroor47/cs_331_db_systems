# Queens COllege
# Database SYstems (CSCI 331)
# Winter 2024
# Assignment 7 Stored functions and procedures
# Masroor Khonkhodzhaev

import os
import sys
sys.path.append("..")

from dotenv import load_dotenv

import as03.Assignment3 as as3
import as05.Assignment5 as as5


def main():
    comments, queries = as5.read_queries("Assignment7.sql")
    as5.process_queries(comments, queries, "udb", "Assignment 7", add_stats=True)

    # query = "CALL run_test(100)"
    # as3.run_query(query, "Test", "udb", assignment)

    comments, queries = as5.read_queries("Analytics.sql")
    as5.process_queries(comments, queries, "meta", "Analytics", add_stats=True)

if __name__ == "__main__":
    assignment = "Assignment 7"
    main()