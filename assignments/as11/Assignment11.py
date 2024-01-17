# Queens College
# Database Systems (CSCI 331)
# Winter 2024
# Assignment 11 - Database Record Storage
# Masroor Khonkhodzhaev

import sys
sys.path.append("..")
sys.path.append("../..")

import as05.Assignment5 as as5
from assignments import OutputUtil as ou



assn = "Assignment 11"
def main():
    comments, queries = as5.read_queries("Assignment11.sql")
    as5.process_queries(comments, queries, "udb", f'{assn}-fixed', debug=False, format="F")
    as5.process_queries(comments, queries, "udb", f'{assn}-variable', debug=False, format="V")

    comments, queries = as5.read_queries("Analytics.sql")
    as5.process_queries(comments, queries, "meta", f"{assn}-analytics")


if __name__ == '__main__':
    main()

