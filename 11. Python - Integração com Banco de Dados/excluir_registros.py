import mysql.connector


# Objeto de conexão
mydb = mysql.connector.connect(
    host = "localhost",
    user = "bruno",
    password= "adm123",
    database="meu_banco_dados"
)

mycursor = mydb.cursor()

sql = "DELETE FROM pessoas WHERE id = %s"
val = ('4',)

mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "registro(s) excluído(s)")