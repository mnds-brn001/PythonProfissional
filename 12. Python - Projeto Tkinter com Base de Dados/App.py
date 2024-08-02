import tkinter as tk
from tkinter import ttk
import re
import mysql.connector

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuração do Resultado
        self.varResultado = tk.StringVar(self)
        self.lblResultado = ttk.Label(
            self,textvariable=self.varResultado,
            font=("Gill-Sans-MT", 18),
            background="#DDDDDD"
        )
        self.lblResultado.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky= "ewns")
        
        
        # Configuração da barra de Input do Nome
        self.lblNome = ttk.Label(
            self, text="Nome",
            font=("Gill-Sans-MT", 18, "bold")
        )
        self.lblNome.grid(row=1, column=0, columnspan=3, padx=20, pady=5, sticky= "w")
        self.varNome = tk.StringVar(self)
        self.txtNome= ttk.Entry(
            self, textvariable=self.varNome,
            font=("Gill-Sans-MT", 18)
        )
        self.txtNome.grid(row=1, column=1, sticky="we", padx=20, pady=5)
        self.txtNome.focus()



        # Configuração da barra de Input do E-mail
        self.lblEmail= ttk.Label(
            self, text="E-mail",
            font=("Gill-Sans-MT", 18, "bold")
        )
        self.lblEmail.grid(row=2, column=0, sticky="w", padx=20 , pady=5)

        self.varEmail= tk.StringVar(self)
        self.txtEmail= ttk.Entry(
            self, textvariable=self.varEmail,
            font=("Gill-Sans-MT", 18)
        )
        self.txtEmail.grid(row=2, column=1, sticky="we", padx=20, pady=5)

        # Configuração do Campo da Lista de Resultados
        self.frameLista= ttk.Frame(self)
        self.frameLista.grid(row=3, column=0, columnspan=2, rowspan=4, sticky="nwes", padx=20, pady=10)

        self.txtLista= ttk.Treeview(
            self.frameLista, columns=('nome','email'),
            show="headings", height=7
        )
        self.txtLista.heading('nome', text='Nome')
        self.txtLista.heading('email',text='Email')

        # Configuração da Seleção de Valores
        def item_selected(event): # Sem o self pois o método não será público para todas as classes // tbm pois ja esta dentro da classe principal
            for selected_item in self.txtLista.selection():
                item = self.txtLista.item(selected_item)
                record= item['values'] # Inicializa a lista
                self.varNome.set(record[0])
                self.varEmail.set(record[1])

        
        self.txtLista.bind('<<TreeviewSelected>>', item_selected)
        # Configuração de geometria da Tabela com a lista de nomes e emails
        self.txtLista.grid(row=0, column=0, sticky='nwes')

        # Configuração do Scrollbar
        scrollbar= ttk.Scrollbar(
            self.frameLista, orient=tk.VERTICAL,
            command=self.txtLista.yview)
        self.txtLista.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
    
        # Configuração dos Botões

        # Botão para Conectar
        self.btnConectar= ttk.Button(
            self, text="Conectar",
            command=self.btnConectar_Click
        )
        self.btnConectar.grid(row=1, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)


        # Botão para Criar Tabela
        self.btnCriarTabela= ttk.Button(
            self,text="Criar Tabela",
            command=self.btnCriarTabela_Click
        )
        self.btnCriarTabela.grid(row=2, column=2, sticky="nwes", padx=20, pady=5,ipadx=20)

        # Botão para Inserir na Tabela
        self.btnInserir= ttk.Button(
            self,text="Inserir",
            command=self.btnInserir_Click
        )
        self.btnInserir.grid(row=3, column=2, sticky="nwes", padx=20, pady=5,ipadx=20)

        # Botão para Procurar na Tabela
        self.btnProcurar= ttk.Button(
            self,text="Procurar",
            command=self.btnProcurar_Click
        )
        self.btnProcurar.grid(row=4, column=2, sticky="nwes", padx=20, pady=5,ipadx=20)

        # Botão para Excluir Registros da Base de Dados
        self.btnExcluir= ttk.Button(
            self,text="Excluir",
            command=self.btnExcluir_Click
        )
        self.btnExcluir.grid(row=5, column=2, sticky="nwes", padx=20, pady=5,ipadx=20)

        # Botão para Editar Registros na base de Dados
        self.btnEditar= ttk.Button(
            self,text="Editar",
            command=self.btnEditar_Click
        )
        self.btnEditar.grid(row=6, column=2, sticky="nwes", padx=20, pady=5,ipadx=20)

    def btnConectar_Click(self):
        try:
            conexao= mysql.connector.connect(
                host="localhost",
                user="",
                password="root"
            )
            mycursor= conexao.cursor()
            sql= "CREATE DATABASE IF NOT EXISTS curso_db"
            mycursor.execute(sql)
            self.varResultado.set("Base de dados criada com sucesos!")
            self.lblResultado.configure(background="#99FF99")
        except:
            self.varResultado.set("Erro ao conectar com a base dados ")
            self.lblResultado.configure(background="#FF9999")

    def btnCriarTabela_Click(self):
        try:
                conexao= mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="curso_db"
            )
                mycursor=conexao.cursor()
                sql="""
                    CREATE TABLE IF NOT EXISTS pessoas(
                    nome VARCHAR(50),
                    email VARCHAR(50),
                    PRIMARY KEY(email))
                """
                mycursor.execute(sql)
                self.varResultado.set("Tabela criada com sucesso ")
                self.lblResultado.configure(background="#99FF99")

        except:
            self.varResultado.set("Erro ao criar a tabela ")
            self.lblResultado.configure(background="#FF9999")

    def btnInserir_Click(self):
        nome= self.varNome.get().strip()
        email= self.varEmail.get().strip()

        reNome= re.fullmatch(r"\b[A-Za-z ]+\b",nome)
        reEmail= re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email)

        if reNome is None:
            self.varResultado.set("O campo nome é obrigatório ")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()
        elif reEmail is None:
            self.varResultado.set("Insira um email válido ")
            self.lblResultado.configure(background="#FF9999")
            self.txtEmail.focus()
        else:
            try:
                conexao= mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root",
                    database="curso_db"
                )
                mycursor= conexao.cursor()
                sql= "INSERT INTO pessoas (nome,email) VALUES (%s, %s)"
                val=(nome,email)
                mycursor.execute(sql,val)
                conexao.commit()

                self.varResultado.set(str(mycursor.rowcount) + " Registro(s) inseridos")
                self.lblResultado.configure(background="#99FF99")
                self.varNome.set("")
                self.varEmail.set("")
                self.txtNome.focus()
                self.btnProcurar_Click()

                # Mostrar os registros na lista


            except:
                self.varResultado.set("Erro ao inserir novo registro.")
                self.lblResultado.configure(background="#FF9999")

    def btnProcurar_Click(self):
        self.txtLista.delete(*self.txtLista.get_children())

        try:
            conexao= mysql.connector.connect(
                host="localhost",
                user="",
                password="root",
                database="curso_db"
            )
            mycursor= conexao.cursor()
            sql= "SELECT * FROM pessoas ORDER BY nome ASC"

            if self.varNome.get() != "":
                sql= "SELECT * FROM pessoas WHERE nome LIKE"
                val= (self.varNome.get(),)
                mycursor.execute(sql,val)
            elif self.varEmail.get() != "":
                sql= "SELECT * FROM pessoas WHERE email LIKE %s"
                val= (self.varEmail.get(),)
                mycursor.execute(sql,val)
            else:
                mycursor.execute(sql)

            myresult= mycursor.fetchall()
            
            for contato in myresult:
                self.txtLista.insert('',tk.END, values=contato)

            self.varResultado.set("")
            self.lblResultado.configure(background="#99FF99")
            self.txtNome.focus()

        except:
            self.varResultado.set("Erro ao buscar registro")
            self.lblResultado.configure(background="#FF9999")

    def btnExcluir_Click(self):
        nome= self.varNome.get().strip()
        email=self.varEmail.get().strip()

        if nome == "" or email == "":
            self.varResultado.set("Selecione um registro para excluir")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()

        else:
            try:
                conexao= mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="curso_db"
            )
                mycursor= conexao.cursor()
                sql= "DELETE FROM pessoas WHERE nome= %s AND email= %s"
                val = (nome, email)
                
                mycursor.execute(sql,val)
                conexao.commit()

                self.varNome.set("")
                self.varEmail.set("")

                self.btnProcurar_Click()
                
                if mycursor.rowcount > 0:
                    self.varResultado.set("Registro excluido com sucesso")
                    self.lblResultado.configure(background="#99FF999")
                    self.txtNome.focus()
                else:
                    self.varResultado.set("Registro não excluido.")
                    self.lblResultado.configure(background="#99FF99")
                    self.txtNome.focus()
            except:
                self.varResultado.set("Erro ao excluir o registro.")
                self.lblResultado.configure(background="#FF9999")
        
    def btnEditar_Click(self):
        nome= self.varNome.get().strip()
        email= self.varEmail.get().strip()

        reNome= re.fullmatch(r"\b[A-Za-z ]+\b", nome)
        reEmail= re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email)

        if len(self.txtLista.selection()) < 1:
            self.varResultado.set("Selecione um registro para editar.")
            self.lblResultado.configure(background= "#FF9999")
            self.txtNome.focus()
            return

        if reNome is None:
            self.varResultado.set("O campo nome é obrigatório")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()
        elif reEmail is None:
            self.varResultado.set("Insira um email válido")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()
        
        else:
            try:
                registro= self.txtLista.selection()[0]
                dadosRegistro= self.txtLista.item(registro)
                nomeRegistro= dadosRegistro["values"][0]  # 0: Nome | 1: Email
                emailRegistro= dadosRegistro["values"][1]

                conexao= mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root",
                    database="curso_db"
                )
                mycursor= conexao.cursor()
                sql= ("UPDATE pessoas SET nome= %s, email= %s WHERE nome= %s AND email %s")
                val= (nome,email, nomeRegistro, emailRegistro)
                mycursor.execute(sql, val)
                conexao.commit()

                self.varNome.set("")
                self.varEmail.set("")

                self.btnProcurar_Click()
                self.varResultado.set("Registro alterado com sucesso")
                self.lblResultado.configure(background="#99FF99")
                self.txtNome.focus()
            except:
                self.varResultado.set("Erro ao editar registro")
                self.lblResultado.configure(background="#FF9999")
if __name__ == "__main__":
    app = App()
    app.mainloop()



#grid(row=0, column=0, sticky="", padx=, pady=)