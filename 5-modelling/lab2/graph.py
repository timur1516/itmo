def generate_edges_system1():
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
                    state_to_id[code] = state_label
                    state_id += 1

    edges = []

    # Добавляем переходы
    for code, src_state in states:
        n1, q1, n2, n3 = code

        # --- Поступление заявки ---
        # Направляется к П1
        if n1 == 1 and q1 < 2:  # П1 занят, есть место в очереди
            new_code = (n1, q1 + 1, n2, n3)
            if new_code in state_to_id:
                rate = lam * P1
                dst_state = state_to_id[new_code]
                edges.append(f"{src_state} -> {dst_state}")
        elif n1 == 0:  # П1 свободен → сразу на обслуживание
            new_code = (1, q1, n2, n3)
            if new_code in state_to_id:
                rate = lam * P1
                dst_state = state_to_id[new_code]
                edges.append(f"{src_state} -> {dst_state}")

        # Направляется к П2
        if n2 == 0:  # П2 свободен
            new_code = (n1, q1, 1, n3)
            if new_code in state_to_id:
                rate = lam * P2
                dst_state = state_to_id[new_code]
                edges.append(f"{src_state} -> {dst_state}")

        # Направляется к П3
        if n3 == 0:  # П3 свободен
            new_code = (n1, q1, n2, 1)
            if new_code in state_to_id:
                rate = lam * P3
                dst_state = state_to_id[new_code]
                edges.append(f"{src_state} -> {dst_state}")

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
                dst_state = state_to_id[new_code]
                edges.append(f"{src_state} -> {dst_state}")

        # На П2
        if n2 == 1:
            new_code = (n1, q1, 0, n3)
            if new_code in state_to_id:
                dst_state = state_to_id[new_code]
                edges.append(f"{src_state} -> {dst_state}")

        # На П3
        if n3 == 1:
            new_code = (n1, q1, n2, 0)
            if new_code in state_to_id:
                dst_state = state_to_id[new_code]
                edges.append(f"{src_state} -> {dst_state}")

    return edges

# Генерация и вывод
edges = generate_edges_system1()
for edge in edges:
    print(edge)