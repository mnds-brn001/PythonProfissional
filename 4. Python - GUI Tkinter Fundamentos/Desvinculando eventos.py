import tkinter as tk
from tkinter import ttk

def log(event):
    print("Evento disparado... ")


root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

btn1= ttk.Button(root, text="Executar")
btn1.bind("<Any-KeyPress>", log)
btn1.focus()
btn1.pack()

#btn1.unbind("<Any-KeyPress>")

btn2= ttk.Button(root,
                 text="Desvincular evento de executar",
                 command=lambda: btn1.unbind("<Any-KeyPress>"))
btn2.pack()

btn3= ttk.Button(root,
                 text="Vincular evento de executar",
                 command=lambda: btn1.bind("<Any-KeyPress>", log))
btn3.pack()

root.mainloop()