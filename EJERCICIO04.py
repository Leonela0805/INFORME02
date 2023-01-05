#Diseñe un programa que lea un vector y calcule si hay
#un número que sea igual a la suma de los demás elementos
#del vector.

n = int(input('Ingrese tamaño del vector: '))
V = []
suma = 0
num_sum = -1
for i in range(n):
    numero = int(input('Ingrese un número ')) 
    V.append(numero)
    suma += V[i]

    if V[i] == suma:
        num_sum = suma

if num_sum != -1:
    print('El número ',num_sum,' es la suma de los demás números del vector')
else:
    print('Ningún número cumple con el criterio')