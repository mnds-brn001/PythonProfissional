import tkinter as tk
from tkinter import ttk

root= tk.Tk()
root.title("Python Tkinter")

frame1 = ttk.Frame(
    root,
    width=600,
    height=400,
    borderwidth=5,
    relief="solid",
    padding=(10,50,10,50) # Valores referentes a: left, top, right, bottom
    )
frame1.pack()

label1 = ttk.Label(
    frame1,
    text="Label dentro do frame",
    background="yellow"
)
label1.pack()

label2= ttk.Label(
    frame1,
    text="Outor Label dentro do frame",
    background="green"
)
label2.pack()


root.mainloop()