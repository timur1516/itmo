from scipy.differentiate import derivative


class MultiEquation:
    def __init__(self, f, text):
        self.f = f
        self.text = text

    def __str__(self):
        return self.text

    def partial_derivative(self, x, i):
        g = lambda _x: self.f(x[:i] + [_x] + x[i + 1:])
        return derivative(g, x[i]).df
