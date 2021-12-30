"""
Desarrollar un script buscar_archivos.py que reciba
como argumentos la ruta a una carpeta y una extension
para buscar archivos dentro de ella. Luego debe mostrar los
archivos que terminen con dicha extension en la carpeta indicada.
Por ejemplo, en el caso siguiente se listan los archivos con extension
".exe" en la carpeta de instalacion de python:

python buscar_archivos.py "C:\Python.37". exe
Archivos con extension.exe:
python.exe
pythonw.exe

"""

import sys
import os

argumentos = sys.argv
ruta = None
ext= None

try:
    ruta = argumentos[1]
    ext= argumentos[2]
except IndexError:
    print("Error no se pasaron todos los argumentos")
    sys.exit()

archivos = os.listdir(ruta)

#["juego.exe", "documento.pdf","planilla.xlsx"]

for doc in archivos:
    doc = doc.lower()
    if doc.endswith(ext):
        print(doc)



