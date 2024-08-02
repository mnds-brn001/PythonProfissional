import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Intro to Entry")
root.geometry("400x200+650+300")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

# armazena os valores dos textbox
texto = tk.StringVar()
texto.set("Insira seu nome ...")

textbox = ttk.Entry(
    root,
    textvariable=texto,
    font="Gill-Sans-MT 20 italic"
)
textbox.select_range(0, tk.END)
textbox.focus()
textbox.pack()

btn1 = ttk.Button(
    root,
    text="Executar",
    command= lambda: print(texto.get())
)
btn1.pack()

root.mainloop()