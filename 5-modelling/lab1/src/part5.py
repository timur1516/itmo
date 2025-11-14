from math import sqrt

import numpy as np


def latex_part_5(data):
    t = np.mean(data)
    var = np.std(data, ddof=1) / np.mean(data)

    q = 0.5

    t1 = (1 + sqrt(((1 - q) / (2 * q)) * (var ** 2 - 1))) * t
    t2 = (1 - sqrt((q / (2 * (1 - q))) * (var ** 2 - 1))) * t

    def f_val(x): return f"{x:.4f}"

    print(f'q = {f_val(q)}\nt1 = {f_val(t1)}\nt2 = {f_val(t2)}\n')
