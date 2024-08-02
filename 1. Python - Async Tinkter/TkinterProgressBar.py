from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
from random import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x150+750+400")
        self.tarefas= randint(1, 10)
        print(self.tarefas)

        # progressbar
        self.pb= ttk.Progressbar(
            self,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        self.pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

        # label
        self.value_label= ttk.Label(self, text="")
        self.value_label.grid(column=0, row=1, columnspan=2)

        # start button
        start_button= ttk.Button(self,text='Iniciar', command=self.progress)
        start_button.grid(column=0, row=2, padx=10, pady=10, sticky= tk.E)

        # Stop Button
        stop_button= ttk.Button(self,text='Parar', command=self.stop)
        stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)


    def update_progress_label(self):
        return  f'Progresso Atual: {round(self.pb["value"], None)}%' # Substitute None to a Number variable if you want more decimal lenght

    def progress(self):
        if self.pb['value'] < 100:
            self.pb['value'] += (100 / self.tarefas)
            self.value_label['text']= self.update_progress_label()

            self.after(randint(100,3000)) # Simulated Task

            # tarefa
            self.id=self.after_idle(self.progress)
            print(self.id)
        else:
            self.pb['value'] = 100
            self.value_label['text']= self.update_progress_label()
            showinfo(message='O processo esta concluído!')

    def stop(self):
        self.pb.stop()
        self.value_label['text'] = self.update_progress_label()
        self.after_cancel(self.id)

if __name__ == "__main__":
    app= App()
    app.mainloop()