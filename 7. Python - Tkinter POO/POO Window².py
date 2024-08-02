import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Root window config
        self.title("Minha aplicação POO")
        self.geometry("300x50+750+400")

        # LABEL
        self.label = ttk.Label(
            self,
            text="Ola, Tkinter!"
        )
        self.label.pack()

        # BUTTON
        self.btn = ttk.Button(
            self,
            text="Click me!"
        )
        self.btn["command"] = self.button_clicked
        self.btn.pack()

    def button_clicked(self):
           showinfo(
           title="Informação",
           message="Ola, Tkinter!"
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()