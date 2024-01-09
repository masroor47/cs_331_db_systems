import texttable
from copy import deepcopy


def create(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        table = [line.strip().split(",") for line in lines]
        return table


def display(table, title="", alignment="l"):
    headers = table[0]
    data = table[1:]
    alignments = [alignment] * len(headers)
    print_table(title, headers, data, alignments)


def print_table(title, headers, data, alignments):
    tt = texttable.Texttable(0)
    tt.set_cols_align(alignments)
    tt.add_rows([headers] + data, True)
    print(title)
    print(tt.draw())
    print()


def project(table, column_names=["*"]):
    if column_names == ["*"]:
        return deepcopy(table)
    
    indices = [i for i, col_name in enumerate(table[0]) if col_name in column_names]
    new_table = [[row[idx] for idx in indices] for row in table]
    return new_table


def select(table, predicate=None):
    if predicate is None:
        return table

    headers = table[0]
    new_table = [headers]
    col_idx = table[0].index(predicate[0])

    for row in table[1:]:
        if row[col_idx] == predicate[1]:
            new_table.append(row)
    return new_table


def join(table1, table2, join_pair=None):
    header1 = table1[0]
    header2 = table2[0]
    # construct new header
    if join_pair is None:
        idx1, idx2 = -1, -1
        new_header = header1 + header2
    else:
        # omit the matching column from second row
        idx1 = header1.index(join_pair[0])
        idx2 = header2.index(join_pair[1])
        new_header = header1 + header2[:idx2] + header2[idx2+1:]

    new_table = [new_header]
    for row1 in table1:
        for row2 in table2:
            if idx1 == -1 and idx2 == -1:
                # cross join
                new_table.append(row1 + row2)
            elif row1[idx1] == row2[idx2]:
                new_table.append(row1 + row2[:idx2] + row2[idx2 + 1:])

    return new_table


def sort(table, column_name):
    col_idx = table[0].index(column_name) 
    return [table[0]] + sorted(table[1:], key=lambda row: row[col_idx])


def rename(table, old_column_name, new_column_name):
    renamed_table = deepcopy(table)
    rename_idx = table[0].index(old_column_name)
    renamed_table[0][rename_idx] = new_column_name
    return renamed_table


def main():
    countries = create("countries.csv")
    cities = create("cities.csv")
    
    display(countries, "Countries Default")
    display(cities, "Cities Default")

    # Rename
    display(rename(rename(cities, "CityName", "Name"), "CityPopulation", "Population"), "Renamed Cities")

    # Project
    country_capitals = project(countries, ["Name", "Capital"])
    display(country_capitals, "Country Capitals Projeciton")

    # Select
    asian_countries = select(countries, ('Continent', 'Asia'))
    display(asian_countries, "Asian Countries")
    
    # Join
    display(join(countries, cities, ("Capital", "CityName")), "Countries JOIN Cities ON Capital = City")

    # Cross Join
    display(join(countries, cities), "Cross Join")

    # Sort
    display(sort(countries, "Name"), "Countries in Alphabetical Order")


if __name__ == "__main__":
    main()