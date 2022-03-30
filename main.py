import fileOperations
from matrixGenerator import createMatrix
import fileOperations as fo
import decoding as d
import numpy as np


def encodeFile(matrix, encodedFileName, inputFileName):
    content = open(inputFileName, 'r').read()
    print(content)
    contentBinary = fo.stringToByteArray(content)
    encoded = d.encodeToString(contentBinary, matrix)
    fo.saveStringToFile(encodedFileName, encoded)


def decodeToFile(matrix, encodedFileName, outputFileName, areThereTwoErrors):
    encodedWordLen = len(matrix) + 8 # wys = ilosc bitow parzystosci - dlugosc slowa kodowego
    encodedString = fo.loadStringFromFile(encodedFileName)
    wordCount = int(len(encodedString)/encodedWordLen)  #ilosc slow

    encodedArray = []
    for i in range(wordCount):
        wordStr = encodedString[(encodedWordLen * i): ((i + 1) * encodedWordLen): 1] #wydzielinie slow jako tablica
        wordArray = []
        for j in range(encodedWordLen):
            wordArray.append(int(wordStr[j])) #string cast to int
        encodedArray.append(wordArray)
#zakodowe inty w tablicy

    decoded = []
    while encodedArray:
        encodedWord = d.dekodujSlowo(encodedArray.pop(0), matrix, areThereTwoErrors)
        decoded.append(encodedWord)

    decodedBytesString = ""
    while decoded:
        word = decoded.pop(0)
        wordStr = ""
        for char in word:
            wordStr += str(char)
        decodedBytesString += wordStr
    output = ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(decodedBytesString)]*8))
    fo.saveStringToFile(outputFileName, output)


# ----------------- PROBLEM JEDNEGO BLEDNEGO BITU -----------------

# matrix = createMatrix(4, False)
# print(matrix)
# matrix = np.asarray([[1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
#                      [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
#                      [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
#                      [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1]])


# encodeFile(matrix, 'encoded', 'input.txt')
# decodeToFile(matrix, 'encoded', 'output.txt', False)



# ----------------- PROBLEM DWOCH BLEDNYCH BITOW -----------------

# matrixTwoBadBits = createMatrix(6, True)
matrixTwoBadBits = np.asarray([[0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                               [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1],
                               [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1],
                               [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                               [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
                               [0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]])
print(matrixTwoBadBits)
# textStr = "hello"
# print(textStr)
# textBit = fo.stringToByteArray(textStr)
# print(textBit)
# textEncoded = []
# while textBit:
#     textEncoded.append(d.zakodujSlowo(textBit.pop(0), matrixTwoBadBits))
# print(textEncoded)
# encodeFile(matrixTwoBadBits, 'encodedTwoErrors', 'inputTwoErrors.txt')
#
decodeToFile(matrixTwoBadBits, 'encodedTwoErrors', 'outputTwoErrors.txt', True)




