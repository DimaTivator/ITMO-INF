symbols = '0123456789abcdefghijklmnopqrstuvwxyz'


def factorial(n: int) -> int:
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


# перевод из 10 в p
def from_10_to_p(n: str, p: int) -> str:
    n = int(n)
    res = ''
    while n > 0:
        res += symbols[n % p]
        n //= p
    return res[::-1]


def get_number(a: str) -> int:
    return symbols.index(a)


# перевод из p в s
def from_p_to_s(n: str, p: int, s: int) -> str:
    return from_10_to_p(str(int(n, p)), s)


# перевод из 10 в факториальную
def from_10_to_fact(n: str) -> str:
    n = int(n)
    m = 2
    res = ''
    while n // m:
        res += str(n % m)
        n //= m
        m += 1
    return str(n % m) + res[::-1]


def from_fact_to_10(n: str) -> int:
    res = 0
    for i in range(len(n)):
        res += int(n[i]) * factorial(len(n) - i)
    return res


# проверки валидности введенного числа
def check(n: str, p: int) -> bool:
    return 2 <= p <= 36 and all(x in symbols and get_number(x) < p for x in n.lower())


def check_fact(n: str) -> bool:
    return all(n[i].isdigit() and int(n[i]) <= len(n) - i for i in range(len(n)))

print('1) перевод из системы счисления с основанием p в систему счисления с основанием s')
print('2) перевод из факториальной системы счисления в десятичную')
print('3) перевод из десятичной системы счисления в факториальную')

num = input('Введите номер операции: ')

if int(num) <= 0 or int(num) > 3 or not num.isdigit():
    print('Некорректный номер операции!')
    quit()

num = int(num)

if num == 1:
    n, p, s = map(str, input('Введите через пробел число, его систему счисления и желаемую систему счисления: ').split())
    p = int(p)
    s = int(s)
    if not check(n, p) or not 2 <= s <= 36:
        print('Некорректный ввод!')
        quit()
    print('Результат: ', from_p_to_s(n, p, s))

elif num == 2:
    n = input('Введите число в факториальной системе счисления: ')
    if not check_fact(n):
        print('Некорректный ввод!')
        quit()
    print('Результат: ', from_fact_to_10(n))

else:
    n = input('Введите число в десятичной системе счисления: ')
    if not check(n, 10):
        print('Некорректный ввод!')
        quit()
    print('Результат: ', from_10_to_fact(n))

