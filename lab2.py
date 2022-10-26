def decode(code: str):
    r1, r2, i1, r3, i2, i3, i4 = code
    # Подсчет контрольных сумм
    s1 = (int(r1) + int(i1) + int(i2) + int(i4)) % 2
    s2 = (int(r2) + int(i1) + int(i3) + int(i4)) % 2
    s3 = (int(r3) + int(i2) + int(i3) + int(i4)) % 2
    code_table = {
        '000': 0,
        '001': 0,
        '010': 0,
        '011': 3,
        '100': 0,
        '101': 2,
        '110': 1,
        '111': 4
    }
    code = [i1, i2, i3, i4]
    control_num = str(s1) + str(s2) + str(s3)
    if code_table[control_num]:
        print(f'Обнаружена ошибка в бите {code_table[control_num]}')
        if code[code_table[control_num] - 1] == '0':
            code[code_table[control_num] - 1] = '1'
        else:
            code[code_table[control_num] - 1] = '0'
        print(f"Исходный код: {''.join(code)}")
    else:
        print(f"Код {''.join(code)} передан без ошибок")


s = input('Введите код Хэмминга (7, 4): ')
if len(s) != 7:
    print('Некорректный ввод!')
    quit()
decode(s)
