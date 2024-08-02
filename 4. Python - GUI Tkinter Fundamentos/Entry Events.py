import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Entry Widget")
root.geometry("400x200+650+300")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

def btn1_clicked(event=None):
    if texto.get() != "insira seu nome...":
        msg = f"Seja Bem vindo(a) {texto.get()}!"
        showinfo(title ="informação", message=msg)
        texto.set("insira seu nome...")
        textbox.select_range(0, tk.END)
        textbox.focus()

# armazena os valores dos textbox
texto = tk.StringVar()
texto.set("Insira seu nome ...")

textbox = ttk.Entry(
    root,
    textvariable=texto,
    font="Gill-Sans-MT 20 italic"
)
textbox.select_range(0, tk.END)
textbox.focus()
textbox.bind("<Return>", btn1_clicked)
textbox.pack()

btn1 = ttk.Button(
    root,
    text="Executar",
    command= btn1_clicked
)
btn1.pack()

root.mainloop()