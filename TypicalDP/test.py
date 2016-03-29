# coding: utf-8

import numpy as np

vector = np.array([1,2,3])

matrix1 = np.eye(3)
matrix2 = 2*np.eye(3)
matrix3 = 3*np.eye(3)
matrix = np.array([matrix1, matrix2, matrix3])
for i in matrix:
    vector = i.dot(vector)
    print(vector)




