from database import Database, Table



students = [
    {
        "id": "1", 
        "first_name": "Mark", 
        "last_name": "Andreessen", 
        "grade": "4"
    },
    {
        "id": "2", 
        "first_name": "Mark", 
        "last_name": "Zuck", 
        "grade": "1"
    },
    {
        "id": "3", 
        "first_name": "Elan", 
        "last_name": "Muks", 
        "grade": "3"
    },
        {
        "id": "4", 
        "first_name": "Lev", 
        "last_name": "Deych", 
        "grade": "55"
    },
        {
        "id": "5", 
        "first_name": "Anand", 
        "last_name": "Persaud", 
        "grade": "7"
    },
]

def print_table(table):
    for row in table:
        print(row)


if __name__ == "__main__":

    table = Table("Students", ["id", "first_name", "last_name", "grade"])
    print(table)

    for student_info in students:
        table.insert(student_info)
    
    print("\nAfter insertion:")
    print(table)

    print("\nSelect *")
    select_all = table.select("*")
    print_table(select_all)

    print("\nSelect id, name")
    select_name = table.select(["id", "first_name"])
    print_table(select_name)