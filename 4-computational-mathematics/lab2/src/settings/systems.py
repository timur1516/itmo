import numpy as np

from lab2.src.equation.multi_equation import MultiEquation
from lab2.src.equation.system_of_equations import SystemOfEquations

SYSTEMS = [
    SystemOfEquations([
        MultiEquation(lambda x_: x_[0] ** 2 + x_[1] ** 2 - 4, 'x^2 + y^2 = 4'),
        MultiEquation(lambda x_: -3 * x_[0] ** 2 + x_[1], 'y = 3x^2')
    ]),
    SystemOfEquations([
        MultiEquation(lambda x_: x_[0] ** 2 + x_[1] ** 2 - 4, 'x^2 + y^2 = 4'),
        MultiEquation(lambda x_: x_[1] - np.sin(x_[0]), 'y = sin(x)')
    ]),
    SystemOfEquations([
        MultiEquation(lambda x_: x_[0] ** 2 + x_[1] ** 2 - 6, 'x^2 + y^2 = 6'),
        MultiEquation(lambda x_: x_[1] - np.tan(x_[0]), 'y = tg(x)')
    ])
]
