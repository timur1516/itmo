from tabulate import tabulate


def generate_result_log(method_name, result, y_real):
    log = [method_name]
    table = [
        ['x'] + result.x,
        ['y'] + result.y,
        ['y_real'] + y_real
    ]
    log.append(tabulate(table, tablefmt='grid'))
    log.append(f'Погрешность: {result.error}')
    log.append(f'Для достижения необходимой точности потребовалось разбиение на {result.n} точек')
    return "\n".join(log)


def print_result(result_log):
    separator = '=' * 50
    line = f"\n\n{separator}\n\n".join(result_log)
    print(f'\n{separator}\n\n{line}\n\n{separator}\n')


def choose_options(message, options):
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


def read_positive_integer(message):
    value = None
    while value is None:
        try:
            value = int(input(f'{message}: '))
            if value <= 1:
                print('Значение должно быть > 1')
                value = None
        except:
            print('Значение должно быть целым числом!')
            value = None
    return value


def read_float(message):
    value = None
    while value is None:
        try:
            value = float(input(f'{message}: '))
        except:
            print('Значение должно быть целым или дробным числом!')
            value = None
    return value
