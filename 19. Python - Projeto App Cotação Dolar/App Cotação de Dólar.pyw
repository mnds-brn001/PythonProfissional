import tkinter as tk
from tkinter import ttk
import matplotlib
import requests
from datetime import datetime as dt

matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("API Cotaçao do Dolar")

        # criar uma figure
        self.figure= Figure(figsize=(15, 6), dpi=100)

        # criar um objeto FigureCanvasTkAgg
        self.figure_canvas= FigureCanvasTkAgg(self.figure, self)

        # Criar a barra de ferramentas
        NavigationToolbar2Tk(self.figure_canvas, self)

        # Criar o gráfico
        self.chart= self.figure.add_subplot()
        
        self.current_value= tk.StringVar(value=10)

        self.cmdExecutar()

        self.figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        self.spinRange= ttk.Spinbox(
            self,
            from_=1,
            to=60,
            textvariable=self.current_value,
            wrap=True,
            font=("Gill-Sans-MT",18)
        )
        self.spinRange.pack(fill='x', expand=True, padx=5, side='left')

        # Botão para atualizar o gráfico
        ttk.Button(
            self,
            text="Mostrar",
            command=self.cmdExecutar
        ).pack(fill='x', side='left', expand=True, padx=5)



    def cmdExecutar(self):
        # Obter os dados do gráfico
        # https://economia.awesomeapi.com.br/json/daily/USD-BRL/10

        cotacoes= requests.get(f"https://economia.awesomeapi.com.br/json/daily/USD-BRL/{self.current_value.get()}")
        xData=[]
        yData=[]
        yData2=[]
        yData3=[]
        yData4=[]
        
        for x in cotacoes.json():
            ts= int(x["timestamp"])
            xEixo= dt.utcfromtimestamp(ts).strftime('%d/%m\n%Y')
            xData.insert(0, xEixo)
            yData.insert(0, float(x['bid'])) # Compra
            yData2.insert(0, float(x['ask'])) # Venda
            yData3.insert(0, float(x['low'])) # Baixa
            yData4.insert(0, float(x['high'])) # Alta

        self.chart.clear()

        self.chart.plot(xData, yData, marker= 'o', label='compra')
        self.chart.plot(xData, yData2, marker= 'o', label='venda')
        self.chart.plot(xData, yData3, marker= 'o', label='minimo')
        self.chart.plot(xData, yData4, marker= 'o', label='maximo')
        
        self.chart.set_title(cotacoes.json()[0]["name"])
        self.chart.set_xlabel('Datas')
        self.chart.set_ylabel('BRL')
        self.chart.grid()
        self.chart.legend()

        self.figure_canvas.draw()

if __name__== "__main__":
    app = App()
    app.mainloop()

