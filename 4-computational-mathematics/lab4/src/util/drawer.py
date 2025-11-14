import numpy as np
from matplotlib import pyplot as plt


def draw_plot(x, y, phis, names):
    x = np.array(x)
    y = np.array(y)

    x_min, x_max = min(x), max(x)
    x_margin = (x_max - x_min) * 0.1 if x_min != x_max else 1
    y_min, y_max = min(y), max(y)
    y_margin = (y_max - y_min) * 0.1 if y_min != y_max else 1

    plt.figure(figsize=(8, 6))

    plt.scatter(x, y, color='blue', label='Точки (x, y)')

    x_smooth = np.linspace(x_min - x_margin, x_max + x_margin, 1000)
    for i, phi in enumerate(phis):
        y_smooth = phi(x_smooth)
        plt.plot(x_smooth, y_smooth, label=names[i])

    plt.xlim(x_min - x_margin, x_max + x_margin)
    plt.ylim(y_min - y_margin, y_max + y_margin)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()
