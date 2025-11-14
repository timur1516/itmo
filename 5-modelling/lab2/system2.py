import math

# Параметры системы
lam = 0.3  # интенсивность входящего потока
b = 15.0
nu = 2.4  # коэффициент вариации
q = 1 / 7  # вероятность выбора первой фазы (из методички)

# Генерация всех допустимых состояний
codes = [
    (0, 0),
    (1, 0),
    (2, 0),
    (1, 1),
    (2, 1),
    (1, 2),
    (2, 2),
    (1, 3),
    (2, 3),
]

p = [
    0.0131, 0.0055, 0.0214, 0.0131, 0.0438, 0.0293, 0.0925, 0.6273, 0.1541
]


def generate_intensity_matrix_system1():
    term1 = (1 - q) / (2 * q) * (nu ** 2 - 1)
    b1_prime = (1 + math.sqrt(term1)) * b
    mu1 = 1 / b1_prime

    term2 = q / (2 * (1 - q)) * (nu ** 2 - 1)
    b2_prime = (1 - math.sqrt(term2)) * b
    mu2 = 1 / b2_prime

    print(f"b1' = {b1_prime:.6f}, b2' = {b2_prime:.6f}")
    print(f"μ1 = {mu1:.6f}, μ2 = {mu2:.6f}")

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

    # Заполнение переходов
    for code, src_label in states:
        f, queue_len = code  # ← используем другое имя
        src_id = state_to_id[code]

        if f == 0:
            # Поступление в пустую систему
            if (1, 0) in state_to_id:
                matrix[src_id][state_to_id[(1, 0)]] = lam * q  # q = 1/7 — вероятность фазы
            if (2, 0) in state_to_id:
                matrix[src_id][state_to_id[(2, 0)]] = lam * (1 - q)
        else:
            # Поступление (если очередь < 3)
            if queue_len < 3:
                if (f, queue_len + 1) in state_to_id:
                    matrix[src_id][state_to_id[(f, queue_len + 1)]] = lam

            # Завершение обслуживания
            mu = mu1 if f == 1 else mu2

            if queue_len == 0:
                # Система становится пустой
                matrix[src_id][state_to_id[(0, 0)]] = mu
            else:
                # Новая заявка идёт на обслуживание с вероятностями q и (1-q)
                if (1, queue_len - 1) in state_to_id:
                    matrix[src_id][state_to_id[(1, queue_len - 1)]] = mu * q
                if (2, queue_len - 1) in state_to_id:
                    matrix[src_id][state_to_id[(2, queue_len - 1)]] = mu * (1 - q)

    # matrix = matrix_exponential(matrix)

    # Вычисление диагональных элементов (g_ii = -sum_{j≠i} g_ij)
    for i in range(n_states):
        row_sum = sum(matrix[i])
        matrix[i][i] = -row_sum

    state_names = [s[1] for s in states]

    for i in range(n_states):
        for j in range(n_states):
            if matrix[i][j] != 0 and i != j:
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
    n_states = len(p)

    # Загрузки (через вероятности простоя)
    def safe_sum(indices):
        return sum(p[i] for i in indices if i < n_states)

    pp = [[], []]
    p_q = [[], [], [], []]

    for i in range(len(codes)):
        (f, qq) = codes[i]
        if f == 0:
            pp[0].append(i)
        else:
            pp[1].append(i)
        p_q[qq].append(i)

    rho1 = 1 - safe_sum(pp[0])
    rho_sum = rho1

    # Вероятности потери
    pi1 = safe_sum(p_q[3])
    pi_sum = lam * pi1

    # Длины очередей
    l1 = safe_sum(p_q[1]) + 2 * safe_sum(p_q[2]) + 3 * safe_sum(p_q[3])
    l_sum = l1

    # Число заявок в системе
    m1 = l1 + rho1
    m_sum = m1

    # Производительность
    lam1_out = (1 - pi1) * lam
    lam_out = lam1_out

    # Коэффициенты простоя
    eta1 = 1 - rho1
    eta_sum = 1 - rho_sum

    # Время ожидания
    w1 = l1 / lam1_out if lam1_out > 1e-9 else 0.0
    w_sum = l_sum / lam_out if lam_out > 1e-9 else 0.0

    # Время пребывания
    u1 = w1 + b
    u_sum = w_sum + b

    # Форматируем формулы в стиле Typst: p_0 → p0, суммы → p7 + p10 + ...
    def format_sum(indices):
        terms = [f"p_{i}" for i in sorted(indices) if i < n_states]
        if not terms:
            return "0"
        return " + ".join(terms)

    print(f'''
[Хар-ка], [Прибор], [Расчетная формула], [Сист.1],

table.cell(rowspan: 2)[Нагрузка],
[П1], [$y_1 = lambda_1 dot b$], [{lam * b:.1f}],
[Сумм], [$Y = y_1$], [{lam * b:.1f}],

table.cell(rowspan: 2)[Загрузка],
[П1], [$rho_1 = 1 - {format_sum(pp[0])}$], [{rho1:.6f}],
[Сумм], [$(rho = rho_1 + rho_2 + rho_3) \\/ 3$], [{rho_sum:.6f}],

table.cell(rowspan: 2)[Вероятность потери],
[П1], [$pi_1 = {format_sum(p_q[3])}$], [{pi1:.6f}],
[Сумм], [$pi = lambda dot pi_1$], [{pi_sum:.6f}],

table.cell(rowspan: 2)[Длина очереди],
[П1], [$l_1 = {format_sum(p_q[1])} + 2 dot ({format_sum(p_q[2])}) + 3 dot ({format_sum(p_q[3])})$], [{l1:.6f}],
[Сумм], [$l = l_1$], [{l_sum:.6f}],

table.cell(rowspan: 2)[Число заявок в системе],
[П1], [$m_1 = l_1 + rho_1$], [{m1:.6f}],
[Сумм], [$m = m_1$], [{m_sum:.6f}],

table.cell(rowspan: 2)[Производительность],
[П1], [$lambda_1' = (1 - pi_1) dot lambda_1$], [{lam1_out:.6f}],
[Сумм], [$lambda' = lambda_1'$], [{lam_out:.6f}],

table.cell(rowspan: 2)[Коэффициент простоя системы],
[П1], [$eta_1 = 1 - rho_1$], [{eta1:.6f}],
[Сумм], [$eta = 1 - rho$], [{eta_sum:.6f}],

table.cell(rowspan: 2)[Время ожидания],
[П1], [$w_1 = l_1 \\/ lambda_1'$], [{w1:.6f}],
[Сумм], [$w = l \\/ lambda'$], [{w_sum:.6f}],

table.cell(rowspan: 2)[Время пребывания],
[П1], [$u_1 = w_1 + b$], [{u1:.6f}],
[Сумм], [$u = w + b$], [{u_sum:.6f}],
''')


generate_intensity_matrix_system1()
generate_typst_table_system1()
