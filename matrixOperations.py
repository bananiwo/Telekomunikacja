import numpy as np
import copy


def isEachColumnDifferent(matrix):  # zwraca wartość logiczną true jesli w każda kolumna macierzy jest unikalna
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


def isEveryColumnNotZero(matrix): # zwraca wartość logiczną true jesli w macierzy żadna kolumna nie jest kolumną zerową
    isNotZero = True
    numOfColumns = len(matrix[0])
    numOfRows = len(matrix)
    zeros = np.asarray([0] * numOfRows)
    for i in range(numOfColumns):
        if np.array_equal(matrix[:, i], zeros):
            isNotZero = False
            break

    return isNotZero



def sumOfColsNotGiveCol(matrix):
    colNum = len(matrix[0])
    for i in range(colNum):
        for j in range(colNum):
            matrix = copy.deepcopy(matrix)
            sumOfTwoCols = (matrix[:, i] + matrix[:, j]) % 2
            for k in range(colNum):
                if np.array_equal(sumOfTwoCols, matrix[:,k]):
                    return False
    return True


def createMatrix(parityBitCount, shouldCorrectTwoBitErrors):
    matrix = np.zeros((parityBitCount, 8+parityBitCount), dtype=int)
    for i in range(50000):
        for row in range(parityBitCount):
            for col in range(8+parityBitCount):
                matrix[row][col] = np.random.randint(0, 2)

        a = isEachColumnDifferent(matrix)
        b = isEveryColumnNotZero(matrix)
        c = sumOfColsNotGiveCol(matrix) if shouldCorrectTwoBitErrors else True

        if a and b and c:
            return matrix

    return np.zeros((parityBitCount, 8 + parityBitCount), dtype=int)