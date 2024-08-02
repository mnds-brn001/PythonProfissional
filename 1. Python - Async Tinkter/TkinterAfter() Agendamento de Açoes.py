import tkinter as tk
from tkinter import ttk
import time

# App adiciona um botão que muda a cor no clique e volta ao normal após N segundos.

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title( 'Tkinter "after()" Demo')
        self.geometry('300x100')

        self.style= ttk.Style(self)
        self.style.configure("TButton", font=("Gill-Sans-MT", 16, "bold"))

        self.button= ttk.Button(self, text="Espere 3 segundos")
        self.button["command"]= self.start
        self.button.pack(expand=True, ipadx=10, ipady=5)

    def start(self):
        self.change_button_collor("red")
        # time.sleep(3)
        # self.change_button_collor("black")
        self.after(3000, self.change_button_collor, "black")

    def change_button_collor(self, color):
        self.style.configure("TButton", foreground=color)



if __name__ == "__main__":
    app= App()
    app.mainloop()