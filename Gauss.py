import numpy as np

A = [[1, 9, 0, 0, 41],
     [-4, -3, 0, 0, 1],
     [0, -5, -7, -5, -51],
     [0, 0, -4, 1, -11]]


x = np.zeros((4, 1))


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("%2.4f" % (matrix[i][j]), end=' ')
        print()


def matrix_max_row(matrix, n):
    max_element = matrix[n][n]
    max_row = n
    for i in range(n + 1, len(matrix)):
        if abs(matrix[n][i]) > abs(max_element):
            max_element = matrix[n][i]
            max_row = i
        if max_row != n:
            matrix[n], matrix[max_row] = matrix[max_row], matrix[n]


def Gauss(matrix):
    n = len(matrix)
    for k in range(n - 1):
        matrix_max_row(matrix, k)
        for i in range(k + 1, n):
            div = matrix[i][k] / matrix[k][k]
            matrix[i][-1] -= div * matrix[k][-1]
            for j in range(k, n):
                matrix[i][j] -= div * matrix[k][j]
    if is_singular(matrix):
        print('Система имеет бесконечное число решений')
        return
    # Обратный ход
    for k in range(n - 1, -1, -1):
        x[k] = (matrix[k][-1] - sum([matrix[k][j] * x[j] for j in range(k + 1, n)])) / matrix[k][k]
    return x


def Gauss_print(x):
    print("Решение методом Гауса: ")
    for k in range(len(x)):
        print('x[', k + 1, '] =', "%2.5f" % (x[k]), end='\n')
    return x


def is_singular(matrix):
    for i in range(len(matrix)):
        if not matrix[i][i]:
            return True
        return False


def nevyazka():
    temp = np.zeros((4, 1))
    r = np.zeros((4, 1))
    print('Вектор невязки:')
    for i in range(len(A)):
        temp[i] = 0
        for j in range(len(A)):
            temp[i] += x[j] * A[i][j]
        r[i] = temp[i] - A[i][len(A[0]) - 1]
        print('r[', i + 1, '] =', "%.12f" % (r[i]), end='\n')


print_matrix(A)
Gauss(A)
Gauss_print(x)
print('')
nevyazka()
print('')
