# Queens College
# Database Systems (CSCI 331)
# Winter 2024
# Assignment 10 - Database Design and Normalization
# Masroor Khonkhodzhaev

import sys
sys.path.append("..")
sys.path.append("../..")

import as05.Assignment5 as as5
from assignments import OutputUtil as ou


assn = "Assignment 10"
def main():
    comments, queries = as5.read_queries("Assignment10.sql")
    as5.process_queries(comments, queries, "udb", assn, debug=False)

    comments, queries = as5.read_queries("Analytics.sql")
    as5.process_queries(comments, queries, "meta", f"{assn}-Analytics")

if __name__ == "__main__":
    main()