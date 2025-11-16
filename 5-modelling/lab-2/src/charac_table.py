def generate_typst_table_system1():
    # Параметры из варианта 1/8/8 → NG=8 → λ=0.3, b=15
    lam_total = 0.3
    b = 15.0
    P1, P2, P3 = 0.5, 0.15, 0.35
    lam1 = lam_total * P1  # 0.15
    lam2 = lam_total * P2  # 0.045
    lam3 = lam_total * P3  # 0.105

    # Стационарные вероятности (пример для 24 состояний, как в СИСТЕМЕ_1)
    # В реальной работе — результат из MARK
    p = [
        0.150635, 0.117448, 0.062942, 0.120881,
        0.025221, 0.074269, 0.072665, 0.072091,
        0.015622, 0.049536, 0.061319, 0.017945,
        0.036974, 0.021110, 0.042547, 0.016405,
        0.026124, 0.016266, 0.012345, 0.009876,
        0.008765, 0.007654, 0.006543, 0.005432
    ]
    n_states = len(p)

    # Загрузки (через вероятности простоя)
    def safe_sum(indices):
        return sum(p[i] for i in indices if i < n_states)

    rho1 = 1 - safe_sum([0, 2, 3, 6, 8, 11])
    rho2 = 1 - safe_sum([0, 1, 3, 5, 7, 10])
    rho3 = 1 - safe_sum([0, 1, 2, 4, 7, 8, 12, 13, 16])
    rho_sum = (rho1 + rho2 + rho3) / 3

    # Вероятности потери
    pi1 = safe_sum([7, 10, 12, 14, 16, 17])
    pi2 = safe_sum([8, 11, 13, 15, 16, 17])
    pi3 = rho3  # как в doc.pdf
    pi_sum = P1 * pi1 + P2 * pi2 + P3 * pi3

    # Длины очередей
    l1 = pi1
    l2 = pi2
    l3 = 0.0
    l_sum = l1 + l2 + l3

    # Число заявок в системе
    m1 = l1 + rho1
    m2 = l2 + rho2
    m3 = l3 + rho3
    m_sum = m1 + m2 + m3

    # Производительность
    lam1_out = (1 - pi1) * lam1
    lam2_out = (1 - pi2) * lam2
    lam3_out = (1 - pi3) * lam3
    lam_out = lam1_out + lam2_out + lam3_out

    # Коэффициенты простоя
    eta1 = 1 - rho1
    eta2 = 1 - rho2
    eta3 = 1 - rho3
    eta_sum = 1 - rho_sum

    # Время ожидания
    w1 = l1 / lam1_out if lam1_out > 1e-9 else 0.0
    w2 = l2 / lam2_out if lam2_out > 1e-9 else 0.0
    w3 = 0.0
    w_sum = l_sum / lam_out if lam_out > 1e-9 else 0.0

    # Время пребывания
    u1 = w1 + b
    u2 = w2 + b
    u3 = w3 + b
    u_sum = w_sum + b

    # Форматируем формулы в стиле Typst: p_0 → p0, суммы → p7 + p10 + ...
    def format_sum(indices):
        terms = [f"p_{i}" for i in sorted(indices) if i < n_states]
        if not terms:
            return "0"
        return " + ".join(terms)

    # Формулы
    f_rho1 = f"1 - ({format_sum([0, 2, 3, 6, 8, 11])})"
    f_rho2 = f"1 - ({format_sum([0, 1, 3, 5, 7, 10])})"
    f_rho3 = f"1 - ({format_sum([0, 1, 2, 4, 7, 8, 12, 13, 16])})"
    f_pi1 = format_sum([7, 10, 12, 14, 16, 17])
    f_pi2 = format_sum([8, 11, 13, 15, 16, 17])
    f_pi3 = "rho_3"

    print(f'''
[Хар-ка], [Прибор], [Расчетная формула], [Сист.1],

table.cell(rowspan: 4)[Нагрузка],
[П1], [$y_1 = lambda_1 dot b$], [{lam1 * b:.1f}],
[П2], [$y_2 = lambda_2 dot b$], [{lam2 * b:.1f}],
[П3], [$lambda_3 dot b$], [{lam3 * b:.1f}],
[Сумм], [$y_1 + y_2 + y_3$], [{lam1*b + lam2*b + lam3*b:.1f}],

table.cell(rowspan: 4)[Загрузка],
[П1], [${f_rho1}$], [{rho1:.6f}],
[П2], [${f_rho2}$], [{rho2:.6f}],
[П3], [${f_rho3}$], [{rho3:.6f}],
[Сумм], [$(rho_1 + rho_2 + rho_3) / 3$], [{rho_sum:.6f}],

table.cell(rowspan: 4)[Вероятность потери],
[П1], [${f_pi1}$], [{pi1:.6f}],
[П2], [${f_pi2}$], [{pi2:.6f}],
[П3], [${f_pi3}$], [{pi3:.6f}],
[Сумм], [$P_1 dot pi_1 + P_2 dot pi_2 + P_3 dot pi_3$], [{pi_sum:.6f}],

table.cell(rowspan: 4)[Длина очереди],
[П1], [$pi_1$], [{l1:.6f}],
[П2], [$pi_2$], [{l2:.6f}],
[П3], [$0$], [{l3:.1f}],
[Сумм], [$l_1 + l_2 + l_3$], [{l_sum:.6f}],

table.cell(rowspan: 4)[Число заявок в системе],
[П1], [$l_1 + rho_1$], [{m1:.6f}],
[П2], [$l_2 + rho_2$], [{m2:.6f}],
[П3], [$l_3 + rho_3$], [{m3:.6f}],
[Сумм], [$m_1 + m_2 + m_3$], [{m_sum:.6f}],

table.cell(rowspan: 4)[Производительность],
[П1], [$(1 - pi_1) dot lambda_1$], [{lam1_out:.6f}],
[П2], [$(1 - pi_2) dot lambda_2$], [{lam2_out:.6f}],
[П3], [$(1 - pi_3) dot lambda_3$], [{lam3_out:.6f}],
[Сумм], [$lambda_1' + lambda_2' + lambda_3'$], [{lam_out:.6f}],

table.cell(rowspan: 4)[Коэффициент простоя системы],
[П1], [$1 - rho_1$], [{eta1:.6f}],
[П2], [$1 - rho_2$], [{eta2:.6f}],
[П3], [$1 - rho_3$], [{eta3:.6f}],
[Сумм], [$1 - rho$], [{eta_sum:.6f}],

table.cell(rowspan: 4)[Время ожидания],
[П1], [$l_1 \\/ lambda_1'$], [{w1:.6f}],
[П2], [$l_2 \\/ lambda_2'$], [{w2:.6f}],
[П3], [$l_3 \\/ lambda_3'$], [{w3:.1f}],
[Сумм], [$l \\/ lambda'$], [{w_sum:.6f}],

table.cell(rowspan: 4)[Время пребывания],
[П1], [$w_1 + b$], [{u1:.6f}],
[П2], [$w_2 + b$], [{u2:.6f}],
[П3], [$w_3 + b$], [{u3:.1f}],
[Сумм], [$w + b$], [{u_sum:.6f}],
''')

# Запуск
generate_typst_table_system1()