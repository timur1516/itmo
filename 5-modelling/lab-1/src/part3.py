import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def autocorrelation(data, lag):
    dd = pd.Series(data)
    acf = [dd.autocorr(lag=k) for k in range(1, lag + 1)]
    return np.array(acf)

def latex_part_3(data):
    acf = autocorrelation(data, 10)
    formatted = [f"{x:.4f}" for x in acf]
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 = formatted

    latex_code = f'''
#figure(
  align(center)[#table(
    columns: 11,
    align: (center, center, center, center, center, center, center, center, center, center, center,),
    table.header(
      [#strong[Сдвиг ЧП];], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10],
    ),
    table.hline(),
    [#strong[К-т АК];],
    [{c1}], [{c2}], [{c3}], [{c4}], [{c5}], [{c6}], [{c7}], [{c8}], [{c9}], [{c10}],
  )],
  kind: table,
)
'''
    return latex_code.strip()

def plot_part_3(data, name, lag=10):
    acf = autocorrelation(data, lag)
    plt.plot(range(1, 10+1), acf)
    plt.title('Автокорреляционный анализ')
    plt.xlabel('Сдвиг')
    plt.ylabel('Коэффициент автокорреляции')
    plt.tight_layout()
    plt.savefig(f'lab1/img/{name}', dpi=300)
    plt.clf()