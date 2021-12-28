while True:
    try:
        edad= int(input("Ingrese edad:"))
        break
    except ValueError:
        print("Error de ingreso, no se ingreso un entero")

