import mysql.connector


# Objeto de conexão
mydb = mysql.connector.connect(
    host = "localhost",
    user = "bruno",
    password= "adm123",
    database="meu_banco_dados"
)

mycursor = mydb.cursor()

#sql = "CREATE TABLE pessoas ( id INT AUTO_INCREMENT PRIMARY KEY nome VARCHAR(255), idade INT(2))"

sql = "ALTER TABLE pessoas ADD id INT AUTO_INCREMENT PRIMARY KEY PRIMARY KEY FIRST"

mycursor.execute(sql)