#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro


Instalar:
=========
$ pip install mysql-connector-python
"""
import mysql.connector

# Conectar ao MySQL:
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="DB_projetoSQL"
)


# Executar uma consulta:
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM minha_tabela")

resultado = mycursor.fetchall()
print(resultado)