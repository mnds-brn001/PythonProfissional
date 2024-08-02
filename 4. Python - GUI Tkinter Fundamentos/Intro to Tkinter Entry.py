import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Intro to Entry")
root.geometry("600x400+650+300")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

textbox = ttk.Entry(
    root
)
textbox.focus()
textbox.pack()

btn1 = ttk.Button(
    root,
    text="executar",
    command=lambda: print(textbox.get())
)
btn1.pack()

root.mainloop()