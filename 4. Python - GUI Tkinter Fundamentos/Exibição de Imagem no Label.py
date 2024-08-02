import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

foto = tk.PhotoImage(file="Imagem/python-moderno-icon.png")

label1 = ttk.Label(
    root,
    image=foto,
    text="Logo Moderno Python",
    font= "Gill-Sans-MT 20",
    compound = "top" # 'top', 'bottom', 'left', 'right', 'none', 'text', 'image'
)
label1.pack()

root.mainloop()