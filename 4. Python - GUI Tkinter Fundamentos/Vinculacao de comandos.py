import tkinter as tk
from tkinter import ttk # Dá uma temática mais moderna para o app

def button_clicked():
    root.config(background="grey") # Tbm aceita valores tipo: #0000FF
    print("Button pressed!")

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")
root.iconbitmap("Imagem/pythonsss.ico")
root.attributes("-topmost", 1)

btn = ttk.Button(root, text="Clique em mim!", command = button_clicked)
btn.pack()

root.mainloop()