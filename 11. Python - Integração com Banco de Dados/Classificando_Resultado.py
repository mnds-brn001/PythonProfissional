import mysql.connector


# Objeto de conexão
mydb = mysql.connector.connect(
    host = "localhost",
    user = "bruno",
    password= "adm123",
    database="meu_banco_dados"
)

mycursor = mydb.cursor()

#sql = "SELECT * FROM pessoas ORDER BY idade ASC"
#sql = "SELECT * FROM pessoas ORDER BY nome"
#sql = "SELECT * FROM pessoas ORDER BY idade DESC"
sql = "SELECT * FROM pessoas ORDER BY nome DESC"



mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)