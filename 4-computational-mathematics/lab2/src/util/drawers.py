import numpy as np
from matplotlib import pyplot as plt


def draw_equation(x0, left, right, equation):
    side_step = abs(right - left) * 0.15
    l = left - side_step
    r = right + side_step

    plt.figure(figsize=(10, 10))

    x = np.linspace(l, r, 1000)
    y = equation.f(x)
    plt.plot(x, y, label=f'f(x)', color='blue')

    y0 = equation.f(x0)
    plt.scatter([x0], [y0], label=f'({round(x0, 3)}; {round(y0, 3)})', color='red', s=50)

    x_l = left
    y_l = equation.f(x_l)
    plt.vlines(x_l, 0, y_l, colors='black', linestyles='--')
    plt.scatter([x_l], [y_l], color='black', s=50)

    x_r = right
    y_r = equation.f(x_r)
    plt.vlines(x_r, 0, y_r, colors='black', linestyles='--')
    plt.scatter([x_r], [y_r], color='black', s=50)

    plt.axhline(0, color='black')

    plt.title(f'График функции f(x)={equation.text}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.xlim(l, r)
    plt.show()


def draw_system(x0, point, system):
    if system.n > 2: return
    r = np.sqrt(max(x0[0] ** 2 + x0[1] ** 2, point[0] ** 2 + point[1] ** 2)) * 1.5
    x_min, x_max = -r, r
    y_min, y_max = -r, r

    plt.figure(figsize=(10, 10))

    x = np.linspace(x_min, x_max, 1000)
    y = np.linspace(y_min, y_max, 1000)
    x, y = np.meshgrid(x, y)
    f = system.equations[0].f([x, y])
    g = system.equations[1].f([x, y])
    plt.contour(x, y, f, levels=[0], colors='blue')
    plt.contour(x, y, g, levels=[0], colors='green')

    plt.scatter([x0[0]], [x0[1]], label=f'({round(x0[0], 3)}; {round(x0[1], 3)})', color='red', s=50)
    plt.scatter([point[0]], [point[1]], label=f'({round(point[0], 3)}; {round(point[1], 3)})', color='black', s=50)

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.title(f'График функции f(x)={system.equations[0].text}')
    plt.title(f'График функции g(x)={system.equations[1].text}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.show()
