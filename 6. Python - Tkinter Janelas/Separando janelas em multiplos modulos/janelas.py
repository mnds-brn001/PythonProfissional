import tkinter as tk
from tkinter import ttk


class NovaJanela(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("Nova Janela")
        
        self.txtLabel= tk.StringVar()

        self.lblTitulo= ttk.Label(
            self,
            font=("Gill-Sans-MT", 28, "bold"),
            textvariable=self.txtLabel
        )
        self.lblTitulo.pack(expand=True)
 
        # Criação do Button da Nova Janela
        ttk.Button(
            self, text="Fechar",
            command= self.destroy
        ).pack(expand=True)