from math import sqrt

import numpy as np


# def generate_hyperexp(q, t1, t2, size=300):
#     np.random.seed(42)
#     r1 = np.random.rand(size)  # выбор компоненты
#     r2 = np.random.rand(size)  # для экспоненты
#
#     lambdas = np.where(r1 < q, t1, t2)  # если r1 < q, то t1, иначе t2
#     samples = -np.log(1 - r2) / lambdas
#
#     return samples


def generate_hyperexp(q, t1, t2, n_samples=300):
    np.random.seed(42)

    generated_numbers = []

    for i in range(n_samples):
        r1 = np.random.uniform(0, 1)
        r2 = np.random.uniform(0, 1)

        if r1 < q:
            x = t1 * -np.log(1 - r2)
        else:
            x = t2 * -np.log(1 - r2)

        generated_numbers.append(x)

    return generated_numbers


def do_part_6(data):
    t = np.mean(data)
    var = np.std(data, ddof=1) / np.mean(data)

    q = 0.5

    t1 = (1 + sqrt(((1 - q) / (2 * q)) * (var ** 2 - 1))) * t
    t2 = (1 - sqrt((q / (2 * (1 - q))) * (var ** 2 - 1))) * t

    generated_data = generate_hyperexp(q, t1, t2)

    return generated_data
