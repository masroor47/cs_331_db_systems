# Queens College
# Database Systems (CSCI 331)
# Winter 2024
# Assignment 6 DDL and DML Practice
# Masroor Khonkhodzhaev

import sys
sys.path.append("..")

import as05.Assignment5 as as5

def main():
    comments, queries = as5.read_queries("Assignment6.sql")
    as5.process_queries(comments, queries, "udb", "Assignment 6", add_stats=True)

    comments, queries = as5.read_queries("Analytics.sql")
    as5.process_queries(comments, queries, "meta", "Analytics", add_stats=True)

if __name__ == "__main__":
    assignment = "Assignment 6"
    main()
