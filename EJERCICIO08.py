#Hallar la matriz transpuesta

filasA=int(input('Ingrese número de filas: '))
columnasA=int(input('Ingrese número de columnas: '))

matrizA = []
for i in range(filasA):
    matrizA.append([0] * columnasA)

print('Ingrese la matriz A')
for fila in range (filasA):
    for columna in range(columnasA):
        matrizA[fila][columna] = float(
            input(f'Ingrese la posición número {fila}, {columna}: '))

print('\n Matriz Inicial\n')
for i in matrizA:
    print(i)

filasB = columnasA
columnasB = filasA

matrizB = []
for i in range(filasB):
    matrizB.append([0] * columnasB)

for fila in range(filasB):
    for columna in range(columnasB):
        matrizB[fila][columna] = matrizA[columna][fila]

print('\n Matriz Transpuesta\n')
for i in matrizB:
    print(i)