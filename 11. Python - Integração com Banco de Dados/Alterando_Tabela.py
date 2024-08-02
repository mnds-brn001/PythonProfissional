import mysql.connector


# Objeto de conexão
mydb = mysql.connector.connect(
    host = "localhost",
    user = "bruno",
    password= "adm123",
    database="meu_banco_dados"
)

mycursor = mydb.cursor()

#sql = """ALTER TABLE pessoas ADD sobrenome VARCHAR(255)"""
#sql= "ALTER TABLE pessoas DROP sobrenome"
sql = "ALTER TABLE pessoas ADD sobrenome VARCHAR(255) AFTER nome"

mycursor.execute(sql)