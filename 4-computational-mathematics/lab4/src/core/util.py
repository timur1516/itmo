import math


def pearson_correlation_coefficient(x, y, n):
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    r = (sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) /
         math.sqrt(sum((xi - mean_x) ** 2 for xi in x) * sum((yi - mean_y) ** 2 for yi in y)))

    return r


def mean_squared_error(x, y, phi, n):
    return math.sqrt(sum(((phi(xi) - yi) ** 2 for xi, yi in zip(x, y))) / n)


def measure_of_deviation(x, y, phi):
    return sum(((phi(xi) - yi) ** 2 for xi, yi in zip(x, y)))


def coefficient_of_determination(x, y, phi, n):
    mean_phi = sum(phi(xi) for xi in x) / n
    return 1 - sum((yi - phi(xi)) ** 2 for xi, yi in zip(x, y)) / sum((yi - mean_phi) ** 2 for yi in y)
