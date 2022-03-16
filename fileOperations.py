content = open('input.txt', 'r').read()

def textToBinary(content):
    byteArray = bytearray(content, "utf8")
    byteList = []
    for byte in byteArray:
        singleByte = bin(byte)
        byteList.append(singleByte)
    return byteList

print(textToBinary(content))