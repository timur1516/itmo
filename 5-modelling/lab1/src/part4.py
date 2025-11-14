from math import ceil, sqrt

import numpy as np
from matplotlib import pyplot as plt


def plot_part_4(data, name):
    # Определяем количество интервалов (bins)
    bins = ceil(sqrt(300))  # Округляем вверх sqrt(300), чтобы получить 18 интервалов

    # Вычисляем количество значений в каждом интервале и границы интервалов
    counts, bin_edges = np.histogram(data, bins=bins)

    # Построение гистограммы
    plt.figure(figsize=(12, 6))
    plt.hist(data, bins=bin_edges, color='blue', edgecolor='black', alpha=0.7)

    # Формируем подписи для каждого интервала в формате "min - max"
    bin_labels = [f"{bin_edges[i]:.2f} - {bin_edges[i + 1]:.2f}" for i in range(len(bin_edges) - 1)]

    # Настраиваем метки по оси X
    plt.xticks((bin_edges[:-1] + bin_edges[1:]) / 2, bin_labels, rotation=45, ha='right')

    # Добавляем подписи и сетку
    plt.title('Гистограмма распределения частот', fontsize=15)
    plt.xlabel('Интервалы значений', fontsize=12)
    plt.ylabel('Частота', fontsize=12)
    plt.grid(True)

    plt.tight_layout()  # Для корректного отображения подписей
    plt.savefig(f'lab1/img/{name}', dpi=150     )
    plt.clf()
