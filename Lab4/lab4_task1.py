def make_text(tag: str) -> str:
    return tag.replace('<', '').replace('>', '')


def make_beautiful_xml(xml_file: str):
    xml_obj = open(xml_file)
    result_xml = open('beautiful_xml.xml', 'w')

    xml_list = []
    for line in xml_obj:
        xml_list.append(''.join([symbol for symbol in line if symbol not in ['\n', '\t']]))

    result_list = []

    for line in xml_list:

        is_open_tag = False
        is_close_tag = False
        open_tag = ''
        close_tag = ''
        text = ''

        for i in range(len(line)):

            if is_open_tag:
                open_tag += line[i]

            if is_close_tag:
                close_tag += line[i]

            if line[i] == '<':
                if line[i + 1] == '/':
                    is_close_tag = True
                    close_tag += line[i]
                else:
                    is_open_tag = True
                    open_tag += line[i]

                if len(text):
                    result_list.append(text + '\n')
                    text = ''

            if not is_open_tag and not is_close_tag:
                text += line[i]

            if line[i] == '>':
                if is_close_tag:
                    is_close_tag = False
                    result_list.append(close_tag + '\n')
                    close_tag = ''
                else:
                    is_open_tag = False
                    result_list.append(open_tag + '\n')
                    open_tag = ''

            if i == len(line) - 1 and len(text):
                result_list.append(text + '\n')

    indent = -1
    result_xml.write(result_list[0])

    for i in range(1, len(result_list)):

        if '<' in result_list[i] and '</' not in result_list[i]:
            if '</' not in result_list[i - 1]:
                indent += 1

        elif '</' in result_list[i]:
            indent -= 1

        else:
            indent += 1

        result_xml.write(indent * '\t' + result_list[i])


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
                res.write(indent * ' ' + '"' + make_text(s) + '": ')
            else:
                res.write(indent * ' ' + '"' + make_text(s) + '": {\n')

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


make_beautiful_xml("timetable.xml")
xml_to_json_task1("beautiful_xml.xml")
