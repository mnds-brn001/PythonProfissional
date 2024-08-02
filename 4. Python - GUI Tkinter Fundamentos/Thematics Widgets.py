import tkinter as tk
from tkinter import ttk # Dá uma temática mais moderna para o app
root = tk.Tk()

root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")
root.iconbitmap("Imagem/pythonsss.ico")
root.attributes("-topmost", 1)

# Widget Tematico Classico
tk.Label(root, text="LABEL CLASSICO").pack()

# Widget Tematico Moderno
ttk.Label(root, text="LABEL TEMATICO").pack()

# Widget Tematico Classico
tk.Button(root, text="Button CLASSICO").pack()

# Widget Tematico Moderno
ttk.Button(root, text="Button TEMATICO").pack()


root.mainloop()
