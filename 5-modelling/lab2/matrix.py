def generate_intensity_matrix_system1():
    # Параметры системы
    lam = 0.3          # интенсивность входящего потока
    mu = 1 / 15        # интенсивность обслуживания
    P1, P2, P3 = 0.5, 0.15, 0.35

    # Генерация всех допустимых состояний
    states = []
    state_to_id = {}
    state_id = 0

    for q1 in range(0, 3):  # 0, 1, 2
        for n3 in [0, 1]:
            for n2 in [0, 1]:
                for n1 in [0, 1]:
                    if n1 == 0 and q1 > 0:
                        continue  # недопустимо: очередь без обслуживания
                    code = (n1, q1, n2, n3)
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

    return matrix, [s[1] for s in states]  # Возвращаем матрицу и список имён состояний

# Генерация и вывод
matrix, state_names = generate_intensity_matrix_system1()

for r in matrix:
    for c in r:
        print(f"{c:.6f}", end=" ")
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
                print(f"table.cell(fill: rgb(200, 200, 200))[{val:.2f}]", end="")
            else:
                print(f"[{val:.2f}]", end="")
        if j < len(row) - 1:
            print(", ", end="")
    if i < len(matrix) - 1:
        print(",\n ", end="")