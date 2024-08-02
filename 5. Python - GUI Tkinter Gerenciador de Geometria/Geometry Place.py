import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Gerenciador de Geometria")
root.geometry("600x400+700+300")

# widget.place(**options)
# label1
label1 = ttk.Label(
    root,
    text="Posição Absoluta",
    background="red",
    foreground="white",
    font="Gill-Sans-MT 24"
)
label1.place(x=20, y=20)

label2 = ttk.Label(
    root,
    text="Posição Relativa",
    background="blue",
    foreground="white",
    font="Gill-Sans-MT 24"
)
label2.place(relx=0.8, rely=0.5, anchor= tk.NE, relwidth=0.5) # relx , rely | relwidth : Posição Relativa



root.mainloop()