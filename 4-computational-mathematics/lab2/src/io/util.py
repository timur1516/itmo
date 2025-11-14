from tabulate import tabulate

from lab2.src.io.reader import FileReader, ConsoleReader
from lab2.src.io.writer import ConsoleWriter, FileWriter
from lab2.src.settings.constants import IO_METHODS


def round_(n, precision):
    return "{:.{}f}".format(n, precision)


def create_reader():
    intput_mode = choose_options('Выберите способ ввода границ интервала и точности', IO_METHODS)
    reader = ConsoleReader()
    if intput_mode == 2:
        filename = read_filename('r')
        reader = FileReader(filename)
    return reader


def create_writer():
    output_mode = choose_options('Выберите способ вывода ответа', IO_METHODS)
    writer = ConsoleWriter()
    if output_mode == 2:
        filename = read_filename('w')
        writer = FileWriter(filename)
    return writer


def print_log(log, writer, log_decimals):
    header = list(log[0].keys())
    data = [
        [f'{v:.{log_decimals}f}' if isinstance(v, (int, float)) else
         [f'{num:.{log_decimals}f}' for num in v] if isinstance(v, list) else str(v)
         for v in item.values()]
        for item in log
    ]
    writer.write(tabulate(data, header, tablefmt='pretty', showindex=True))


def print_result(result, real_root, writer, log_decimals):
    writer.write(f'Найденный корень: {result.x}')
    writer.write(f'Истинный корень: {real_root}')
    writer.write(f'Потребовалось итераций: {result.iterations}')
    writer.write('Лог решения:')
    print_log(result.log, writer, log_decimals)


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


def read_root_limits(reader):
    left = None
    right = None
    while left is None or right is None:
        message = ''
        try:
            left, right = map(float, reader.read('Введите нижнюю и верхнюю границу диапазона корней: ').split())
            if left > right:
                message = 'Левая граница должна быть меньше левой!'
                left = None
                right = None
            else:
                break
        except:
            message = 'Значения должны быть числами!'
        if isinstance(reader, FileReader):
            raise Exception(message)
        else:
            print(message)
    return left, right


def read_eps(reader):
    eps = None
    while eps is None:
        try:
            eps = float(reader.read('Введите точность: '))
            break
        except:
            message = 'Значение должно быть числом'
        if isinstance(reader, FileReader):
            raise Exception(message)
        else:
            print(message)
    return eps


def read_initial_point(reader, n):
    point = None
    while point is None:
        message = ''
        try:
            point = list(map(float, reader.read(f'Введите {n} координат начального приближения: ').split()))
            if len(point) != n:
                print(f'Введите {n} чисел!')
                point = None
            else:
                break
        except:
            message = 'Значения должны быть числами!'
        if isinstance(reader, FileReader):
            raise Exception(message)
        else:
            print(message)
    return point
