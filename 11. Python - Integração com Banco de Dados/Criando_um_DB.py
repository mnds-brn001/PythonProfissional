import mysql.connector


# Objeto de conexão
mydb = mysql.connector.connect(
    host = "localhost",
    user = "bruno",
    password= "adm123"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE meu_banco_dados")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)