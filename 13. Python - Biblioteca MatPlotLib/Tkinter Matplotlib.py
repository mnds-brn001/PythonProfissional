import tkinter as tk
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tkinter Matplotlib')

        # Data Preparation
        data= {
            'Python': 11.27,
            'C': 11.16,
            'Java': 7.46,
            'C++': 15.5,
            'C#': 17.26
        }
            
        languages = data.keys()
        popularity= data.values()

        # Criar uma figura
        figure= Figure(figsize=(6, 4), dpi=100) # Figsize: Lido em polegadas

        # Criar um objeto FigureCanvasTkAgg
        figure_canvas= FigureCanvasTkAgg(figure, self) # Comentar esta linha para esconder a barra de ferramentas

        # Criar a barra de ferramentas
        NavigationToolbar2Tk(figure_canvas, self)

        # Criar os eixos
        axes= figure.add_subplot()

        # Criar o gráfico de barras
        axes.bar(languages, popularity)        
        axes.set_title("Top 5 linguagens de Programação")
        axes.set_ylabel("Popularidade")

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1 )

        tk.Button(
            self,
            text="Sair",
            command=self.destroy
            ).pack()

if __name__ == '__main__':
    app = App()
    app.mainloop()


# plt.title("Top 5 linguagens de Programação")
# plt.ylabel('Popularidade')
# plt.bar(languages, popularity)
#plt.show()
