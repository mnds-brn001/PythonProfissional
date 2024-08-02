import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Caixas de mensagem')
        self.geometry("300x150+800+400")

        ttk.Button(
            self,
            text="Abrir um arquivo",
            command= self.select_file
        ).pack(expand=True)

    def select_file(self):
        filetypes=(("Arquivos de texto","*.txt"), ("Todos os arquivos", "*.*"))
        filename = fd.askopenfilename(
        title="Abrir arquivo",
        initialdir= "/",
        filetypes= filetypes
        )

        showinfo("Arquivo Selecionado", message=filename)

if __name__ == "__main__":
    app= App()
    app.mainloop()

