import mysql.connector


# Objeto de conexão
mydb = mysql.connector.connect(
    host = "localhost",
    user = "bruno",
    password= "adm123",
    database="meu_banco_dados"
)

mycursor = mydb.cursor()

#sql = "SELECT * FROM pessoas LIMIT 5"
sql = "SELECT * FROM pessoas LIMIT 5 OFFSET 2"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

