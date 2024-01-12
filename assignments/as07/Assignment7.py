# Queens COllege
# Database SYstems (CSCI 331)
# Winter 2024
# Assignment 7 Stored functions and procedures
# Masroor Khonkhodzhaev

import sys
sys.path.append("..")

import as05.Assignment5 as as5


def main():
    comments, queries = as5.read_queries("Assignment7.sql")
    as5.process_queries(comments, queries, "udb", "Assignment 7", add_stats=True)

    comments, queries = as5.read_queries("Analytics.sql")
    as5.process_queries(comments, queries, "meta", "Analytics", add_stats=True)

if __name__ == "__main__":
    assignment = "Assignment 7"
    main()