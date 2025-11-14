import numpy as np

from lab2.src.equation.simple_equation import SimpleEquation

EQUATIONS = [
    SimpleEquation(lambda x: x ** 3 - x + 4, 'x^3 - x + 4'),
    SimpleEquation(lambda x: x ** 3 - x ** 2 - 25 * x + 2, 'x^3 - x^2 - 25x + 2'),
    SimpleEquation(lambda x: np.atan(x), 'arctg(x)')
]
