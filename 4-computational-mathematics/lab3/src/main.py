from lab3.core.util import calculate_integral, get_breaking_points, is_converges, calculate_improper_integral
from lab3.io.util import choose_options, read_float, print_result
from lab3.settings.constants import METHODS, METHODS_STRS, METHODS_RUNGE_K
from lab3.settings.functions import FUNCTIONS


def main():
    function_id = choose_options('Выберите функцию для интегрирования', FUNCTIONS) - 1
    function = FUNCTIONS[function_id]

    a = read_float('Введите нижний предел интегрирования')
    b = read_float('Введите верхний предел интегрирования')

    is_inv = False
    if b < a:
        a, b = b, a
        is_inv = True

    is_improper_integral = False

    breaking_points = get_breaking_points(function, a, b)
    if len(breaking_points) != 0:
        print(f'Функция терпит разрыв в точках: {breaking_points}')
        is_improper_integral = True

    if is_improper_integral and not is_converges(function, a, b, breaking_points):
        raise Exception('Интеграл расходится')

    method_id = choose_options('Выберите метод для интегрирования', METHODS_STRS) - 1
    method = METHODS[method_id]
    runge_k = METHODS_RUNGE_K[method_id]

    eps = read_float('Введите точность')

    if not is_improper_integral:
        result = calculate_integral(function, a, b, eps, method, runge_k)
    else:
        result = calculate_improper_integral(function, a, b, eps, method, runge_k, breaking_points)

    if is_inv:
        result.value *= -1

    print_result(result)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
