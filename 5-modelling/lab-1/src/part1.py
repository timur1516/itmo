import numpy as np
from scipy import stats

def compute_form1_results(data):

    def calc_mean(d):
        return np.mean(d)
    def calc_var(d):
        return np.var(d, ddof=1)
    def calc_std(d):
        return np.std(d, ddof=1)
    def calc_cv(d):
        return calc_std(d) / calc_mean(d)
    def calc_me(d, alpha):
        z_score = stats.norm.ppf(1 - alpha / 2)
        return z_score * (calc_std(d) / np.sqrt(len(d)))

    def rel_dev(val, best):
        return abs(val - best) / best * 100 if best != 0 else 0.0

    sample_sizes = [10, 20, 50, 100, 200, 300]
    results = {}

    best_mean = calc_mean(data)
    best_var = calc_var(data)
    best_std = calc_std(data)
    best_cv = calc_cv(data)
    best_me_90 = calc_me(data, 0.9)
    best_me_95 = calc_me(data, 0.95)
    best_me_99 = calc_me(data, 0.99)

    for n in sample_sizes:
        sample = data[:n]

        mean = calc_mean(sample)
        var = calc_var(sample)
        std = calc_std(sample)
        cv = calc_cv(sample)

        me_90 = calc_me(sample, 0.9)
        me_95 = calc_me(sample, 0.95)
        me_99 = calc_me(sample, 0.99)

        results[n] = {
            'mean': mean,
            'mean_dev': rel_dev(mean, best_mean),
            'var': var,
            'var_dev': rel_dev(var, best_var),
            'std': std,
            'std_dev': rel_dev(std, best_std),
            'cv': cv,
            'cv_dev': rel_dev(cv, best_cv),
            'me_90': me_90,
            'me_90_dev': rel_dev(me_90, best_me_90),
            'me_95': me_95,
            'me_95_dev': rel_dev(me_95, best_me_95),
            'me_99': me_99,
            'me_99_dev': rel_dev(me_99, best_me_99),
        }

    return results

def latex_part_1(data):
    results = compute_form1_results(data)
    # Извлекаем значения для каждого n
    n_vals = [10, 20, 50, 100, 200, 300]

    def f_val(x): return f"{x:.4f}"

    # Извлекаем данные в удобные переменные
    mean_vals = [f_val(results[n]['mean']) for n in n_vals]
    mean_devs = [f_val(results[n]['mean_dev']) for n in n_vals]

    me90_vals = [f_val(results[n]['me_90']) for n in n_vals]
    me90_devs = [f_val(results[n]['me_90_dev']) for n in n_vals]

    me95_vals = [f_val(results[n]['me_95']) for n in n_vals]
    me95_devs = [f_val(results[n]['me_95_dev']) for n in n_vals]

    me99_vals = [f_val(results[n]['me_99']) for n in n_vals]
    me99_devs = [f_val(results[n]['me_99_dev']) for n in n_vals]

    var_vals = [f_val(results[n]['var']) for n in n_vals]
    var_devs = [f_val(results[n]['var_dev']) for n in n_vals]

    std_vals = [f_val(results[n]['std']) for n in n_vals]
    std_devs = [f_val(results[n]['std_dev']) for n in n_vals]

    cv_vals = [f_val(results[n]['cv']) for n in n_vals]
    cv_devs = [f_val(results[n]['cv_dev']) for n in n_vals]

    # Распаковываем списки в переменные для f-строки
    m10, m20, m50, m100, m200, m300 = mean_vals
    md10, md20, md50, md100, md200, md300 = mean_devs

    d90_10, d90_20, d90_50, d90_100, d90_200, d90_300 = me90_vals
    d90d10, d90d20, d90d50, d90d100, d90d200, d90d300 = me90_devs

    d95_10, d95_20, d95_50, d95_100, d95_200, d95_300 = me95_vals
    d95d10, d95d20, d95d50, d95d100, d95d200, d95d300 = me95_devs

    d99_10, d99_20, d99_50, d99_100, d99_200, d99_300 = me99_vals
    d99d10, d99d20, d99d50, d99d100, d99d200, d99d300 = me99_devs

    v10, v20, v50, v100, v200, v300 = var_vals
    vd10, vd20, vd50, vd100, vd200, vd300 = var_devs

    s10, s20, s50, s100, s200, s300 = std_vals
    sd10, sd20, sd50, sd100, sd200, sd300 = std_devs

    c10, c20, c50, c100, c200, c300 = cv_vals
    cd10, cd20, cd50, cd100, cd200, cd300 = cv_devs

    latex_code = f'''
#figure(
  align(center)[#table(
    columns: 8,
    align: (left, center, center, center, center, center, center, center,),
    table.header(
      [#strong[Характеристика];], [],
      table.cell(align: center, colspan: 6)[#strong[Количество случайных величин];],
    ),
    table.hline(),
    [3-8], [], [10], [20], [50], [100], [200], [300],
    table.cell(rowspan: 2)[#strong[Мат.ож.];], [Знач.],
    [{m10}], [{m20}], [{m50}], [{m100}], [{m200}],
    table.cell(rowspan: 2)[{m300}],
    [%], [{md10}], [{md20}], [{md50}], [{md100}], [{md200}],
    table.cell(rowspan: 2)[Дов. инт. (0.9)], [Знач.],
    [{d90_10}], [{d90_20}], [{d90_50}], [{d90_100}], [{d90_200}],
    table.cell(rowspan: 2)[{d90_300}],
    [%], [{d90d10}], [{d90d20}], [{d90d50}], [{d90d100}], [{d90d200}],
    table.cell(rowspan: 2)[Дов. инт. (0.95)], [Знач.],
    [{d95_10}], [{d95_20}], [{d95_50}], [{d95_100}], [{d95_200}],
    table.cell(rowspan: 2)[{d95_300}],
    [%], [{d95d10}], [{d95d20}], [{d95d50}], [{d95d100}], [{d95d200}],
    table.cell(rowspan: 2)[Дов. инт. (0.99)], [Знач.],
    [{d99_10}], [{d99_20}], [{d99_50}], [{d99_100}], [{d99_200}],
    table.cell(rowspan: 2)[{d99_300}],
    [%], [{d99d10}], [{d99d20}], [{d99d50}], [{d99d100}], [{d99d200}],
    table.cell(rowspan: 2)[#strong[Дисперсия];], [Знач.],
    [{v10}], [{v20}], [{v50}], [{v100}], [{v200}],
    table.cell(rowspan: 2)[{v300}],
    [%], [{vd10}], [{vd20}], [{vd50}], [{vd100}], [{vd200}],
    table.cell(rowspan: 2)[#strong[С.к.о.];], [Знач.],
    [{s10}], [{s20}], [{s50}], [{s100}], [{s200}],
    table.cell(rowspan: 2)[{s300}],
    [%], [{sd10}], [{sd20}], [{sd50}], [{sd100}], [{sd200}],
    table.cell(rowspan: 2)[#strong[К-т вариации];], [Знач.],
    [{c10}], [{c20}], [{c50}], [{c100}], [{c200}],
    table.cell(rowspan: 2)[{c300}],
    [%], [{cd10}], [{cd20}], [{cd50}], [{cd100}], [{cd200}],
  )],
  kind: table,
)
'''
    return latex_code.strip()

