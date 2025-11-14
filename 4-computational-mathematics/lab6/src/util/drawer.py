import numpy as np
from matplotlib import pyplot as plt


def draw_plot(x, y, solution_f, method_name):
    plt.figure(figsize=(8, 6))

    plt.scatter(x, y, color='red', label='Численное решение')

    x_smooth = np.linspace(min(x), max(x), 1000)
    y_smooth = np.array(list(map(solution_f, x_smooth)))
    plt.plot(x_smooth, y_smooth, label='Истинное решение')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title(method_name)
    plt.grid(True)
    plt.tight_layout()

    plt.show()
