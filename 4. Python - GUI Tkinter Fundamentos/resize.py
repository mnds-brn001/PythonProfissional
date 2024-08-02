import tkinter as tk
root = tk.Tk()

root.title("Minha aplicação GUI")
root.geometry("600x400+200+100")

#janela.metodo(largura,altura)
root.resizable(True, True) # To Height or Width
# True, False
# False, True
# False, False
root.minsize(300, 420)
root.maxsize(800, 616)

root.mainloop()