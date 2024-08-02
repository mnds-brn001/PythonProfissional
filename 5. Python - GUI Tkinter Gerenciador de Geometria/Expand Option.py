import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Gerenciador de Geometria")
root.geometry("400x200+650+300")

# Box 1
box1= tk.Label(
    root,
    text="Box 1",
    bg="green",
    fg="white"
)
box1.pack(
    ipadx=10,
    ipady=10,
    fill="both",  # x , y, both
    expand= True
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
    expand= True
)

root.mainloop()