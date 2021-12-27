m=[[1,2,3],[4,5,6],[7,8,9]]

for n in m:
    print(n)

#Ejercicio2

filas = input("Ingrese numero de filas: ")
col= input("Ingrese numero de col: ")
filas= int(filas)
col= int(col)

m=[]

for fila in range(filas):
 m.append([])
for columna in range(col):
    print("Fila", fila,"Col", columna )
    dato= input()   
    dato= int(dato)
    m[fila].append(dato)

for n in m:
    print(n)