import pymysql

personas=(("Oscar",30),("Ernesto",41),("Osvaldo",27))

conn=pymysql.connect(host="db4free.net",port=3306,user="sofiasa",passwd="Sanchez0503",db="bddsanchez")

cursor=conn.cursor()

idi=1
for nombre,edad in personas:
    cursor.execute("INSERT INTO Personas VALUES (%s,%s,%s)",(idi,nombre,edad))
    idi= idi+1

conn.commit()
conn.close()

print("Datos ingresados correctamente!")