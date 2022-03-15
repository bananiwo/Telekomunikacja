# -*- coding: utf-8 -*-
import copy

import numpy as np;

def decToBin(a):
    bnr = bin(a).replace('0b','')
    x = bnr[::-1] #this reverses an array
    while len(x) < 8:
        x += '0'
        bnr = x[::-1]
    return bnr

def zakodujSlowa(slowaMatr, H):
    iloscBitowParzystosci = len(H[0]) - 8
    print("iloscBitowParzystosci: %d" %iloscBitowParzystosci)
    slowaZakodowaneMatrix = copy.deepcopy(slowaMatr)
    counter = 0
    for s in slowaZakodowaneMatrix:
        bityParzystosci = [0] * iloscBitowParzystosci # inicjacja listy zerami
        for i in range(8):


            for j in range(iloscBitowParzystosci):
                bityParzystosci[j] += s[i] * H[j][i]
                # print(bityParzystosci[j])


            # print("----------")
            # print(bityParzystosci)
        for bp in bityParzystosci:
            s.append(bp % 2)
    return slowaZakodowaneMatrix

def odleglosc(slowo1, slowo2):
    suma = 0
    for i in range(8):
        suma += abs(slowo1[i] - slowo2[i])
    return suma;

def minimalnaOdleglosc(slowa):
    minOdleglosc = 8
    for i in range (256):
        for j in range (256):
            if(i == j):
                continue

            odl = odleglosc(slowa[i], slowa[j])
            if(odl < minOdleglosc):
                minOdleglosc = odl
    return minOdleglosc

def printSlowaZakowodane(slowa):
    counter = 0
    for slowo in slowa:
        print("%3d: [%d, %d, %d, %d, %d, %d, %d, %d,  %d, %d, %d, %d]" % (counter,slowo[0], slowo[1],slowo[2],slowo[3],slowo[4],slowo[5],slowo[6],slowo[7],slowo[8],slowo[9],slowo[10],slowo[11]))
        counter += 1

# 256 kolejnych liczb dziesiatkowo
slowaDec = []
for i in range (256):
    slowaDec.append(i)

# 256 kolejnych liczb binarnie
slowaBin = []
for i in range (256):
    slowaBin.append(decToBin(slowaDec[i]))

#array 256 slow, kazde jest arrayem bitow
slowaMatrix = []
for k in range (256):
    s = []
    for i in range (8):
        s.append(int(slowaBin[k][i]))
    slowaMatrix.append(s)

# H = ([[1, 1, 1, 0, 1, 0, 1, 1,    1, 0, 0],
#       [1, 0, 1, 1, 0, 1, 1, 1,    0, 1, 0],
#       [0, 1, 1, 0, 1, 1, 1, 1,    0, 0, 1]])

H = ([[0, 1, 1, 1, 0, 1, 1, 0,    1, 0, 0, 0],
      [1, 0, 1, 1, 0, 0, 1, 1,    0, 1, 0, 0],
      [1, 1, 0, 1, 1, 0, 0, 1,    0, 0, 1, 0],
      [1, 1, 1, 0, 1, 1, 0, 0,    0, 0, 0, 1]])


slowaZakodowane = zakodujSlowa(slowaMatrix, H)
minOdleglosc = minimalnaOdleglosc(slowaZakodowane)


printSlowaZakowodane(slowaZakodowane)
print("Minimalna odleglosc: %d" % minOdleglosc)
