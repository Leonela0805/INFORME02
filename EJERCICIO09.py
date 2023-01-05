#Hallar la matriz simétrica
filasA=int(input('Ingrese número de filas: '))
columnasA=int(input('Ingrese número de columnas: '))
contador = 0

if columnasA == filasA:

    matrizA = []
    for i in range(filasA):
        matrizA. append([0] * columnasA)

    print('Ingrese la matriz A')
    for fila in range(filasA):
        for columna in range(columnasA):
            matrizA[fila][columna] = float(
                input(f'Ingrese la posición número {fila}, {columna}: '))

    # Calculando si una matriz es simétrico o no lo es
    for fila in range(filasA):
        for columna in range(columnasA):
            normal = matrizA[fila][columna]
            transpuesta = matrizA[columna][fila]
            if normal == transpuesta:
                contador += 1


    if contador == (filasA * columnasA):
        print('La matriz es simétrica')
    else:
        print('La matriz NO es simétrica')
