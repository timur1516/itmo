from lab5.src.core.util import calculate_finite_difference_table
from lab5.src.io.util import choose_options, print_finite_difference_table, print_result
from lab5.src.settings.constants import DATA_SOURCES, INTERPOLATION_FUNCTIONS, INTERPOLATION_FUNCTIONS_NAMES
from lab5.src.util.data_loaders import load_from_console, load_from_file, load_from_function
from lab5.src.util.drawer import draw_plot


def main():
    mode = choose_options('Выберите способ задания функции', DATA_SOURCES)

    if mode == 1:
        x0, x, y = load_from_console()
    elif mode == 2:
        x0, x, y = load_from_file()
    else:
        x0, x, y = load_from_function()

    finite_difference_table = calculate_finite_difference_table(y)

    print('Таблица конечных разностей:')
    print_finite_difference_table(finite_difference_table)

    interpolation_polynomes = []
    interpolation_polynomes_names = []

    result = []

    for i in range(len(INTERPOLATION_FUNCTIONS)):
        f = INTERPOLATION_FUNCTIONS[i]
        name = INTERPOLATION_FUNCTIONS_NAMES[i]

        try:
            p = f(x, y)
        except Exception as e:
            result.append(f'Интерполирующая функция: {name}\nОШИБКА: {e}')
            continue

        result.append(f'Интерполирующая функция: {name}\nP({x0}) = {p(x0)}')

        interpolation_polynomes.append(p)
        interpolation_polynomes_names.append(name)

    print_result(result)

    draw_plot(x, y, x0, interpolation_polynomes, interpolation_polynomes_names)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
