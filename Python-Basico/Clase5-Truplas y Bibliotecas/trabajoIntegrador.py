"""
Vamos a migrar las funcionalidades: 
Agregar alumno, ver la cantidad de cursos de un alumno, Y ver la lista completa
a una aplicacion de escritorio.
La información se seguira mostrando en la consola.

"""

import tkinter as tk

alumnos={}

def ver_lista():
    print("Lista de alumnos:")
    #El bucle "for" aplicado sobre un diccionario recorre sus claves
    for nombre in alumnos:
        cursos=alumnos[nombre]
        #Necesito convertir "cursos" a una cadena para poder concatenarlo con otras cadenas
        print(nombre + " - " + str(cursos) + "cursos")

def agregar():
    #obtener el nombre de la cajaa de texto
    nombre_alumno = caja_nombre.get()
    #obtener la cantidad de cursos de la caja de texto y convertirla a un entero
    cursos= int(caja_cursos.get())
    if nombre_alumno == "":
        print("Error: no ha ingresado un nombre valido")
    else:
        #Agregar un nuevo par clave-valor al diccionario "alumnos"
        #La clave es el nombre del alumno y el valor, la cantidad de cursos
        alumnos[nombre_alumno]=cursos
        print("Has ingresado el alumno correctamente")

def ver_cursos():
    #obtener el nombre de la caja de texto
    nombre= caja_nombre.get()
    print("Cursos: " +str(alumnos[nombre]))

ventana = tk.Tk()
ventana.config(width=400, height=300)
ventana.title("Proyecto Integrador")

boton_lista= tk.Button(text="Ver lista de alumnos", command= ver_lista)
boton_lista.place(x=10, y=10)

etiqueta_nombre = tk.Label(text= "Nombre alumno:")
etiqueta_nombre.place(x=10, y=60)

caja_nombre=tk.Entry()
caja_nombre.place(x=110, y=60, width=150, height=20)

etiqueta_cursos= tk.Label(text="Cursos:")
etiqueta_cursos.place(x=10, y=100)

caja_cursos=tk.Entry()
caja_cursos.place(x=110, y=100, width=50, height=20)

boton_agregar = tk.Button(text="Agregar a la lista", command=agregar)
boton_agregar.place(x=10, y=150)

boton_cursos= tk.Button(text="Ver cantidad de cursos", command=ver_cursos)
boton_cursos.place(x=115, y=150)

ventana.mainloop()


