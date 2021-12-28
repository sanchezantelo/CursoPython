import tkinter as tk

def suma():
    cajatres.delete(0,tk.END)
    a= cajauno.get()
    b= cajados.get()
    cajauno.delete(0,tk.END)
    cajados.delete(0,tk.END)
    a= float(a)
    b= float(b)
    c=a+b
    cajatres.insert(0,c)

def resta():
    cajatres.delete(0,tk.END)
    a= cajauno.get()
    b= cajados.get()
    cajauno.delete(0,tk.END)
    cajados.delete(0,tk.END)
    a= float(a)
    b= float(b)
    c=a-b
    cajatres.insert(0,c)


def multiplicacion():
    cajatres.delete(0,tk.END)
    a= cajauno.get()
    b= cajados.get()
    cajauno.delete(0,tk.END)
    cajados.delete(0,tk.END)
    a= float(a)
    b= float(b)
    c=a*b
    cajatres.insert(0,c)


def division():
    cajatres.delete(0,tk.END)
    a= cajauno.get()
    b= cajados.get()
    cajauno.delete(0,tk.END)
    cajados.delete(0,tk.END)
    a= float(a)
    b= float(b)
    
    if b == 0:
        c= "Error"
        cajatres.insert(0,c)
    else:
        c=a/b
        cajatres.insert(0,c)

    

#Aplicacion de escritorio
ventana= tk.Tk()
ventana.config(width=400, height=250)
ventana.title("App")

botonsuma = tk.Button(text="suma", command=suma)
botonsuma.place(x= 20, y=80)
botonresta= tk.Button(text="resta", command=resta)
botonresta.place(x= 120, y=80)
botonmultiplicacion = tk.Button(text="mult", command=multiplicacion)
botonmultiplicacion.place(x= 240, y=80)
botondivision = tk.Button(text="div", command=division)
botondivision.place(x= 350, y=80)

cajauno= tk.Entry()
cajauno.place(x=20, y=40)
cajados= tk.Entry()
cajados.place(x=250, y=40)
cajatres=tk.Entry()
cajatres.place(x=125, y=150)
etiquetauno=tk.Label(text="Valor 1")
etiquetauno.place(x=20, y=10)
etiquetados=tk.Label(text="Valor 2")
etiquetados.place(x=250, y=10)
etiquetatres=tk.Label(text="Resultado")
etiquetatres.place(x=125, y=120)
ventana.mainloop()

