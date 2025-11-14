import re
import random

pattern = "=-{O"

#Подсчет смайликов без regex
def chek(s):
    cnt = 0
    for i in range(3, len(s)):
        ok = True
        for j in range(0, 4):
            if s[i-j] != pattern[len(pattern) - j - 1]:
                ok = False
                break
        if ok:
            cnt += 1
    return cnt
#Генератор тестов
def gen(n):
    s = ""
    for i in range(n):
        k = random.randint(0, len(pattern) - 1)
        s += pattern[k]
    return s

#Считывание тестов из файла
with open('tests/tests1.txt', mode='r', encoding='utf8') as f:
    m = f.read().split('\n')
    f.close()

#Обработка тестов
n = 1
for s in m:
    print(f'TEST #{n}')
    print(s)
    match = re.findall(r'=-\{O', s)
    print(f'Smiles found: {match}')
    print(f'Correct answer: {chek(s)}')
    print(f'Regex answer: {len(match)}')
    print()
    n += 1