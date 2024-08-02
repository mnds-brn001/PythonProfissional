import mysql.connector


# Objeto de conexão
mydb = mysql.connector.connect(
    host = "localhost",
    user = "bruno",
    password= "adm123",
    database="meu_banco_dados"
)

mycursor = mydb.cursor()

sql = "UPDATE pessoas SET nome = %s WHERE id = %s"

val = ('Bruno', '2')

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "registro(s) afetado(s)")