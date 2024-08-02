import tkinter as tk
from tkinter import ttk
# from janelas import NovaJanela
import janelas as jn

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")

        # Label
        ttk.Label(
            self, text="Tela Inicial",
            font=('Gill-Sans-MT', 28, "bold")
        ).pack(fill="x", padx=5, pady=5)

        # Campo para enviar Dados
        self.txtVarDados = tk.StringVar()
        txtDados= ttk.Entry(
            self,
            textvariable=self.txtVarDados,
            font=("Arial", 18)
        )
        txtDados.pack(fill= "x", side="left", expand=True, padx= 5)

        # Button
        ttk.Button(
            self, text="Abrir nova janela",
            command=self.abrirJanela
        ).pack(fill= "x", side="left", expand=True, padx= 5, ipady=5)
        
    # Função Criar Nova Janela
    def abrirJanela(self):
        novaJanela= jn.NovaJanela()
        novaJanela.txtLabel.set(self.txtVarDados.get())
        # NovaJanela()
        # NovaJanela()
        # NovaJanela()
        # NovaJanela()
        # NovaJanela()
        


if __name__ == "__main__":
    app = App()
    app.mainloop()


