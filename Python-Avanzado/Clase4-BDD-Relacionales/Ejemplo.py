import sqlite3

conn=sqlite3.connect("basededatos.sqlite")

cursor=conn.cursor()

#crear tabla

#cursor.execute("CREATE TABLE alumnos(nombre TEXT, edad NUMERIC)")

#Cargamos la tabla

#personas= (("Carlos",30),("Jorge",50),("Oscar",42))
#for nombre,edad in personas:
#    cursor.execute("INSERT INTO alumnos VALUES (?,?)",(nombre,edad))

#Leer los datos
cursor.execute("SELECT*FROM alumnos")
datos = cursor.fetchall()

print(datos)

#para comprobar si me trajo una lista
#print(type((datos))

conn.commit()

conn.close()
