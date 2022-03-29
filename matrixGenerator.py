import copy
import numpy as np


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


def initMatrixWithUnitPart(k, w, z):
    zeroCounter = 0
    unitMatrix = np.identity(w)
    matrix = np.ones((w, k))
    for col in range(k):
        for row in range(w):
            if zeroCounter < z:
                matrix[row, col] = 0
                zeroCounter += 1
    np.random.shuffle(matrix)
    matrix[0:w, k - w:k] = unitMatrix
    return matrix


def shuffleMatrix(matrix):
    np.random.shuffle(matrix)
    return matrix


def isEachColumnDifferent(matrix):
    isDifferent = True
    numOfColumns = len(matrix[0])
    for i in range(numOfColumns):
        for j in range(numOfColumns):
            if i == j:
                continue
            if np.array_equal(matrix[:, i], matrix[:, j]):
                isDifferent = False
                return isDifferent

    return isDifferent


def isEveryColumnNotZero(matrix):
    isNotZero = True
    numOfColumns = len(matrix[0])
    numOfRows = len(matrix)
    zeros = np.asarray([0] * numOfRows)
    for i in range(numOfColumns):
        if np.array_equal(matrix[:, i], zeros):
            isNotZero = False
            break

    return isNotZero


def ifTwoColsSumNotGiveColInMatrix(matrix):
    k = len(matrix)
    w = len(matrix[0])
    statement = True
    for i in range(k):
        for j in range(k):
            if j == i:
                continue
            sumArray = np.empty((w, 1))
            for row in range(w):
                sumArray = copy.deepcopy(matrix[:, i]) + matrix[:, j]
            for m in range(k):
                statement = not np.array_equal(matrix[:, m], sumArray)
                if not statement:
                    return statement
    return statement


def createMatrix(parityBitCount, shouldCorrectTwoBitErrors):
    matrix = np.zeros((parityBitCount, 8), dtype=int)
    identityMatrix = np.identity(parityBitCount, dtype=int)
    matrix = np.hstack((matrix, identityMatrix))
    for i in range(5000):
        for row in range(parityBitCount):
            for col in range(8):
                matrix[row][col] = np.random.randint(0, 2)

        a = isEachColumnDifferent(matrix)
        b = isEveryColumnNotZero(matrix)
        c = ifTwoColsSumNotGiveColInMatrix(matrix) if shouldCorrectTwoBitErrors else True
        if a and b and c:
            return matrix

    return np.zeros((parityBitCount, 8 + parityBitCount), dtype=int)
