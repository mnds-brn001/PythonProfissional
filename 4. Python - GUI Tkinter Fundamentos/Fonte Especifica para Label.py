import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

label1= ttk.Label(
    root,
    text= "Este é um Label",
    font=("Verdana", 36, "bold", "italic") # font = "Gill-Sans-MT 24 bold italic"
)
label1.pack()

root.mainloop()