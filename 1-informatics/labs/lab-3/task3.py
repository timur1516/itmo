import re
import random

#Вариант 2

def g(m):
    x = int(m[0])
    return str(4*x*x - 7)

with open('tests/tests3.txt', mode='r', encoding='utf8') as f:
    m = f.read().split('\n')
    f.close()

#Обработка тестов
n = 1
for s in m:
    print(f'TEST #{n}')
    print(f'Входные данные: {s}')
    s1 = re.sub(r'\d+', g, s)
    print(f'Выходные данные: {s1}')
    print()
    n += 1