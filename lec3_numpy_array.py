import numpy as np
A = np.zeros((2, 3))
print(A)
A[0, 2] = 5
print(A)

B = np.ones((4, 2))
print(B)

A = np.ndarray(shape=(2, 3))
print(A)

A = np.arange(0, 5, 0.5)
print(A)

print(A[-1])

print(len(A))