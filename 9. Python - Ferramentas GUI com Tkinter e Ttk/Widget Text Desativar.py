from tkinter import Tk, Text, ttk


root=Tk()
root.title("Python Tkinter")

text= Text(
    root,
    height=10,
    width=20,
    font="Gill-Sans-MT 24"
)
text.pack()
text.insert("1.0", "Este é um Widget Text demo")

# text["state"] = "normal"
# text["state"] = "disabled" # Fica visivel apenas para leitura mas não editável
ttk.Button(
    root,
    text="Ativar",
    command=lambda:text.config(state="normal")
).pack()

ttk.Button(
    root,
    text="Desativar",
    command=lambda:text.config(state="disabled")
).pack()

root.mainloop()