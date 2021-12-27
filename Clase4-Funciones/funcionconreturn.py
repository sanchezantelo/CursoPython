def promedio(lista):
    suma =0
    for n in lista:
        suma = suma + n
    p = suma / len(lista)
    return p

alumnos= [[6,4,10,8], [5,5,7,7], [4,6,8,10]]
curso =[]
for notas in alumnos:
    r= promedio(notas)
    curso.append(r)

print(curso)