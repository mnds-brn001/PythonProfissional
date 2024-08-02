import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Caixas de Dialogos')
        self.geometry("550x250+750+350")

        self.text= tk.Text(self, height=12)
        self.text.pack(expand=True)


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
        file = fd.askopenfile(
        title="Abrir arquivo",
        initialdir= "/",
        filetypes= filestypes
        )


#        self.text.insert("1.0", file.readline())
#         self.text.insert("1.0", file.readline())
#         self.text.insert("1.0", file.readline())
        self.text.delete("1.0", "end")
        for line in file.readlines():
            self.text.insert("1.0", line)


if __name__ == "__main__":
    app= App()
    app.mainloop()

