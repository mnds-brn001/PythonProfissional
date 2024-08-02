import tkinter as tk
from tkinter import ttk

def log(event):
    print(event)
    print(f"keysym...: {event.keysym}")
    print(f"keycode...: {event.keycode}")
    print(f"keysym_num...: {event.keysym_num}")
    print(f"char...: {event.char}")

root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

btn1= ttk.Button(root, text="Executar")
btn1.bind("<Return>", log)
btn1.bind("<Control-KeyPress-x>", log)
btn1.focus()
btn1.pack(expand=True)

root.mainloop()


# <modificador-tipo-detalhe>
# <KeyPress-A>
# <Alt-Control-KeyPress-KP_Delete>
# <Control-KeyPress-x>