import copy

import numpy
import numpy as np
# 1) kolumny nie moga byc takie same
# 2) suma kolumn nie moze dac kolumny macierzy (tylko do 2 bledow)
# 3) kolumna nie moze byc kolna zerowa

def shuffleMatrix(matrix):
    np.random.shuffle(matrix)
    return matrix


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
                if numpy.array_equal(sumOfTwoCols, matrix[:,k]):
                    return False
    return True


def createMatrix(parityBitCount, shouldCorrectTwoBitErrors):
    matrix = np.zeros((parityBitCount, 8+parityBitCount), dtype=int)
    # identityMatrix = np.identity(parityBitCount, dtype=int)
    # matrix = np.hstack((zeros, identityMatrix))
    for i in range(50000):
        for row in range(parityBitCount):
            # for col in range(8):
            for col in range(8+parityBitCount):
                matrix[row][col] = np.random.randint(0, 2)

        a = isEachColumnDifferent(matrix)
        b = isEveryColumnNotZero(matrix)
        # if shouldCorrectTwoBitErrors:
        # c = ifTwoColsSumNotGiveColInMatrix(matrix)
        # else:
        #     c = True
        c = sumOfColsNotGiveCol(matrix) if shouldCorrectTwoBitErrors else True
        # c = not c
        if a and b and c:
            return matrix

    return np.zeros((parityBitCount, 8 + parityBitCount), dtype=int)
