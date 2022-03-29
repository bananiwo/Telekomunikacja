from matrixGenerator import createMatrix
import fileOperations as fo
import decoding as d
import numpy as np


def encodeFile(matrix):
    content = open('input.txt', 'r').read()
    print(content)
    contentBinary = fo.stringToByteArray(content)
    encoded = d.encodeToString(contentBinary, matrix)
    fo.saveStringToFile("encoded", encoded)


def decodeToFile(matrix):
    encodedWordLen = len(matrix) + 8
    encodedString = fo.loadStringFromFile("encoded")
    wordCount = int(len(encodedString)/encodedWordLen)

    encodedArray = []
    for i in range(wordCount):
        wordStr = encodedString[(encodedWordLen * i): ((i + 1) * encodedWordLen): 1]
        wordArray = []
        for j in range(encodedWordLen):
            wordArray.append(int(wordStr[j]))
        encodedArray.append(wordArray)

    decoded = []
    while encodedArray:
        encodedWord = d.dekodujSlowo(encodedArray.pop(0), matrix)
        decoded.append(encodedWord)

    decodedBytesString = ""
    while decoded:
        word = decoded.pop(0)
        wordStr = ""
        for char in word:
            wordStr += str(char)
        decodedBytesString += wordStr
    output = ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(decodedBytesString)]*8))
    fo.saveStringToFile("output", output)


# ----------------- PROBLEM JEDNEGO BLEDNEGO BITU -----------------

matrix = createMatrix(4, False)
# print(matrix)
# matrix = np.asarray([[1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
#                      [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
#                      [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
#                      [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1]])
#
#
# encodeFile(matrix)
# decodeToFile(matrix)

# ----------------- PROBLEM DWOCH BLEDNYCH BITOW -----------------

# matrixTwoBadBits = createMatrix(4, True)
# matrixTwoBadBits = np.asarray([[0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
#                                [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0],
#                                [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
#                                [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1]])
# print(matrixTwoBadBits)
# textStr = "hello"
# print(textStr)
# textBit = fo.stringToByteArray(textStr)
# print(textBit)
# textEncoded = d.zakodujSlowo(textBit, matrixTwoBadBits)
