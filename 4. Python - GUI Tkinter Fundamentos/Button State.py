import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")


btn1 = ttk.Button(
    root,
    text="Sair",
    command=lambda: root.quit()
)
btn1.pack()

btn2 = ttk.Button(
    root,
    text="Desabilitar",
    command=lambda: btn1.state(["disabled"])
)
btn2.pack()

btn3 = ttk.Button(
    root,
    text="Habilitar",
    command=lambda: btn1.state(["!disabled"])
)
btn3.pack()

root.mainloop()