from random import random

def randsquare(A, B):
    M = [0, 0]
    M[0] = (A[0] + B[0]) / 2
    M[1] = (A[1] + B[1]) / 2

    R = []
    if A[0] > B[0]:
        R = A
    else:
        R = B

    C = [0, 0]
    C[0] = M[0] - R[1] + M[1]
    C[1] = M[1] + R[0] - M[0]

    D = [0, 0]
    D[0] = M[0] + R[1] - M[1]
    D[1] = M[1] - R[0] + M[0]

    r1 = random()
    r2 = random()


    Q = [D[0] - A[0], C[0] - A[0]]
    N = [D[1] - A[1], C[1] - A[1]]

    return [Q[0] * r1 + Q[1] * r2 + A[0], N[0] * r1 + N[1] * r2 + A[1]]