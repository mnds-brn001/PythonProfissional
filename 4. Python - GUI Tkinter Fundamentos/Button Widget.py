import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

def executar():
    root.quit()

    
btn1 = ttk.Button(
    root,
    text="Sair",
    command=executar
)
btn1.pack()

btn2 = ttk.Button(
    root,
    text="Sair Lambda",
    command= lambda:root.quit()
)
btn2.pack()


root.mainloop()



"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

root.mainloop()
"""
