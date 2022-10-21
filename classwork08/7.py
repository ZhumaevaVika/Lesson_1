import numpy as np
np.random.seed(2)
arr = np.random.randint(65, size=64)
# print(array)

matrix = arr.reshape(8, 8)
print(matrix)
matrix = np.delete(matrix, (7), axis=0)
matrix = np.delete(matrix, (0), axis=1)
print(np.linalg.det(matrix))
