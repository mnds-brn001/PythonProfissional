import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Gerenciador de Geometria")
root.geometry("400x200+650+300")

# Exemplo de Grid
# Coluna: |    Linhas: --  Células: (x,x)
# (0,0) (1,0) (2,0)

# (0,1) (1,1) (2,1)

# (0,2) (1,2) (2,2)

# (0,3) (1,3) (2,3)


root.columnconfigure(index=0, weight=2)
root.rowconfigure(index=0, weight=1)

root.mainloop()