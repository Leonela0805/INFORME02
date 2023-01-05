#Calcular la diagonal principal de una matriz

filas=int(input('Ingrese número de filas: '))
columnas=int(input('Ingrese número de columnas: '))

diagonal = 0

if filas == columnas:
    matrizA = []
    for i in range(filas):
        matrizA. append([0] * columnas)

    # Rellenando la matriz
    print('Ingrese la matriz A')
    for f in range(filas):
        for c in range(columnas):
            matrizA[f][c] = float(
                input(f'Ingrese la posición número {f}, {c}: '))

    # Calculando la diagonal principal de la matriz A
    for f in range (filas):
        for c in range(columnas):
            if f == c:
                diagonal += matrizA[f][c]
    
    print(f'El valor de la diagonal principal es: {diagonal}')