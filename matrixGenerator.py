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
    matrix = np.ones((k, w))
    for col in range(k):
        for row in range(w):
            if zeroCounter < z:
                matrix[col, row] = 0
                zeroCounter += 1
    np.random.shuffle(matrix)
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

k = 4
w = 4
z = 4
m = initMatrix(k, w, z)
loopCounter = 0

def ifTwoColsSumGiveColInMatrix(matrix, k, w):
    statement = False
    for i in range(k):
        for j in range(i + 1, k):
            for m in range(j + 1, k):
                sumArray = np.empty((w, 1))
                for row in range(w):
                    sumArray[row] = (matrix[row, i] + matrix[row, j]) % 2
                print(sumArray)
                if not np.array_equal(sumArray, matrix[:, m]):
                    statement = True
                    return statement
    return statement



H = np.asarray([[0, 1, 1, 1, 0, 1, 1, 0,   1, 0, 0, 0],
                [1, 0, 1, 1, 0, 0, 1, 1,   0, 1, 0, 0],
                [1, 1, 0, 1, 1, 0, 0, 1,   0, 0, 1, 0],
                [1, 1, 1, 0, 1, 1, 0, 0,   0, 0, 0, 1]])

#print(notSameColToCol(H, H.shape[1]))
print(ifTwoColsSumGiveColInMatrix(H,H.shape[1],H.shape[0]))

H2 = np.asarray([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])
print(ifTwoColsSumGiveColInMatrix(H2,H2.shape[1],H2.shape[0]))