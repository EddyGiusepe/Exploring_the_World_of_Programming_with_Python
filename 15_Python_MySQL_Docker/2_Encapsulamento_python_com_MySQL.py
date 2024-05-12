#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Instalar:
=========
$ pip install mysql-connector-python

Executar script:
================
$ python 2_Encapsulamento_python_com_MySQL.py 
"""
import mysql.connector

# Os seguintes parâmetros são para cor:
YELLOW = "\033[0;33m"
GREEN = "\033[0;32m"
WHITE = "\033[0;37m"
RED = "\033[0;31m"
RESET= "\033[m"

class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None

    def conectar(self):
        self.conexao = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )

    def executar_consulta(self, query):
        if not self.conexao:
            self.conectar()
        cursor = self.conexao.cursor()
        cursor.execute(query)

        resultado = cursor.fetchall()
        return resultado



if __name__ == "__main__":
    connectionMySQL = MySQLDatabase(host='localhost',
                                    user='root',
                                    password='123456',
                                    database='DB_projetoSQL'
                                   )
    
    #meu_resultado = connectionMySQL.executar_consulta("SELECT * FROM minha_tabela")
    #meu_resultado = connectionMySQL.executar_consulta("SELECT * FROM my_dataframe")
    meu_resultado = connectionMySQL.executar_consulta(
        """
        SELECT MIN(index_price) AS minimo, MAX(index_price) AS maximo
        FROM my_dataframe;
        """
    )
    print(f"{YELLOW}{meu_resultado}{RESET}")
    print("")
    print(f"{RED}{meu_resultado[0][1]}{RESET}")
    