import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")

        # Label
        ttk.Label(
            self, text="Tela Inicial",
            font=('Gill-Sans-MT', 28, "bold")
        ).pack(expand=True)

        # Button
        ttk.Button(
            self, text="Abrir nova janela",
            command=self.abrirJanela
        ).pack(expand=True)
        
    # Função Criar Nova Janela
    def abrirJanela(self):
        novaJanela= NovaJanela()
        novaJanela.lblTitulo["text"]= "Ola Mundo '-' "
        # NovaJanela()
        # NovaJanela()
        # NovaJanela()
        # NovaJanela()
        # NovaJanela()
        

class NovaJanela(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("Nova Janela")

        self.lblTitulo= ttk.Label(
            self,
            font=("Gill-Sans-MT", 28, "bold"),
            text="Segunda Janela"
        )
        self.lblTitulo.pack(expand=True)
 
        # Criação do Button da Nova Janela
        ttk.Button(
            self, text="Fechar",
            command= self.destroy
        ).pack(expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()



    """
        janela2= tk.Toplevel(self)
        janela2.geometry("400x200")
        janela2.title("Nova Janela")
        
        # Label da nova janela
        janela2Label= ttk.Label(janela2, text="Segunda Janela")
        # Label configuração de geometria
        janela2Label.grid(row=0, column=0)
        
        # Botão de Fechar da nova janela
        janela2Button= ttk.Button(janela2,
                        text="Fechar",
                        command=janela2.destroy)
        # Button configuração de geometria
        janela2Button.grid(row=1, column=0)


    """
    