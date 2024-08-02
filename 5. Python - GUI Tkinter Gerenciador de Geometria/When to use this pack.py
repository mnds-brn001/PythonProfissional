import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Gerenciador de Geometria")
root.geometry("400x200+650+300")

# coloque widgets de cima para baixo
box1= tk.Label(
    root,
    text="Box 1",
    bg="green",
    fg="white"
)
box1.pack(
    ipadx=10,
    ipady=10,
    fill="x",  # x , y, both
)
box2= tk.Label(
    root,
    text="Box 2",
    bg="red",
    fg="white"
)
box2.pack(
    ipadx=10,
    ipady=10,
    fill="x"
)

# Coloque widgets lado a lado

label3 = tk.Label(
        root,
        text="Box 3",
        bg="blue",
        fg="white"
)
label3.pack(
    ipadx=10,
    ipady=10,
    fill="x"
)


label4 = tk.Label(
        root,
        text="Esquerda",
        bg="cyan",
        fg="black"
)
label4.pack(
    ipadx=10,
    ipady=10,
    fill="both",
    expand=True,
    side= tk.LEFT
)

label5 = tk.Label(
    root,
    text="Centro",
    bg="magenta",
    fg="black"
)
label5.pack(
    ipadx=10,
    ipady=10,
    expand=True,
    fill="both",
    side= tk.LEFT
)

label6 = tk.Label(
    root,
    text="Direita",
    bg="yellow",
    fg="black"
)
label6.pack(
    ipadx=10,
    ipady=10,
    expand=True,
    fill="both",
    side= tk.RIGHT
)




root.mainloop()