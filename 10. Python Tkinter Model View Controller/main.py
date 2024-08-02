from tkinter import ttk
import tkinter as tk
import TkinterController, TkinterModel, TkinterView

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC')

        # Criar o Modelo
        model= TkinterModel.Model("teste@email.com")
        # Criar o View e definir o seu container
        view= TkinterView.View(self)
        view.grid(row=0, column=0, padx=10, pady=10)
        # Criar o Controller
        controller= TkinterController.Controller(model, view)
        # Definir o Controlador para o View
        view.set_controller(controller)

if __name__ == '__main__':
    app= App()
    app.mainloop()