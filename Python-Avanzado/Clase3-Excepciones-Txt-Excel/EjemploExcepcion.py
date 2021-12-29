try:
    edad:int(input("Ingrese su edad:"))
    print(edad)
except ValueError:
    print("Error")

#########################################

try:
    r= 8/0
except ValueError:
    print("Error")
except ZeroDivisionError:
    print("No se puede dividir por cero")

#########################################

#diccionario
d={"messi":10, "palermo":9}
try:
    print(d["riquelme"])
except ValueError():
    print("Error")
except ZeroDivisionError():
    print("No se puede dividir por cero")
except TypeError:
    print("Error no se puede convertir a este tipo")
except IndexError():
    print("Fuera de rango")
except KeyError:
    print("Elemento no existe")

