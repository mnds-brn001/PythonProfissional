import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Login")
root.geometry("240x100+750+400")

# Configuração GRID 
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Username
username_label = ttk.Label(root, text="Nome de Usuário:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky= tk.E, padx=5, pady=5)

# Password
password_label = ttk.Label(root, text="Senha:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = ttk.Entry(root, show="*")
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# Login Button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky= tk.E, padx=5, pady=5)




root.mainloop()