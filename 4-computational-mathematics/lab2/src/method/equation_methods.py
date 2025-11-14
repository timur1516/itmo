import numpy as np
from scipy.differentiate import derivative

from lab2.src.dto.result import Result
from lab2.src.settings.config import MAX_ITERATIONS


def chord_method(equation, a, b, eps):
    f = equation.f
    iterations = 0
    log = []

    x = (a * f(b) - b * f(a)) / (f(b) - f(a))

    while True:
        if iterations == MAX_ITERATIONS:
            raise Exception(f'Произведено {MAX_ITERATIONS} итераций, но решение не найдено.')
        iterations += 1

        if f(a) * f(x) <= 0:
            b = x
        else:
            a = x

        next_x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        delta = abs(next_x - x)

        log.append({
            'a': a,
            'b': b,
            'x': x,
            'f(a)': f(a),
            'f(b)': f(b),
            'f(x)': f(x),
            'delta': delta})

        if delta < eps:
            break

        x = next_x

    return Result(x, iterations, log)


def secant_method(equation, a, b, eps):
    f = equation.f
    f__ = equation.snd_derivative
    iterations = 0
    log = []

    if f__(a) * f__(b) < 0:
        raise Exception(
            'Условия сходимости метода секущих не выполнены! Вторая производная не сохраняет знак на выбранном отрезке')

    x0 = a
    if f(a) * f__(a) > 0:
        x0 = a
    if f(b) * f__(b) > 0:
        x0 = b

    x1 = x0 + eps

    while True:
        if iterations == MAX_ITERATIONS:
            raise Exception(f'Произведено {MAX_ITERATIONS} итераций, но решение не найдено.')
        iterations += 1

        x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        delta = abs(x - x1)

        log.append({
            'x_{i-1}': x0,
            'x_i': x1,
            'x_{i+1}': x,
            'f(x_{i+1})': f(x),
            'delta': delta
        })

        if delta < eps:
            break

        x0 = x1
        x1 = x

    return Result(x, iterations, log)


def simple_iteration_method(equation, a, b, eps):
    f = equation.f
    f_ = equation.fst_derivative
    iterations = 0
    log = []

    max_derivative = max(abs(f_(a)), abs(f_(b)))
    _lambda = 1 / max_derivative
    if f_(a) > 0: _lambda *= -1

    phi = lambda x: x + _lambda * f(x)

    phi_ = lambda x: derivative(phi, x).df
    q = np.max(abs(phi_(np.linspace(a, b, int(1 / eps)))))
    if q > 1:
        raise Exception(f'Метод не сходится так как значение q >= 1')

    prev_x = a
    while True:
        if iterations == MAX_ITERATIONS:
            raise Exception(f'Произведено {MAX_ITERATIONS} итераций, но решение не найдено.')
        iterations += 1

        x = phi(prev_x)
        delta = abs(x - prev_x)

        log.append({
            'x_i': prev_x,
            'x_{i+1}': x,
            'phi(x_{i+1})': phi(x),
            'f(x_{i+1})': f(x),
            'delta': delta
        })

        if delta <= eps:
            break

        prev_x = x

    return Result(x, iterations, log)
