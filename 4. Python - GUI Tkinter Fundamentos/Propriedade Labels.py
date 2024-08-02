import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

label1= ttk.Label(
    root,
    text= "Este é um Label\nCurso Python Tkinter",
    background="#6A6F73",
    foreground= "#B4690E",
    padding = 20,
    width=30,
    justify= tk.LEFT, # CENTER/RIGHT
    anchor=tk.CENTER # N S E W NE NW SE SW CENTER
)
label1.pack()

root.mainloop()