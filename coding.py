import filesOperations as fo
import copy
import numpy as np


def encodeSingleWord(word, H):
    parityBitCount = len(H[0]) - 8
    encodedWord = copy.deepcopy(word)
    parityBits = [0] * parityBitCount  # inicjacja listy zerami
    for i in range(8):
        for j in range(parityBitCount):
            parityBits[j] += word[i] * H[j][i] #kazdy z 8 bitow wiadom musi miec operacje z bitow parzystosci

    for pb in parityBits:
        encodedWord.append(pb % 2)

    return encodedWord


def isWordEncodedCorrectly(word, H): #czy iloczyn jest zerem wg instrukcji
    iloczyn = np.matmul(H, word) % 2
    result = True
    for bit in iloczyn:
        if bit == 1:
            result = False
            break

    return result


def singleIncorrectBitIndex(slowo, H):
    result = -1
    colInHE = np.matmul(H, slowo) % 2
    columnCount = len(H[0])
    for i in range(columnCount):
        # H[:,i] zwraca i-ta kolumne macierzy H
        # any() zwraca falsz jesli wszystkie elementy macierzy sa 0
        if not any(colInHE - H[:, i]):        #zwroci index gdzie kolumny w slowie i H beda takie same
            result = i
            break

    return result


def doubleIncorrectBitsIndexes(slowo, H):
    result = [-1, -1]
    matrixHE = np.dot(H, slowo) % 2
    columnCount = len(H[0])
    for col1Index in range(columnCount):
        for col2Index in range(columnCount):
            if col1Index == col2Index:
                continue

            sum = copy.deepcopy(H[:, col1Index]) + copy.deepcopy(H[:, col2Index])
            sum = sum % 2
            if np.array_equal(sum, matrixHE):
                result = [col1Index, col2Index]
                break

    return result


def correctionOfSingleBitInWord(word, H):
    incorrectBitIndex = singleIncorrectBitIndex(word, H)
    result = copy.deepcopy(word)
    result[incorrectBitIndex] = (result[incorrectBitIndex] + 1) % 2
    return result

def correctionOfDoubleBitsInWord(word, H):
    incorrectBitsIndexes = doubleIncorrectBitsIndexes(word, H)
    result = copy.deepcopy(word)
    result[incorrectBitsIndexes[0]] = (result[incorrectBitsIndexes[0]] + 1) % 2
    result[incorrectBitsIndexes[1]] = (result[incorrectBitsIndexes[1]] + 1) % 2
    return result


def decodeWord(word, H, areThereTwoErrors):
    if isWordEncodedCorrectly(word, H):
        result = copy.deepcopy(word)
    else:
        if areThereTwoErrors:
            result = correctionOfDoubleBitsInWord(word, H)
        if not areThereTwoErrors:
            result = correctionOfSingleBitInWord(word, H)
    result = result[0: 8]
    return result


def encodeToString(binaryContent, H):
    output = ""
    while binaryContent:
        wordArr = encodeSingleWord(binaryContent.pop(0), H)
        wordStr = ''.join([str(elem) for elem in wordArr])
        output += wordStr

    return output


def encodeFile(matrix, encodedFileName, inputFileName):
    content = open(inputFileName, 'r').read()
    print(content)
    contentBinary = fo.stringToByteArray(content)
    encoded = encodeToString(contentBinary, matrix)
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

    decoded = []
    while encodedArray:
        encodedWord = decodeWord(encodedArray.pop(0), matrix, areThereTwoErrors)
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