from matrixGenerator import createZad2Matrix
import fileOperations as fo
import decoding as d
import numpy as np

# ------------------ ZAKODOWANIE TEKSTU, PODPUNKT 3 ------------------

# matrix = createZad2Matrix(4, False)
matrix = np.asarray([[1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0],
                     [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
                     [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1]])



def encodeFile(matrix):
    content = open('input.txt', 'r').read()
    print(content)
    contentBinary = fo.stringToByteArray(content)
    encoded = d.encodeToString(contentBinary, matrix)
    fo.saveStringToFile("encoded", encoded)

# ------------------ ODKODOWANIE TEKSTU, PODPUNKT 3 ------------------


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
    # print(output)

# encodeFile(matrix)
decodeToFile(matrix)
