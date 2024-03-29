# Queens College
# Masroor Khonkhodzhaev
# CSCI 331 Winter


import time
import os
import texttable
from dotenv import load_dotenv
# import mysql.connector
import pymysql


def create_connection(db):
    # conn = mysql.connector.connect(
    conn = pymysql.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db
    )
    return conn


def log_query(query_text, 
            query_desc, 
            query_db, 
            query_rows, 
            query_user, 
            query_assn, 
            query_dur, 
            conn=None):
    
    query_text = query_text.replace("'", "\\'")
    query_desc = query_desc.replace("'", "\\'").replace("\\\\", "\\")
    query = f"""
    INSERT into query 
    (query_text, query_desc, query_db, query_rows, query_user, query_assn, query_dur) 
    \nvalues ('{query_text}', '{query_desc}', '{query_db}', {query_rows}, '{query_user}', '{query_assn}', {query_dur});
    """

    new_conn = False
    if conn is None:
        new_conn = True
        conn = create_connection("meta")
        cursor = conn.cursor()

    cursor.execute(query)
    conn.commit()
    if new_conn:
        conn.close()

def call_procedure(query_text, cursor):
    proc_query = query_text[4:].strip()
    idx1 = proc_query.index('(')
    idx2 = proc_query.index(')')
    arg = int(proc_query[idx1+1 : idx2])
    proc = proc_query[:idx1]
    cursor.callproc(proc, (arg, ))


def run_query(
        query_text, 
        query_desc, 
        query_db, 
        assignment,
        query_execute_values=None,
        debug=False,
        get_cursor_desc=False):
    
    query_src = assignment
    conn = create_connection(query_db)
    cursor = conn.cursor()
    start = time.time()
    if debug: print(query_text)
    if query_text.upper().startswith("CALL"):
        call_procedure(query_text, cursor)
    else:
        if query_execute_values is None:
            cursor.execute(query_text) 
        else:
            cursor.execute(query_text, query_execute_values)
    end = time.time()
    duration = end - start
    rows = cursor.fetchall()
    conn.commit()
    log_query(query_text, query_desc, query_db, len(rows), "masroor", query_src, duration)
    conn.close()

    first_word = query_text.upper().split(None, 1)[0]
    keywords = {'SELECT', '(SELECT', 'SHOW', 'DESC'}
    if first_word not in keywords:
        return [], []
    
    headers = [desc[0] for desc in cursor.description]
    if len(rows) == 0:
        data = [[None for _ in headers]]
    else:
        data = [[str(col) for col in row] for row in rows]

    if get_cursor_desc:
        return headers, data, cursor.description
    else:
        return headers, data


def print_table(title, headers, data, alignments=None):
   if alignments is None:
       alignments = ['l'] * len(headers)
   tt = texttable.Texttable(0)
   tt.set_cols_align(alignments)
   tt.add_rows([headers] + data, header=True)
   print(title)
   print(tt.draw())


def list_db_data(conn, query, desc):
    cur = conn.cursor()
    run_query(query, desc, "udb", assignment)
    cur.execute(query)
    results = [row[0] for row in cur]
    print(desc + ":\n", results)
    return results


def preliminary(conn):
    cursor = conn.cursor()
    databases = list_db_data(conn, "SHOW DATABASES", "listing databases") 
    print()
    cursor.execute("USE udb")
    run_query("USE udb", "Make udb default", "udb", assignment)
    tables = list_db_data(conn, "SHOW TABLES", "listing tables in udb")
    print()
    conn.close()
    return tables


def create_graduates():
    query = "CREATE TABLE IF NOT EXISTS graduate (graduate_id int, graduate_name varchar(30))"
    run_query(query, "creating graduate table", "udb", assignment)

    insert_query = "insert into graduate (graduate_id, graduate_name) values (%s, %s)"
    graduates = [
        (1, "Mark"),
        (2, "Anthony"),
        (3, "Abrough"),
        (4, "Samantha"),
        (5, "Joshua"),
        (6, "Park Li"),
    ]
    for graduate in graduates:
        run_query(insert_query, "inserting into graduate", "udb", assignment, graduate)


load_dotenv()
user = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")

if __name__ == "__main__":
    assignment = "Assignment 3"
    conn = create_connection(None)

    create_graduates()
    tables = preliminary(conn)

    for table in tables:
        query = f"select * from {table}"
        desc = f"retrieve all rows from {table}" 
        headers, data = run_query(query, desc, "udb", assignment)
        print_table(f"{table} info", headers, data)
        print()

    headers, data = run_query("select * from query", "logged queries", "meta", assignment)
    print_table("query info", headers, data)
