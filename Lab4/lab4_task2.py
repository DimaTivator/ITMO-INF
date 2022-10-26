import json
import xmltodict


def xml_to_json_task2(xml_file: str):
    with open(xml_file) as xml_obj:
        data_dict = xmltodict.parse(xml_obj.read())

    json_data = json.dumps(data_dict)

    with open('result2.json', 'w') as json_file:
        json_file.write(json_data)


xml_to_json_task2("timetable.xml")
