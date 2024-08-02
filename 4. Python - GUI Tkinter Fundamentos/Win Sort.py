import tkinter as tk
root = tk.Tk()
root.title("Minha aplicação GUI")
root.geometry("600x400+500+200")
root.attributes("-alpha", 0.9) # de 0.0  até 1.0
root.state("normal")

# Valor 1 garante que a janela sempre fique sobreposta
#root.attributes("-topmost", 1)

# Para sobrepor ao topo uma janela
#root.lift()
# Para diminuir a janela da pilha
root.lower()


root.mainloop()