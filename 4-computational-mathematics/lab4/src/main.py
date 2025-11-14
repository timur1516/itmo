from lab4.src.io.reader import ConsoleReader
from lab4.src.core.approximation_functions import linear_approximation
from lab4.src.core.util import mean_squared_error, measure_of_deviation, coefficient_of_determination, \
    pearson_correlation_coefficient
from lab4.src.io.util import create_reader, approximation_functions_coefficients_to_str, read_points, print_result, \
    create_writer, round_
from lab4.src.settings.constants import APPROXIMATION_FUNCTIONS, APPROXIMATION_FUNCTIONS_NAMES
from lab4.src.util.drawer import draw_plot


def main():
    reader = create_reader()
    if isinstance(reader, ConsoleReader):
        print('Вводите точки, по одной в строке. По окончании ввода введите q')
    x, y = read_points(reader)
    n = len(x)

    phis = []
    phis_names = []

    min_mse = 1e10
    best_approximation_function_index = None

    result = []

    for i in range(len(APPROXIMATION_FUNCTIONS)):
        f = APPROXIMATION_FUNCTIONS[i]
        name = APPROXIMATION_FUNCTIONS_NAMES[i]

        log = [f'Аппроксимирующая функция: {name}']

        try:
            phi, c = f(x, y, n)
        except Exception as e:
            log.append(f'ОШИБКА: {e}')
            result.append("\n".join(log))
            continue

        phis.append(phi)
        phis_names.append(name)

        phi_str = approximation_functions_coefficients_to_str[i](c)
        mse = mean_squared_error(x, y, phi, n)
        r2 = coefficient_of_determination(x, y, phi, n)
        s = measure_of_deviation(x, y, phi)

        if mse < min_mse:
            min_mse = mse
            best_approximation_function_index = i

        log.append(f'Функция: φ(x) = {phi_str}')
        log.append(f'Среднеквадратичное отклонение: σ = {round_(mse, 3)}')
        log.append(f'Коэффициент детерминации: R² = {round_(r2, 3)}')
        log.append(f'Мера отклонения: S = {round_(s, 3)}')

        if f is linear_approximation:
            r = pearson_correlation_coefficient(x, y, n)
            log.append(f'Коэффициент кореляции Пирсона: r = {round_(r, 3)}')

        result.append("\n".join(log))

    writer = create_writer()

    print_result(result, writer)

    best_approximation_function_name = None
    if best_approximation_function_index is not None:
        best_approximation_function_name = APPROXIMATION_FUNCTIONS_NAMES[best_approximation_function_index]

    print(f'Лучшая аппроксимирующая функция: {best_approximation_function_name}')

    if n != 0: draw_plot(x, y, phis, phis_names)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
