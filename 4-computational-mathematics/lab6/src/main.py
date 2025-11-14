from lab6.core.util import solve_one_step, solve_multy_step
from lab6.io.util import choose_options, read_float, read_positive_integer, generate_result_log, print_result
from lab6.settings.constants import EQUATIONS, EQUATIONS_NAMES, ONE_STEP_METHODS, RUNGE_P, MULTY_STEP_METHODS, \
    EQUATIONS_SOLUTIONS, ONE_STEP_METHODS_NAMES, MULTY_STEP_METHODS_NAMES
from lab6.util.drawer import draw_plot
from lab6.util.validators import is_save_interval


def main():
    equation_id = choose_options('Выберите уравнение', EQUATIONS_NAMES) - 1
    equation = EQUATIONS[equation_id]
    solution = EQUATIONS_SOLUTIONS[equation_id]

    x0 = read_float('Введите первый элемент интервала')
    xn = read_float('Введите последний элемент интервала')

    if x0 > xn:
        x0, xn = xn, x0
        print('Значения x0 и xn были поменяны местами')

    n = read_positive_integer('Введите количество элементов в интервале')
    y0 = read_float('Введите y0')

    if not is_save_interval(x0, xn, lambda x_: solution(x_, x0, y0)):
        raise Exception('Решение определено не на всём интервале')

    eps = read_float('Введите точность')
    result_log = []

    for i in range(len(ONE_STEP_METHODS)):
        method = ONE_STEP_METHODS[i]
        method_name = ONE_STEP_METHODS_NAMES[i]
        p = RUNGE_P[i]

        try:
            result = solve_one_step(equation, method, p, x0, xn, n, y0, eps)
        except Exception as e:
            result_log.append(f'{method_name}\nОшибка: {e}')
            continue

        y_real = [solution(x_, x0, y0) for x_ in result.x]
        result_log.append(generate_result_log(method_name, result, y_real))

        solution_f = lambda x_: solution(x_, x0, y0)
        draw_plot(result.x, result.y, solution_f, method_name)

    for i in range(len(MULTY_STEP_METHODS)):
        method = MULTY_STEP_METHODS[i]
        method_name = MULTY_STEP_METHODS_NAMES[i]

        try:
            result = solve_multy_step(equation, method, solution, x0, xn, n, y0, eps)
        except Exception as e:
            result_log.append(f'{method_name}\nОшибка: {e}')
            continue

        y_real = [solution(x_, x0, y0) for x_ in result.x]
        result_log.append(generate_result_log(method_name, result, y_real))

        solution_f = lambda x_: solution(x_, x0, y0)
        draw_plot(result.x, result.y, solution_f, method_name)

    print_result(result_log)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
