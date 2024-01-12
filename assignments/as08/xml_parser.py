student_xml = """
<?xml version="1.0" encoding="UTF-8"?>
<root>
    <title>advisor</title>
    <row>
        <s_ID>12345</s_ID>
        <i_ID>10101</i_ID>
    </row>
    <row>
        <s_ID>44553</s_ID>
        <i_ID>22222</i_ID>
    </row>
    <row>
        <s_ID>45678</s_ID>
        <i_ID>22222</i_ID>
    </row>
    <row>
        <s_ID>00128</s_ID>
        <i_ID>45565</i_ID>
    </row>
    <row>
        <s_ID>76543</s_ID>
        <i_ID>45565</i_ID>
    </row>
    <row>
        <s_ID>23121</s_ID>
        <i_ID>76543</i_ID>
    </row>
    <row>
        <s_ID>98988</s_ID>
        <i_ID>76766</i_ID>
    </row>
    <row>
        <s_ID>76653</s_ID>
        <i_ID>98345</i_ID>
    </row>
    <row>
        <s_ID>98765</s_ID>
        <i_ID>98345</i_ID>
    </row>
</root>
"""

course_xml = """
<?xml version="1.0" encoding="UTF-8"?>
<root>
<title>course</title>
<row>
<course_id>BIO-101</course_id>
<title>Intro. to Biology</title>
<dept_name>Biology</dept_name>
<credits>4</credits>
</row>
<row>
<course_id>BIO-301</course_id>
<title>Genetics</title>
<dept_name>Biology</dept_name>
<credits>4</credits>
</row>
<row>
<course_id>BIO-399</course_id>
<title>Computational Biology</title>
<dept_name>Biology</dept_name>
<credits>3</credits>
</row>
<row>
<course_id>CS-101</course_id>
<title>Intro. to Computer Science</title>
<dept_name>Comp. Sci.</dept_name>
<credits>4</credits>
</row>
<row>
<course_id>CS-190</course_id>
<title>Game Design</title>
<dept_name>Comp. Sci.</dept_name>
<credits>4</credits>
</row>
<row>
<course_id>CS-315</course_id>
<title>Robotics</title>
<dept_name>Comp. Sci.</dept_name>
<credits>3</credits>
</row>
<row>
<course_id>CS-319</course_id>
<title>Image Processing</title>
<dept_name>Comp. Sci.</dept_name>
<credits>3</credits>
</row>
<row>
<course_id>CS-347</course_id>
<title>Database System Concepts</title>
<dept_name>Comp. Sci.</dept_name>
<credits>3</credits>
</row>
<row>
<course_id>EE-181</course_id>
<title>Intro. to Digital Systems</title>
<dept_name>Elec. Eng.</dept_name>
<credits>3</credits>
</row>
<row>
<course_id>FIN-201</course_id>
<title>Investment Banking</title>
<dept_name>Finance</dept_name>
<credits>3</credits>
</row>
<row>
<course_id>HIS-351</course_id>
<title>World History</title>
<dept_name>History</dept_name>
<credits>3</credits>
</row>
<row>
<course_id>MU-199</course_id>
<title>Music Video Production</title>
<dept_name>Music</dept_name>
<credits>3</credits>
</row>
<row>
<course_id>PHY-101</course_id>
<title>Physical Principles</title>
<dept_name>Physics</dept_name>
<credits>4</credits>
</row>
</root>
"""

