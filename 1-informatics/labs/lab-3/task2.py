import re
import random

#Вариант 4

with open('tests/tests2.txt', mode='r', encoding='utf8') as f:
    m = f.read().split('\n')
    f.close()

#Обработка тестов
n = 1.
for s in m:
    print(f'TEST #{n}')
    print(f'Входные данные: {s}')
    s1 = re.sub(r'([^\d:]|^)([0-1]\d|2[0-3])(:[0-5]\d){1,2}([^\d:]|$)', r'\1(TBD)\4', s)
    print(f'Выходные данные: {s1}')
    print()
    n += 1