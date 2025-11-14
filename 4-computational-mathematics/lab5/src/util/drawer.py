import numpy as np
from matplotlib import pyplot as plt


def draw_plot(x, y, x0, polynomes, names):
    x = np.array(x)
    y = np.array(y)

    y0 = [p(x0) for p in polynomes]
    x0 = [x0 for _ in polynomes]

    x_min, x_max = min([*x, *x0]), max([*x, *x0])
    x_margin = (x_max - x_min) * 0.1 if x_min != x_max else 1
    y_min, y_max = min([*y, *y0]), max([*y, *y0])
    y_margin = (y_max - y_min) * 0.1 if y_min != y_max else 1

    plt.figure(figsize=(8, 6))

    plt.scatter(x, y, color='blue', label='Точки (x, y)')

    x_smooth = np.linspace(x_min - x_margin, x_max + x_margin, 1000)
    for i, p in enumerate(polynomes):
        y_smooth = np.array(list(map(p, x_smooth)))
        plt.plot(x_smooth, y_smooth, label=names[i])

    plt.scatter(x0, y0, color='red', label='Исследуемая (x, y)')

    plt.xlim(x_min - x_margin, x_max + x_margin)
    plt.ylim(y_min - y_margin, y_max + y_margin)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()
