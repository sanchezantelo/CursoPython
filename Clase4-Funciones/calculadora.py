def suma(a,b):
    c= a+b
    print("Resultado=",c)

def resta(a,b):
    c= a-b
    print("Resultado=",c)

def multiplicacion(a,b):
    c= a*b
    print("Resultado=",c)

def division(a,b):
    if(b == 0):
        print("No se puede dividir por cero")
    else:
        c= a/b
        print("Resultado=",c)

while True:
    print("Calculadora: ")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicacion")
    print("4 - Division")
    print("5 - Salir")
    op = input("Ingrese opcion: ")
    op = int(op)
    if op>=5 or op<=0:
        if op ==5:
            break
        print("No existe opcion")
    else:
        x= input("Ingrese primer dato:")
        x=int(x)
        y= input("Ingrese segundo dato:")
        y= int(y)
        if op == 1:
            suma(x,y)
        elif op == 2:
            resta(x,y)
        elif op == 3:
            multiplicacion(x,y)
        elif op == 4:
            division(x,y)
       
