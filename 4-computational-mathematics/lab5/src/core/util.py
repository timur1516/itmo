def calculate_finite_difference_table(y):
    n = len(y)
    delta_y = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        delta_y[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            delta_y[i][j] = delta_y[i + 1][j - 1] - delta_y[i][j - 1]
    return delta_y


def calculate_divided_differences(x, y):
    n = len(y)
    k = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        k[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            k[i][j] = (k[i + 1][j - 1] - k[i][j - 1]) / (x[i + j] - x[i])

    return k[0]


def is_finite_difference(x):
    n = len(x)
    h = x[1] - x[0]
    for i in range(1, n):
        if abs((x[i] - x[i - 1]) - h) > 1e-6:
            return False
    return True
