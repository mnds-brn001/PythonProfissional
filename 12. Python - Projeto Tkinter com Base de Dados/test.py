import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import StringVar

class MyApp:
    def __init__(self, master):
        self.master = master
        self.varResultado = StringVar()
        self.lblResultado = tk.Label(master, textvariable=self.varResultado)
        self.lblResultado.pack()
        self.btnConectar = tk.Button(master, text="Conectar", command=self.btnConectar_Click)
        self.btnConectar.pack()
        
    def btnConectar_Click(self):
        try:
            conexao = mysql.connector.connect(
                host="localhost:3307",
                user="root",
                password="root"  # Senha vazia
            )
            if conexao.is_connected():
                mycursor = conexao.cursor()
                sql = "CREATE DATABASE IF NOT EXISTS curso_db"
                mycursor.execute(sql)
                self.varResultado.set("Base de dados criada com sucesso!")
                self.lblResultado.configure(background="#99FF99")
        except Error as e:
            self.varResultado.set(f"Erro ao conectar com a base de dados: {e}")
            self.lblResultado.configure(background="#FF9999")

root = tk.Tk()
app = MyApp(root)
root.mainloop()


# 2003: Can't connect to MySQL server on 'localhost3037:3306'(11001 getaddrinfo failed)
# Failed to Connecto to MySQL at localhost:3305 with user root Unable to connect to localhost