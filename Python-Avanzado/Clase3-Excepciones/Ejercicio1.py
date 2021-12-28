import biblioteca as bib
import os

def pedido():
    nombre = input("Ingrese el nombre del cliente: ")
    ec = input("Ingrese empanadas de carne: ")
    ec = entero(ec)
    ejq= input("Ingrese empanadas de jamon y queso:")
    ejq= entero(ejq)
    eh = input("Ingrese empanadas de humita: ")
    eh = entero(eh)
    ea = input("Ingrese empanadas de atun: ")
    ea = entero(ea)
    empanadas =[nombre, ec, ejq, eh, ea]
    return empanadas

def entero(numero):
    while True:
        try:
            numero= int(numero)
            return numero
        except ValueError:
            print("Error, ingreso no valido")
            numero= input("Ingrese nuevamente: ")

#[0 ,1, 2, 3, 4]
#[nombre, ec, ejq, eh, ea]
def calculo(lista):
    print("El cliente: ", lista[0])
    suma =0 
    i=1
    while i < len(lista):
        suma = suma + lista[i]
        i = i+1
    total = suma * precio
    print("Debe abonar: $", total)
    return total

print("Bienvenido")
empleado= input("Ingrese su nombre: ")
precio = input("Ingrese precio unitario: ")
precio = entero(precio)
while True:
    print("""
    1 - Nuevo pedido
    2 - Salir
    """)
    opcion = input("Ingrese opcion: ")
    if opcion == "1" :
        listap = pedido()
        print(listap)
        importe= calculo(listap)
        input("Presione enter para continuar...")
        os.system("cls")
    if opcion == "2" :
        break
