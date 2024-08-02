import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

label1= ttk.Label(
    root,
    text= "0123456789",
    font = "Gill-Sans-MT 24 bold italic",
    borderwidth=1,
    relief="solid",
    #width=5, # Alinhamento do ttk é na ESQUERDA
    # O Módulo temático não reconhece o height=
    wraplength=100 
)
label1.pack()

label2= tk.Label(
    root,
    text= "0123456789\n0123456789\n0123456789",
    font = "Gill-Sans-MT 24 bold italic",
    borderwidth=1,
    relief="solid",
    width=5,  # Alinhamento do tk é no CENTRO
    height=2 # Width e height aqui se refere A LINHA

)
label2.pack()

root.mainloop()






"""import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

label1= ttk.Label(
    root,
    text= "0123456789",
    font = "Gill-Sans-MT 24 bold italic",
    borderwidth=1,
    relief="solid"
)
label1.pack()

root.mainloop()

"""
