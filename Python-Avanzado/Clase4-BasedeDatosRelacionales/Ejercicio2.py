"""
Realizar un programa que permita agregar nuevos productos a la base de datos anterior a
traves de la consola. Se debera solicitar para cada producto un id(numerico entero), un
nombre(texto) y un precio(numerico entero). En el caso de los datos numericos, volver a preguntar
si el valor ingresado por el usuario es incorrecto.
Una vez insertado el nuevo producto, mostrar en pantalla todos los productos almacenados
en la base de datos.

"""

import sqlite3

def pedir_entero(texto):  
    while True:
        try:
            variable=int(input(texto))
            break
        except ValueError:
            print("Error al ingresar. Ingrese solo numeros enteros")
    return variable 

try:
    conn=sqlite3.connect("local.sqlite")
    cursor=conn.cursor()

except:
    print("No hay conexion")


while True:
   
    print("1- Ingreso de producto")
    print("2- Salir")
    op=input("Ingrese una opcion:")
    
    if op=="1":
        i = pedir_entero("Ingreso del id del producto: ")
        nombre = input("Ingrese nombre del producto: ")
        precio = pedir_entero("Indique el precio del producto")
        cursor.execute("INSERT INTO productos VALUES (?,?,?)",(i,nombre,precio))
        conn.commit()

    if op=="2":
        break

conn.close()

