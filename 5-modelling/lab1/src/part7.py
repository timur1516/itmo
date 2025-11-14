from math import sqrt

import numpy as np

from lab1.src.part1 import latex_part_1
from lab1.src.part2 import plot_part_2
from lab1.src.part3 import plot_part_3
from lab1.src.part4 import plot_part_4


def corr(x, y):
    xm = np.mean(x)
    ym = np.mean(y)

    sxyi = 0
    for i in range(len(x)):
        sxyi += (x[i] - xm) * (y[i] - ym)

    sxi2 = 0
    for i in range(len(x)):
        sxi2 += (x[i] - xm) ** 2

    syi2 = 0
    for i in range(len(x)):
        syi2 += (x[i] - xm) ** 2

    r = sxyi / (sqrt(sxi2) * sqrt(syi2))

    return r


def do_part_7(data, generated_data):
    tex7 = latex_part_1(generated_data)
    print(f'\n{tex7}\n')

    plot_part_2(generated_data, 'part2_7.png')

    plot_part_3(generated_data, 'part3_7.png')

    plot_part_4(generated_data, 'part4_7.png')

    r = corr(data, generated_data)

    print(f'r = {r:.4f}')