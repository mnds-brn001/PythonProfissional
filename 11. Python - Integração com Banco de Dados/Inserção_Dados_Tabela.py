import mysql.connector


# Objeto de conexão
mydb = mysql.connector.connect(
    host = "localhost",
    user = "bruno",
    password= "adm123",
    database="meu_banco_dados"
)

mycursor = mydb.cursor()

#sql= "INSERT INTO pessoas (id, nome, sobrenome, idade) VALUES (NULL, 'Bruno', 'Mendes', 23)" #Está em NULL pois o valor da PK é inserido automaticamente

sql = "INSERT INTO pessoas (id, nome, sobrenome, idade) VALUES ( NULL, %s, %s, %s)"

val = [("Luiz", "Purificacao", "79"),
       ("Katia", "Purificacao", "67"),
       ("Steve", "Jobs", "52"),
       ("Robert", "Shikamura", "49")
       ]

#val = ("Danny", "Logan", "35")
#mycursor.execute(sql,val)

mycursor.executemany(sql,val)
mydb.commit()

print(mycursor.rowcount,"Registros Inseridos")
print(mycursor.lastrowid)