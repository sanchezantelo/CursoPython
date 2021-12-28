def entero(numero):
    while True:
        try:
            numero= int(numero)
            return numero
        except ValueError:
            print("Error, ingreso no valido")
            numero= input("ingrese nuevamente: ")

edad= input("Ingrese su edad: ")
edad= entero(edad)
print(edad)
vs = input("Cuantas veces va al super por semana? : ")
vs = entero(vs)
print(vs)