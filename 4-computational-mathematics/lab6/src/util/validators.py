import numpy as np


def is_save_interval(x0, xn, f):
    for x in np.linspace(x0, xn, int((xn - x0) * 1000)):
        try:
            f(x)
        except Exception:
            return False
    return True
