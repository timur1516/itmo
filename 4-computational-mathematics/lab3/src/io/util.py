from typing import List

from lab3.dto.result import Result


def round_(n: float, precision: int):
    return "{:.{}f}".format(n, precision)


def print_result(result: Result):
    print(f'Найденное значение интеграла: {result.value}')
    print(f'Число разбиения интервала интегрирования для достижения требуемой точности: {result.iterations}')


def choose_options(message: str, options: List[str]) -> int:
    options_str = ''.join(f'{i + 1} -> {val}\n' for i, val in enumerate(options))[:-1]
    print(f'{message}:\n{options_str}')
    result = None
    while result is None:
        try:
            result = int(input())
            if result not in range(1, len(options) + 1):
                print(f'Выберите один из вариантов:\n{options_str}')
                result = None
                continue
            break
        except:
            print('Значение должно быть числом. Попробуйте снова')
    return result


def read_float(message: str) -> float:
    value = None
    while value is None:
        try:
            value = float(input(f'{message}: '))
            break
        except:
            print('Значение должны быть целым или дробным числом!')
    return value
