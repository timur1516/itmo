import copy


def transform_to_triangle_matrix(matrix):
    n = min(len(matrix), len(matrix[0]))
    l = 0
    while l < n:
        if matrix[l][l] == 0:
            for i in range(l + 1, n):
                if matrix[i][l] != 0:
                    matrix[i], matrix[l] = matrix[l], matrix[i]
                    break
        for i in range(l + 1, n):
            k = matrix[i][l] / matrix[l][l]
            for j in range(l, n):
                matrix[i][j] -= matrix[l][j] * k
        l += 1


def calculate_det(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        print("Матрица должна быть квадратной!")
        exit(1)
    tmp = copy.deepcopy(matrix)
    transform_to_triangle_matrix(tmp)
    det = 1
    for i in range(n):
        det *= tmp[i][i]
    return det


def rang(matrix):
    tmp = copy.deepcopy(matrix)
    transform_to_triangle_matrix(tmp)
    return sum(any(c != 0 for c in r) for r in tmp)


def gauss_with_main_col_dir(a, b):
    n = len(a)
    for i in range(n):
        # --------------------------------------------
        l = i
        for m in range(i + 1, n):
            if abs(a[m][i] > abs(a[l][i])):
                l = m
        # ----------------------
        if l != i:
            for j in range(i, n):
                a[i][j], a[l][j] = a[l][j], a[i][j]
            b[i], b[l] = b[l], b[i]
        # --------------------------------------------
        for k in range(i + 1, n):
            c = a[k][i] / a[i][i]
            a[k][i] = 0
            for j in range(i + 1, n):
                a[k][j] = a[k][j] - a[i][j] * c
            b[k] = b[k] - b[i] * c


def gauss_with_main_col_inv(a, b):
    n = len(a)
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s = s + a[i][j] * x[j]
        x[i] = (b[i] - s) / a[i][i]
    return x


def concatenate_matrix_and_column(matrix, column):
    return [row + [column[i]] for i, row in enumerate(matrix)]


def solve_equation(a, b):
    n = len(a)
    ext_matrx = concatenate_matrix_and_column(a, b)

    matrix_rang = rang(a)
    ext_matrx_rang = rang(ext_matrx)

    if matrix_rang != ext_matrx_rang:
        print("СЛАУ несовместна!")
        exit(1)
    if matrix_rang < n:
        print("СЛАУ имеет бесконечно много решений")

    gauss_with_main_col_dir(a, b)

    tmp_triangle_matrix = concatenate_matrix_and_column(a, b)
    print("Треугольная матрица:")
    print_matrix(tmp_triangle_matrix)

    x = gauss_with_main_col_inv(a, b)
    return x


def calculate_r(a, b, x):
    n = len(a)
    r = [0 for _ in range(n)]
    for i in range(n):
        s = 0
        for j in range(n):
            s = s + a[i][j] * x[j]
        r[i] = s - b[i]
    return r


def read_n():
    try:
        n = int(input("Введите n: "))
    except:
        print("n должно быть числом!")
        exit(1)
    if n < 1 or n > 20:
        print("Размер матрицы должен быть от 1 до 20 включительно!")
        exit(1)
    return n


def read_matrix(n):
    matrix = []
    print("Введите матрицу построчно (и A и B):")
    for _ in range(n):
        try:
            row = list(map(int, input().split()))
        except:
            print("Элементы матрицы должны быть числами!")
            exit(1)
        if len(row) != n + 1:
            print("В каждой строке матрицы должно быть n+1 элементов!")
            exit(1)
        matrix.append(row)
    return matrix


def split_matrix(matrix):
    a = [row[:-1] for row in matrix]
    b = [row[-1] for row in matrix]
    return a, b


def print_matrix(matrix):
    for r in matrix:
        for c in r:
            print(_round(c, 2), end='\t')
        print()


def print_vector(vector):
    for c in vector:
        print(_round(c, 2), end=' ')
    print()


def _round(n, precision):
    return "{:.{}f}".format(n, precision)


def main():
    n = read_n()
    matrix = read_matrix(n)
    a, b = split_matrix(matrix)
    x = solve_equation(a, b)
    print("Решение системы:")
    print_vector(x)
    r = calculate_r(a, b, x)
    print("Невязка:")
    print_vector(r)


if __name__ == "__main__":
    main()
