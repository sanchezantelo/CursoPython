import pymysql

conn=pymysql.connect(host="db4free.net",port=3306,user="sofiasa",passwd="SOSAAN22",db="bddsanchez")

cursor=conn.cursor()

cursor.execute("SELECT * FROM Personas")
datos=cursor.fetchall()

conn.commit()

conn.close()

print(datos)
