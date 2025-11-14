class SystemOfEquations:
    def __init__(self, equations):
        self.equations = equations
        self.n = len(equations)

    def __str__(self):
        return '{' + ''.join(f'{str(eq)}; ' for eq in self.equations) + '}'

    def partial_derivative(self, x, i, j):
        return self.equations[i].partial_derivative(x, j)

    def get_jacobi(self, x):
        jcb = [[] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                jcb[i].append(self.partial_derivative(x, i, j))
        return jcb

    def get_value(self, x):
        v = []
        for e in self.equations:
            v.append(e.f(x))
        return v
