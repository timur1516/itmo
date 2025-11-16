# Параметры системы
lam = 0.3  # интенсивность входящего потока
b = 15.0
mu = 1 / b  # интенсивность обслуживания
P1, P2, P3 = 0.5, 0.15, 0.35

# Генерация всех допустимых состояний
codes = [
    (0, 0, 0, 0),
    (1, 0, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (1, 0, 1, 0),
    (1, 0, 0, 1),
    (0, 0, 1, 1),
    (1, 1, 0, 0),
    (1, 0, 1, 1),
    (1, 1, 1, 0),
    (1, 1, 0, 1),
    (1, 2, 0, 0),
    (1, 1, 1, 1),
    (1, 2, 1, 0),
    (1, 2, 0, 1),
    (1, 2, 1, 1),
]

p = [
    0.0149, 0.0319, 0.0085, 0.0213, 0.0183, 0.0456, 0.0122, 0.0685,
    0.0261, 0.0391, 0.0978, 0.1467, 0.0559, 0.0838, 0.2096, 0.1198
]


def generate_states_system1():
    states = []
    state_id = 0

    for (n1, q1, n2, n3) in codes:
        # Проверка: если П1 свободен (n1=0), то очередь должна быть 0
        if n1 == 0 and q1 > 0:
            continue
        # Всё остальное — допустимо
        code = f"{n1}/{q1}/{n2}/{n3}"
        # Описание
        parts = []

        total = n1 + q1 + n2 + n3
        if total == 0:
            desc = "В системе нет заявок"
        else:
            if n1 == 1:
                parts.append("П1")
            if n2 == 1:
                parts.append("П2")
            if n3 == 1:
                parts.append("П3")
            if q1 == 1:
                parts.append("в очереди перед П1")
            elif q1 == 2:
                parts.append("в очереди перед П1 (2)")

            desc = f"В системе {total} заявок: на " + ", ".join(parts)

        states.append((f"[S{state_id}]", f"[{code}]", f"[{desc}]"))
        state_id += 1

    for s in states:
        print(f"{s[0]}, {s[1]}, {s[2]},")


def generate_intensity_matrix_system1():
    # Генерация всех допустимых состояний
    states = []
    state_to_id = {}
    state_id = 0

    for code in codes:
        state_label = f"S{state_id}"
        states.append((code, state_label))
        state_to_id[code] = state_id
        state_id += 1

    n_states = len(states)

    # Инициализация матрицы нулями
    matrix = [[0.0 for _ in range(n_states)] for _ in range(n_states)]

    # Заполнение матрицы
    for code, src_state in states:
        n1, q1, n2, n3 = code
        src_idx = state_to_id[code]

        # --- Поступление заявки ---
        # Направляется к П1
        if n1 == 1 and q1 < 2:  # П1 занят, есть место в очереди
            new_code = (n1, q1 + 1, n2, n3)
            if new_code in state_to_id:
                rate = lam * P1
                dst_idx = state_to_id[new_code]
                matrix[src_idx][dst_idx] = rate
        elif n1 == 0:  # П1 свободен → сразу на обслуживание
            new_code = (1, q1, n2, n3)
            if new_code in state_to_id:
                rate = lam * P1
                dst_idx = state_to_id[new_code]
                matrix[src_idx][dst_idx] = rate

        # Направляется к П2
        if n2 == 0:  # П2 свободен
            new_code = (n1, q1, 1, n3)
            if new_code in state_to_id:
                rate = lam * P2
                dst_idx = state_to_id[new_code]
                matrix[src_idx][dst_idx] = rate

        # Направляется к П3
        if n3 == 0:  # П3 свободен
            new_code = (n1, q1, n2, 1)
            if new_code in state_to_id:
                rate = lam * P3
                dst_idx = state_to_id[new_code]
                matrix[src_idx][dst_idx] = rate

        # --- Завершение обслуживания ---
        # На П1
        if n1 == 1:
            if q1 > 0:
                # очередь не пуста → новая заявка идёт на обслуживание
                new_code = (1, q1 - 1, n2, n3)
            else:
                # очередь пуста → П1 освобождается
                new_code = (0, 0, n2, n3)
            if new_code in state_to_id:
                dst_idx = state_to_id[new_code]
                matrix[src_idx][dst_idx] = mu

        # На П2
        if n2 == 1:
            new_code = (n1, q1, 0, n3)
            if new_code in state_to_id:
                dst_idx = state_to_id[new_code]
                matrix[src_idx][dst_idx] = mu

        # На П3
        if n3 == 1:
            new_code = (n1, q1, n2, 0)
            if new_code in state_to_id:
                dst_idx = state_to_id[new_code]
                matrix[src_idx][dst_idx] = mu

    # Вычисление диагональных элементов (g_ii = -sum_{j≠i} g_ij)
    for i in range(n_states):
        row_sum = sum(matrix[i])
        matrix[i][i] = -row_sum

    state_names = [s[1] for s in states]

    for i in range(n_states):
        for j in range(i + 1, n_states):
            if matrix[i][j] != 0:
                print(f'S{i} -> S{j}')

    for r in matrix:
        for c in r:
            print(f"{c:.2f}", end=" ")
        print()

    print("[C1], ", end="")
    for i in range(len(matrix)):
        print(f"[S{i}], ", end="")
    print()
    for i, row in enumerate(matrix):
        print(f"[S{i}], ", end="")
        for j, val in enumerate(row):
            if val == 0:
                print("[]", end="")
            else:
                if i == j:
                    print(f"table.cell(fill: rgb(200, 200, 200))[{val:.3f}]", end="")
                else:
                    print(f"[{val:.3f}]", end="")
            if j < len(row) - 1:
                print(", ", end="")
        if i < len(matrix) - 1:
            print(",\n ", end="")


def generate_typst_table_system1():
    lam1 = lam * P1
    lam2 = lam * P2
    lam3 = lam * P3

    # Стационарные вероятности (пример для 24 состояний, как в СИСТЕМЕ_1)
    # В реальной работе — результат из MARK

    n_states = len(p)

    # Загрузки (через вероятности простоя)
    def safe_sum(indices):
        return sum(p[i] for i in indices if i < n_states)

    p1 = [[], []]
    p1_q = [[], [], []]
    p2 = [[], []]
    p3 = [[], []]

    for i in range(len(codes)):
        (n1, q1, n2, n3) = codes[i]
        p1[n1].append(i)
        p1_q[q1].append(i)
        p2[n2].append(i)
        p3[n3].append(i)

    rho1 = 1 - safe_sum(p1[0])
    rho2 = 1 - safe_sum(p2[0])
    rho3 = 1 - safe_sum(p3[0])
    rho_sum = (rho1 + rho2 + rho3) / 3

    # Вероятности потери
    pi1 = safe_sum(p1_q[2])
    pi2 = safe_sum(p2[1])
    pi3 = safe_sum(p3[1])
    pi_sum = P1 * pi1 + P2 * pi2 + P3 * pi3

    # Длины очередей
    l1 = safe_sum(p1_q[1]) + 2 * safe_sum(p1_q[2])
    l2 = 0.0
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

    print(f'''
[Хар-ка], [Прибор], [Расчетная формула], [Сист.1],

table.cell(rowspan: 4)[Нагрузка],
[П1], [$y_1 = lambda_1 dot b$], [{lam1 * b:.1f}],
[П2], [$y_2 = lambda_2 dot b$], [{lam2 * b:.1f}],
[П3], [$y_3 = lambda_3 dot b$], [{lam3 * b:.1f}],
[Сумм], [$Y = y_1 + y_2 + y_3$], [{lam1 * b + lam2 * b + lam3 * b:.1f}],

table.cell(rowspan: 4)[Загрузка],
[П1], [$rho_1 = 1 - {format_sum(p1[0])}$], [{rho1:.6f}],
[П2], [$rho_2 = 1 - {format_sum(p2[0])}$], [{rho2:.6f}],
[П3], [$rho_3 = 1 - {format_sum(p3[0])}$], [{rho3:.6f}],
[Сумм], [$(rho = rho_1 + rho_2 + rho_3) \\/ 3$], [{rho_sum:.6f}],

table.cell(rowspan: 4)[Вероятность потери],
[П1], [$pi_1 = {format_sum(p1_q[2])}$], [{pi1:.6f}],
[П2], [$pi_2 = {format_sum(p2[1])}$], [{pi2:.6f}],
[П3], [$pi_3 = {format_sum(p3[1])}$], [{pi3:.6f}],
[Сумм], [$pi = P_1 dot pi_1 + P_2 dot pi_2 + P_3 dot pi_3$], [{pi_sum:.6f}],

table.cell(rowspan: 4)[Длина очереди],
[П1], [$l_1 = {format_sum(p1_q[1])} + 2 dot ({format_sum(p1_q[2])})$], [{l1:.6f}],
[П2], [$l_2 = 0$], [{l2:.1f}],
[П3], [$l_3 = 0$], [{l3:.1f}],
[Сумм], [$l = l_1 + l_2 + l_3$], [{l_sum:.6f}],

table.cell(rowspan: 4)[Число заявок в системе],
[П1], [$m_1 = l_1 + rho_1$], [{m1:.6f}],
[П2], [$m_2 = l_2 + rho_2$], [{m2:.6f}],
[П3], [$m_3 = l_3 + rho_3$], [{m3:.6f}],
[Сумм], [$m = m_1 + m_2 + m_3$], [{m_sum:.6f}],

table.cell(rowspan: 4)[Производительность],
[П1], [$lambda_1' = (1 - pi_1) dot lambda_1$], [{lam1_out:.6f}],
[П2], [$lambda_2' = (1 - pi_2) dot lambda_2$], [{lam2_out:.6f}],
[П3], [$lambda_3' = (1 - pi_3) dot lambda_3$], [{lam3_out:.6f}],
[Сумм], [$lambda' = lambda_1' + lambda_2' + lambda_3'$], [{lam_out:.6f}],

table.cell(rowspan: 4)[Коэффициент простоя системы],
[П1], [$eta_1 = 1 - rho_1$], [{eta1:.6f}],
[П2], [$eta_2 = 1 - rho_2$], [{eta2:.6f}],
[П3], [$eta_3 = 1 - rho_3$], [{eta3:.6f}],
[Сумм], [$eta = 1 - rho$], [{eta_sum:.6f}],

table.cell(rowspan: 4)[Время ожидания],
[П1], [$w_1 = l_1 \\/ lambda_1'$], [{w1:.6f}],
[П2], [$w_2 = l_2 \\/ lambda_2'$], [{w2:.1f}],
[П3], [$w_3 = l_3 \\/ lambda_3'$], [{w3:.1f}],
[Сумм], [$w = l \\/ lambda'$], [{w_sum:.6f}],

table.cell(rowspan: 4)[Время пребывания],
[П1], [$u_1 = w_1 + b$], [{u1:.6f}],
[П2], [$u_2 = w_2 + b$], [{u2:.6f}],
[П3], [$u_3 = w_3 + b$], [{u3:.1f}],
[Сумм], [$u = w + b$], [{u_sum:.6f}],
''')


generate_states_system1()
generate_intensity_matrix_system1()
generate_typst_table_system1()