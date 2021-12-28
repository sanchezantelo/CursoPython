"""
Utilizando un bucle "while" elaborar un codigo que imprima en pantalla cada uno
de los elementos de una lista y simultaneamente los elimine hasta quedar vacia

"""

lista=[10,20,30,50]

i=0
suma= 0
print(lista)

while len(lista) !=0 :
    print(lista[0])
    del(lista[0])

print(lista)


