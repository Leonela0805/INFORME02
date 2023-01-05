#Dada las siguientes notas almacenadas en un arreglo:
#[20, 15, 12, 11, 8, 4, 1]
#Elimine la nota más baja programáticamente sin usar la
#función (min) y escriba en pantalla.
#Luego programáticamente calcule el promedio de notas
#descontando la nota eliminada.

A = [20,15,12,11,8,4,1]
for i in range (len(A)):
    if i == 1:
        A.remove(i)

print(A)

suma = 0
for i in A:
    suma += i
print(suma/len(A))