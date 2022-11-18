import re


def get_tests_and_answers(file_tests_name: str, file_answers_name: str) -> tuple:
    tests = list(open(file_tests_name, 'r'))
    answers_file = list(open(file_answers_name, 'r'))
    answers = [str(line) for line in answers_file]
    return tests, answers


# вариант 4 2 2
def task1():
    print("1 - ввод с клавиатуры \n2 - проверка по тестам из файлов")
    type = input("Введите тип операции: ")

    if type == '1':
        emoji = input("Введите смайлик: ")
        text = input("Введите текст: ")
        # print(emoji)
        pattern = re.compile(emoji)
        print(len(re.findall(pattern, text)))
    else:
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
# В тестах сначала идут 3 буквы, затем интервал между ними, затем строка (все через пробел)
def task3():
    tests, answers = get_tests_and_answers('tests_task3.txt', 'answers_task3.txt')
    # pattern = re.compile(r'\bA.{2}B.{2}C\b')
    a = 'A'
    b = 'B'
    c = 'C'
    pattern = re.compile(rf'\b{a}.{2}{b}.{2}{c}\b')
    for i in range(len(tests)):
        a = re.findall(pattern, tests[i])
        # print(a)
        print(f"Test {i + 1} OK" if a == answers[i].split() else f"Test {i + 1} WA")


# task1()
# task2()
# task3()

