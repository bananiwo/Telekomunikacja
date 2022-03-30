import filesOperations as fo
import copy
import numpy as np


def zakodujSlowo(slowo, H):
    iloscBitowParzystosci = len(H[0]) - 8
    zakodowaneSlowo = copy.deepcopy(slowo)
    bityParzystosci = [0] * iloscBitowParzystosci  # inicjacja listy zerami
    for i in range(8):
        for j in range(iloscBitowParzystosci):
            bityParzystosci[j] += slowo[i] * H[j][i] #kazdy z 8 bitow wiadom musi miec operacje z bitow parzystosci

    for bp in bityParzystosci:
        zakodowaneSlowo.append(bp % 2)

    return zakodowaneSlowo


def czySlowoZakodowanePoprawnie(slowo, H): #czy iloczyn jest zerem wg instrukcji
    iloczyn = np.matmul(H, slowo) % 2
    wynik = True
    for bit in iloczyn:
        if bit == 1:
            wynik = False
            break

    return wynik


def numerPojedynczejBlednejKolumny(slowo, H):
    wynik = -1
    colInHE = np.matmul(H, slowo) % 2
    iloscKolumn = len(H[0])
    for i in range(iloscKolumn):
        # H[:,i] zwraca i-ta kolumne macierzy H
        # any() zwraca falsz jesli wszystkie elementy macierzy sa 0
        if not any(colInHE - H[:, i]):        #zwroci index gdzie kolumny w slowie i H beda takie same
            wynik = i
            break

    return wynik


def numerPodwojnejBlednejKolumny(slowo, H):
    wynik = [-1, -1]
    macierzHE = np.dot(H, slowo) % 2
    print("he")
    print(macierzHE)
    iloscKolumn = len(H[0])
    for col1Index in range(iloscKolumn):
        for col2Index in range(iloscKolumn):
            if col1Index == col2Index:
                continue

            sum = copy.deepcopy(H[:, col1Index]) + copy.deepcopy(H[:, col2Index])
            sum = sum % 2
            if np.array_equal(sum, macierzHE):
                print('col1')
                print(H[:, col1Index])
                print('col2')
                print(H[:, col2Index])
                wynik = [col1Index, col2Index]
                print(wynik)
                break

    return wynik


def korekcjaPojedynczegoBledu(slowo, H):
    pozycjaZlegoBitu = numerPojedynczejBlednejKolumny(slowo, H)
    wynik = copy.deepcopy(slowo)
    wynik[pozycjaZlegoBitu] = (wynik[pozycjaZlegoBitu] + 1) % 2
    return wynik

def korekcjaPodwojnegoBledu(slowo, H):
    pozycjeZlychBitow = numerPodwojnejBlednejKolumny(slowo, H)
    wynik = copy.deepcopy(slowo)
    wynik[pozycjeZlychBitow[0]] = (wynik[pozycjeZlychBitow[0]] + 1) % 2
    wynik[pozycjeZlychBitow[1]] = (wynik[pozycjeZlychBitow[1]] + 1) % 2
    return wynik


def dekodujSlowo(slowo, H, areThereTwoErrors):
    if czySlowoZakodowanePoprawnie(slowo, H):
        w = copy.deepcopy(slowo)
    else:
        if areThereTwoErrors:
            w = korekcjaPodwojnegoBledu(slowo, H)
        if not areThereTwoErrors:
            w = korekcjaPojedynczegoBledu(slowo, H)
    w = w[0: 8]
    return w


def encodeToString(binaryContent, H):
    output = ""
    while binaryContent:
        wordArr = zakodujSlowo(binaryContent.pop(0), H)
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
        encodedWord = dekodujSlowo(encodedArray.pop(0), matrix, areThereTwoErrors)
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