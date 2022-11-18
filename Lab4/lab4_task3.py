import re


def make_text(tag: str) -> str:
    return tag.replace('<', '').replace('>', '')


def check_open_tag(s: str) -> bool:
    return len(re.findall(re.compile(r'<[^/]*>'), s)) > 0


def check_close_tag(s: str) -> bool:
    return len(re.findall(re.compile(r'</.*>'), s)) > 0


def xml_to_json(xml_file: str):
    xml_obj = open(xml_file)

    xml_list = []

    for line in [''.join(line.replace('\t', '').replace('\n', '')) for line in xml_obj]:

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
                    xml_list.append(text)
                    text = ''

            if not is_open_tag and not is_close_tag:
                text += line[i]

            if line[i] == '>':
                if is_close_tag:
                    is_close_tag = False
                    xml_list.append(close_tag)
                    close_tag = ''
                else:
                    is_open_tag = False
                    xml_list.append(open_tag)
                    open_tag = ''

            if i == len(line) - 1 and len(text):
                xml_list.append(text)

    res = open('result3.json', 'w')
    res.write('{\n')

    indent = 0
    for i in range(1, len(xml_list)):
        line = xml_list[i]
        text = ''
        is_text = False

        if check_open_tag(line):
            if check_open_tag(xml_list[i + 1]):
                text = '"' + make_text(line) + '"' + ': {\n'
            else:
                text = '"' + make_text(line) + '": '
            indent += check_open_tag(xml_list[i - 1])
            res.write(indent * 2 * ' ' + text)

        elif check_close_tag(line):
            if check_close_tag(xml_list[i - 1]):
                if '<' not in xml_list[i - 2] and not check_close_tag(xml_list[i + 1]):
                    text = '},\n'
                else:
                    text = '}\n'
                indent -= 1
                res.write(indent * 2 * ' ' + text)

        else:
            is_text = True
            if check_close_tag(xml_list[i + 1]) and not check_close_tag(xml_list[i + 2]):
                text = '"' + line + '",\n'
            else:
                text = '"' + line + '"\n'
            res.write(text)

    res.write('}')
    res.close()
    xml_obj.close()


xml_to_json("timetable.xml")

