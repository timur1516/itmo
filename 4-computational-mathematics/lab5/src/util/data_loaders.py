from lab3.io.util import choose_options
from lab5.src.io.reader import ConsoleReader, FileReader
from lab5.src.io.util import read_points, read_filename, read_point, read_positive_integer
from lab5.src.settings.constants import FUNCTIONS_NAMES, FUNCTIONS


def validate_data(x, y):
    if len(set(x)) != len(x):
        raise Exception('Узлы интерполяции не должны совпадать!')
    elif x != sorted(x):
        raise Exception('Узлы интерполяции должны быть отсортированы по значению X!')


def load_from_console():
    reader = ConsoleReader()
    x, y = read_points(reader)
    validate_data(x, y)
    x0 = read_point('Введите точку интерполяции')
    return x0, x, y


def load_from_file():
    filename = read_filename('r')
    reader = FileReader(filename)
    x, y = read_points(reader)
    validate_data(x, y)
    x0 = read_point('Введите точку интерполяции')
    return x0, x, y


def load_from_function():
    function_id = choose_options('Выберите функцию', FUNCTIONS_NAMES) - 1
    function = FUNCTIONS[function_id]

    l = read_point('Введите левую границу исследуемого интервала', function)
    r = read_point('Введите правую границу исследуемого интервала', function)

    if l == r:
        raise Exception('Задан интервал нулевой длинны!')

    if l > r:
        l, r = r, l
        print('Левая граница больше правой. Границы были поменяны местами')

    n = read_positive_integer('Введите число узлов')

    h = (r - l) / (n - 1)
    x = [l + h * i for i in range(n)]
    y = list(map(function, x))

    x0 = read_point('Введите точку интерполяции', function)

    return x0, x, y
