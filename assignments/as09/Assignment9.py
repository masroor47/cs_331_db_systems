# Queens College
# Database Systems (CSCI 331)
# Winter 2024
# Assignment 9 - Pivot Tables
# Masroor Khonkhodzhaev

import sys
sys.path.append("..")
sys.path.append("../..")

import as05.Assignment5 as as5
from assignments import OutputUtil as ou


assn = "Assignment 9"
db = "udb"
def main():
    comments, queries = as5.read_queries("Assignment9.sql")
    as5.process_queries(comments, queries, db, assn)

    # comments, queries = as5.read_queries("Analytics.sql")
    # as5.process_queries(comments, queries, "meta", "Analytics-"+assn)

if __name__ == "__main__":
    main()