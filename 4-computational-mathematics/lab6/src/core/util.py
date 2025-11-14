from lab6.dto.result import Result
from lab6.settings.config import MAX_N


def solve_one_step(equation, method, p, x0, xn, n, y0, eps):
    error = 1e9
    x = [x0 + _ * (xn - x0) / (n - 1) for _ in range(n)]
    try:
        y = method(equation, x, y0)
    except OverflowError:
        raise Exception('Не удалось вычислить, слишком большие значения')
    except ZeroDivisionError:
        raise Exception('В ходе поиска решения произошло деление на ноль')

    while error > eps:
        if n > MAX_N:
            raise Exception(f'Произведено разбиение на {n} отрезков, но необходимая точность не достигнута')

        n *= 2

        x = [x0 + _ * (xn - x0) / (n - 1) for _ in range(n)]
        try:
            next_y = method(equation, x, y0)
        except OverflowError:
            raise Exception('Не удалось вычислить, слишком большие значения')

        error = abs(next_y[-1] - y[-1]) / (2 ** p - 1)

        y = next_y

    return Result(x, y, error)


def solve_multy_step(equation, method, solution, x0, xn, n, y0, eps):
    error = 1e9
    x = [x0 + _ * (xn - x0) / (n - 1) for _ in range(n)]
    try:
        y = method(equation, x, y0, eps)
    except OverflowError:
        raise Exception('Не удалось вычислить, слишком большие значения')
    except ZeroDivisionError:
        raise Exception('В ходе поиска решения произошло деление на ноль')

    while error > eps:
        if n > MAX_N:
            raise Exception(f'Произведено разбиение на {n} отрезков, но необходимая точность не достигнута')

        n *= 2

        x = [x0 + _ * (xn - x0) / (n - 1) for _ in range(n)]
        try:
            y = method(equation, x, y0, eps)
        except OverflowError:
            raise Exception('Не удалось вычислить, слишком большие значения')

        error = max([abs(solution(x_, x0, y0) - y_) for x_, y_ in zip(x, y)])

    return Result(x, y, error)
