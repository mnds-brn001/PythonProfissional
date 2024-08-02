import tkinter as tk
root = tk.Tk()

root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")
root.iconbitmap("Imagem/pythonsss.ico")

root.mainloop()
