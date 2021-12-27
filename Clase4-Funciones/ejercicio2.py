"""
Ejercicio 2
Crear una funcion rango(desde, hasta, intervalo) que retorne una lista de numeros, tal 
como la funcion incorporada range(), aunque segun el intervalo especificado. Por ejemplo, el siguiente codigo:
lista= rango(1,10,2)
print(lista)
debe imprimir:
[1,3,5,7,9]
puesto que se genera una lista desde 1 hasta 10 con un intervalo de 2.

"""

def rango(desde,hasta, salto):
    lista= []
    lista.append(desde)
    suma = desde
    while suma < hasta-salto:
        suma = suma + salto
        lista.append(suma)
    print(lista)

rango(20,50,5)
