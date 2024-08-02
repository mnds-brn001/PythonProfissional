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
            text="Abrir até varios arquivos",
            command= self.select_file
        ).pack(expand=True)

    def select_file(self):
        filestypes=(
            ("Arquivos de texto","*.txt"),
            ("Arquivos de PDF", "*.pdf*"),
            ("Todos os arquivos", "*.*")
            )
        filenames = fd.askopenfilenames(
        title="Abrir arquivo",
        initialdir= "/",
        filetypes= filestypes
        )

        for file in filenames:
            print(file)

        showinfo("Arquivo Selecionado", message=filenames)

if __name__ == "__main__":
    app= App()
    app.mainloop()

