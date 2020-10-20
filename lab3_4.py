import numpy as np
N = int(input("Введите высоту: "))
M = int(input("Введите ширину: "))
A = np.ndarray(shape=(N, M))
for i in range(N):
    for j in range(M):
        if i == 1 or j == 1:
            A[i, j] = np.sin(N * i + M * j)
        else:
            A[i, j] = np.sin(N * (i + 1) + M * (j + 1))
        if A[i, j] < 0:
            A[i, j] = 0            
print(A)
