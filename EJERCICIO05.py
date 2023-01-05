#Suma, resta, multiplicación de matrices.
import numpy as np
f = int(input('Ingrese el número de filas de la matriz: '))
c = int(input('Ingrese el número de columnas de la matriz: '))

def definir_matriz (filas,columnas):
    f = -1
    c = -1
    e_fil=[]
    for i in range (0,filas):
        e_col =[]
        f += 1
        for j in range(0,columnas):
            c += 1
            dato = int(input(f'Ingrese el componenete {i},{j} '))
            e_col.append(dato)
        e_fil.append(e_col)
    return e_fil

A = np.array(definir_matriz(f, c))
B = np.array(definir_matriz(f, c))
suma = A+B
resta = A-B
mult = A*B

print('Suma de mtrices \n', suma)
print('Diferencia de matrices \n', resta)
print('Producto de matrices \n', mult)