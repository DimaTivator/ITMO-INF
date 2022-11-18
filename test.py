import re


letter1 = 'A'
letter2 = 'B'
letter3 = 'C'
ln = '1'
pattern = re.compile(r'\b' + letter1 + r'.{' + ln + r'}' + letter2 + r'.{' + ln + r'}' + letter3 + r'\b')
print(pattern)
s = input()
print(re.findall(pattern, s))

