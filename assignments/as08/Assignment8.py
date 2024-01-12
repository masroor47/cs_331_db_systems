# Queens College
# Database Systems (CSCI 331)
# Winter 2024
# Assignment 8 Complex data types
# Masroor Khonkhodzhaev

import sys
sys.path.append("..")
sys.path.append("../..")

import as03.Assignment3 as as3
import as05.Assignment5 as as5
from assignments import OutputUtil as ou

# [2a] Create a Python function to_csv(headers, data) that converts the headers and data into CSV format
def to_csv(headers, data):
    s_headers = ','.join(headers)
    s_data = '\n'.join([','.join([str(col) for col in row]) for row in data])
    return s_headers + "\n" + s_data

def xml_clean(item): return str(item).replace("&", "&amp;")

# [2b] Create a Python function to_xml(headers, data) that converts the headers and data into XML format
def to_xml( title,  headers, data):
    nl = "\n"
    headers = [header.replace(" ", "") for header in headers]
    x_header = '<?xml version="1.0" encoding="UTF-8"' + '?>'
    x_title = nl + ou.create_element("title", xml_clean(title))
    content = ""
    for row in data:
        x_items = nl + "".join([ou.create_element(headers[i], xml_clean(row[i])) for i in range(len(row))])
        x_row = ou.create_element("row", x_items)
        content += x_row
    x_body = nl + ou.create_element("root", x_title + content)
    return x_header + x_body

# [2c] Create a Python function to_json(headers, data) that converts the headers and data into JSON format
def to_json(title, headers, data):
    json_rows = []
    for row in data:
        json_rows.append('{' + ','.join([f'"{header}":"{elt}"' for header, elt in zip(headers, row)]) + '},')
    # join and remove last comma
    all_rows_str = "".join(json_rows)[:-1]
    return f'{{"{title}":[{all_rows_str}]}}'

# [3a] Create a Python function from_csv(csv) that converts the csv into headers (1D) and data (2D)
def from_csv(csv: str):
    csv = csv.split("\n")
    headers = csv[0].split(',')
    data = [[item.strip() for item in row.split(',')] for row in csv[1:]]
    return headers, data

# [3b] Create a Python function from_xml(xml) that converts the xml into headers (1D) and data (2D)
def from_xml(xml: str):
    root = xml.split('<root>', 1)[-1].split('</root>')[0].strip()
    idk = root.split('</title>')
    title, body = idk[0], "".join(idk[1:])
    title = title.split('<title>')[-1]
    rows = [ pair for pair in body.split('</row>') ]
    pairs = [ [ item.strip() for item in row.split('\n')[2:-1]] for row in rows[:-1]]
    first_row = pairs[0]
    header = [elt.split('>')[0].split('<')[-1] for elt in first_row]
    data = []
    for pair in pairs:
        res_row = [elt.split('>')[1].split('<')[0] for elt in pair]
        data.append(res_row)
    return header, data

# [3c] Create a Python function from_json(json) that converts the json into headers (1D) and data (2D)
def from_json(json: str):
    title, body = json.strip().split('[')
    title = title.strip().split('"')[1]
    if len(body) < 1: return title, None, None
    body = [row.strip().split('{')[-1] for row in body.split("}")[:-2]]
    if len(body) == 0: return title, [], [] 
    header = [pair.split(':')[0].strip().replace('"','') for pair in body[0].split(',')]
    data = []
    for row in body:
        items = [item.split(':')[-1].strip().replace('"', '') for item in row.split(',')]
        data.append(items)
    return header, data

# [4] Create a Python function backup_table(name) that will 
# read the contents of the table using run_query
# determine the number of rows, i.e. len(data)
# determine the number of columns, i.e. len(headers)
# use to_csv() to convert the data to CSV
# use to_xml() to convert the data to XML
# use to_json() to convert the data to JSON
# insert this information into the new backup table.

# Note: due to space constraints, there may be issues with logging huge inserts into the existing query table. 
def backup_table(name):
    query = f"SELECT * FROM {name}"
    desc = f"Retrieve all rows from {name}"
    headers, data = as3.run_query(query, desc, db, assignment)
    csv_data = to_csv(headers, data)
    xml_data = to_xml(name, headers, data)
    json_data = to_json(name, headers, data)
    query2 = f"""
        INSERT INTO 
            backup (relation, num_rows, num_cols, csv_length, xml_length, 
                json_length, csv_data, xml_data, json_data)
        VALUES 
            ('{name}', {len(data)}, {len(headers)}, {len(csv_data)}, {len(xml_data)}, 
                {len(json_data)}, '{csv_data}', '{xml_data}', '{json_data}')"""
    desc2 = f"Save copy of table {name} in different formats"
    headers2, data2 = as3.run_query(query2, desc2, db, assignment)

# [5] Create a Python function restore_data(name, format) that will 
# read the row of the latest backup of the table/relation name
# get the request format of that backup
# use from_csv() to convert the data from CSV back to headers and data
# use from_xml() to convert the data from XML back to headers and data
# use from_json() to convert the data from JSON back to headers and data
# makes an HTML page with the headers, and data for each of three format, each appropriately labeled (They should look similar as they were originally formed from the same data)

# A query to get the latest backup row for a given relation r is:
# SELECT * FROM backup where dtm = (SELECT MAX(dtm) FROM backup where relation = r);
def restore_data(name):
    query = f"""SELECT csv_data, xml_data, json_data 
              FROM backup 
              WHERE lower(relation) = '{name.lower()}' 
                    AND dtm = (SELECT 
                            MAX(dtm) FROM backup where lower(relation) = '{name.lower()}');"""
    desc = f"Restoring the latest backup row for table {name}"
    headers, data = as3.run_query(query, desc, db, assignment)
    csv_h, csv_d = from_csv(data[0][0])
    xml_h, xml_d = from_xml(data[0][1])
    json_h, json_d = from_json(data[0][2])
    tables = []
    tables.append(make_table_for_html(csv_h, csv_d, name, "CSV"))
    tables.append(make_table_for_html(xml_h, xml_d, name, "XML"))
    tables.append(make_table_for_html(json_h, json_d, name, "JSON"))
    return tables

def make_table_for_html(headers, data, name, format):
    title = f"Restoration of data for table {name} in {format} format"
    numeric = [all([as5.is_number(data[i][j]) for i in range(len(data))]) for j in range(len(data[0]))]
    types = ["N" if numeric[j] else "S" for j in range(len(numeric))]
    alignments = ["r" if numeric[j] else "l" for j in range(len(numeric))]
    return [title, headers, types, alignments, data]


def main():
    # comments, queries = as5.read_queries("Assignment8.sql")
    # as5.process_queries(comments, queries, db, "Assignment 8", add_stats=True)

    udb_tables = [
        "advisor", 
        "classroom", 
        "course", 
        "department", 
        "instructor", 
        "prereq", 
        "section", 
        "student",
        "takes",
        "teaches", 
        "time_slot"]

    for t in udb_tables:
        backup_table(t)

    html_tables = []
    for t in udb_tables:
        html_tables.extend(restore_data(t))
    output_file = assignment.replace(" ", "") + '-restoration.html'
    title = f"Restoration of all original university database tables"
    ou.write_html_file_new(output_file, title, html_tables, True, None, True)

    comments, queries = as5.read_queries("Analytics.sql")
    as5.process_queries(comments, queries, "udb", "Analytics-"+assignment, add_stats=True)

if __name__ == "__main__":
    assignment = "Assignment 8"
    db = "udb"
    main()