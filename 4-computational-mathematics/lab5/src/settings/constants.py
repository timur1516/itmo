from math import sin, sqrt

from lab5.src.core.interpolation_functions import newton_divided_difference_polynomial, lagrange_polynomial, \
    gauss_polynomial, stirling_polynomial, bessel_polynomial

INTERPOLATION_FUNCTIONS = [
    lagrange_polynomial,
    newton_divided_difference_polynomial,
    gauss_polynomial,
    stirling_polynomial,
    bessel_polynomial
]
INTERPOLATION_FUNCTIONS_NAMES = [
    'Интерполяционный многочлен Лагранжа',
    'Интерполяционный многочлен Ньютона с разделенными разностями',
    'Интерполяционный многочлен Гаусса',
    'Интерполяционный многочлен Стирлинга',
    'Интерполяционный многочлен Бесселя'
]

DATA_SOURCES = ['Консоль', 'Файл', 'Функция']

FUNCTIONS = [
    lambda x: x ** 2,
    lambda x: x ** 3,
    lambda x: x ** 5,
    lambda x: sin(x),
    lambda x: sqrt(x)
]

FUNCTIONS_NAMES = [
    'x^2',
    'x^3',
    'x^5',
    'sin(x)',
    'sqrt(x)'
]
