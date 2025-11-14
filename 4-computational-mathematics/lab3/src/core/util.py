import math
from typing import List

from lab3.core.function import Function
from lab3.dto.result import Result
from lab3.settings.config import INIT_N, MAX_N, BREAKING_POINTS_ACCURACY, CONVERGENCE_EPS


def calculate_integral(function: Function, a: float, b: float, eps: float, method, runge_k: int) -> Result:
    n = INIT_N

    result = method(function, a, b, n)
    delta = math.inf

    while delta > eps:
        if n >= MAX_N:
            raise Exception(f'Произведено разбиение на {MAX_N} отрезков, но ответ не найден')

        n *= 2

        new_result = method(function, a, b, n)
        delta = abs(new_result - result) / (2 ** runge_k - 1)
        result = new_result

    return Result(result, n)


def get_breaking_points(function: Function, a: float, b: float):
    n = math.ceil((b - a) / BREAKING_POINTS_ACCURACY)
    h = (b - a) / n

    breaking_points = []
    last_i = -2
    for i in range(n + 1):
        x = a + i * h
        if function.compute_or_none(x) is None:
            if i - 1 == last_i and i != n:
                raise Exception(
                    "Фунция может быть неопределена только в некоторых точках.\nНа выбранном отрезке существуют области неопредедённости.\nИнтегрирование невозможно")
            last_i = i
            breaking_points.append(x)

    return breaking_points


def is_inf(x):
    return abs(x) >= 1 / CONVERGENCE_EPS - 1 / BREAKING_POINTS_ACCURACY


def is_converges(function: Function, a: float, b: float, breaking_points: List[float]) -> bool:
    eps = CONVERGENCE_EPS

    breaking_points_tmp = breaking_points.copy()

    if a in breaking_points_tmp:
        breaking_points_tmp.remove(a)
        y = function.compute_or_none(a + eps)
        if y is None or is_inf(y):
            return False

    if b in breaking_points_tmp:
        breaking_points_tmp.remove(b)
        y = function.compute_or_none(b - eps)
        if y is None or is_inf(y):
            return False

    for p in breaking_points_tmp:
        y1 = function.compute_or_none(p - eps)
        y2 = function.compute_or_none(p + eps)
        if (y1 is None and y2 is None) or (is_inf(y1) and is_inf(y2) and y1 * y2 > 0):
            return False

    return True


def calculate_improper_integral(function: Function, a: float, b: float, eps: float, method: Function, runge_k: int,
                                breaking_points: List[float]) -> Result:
    conv_eps = CONVERGENCE_EPS

    result = 0
    iterations = 0

    if a not in breaking_points:
        b_ = breaking_points[0] - conv_eps
        y = function.compute_or_none(b_)
        if y is not None and not is_inf(y):
            result_ = calculate_integral(function, a, b_, eps, method, runge_k)
            result += result_.value
            iterations += result_.iterations

    if b not in breaking_points:
        a_ = breaking_points[-1] + conv_eps
        y = function.compute_or_none(a_)
        if y is not None and not is_inf(y):
            result_ = calculate_integral(function, a_, b, eps, method, runge_k)
            result += result_.value
            iterations += result_.iterations

    for i in range(1, len(breaking_points)):
        a_ = breaking_points[i] - conv_eps
        b_ = breaking_points[i - 1] + conv_eps
        y_a_ = function.compute_or_none(a_)
        y_b_ = function.compute_or_none(b_)

        if y_a_ is not None and y_b_ is not None and not (is_inf(y_a_) and is_inf(y_b_) and y_a_ * y_b_ > 0):
            result_ = calculate_integral(function, a_, b_, eps, method, runge_k)
            result += result_.value
            iterations += result_.iterations

    return Result(result, iterations)
