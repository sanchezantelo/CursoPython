notas = [8,9,10]
#agregaalfinaldelalista
notas.append(8)
#insertarenlalista
notas.insert(2,8)
print(notas)

numeros=[6,7,0,100,50,5]
#ordenaelementos
numeros.sort()
print(numeros)
print(numeros[0])
print(numeros[-1])
#borraelemento
del(numeros[3])
print(numeros)
#cantidaddeelementos
print(len(numeros))

#matrices
m=[[4,5],[10,11]]
print(m[0], m[1])
alumnos=[["Jorge", 50],["Oscar",30]]
print("El alumno", alumnos[0][0], "tiene", alumnos[0][1],"años")

nombres=["carlos","oscar","maria","eduardo","ernesto","romina"]
i=0
while i<6:
    print(nombres[i])
    i=i+1

lista=[10,20,30,40,100]
suma=0
i=0
while i<len(lista)-1:
    suma=suma+lista[i]
    i=i+1
print(suma)

for n in lista:
    suma=suma+n
suma= suma - lista[-1]
print(suma) 



