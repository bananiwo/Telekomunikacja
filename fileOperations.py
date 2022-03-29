def loadStringFromFile(filename):
    file = open(filename, "r")
    return file.read()

def stringToByteArray(text):
    wordCount = len(text)
    output = []
    for i in range(wordCount):
        char = text[i]
        charBin = bin(ord(char)).replace('b', '')
        charBinArr = []
        for j in range(len(charBin)):
            charBinArr.append(int(charBin[j]))

        # jesli bitow jest mniej niz 8 to uzupelnia do 8
        for j in range(8 - len(charBinArr)):
            charBinArr.insert(0, 0)

        output.append(charBinArr)

    return output

def saveStringToFile(filename, text):
    file = open(filename, "w")
    file.write(text)
    file.close()





