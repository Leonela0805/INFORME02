#Multiplicación de matrices.

def mult_matrices ():
    print('Ingrese el orden de la matriz A')
    fA, cA = int(input()), int(input()) # 2 x 3

    print('Ingrese el orden de la matriz B')
    fB, cB = int(input()), int(input()) # 3 x 2 

    if cA == fB:
        A = []
        for i in range(fA):
            A.append([0] * cA)

        B = []
        for i in range (fB):
            B.append([0] * cB)

        print('Ingrese la matriz A ')
        for filas in range (fA): 
            for columnas in range(cA): 
                A[filas][columnas] = float(
                    input(f'Ingresa la posición número {filas},{columnas} se la matriz A '))

        print('Ingrese la matriz B ')
        for filas in range(fB):
            for columnas in range(cB):
                B[filas][columnas] = float(
                    input(f'Ingresa la posición número {filas},{columnas} se la matriz B '))
        
        matrizC = []
        for i in range(fA):
            matrizC. append([0] * cB)
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    matrizC[i][j] += A[i][k] * B[k][j ]

        print('\nLa matriz resultante es: ')
        for i in matrizC:
            print(i)
mult_matrices()