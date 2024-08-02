import tkinter as tk
from tkinter import ttk # Dá uma temática mais moderna para o app
root = tk.Tk()

root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")
root.iconbitmap("Imagem/pythonsss.ico")
root.attributes("-topmost", 1)

def select(arg):
    root.config(background=arg)

btn1 = ttk.Button(
    root,
    text= "Vermelho",
    command=lambda:select("red")

    )
btn1.pack()

btn2= ttk.Button(
    root,
    text= "Verde",
    command=lambda:select("green")

    )
btn2.pack()

btn3= ttk.Button(
    root,
    text= "Azul",
    command=lambda:select("Blue")

    )
btn3.pack()


root.mainloop()