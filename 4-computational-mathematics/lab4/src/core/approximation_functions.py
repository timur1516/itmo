import numpy as np


def linear_approximation(x, y, n):
    if n < 2:
        raise Exception('Должно быть минимум 2 точки')

    sx = sum(x)
    sxx = sum(xi ** 2 for xi in x)
    sy = sum(y)
    sxy = sum(xi * yi for xi, yi in zip(x, y))

    try:
        a, b = np.linalg.solve(
            [
                [sxx, sx],
                [sx, n]
            ],
            [sxy, sy]
        )
    except np.linalg.LinAlgError:
        raise Exception('Не удалось подобрать коэффициенты')

    phi = lambda x_: a * x_ + b

    return phi, (a, b)


def square_approximation(x, y, n):
    if n < 3:
        raise Exception('Должно быть минимум 3 точки')

    sx = sum(x)
    sxx = sum(xi ** 2 for xi in x)
    sxxx = sum(xi ** 3 for xi in x)
    sxxxx = sum(xi ** 4 for xi in x)
    sy = sum(y)
    sxy = sum(xi * yi for xi, yi in zip(x, y))
    sxxy = sum(xi * xi * yi for xi, yi in zip(x, y))

    try:
        a0, a1, a2 = np.linalg.solve(
            [
                [n, sx, sxx],
                [sx, sxx, sxxx],
                [sxx, sxxx, sxxxx]
            ],
            [sy, sxy, sxxy]
        )
    except np.linalg.LinAlgError:
        raise Exception('Не удалось подобрать коэффициенты')

    phi = lambda x_: a2 * x_ ** 2 + a1 * x_ + a0

    return phi, (a0, a1, a2)


def cubic_approximation(xs, ys, n):
    if n < 4:
        raise Exception('Должно быть минимум 4 точки')

    sx = sum(xs)
    sxx = sum(xi ** 2 for xi in xs)
    sxxx = sum(xi ** 3 for xi in xs)
    sxxxx = sum(xi ** 4 for xi in xs)
    sxxxxx = sum(xi ** 5 for xi in xs)
    sxxxxxx = sum(xi ** 6 for xi in xs)
    sy = sum(ys)
    sxy = sum(xi * yi for xi, yi in zip(xs, ys))
    sxxy = sum(xi * xi * yi for xi, yi in zip(xs, ys))
    sxxxy = sum(xi * xi * xi * yi for xi, yi in zip(xs, ys))

    try:
        a0, a1, a2, a3 = np.linalg.solve(
            [
                [n, sx, sxx, sxxx],
                [sx, sxx, sxxx, sxxxx],
                [sxx, sxxx, sxxxx, sxxxxx],
                [sxxx, sxxxx, sxxxxx, sxxxxxx]
            ],
            [sy, sxy, sxxy, sxxxy]
        )
    except np.linalg.LinAlgError:
        raise Exception('Не удалось подобрать коэффициенты')

    phi = lambda x_: a3 * x_ ** 3 + a2 * x_ ** 2 + a1 * x_ + a0

    return phi, (a0, a1, a2, a3)


def exponential_approximation(x, y, n):
    if n < 2:
        raise Exception('Должно быть минимум 2 точки')
    if min(y) <= 0:
        raise ValueError('Аппроксимация возможна только для наборов точек у которых y > 0')

    _, (a_, b_) = linear_approximation(x, np.log(y), n)

    a = a_
    b = np.exp(b_)

    phi = lambda x_: b * np.exp(a * x_)

    return phi, (a, b)


def logarithmic_approximation(x, y, n):
    if n < 2:
        raise Exception('Должно быть минимум 2 точки')
    if min(x) <= 0:
        raise ValueError('Аппроксимация возможна только для наборов точек у которых x > 0')

    _, (a_, b_) = linear_approximation(np.log(x), y, n)

    a = a_
    b = b_

    phi = lambda x_: a * np.log(np.clip(x_, 1e-10, None)) + b

    return phi, (a, b)


def power_approximation(x, y, n):
    if n < 2:
        raise Exception('Должно быть минимум 2 точки')
    if min(x) <= 0 or min(y) <= 0:
        raise ValueError('Аппроксимация возможна только для наборов точек у которых x > 0 и y > 0')

    _, (b_, a_) = linear_approximation(np.log(x), np.log(y), n)

    a = np.exp(a_)
    b = b_

    def phi(x_):
        if b < 0:
            x_ = np.where(x_ != 0, x_, 1e-10)
        if abs(b) < 1:
            x_ = np.clip(x_, 1e-10, None)

        return a * np.power(x_, b)

    return phi, (a, b)
