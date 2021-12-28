"""
Crear un bucle que almacene en una variable la suma de todos los elementos numericos
de una lista, a excepcion del ultimo

"""

lista=[10,20,30,50]

i=0
suma= 0

while i< len(lista)-1:
    suma=suma+lista[i]
    i=i+1

print(suma)


