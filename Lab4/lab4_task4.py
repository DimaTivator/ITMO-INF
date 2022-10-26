import lab4_task1 as task1
import lab4_task2 as task2
import lab4_task3 as task3
import time


start_time = time.time()
for _ in range(1000):
    task1.xml_to_json_task1("timetable.xml")
print(f'FIRST TASK: {time.time() - start_time} seconds')

start_time = time.time()
for _ in range(1000):
    task2.xml_to_json_task2("timetable.xml")
print(f'SECOND TASK: {time.time() - start_time} seconds')

start_time = time.time()
for _ in range(1000):
    task3.xml_to_json_task3("timetable.xml")
print(f'THIRD TASK: {time.time() - start_time} seconds')
