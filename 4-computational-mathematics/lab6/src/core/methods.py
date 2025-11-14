from lab6.settings.config import MAX_ITERATIONS


def euler_method(f, x, y0):
    n = len(x)
    y = [y0]
    for i in range(1, n):
        h = x[i] - x[i - 1]
        y.append(y[i - 1] + h * f(x[i - 1], y[i - 1]))
    return y


def improved_euler_method(f, x, y0):
    n = len(x)
    y = [y0]
    for i in range(1, n):
        h = x[i] - x[i - 1]
        y.append(y[i - 1] + (h / 2) * (f(x[i - 1], y[i - 1]) + f(x[i - 1] + h, y[i - 1] + h * f(x[i - 1], y[i - 1]))))
    return y


def fourth_order_runge_kutta_method(f, x, y0):
    n = len(x)
    y = [y0]
    for i in range(1, n):
        h = x[i] - x[i - 1]
        k1 = h * f(x[i - 1], y[i - 1])
        k2 = h * f(x[i - 1] + (h / 2), y[i - 1] + (k1 / 2))
        k3 = h * f(x[i - 1] + (h / 2), y[i - 1] + (k2 / 2))
        k4 = h * f(x[i - 1] + h, y[i - 1] + k3)
        y.append(y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
    return y


def milne_method(f, x, y0, eps):
    n = len(x)
    y = fourth_order_runge_kutta_method(f, x[:4], y0)

    for i in range(4, n):
        h = x[i] - x[i - 1]
        y_pred = y[i - 4] + (4 * h / 3) * (
                2 * f(x[i - 3], y[i - 3]) - f(x[i - 2], y[i - 2]) + 2 * f(x[i - 1], y[i - 1]))

        iterations = 0
        while True:
            if iterations == MAX_ITERATIONS:
                raise Exception(f"Достигнуто максимальное количество итераций")
            iterations += 1
            y_corr = y[i - 2] + (h / 3) * (f(x[i - 2], y[i - 2]) + 4 * f(x[i - 1], y[i - 1]) + f(x[i], y_pred))

            if abs(y_corr - y_pred) < eps:
                y_pred = y_corr
                break
            y_pred = y_corr

        y.append(y_pred)

    return y
