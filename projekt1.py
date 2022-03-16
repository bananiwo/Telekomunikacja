# -*- coding: utf-8 -*-
import copy

def decToBin(a):
    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]  # this reverses an array
    while len(x) < 8:
        x += '0'
        bnr = x[::-1]
    return bnr


def zakodujSlowa(slowaMatr, H):
    iloscBitowParzystosci = len(H[0]) - 8
    slowaZakodowaneMatrix = copy.deepcopy(slowaMatr)

    for s in slowaZakodowaneMatrix:
        bityParzystosci = [0] * iloscBitowParzystosci  # inicjacja listy zerami
        for i in range(8):

            for j in range(iloscBitowParzystosci):
                bityParzystosci[j] += s[i] * H[j][i]

        for bp in bityParzystosci:
            s.append(bp % 2)
    return slowaZakodowaneMatrix


def odleglosc(slowo1, slowo2):
    suma = 0
    for i in range(len(slowo1)):
        suma += abs(slowo1[i] - slowo2[i])
    return suma


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
def printSlowaZakodowane(slowa):
    counter = 0
    iloscBitowParzystosci = len(slowa[0]) - 8
    for slowo in slowa:
        if iloscBitowParzystosci == 4:
            print("%3d: [%d, %d, %d, %d, %d, %d, %d, %d,  %d, %d, %d, %d]" % (
            counter, slowo[0], slowo[1], slowo[2], slowo[3], slowo[4], slowo[5], slowo[6], slowo[7], slowo[8], slowo[9],
            slowo[10], slowo[11]))
        if iloscBitowParzystosci == 3:
            print("%3d: [%d, %d, %d, %d, %d, %d, %d, %d,  %d, %d, %d]" % (
            counter, slowo[0], slowo[1], slowo[2], slowo[3], slowo[4], slowo[5], slowo[6], slowo[7], slowo[8], slowo[9],
            slowo[10]))

        counter += 1


# 256 kolejnych liczb dziesiatkowo
slowaDec = []
for i in range(256):
    slowaDec.append(i)

# 256 kolejnych liczb binarnie
slowaBin = []
for i in range(256):
    slowaBin.append(decToBin(slowaDec[i]))

# array 256 slow, kazde jest arrayem bitow
slowaMatrix = []
for k in range(256):
    s = []
    for i in range(8):
        s.append(int(slowaBin[k][i]))
    slowaMatrix.append(s)

H = ([[1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
      [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
      [0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1]])

# H = ([[0, 1, 1, 1, 0, 1, 1, 0,    1, 0, 0, 0],
#       [1, 0, 1, 1, 0, 0, 1, 1,    0, 1, 0, 0],
#       [1, 1, 0, 1, 1, 0, 0, 1,    0, 0, 1, 0],
#       [1, 1, 1, 0, 1, 1, 0, 0,    0, 0, 0, 1]])


slowaZakodowane = zakodujSlowa(slowaMatrix, H)
minOdleglosc = minimalnaOdleglosc(slowaZakodowane)

printSlowaZakodowane(slowaZakodowane)
print("Ilosc bitow parzystosci: %d" % (len(H[0]) - 8))
print("Minimalna odleglosc: %d" % minOdleglosc)
print("Rozkład odległosci zakodowanych słów w formacie (odleglość: liczba wystąpień)")
print(rozkladOdleglosci(slowaZakodowane))
