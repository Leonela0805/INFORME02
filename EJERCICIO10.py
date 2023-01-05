#Calcular la determinante de una matriz

import numpy as np

filasA=int(input('Ingrese número de filas: '))
columnasA=int(input('Ingrese número de columnas: '))

# Creando la matriz vacía
matrizA = []
for i in range(filasA):
    matrizA. append([0] * columnasA)

# Rellenando la matriz
print('Ingrese la matriz A')
for fila in range(filasA):
    for columna in range(columnasA):
        matrizA[fila][columna] = float(
            input(f'Ingrese la posición número {fila}, {columna}: '))

determinante = np. linalg. det(matrizA)
print(determinante)