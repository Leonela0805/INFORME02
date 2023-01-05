#Crea dos arrays o arreglos unidimensionales que tengan
# el mismo tamaño (lo pedirá por teclado), en uno de ellos
# almacenarás nombres de personas como cadenas, en el
# otro array o arreglo ira almacenando la longitud de los
# nombres.

n = int(input('Número de datos: '))
nombre = []
longitud = []
for i in range(n):
    dato = input('Nombre: ')
    nombre.append(dato)
    longitud.append(len(dato))
print(nombre)
print(longitud)