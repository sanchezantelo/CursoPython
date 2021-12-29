import os

#BuscarArchivo
texto= input("Ingrese documento a buscar: ")

texto= texto.replace(" ","")
texto= texto.lower()

archivos=os.listdir()

for d in archivos:
    d= d.replace(" ","")
    d= d.lower()
    if d == texto:
        print(os.getcwd())
