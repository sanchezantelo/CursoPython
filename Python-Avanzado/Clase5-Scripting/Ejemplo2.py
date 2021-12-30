import shutil

#Borrar carpetas con contenido en su interior
#No va a la papelera, lo borra por completo
#Ruta de la carpeta entra las comillas
shutil.rmtree("") 

#Permite poder ejecutar de forma autonoma
import subprocess

subprocess.run(["mkdir", "Nueva carpeta"], shell=True)

subprocess.call("shutdown -s -f -t %d" % seg)



