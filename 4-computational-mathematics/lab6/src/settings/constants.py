from math import exp, sin, cos

from lab6.core.methods import euler_method, improved_euler_method, milne_method

ONE_STEP_METHODS = [
    euler_method,
    improved_euler_method
]

ONE_STEP_METHODS_NAMES = [
    'Метод Эйлера',
    'Модифицированный метод Эйлера'
]

RUNGE_P = [1, 2]

MULTY_STEP_METHODS = [
    milne_method
]

MULTY_STEP_METHODS_NAMES = [
    'Метод Милна'
]

EQUATIONS = [
    lambda x, y: y + (1 + x) * y ** 2,
    lambda x, y: x + y,
    lambda x, y: cos(x) - y,
    lambda x, y: y * cos(x)
]

EQUATIONS_NAMES = [
    'y + (1 + x) * y^2',
    'x + y',
    'cos(x) - y',
    'y * cos(x)'
]

EQUATIONS_SOLUTIONS = [
    lambda x, x0, y0: -exp(x) / (x * exp(x) - (x0 * exp(x0) * y0 + exp(x0)) / y0),
    lambda x, x0, y0: ((y0 + x0 + 1) / exp(x0)) * exp(x) - x - 1,
    lambda x, x0, y0: sin(x) / 2 + cos(x) / 2 + (exp(x0) * (y0 - cos(x0) / 2 - sin(x0) / 2)) / exp(x),
    lambda x, x0, y0: y0 * exp(sin(x) - sin(x0))
]
