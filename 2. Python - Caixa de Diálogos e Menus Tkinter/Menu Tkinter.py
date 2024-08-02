import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning, showerror

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Menus')
        self.geometry("300x150+800+400")

        # Criar menubar
        menubar= tk.Menu(self)
        self.configure(menu=menubar)

        # Criar um menu
        file_menu = tk.Menu(menubar, tearoff=False)

        # Criar um item de menu para o menu criado
        file_menu.add_command(
            label="Sair",
            command=self.destroy
    )
        # Adicionar o menu no menu bar
        menubar.add_cascade(
            label="Arquivo",
            menu=file_menu,
            underline= 0
        )

if __name__ == "__main__":
    app= App()
    app.mainloop()

