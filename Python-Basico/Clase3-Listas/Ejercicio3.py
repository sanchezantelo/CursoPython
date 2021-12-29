alumnos=[]

while True:
    print("Menu:")
    print("1- Ingreso de alumno")
    print("2- Mostrar alumnos")
    print("3- Salir")
    op = input("Ingrese opcion: ")
    op= int(op)
    if op== 1:
        nombre= input("Ingrese nombre: ")
        cursos= input("Ingrese cursos: ")
        cursos= int(cursos)
        alumnos.append([nombre,cursos])
    elif op== 2:
        for aux in alumnos:
            print("El alumno:",aux[0],"Tiene asignado:",aux[1],"Cursos")
    elif op== 3:
        break
    else:
        print("Opcion no valida")
