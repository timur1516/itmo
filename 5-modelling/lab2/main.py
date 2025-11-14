def generate_states_system1():
    states = []
    state_id = 0

    # n1: 0 или 1 (П1 занят или нет)
    # q1: 0, 1, 2 (очередь перед П1)
    # n2: 0 или 1 (П2 занят или нет)
    # n3: 0 или 1 (П3 занят или нет)

    for q1 in range(0, 3):  # 0, 1, 2
        for n3 in [0, 1]:
            for n2 in [0, 1]:
                for n1 in [0, 1]:
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

    return states

def main():
    # Генерация и вывод
    states = generate_states_system1()
    for s in states:
        print(f"{s[0]}, {s[1]}, {s[2]},")

if __name__ == "__main__":
    main()