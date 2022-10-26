import json
import xmltodict
import re
import time


def xml_to_json_task1(xml_file: str):
    res = open('result.json', 'w')
    xml_obj = open(xml_file)

    res.write('{\n')

    xml_list = []
    for line in xml_obj:
        xml_list.append(''.join([symbol for symbol in line if symbol != '\n']))

    tags_stack = []
    for i in range(1, len(xml_list)):
        s = xml_list[i]
        indent = s.count('\t') * 2 + 2
        s = s.replace('\t', '')

        if '<' in s and '</' not in s:
            tags_stack.append(s)
            if '<' not in xml_list[i + 1]:
                res.write(indent * ' ' + '"' + s.replace('<', '').replace('>', '') + '": ')
            else:
                res.write(indent * ' ' + '"' + s.replace('<', '').replace('>', '') + '": {\n')

        elif '</' in s:
            tags_stack.pop()
            if '</' in xml_list[i - 1]:
                if '<' not in xml_list[i - 2] and '</' not in xml_list[i + 1]:
                    res.write(indent * ' ' + '},\n')
                else:
                    res.write(indent * ' ' + '}\n')

        else:
            if '</' in xml_list[i + 1] and '</' not in xml_list[i + 2]:
                res.write('"' + s + '",' + '\n')
            else:
                res.write('"' + s + '"' + '\n')

    res.write('}')

    res.close()
    xml_obj.close()


xml_to_json_task1("timetable.xml")