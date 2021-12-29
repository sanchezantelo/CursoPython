"""
Desarrollar un programa de python que cree una base de datos de SQLLite llamada productos.db
y una tabla de nombre productos con las siguientes columnas:
Columna:  id / nombre / precio
Tipo de dato: Entero / Texto / Entero

Luego el programa debe insertar las siguientes filas:

id: 1 / 2 / 3 / 4
nombre: Teclado / Mouse / Monitor / Parlantes
precio: 500 / 350 / 1500 / 1100

"""
import sqlite3

try:
    conn=sqlite3.connect("local.sqlite")
    cursor=conn.cursor()

except:
    print("No hay conexion")


#crear tabla

try:
    cursor.execute("CREATE TABLE productos(id NUMERIC, nombre TEXT, precio NUMERIC)")
except:
    print("La tabla existe")

#Cargamos la tabla

mercaderia = (("Teclado",500),("Mouse",350),("Monitor",1500),("Parlantes",1100))

i=1
for nombre,precio in mercaderia:
   cursor.execute("INSERT INTO productos VALUES (?,?,?)",(i,nombre,precio))
   i= i+1

#Leer los datos
#cursor.execute("SELECT*FROM productos")
#datos = cursor.fetchall()

#print(datos)

#para comprobar si me trajo una lista
#print(type((datos))

conn.commit()

conn.close()

