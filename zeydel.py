import numpy as np


A = [
    [0.87, -0.24, 7.03],
    [5.02, 2.76, -0.04],
    [-0.01, 7.02, -0.51]
]

B = [
    -3.06,
    1.35,
    -0.75
]


def nevyazka(A, B, X):
    r = np.dot(A, X) - B
    R = 0
    for i in range(len(r)):
        R += r[i] ** 2
    R = np.sqrt(R)
    return R


def zeydel(A, B, eps):
    n = len(A)
    X = [0] * n
    while nevyazka(A, B, X) > eps:
        for i in range(n):
            sum1 = 0
            for j in range(i):
                sum1 += A[i][j] / A[i][i] * X[j]
            sum2 = 0
            for j in range(i + 1, n):
                sum2 += A[i][j] / A[i][i] * X[j]
            X[i] = B[i] / A[i][i] - sum1 - sum2
    print("Метод Зейделя.")
    print("X:", X)
    print("epsilon =", eps)
    print("Невязка: r = ", nevyazka(A, B, X))


zeydel(A, B, 0.001)
