import math

from lab3.core.function import Function

FUNCTIONS = [
    Function(lambda x: x ** 2, 'x^2'),
    Function(lambda x: math.sin(x), 'sin(x)'),
    Function(lambda x: x ** 3 - 3 * x ** 2 + 7 * x - 10, 'x^3 - 3x^2 + 7x - 10'),
    Function(lambda x: 5, '5'),
    Function(lambda x: 1 / math.sqrt(x), '1 / sqrt(x)'),
    Function(lambda x: 1 / (1 - x), '1 / (1 - x)'),
    Function(lambda x: 1 / x, '1 / x'),
    Function(lambda x: 1 / x ** 2, '1 / x^2')
]
