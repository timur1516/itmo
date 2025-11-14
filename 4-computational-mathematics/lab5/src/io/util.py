from lab5.src.io.reader import ConsoleReader, FileReader


def round_(n, precision):
    return "{:.{}f}".format(n, precision)


def print_finite_difference_table(table):
    n = len(table)
    for i in range(n):
        print(*[round_(table[i][j], 4) if i + j < n else '' for j in range(n)], sep='\t')


def print_result(result):
    separator = '=' * 50
    line = f"\n\n{separator}\n\n".join(result)
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


def read_filename(mode):
    filename = None
    while filename is None:
        filename = input('Введите имя файла: ').strip()
        try:
            open(filename, mode).close()
        except:
            filename = None
            print('Не удалось найти файл!')
    return filename


def read_points(reader):
    if isinstance(reader, ConsoleReader):
        print('Вводите точки, по одной в строке. По окончании ввода введите q')
    x = []
    y = []
    while True:
        try:
            s = reader.read()

            if s == 'q' or s == '' and isinstance(reader, FileReader):
                break

            xi, yi = list(map(float, s.split()))
            x.append(xi)
            y.append(yi)
        except:
            message = 'Некорректный ввод'
            if isinstance(reader, FileReader):
                raise Exception(message)
            else:
                print(message)

    return x, y


def read_positive_integer(message):
    value = None
    while value is None:
        try:
            value = int(input(f'{message}: '))
            if value <= 0:
                print('Значение должно быть > 0')
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


def read_point(message, function=None):
    if function is None:
        return read_float(message)

    value = None
    while value is None:
        try:
            value = read_float(message)
            function(value)
        except:
            print('Значение функции не определено в данной точке. Попробуйте снова')
            value = None
    return value
