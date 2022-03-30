# -*- coding: utf-8 -*-
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


# zakodowane na sztywno dziala tylko dla 4 bitów parzystości
def printZakodowanySlownik(slowa):
    counter = 0
    iloscBitowParzystosci = len(slowa[0]) - 8
    for slowo in slowa:
        if iloscBitowParzystosci == 4:
            print("%3d: [%d, %d, %d, %d, %d, %d, %d, %d,  %d, %d, %d, %d]" % (
                counter, slowo[0], slowo[1], slowo[2], slowo[3], slowo[4], slowo[5], slowo[6], slowo[7], slowo[8],
                slowo[9],
                slowo[10], slowo[11]))

        counter += 1


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