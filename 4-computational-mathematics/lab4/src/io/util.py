from lab4.src.io.reader import ConsoleReader, FileReader
from lab4.src.io.writer import ConsoleWriter, FileWriter
from lab4.src.settings.constants import IO_METHODS

approximation_functions_coefficients_to_str = [
    lambda c: f'{round_(c[0], 3)}x + {round_(c[1], 3)}',
    lambda c: f'{round_(c[2], 3)}x^2 + {round_(c[1], 3)}x + {round_(c[0], 3)}',
    lambda c: f'{round_(c[3], 3)}x^3 + {round_(c[2], 3)}x^2 + {round_(c[1], 3)}x + {round_(c[0], 3)}',
    lambda c: f'{round_(c[1], 3)} * e^{round_(c[0], 3)}x',
    lambda c: f'{round_(c[0], 3)} * ln(x) + {round_(c[1], 3)}',
    lambda c: f'{round_(c[0], 3)} * x^{round_(c[1], 3)}'
]


def round_(n, precision):
    return "{:.{}f}".format(n, precision)


def print_result(result, writer):
    separator = '=' * 50
    line = f"\n\n{separator}\n\n".join(result)
    writer.write(f'\n{separator}\n\n{line}\n\n{separator}\n')


def create_reader():
    intput_mode = choose_options('Выберите способ ввода', IO_METHODS)
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
