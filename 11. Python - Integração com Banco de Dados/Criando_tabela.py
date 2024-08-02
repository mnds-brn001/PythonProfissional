import mysql.connector


# Objeto de conexão
mydb = mysql.connector.connect(
    host = "localhost",
    user = "bruno",
    password= "adm123",
    database= "meu_banco_dados"
)

mycursor = mydb.cursor()

sql = """CREATE TABLE pessoas (
                      nome VARCHAR(255),
                      idade INT(2))"""

mycursor.execute(sql)

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)