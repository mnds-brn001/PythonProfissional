import tkinter as tk
from tkinter import ttk
import time

class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Digital Clock')
        self.resizable(0, 0)
        self.geometry("500x160+750+400")
        self['bg'] = 'black'

        self.style= ttk.Style(self)
        self.style.configure(
            "TLabel",
            background='black',
            foreground='red'
        )
        # Label
        self.label= ttk.Label(
            self,
            text=self.time_string(),
            font=("Digital-7", 80)
        )
        self.label.pack(expand=True)

        self.label.after(1000, self.update)

    def time_string(self):
        return time.strftime("%H:%M:%S") # HORA : MIN : SEG

    def update(self):
        self.label.config(text=self.time_string())
        self.label.after(1000, self.update)

if __name__ == "__main__":
    clock= DigitalClock()
    clock.mainloop()