import tkinter as tk

root = tk.Tk()

root.title("Minha aplicação GUI")

window_width = 300   # Depois invocada no root.geometry
window_height = 200

#Obter dimensões da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Encontrar o ponto central
center_x= int(screen_width / 2 - window_width /2)
center_y= int(screen_height / 2 - window_height /2)

# Definir a posição da janela no centro da tela

root.geometry("{window_width}x{window_height}+{center_x}+{center_y}") # 600x400+300+100
root.mainloop()