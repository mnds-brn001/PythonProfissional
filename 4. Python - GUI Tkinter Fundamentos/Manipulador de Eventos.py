import tkinter as tk
from tkinter import ttk

def return_pressed(event):
    print("Tecla Enter pressionada!")

def log(event):
    print(event)

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")
root.config(background="#B4690E")

btn1= ttk.Button(root, text="Executar")
btn1.bind("<Return>", return_pressed) # <Return> = TECLA ENTER
btn1.bind("<Return>", log, add="+")
btn1.focus()
btn1.pack(expand=True)



root.mainloop()





"""
import tkinter as tk
from tkinter import ttk

def return_pressed(event):
    print("Tecla Enter pressionada!")

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

btn1= ttk.Button(root, text="Executar")
btn1.bind("<Return>", return_pressed)
btn1.focus()
btn1.pack(expand=True)

root.mainloop()


"""
