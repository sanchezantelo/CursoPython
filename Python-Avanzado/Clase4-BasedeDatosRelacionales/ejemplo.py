import sqlite3

conn=sqlite3.connect("basededatos.sqlite")

cursor=conn.cursor()
#crear tabla
#cursor.execute("CREATE TABLE alumnos(nombre TEXT, edad NUMERIC)")

personas= (("Carlos",30),("Jorge",50),("Oscar",42))

for nombre,edad in personas:
    cursor.execute("INSERT INTO alumnos VALUES (?,?)",(nombre,edad))

conn.commit()

conn.close()
