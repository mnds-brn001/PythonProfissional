import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

label1= ttk.Label(
    root,
    text= "Label Temático",
    font = "Gill-Sans-MT 24 bold italic",
    borderwidth= 10,
    relief="flat" # groove , ridge, sunken, raised, flat
)
label1.pack()

label2= tk.Label(
    root,
    text= "Label Padrão",
    font = "Gill-Sans-MT 24 bold italic",
    bd= 10, # bd Funciona Apenas para o Label Padrão
    relief="flat"
)
label2.pack()


root.mainloop()