import re


def xml_to_json_task3(xml_file: str):
    res = open('result3.json', 'w')
    xml_obj = open(xml_file)

    res.write('{\n')

    xml_list = []
    for line in xml_obj:
        xml_list.append(''.join([symbol for symbol in line if symbol != '\n']))

    open_tag = re.compile(r'<[^/]*>')
    close_tag = re.compile(r'</.*>')
    text = re.compile(r'[^<]*')

    tags_stack = []
    for i in range(1, len(xml_list)):
        s = xml_list[i]
        indent = s.count('\t') * 2 + 2
        s = s.replace('\t', '')

        if len(re.findall(open_tag, s)):
            tags_stack.append(s)
            if len(re.findall(open_tag, xml_list[i + 1])) == 0:
                res.write(indent * ' ' + '"' + s.replace('<', '').replace('>', '') + '": ')
            else:
                res.write(indent * ' ' + '"' + s.replace('<', '').replace('>', '') + '": {\n')

        elif len(re.findall(close_tag, s)):
            tags_stack.pop()
            if len(re.findall(close_tag, xml_list[i - 1])):
                if '<' not in xml_list[i - 2] and '</' not in xml_list[i + 1]:
                    res.write(indent * ' ' + '},\n')
                else:
                    res.write(indent * ' ' + '}\n')

        else:
            if len(re.findall(close_tag, xml_list[i + 1])) and len(re.findall(close_tag, xml_list[i + 2])) == 0:
                res.write('"' + s + '",' + '\n')
            else:
                res.write('"' + s + '"' + '\n')

    res.write('}')

    res.close()
    xml_obj.close()


xml_to_json_task3("timetable.xml")
