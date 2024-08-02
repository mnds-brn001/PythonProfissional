import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Button Widget")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

def download_clicked():
    showinfo(
        title="Informação",
        message="Botão de download clicado!"
    )

btnIcon = tk.PhotoImage(file="Imagem/python-moderno-icon.png")

btn1 = ttk.Button(
    root,
    image=btnIcon,
    command=download_clicked
)
btn1.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()



"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

btn1 = ttk.Button(
    root,
)

root.mainloop()
"""
