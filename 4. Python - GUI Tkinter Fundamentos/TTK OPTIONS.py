import tkinter as tk
from tkinter import ttk # Dá uma temática mais moderna para o app
root = tk.Tk()

root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")
root.iconbitmap("Imagem/pythonsss.ico")
root.attributes("-topmost", 1)

ttk.Label(root, text="Hello World!").pack()

# Usando um índice de dicionario após a criação do widget
lbl1 = ttk.Label(root)
lbl1["text"] = "Outro Ola Mundo!"
lbl1.pack()

# Usando o método config() com atributos de palavra-chave
lbl2 = ttk.Label(root)
lbl2.config(text="Mais um Ola Mundo!")
lbl2.pack()

tk.mainloop()