import copy

import numpy as np

# k - ilosc wierszy w macierzy
k = 8

# w - ilosc wierszy w macierzy
w = 9

# z - ilosc zer w macierzy
z = 3

matrix = np.ones((k, w))


def initMatrix(k, w, z):
    zeroCounter = 0
    matrix = np.ones((w, k))
    for col in range(k):
        for row in range(w):
            if zeroCounter < z:
                matrix[row, col] = 0
                zeroCounter += 1
    np.random.shuffle(matrix)
    return matrix

def initMatrixWithUnitPart(k, w, z) :
    zeroCounter = 0
    unitMatrix = np.identity(w)
    matrix = np.ones((w, k))
    for col in range(k):
        for row in range(w):
            if zeroCounter < z:
                matrix[row, col] = 0
                zeroCounter += 1
    np.random.shuffle(matrix)
    matrix[0:w, k-w:k] = unitMatrix
    return matrix

def shuffleMatrix(matrix):
    np.random.shuffle(matrix)
    return matrix

def notSameColToCol(matrix, k):
    same = True
    for i in range(k):
        for j in range(i + 1, k):
            if np.array_equal(matrix[:, i], matrix[:, j]):
                same = False
                return same
    return same

def ifTwoColsSumNotGiveColInMatrix(matrix, k, w):
    statement = True
    for i in range(k):
        for j in range(k):
            if j == i:
                continue
            sumArray = np.empty((w, 1))
            for row in range(w):
                sumArray = copy.deepcopy(matrix[:, i]) + matrix[:,j]
            for m in range(k):
                statement = not np.array_equal(matrix[:, m], sumArray)
                if not statement:
                    return statement
    return statement

H = np.asarray([[0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0],
                [1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1]])

# print(notSameColToCol(H, H.shape[1]))
# print(ifTwoColsSumNotGiveColInMatrix(H, H.shape[1], H.shape[0]))

H2 = np.asarray([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])

H3 = np.asarray([[1, 0, 1, 0],
                 [0, 1, 1, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 1]])
#print(H3[:, 1])

# print(ifTwoColsSumNotGiveColInMatrix(H2, H2.shape[1], H2.shape[0]))
#print(ifTwoColsSumNotGiveColInMatrix(H3, H3.shape[1], H3.shape[0]))