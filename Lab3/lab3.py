import re


def get_tests_and_answers(file_tests_name: str, file_answers_name) -> tuple:
    tests = list(open(file_tests_name, 'r'))
    answers_file = list(open(file_answers_name, 'r'))
    answers = [str(line) for line in answers_file]
    return tests, answers


# вариант 4 2 2
def task1():
    tests, answers = get_tests_and_answers('tests_task1.txt', 'answers_task1.txt')
    pattern = re.compile(r'=-{0')
    for i in range(len(tests)):
        # print(re.findall(pattern, tests[i]))
        print(f"Test {i + 1} OK" if len(re.findall(pattern, tests[i])) == int(answers[i].replace('\n', '')) else f"Test {i + 1} WA")


# вариант 4
def task2():
    tests, answers = get_tests_and_answers('tests_task2.txt', 'answers_task2.txt')

    pattern = re.compile(r'(([0-1]\d|2[0-3]):([0-5]\d:[0-5]\d))|(([0-1]\d|2[0-3]):([0-5]\d:[0-5]\d)[^:])')
    for i in range(len(tests)):
        # print(re.sub(pattern, '(TBD', tests[i]))
        print(f"Test {i + 1} OK" if re.sub(pattern, '(TBD)', tests[i]) == answers[i] else f"Test {i + 1} WA")


# вариант 4
def task3():
    tests, answers = get_tests_and_answers('tests_task3.txt', 'answers_task3.txt')

    pattern = re.compile(r'\bA.{2}B.{2}C\b')
    for i in range(len(tests)):
        a = re.findall(pattern, tests[i])
        # print(a)
        print(f"Test {i + 1} OK" if a == answers[i].split() else f"Test {i + 1} WA")


task1()
task2()
task3()

