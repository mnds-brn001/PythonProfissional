import mysql.connector


# Objeto de conexão
mydb = mysql.connector.connect(
    host = "localhost",
    user = "bruno",
    password= "adm123",
    database="meu_banco_dados"
)

mycursor = mydb.cursor()
#sql = "SELECT * FROM pessoas WHERE sobrenome = 'Mendes'"
#sql= "SELECT * FROM pessoas WHERE id = '4'"
#sql= "SELECT * FROM pessoas WHERE idade >= '30'"
#sql= "SELECT * FROM pessoas WHERE sobrenome LIKE '%des%'"
sql = "SELECT * FROM pessoas WHERE sobrenome = %s"
sobrenome = ("Mendes",)

mycursor.execute(sql, sobrenome)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

    