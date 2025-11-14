from lab3.core.function import Function


def rectangles_method_right(function: Function, a: float, b: float, n: int):
    h = (b - a) / n

    result = 0
    for i in range(1, n + 1):
        result += function.compute(a + i * h)
    result *= h

    return result


def rectangles_method_left(function: Function, a: float, b: float, n: int):
    h = (b - a) / n

    result = 0
    for i in range(n):
        result += function.compute(a + i * h)
    result *= h

    return result


def rectangles_method_middle(function: Function, a: float, b: float, n: int):
    h = (b - a) / n

    result = 0
    for i in range(1, n + 1):
        x_prev = a + (i - 1) * h
        x_i = a + i * h
        x_h = (x_prev + x_i) / 2
        result += function.compute(x_h)
    result *= h

    return result


def trapezoid_method(function: Function, a: float, b: float, n: int):
    h = (b - a) / n

    result = (function.compute(a) + function.compute(b)) / 2
    for i in range(1, n):
        result += function.compute(a + i * h)
    result *= h

    return result


def simpson_method(function: Function, a: float, b: float, n: int):
    h = (b - a) / n

    result = function.compute(a) + function.compute(b)
    for i in range(1, n):
        k = 2 if i % 2 == 0 else 4
        result += k * function.compute(a + i * h)
    result *= h / 3

    return result
