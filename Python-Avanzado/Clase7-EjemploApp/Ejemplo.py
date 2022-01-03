import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.config(width=300,height=220)
ventana.title("App")

lista_desplegable= ttk.Combobox(values=["Visual Basic","Python","C","C++","Java"])
lista_desplegable.place(x=10, y=10)

ventana.mainloop()

