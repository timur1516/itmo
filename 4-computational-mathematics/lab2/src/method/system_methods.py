import numpy as np

from lab2.src.dto.result import Result
from lab2.src.settings.config import MAX_ITERATIONS


def newton_method(system, x0, eps):
    x = x0
    iterations = 0
    log = []
    while True:
        if iterations == MAX_ITERATIONS:
            raise Exception(f'Произведено {MAX_ITERATIONS} итераций, но решение не найдено.')
        iterations += 1

        jcb = system.get_jacobi(x)
        b = system.get_value(x)
        try:
            dx = np.linalg.solve(np.array(jcb), -1 * np.array(b))
        except np.linalg.LinAlgError:
            raise Exception('Не удалось применить метод, промежуточная система не имеет решений!')
        nx = x + dx

        log.append({
            'x_i': x,
            'x_{i+1}': nx.tolist(),
            'dx': dx.tolist()
        })

        if np.max(np.abs(nx - x)) <= eps:
            break
        x = nx.tolist()

    return Result(x, iterations, log)
