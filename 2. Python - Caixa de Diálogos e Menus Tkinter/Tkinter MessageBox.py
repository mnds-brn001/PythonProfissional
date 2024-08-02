import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning, showerror

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Caixas de mensagem')
        self.geometry("300x150+800+400")

        options= {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5 }

        ttk.Button(
            self,
            text="Informação",
            command=lambda: showinfo(title="Informação",
            message="Esta uma mensagem de Informação")
        ).pack(**options)

        ttk.Button(
            self,
            text="Aviso",
            command=lambda: showwarning(title="Aviso",
            message="Esta uma mensagem de aviso")
        ).pack(**options)

        ttk.Button(
            self,
            text="Erro",
            command=lambda: showerror(title="Erro",
            message="Esta uma mensagem de Erro")
        ).pack(**options)




if __name__ == "__main__":
    app= App()
    app.mainloop()








"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning, showerror

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Caixas de mensagem')
        self.geometry("300x150+800+400")

if __name__ == "__main__":
    app= App()
    app.mainloop()


        

"""
