import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A[1, :])
print(A[:, 1])
B = A[:, ::-1]
print(B)

# [start:stop:step]
# По умолчанию
# start = 0
# stop = len
# step = 1