takes_xml = """
<?xml version="1.0" encoding="UTF-8"?>
<root>
<title>takes</title>
<row>
<ID>98988</ID>
<course_id>BIO-301</course_id>
<sec_id>1</sec_id>
<semester>Summer</semester>
<year>2018</year>
<grade>None</grade>
</row>
<row>
<ID>00128</ID>
<course_id>CS-101</course_id>
<sec_id>1</sec_id>
<semester>Fall</semester>
<year>2017</year>
<grade>A</grade>
</row>
<row>
<ID>12345</ID>
<course_id>CS-190</course_id>
<sec_id>2</sec_id>
<semester>Spring</semester>
<year>2017</year>
<grade>A</grade>
</row>
<row>
<ID>12345</ID>
<course_id>CS-315</course_id>
<sec_id>1</sec_id>
<semester>Spring</semester>
<year>2018</year>
<grade>A</grade>
</row>
<row>
<ID>12345</ID>
<course_id>CS-347</course_id>
<sec_id>1</sec_id>
<semester>Fall</semester>
<year>2017</year>
<grade>A</grade>
</row>
<row>
<ID>76543</ID>
<course_id>CS-101</course_id>
<sec_id>1</sec_id>
<semester>Fall</semester>
<year>2017</year>
<grade>A</grade>
</row>
<row>
<ID>76543</ID>
<course_id>CS-319</course_id>
<sec_id>2</sec_id>
<semester>Spring</semester>
<year>2018</year>
<grade>A</grade>
</row>
<row>
<ID>98988</ID>
<course_id>BIO-101</course_id>
<sec_id>1</sec_id>
<semester>Summer</semester>
<year>2017</year>
<grade>A</grade>
</row>
<row>
<ID>00128</ID>
<course_id>CS-347</course_id>
<sec_id>1</sec_id>
<semester>Fall</semester>
<year>2017</year>
<grade>A-</grade>
</row>
<row>
<ID>54321</ID>
<course_id>CS-101</course_id>
<sec_id>1</sec_id>
<semester>Fall</semester>
<year>2017</year>
<grade>A-</grade>
</row>
<row>
<ID>55739</ID>
<course_id>MU-199</course_id>
<sec_id>1</sec_id>
<semester>Spring</semester>
<year>2018</year>
<grade>A-</grade>
</row>
<row>
<ID>19991</ID>
<course_id>HIS-351</course_id>
<sec_id>1</sec_id>
<semester>Spring</semester>
<year>2018</year>
<grade>B</grade>
</row>
<row>
<ID>45678</ID>
<course_id>CS-319</course_id>
<sec_id>1</sec_id>
<semester>Spring</semester>
<year>2018</year>
<grade>B</grade>
</row>
<row>
<ID>98765</ID>
<course_id>CS-315</course_id>
<sec_id>1</sec_id>
<semester>Spring</semester>
<year>2018</year>
<grade>B</grade>
</row>
<row>
<ID>44553</ID>
<course_id>PHY-101</course_id>
<sec_id>1</sec_id>
<semester>Fall</semester>
<year>2017</year>
<grade>B-</grade>
</row>
<row>
<ID>45678</ID>
<course_id>CS-101</course_id>
<sec_id>1</sec_id>
<semester>Spring</semester>
<year>2018</year>
<grade>B+</grade>
</row>
<row>
<ID>54321</ID>
<course_id>CS-190</course_id>
<sec_id>2</sec_id>
<semester>Spring</semester>
<year>2017</year>
<grade>B+</grade>
</row>
<row>
<ID>12345</ID>
<course_id>CS-101</course_id>
<sec_id>1</sec_id>
<semester>Fall</semester>
<year>2017</year>
<grade>C</grade>
</row>
<row>
<ID>76653</ID>
<course_id>EE-181</course_id>
<sec_id>1</sec_id>
<semester>Spring</semester>
<year>2017</year>
<grade>C</grade>
</row>
<row>
<ID>98765</ID>
<course_id>CS-101</course_id>
<sec_id>1</sec_id>
<semester>Fall</semester>
<year>2017</year>
<grade>C-</grade>
</row>
<row>
<ID>23121</ID>
<course_id>FIN-201</course_id>
<sec_id>1</sec_id>
<semester>Spring</semester>
<year>2018</year>
<grade>C+</grade>
</row>
<row>
<ID>45678</ID>
<course_id>CS-101</course_id>
<sec_id>1</sec_id>
<semester>Fall</semester>
<year>2017</year>
<grade>F</grade>
</row>
</root>
"""

def from_xml(xml):
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
    return title, header, data



if __name__ == '__main__':
    xmls = [student_xml, course_xml, takes_xml]
    for xml in xmls:
        title, head, data = from_xml(xml)
        print(title)
        print(head)
        for row in data:
            print(row)
        print()