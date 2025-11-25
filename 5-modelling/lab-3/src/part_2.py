import re
import os
import sys

def f(report_text):
    """
    Извлекает значения A, B, C, D, E из отчета GPSS World Simulation.

    Args:
        report_text (str): Текст отчета GPSS

    Returns:
        dict: Словарь с ключами 'A', 'B', 'C', 'D', 'E' и соответствующими значениями
    """
    lines = report_text.split('\n')
    
    # Извлечение значения A (REJECT TERMINATE)
    A = None
    for line in lines:
        if 'REJECT' in line and 'TERMINATE' in line:
            # Ищем строку вида "REJECT    25    TERMINATE    3    0    0"
            parts = line.split()
            if len(parts) >= 4 and parts[2] == 'TERMINATE':
                try:
                    A = int(parts[3])  # Второе число после TERMINATE
                except (ValueError, IndexError):
                    pass
            break

    # Извлечение значений QUEUE
    B = None  # AVE.CONT.
    D = None  # AVE.TIME
    for line in lines:
        if line.strip().startswith('BUF_1'):
            # Пример строки: "BUF_1               1    0      4      2     0.106      5.546     11.092   0"
            parts = line.split()
            if len(parts) >= 7:
                try:
                    B = float(parts[5])  # AVE.CONT. - 6-й элемент (0-индексация)
                    D = float(parts[6])  # AVE.TIME - 7-й элемент
                except (ValueError, IndexError):
                    pass
                break

    # Извлечение значений STORAGE UTIL
    storage_utils = []
    in_storage_section = False
    for line in lines:
        if 'STORAGE' in line and 'CAP.' in line:
            in_storage_section = True
            continue
        if in_storage_section:
            if line.strip() == '' or (not line.startswith(' ') and not line.startswith('\t') and 'BLOCK TYPE' not in line):
                in_storage_section = False
                continue
            if line.strip().startswith('NODE_'):
                # Пример строки: "NODE_1              1    1   0     1        4   1    0.269  0.269    0    0"
                parts = line.split()
                if len(parts) >= 8:
                    try:
                        util = float(parts[7])  # UTIL - 8-й элемент (0-индексация)
                        storage_utils.append(util)
                    except (ValueError, IndexError):
                        pass
    C = sum(storage_utils) / len(storage_utils) if storage_utils else None

    # Извлечение значения E (BUF_LEN_1 STD.DEV.)
    E = None
    in_table_section = False
    for line in lines:
        if 'TABLE' in line and 'MEAN' in line:
            in_table_section = True
            continue
        if in_table_section:
            if line.strip() == '' or (not line.startswith(' ') and not line.startswith('\t') and 'MEAN' not in line and 'STD.DEV.' not in line):
                in_table_section = False
                continue
            if line.strip().startswith('BUF_LEN_1'):
                # Пример строки: "BUF_LEN_1         5.546    6.789"
                parts = line.split()
                if len(parts) >= 3:
                    try:
                        E = float(parts[2])  # STD.DEV. - 3-й элемент (0-индексация)
                    except (ValueError, IndexError):
                        pass
                break

    return {
        'Потери': A,
        'Длина очер.': B,
        'Загрузка': C,
        'Ср.вр. ож.': D,
        'СКО вр.ож.': E
    }


def build_form2_table_from_reports(folder_path: str):
    """
    Собирает таблицу Формы 2 из всех .txt файлов в папке, используя внешнюю функцию f для парсинга.
    """
    data_rows = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f_obj:
                    report_text = f_obj.read()
            except UnicodeDecodeError:
                # Если UTF-8 не сработал, пробуем cp1251
                with open(filepath, 'r', encoding='cp1251') as f_obj:
                    report_text = f_obj.read()

            N_str = filename[:-4] # Убираем ".txt"
            try:
                N = int(N_str)
            except ValueError:
                print(f"Предупреждение: Не удалось распознать N из имени файла '{filename}'. Пропускаю.")
                continue

            parsed_data = f(report_text)
            row = {"Заявок": N, **parsed_data}
            data_rows.append(row)

    # Сортировка по N (Заявок)
    data_rows.sort(key=lambda x: x["Заявок"])

    # Вычисление производных столбцов (после сортировки)
    for i, row in enumerate(data_rows):
        N = row["Заявок"]
        lost = row["Потери"]
        
        # Вер-ть потери и П(%)
        loss_prob = (lost / N) * 100
        row["Вер-ть потери"] = round(loss_prob, 2)
        if i == 0 or data_rows[i-1]["Вер-ть потери"] == 0.0:
            row["П(%)"] = '-'
        else:
            row["П(%)"] = round(abs(loss_prob / data_rows[i-1]["Вер-ть потери"]), 2)

        # О(%) - относительное изменение Ср.вр. ож. по сравнению с предыдущим
        current_wait = row["Ср.вр. ож."]
        if i == 0 or data_rows[i-1]["Ср.вр. ож."] == 0.0:
            row["О(%)"] = '-' # Для первой строки нет предыдущего
        else:
            prev_wait = data_rows[i-1]["Ср.вр. ож."]
            if prev_wait is not None and prev_wait != 0:
                row["О(%)"] = round(abs((current_wait - prev_wait) / prev_wait) * 100, 2)
            else:
                row["О(%)"] = None

        # Дов. инт. и Д(%) - требуют отдельных расчетов, оставим пока None
        dov_int = 2.576*row["СКО вр.ож."]/((N)**0.5)
        row["Дов. инт."] = round(dov_int, 3)
        if row['Ср.вр. ож.'] == 0.0:
            row["Д(%)"] = '-'
        else:
            row["Д(%)"] = round(dov_int / row['Ср.вр. ож.']*100, 2)

    # Возвращаем отсортированные строки
    return data_rows

def main():
    folder_path = sys.argv[1]
    
    form2_table = build_form2_table_from_reports(folder_path)
    
    for row in form2_table:
        print(f'[{row["Заявок"]}], [{row["Потери"]}], [{row["Вер-ть потери"]}%], [{row["П(%)"]}%], [{row["Длина очер."]:.3f}], [{row["Загрузка"]:.3f}], [{row["Ср.вр. ож."]:.3f}], [{row["О(%)"]}%], [{row["СКО вр.ож."]:.3f}], [{row["Дов. инт."]}], [{row["Д(%)"]}%],')

if __name__ == "__main__":
    main()