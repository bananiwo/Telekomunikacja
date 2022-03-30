import coding as c
import numpy as np
import matrixOperations as mo
import filesOperations as fo


matrixOneError = np.asarray([[1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                             [1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                             [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
                             [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
                             [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0],
                             [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]])

matrixTwoBadBits = np.asarray([[1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                               [1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                               [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                               [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                               [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                               [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                               [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                               [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1]])

if __name__ == '__main__':
    cont = True
    while cont:
        print(
            "Wybierz: \n 1. Zakoduj plik gdy ma 1 bład \n 2. Dekoduj i koryguj plik gdy ma 1 bład \n 3. Zakoduj plik "
            "gdy ma 2 błędy \n 4. Dekoduj i koryguj plik gdy ma 2 błędy \n 5. Wyjdź")
        choice = input()
        if choice == str(1):
            # matrix = mo.createMatrix(6, False)
            inputMessage = input()
            fo.saveStringToFile('input.txt', inputMessage)
            c.encodeFile(matrixTwoBadBits, 'encoded', 'input.txt')
        elif choice == str(2):
            c.decodeToFile(matrixTwoBadBits, 'encoded', 'output.txt', False)
            print(fo.loadStringFromFile('output.txt'))
        elif choice == str(3):
            # matrixTwoBadBits = mo.createMatrix(6, True)
            inputMessage = input()
            fo.saveStringToFile('input.txt', inputMessage)
            c.encodeFile(matrixTwoBadBits, 'encoded', 'input.txt')
        elif choice == str(4):
            c.decodeToFile(matrixTwoBadBits, 'encoded', 'output.txt', True)
            print(fo.loadStringFromFile('output.txt'))
        elif choice == str(5):
            cont = False
        else:
            print("Zły input")
