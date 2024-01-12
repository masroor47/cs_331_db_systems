course = '{"course": [{"title": "Intro. to Biology", "credits": "4", "course_id": "BIO-101", "dept_name": "Biology"}, {"title": "Genetics", "credits": "4", "course_id": "BIO-301", "dept_name": "Biology"}, {"title": "Computational Biology", "credits": "3", "course_id": "BIO-399", "dept_name": "Biology"}, {"title": "Intro. to Computer Science", "credits": "4", "course_id": "CS-101", "dept_name": "Comp. Sci."}, {"title": "Game Design", "credits": "4", "course_id": "CS-190", "dept_name": "Comp. Sci."}, {"title": "Robotics", "credits": "3", "course_id": "CS-315", "dept_name": "Comp. Sci."}, {"title": "Image Processing", "credits": "3", "course_id": "CS-319", "dept_name": "Comp. Sci."}, {"title": "Database System Concepts", "credits": "3", "course_id": "CS-347", "dept_name": "Comp. Sci."}, {"title": "Intro. to Digital Systems", "credits": "3", "course_id": "EE-181", "dept_name": "Elec. Eng."}, {"title": "Investment Banking", "credits": "3", "course_id": "FIN-201", "dept_name": "Finance"}, {"title": "World History", "credits": "3", "course_id": "HIS-351", "dept_name": "History"}, {"title": "Music Video Production", "credits": "3", "course_id": "MU-199", "dept_name": "Music"}, {"title": "Physical Principles", "credits": "4", "course_id": "PHY-101", "dept_name": "Physics"}]}'

student_no_fmt = '{"student": [{"ID": "00128", "name": "Zhang", "tot_cred": "102", "dept_name": "Comp. Sci."}, {"ID": "12345", "name": "Shankar", "tot_cred": "32", "dept_name": "Comp. Sci."}, {"ID": "19991", "name": "Brandt", "tot_cred": "80", "dept_name": "History"}, {"ID": "23121", "name": "Chavez", "tot_cred": "110", "dept_name": "Finance"}, {"ID": "44553", "name": "Peltier", "tot_cred": "56", "dept_name": "Physics"}, {"ID": "45678", "name": "Levy", "tot_cred": "46", "dept_name": "Physics"}, {"ID": "54321", "name": "Williams", "tot_cred": "54", "dept_name": "Comp. Sci."}, {"ID": "55739", "name": "Sanchez", "tot_cred": "38", "dept_name": "Music"}, {"ID": "70557", "name": "Snow", "tot_cred": "0", "dept_name": "Physics"}, {"ID": "76543", "name": "Brown", "tot_cred": "58", "dept_name": "Comp. Sci."}, {"ID": "76653", "name": "Aoi", "tot_cred": "60", "dept_name": "Elec. Eng."}, {"ID": "98765", "name": "Bourikas", "tot_cred": "98", "dept_name": "Elec. Eng."}, {"ID": "98988", "name": "Tanaka", "tot_cred": "120", "dept_name": "Biology"}]}'

student = """
{
  "student": [
    {
      "ID": "00128",
      "name": "Zhang",
      "tot_cred": "102",
      "dept_name": "Comp. Sci."
    },
    {
      "ID": "12345",
      "name": "Shankar",
      "tot_cred": "32",
      "dept_name": "Comp. Sci."
    },
    {
      "ID": "19991",
      "name": "Brandt",
      "tot_cred": "80",
      "dept_name": "History"
    },
    {
      "ID": "23121",
      "name": "Chavez",
      "tot_cred": "110",
      "dept_name": "Finance"
    },
    {
      "ID": "44553",
      "name": "Peltier",
      "tot_cred": "56",
      "dept_name": "Physics"
    },
    {
      "ID": "45678",
      "name": "Levy",
      "tot_cred": "46",
      "dept_name": "Physics"
    },
    {
      "ID": "54321",
      "name": "Williams",
      "tot_cred": "54",
      "dept_name": "Comp. Sci."
    },
    {
      "ID": "55739",
      "name": "Sanchez",
      "tot_cred": "38",
      "dept_name": "Music"
    },
    {
      "ID": "70557",
      "name": "Snow",
      "tot_cred": "0",
      "dept_name": "Physics"
    },
    {
      "ID": "76543",
      "name": "Brown",
      "tot_cred": "58",
      "dept_name": "Comp. Sci."
    },
    {
      "ID": "76653",
      "name": "Aoi",
      "tot_cred": "60",
      "dept_name": "Elec. Eng."
    },
    {
      "ID": "98765",
      "name": "Bourikas",
      "tot_cred": "98",
      "dept_name": "Elec. Eng."
    },
    {
      "ID": "98988",
      "name": "Tanaka",
      "tot_cred": "120",
      "dept_name": "Biology"
    }
  ]
}"""

may_fail = """
{
    "HEY": []
}
"""

also_may_fail = """
{
"": []
}"""

def from_json(json):
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
    return title, header, data



if __name__ == '__main__':
    jsons = [student, student_no_fmt, course, may_fail, also_may_fail]
    for json in jsons:
        title, header, data = from_json(json)
        print(f"{title = }")
        print(f"{header = }")
        print("data: ")
        for row in data:
            print(row)
        print()