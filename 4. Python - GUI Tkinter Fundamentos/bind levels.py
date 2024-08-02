import tkinter as tk
from tkinter import ttk

def log(event):
    print(event)


root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

root.bind_class("Button","<Any-KeyPress>", log)

btn1= tk.Button(root, text= "Executar 1")
btn1.focus()
btn1.pack()

btn2= tk.Button(root, text= "Executar 2")
btn2.pack()

btn3= tk.Button(root, text= "Executar 3")
btn3.pack()

root.mainloop()