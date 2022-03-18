# -*- coding: utf-8 -*-
import copy
import numpy as np


def decToBin(a):
    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]
    while len(x) < 8:
        x += '0'
        bnr = x[::-1]
    return bnr


def zakodujSlownik(slowaMatr, H):
    slowaZakodowaneMatrix = []

    for s in slowaMatr:
        slowaZakodowaneMatrix.append(zakodujSlowo(s, H))

    return slowaZakodowaneMatrix


def zakodujSlowo(slowo, H):
    iloscBitowParzystosci = len(H[0]) - 8
    zakodowaneSlowo = copy.deepcopy(slowo)
    bityParzystosci = [0] * iloscBitowParzystosci  # inicjacja listy zerami
    for i in range(8):
        for j in range(iloscBitowParzystosci):
            bityParzystosci[j] += slowo[i] * H[j][i]

    for bp in bityParzystosci:
        zakodowaneSlowo.append(bp % 2)

    return zakodowaneSlowo


def odleglosc(slowo1, slowo2):
    suma = 0
    for i in range(len(slowo1)):
        suma += abs(slowo1[i] - slowo2[i])
    return suma

# funkcja do debugowania
def rozkladOdleglosci(slowa):
    output = {}

    # stworzenie slownika
    for i in range(len(slowa[0]) + 1):
        output[i] = 0

    # wypelnienie slownika 256*256=65536 elementami
    for i in range(256):
        for j in range(256):
            if i == j:
                continue

            odl = odleglosc(slowa[i], slowa[j])
            output[odl] += 1

    return output


def minimalnaOdleglosc(slowa):
    minOdleglosc = 8

    for i in range(256):
        for j in range(256):
            if i == j:
                continue
            odl = odleglosc(slowa[i], slowa[j])
            if odl < minOdleglosc:
                minOdleglosc = odl

    return minOdleglosc


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


def czySlowoZakodowanePoprawnie(slowo, H):
    iloczyn = np.matmul(H, slowo) % 2
    wynik = True
    for bit in iloczyn:
        if bit == 1:
            wynik = False
            break

    return wynik


def numerBlednejKolumny(slowo, H):
    wynik = -1
    macierzHE = np.matmul(H, slowo) % 2
    iloscKolumn = len(H[0])
    for i in range(iloscKolumn):
        # H[:,i] zwraca i-ta kolumne macierzy H
        # any() zwraca falsz jesli wszystkie elementy macierzy sa 0
        if not any(macierzHE - H[:, i]):
            wynik = i
            break

    return wynik


def korekcjaPojedynczegoBledu(slowo, H):
    pozycjaZlegoBitu = numerBlednejKolumny(slowo, H)
    wynik = copy.deepcopy(slowo)
    wynik[pozycjaZlegoBitu] = (wynik[pozycjaZlegoBitu] + 1) % 2
    return wynik


def dekodujSlowo(slowo, H):
    if czySlowoZakodowanePoprawnie(slowo, H):
        w = copy.deepcopy(slowo)
    else:
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