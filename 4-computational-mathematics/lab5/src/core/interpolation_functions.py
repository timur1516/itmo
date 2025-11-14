from lab5.src.core.util import calculate_divided_differences, calculate_finite_difference_table, is_finite_difference


def lagrange_polynomial(x, y):
    n = len(x)

    def p(x_):
        result = 0
        for k in range(n):
            nominator = 1
            denominator = 1
            for i in range(n):
                if i == k:
                    continue
                nominator *= x_ - x[i]
                denominator *= x[k] - x[i]
            result += y[k] * (nominator / denominator)
        return result

    return p


def newton_divided_difference_polynomial(x, y):
    n = len(x)
    diffs = calculate_divided_differences(x, y)

    def p(x_):
        result = y[0]
        for k in range(1, n):
            d = diffs[k]
            for i in range(0, k):
                d *= (x_ - x[i])
            result += d
        return result

    return p


def _first_gauss_polynomial(x, y):
    if len(x) <= 1:
        raise Exception('Должно быть минимум две точки')

    n = len(x)
    h = x[1] - x[0]
    alpha_ind = n // 2
    diffs = calculate_finite_difference_table(y)

    def p(x_):
        t = (x_ - x[alpha_ind]) / h
        result = 0

        for k in range(n):
            m = (k + 1) // 2

            nominator = 1
            for j in range(-(m - 1), m):
                nominator *= t + j
            if k == 2 * m and m != 0: nominator *= t - m

            factorial = 1
            for j in range(1, k + 1):
                factorial *= j

            if k == 2 * m:
                result += diffs[alpha_ind - m][k] * (nominator / factorial)
            else:
                result += diffs[alpha_ind - (m - 1)][k] * (nominator / factorial)
        return result

    return p


def _second_gauss_polynomial(x, y):
    if len(x) <= 1:
        raise Exception('Должно быть минимум две точки')

    n = len(x)
    h = x[1] - x[0]
    alpha_ind = n // 2
    diffs = calculate_finite_difference_table(y)

    def p(x_):
        t = (x_ - x[alpha_ind]) / h
        result = 0

        for k in range(n):
            m = (k + 1) // 2

            nominator = 1
            for j in range(-(m - 1), m):
                nominator *= t + j
            if k == 2 * m and m != 0: nominator *= t + m

            factorial = 1
            for j in range(1, k + 1):
                factorial *= j

            result += diffs[alpha_ind - m][k] * (nominator / factorial)
        return result

    return p


def gauss_polynomial(x, y):
    if len(x) <= 1:
        raise Exception('Должно быть минимум две точки')
    if not is_finite_difference(x):
        raise Exception('Значения X должны иметь фиксированный шаг!')

    n = len(x)
    alpha_ind = n // 2

    p1 = _first_gauss_polynomial(x, y)
    p2 = _second_gauss_polynomial(x, y)

    p = lambda x_: p1(x_) if x_ > x[alpha_ind] else p2(x_)

    return p


def stirling_polynomial(x, y):
    if len(x) <= 1:
        raise Exception('Должно быть минимум две точки')
    if len(x) % 2 != 1:
        raise Exception('Число узлов должно быть нечетным')
    if not is_finite_difference(x):
        raise Exception('Значения X должны иметь фиксированный шаг!')

    p1 = _first_gauss_polynomial(x, y)
    p2 = _second_gauss_polynomial(x, y)

    p = lambda x_: (p1(x_) + p2(x_)) / 2

    return p


def bessel_polynomial(x, y):
    if len(x) <= 1:
        raise Exception('Должно быть минимум две точки')
    if len(x) % 2 != 0:
        raise Exception('Число узлов должно быть чётным')
    if not is_finite_difference(x):
        raise Exception('Значения X должны иметь фиксированный шаг')

    n = len(x)
    h = x[1] - x[0]
    alpha_ind = n // 2 - 1
    diffs = calculate_finite_difference_table(y)

    def p(x_):
        t = (x_ - (x[alpha_ind] + x[alpha_ind + 1]) / 2) / h
        result = (y[alpha_ind] + y[alpha_ind + 1]) / 2
        result += (t - 0.5) * diffs[alpha_ind][1]
        if alpha_ind > 0:
            result += (t * (t - 1) / (1 * 2)) * ((diffs[alpha_ind - 1][2] + diffs[alpha_ind][2]) / 2)
            result += ((t - 0.5) * t * (t - 1) / (1 * 2 * 3)) * diffs[alpha_ind - 1][3]
        if alpha_ind > 1:
            result += ((t * (t - 1) * (t + 1) * (t - 2) / (1 * 2 * 3 * 4)) *
                       ((diffs[alpha_ind - 2][4] + diffs[alpha_ind - 1][4]) / 2))
        return result

    return p
