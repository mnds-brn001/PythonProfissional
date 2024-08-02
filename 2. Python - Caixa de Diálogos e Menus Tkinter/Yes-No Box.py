import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Caixas de mensagem')
        self.geometry("300x150+800+400")

        ttk.Button(
            self,
            text="Sair",
            command=self.confirm
        ).pack(expand=True)

    def confirm(self):
        result = askyesno(title="Confirmação", message="Realmente quer sair?")
        if result:
            self.destroy()

if __name__ == "__main__":
    app= App()
    app.mainloop()

